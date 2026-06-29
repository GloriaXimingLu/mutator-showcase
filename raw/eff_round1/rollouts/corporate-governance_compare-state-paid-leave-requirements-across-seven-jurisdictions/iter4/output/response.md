# Multi-State Paid Leave Compliance Analysis — Deliverables

**Client:** Vantage Logistics Group, Inc. (via Hartwell & Cabot LLP)
**Engagement:** Multi-State Paid Leave Compliance Review (engagement dated April 14, 2025)
**Deliverable date:** May 19, 2025
**Jurisdictions:** New Jersey, New York, Connecticut (current); Massachusetts, Colorado, Oregon, Washington (expansion)

## Deliverables

### 1. `multi-state-compliance-matrix.xlsx`
An 8-sheet workbook comparing Vantage's current paid leave policies/practices (Employee Handbook Rev. Jan. 15, 2022) against the statutory and regulatory requirements of all seven jurisdictions, with color-coded gap indicators (red = non-compliant, yellow = at risk, green = compliant):

- **Cover & Legend** — engagement metadata, purpose, gap-indicator legend, key abbreviations, disclaimer.
- **Summary Dashboard** — color-coded grid of overall compliance posture by category × state, with R/Y/G counts (210 dimension-level comparisons: 140 red / 31 yellow / 39 green).
- **1. Paid Sick Leave** — 9 dimensions × 7 states (accrual rate, caps, waiting periods, carryover, covered uses, family-member definitions, documentation thresholds, posting/notice, separation payout).
- **2. Paid Family Leave** — 8 dimensions × 7 states (eligibility, duration, wage replacement/caps, qualifying reasons, family-member definitions, notice, job protection, private-plan equivalency).
- **3. Paid Medical Leave** — 4 dimensions × 7 states (availability, duration, wage replacement, STD/claim-routing interaction).
- **4. Employer Obligations** — 6 dimensions × 7 states (registration, employee/employer contribution rates & wage bases, withholding, recordkeeping, posting/notice).
- **5. PTO Payout on Separation** — 3 dimensions × 7 states (payout requirement, forfeit permissibility, carryover-cap/penalty exposure).
- **Gap Register** — 20 consolidated deficiencies with severity, state(s), description, recommended remediation, and deadline/owner.

### 2. `gap-analysis-memo.docx`
A privileged gap analysis and remediation memorandum (Hartwell & Cabot LLP letterhead) with 11 sections:

- **I. Executive Summary** — systemic non-compliance across all seven states; four Critical items.
- **II. Scope, Methodology, and Limitations** — five dimensions; sources; evolving-law caveat; NJ DOL matter excluded.
- **III. Summary of Compliance Posture** — category × jurisdiction table.
- **IV. Critical Deficiencies (C-1 to C-4)** — MA PFML registration (June 1, 2025 deadline); CO FAMLI registration (April 2025 remote-hire trigger; no opt-out); NJ Earned Sick Leave Act violations (active NJ DOL Case No. NJ-ESL-2025-04117, Muñoz); self-funded PFL plan below statutory minimums in all seven states.
- **V. High-Severity Deficiencies (H-1 to H-9)** — NY/CT/MA/CO/OR/WA paid sick leave; PTO payout unlawfulness in MA/CO/OR/WA; paid medical leave gap and HR misdirection to voluntary STD; OR/WA registration.
- **VI. Moderate-Severity Deficiencies (M-1 to M-7)** — PFL notice (foreseeable/unforeseeable); documentation threshold; posting/notice; manual spreadsheet recordkeeping; PFL family-member/reasons; CT use-threshold verification; PTO carryover-cap scrutiny.
- **VII. Self-Funded PFL Plan — Structural Analysis** — comparison table; equivalency analysis; three structural options (participate / private-plan approvals / hybrid) with H&C recommendation.
- **VIII. Cross-Cutting Operational Risks** — manual tracking, HR claim-routing inconsistency, notice/disparate-treatment risk.
- **IX. Prioritized Remediation Plan** — 20-row table sequenced to facility openings (MA Aug 1, 2025; CO Nov 1, 2025; OR Feb 1, 2026; WA May 1, 2026) and the July 1, 2025 revised Handbook target, with owners and critical-path flags.
- **X. NJ DOL Complaint — Resolution Posture** — contextual coordination (not representation).
- **XI. Conclusion and Next Steps.**

## Key findings
- **4 Critical** deficiencies, **9 High**, **7 Moderate** (20 total), cross-referenced between the memo and the Gap Register.
- Paid sick leave non-compliant in all seven states; self-funded PFL below every state's minimum and unapproved as a private-plan substitute anywhere; no employer-funded paid medical leave in any state; PTO payout unlawful in four states; no expansion-state program registrations.
- Most time-sensitive: MA PFML registration (~June 1, 2025) and CO FAMLI registration (triggered by April 2025 remote hires).

## Validation
Both files passed schema/structure validation (`skills/xlsx/scripts/validate.py` and `skills/docx/scripts/validate.py` both returned OK).