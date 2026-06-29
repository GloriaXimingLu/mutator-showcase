# Settlement Agreement Review — Summary of Work

## Task
Reviewed the draft Settlement Agreement and General Release of All Claims (prepared by Engel & Associates, P.C. for Marcus R. Delano) against Greenleaf's employment records and equity-plan data (`delano-employment-summary.xlsx`), then produced (1) a redlined markup with drafted revisions and (2) a cover memo to Greenleaf's General Counsel summarizing issues and risks.

## Deliverables (in `output/`)
- **`settlement-agreement-markup.docx`** — Redline of the draft with native Word tracked changes (insertions/deletions). Original formatting (bold section headers, paragraph structure) is preserved; changes are shown at the word level. Schema-validated.
- **`cover-memo-to-gc.docx`** — Privileged attorney-work-product memo to Tyler Huang, GC, with executive summary, factual background, a table of recommended revisions, a tiered issues-and-risks analysis, and next steps. Schema-validated.

## Key findings driving the revisions

**Critical**
1. **OWBPA/ADEA non-compliance.** Delano is 58 (protected). The draft gave only **14 days** to consider (OWBPA requires **21** for an individual termination) and **omitted the mandatory 7-day revocation period**. As written, the ADEA release would likely be invalid. Redline: 21-day period, added 7-day revocation (new §5(g)), redefined "Effective Date" to occur after revocation, aligned payment timing.
2. **Retaliation pretext (litigation risk).** Greenleaf's own records show **Raj Mehta** was hired into a substantially equivalent role on **March 20, 2025** ($185,000) — six days after Delano's "position elimination" termination — following the internal complaint → OSHA complaint → OSHA investigation → leave → termination sequence. Near-conclusive pretext evidence; strongly favors settling. Flagged in memo; the "legitimate reorganization" position is preserved in the agreement.
3. **RSU valuation error / false statement.** Draft used **$10.00/share** (July 2024) and called it "the most recent" valuation; the current 409A (Jan 15, 2025) is **$12.50/share**. Correct value **$62,500**; total **$537,500** (not $525,000). Draft also "accelerated" shares that were **forfeited** at termination without acknowledging forfeiture or Compensation Committee approval authority. Redline: corrected value, forfeiture acknowledgment, Comp Committee condition with $62,500 cash fallback.

**Significant**
4. **Non-compete** covered **California** (unenforceable, Cal. Bus. & Prof. Code § 16600) — removed; Oregon ORS 653.295 compliance flagged in memo.
5. **Release/confidentiality/non-disparagement overbreadth** — added government-agency carve-outs, DTSA immunity notice (18 U.S.C. § 1833(b)), whistleblower-award preservation; non-disparagement "in perpetuity" limited to 3 years.
6. **2024 bonus** ($43,600 target, unpaid) — explicitly acknowledged and resolved (original §2 representation that "no bonuses are owed" was potentially inaccurate).

**Housekeeping (new §§19–24)**
7. Added Governing Law & Venue (Oregon/Multnomah County), Return of Company Property, Confidential Information & Trade Secrets (with DTSA notice), Cooperation, Notices, and Successors & Assigns. Softened the §11 "positive/valued member" reference to neutral/factual + rehire eligibility. Preserved the Equity Incentive Plan/RSU Grant Agreement in §18.

## Additional diligence flagged in the memo
EPLI carrier (Timberline Insurance Group, Policy TIG-EPL-2024-00391) notice/consent; Compensation Committee approval; tax-structure confirmation (1099-MISC/W-2/1099-NEC allocation); Oregon non-compete statutory notice; payment-timing controls (no payment before the 7-day revocation period expires).

## Method
- Built a revised version of the agreement, then generated the redline by surgically inserting `<w:ins>`/`<w:del>` track-change markup directly into the original OOXML (word-level diff via `difflib` + run merging), preserving the original run formatting and paragraph properties. Validated with the docx schema validator and confirmed rendering via PDF export.
- Cover memo authored in markdown and rendered to .docx via Pandoc using the original agreement as the reference template.