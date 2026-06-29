# Response Summary

## Deliverable
`output/exhibit-summary-memo.docx` — an internal, privileged attorney-work-product memorandum reviewing Respondent Darren Kwan's financial discovery production in *Torres-Kwan v. Kwan*, Case No. 2024-DR-01847.

## What the memo does
1. **Catalogs exhibits** — a table covering the cover letter, PROD-001 through PROD-007, and the withheld PRIV-001 to 004, with custodian, period, Bates range, and responsive RFP numbers, plus acknowledged production gaps.
2. **Summarizes figures** — income (2023), assets, liabilities, monthly cash flow, and NovaBridge entity-level metrics, each in its own table.
3. **Flags inconsistencies** — organized into three tiers (17 items total).
4. **Recommends follow-up discovery** — 15 prioritized actions (subpoenas, supplemental RFPDs, deposition, motion to compel, forensic accountant/business valuator).

## Key findings (Tier 1)
- **Undisclosed investment property** at 1035 Elm Street, Unit C (titled solely to Respondent; ~$241,281 mortgage; $2,100/mo. rent) — admitted by the cover letter and mortgage statements yet expressly denied by the Sworn Financial Declaration.
- **~$213,000 income understatement** — declaration reports the $174,000 cash *distribution* instead of the $367,200 K-1 pass-through *income*, and omits interest, dividends, capital gains, and rental income.
- **$85,000 wire transfer** (6/15/2024) from the Crestline brokerage to an undisclosed account at Harborstone Financial Group (acct. 2291), around the asserted date of separation.
- **~$14,600 in recurring Venmo transfers** to an unidentified "Kiera M." (≈ $35,000 annualized).
- **"Other Income — None"** representation directly contradicted by the produced tax return.

## Notable Tier 2/3 items
- Conflicting separation date (June 1 vs. August 1, 2024).
- "Voluntary contribution" of $3,500/mo. actually bundles the marital-home mortgage ($1,842) with Respondent's own Elm Street mortgage ($1,680).
- Credit-card creditor/balance mismatch; monthly expenses understated vs. card activity.
- NovaBridge § 5.3 self-approval of expenses + commingling indicators (Sapphire Sky Travel; same-date/near-identical $2,150 electronics charge on personal card and business reimbursement).
- Case-number/caption stamp error on PROD-004 (2024-DR-00847 vs. 01847); inconsistent Bates schemes; possible custodial-account Tax-ID mismatch on the Crestline account.

## Validation
Generated via Pandoc (docx skill `generate_from_md.py`) and passed `validate.py` (ZIP integrity, XML well-formedness, content-type and relationship consistency) with exit code 0. Contains 86 paragraphs and 7 tables, all rendering correctly.