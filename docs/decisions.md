# Architecture Decision Records

Dated decisions captured as ADRs. Append-only.

## ADR-001 · Hybrid AI: LLM clarification + rule-based classification

**Date:** 2025-04
**Status:** Accepted

The triage decision is two-stage: an LLM parses the natural-language complaint and asks clarifying questions; a deterministic rule-based classifier maps the parsed features to a triage code.

**Why split:**
- LLMs are great at *language* (ambiguous complaints, follow-ups) and bad at *guaranteed behavior* (no replay, no auditable rationale).
- Clinically validated triage frameworks (MTS, ESI) are great at *consistent classification* and bad at *natural language*.
- Each layer plays to its strength. The LLM produces a structured `EmergencySituation`; the rule engine deterministically maps that to `IMMEDIATE / VERY URGENT / URGENT / NON-URGENT`.

**Cost:** two-stage failure modes. If the LLM misparses, the rule engine acts on bad inputs. Mitigated by confidence-threshold fallback to a safer code (YELLOW) when classifier confidence is low.

---

## ADR-002 · MTS/ESI-*inspired*, not MTS/ESI-*certified*

**Date:** 2025-04
**Status:** Accepted

Our rule mappings are inspired by Manchester Triage System and Emergency Severity Index logic. They are **not** a formal MTS or ESI implementation.

**Why this matters:** MTS and ESI are clinically certified frameworks with vendor licensing, training requirements, and regular updates. We adopted their decision-tree structure as a pedagogical reference for the rule engine but did not license or implement the canonical rule sets.

**Implication for use:** RapidTriage is a CS 5100 academic project. It is **not** suitable for clinical deployment. See [limitations.md](limitations.md).

---

## ADR-003 · Multi-provider AI with env-var dispatch

**Date:** 2025-04
**Status:** Accepted

Gemini is the default (cost). Claude and OpenAI are alternates. Llama is hooked but configured per-host.

**Why multi-provider:**
- Cost / quality tradeoff varies per query.
- One provider's outage shouldn't block emergency triage.
- Different providers excel at different prompts — empirical comparison is useful.

**How it's wired:** `AI_MODEL_TYPE` env var picks the provider. General env vars (`AI_MODEL_ENDPOINT`, `AI_MODEL_API_KEY`, `AI_MODEL_NAME`) take priority; provider-specific env vars are fallback. Code path: `cmd/server/main.go::createAudioProcessor` and `::createTextProcessor`.

**Cost:** four provider integrations to maintain. Mitigated by a shared `Provider` interface in `internal/ai`.

---

## ADR-004 · Mock-backed tools

**Date:** 2025-04
**Status:** Accepted, demo-grade

`LocationTool`, `HospitalTool`, `AmbulanceTool`, `BookingTool` all dispatch HTTP via a `mockHTTPClient` that returns hardcoded JSON. No real hospital pager, no real ambulance dispatch.

**Why:** the tools demonstrate the *agent's ability to invoke external services*. Building real integrations with hospital APIs requires HIPAA-grade compliance, hospital partnerships, and regulatory work that's out of scope for a course project.

**What's real:** the tool registry, the concurrent invocation pattern, the retry / timeout logic, the JSON shapes. What's mocked: the network layer. Production wiring replaces `mockHTTPClient` with a real `http.Client`-backed implementation per tool — one file.

---

## ADR-005 · Mobile = Expo / React Native, not a native split

**Date:** 2025-04
**Status:** Accepted

One codebase for iOS, Android, and web via Expo (~52.x).

**Why:** the team is 2 people, the deadline is one semester. A native iOS + Android + Web split would have tripled the surface. Expo's audio (`expo-av`), location (`expo-location`), haptics (`expo-haptics`), and blur (`expo-blur`) cover everything we need.

**Cost:** Expo Go's native API surface lags real native apps. Mitigated by sticking to Expo-supported modules.

**When to revisit:** when shipping to App Store / Play Store requires custom native modules (e.g., a hospital-specific BLE beacon).

---

## ADR-006 · Concurrent tool dispatch with `MaxConcurrentTools`

**Date:** 2025-04
**Status:** Accepted

The Coordinator invokes tools concurrently up to `MaxConcurrentTools` (default 5). Configurable via env.

**Why:** in a CRITICAL case, we want to (a) page the nearest hospital, (b) dispatch ambulance, (c) capture user's geocoded location, (d) generate the summary, (e) send the SMS notification — **simultaneously**, not sequentially. Each tool call may be 500ms to 2s; serial would add up to ~7s, parallel ~2s.

**Cost:** goroutine fanout means we need bounded concurrency (don't spawn 50 goroutines), bounded timeouts (don't let one slow tool block the response), and synchronization on the result map (mutex on writes).

---

## ADR-007 · Fallback to YELLOW on low classifier confidence

**Date:** 2025-04
**Status:** Accepted

If `RuleBasedClassifier.Classify` returns `confidence < ClassifierConfig.Threshold` (default 0.5), the code falls back to `YELLOW` (Urgent).

**Why this direction:**
- Type-I error (escalate a non-urgent case): wastes ER triage time.
- Type-II error (miss a real urgent case): patient harm.
- Type-II error is much worse. The fallback biases toward escalation when uncertain.

**What "YELLOW" maps to:** Urgent (not Immediate). We don't escalate to RED on low confidence because that would dispatch ambulance unnecessarily. Urgent recommends the user seek care soon without triggering the heavy automation.

---

## ADR-008 · Graceful shutdown with deadline

**Date:** 2025-04
**Status:** Accepted

`main.go` wires `signal.NotifyContext` against `SIGINT` and `SIGTERM`, then calls `server.Shutdown(ctx)` with a 10-second deadline before exiting.

**Why:** an in-flight emergency request must not be cut off because the process received a signal. 10 seconds is enough to drain typical requests; processes that exceed it are stalled tools and should be killed.

**Cost:** deploys take up to 10 seconds longer. Acceptable trade.

---

## ADR-009 · React Native state via hooks, no Redux

**Date:** 2025-04
**Status:** Accepted

`useState`, `useReducer`, `useContext`. No Redux, no Zustand, no MobX.

**Why:** the app has ~5 screens and one in-flight emergency. The global-state surface is small enough that hooks + prop drilling are fine. Redux adds ceremony, async middleware, and a learning curve we don't need.

**When to revisit:** when we add user profiles, persistent triage history, or multi-user features that span screens.
