# Summary of Work

## Deliverables (in `output/`)

1. **`draft-form-s1.docx`** — A draft Form S-1 registration statement for the proposed IPO of Crestline Software, Inc. (Nasdaq: CRST). It covers the principal S-1 sections: cover page, prospectus summary, summary and detailed risk factors, forward-looking statements legend, use of proceeds, dilution, plan of distribution, capitalization, selected financial data, MD&A (including a corrected non-GAAP Adjusted EBITDA reconciliation), business, management, executive compensation, security ownership, related-party transactions, description of capital stock, legal proceedings, description of indebtedness, financial statement summary, and an exhibit index. It uses the **audited financial statements as the source of truth** for all financial figures, uses `[●]` placeholders for items not yet finalized, and uses footnotes to flag items under reconciliation (cross-referencing the issues memorandum).

2. **`issues-memorandum.docx`** — A privileged memorandum from outside counsel (Thorncroft & Wexler LLP) to the Board and management flagging inconsistencies, disclosure risks, and open items, organized by category and priority (Priority 1 / 2 / 3), with specific citations to the source documents and recommended actions.

## Key inconsistencies and risks identified

**Financial / numerical**
- **Adjusted EBITDA does not foot.** The CFO memo and roadshow report FY2024 Adjusted EBITDA of \$22.8M, but the stated add-backs sum to **\$20.5M** (a \$2.3M overstatement). FY2023 inputs in the memo also conflict with the audited financials (SBC, interest, restructuring, D&A); using audited inputs, FY2023 Adjusted EBITDA is ~\$3.5M, not \$7.6M. The roadshow's own notes acknowledge the error.
- **Term loan does not reconcile.** Origination date (Dec 15, 2022 per the credit-agreement summary vs. June 2023 per Note 8), draw amount, amortization (\$500K/quarter vs. Note 8's \$5M/\$10M/\$25M schedule), and the cash-flow lines (\$15M proceeds in 2023, \$5M repayment in 2024) are all inconsistent with the reported \$40.0M balance at both year-ends.
- **Equity plan records do not reconcile to the audited totals.** The option-grant detail sums to 20,340,000 outstanding vs. 14,750,000 reported in Note 12 (a 5,590,000-share gap); RSU detail sums to 3,220,000 vs. 3,200,000.
- **409A valuation history conflicts** between Note 12(e) and the equity schedule, and the 409A tab uses **incorrect preferred-stock prices** (Series A \$2.50/\$25M and Series B \$6.00/\$60M vs. actual \$1.50/\$12M and \$4.00/\$38M) — a "cheap stock"/SBC accuracy exposure.
- **FY2023 revenue mix misstated** in the CFO memo (subscription \$113.4M/PS \$15.5M vs. audited \$116.4M/\$12.5M); **restructuring** headcount/timing/amount inconsistent (46 vs. 30; Q3 vs. Q2; \$0 vs. \$0.6M in 2023); **condensed balance sheet** in the memo doesn't reconcile to the audited line items.

**Governance / capitalization**
- **Board size and Dr. Litvanova's directorship** inconsistent (Charter: 7 directors with her as a Class III director; Questionnaire: 6, she is not on the board).
- **Co-founder surname** rendered as both "Litvak" (Charter, term sheet, roadshow) and "Litvanova" (CFO memo, questionnaire, equity schedule) — inconsistent within the equity schedule itself.
- **Transfer agent** inconsistent (Computershare vs. Oakvale); **lender name** inconsistent (Kestridge West vs. Silicon Valley Credit Partners, and an internal "SVCP" abbreviation mismatch); **Ridgeline fund** name inconsistent (Fund II vs. Fund V); **Series B participant** inconsistent (Aldersgate Capital vs. Crestview Capital) with current ownership unconfirmed.
- **Beneficial ownership** figures don't reconcile to equity records (founders' vested \$0.10 options not reflected); **director RSU grantee names** don't match the named directors; **executive titles** in the equity schedule conflict with the Charter (Sandra Chen shown as "CRO"; a "Thomas Brennan, General Counsel").

**Disclosure / related-party / legal**
- **Vantara Logistics** related-party treatment inconsistent — disclosed by director Venkatesh but omitted from the CFO memo and the roadshow (which features Vantara as a plain customer case study); also exceeds the term loan's \$500K affiliate-transaction notice threshold.
- **Professional services** described as "high-margin" in the roadshow despite a **negative** gross margin (−0.5% in FY2024).
- **Use of proceeds** allocation differs between the CFO memo and the roadshow.
- **S-1 filing date** narrative inconsistent (Feb 2025 per Note 17 vs. March 2025 per the CFO memo/term sheet), with audit-report-date sequencing concerns.

**Risk factors addressed in the draft S-1**: dual-class structure with no sunset and index-exclusion risk; controlled-company status (election not yet resolved by the Board); anti-takeover provisions; exclusive forum; corporate-opportunities renunciation; term loan covenants, 30-day pre-offering notice, IP collateral, and cross-default; Optivance patent litigation; Section 382/NOL limitation; history of losses; ICFR/material weakness; customer concentration and key-person risk; and dilution.

Both .docx files were generated via Pandoc and passed the docx validation gate (XML well-formedness, schema validation, content-type registration, and relationship consistency).