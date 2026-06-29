# Buy-Side CIM Analysis Memo — Summary

**Deliverable:** `output/buy-side-cim-analysis-memo.docx` (validated, ~6,150 words, 11 sections + 2 appendices)

## What I did

Reviewed all five furnished materials for the **Cascade Environmental Solutions, Inc. ("CES")** sale process (Project Cascade, sell-side advisor Greenleaf Advisory Group):

1. `cascade-cim.docx` — the Confidential Information Memorandum
2. `ces-financial-exhibits.xlsx` — the financial model (income statement, balance sheet, cash flow, EBITDA bridge, segment revenue, capex)
3. `ces-customer-backlog-report.docx` — customer concentration, backlog, and pipeline detail
4. `greenleaf-process-letter.docx` — auction process, timeline, and IOI requirements
5. `thornfield-sector-memo.docx` — internal sector context and screening notes (establishes the buyer as Thornfield Capital Partners Fund III and tasks Associate David Koh with this memo by June 25, 2025)

I then authored a comprehensive buy-side CIM analysis memo from David Koh to the deal team (Yuen/Holbrook, cc Lindgren), built on the sector memo's benchmark framework and extended with original quantitative findings.

## Key analytical contributions (beyond restating the CIM)

- **Quality-of-earnings teardown** of the $5.0M Adjusted EBITDA bridge (41% uplift), with a buy-side normalized EBITDA of **~$15.6M (range $15.0M–$16.0M)** vs. the sell-side's $17.1M — quantifying haircuts to owner-comp (declining $700K→$500K replacement assumption), the related-party lease (CIM's own $1.0–1.2M specialized-facility rent contradicts the $600K used), and the DEQ settlement (recurring regulatory run-rate).
- **DSO verification:** CIM claims 52 days; balance sheet implies **~71 days** (~82 days incl. unbilled) — ~$4.5M–$7.2M of extra working capital.
- **CIM vs. Financial Exhibits reconciliation:** flagged material discrepancies in gross profit, operating income, net income, cash, PP&E, total assets, debt, and equity; an internal EBIT→EBITDA model inconsistency; and unexplained $2.5M goodwill.
- **Growth-mix decomposition:** showed ex-PFAS the core business grows only ~3–8%, with PFAS driving 64% of incremental revenue — isolating the single point of failure in the thesis.
- **PNR contract-expiry flag:** largest customer (21.4% of revenue) MSA expired March 31, 2025 — before the CIM was even distributed.
- **Customer-list inconsistencies** between the CIM and the Customer Report (different names for customers #6–#10; conflicting segment attributions and relationship dates; 75/25 vs. 82.3/17.7 geographic split).
- **Valuation:** recommended IOI EV range **$130M–$150M** on buy-side LTM EBITDA at 8.5x–9.5x, with a PFAS-sensitivity table, an indicative equity bridge, and a fund-sizing flag (CES EV exceeds Fund III's stated $30M–$100M platform target; ~22% equity check).
- **Structuring recommendations** (earnout tied to PFAS/PNR, seller rollover, real-estate acquire-vs-lease, phantom-unit cash settlement, retention agreements) and a **20-item Phase II diligence request list**.

## Method

Authored the memo in markdown and converted to .docx via the docx skill's `generate_from_md.py` (Pandoc), then ran the mandatory `validate.py` gate (exit 0 — valid). Em/en-dashes and all pipe-tables rendered correctly as native Word tables.