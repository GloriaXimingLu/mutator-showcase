# Settlement Statement Package — 4280 Harborview Boulevard, Bridgeport, CT

## Deliverables (in `output/`)
- **`settlement-statement.docx`** — full commercial settlement statement with detailed proration schedules and a funds-flow reconciliation.
- **`settlement-statement-notes.docx`** — closing notes memo flagging discrepancies, assumptions, and items pending confirmation.

Both files were built with `python-docx` and passed the ECMA-376 schema/ZIP validation gate.

## Transaction at a glance
| | |
|---|---|
| Seller | Estate of Gerald T. Whitford (Claudia Whitford-Barnes, Executrix) |
| Buyer | Meridian Cove Properties LLC (Elaine R. Matsuda, Manager) |
| Property | 4280 Harborview Blvd, Bridgeport, CT — Lot 17, Block 42, mixed-use (1 commercial + 12 residential) |
| Closing | July 15, 2025 (closing day allocated to Buyer; 365-day proration year) |
| Purchase Price | $3,900,000.00 |
| Loan | $2,640,000.00 — Tidewater Savings Bank (6.875%, 30-yr am., 7-yr balloon) |

## Headline figures (reconciled to the penny)
- **Cash required from Buyer at closing:** $1,083,564.52 (before pending earnest-money interest)
- **Net proceeds to Seller:** $2,864,663.83
- **Total sources of funds = total uses of funds:** $3,918,564.52 (balanced ✓)

## Settlement statement contents
- **Section A** — Summary of transaction (Buyer/Seller two-column)
- **Section B** — Buyer's detailed charges ($3,967,767.00) and credits ($2,884,202.48)
- **Section C** — Seller's amounts due ($3,900,693.00) and deductions ($1,036,029.17)
- **Section D** — Five proration schedules:
  1. Real property taxes — current FY delinquent payoff ($28,602.80) + next-FY estimate (Seller 14 days = $2,012.93)
  2. Rents — per-lease proration of collected July rents (Buyer's share $12,941.95; 2E delinquent & 3C vacant excluded)
  3. Security deposits — $32,400.00 (residential $18,000 + commercial $14,400)
  4. Water/sewer — $1,847.60 (billing period ends before closing → Seller's, credited to Buyer)
  5. Heating oil — 180 gal × $3.85 = $693.00 (credit Seller / debit Buyer)
- **Section E** — Reconciliation summary (sources vs. uses, balances to $0.00)
- **Section F** — POC disclosure (appraisal $4,500, $0 impact on cash-to-close)
- **Section G** — Disbursement/wire summary + signature block

## Notes memo contents
- **Part 1 — Discrepancies (6):** title-commitment number mismatch (PCT-2025-08814 vs TC-2025-07182); title-insurer name inconsistency; mechanic's-lien recording-reference conflict (Vol. 1398/Pg. 77 vs Vol. 1064/Pg. 517); first-mortgage/HELOC recording-reference errors; party address/telephone inconsistencies; lender LTV narrative inconsistency.
- **Part 2 — Assumptions (10):** conveyance tax is an estimate; next-FY tax estimated; no prepaid loan interest/impounds; per-lease rent method; water/sewer as Buyer credit per PSA; repair escrow as Seller holdback; heating-oil gauge-based value; closing on/before 7/20/2025 payoff validity; no brokerage commission; each party bears own attorney fees.
- **Part 3 — Pending confirmation (11):** earnest-money interest; security-deposit interest (CT §47a-21); conveyance-tax finalization; water/sewer disbursement split vs. City's bundled $30,450.40 payoff; uncollected Unit 2E rent; CT DRS lien-release recording; fiduciary/probate certificate; management-agreement termination & deposit transfer; repair-escrow roof adequacy; unquantified lender-required costs (survey, Phase I, SNDA, insurance); final payoff/wire verification.
- **Part 4** — Financial-impact summary of pending items.

## Key methodology notes
- Rents prorated **separately per lease then aggregated** per PSA §7.2(d); the $0.01 difference vs. an aggregate calc is allocated to Buyer per §7.2(c).
- Delinquent FY2024-25 tax ($28,602.80) paid to the City from Seller proceeds; next-FY tax estimated at $52,480 and prorated (Seller 14 days / Buyer 351 days), reproration reserved under §7.7.
- $45,000 repair escrow is a Seller-side holdback (not a Buyer credit, not part of purchase price) per §8.4(c).
- All lien payoffs good through July 20, 2025; no per-diem adjustments applied (closing 7/15/2025).