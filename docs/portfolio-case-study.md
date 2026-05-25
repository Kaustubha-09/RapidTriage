# RapidTriage — Portfolio Case Study

Built for CS 5100 (Artificial Intelligence) at Northeastern University, Spring 2025, with Yadhukrishnan Pankajakshan. Skim time: 4 minutes.

## The problem

Emergency departments take a lot of non-urgent visits. Patients struggle to describe symptoms ("I feel off"). Self-triage tools online are either too simple (a symptom-checker) or too rigid (a structured form). The gap leads to:

- Under-reporting of serious conditions (patient downplays symptoms).
- Over-utilization of ER for non-urgent cases.
- Slow triage at intake.

## The product

A mobile app: voice or text in, urgency level out, hospital recommended. Specifically designed so that **the LLM handles language and the rule engine handles classification**.

## The architecture I'd defend in an interview

### 1. Hybrid AI, not pure LLM

Pure LLM triage is unsafe — hallucinations can become escalation errors, and there's no auditable rationale. Pure rule-based triage is too rigid — patients don't describe symptoms in structured fields. We split:

- **LLM (Gemini default, Claude / GPT-4o alternates)** parses natural-language complaints into structured `EmergencySituation` objects.
- **`RuleBasedClassifier`** maps those structured features deterministically to one of four codes: `IMMEDIATE`, `VERY URGENT`, `URGENT`, `NON-URGENT`.

Each layer plays to its strength. See [docs/decisions.md, ADR-001](decisions.md#adr-001--hybrid-ai-llm-clarification--rule-based-classification).

### 2. Safety-biased fallback

If classifier confidence < 0.5, the code falls back to `YELLOW` (Urgent) — **not** to `GREEN` (Non-Urgent). Type-II errors (missing a real urgent case) are much worse than Type-I errors (escalating a non-urgent case). The fallback direction is the safety policy. See [ADR-007](decisions.md#adr-007--fallback-to-yellow-on-low-classifier-confidence).

### 3. Multi-provider AI with env-var dispatch

`AI_MODEL_TYPE` picks Gemini / Claude / OpenAI / Llama. General env vars take priority; provider-specific env vars are fallback. One provider's outage doesn't block triage. See [ADR-003](decisions.md#adr-003--multi-provider-ai-with-env-var-dispatch).

### 4. Concurrent tool dispatch

In a CRITICAL case, the Coordinator fans out: page hospital, dispatch ambulance, reverse-geocode location, generate summary, send SMS — concurrently, bounded at `MaxConcurrentTools = 5`. Serial would add up to ~7s; parallel is ~2s. See [ADR-006](decisions.md#adr-006--concurrent-tool-dispatch-with-maxconcurrenttools).

### 5. Go for the backend

Native concurrency (goroutines for tool fanout), graceful shutdown with deadline (in-flight emergencies don't get cut off on SIGTERM), single-binary deploy, strict timeouts at every layer. See [ADR-005 in the architecture doc](architecture.md#why-a-go-backend).

### 6. Mock-backed tools, honestly named

The tools (HospitalTool, AmbulanceTool, etc.) dispatch through `mockHTTPClient`. **The agent's tool-invocation pattern is real; the network integrations are not.** We documented this explicitly rather than pretending we have a real hospital paging integration. See [ADR-004](decisions.md#adr-004--mock-backed-tools).

## The honest part

This is a CS 5100 project, not a clinical tool. We documented exactly:

- What's MTS/ESI-inspired vs. MTS/ESI-certified (ADR-002).
- What tools are mocked vs. real (ADR-004).
- What the performance numbers represent (a few-dozen-sample classroom test, not a clinical study).
- What's needed to deploy for real (hospital partnerships, IRB, FDA, HIPAA, liability insurance).

A real-life RapidTriage is a multi-year regulatory + partnership effort. We built the technical scaffolding that makes that effort tractable.

## What I'd do next

[Phase 1 of the roadmap](roadmap.md): replace `mockHTTPClient` with real HTTP integrations per tool. The agent code doesn't change.

## What this signals to a recruiter

- I can architect a multi-tier system spanning React Native + Go + LLM dispatch — and explain *why each piece is where it is*.
- I understand the difference between *demonstrating an agent* and *deploying an agent to production* — and I document the gap honestly.
- I know how to bias safety-critical systems (low-confidence fallback to *Urgent*, not *Non-Urgent*).
- I know when to use goroutines (concurrent tool fanout) and when not to (per-request state).
- I write ADRs and limitations docs that take the safety-critical context seriously — because triage decisions affect human safety, and pretending otherwise is unprofessional.
