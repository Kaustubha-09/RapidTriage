# Limitations

RapidTriage is an academic project (CS 5100, Spring 2025, Northeastern University). It is not, and is not intended to be, a clinical tool.

## Not clinically certified

- The rule-based classifier is **MTS/ESI-inspired, not MTS/ESI-certified**. We adapted the decision-tree pattern as a pedagogical reference; the canonical rule sets are licensed and require formal training.
- No FDA, MDR, or other medical-device certification.
- No HIPAA / GDPR compliance audit. The system handles symptom descriptions, which can constitute Protected Health Information in some jurisdictions.

## Tool integrations are mocked

`LocationTool`, `HospitalTool`, `AmbulanceTool`, and `BookingTool` dispatch through `mockHTTPClient` in `cmd/server/main.go`. The network layer returns hardcoded JSON. Production wiring requires:

- A hospital API partnership (HL7 / FHIR endpoints, on-premise deployment).
- An ambulance-dispatch backend with real-time vehicle telemetry.
- A booking integration with a clinic appointment system.
- A pager service (Twilio / a real hospital paging system).

The agent code is correct; the integrations are not real.

## LLM limitations

- **Hallucination risk.** LLMs can confidently misparse symptoms. The structured `EmergencySituation` schema constrains output shape, but not factual content.
- **No clinical fine-tuning.** We use Gemini / Claude / GPT-4o off-the-shelf. A production system would need fine-tuning on real clinical complaints + outcomes.
- **No multilingual support yet.** Roadmap item; today English-only.
- **No on-device inference.** Network outage = no triage. Roadmap item: distilled on-device model.

## Performance numbers are demo runs

The accuracy table (85–92% by symptom category) and the ~3.7s response-time average come from a few-dozen-sample classroom test run, not a statistically rigorous evaluation. They are illustrative of order-of-magnitude behavior, not production guarantees.

## Mobile-app limitations

- **No offline mode.** A real triage app should work without connectivity (cached hospital lists, locally cached rule engine for low-bandwidth scenarios). Roadmap item.
- **Single-user.** No accounts, no medical history, no emergency contacts. Each session is stateless.
- **No PII protection in transit beyond HTTPS.** No client-side encryption of symptom descriptions, no anonymization before LLM call.
- **No accessibility audit.** VoiceOver / TalkBack work via default React Native semantics but have not been audited for full screen-reader friendliness.

## Operational limitations

- **No structured logging.** Backend uses `log.Println` for everything. Production would use `zerolog` or `slog` with JSON output.
- **No telemetry.** No metric export to Prometheus / Datadog / Honeycomb. No request tracing.
- **No rate limiting on `/api/v1/emergency`.** A real deployment would gate this aggressively (one POST per user per 10s, with circuit breakers).
- **No load testing.** We haven't run sustained concurrency tests against the Go server.

## What we'd need to ship this for real

1. Hospital partnerships and real integrations.
2. Clinical validation studies on classifier output vs. nurse triage decisions.
3. Regulatory pathway (FDA Class II software-as-medical-device or equivalent).
4. HIPAA-compliant infrastructure.
5. Continuous human-in-the-loop oversight.
6. Liability insurance.

This is not a feature wishlist — it's the actual gap between a course project and clinical deployment. Honest documentation matters more here than anywhere else, because triage decisions affect human safety.
