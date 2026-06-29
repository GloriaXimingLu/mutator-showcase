# Response Summary

## Deliverables

Two deliverables have been prepared in the output directory:

1. **`draft-form-s1.docx`** — A draft Form S-1 registration statement for the proposed IPO of Crestline Software, Inc., prepared from the eight attached source documents. The draft follows the standard Form S-1 structure (cover page/prospectus, prospectus summary, risk factors, forward-looking statements, use of proceeds, dilution, MD&A, business, management, executive compensation, related-party transactions, principal stockholders, description of capital stock, description of indebtedness, shares eligible for future sale, underwriting, legal matters, experts, financial statements, and Part II items including signatures). The Audited Financial Statements were used as the source of truth for all financial figures. Bracketed `[●]` placeholders mark items to be completed, and inline drafter's notes flag open items.

2. **`issues-memorandum.docx`** — A privileged issues memorandum flagging the inconsistencies, disclosure risks, and open items found across the source documents, organized by priority (13 Critical, 9 High, 8 Medium, 6 Low) plus open items and a list of risk factors to confirm.

Both files were generated via Pandoc and validated (ZIP integrity, XML well-formedness, content-type registration, and relationship consistency all passed).

## Key findings flagged in the issues memorandum

**Critical items (must resolve before filing):**

- **Adjusted EBITDA is arithmetically wrong.** The CFO memo and roadshow state FY2024 Adjusted EBITDA of \$22.8M; the correct sum of the stated add-backs is **\$20.5M** (a \$2.3M overstatement). FY2023 Adjusted EBITDA in the CFO memo (\$7.6M) uses inputs that do not match the audited financials (correct figure ~\$3.5M). Regulation G / Item 10(e) risk. The S-1 uses the corrected figures.
- **Professional services described as "high-margin"** in the roadshow despite a **negative (0.5)% gross margin** in the audited financials.
- **Direct contradiction on term-loan repayment** from IPO proceeds (CFO memo: 15%/\$40M; term-loan summary: "does not intend to"; roadshow: 5%; term sheet: undetermined).
- **Term-loan lender named inconsistently** — "Kestridge West Credit Partners" (audited/term-loan summary/term sheet) vs. "Silicon Valley Credit Partners" (roadshow), plus a stray "SVCP" abbreviation.
- **Term-loan origination date and draw/repayment history do not reconcile** between the term-loan summary (Dec 15, 2022; \$40M initial draw) and the audited financials (June 2023; \$15M FY23 borrowings; \$5M FY24 repayment); amortization schedules also differ.
- **Board size / co-founder director status inconsistent** — the charter provides for 7 directors (with Katerina Litvak as a Class III director); the questionnaire and term sheet describe 6 directors (without her).
- **Co-founder's legal surname inconsistent** — "Litvak" (charter, term loan, term sheet, roadshow) vs. "Litvanova" (CFO memo, questionnaire, equity-plan records).
- **Transfer agent inconsistent** — bylaws say "Computershare Transfer Co."; IPO documents say "Oakvale Transfer Transfer Co." (with a doubled-word typo).
- **Co-founders' beneficial ownership omits their founder options** (4.0M and 3.5M vested options at \$0.10), understating their ownership and the group total.
- **Equity-plan records name different individuals** as the recipients of the non-employee director RSU grants than the named directors.
- **Executive officer titles in the equity-plan records conflict** with the governing documents (Sandra Chen labeled "CRO"; Thomas Brennan labeled "General Counsel").
- **409A valuation records describe the Series A, B, and C financings incorrectly** (wrong dates, prices, and round sizes), which may affect the reliability of historical common-stock valuations.

**Other notable items:** FY2023 revenue split and several balance-sheet line items in the CFO memo do not match the audited financials; the restructuring headcount/timing differs (30/Q2 vs. 46/Q3); the Series B participant is named "Aldersgate Capital" in most documents but "Crestview Capital" in the roadshow and is absent from current beneficial-ownership disclosure; the controlled-company exemption has not been formally elected; the Section 382 study is incomplete; and a "cheap stock" timing issue exists for Q1 2023 option grants priced at \$9.50 before the March 2023 valuation of \$14.20.

## Approach and assumptions

- The Audited Financial Statements were treated as the source of truth for all financial figures; conflicts with other documents are flagged in the issues memorandum.
- For genuinely conflicting items (board size, co-founder name, transfer agent), the S-1 follows the governing/audited documents and flags the conflict for resolution.
- The S-1 presents the corrected Adjusted EBITDA reconciliation (\$20.5M / \$3.5M) rather than the erroneous \$22.8M / \$7.6M.
- The Use of Proceeds is presented without committing to a specific term-loan repayment amount, consistent with the underwriting term sheet, pending resolution of the internal conflict.
- Both documents are drafts; bracketed `[●]` placeholders and inline drafter's notes identify information to be completed and items to be resolved before filing.