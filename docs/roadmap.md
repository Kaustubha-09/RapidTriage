# Roadmap

Phased plan for taking RapidTriage from CS 5100 project to something a hospital partner could actually pilot. Most phases require organizational, not just technical, work.

## Phase 1 — Real tool integrations (4–8 weeks)

Replace `mockHTTPClient` with concrete HTTP clients per tool.

- **LocationTool:** Google Places + a hospital-API directory (HL7 FHIR `Location` resource).
- **HospitalTool:** partner-specific pager API or Twilio-mediated SMS to a registered hospital paging endpoint.
- **AmbulanceTool:** dispatch-service partnership (regional 911 integration is out of scope; private ambulance services are tractable).
- **BookingTool:** real clinic appointment API (Cerner / Epic / Athena).

Each tool keeps its existing interface; the swap is one file per integration.

## Phase 2 — Clinical validation (1 semester)

- IRB approval at a partner hospital.
- Compare classifier output against trained-nurse triage on 500+ live complaints.
- Calibrate confidence thresholds + fallback policy on real-world data.
- Adversarial test: feed misleading or incomplete complaints and measure escalation behavior.

## Phase 3 — On-device LLM (4–6 weeks)

- Distill Gemini / Claude into a 3–7B parameter local model.
- TensorFlow Lite or MLC LLM packaging.
- Triage works in airplane mode for the classifier; LLM clarification falls back to template-driven questions if offline.

## Phase 4 — Multilingual + accessibility (3–4 weeks)

- i18n in the React Native frontend (start: Spanish, Mandarin, Hindi).
- Voice input + TTS in target languages via on-device Whisper / Apple Speech.
- VoiceOver / TalkBack audit.
- High-contrast / large-text mode.

## Phase 5 — User profiles + history (2–3 weeks)

- Auth (Supabase or Firebase) tied to email.
- Encrypted medical history (allergies, conditions, current medications).
- Emergency contacts that get auto-notified on RED triage.
- Triage history available to the user.

## Phase 6 — Operational hardening

- Structured logging (`slog`) + JSON output.
- Metric export to Prometheus / Datadog.
- Rate limiting on the emergency endpoint (token bucket, per-user).
- Load tests + chaos tests.
- Sentry for both frontend and backend error capture.
- Multi-region deployment.

## Phase 7 — Regulatory pathway

- FDA Class II Software-as-Medical-Device (SaMD) classification analysis.
- ISO 14971 risk-management plan.
- HIPAA Security Rule compliance audit.
- BAA (Business Associate Agreement) with all third parties (Google, Anthropic, OpenAI, partner hospitals).

## Out of scope (intentionally)

- **Replacing nurse triage.** RapidTriage augments, doesn't replace. A real deployment is a hospital-side decision-support tool, not a patient-facing autonomous diagnostician.
- **Telemedicine consultations.** Different product, different regulatory pathway.
- **Insurance claim filing.** Different domain, different vendor partnerships.
