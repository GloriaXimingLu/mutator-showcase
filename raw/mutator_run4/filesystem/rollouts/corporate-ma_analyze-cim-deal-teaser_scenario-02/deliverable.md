# Buy-Side CIM Analysis — Summary of Work

## Deliverable
`buy-side-cim-analysis-memo.docx` — a 25-page buy-side analysis memorandum prepared for the Thornfield Capital Partners deal team (Marcus Yuen, Diane Holbrook) on Cascade Environmental Solutions, Inc. ("CES"), in connection with the Greenleaf Advisory Group sale process (IOI deadline July 14, 2025).

## Materials reviewed
- `cascade-cim.docx` — Confidential Information Memorandum (June 9, 2025)
- `ces-financial-exhibits.xlsx` — Income Statement, Balance Sheet, Cash Flow, EBITDA Bridge, Revenue by Segment, Capex Schedule
- `ces-customer-backlog-report.docx` — Customer Summary & Backlog Report
- `greenleaf-process-letter.docx` — Process letter
- `thornfield-sector-memo.docx` — Internal sector memo (benchmarks from GreenWorks & Allied Waste portfolio companies)

## Recommendation in the memo
**Proceed with a conditional IOI at a disciplined valuation.** Recommended enterprise-value range **$130M–$150M** (cash-free, debt-free, normalized NWC) vs. the sell-side guide of $136.8M–$171.0M, with an earnout tied to PFAS revenue and PNR contract renewal, and explicit conditions to a binding bid (QoE, PNR renewal confirmation, PFAS backlog breakout, fleet/capex assessment, 10-year regulatory history, HQ real-estate resolution).

## Key findings driving the valuation gap
1. **Adjusted EBITDA does not foot** — the six stated adjustments sum to $4.7M, so $12.1M reported + $4.7M = $16.8M, not the $17.1M presented (a $0.3M arithmetic error; $2.4M–$3.0M of EV).
2. **Related-party lease add-back contradicted by the CIM's own market data** — the $0.8M add-back assumes $0.6M market rent, but the CIM's Industry Overview states comparable specialized facilities command $1.0M–$1.2M; defensible add-back is $0.2M–$0.4M.
3. **Regulatory/legal add-back treats a recurring cost as one-time** — full $1.2M DEQ add-back vs. a $0.2M–$0.5M recurring run-rate (per sector benchmarks and Thornfield portfolio experience); defensible $0.7M–$0.9M.
4. **Buy-side normalized FY2024 Adjusted EBITDA ≈ $15.9M** (vs. $17.1M); conservative case ≈ $14.5M–$15.0M.
5. **Largest customer MSA already expired** — PNR (21.4% of revenue) MSA expired March 31, 2025, before the CIM was distributed; renewal undisclosed.
6. **Growth story is a PFAS story** — ex-PFAS, traditional remediation grows only 1.2%/3.5%/5.7%; PFAS is ~64% of incremental revenue and the entire margin-expansion thesis; CIM projects +125.8% PFAS growth vs. a 30%–50% achievable company-level rate; no PFAS-specific backlog breakout provided; PE capacity down to two.
7. **Financial exhibits do not reconcile to the CIM or to themselves** — gross profit, operating income, net income, cash, PP&E, goodwill ($2.5M unexplained), total assets, and equity all differ; the exhibits' P&L implies EBITDA of ~$11.1M, not the $12.1M that anchors the bridge.
8. **Capex/FCF and working-capital quality** — maintenance capex at 3.4% of revenue is below the 5%–7% sector floor; FCF is thin (~$2.0M); stated 52-day DSO does not reconcile to the balance sheet (~65–71 days).
9. **Customer disclosure inconsistency** — the CIM and the Backlog Report name entirely different customers for top-10 positions #6–#10 (same revenue figures).
10. **Fund fit** — implied EV is above Fund III's $30M–$100M target range; equity check ~$80M–$95M (~19%–22% of the $425M fund), warranting an IC discussion of mandate/concentration/co-investment.

## How the document was produced
- Authored as structured markdown; converted to .docx via Pandoc with a custom styled reference template (navy heading scheme, Calibri body).
- Post-processed with python-docx: confidentiality header, page-numbered footer, title/subtitle emphasis, and all 10 data tables restyled with navy header rows, alternating row shading, repeated header rows, and content-proportional fixed column widths.
- Validated with `skills/docx/scripts/validate.py` (ZIP integrity, XML well-formedness, relationship consistency — exit 0).
- Visual QA via PDF render: confirmed full-width text rendering and no table overflow across title, body, and appendix pages (text bounding box 10%–90% of page width, matching the 0.85" margins).