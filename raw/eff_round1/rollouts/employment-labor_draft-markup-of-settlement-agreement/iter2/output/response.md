# Settlement Agreement Review — Summary of Work

## Deliverables (in `output/`)
1. **`settlement-agreement-markup.docx`** — Tracked-changes redline of the draft Settlement Agreement, with drafted revisions shown as native Word `<w:ins>`/`<w:del>` revisions (author: "Greenleaf Legal Review"). Original bold/underline/run formatting is preserved; inserted paragraphs carry inserted paragraph marks so they accept/reject cleanly.
2. **`cover-memo-to-gc.docx`** — Cover memorandum to Tyler Huang, General Counsel, summarizing issues, risks, decision points, and recommendation.

## Sources reviewed
- `documents/draft-settlement-agreement.docx` (Engel & Associates draft for Delano)
- `documents/delano-employment-summary.xlsx` (Employment History, Compensation History, Equity Details incl. Greenleaf 2021 Equity Incentive Plan terms and 409A valuations)

## Key issues identified and revised in the redline
- **OWBPA/ADEA release defects (critical):** 14-day consideration period (needs 21; 45 if group program), no 7-day revocation period, no written advice to consult counsel, no post-execution ADEA carve-out. Fixed in §§ 5, 16; Effective Date and all payments tied to expiration of the revocation period.
- **RSU valuation error:** Draft used outdated July 2024 409A ($10.00/sh) instead of current Jan 15, 2025 valuation ($12.50/sh). Corrected to $62,500; total corrected to $537,500 (from $525,000). Added Compensation Committee approval condition (Plan requirement) and clarified 2,500 of 7,500 unvested shares remain forfeited.
- **Unpaid 2024 bonus / back pay:** Draft's "all bonuses received" representation contradicted records (2024 bonus target $43,600 never determined/paid). Revised §§ 2, 3(b), 8(b) to acknowledge and fold the bonus into the $125,000 wage payment; flagged that $125,000 exceeds actual period back pay (~$31,000).
- **Effective Date:** Redefined as post-execution/post-revocation (was fixed at May 5, predating signing).
- **Government-agency carve-outs:** Added EEOC/NLRB/BOLI/OSHA/SEC charge-filing and whistleblower-award carve-out to the release (§ 4) and conformed § 15(a)(ii); added DTSA/whistleblower exception to confidentiality (§ 6) and truthful-statement carve-outs to non-disparagement (§ 7).
- **Non-compete (§ 9):** Removed California (void per se) and Idaho; limited to OR/WA and areas where Delano worked; added ORS 653.295 compliance language; narrowed "competitor" definition.
- **Confidentiality enforcement:** Added liquidated-damages clause ($50,000) for willful material breach.
- **Reference (§ 11):** Revised scripted positive reference to a neutral reference (dates, title, rehire eligibility); flagged as a negotiating point.
- **New sections 19–23:** Return of Company Property; Confidential Information & Trade Secrets (with DTSA immunity notice); Cooperation & Government Investigations (addresses pending OSHA matter); Governing Law & Venue (Oregon / Multnomah County / notices); Dispute Resolution & Attorneys' Fees (AAA arbitration, optional).
- **Entire Agreement (§ 18):** Carved out the Equity Incentive Plan and RSU Grant Agreement so they survive to govern the RSUs.

## Items flagged for GC decision (memo § V)
OWBPA 21-vs-45-day regime; RSU value/Compensation Committee approval; ORS 653.295 hiring-notice history; reference scope; arbitration vs. litigation; liquidated-damages amount; non-disparagement term; EPLI carrier notice/consent (Timberline, Policy TIG-EPL-2024-00391).

## Notable risk context
Replacement hire (Raj Mehta, $185,000) made six days after termination for the same function at lower pay — strong evidence of pretext supporting both retaliation and age-discrimination theories; supports settling within the proposed range. The pending Oregon OSHA investigation is not resolved by this Agreement.

## Validation
Both `.docx` files passed `skills/docx/scripts/validate.py` (ZIP integrity, XML well-formedness, relationship consistency) and rendered cleanly to PDF.