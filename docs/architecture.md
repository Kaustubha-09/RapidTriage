# Architecture

RapidTriage is a two-tier system. A React Native (Expo) mobile client captures symptoms via voice or text, sends them to a Go HTTP server, and renders the triage decision back. The Go server orchestrates LLM-driven symptom parsing, rule-based urgency classification, and tool invocations (hospital lookup, ambulance dispatch, booking) through a single Coordinator.

## System diagram

```
┌────────────────────────────────────────────────────────────────────┐
│                     React Native + Expo (mobile)                   │
│  HomeScreen · AssessmentScreen · EmergencyScreen ·                 │
│  EmergencyResultsScreen · HospitalFinderScreen                     │
│  services/ChatService · AudioService · LocationService             │
└────────────────────────────────────────────────────────────────────┘
                            │ HTTPS · multipart for audio
                            ▼
┌────────────────────────────────────────────────────────────────────┐
│                  Go HTTP server (port 8080)                        │
│  internal/api/EmergencyHandler                                     │
│   ├─ POST /api/v1/emergency        (audio → AudioProcessor)        │
│   ├─ POST /api/v1/emergency/text   (text  → TextProcessor)         │
│   └─ GET  /api/v1/health                                           │
└────────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────────────────┐
│                EmergencyCoordinator (api package)                  │
│  Owns: classifier · toolRegistry · locationTool · summaryGenerator │
│  Notification config: SMS / email / push (retry, interval)         │
│  MaxConcurrentTools (default 5)                                    │
└────────────────────────────────────────────────────────────────────┘
       │                       │                          │
       ▼                       ▼                          ▼
┌────────────────┐   ┌──────────────────────┐   ┌──────────────────────┐
│ AI providers   │   │ Tool registry        │   │ RuleBasedClassifier  │
│ (internal/ai)  │   │ (internal/tools)     │   │ (internal/triage)    │
│  - Gemini      │   │  - LocationTool      │   │  Threshold + fallback│
│  - Claude      │   │  - HospitalTool      │   │  TriageCode output:  │
│  - OpenAI GPT  │   │  - AmbulanceTool     │   │   IMMEDIATE / VERY   │
│  - Llama       │   │  - BookingTool       │   │   URGENT / URGENT /  │
│                │   │  (all mock-backed    │   │   NON-URGENT         │
│  ModelType     │   │   for the demo)      │   │  Confidence ∈ [0,1]  │
│  pluggable     │   └──────────────────────┘   └──────────────────────┘
└────────────────┘
```

## The request loop

```
1. User opens AssessmentScreen, taps mic or types symptoms
2. ChatService.assess(...) builds the request
   - text  → POST /api/v1/emergency/text  (JSON body)
   - audio → POST /api/v1/emergency       (multipart form, ≤ 20 MB)
3. EmergencyHandler dispatches to {Audio,Text}Processor
   - {Audio,Text}Processor builds the AI request from config
   - calls the configured ModelType (Gemini default)
   - returns a structured EmergencySituation
4. Coordinator
   - submits situation to RuleBasedClassifier.Classify(ctx, situation)
     → (TriageCode, confidence, error)
   - if confidence < threshold (0.5), apply FallbackCode (YELLOW)
   - decides which tools to invoke (hospital pager on RED, etc.)
   - invokes tools concurrently (MaxConcurrentTools = 5)
   - sends notifications per NotificationConfig (SMS, email, push)
5. Response shape: { triage_code, confidence, summary, recommended_tools,
                     hospital_alerts, emergency_id, timestamp }
6. EmergencyResultsScreen renders priority badge + summary + actions
```

## Why a Go backend

- **Native concurrency.** `MaxConcurrentTools` defaults to 5 — concurrent tool invocation (location lookup, hospital paging, booking) is a goroutine + WaitGroup, not a callback chain.
- **Graceful shutdown.** `main.go` wires `signal.NotifyContext` against `SIGINT` / `SIGTERM` and runs `server.Shutdown(ctx)` with a 10-second deadline so in-flight emergencies don't get cut off.
- **Single-binary deploy.** No Python venv, no Node `node_modules` on the server. `go build` produces one executable.
- **Strict timeouts at every layer.** ReadTimeout / WriteTimeout / IdleTimeout on the HTTP server; per-AI-call timeout from `AI_MODEL_TIMEOUT_SECONDS`; tool retry intervals on `NotificationConfig`. Every external dependency has a bounded wait.

