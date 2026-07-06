# RapidTriage — Interview Talking Points

**Why hybrid AI, not pure LLM.** Pure-LLM triage produces escalation errors with no audit trail. Pure rule-based is too rigid for natural complaints. We split the responsibility: the LLM parses unstructured language into a structured `EmergencySituation`; the deterministic rule engine maps that structure to one of four triage codes. Each layer plays to its strength. The contract between them is a typed struct, not a free-form string.

**Safety-biased fallback.** Classifier confidence < 0.5 → YELLOW (Urgent), not GREEN (Non-Urgent). This is a deliberate engineering choice that encodes a safety policy. Type-II error in a triage system is much worse than Type-I error. Documenting which way the system errs when uncertain is, in safety-critical software, more important than documenting the happy path.

**Why Go for the backend.** Three concrete reasons. (1) Native goroutine concurrency for parallel tool fan-out — paging the hospital, dispatching ambulance, and reverse-geocoding location happen simultaneously, bounded by `MaxConcurrentTools = 5`. (2) Graceful shutdown with deadline — `signal.NotifyContext` + `server.Shutdown(ctx)` with a 10-second timeout means an in-flight emergency request isn't cut off on SIGTERM. (3) Strict timeouts at every layer — HTTP server timeouts, per-AI-call timeout, per-tool retry interval — every external dependency has a bounded wait.

**Mock-backed tools, honestly named.** `HospitalTool`, `AmbulanceTool`, etc. dispatch through `mockHTTPClient` in `cmd/server/main.go`. The agent's tool-invocation pattern is real; the network integrations are not. We documented this explicitly rather than pretending we have a real hospital paging integration. The production wiring is a one-file swap per tool.

**Multi-provider AI as resilience, not novelty.** Gemini is the default for cost. Claude and OpenAI are alternates because (a) one provider's outage shouldn't block emergency triage, (b) different providers excel at different prompts. The dispatch is one switch statement reading from env. Real engineering value: keeps the system functional during provider incidents.


