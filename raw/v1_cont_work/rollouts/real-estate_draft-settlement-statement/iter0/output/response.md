# Settlement Statement Preparation — Summary

## Task
Prepare a settlement statement for the commercial property closing at 4280 Harborview Boulevard, Bridgeport, CT, with full proration schedules and a reconciliation summary, plus a notes memo flagging discrepancies and assumptions.

## Deliverables (in `output/`)
1. **`settlement-statement.docx`** — full commercial settlement statement
2. **`settlement-statement-notes.docx`** — notes memo flagging discrepancies & assumptions

Both files passed schema validation (`validate.py`, exit 0).

## Source documents reviewed
Purchase & Sale Agreement, Title Commitment, Rent Roll & Security Deposits (xlsx), Bridgeport Tax Lien Statement, Lender Commitment Letter, Lien Payoff Letters, Utility Account Summary, Management Agreement & Termination Notice, Pre-Closing Inspection Report, and Probate Fiduciary Certificate.

## Settlement statement structure
- **Transaction Summary** — property, parties, lender, price, loan, earnest money
- **Part I — Buyer's Transaction** — debits ($3,967,767.00), credits ($2,884,202.48), **cash to close $1,083,564.52**
- **Part II — Seller's Transaction** — credits ($3,900,693.00), debits/payoffs ($1,036,029.17), **net proceeds $2,864,663.83**
- **Part III — Proration Schedules** (A–E):
  - A: Real property tax (delinquent payoff $28,602.80 + next-FY proration $2,012.93 Seller / $50,467.07 Buyer)
  - B: Rent proration — per-unit, 14/31 Seller vs 17/31 Buyer; Unit 2E (delinquent) & 3C (vacant) excluded → net $12,941.95 credit to Buyer
  - C: Security deposits — $32,400.00 transferred (11 residential + 1 commercial)
  - D: Water/sewer — $1,847.60, 100% Seller (period ends before closing), credited to Buyer
  - E: Heating oil — 180 gal × $3.85 = $693.00, credit to Seller
- **Part IV — Reconciliation** — Funds In = Funds Out = **$3,918,564.52** (balances to $0.00)
- **Part V — Disbursement Summary** — 21 payees
- **POC disclosure** — $4,500 appraisal fee (excluded from cash-to-close per lender instructions)
- Signature block for Seller, Buyer, and Closing Agent

## Key figures (verified to reconcile exactly)
| Item | Amount |
|---|---|
| Purchase Price | $3,900,000.00 |
| New Loan | $2,640,000.00 |
| Earnest Money | $195,000.00 |
| Buyer Cash to Close | $1,083,564.52 |
| Seller Net Proceeds | $2,864,663.83 |
| Total Lien Payoffs | $866,631.89 |
| Repair Escrow Holdback | $45,000.00 |
| **Total Funds In = Out** | **$3,918,564.52** |

## Notes memo highlights
- **6 discrepancies** (D-1 to D-6): title commitment number/date mismatch, insurer name inconsistency, water/sewer payoff-vs-proration treatment, conveyance-tax statutory-vs-contractual split, address variations, recording volume/page cross-references
- **7 assumptions** (A-1 to A-7): unquantified earnest-money interest, unquantified residential deposit interest, estimated next-FY tax, estimated conveyance tax, payoff good-through window, per-lease rent rounding, repair-escrow treatment
- **10 pre-closing confirmations**: survey, Phase I ESA, insurance, SNDA, personal guaranty, FIRPTA certification, probate recency, CT DRS lien release, additional assignment-of-rents recording fee, flood determination
- **6 post-closing follow-ups** and **6 surviving-obligation/risk flags**
- Summary table of potential financial adjustments, with a balance-confirmation callout