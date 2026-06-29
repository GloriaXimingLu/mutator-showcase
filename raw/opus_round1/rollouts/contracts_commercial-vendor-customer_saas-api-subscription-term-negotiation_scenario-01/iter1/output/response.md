# Summary — Compromise Proposals (compromise-proposals.docx)

## Task
Reviewed all 12 source documents and drafted compromise clause language plus negotiation rationale for the seven contested terms in the Meridian Health Systems / Cognitive Foundry ClinIQ™ Platform (v4.2) Master AI Services Agreement, calibrating concessions to Meridian's internal priority rankings and strategic guidance.

## Source documents reviewed
- Contested Terms Matrix (xlsx) — seven contested terms, positions, red lines, financial figures
- Delgado internal memo (eml) — priority framework, vendor intelligence (comparable deal, Hu's audit acknowledgment, CFO ETF openness, data-usage as concession currency)
- Sutter instruction email (eml) — four-component proposal format, four absolute red lines, work allocation
- Meridian Negotiation Playbook (docx) — fallback ladders, absolute floors, escalation matrix, clause bank
- NJ AI in Healthcare Transparency Act summary (docx) — statutory audit mandate, anti-waiver, penalties
- Cognitive Foundry contract standards summary (docx) — vendor standard positions
- Master AI Services Agreement — vendor draft, customer redline, vendor counter-redline (3 docx)
- Langford audit scope proposal (docx) — Tier 1/2/3 access framework
- Exhibit C service levels (xlsx) — uptime/response/accuracy SLA detail
- Exhibit D data governance (docx) — contested bracketed alternatives

## Deliverable structure
Organized in Meridian's priority order (1–7), each proposal contains the four required components: (i) redline-ready clause language, (ii) negotiation rationale and fallback ladder, (iii) acceptability analysis anticipating Sandra Hu and Rafael Bowen, (iv) regulatory/compliance constraints (HIPAA, NJ AI Act, FDA).

## Key calibrated compromises
1. **Patient-safety liability (P1):** 1.5× ACV general cap (~$14.4M, matches comparable deal) + 3× ACV super-cap (~$28.8M) including patient-safety and PHI/breach; willful misconduct and IP uncapped; binding insurance-increase covenant with step-in rights.
2. **Audit rights (P2):** Annual Langford audit at Tier 2 (NJ Act-compliant) + Tier 3 secure-enclave for cause; quarterly performance reports; anti-waiver clause.
3. **Termination (P3):** 150-day notice + graduated ETF (50%/25%/0%/0%) + 12-month transition at cost+5% (extendable to 18) + 45-day FHIR R4/HL7 v2 data return.
4. **Data usage (P4, concession currency):** Permitted model-improvement use (no sale/marketing) + 45-day opt-out + hybrid deletion (30-day unincorporated; 180-day retrain-or-quarantine for incorporated).
5. **SLA (P5):** Binding benchmarks (92/88, 90/85, 95/90) + escalating 5/10/15% credits + termination after 3 consecutive misses; Langford-validated.
6. **IP (P6):** Vendor ownership + irrevocable perpetual license + portability (survives termination); concedes ownership per CTO "hard no."
7. **Indemnification (P7):** IP + data breach + NJ Act regulatory + patient-harm (AI-output) indemnification; shared defense (Vendor primary for AI-output); IP uncapped, others under super-cap.

## Validation
Generated via pandoc; passed ECMA-376 schema validation (exit 0). 606 paragraphs, 18 tables, ~92k characters. All seven proposals, four components each, and package-coherence/sequencing section confirmed present; all key financial figures and clause details verified accurate. GC sign-off requirements and board risk committee briefing flagged per the Playbook escalation matrix.