## Multi-provider AI dispatch

`internal/ai` defines a `ModelType` enum (`Gemini`, `Claude`, `GPT4`, `Llama`) and one `Provider` interface. Each provider has model-specific endpoint / API-key env-var fallbacks:

| `AI_MODEL_TYPE` env | Endpoint env (with default) | API key env | Default model |
|---|---|---|---|
| `gemini` | `GEMINI_ENDPOINT` (`https://generativelanguage.googleapis.com/v1`) | `GEMINI_API_KEY` | `gemini-1.5-pro` |
| `claude` | `CLAUDE_ENDPOINT` (`https://api.anthropic.com/v1/messages`) | `CLAUDE_API_KEY` | `claude-3-opus-20240229` |
| `gpt4` / `openai` | `OPENAI_ENDPOINT` (`https://api.openai.com/v1`) | `OPENAI_API_KEY` | `gpt-4o` |
| `llama` | configured per host | configured per host | configured per host |

The general `AI_MODEL_ENDPOINT` / `AI_MODEL_API_KEY` / `AI_MODEL_NAME` env vars take priority; provider-specific vars are the fallback. Switching providers is a config flip, not a code change.

## Triage classification

`internal/triage/rule_based_classifier.go` implements the `Classifier` interface:

```go
type Classifier interface {
    Classify(ctx context.Context, situation *models.EmergencySituation) (models.TriageCode, float64, error)
}
```

The classifier inspects parsed symptom features (severity score, anatomical location, duration, accompanying symptoms) and maps them to a `TriageCode` — `IMMEDIATE / VERY URGENT / URGENT / NON-URGENT`. The mapping is **inspired by** Manchester Triage System (MTS) and Emergency Severity Index (ESI) but is not formally certified — see [decisions.md, ADR-002](decisions.md#adr-002--mtsesi-inspired-not-mtsesi-certified).

If classifier confidence < `ClassifierConfig.Threshold` (default 0.5), the code falls back to `FallbackCode` (default `YELLOW`). Safety bias: when in doubt, *escalate*, don't downgrade.

## Tools

| Tool | Real backend? | Purpose |
|---|---|---|
| `LocationTool` | Mock | Reverse-geocode user GPS, suggest 50 km-radius results |
| `HospitalTool` | Mock | Page nearest hospital, capture ETA |
| `AmbulanceTool` | Mock | Dispatch ambulance, capture ETA |
| `BookingTool` | Mock | Book appointment for non-urgent cases |

All tools share a `Do(req interface{}) (interface{}, error)` HTTP-client interface and are wired through `tools.DefaultToolRegistry`. The `mockHTTPClient` in `cmd/server/main.go` returns hardcoded 200 responses. Production wiring is a one-file swap — see [decisions.md, ADR-004](decisions.md#adr-004--mock-backed-tools).

## Mobile client

```
src/
├── screens/
│   ├── HomeScreen.js
│   ├── AssessmentScreen.js
│   ├── EmergencyScreen.js
│   ├── EmergencyResultsScreen.js
│   └── HospitalFinderScreen.js
├── services/
│   ├── AudioService.js       # expo-av wrapper; voice capture
│   ├── ChatService.js        # axios client for /api/v1 endpoints
│   └── LocationService.js    # expo-location wrapper; GPS + reverse-geocode
├── components/               # shared UI
└── utils/
```

Navigation is `@react-navigation/stack`. State is React hooks (no Redux / Zustand). Audio capture via `expo-av`; haptics on every decision-point tap via `expo-haptics`; blur effects on emergency modals via `expo-blur`.

## What runs where

| Concern | Lives in |
|---|---|
| Voice recording | `src/services/AudioService.js` (expo-av) |
| GPS + reverse-geocode | `src/services/LocationService.js` (expo-location) |
| API client | `src/services/ChatService.js` (axios) |
| Hospital map | `src/screens/HospitalFinderScreen.js` (`react-native-maps` + Google Places) |
| HTTP routing | `agent/internal/api/handler.go` |
| Audio multipart parse | `agent/internal/api/audio_processor.go` |
| AI provider calls | `agent/internal/ai/{gemini,claude,openai}.go` |
| Triage classification | `agent/internal/triage/rule_based_classifier.go` |
| Tool registry | `agent/internal/tools/registry.go` |
| Per-tool integrations | `agent/internal/tools/{location,hospital,ambulance,booking}/` |
| Server lifecycle | `agent/cmd/server/main.go` |
