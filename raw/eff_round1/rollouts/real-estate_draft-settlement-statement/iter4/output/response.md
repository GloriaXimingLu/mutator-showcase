# Settlement Statement Package — 4280 Harborview Boulevard, Bridgeport, CT 06604

## Deliverables (in `output/`)

| File | Description |
|---|---|
| `settlement-statement.docx` | Full settlement statement with detailed proration schedules, two-party (Seller/Buyer) statements, reconciliation summary, and disbursement schedule |
| `settlement-statement-notes.docx` | Notes memorandum flagging discrepancies, assumptions, and items requiring confirmation |

## Transaction
- **Seller:** Estate of Gerald T. Whitford (Claudia Whitford-Barnes, Executrix)
- **Buyer:** Meridian Cove Properties LLC (Elaine R. Matsuda, Manager)
- **Closing Date:** July 15, 2025 (day of closing allocated to Buyer)
- **Purchase Price:** $3,900,000.00
- **New Loan (Tidewater Savings Bank):** $2,640,000.00

## Headline figures (reconciled to $0.00)
- **Net proceeds to Seller:** $2,864,663.83
- **Cash required from Buyer at closing:** $1,085,412.12
- **Total funds received = disbursed:** $3,920,412.12

## Proration schedules included
1. **Real property tax** — delinquent FY2024-25 2nd installment + interest ($28,602.80, Seller payoff) and next-FY 2025-26 estimate prorated 14/351 days ($2,012.93 debit Seller / credit Buyer)
2. **Collected rents** — per-unit breakdown of July 2025 collected rents ($23,600), split 14/17 days; delinquent Unit 2E and vacant Unit 3C excluded per PSA §7.3
3. **Security deposits** — all 12 deposits ($32,400.00) transferred Seller→Buyer
4. **Water/sewer (WPCA)** — $1,847.60, 100% Seller (billing period ends before closing)
5. **Heating oil** — 180 gal × $3.85 = $693.00 (debit Buyer / credit Seller)

## Key discrepancies flagged in the notes memo
- **D-1 (MATERIAL):** Conveyance tax — title commitment estimates $44,750 total, which does not reconcile to the statutory non-residential rate (1.25% state + 0.5% municipal = 1.75% = $68,250). Used the commitment estimate on the statement; flagged for confirmation on Form OP-236.
- **D-2 (MODERATE):** Lender commitment states ~4.5 years remaining on the commercial lease; actual is ~5.5 years (expires 12/31/2030).
- **D-3 (MODERATE):** LTV stated as 67.7% "based on appraised value" but the figure matches purchase-price basis; internal inconsistency.
- **D-4 (MODERATE):** Title underwriter named both "Continental Fidelity" and "Continental Hartleigh" in the same commitment.
- **D-5 (MODERATE):** Three different addresses for the closing agent across documents — verify wire instructions.
- Plus 10 confirmation items (earnest-money interest, security-deposit interest, gas/electric prorations, updated rent roll, payoff recency, FIRPTA certification, repair-escrow adequacy, etc.)

## Validation
Both `.docx` files pass ECMA-376 schema validation (`skills/docx/scripts/validate.py`).