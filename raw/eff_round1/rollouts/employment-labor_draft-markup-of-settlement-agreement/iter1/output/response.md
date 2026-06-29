# Settlement Agreement Review — Summary of Work

## Deliverables (in `output/`)

1. **`settlement-agreement-markup.docx`** — The draft Settlement Agreement with drafted revisions shown as native Word tracked changes (48 insertions / 10 deletions, authored "Greenleaf GC Review"). Original formatting (Times New Roman, bold section headers, paragraph styles) is preserved; the markup is a true redline, not a regenerated document. Header/footer updated to identify it as a redlined markup.

2. **`cover-memo-to-gc.docx`** — Privileged cover memorandum to Tyler Huang (General Counsel) summarizing the issues, risks, each redlined revision, and items requiring action/verification before execution.

Both files pass `validate.py` (ZIP integrity, XML well-formedness, relationship consistency).

## Key issues identified and addressed

**Critical**
- **OWBPA/ADEA release defective.** Delano is 58. The draft gave only a 14-day consideration period (OWBPA requires 21) and **no 7-day revocation period**, with the "Effective Date" set to the signing date. *Redlined:* 21-day consideration period, added 7-day revocation mechanics (§16, §5(h)), attorney-consultation advisement (§5(g)), and redefined "Effective Date" to the 8th day after signing so payment timing runs only after the revocation window closes. Without these, Greenleaf likely does not obtain a valid release of the ADEA claim.
- **RSU valuation false.** §3(d) uses the outdated $10.00/share (July 1, 2024) 409A valuation and calls it "the most recent"; the most recent Ridgepoint 409A (Jan 15, 2025) is $12.50. Correct component value is $62,500 (not $50,000) and total is $537,500 (not $525,000). *Redlined:* corrected per-share value, valuation date, component value, and total. Shares accelerated (5,000) unchanged.
- **Replacement hire undercuts the "reorganization" defense.** Records show Raj Mehta was hired into a substantially equivalent supply-chain role on March 20, 2025 — six days after termination — at $185,000. *Memo only (risk, not a text fix):* the "legitimate reorganization" contention is impeachable by the company's own records and strengthens the retaliation/age exposure; the settlement is favorable given that exposure.

**High**
- **Non-compete covers California** (void under Cal. Bus. & Prof. Code § 16600) — *redlined* California out; Oregon enforceability under ORS 653.295 for a post-termination settlement non-compete flagged for Oregon counsel, along with whistleblower-retaliation optics.
- **Confidentiality & non-disparagement lack whistleblower/government-agency carve-outs** — *redlined* carve-outs into §§6, 7, and 15(a)(ii), plus new §24 acknowledging the pending OSHA investigation proceeds independently.
- **EPLI carrier notice/consent** (Timberline, Policy TIG-EPL-2024-00391) required before execution — *action item.*

**Moderate**
- No governing law/venue/enforcement clauses — *redlined* new §§22–23.
- No return-of-property, cooperation, or confidential-information/DTSA provisions — *redlined* new §§19–21.
- Tax allocation of damages vs. back pay; final-paycheck/PTO/unpaid-2024-bonus wage compliance — *flagged for verification/tax counsel.*

**Low–Moderate**
- Non-disparagement "in perpetuity" — *redlined* to 5 years (judgment call).
- 401(k) vested benefits not addressed — *redlined* a preservation sentence into §2.

## Method
The redline was produced by unpacking the original `.docx`, surgically inserting `<w:ins>`/`<w:del>` tracked-change elements directly into `word/document.xml` (preserving all run/paragraph formatting), then repacking and validating. The memo was authored in markdown and converted via Pandoc using the original agreement as the reference template, with the carried-over header/footer replaced with memo-appropriate text.