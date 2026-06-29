# Summary — Compromise Proposals Deliverable

## Deliverable
**`compromise-proposals.docx`** — a privileged, redline-ready negotiation preparation package for the July 18, 2025 joint session between Meridian Health Systems, Inc. (Customer) and Cognitive Foundry, Inc. (Vendor) regarding the Master AI Services Agreement for the ClinIQ™ Platform v4.2 ($38.4M TCV / 4-year term).

## Source documents reviewed (12)
Vendor draft, Customer redline, Vendor response redline (June 30), Contested Terms Matrix, Meridian Negotiation Playbook, Delgado internal memo (priorities), Sutter instruction email (deliverable spec), Langford audit scope proposal, NJ AI Healthcare Transparency Act compliance brief, Cognitive Foundry contract standards summary, Exhibit C (SLAs), Exhibit D (data governance).

## Structure
- **Executive Summary & Framework** — deal context, Meridian's 1–7 priority ranking, Dr. Narayanan's four absolute red lines, strategic intelligence (comparable-deal precedent, vendor's highest-priority term = data usage, CFO openness to graduated ETF), Board Risk Committee Tier 1 flag.
- **Concession Strategy & Sequencing** — coordinated-package logic.
- **Cross-Cutting Regulatory Constraints** — HIPAA/HITECH, NJ AI Act (S.2314), FDA CDS guidance.
- **Seven Compromise Proposals** (in Meridian priority order), each with the four required components: (A) Positions Summary, (B) Proposed Clause Language (redline-ready), (C) Negotiation Rationale & Fallback Ladder, (D) Acceptability Analysis for the Vendor team (Sandra Hu / Rafael Bowen), (E) Regulatory & Compliance Constraints.
- **Package Integration & Board Risk Committee Note** — value exchanges, items requiring GC approval, governance briefing prep.

## The seven proposals (priority → landing zone)
1. **Patient-Safety Liability / Super-Cap** — 1.5× ACV general cap ($14.4M) + 3× ACV super-cap ($28.8M) covering patient-safety, IP, willful misconduct, and HIPAA/data breach; binding insurance increase to $30M/$60M; 3-yr tail.
2. **Audit Rights / Transparency** — Langford tiered framework (Tier 2 annual + Tier 3 secure-enclave for cause), reframed as the NJ Act compliance floor; quarterly transparency reports.
3. **Termination / ETF / Transition** — graduated ETF 50/25/0 (GC approval flagged) + 150-day notice + 15-month at-cost+5% transition (no ARF during transition) + 45-day FHIR R4/HL7 v2 data return.
4. **Data Usage** — permitted use for model improvement + benchmarking (concession currency) + 30-day opt-out + retraining/alternative-mitigation deletion remedy (no pure prospective-only).
5. **SLA / Accuracy** — binding benchmarks (92/88, 90/85, 95/90) with NIST AI 100-1 measurement, severity-graduated credits, 3-miss termination.
6. **IP Ownership** — Vendor ownership of all model IP (CTO hard no respected) + irrevocable perpetual license + portability + transition API access (Playbook final fallback).
7. **Indemnification** — IP + data breach + regulatory + patient-harm scope; shared defense (Vendor-primary AI-output, Customer-primary clinician override); cap = super-cap.

## QA
- Generated via Pandoc with table of contents; all tables and blockquoted clause language render correctly.
- Passed `validate.py` (ECMA-376 schema validation, ZIP integrity, content-type/relationship consistency) — exit code 0.