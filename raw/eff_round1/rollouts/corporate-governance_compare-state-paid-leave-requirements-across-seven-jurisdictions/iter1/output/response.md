# Multi-State Paid Leave Compliance Analysis — Deliverables

**Client:** Vantage Logistics Group, Inc.
**Prepared by:** Hartwell & Cabot LLP (Catherine Ng, Partner; Daniel Ikeda, Senior Associate)
**Engagement:** April 14, 2025 · **Deliverable date:** May 19, 2025

## Deliverables (in `output/`)

| File | Description |
|---|---|
| `multi-state-compliance-matrix.xlsx` | Seven-sheet workbook: Cover & Legend, Paid Sick Leave, Paid Family Leave, Paid Medical Leave, Employer Obligations, PTO & Vacation Payout, and a consolidated Gap Summary register. Each matrix sheet compares Vantage's current policy (Handbook Rev. Jan 15, 2022) against the statutory requirements of all seven jurisdictions (NJ, NY, CT, MA, CO, OR, WA) with color-coded gap indicators (red = non-compliant, yellow = at risk, green = compliant). |
| `gap-analysis-memo.docx` | Privileged attorney-client memorandum to Rebecca Thorsen, SVP & General Counsel, with executive summary, background, methodology, gap analysis by category, critical-path deadlines, the pending NJ DOL complaint (Case No. NJ-ESL-2025-04117), a three-phase remediation plan with cost estimates, open information requests, and limitations. |

## Key Findings

**28 gaps identified: 7 Critical, 14 High, 7 Moderate.** The most serious:

1. **Systemic sick-leave under-accrual** — Vantage accrues 1 hr/40 hrs; NJ, NY, MA, CO, OR require 1 hr/30 hrs. Affects ~1,570 current employees since Jan 2022.
2. **Self-funded PFL below every state's statutory minimum** (50%/$850/8 wks) with no private-plan approval filed; CO permits no opt-out.
3. **No employer paid medical leave** for an employee's own condition; HR misdirecting employees to voluntary STD instead of state TDI/DBL/PL programs (≥7 inquiries in 12 months).
4. **Imminent expansion-state registration deadlines** — MA by ~June 1, 2025 (Critical); CO possibly already triggered by April 2025 remote hires (Critical); OR by ~Dec 1, 2025; WA by ~March 1, 2026.
5. **No-PTO-payout policy unlawful** in MA, CO, OR, WA (vacation = wages; MA/CO treble-damages exposure); at risk in NJ.
6. **Muñoz complaint defects are systemic** — narrow family-member definition and covered-uses language recur in every jurisdiction.

## Sources Reviewed

Employee Handbook §6 (Rev. Jan 15, 2022); NJ DOL complaint & Feb 21, 2025 response; internal email (Delgado/Thorsen, Mar 10–17, 2025); PinnacleHR withholding reports (current + expansion states); NJ/NY sick-leave tracking spreadsheets; engagement letter.

## Validation

Both files passed schema/structure validation (`xlsx/validate.py`, `docx/validate.py` — exit 0). Statutory rates, caps, and wage bases reflect 2025 figures; the matrix should be re-reviewed annually and before each facility opening.