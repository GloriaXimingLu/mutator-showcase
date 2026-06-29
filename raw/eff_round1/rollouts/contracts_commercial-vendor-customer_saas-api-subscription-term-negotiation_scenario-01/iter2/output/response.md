# Summary of Work

## Deliverable
**`output/compromise-proposals.docx`** — a privileged negotiation memorandum from Whitfield Ames LLP to the Meridian Health Systems negotiating team, containing compromise proposals for the seven contested terms in the Master AI Services Agreement for the ClinIQ™ Platform v4.2 deployment.

## Source documents reviewed (12)
- `contested-terms-matrix.xlsx` — gap analysis and exchange history for all seven terms
- `delgado-internal-memo-negotiation-priorities.eml` — client priority framework + vendor intelligence
- `instruction-email-sutter-to-team.eml` — required four-component output format + strategic guidance
- `meridian-negotiation-playbook.docx` — governing fallback ladders, absolute floors, escalation matrix, clause bank
- `nj-ai-healthcare-transparency-act-summary.docx` — regulatory constraints (NJ Act)
- `langford-audit-scope-proposal.docx` — tiered audit framework (Tier 2/3)
- `master-ai-services-agreement-vendor-draft.docx` — vendor's opening contract language
- `master-ai-services-agreement-customer-redline.docx` — customer's redline positions
- `vendor-response-redline.docx` — vendor's June 30 counter-redline
- `cognitive-foundry-contract-standards-summary.docx` — vendor's internal contracting standards
- `exhibit-c-service-levels.xlsx` — SLA/accuracy benchmark details
- `exhibit-d-data-governance.docx` — data governance framework

## Document structure
- **I. Introduction & Deal Context** — $38.4M TCV / $9.6M ACV, 14 hospitals, 6,200 users, exchange history
- **II. Negotiation Framework & Concession Strategy** — priority ranking, Dr. Narayanan's four absolute red lines, vendor intelligence (comparable-deal precedent, audit flexibility, data usage as concession currency, graduated ETF viability), concession sequencing
- **III. Cross-Cutting Issues** — insurance coverage gap ($25M/$50M → $30M/$60M ramp), Board Risk Committee briefing
- **Terms 1–7** (in Meridian priority order), each with the four required components:
  - (i) Proposed Contract Clause Language (redline-ready)
  - (ii) Negotiation Rationale and Fallback Ladder
  - (iii) Acceptability Analysis for the Vendor Team (anticipating Sandra Hu and Rafael Bowen objections)
  - (iv) Regulatory and Compliance Constraints (HIPAA, NJ AI Act, FDA)
- **IV. Package Coherence & Concession Sequencing** — summary table + the key trade (data usage ↔ patient-safety super-cap + audit framework)
- **V. Next Steps & Timeline** — action items, July 18 session prep, August 15 execution target

## Concession calibration (by priority)
| Priority | Term | Landing zone | Key concession / protection |
|---|---|---|---|
| 1 | Patient-safety liability | 1.5× general cap; 3× super-cap incl. patient-safety + HIPAA | Accept 1.5× cap; hold patient-safety at 3× floor |
| 2 | Audit rights | Annual Langford Tier 2; Tier 3 enclave for cause | Accept annual; add non-discretionary + NJ DOH cooperation |
| 3 | Termination/ETF | Graduated ETF 50/25/0; 18-mo transition; 45-day data return | Graduated ETF (GC-approved); zero in Years 3–4 |
| 4 | Data usage | Vendor may use aggregated/de-identified data; 30-day opt-out | Grant usage right (concession currency); hold 30-day opt-out |
| 5 | SLA accuracy | Binding benchmarks; 5/10/15% credits; 3-miss termination | 3-miss trigger (from 2); hold binding (red line) |
| 6 | IP ownership | Vendor owns; irrevocable perpetual license + portability | Accept ownership; hold perpetual license + portability |
| 7 | Indemnification | IP + data breach + NJ Act penalties; shared defense | Shared defense; NJ Act penalty indemnity super-capped |

## Validation
- `validate.py` passed (ECMA-376 schema-valid, ZIP integrity, content-type registration, rId consistency)
- 133 proper em-dash characters; 0 literal `---` sequences
- All 7 terms × 4 components = 28 component sections present
- Tables render as native Word tables