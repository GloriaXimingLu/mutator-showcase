# Buy-Side CIM Analysis Memo — Deliverable Summary

**Output file:** `output/buy-side-cim-analysis-memo.docx` (validated Microsoft Word .docx, 12 sections, 10 tables)

## What I did

Reviewed all five provided documents for the Cascade Environmental Solutions, Inc. ("CES") sell-side process:

1. `cascade-cim.docx` — the Confidential Information Memorandum
2. `greenleaf-process-letter.docx` — the sale-process letter (IOI due July 14, 2025)
3. `ces-customer-backlog-report.docx` — customer/backlog supplement
4. `ces-financial-exhibits.xlsx` — detailed financial exhibits (6 sheets)
5. `thornfield-sector-memo.docx` — internal sector memo directing the buy-side analysis

I then prepared a comprehensive buy-side analysis memo written from the perspective of David Koh (Associate, Thornfield Capital Partners), addressed to the deal team, applying the sector benchmarks and portfolio experience (GreenWorks, Allied Waste) referenced in the internal sector memo.

## Key analytical findings surfaced in the memo

- **Adjusted EBITDA does not foot.** CIM states $17.1M; reported EBITDA ($12.1M) + the six listed adjustments ($4.7M) = $16.8M. The $0.3M arithmetic error is isolated to the FY2024 valuation year (FY21–FY23 reconcile). Confirmed in both the CIM and the financial exhibits.
- **Adjustment quality is weak.** Regulatory/legal add-backs recur every year; the related-party lease normalization uses a $600K market rate the CIM elsewhere contradicts (§IV.C says specialized facilities command $1.0–1.2M); owner comp includes undisclosed "personal expenses"; "non-recurring" items appear in every historical year.
- **PNR contract cliff.** The largest customer (21.4% / $18.7M) is on an MSA that expired March 31, 2025 — before the CIM was distributed and before the IOI deadline. Renewal status undisclosed.
- **DSO does not reconcile.** Stated 52 days vs. ~71 days implied by AR ($16.9M) and revenue ($87.3M); exhibits show ~68–71 days every year.
- **Maintenance capex understated.** 3.4% of revenue vs. 5–7% sector benchmark (and 5.8–6.2% in Thornfield's own portfolio).
- **CIM vs. exhibits data-integrity gaps.** Different income statements (operating income, pre-tax, net income), different balance sheets (total assets $46.1M vs $50.0M), different top-10 customer names (ranks 6–10), different relationship-tenure years, and a different geographic split (75% vs 82.3% OR/WA). Exhibits income statement is internally inconsistent (EBIT + D&A ≠ stated EBITDA).
- **PFAS growth is aggressive and uncontracted.** ~64% of FY24–FY26E incremental revenue relies on a two-year-old service line growing 126%/57% (vs. 30–50% company-level realistic); traditional remediation is essentially flat; PE headcount just fell 3→2.
- **Buy-side normalized Adjusted EBITDA ~$15.9M** (vs. CIM $17.1M), implying an IOI EV range of ~$135–155M (vs. CIM's $136.8–171.0M).

## Recommendation in the memo

Proceed to submit an IOI at ~$135–155M EV with valuation discipline and a prioritized set of 12 confirmatory-diligence conditions, with movement toward the top of the 8–10x sector range contingent on Phase II validation of the PNR renewal, PFAS contracted backlog, management retention, and true maintenance capex.

## How the file was produced

Authored as structured markdown, then converted to .docx via the docx skill's `generate_from_md.py` (Pandoc), and validated with `validate.py` (ZIP integrity, XML well-formedness, relationship consistency — exit 0).