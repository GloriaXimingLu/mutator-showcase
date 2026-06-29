# Buy-Side CIM Analysis — Summary of Work

## Deliverable
`output/buy-side-cim-analysis-memo.docx` — a buy-side analysis memo for the Thornfield Capital Partners deal team on Cascade Environmental Solutions, Inc. ("Project Cascade"), prepared ahead of the July 14, 2025 IOI deadline. Validated against ECMA-376 schema (exit 0).

## Sources reviewed
- `cascade-cim.docx` — Confidential Information Memorandum (Greenleaf, June 2025)
- `ces-financial-exhibits.xlsx` — Income Statement, Balance Sheet, Cash Flow, EBITDA Bridge, Revenue by Segment, Capex Schedule
- `ces-customer-backlog-report.docx` — Customer Summary and Backlog Report
- `greenleaf-process-letter.docx` — Process letter / IOI requirements
- `thornfield-sector-memo.docx` — Internal sector memo (Thornfield) providing benchmarks and screening framework

## What the memo covers
1. **Executive summary & recommendation** — proceed to IOI at EV meaningfully below the sell-side guide, with a PFAS-linked earnout and diligence conditions.
2. **Transaction/process overview** — structure, timeline, IOI requirements, key structuring items.
3. **Business & investment thesis** — segments, genuine positives, headline financials.
4. **Financial profile & quality of earnings** — the core finding that ex-PFAS the business grows ~6% (traditional remediation ~3.5% CAGR); a line-by-line defensibility assessment of the $5.0M Adjusted EBITDA bridge; weak FCF conversion (~16% / ~2.1% FCF yield).
5. **Financial inconsistencies across the data room** — CIM vs. Financial Exhibits income-statement, balance-sheet, cash-flow, and segment discrepancies; the Financial Exhibits' internal EBIT/EBITDA/D&A reconciliation failure (~$3.2M gap); unexplained $2.5M goodwill; debt reconciliation; and the CIM vs. Backlog Report disagreement on the identity of 5 of the top-10 customers; DSO, geographic concentration, and "visibility" inconsistencies.
6. **Risk factors** — PFAS projection aggressiveness (125.8% vs. 30–50% sector), PE capacity loss, customer concentration with imminent contract expirations (PNR MSA expired 3/31/2025), key-person/transition risk, maintenance capex understatement (3.4% vs. 5–7% sector), regulatory cost recurrence, related-party real estate, unquantified phantom-unit cash settlement, debt maturity, working capital, and fund-fit/check-size.
7. **Valuation analysis** — sell-side guide ($136.8M–$171.0M trailing; $157.6M–$197.0M forward) vs. buy-side reconstruction (defensible Adj. EBITDA ~$14.5M–$15.5M at 8.0x–9.0x = ~$120M–$135M EV), with EV-to-equity bridge notes and an FCF perspective.
8. **Recommended IOI position** — $120M–$135M EV range, proposed structure (stock purchase, debt refinanced, HQ real-estate resolution, phantom-unit treatment, retention/TSAs), a PFAS earnout, and a prioritized 10-item confirmatory-diligence list.

## Key analytical conclusions
- **Adjusted EBITDA overstated by ~$1.8M–$2.3M** (sell-side $17.1M vs. buy-side ~$15.0M), driven by: regulatory add-back that should be normalized to a recurring run-rate; the Boise relocation reclassified as growth capex; a lease add-back contradicted by the CIM's own specialized-facility market-rent figure ($1.0M–$1.2M vs. the $0.6M used); and an aggressive $0.5M replacement-CEO assumption (projections also assume $0 CEO comp).
- **The growth thesis is a PFAS thesis** — ex-PFAS CAGR is ~6% vs. the headline 12.5%.
- **The data room does not reconcile** — material inconsistencies across all three sell-side documents, including five mismatched top-10 customer identities and a non-reconciling income statement.
- **Recommended IOI: $120M–$135M EV** with a PFAS-linked earnout to bridge toward the sell-side value if execution materializes.

## Production notes
- Generated from markdown via Pandoc with the `tex_math_dollars` extension disabled (the `($M)` patterns in table headers were otherwise being parsed as TeX math delimiters, which merged table columns). Validated with `skills/docx/scripts/validate.py`.