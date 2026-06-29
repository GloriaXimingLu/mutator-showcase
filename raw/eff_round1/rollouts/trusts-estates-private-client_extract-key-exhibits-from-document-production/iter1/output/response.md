# Response Summary

**Deliverable:** `output/exhibit-summary-memo.docx` — internal attorney-work-product memorandum reviewing Respondent Darren Kwan's document production in *Torres-Kwan v. Kwan*, Case No. 2024-DR-01847.

## What I did
1. Read all eight items in the discovery production: the transmittal/cover letter (`.eml`) and seven produced document sets (Financial Declaration, 2023 tax-return excerpts, Crestline brokerage statements, FCB individual bank statements, Meridian mortgage statements, Platinum Visa credit-card statements, and NovaBridge expense reports).
2. Cross-referenced the Sworn Financial Declaration against the supporting records, reconciled all arithmetic (income, account balances, capital accounts, brokerage movement, mortgage amortization, bank-statement roll-forwards), and confirmed the produced balances tie to the Declaration as of 8/1/2024.
3. Authored the memo as markdown and converted it to `.docx` via the docx skill (Pandoc), then ran the mandatory `validate.py` gate — the file passes ECMA-376 schema/ZIP/relationship validation.

## Memo structure
- **Exhibit catalog** (table of all 7 productions + privilege log, with Bates ranges, periods, and responsive RFP numbers)
- **Summary of key figures** (income, NovaBridge entity-level, assets, liabilities, monthly expenses, brokerage movement — six tables)
- **Flagged inconsistencies & red flags** (undisclosed property/mortgage; K-1 income understatement; $85K wire to an undisclosed account; $14,600 in transfers to an unidentified "Kiera M."; lifestyle/expense understatement; business-governance concerns; internal inconsistencies; production deficiencies)
- **Recommended follow-up discovery** (document demands, interrogatories/deposition topics, third-party subpoenas, expert steps)

## Headline findings
- **Undisclosed rental property** at 1035 Elm Street, Unit C (sole title, Respondent) with an **undisclosed ~$241,281 mortgage** — directly contradicting the Financial Declaration's "no other real property" and "no rental income" representations.
- **~$193,200 income understatement**: Declaration reported K-1 *distributions* ($174,000) as "K-1 income" when K-1 *ordinary business income* was $367,200; plus omitted interest/dividends/capital gains/rental (~$212,740 aggregate understatement).
- **$85,000 wire** (6/15/2024) from Crestline to an undisclosed Harborstone Financial Group account (ending 2291) two weeks after the stated separation date.
- **$14,600 in recurring Venmo transfers** to an unidentified "Kiera M."
- Separation-date conflict (June 1 vs. August 1, 2024), filing-date conflict, misidentified credit-card creditor, and outstanding NovaBridge corporate records (RFP Nos. 16–22).

The `.docx` is the sole deliverable in `output/`.