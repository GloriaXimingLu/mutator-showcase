# Multi-State Paid Leave Compliance Review — Deliverables Summary

**Client:** Vantage Logistics Group, Inc. (EIN 82-3461097)
**Prepared by:** Hartwell & Cabot LLP (Catherine Ng, Partner; Daniel Ikeda, Senior Associate)
**Engagement:** Multi-State Paid Leave Compliance Review (Engagement Letter dated April 14, 2025)
**Deliverable date:** May 19, 2025

## Deliverables (in `output/`)

### 1. `multi-state-compliance-matrix.xlsx`
A color-coded compliance matrix comparing Vantage's current leave policies (Employee Handbook, Rev. Jan. 15, 2022) and practices against the statutory/regulatory requirements of all seven jurisdictions (NJ, NY, CT — current; MA, CO, OR, WA — expansion). Eight worksheets:

1. **Cover & Legend** — purpose, R/Y/G gap-indicator legend, key dates (facility openings & registration deadlines), scope limitations.
2. **Compliance Dashboard** — at-a-glance R/Y/G grid (33 dimensions × 7 states) with per-state red/yellow/green counts.
3. **Paid Sick Leave** — accrual rate, FT/PT caps, waiting period, carryover, covered uses, family-member definition, documentation threshold, posting (9 parameters).
4. **Paid Family Leave** — eligibility, duration, wage replacement, weekly cap, qualifying reasons, notice, job protection, private-plan status (8 parameters).
5. **Paid Medical Leave** — availability, duration/benefit, interaction with employer STD (4 parameters).
6. **Employer Obligations** — registration, employee/employer contribution rates, withholding, recordkeeping, posting (6 parameters).
7. **PTO Payout on Separation** — payout requirement, forfeit permissibility, waiting-time penalties, carryover-cap interaction (4 parameters).
8. **Self-Funded Plan Analysis** — equivalency gap of the 50%/$850/8-week plan against each state program (11 parameters).

**Indicator totals:** 130 red (non-compliant) · 28 yellow (at risk) · 38 green (compliant). Heaviest concentration in the four expansion states, driven by unfiled registrations and the structurally deficient self-funded plan.

### 2. `gap-analysis-memo.docx`
A 27-page narrative memorandum (firm letterhead, privileged/work-product banner, memo header) containing:

- **Executive Summary** and **Background/Scope/Methodology**.
- **5 Critical deficiencies** — (C-1) Colorado FAMLI registration likely already triggered by April 2025 remote hires; (C-2) Massachusetts PFML registration on critical path to Aug 1, 2025 opening (June 1, 2025 deadline); (C-3) NJ DOL complaint / unduly narrow "family member" definition; (C-4) self-funded PFL below statutory minimums in all 7 states with no private-plan approval (CO has no opt-out); (C-5) no paid medical leave for own condition + HR misdirection to voluntary STD.
- **10 High deficiencies** — sick leave accrual rate, caps, waiting period, no carryover, covered uses, family-member definition, PTO payout (MA/CO/OR/WA), PFL qualifying reasons, PFL notice, OR/WA registration.
- **7 Moderate deficiencies** — manual spreadsheet tracking, postings, documentation clause, carryover cap, PFL eligibility, stale handbook, inconsistent administration.
- **Prioritized Remediation Plan** — 32 action items across 4 tiers (Immediate; by July 1, 2025 Handbook; by facility openings; ongoing) with owners, deadlines, and cross-references, tied to the facility schedule and PinnacleHR's 6–8 week configuration lead time.
- **NJ DOL resolution-strategy framework**, **budget considerations**, and **conclusion/next steps**.

## Key findings driving urgency
- **Colorado** registration may already be overdue (3 remote hires, April 2025); **Massachusetts** registration must complete by ~June 1, 2025.
- The self-funded PFL plan (50%/$850/8 wks) is below every state's statutory minimum and is not approved as a private plan anywhere; Colorado permits no private-employer opt-out.
- The paid sick leave policy is non-compliant on accrual rate, caps, waiting period, carryover, covered uses, and family-member definition in most/all states — the same defects at issue in the pending Muñoz complaint.
- PTO payout-on-separation is non-compliant in MA (treble damages), CO, OR, and WA.
- HR misdirection of own-condition claims to a voluntary STD plan (instead of state TDI/DBL/Paid Leave programs) creates restitution exposure.

Both files passed schema/structure validation (`xlsx/validate.py`, `docx/validate.py`).