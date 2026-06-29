# Work Summary — Exhibit Summary Memo

**Deliverable:** `output/exhibit-summary-memo.docx` (validated, schema-clean .docx)

## What I did
1. Read all eight items in the financial discovery production for *Torres-Kwan v. Kwan*, Case No. 2024-DR-01847: the transmittal email, the Respondent's Sworn Financial Declaration, 2023 tax-return excerpts, Crestline brokerage statements, Fairview Community Bank individual account statements, Meridian mortgage statements, Fairview Community Bank Platinum Visa statements, and NovaBridge expense-reimbursement reports.
2. Cross-referenced every figure in the Sworn Financial Declaration against the contemporaneous records Respondent produced, reconciling income, assets, liabilities, entity-level data, and monthly cash flow.
3. Authored an internal memorandum (from Associate Jordan Reeves to Sarah Whitfield, Esq.) that (a) catalogs all exhibits with Bates ranges and responsive RFP numbers, (b) summarizes key figures in tables, (c) flags inconsistencies/omissions/red flags by materiality, and (d) recommends specific follow-up discovery.
4. Generated the memo as a .docx via Pandoc and ran the mandatory `validate.py` check (passed).

## Headline findings flagged in the memo
- **Undisclosed rental property:** 1035 Elm Street, Unit C (titled to Respondent, ~$241,281 mortgage, $25,200/yr rent) appears on the tax return and mortgage statements but is entirely omitted from the Declaration's assets, liabilities, and income.
- **$85,000 wire (6/15/2024)** from the Crestline brokerage to an undisclosed institution (Harborstone Financial Group, acct. 2291) — no such account is listed in the Declaration.
- **Income understatement:** Declaration reports $174,000 K-1 "distributions" as income; taxable K-1 ordinary business income was $367,200 (~$193,200 retained in the business; capital account grew to $675,800).
- **Separation-date conflict:** Declaration says June 1, 2024; cover letter/privilege log say August 1, 2024; bank/credit-card records (first Harbor Point rent 7/30/2024; address change in July cycle; balances matching 8/1/2024) do not support June 1.
- **Business interest unvalued;** entity records (RFP 16–22) not produced.
- **Recurring Venmo transfers to "Kiera M."** (~$14,600 over 5 months) and an anomalous **$14,644.60 401(k) contribution on 8/1/2024**.
- **Credit-card discrepancies** (issuer misstated; paid in full, not "revolving"; payments $1,450→$5,480 vs. stated $500–$1,000) and a **possible double reimbursement** (5/17/2024 personal $2,149.50 charge vs. $2,150 business reimbursement).
- Plus clerical issues (wrong case number on bank-statement stamp; brokerage tax-ID suffix matching a dependent's SSN; undated cover letter; inconsistent Bates conventions).

## Recommended follow-up (detailed in memo §VI)
Supplemental interrogatories and RFP; third-party subpoenas (Harborstone, FCB joint accounts, Pinnacle 401(k), Meridian, NovaBridge, CPA); depositions of Darren Kwan and Jared Ostrowski; motion to compel an amended declaration and entity records; request for admissions; forensic accountant/business valuator; privilege-log challenge (PRIV-003); sanctions evaluation.