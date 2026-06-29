# Summary of Work

## Deliverables (in `output/`)

1. **`draft-form-s1.docx`** — A draft Form S-1 registration statement for the proposed IPO of Crestline Software, Inc. (Nasdaq: CRST), prepared from the eight source documents.
2. **`issues-memorandum.docx`** — A privileged issues memorandum flagging the inconsistencies, disclosure gaps, and risks found across the source documents.

Both files were generated via Pandoc and passed the docx schema/integrity validator.

## Approach

- Read all eight source documents (CFO IPO readiness memo, underwriting term sheet, audited financial statements FY2023–2024, term loan summary, charter & bylaws, D&O questionnaire responses, equity plan workbook, and the draft roadshow deck).
- Treated the **audited financial statements as the authoritative source** for all financial figures; where other documents conflicted, the audited figures control and the conflict is flagged in the issues memo.
- Drafted the S-1 with the full Form S-1 structure: cover page/face page, prospectus summary, risk factors, forward-looking statements, use of proceeds, dilution, selling security holders (none — all primary), plan of distribution, description of securities, named experts, MD&A, market risk, directors/officers/governance, executive compensation, security ownership, related-party transactions, description of capital stock, material changes, financial statements, and Part II (indemnification, recent sales, exhibits, undertakings, signatures).

## Key decisions reflected in the S-1 draft

- **Adjusted EBITDA** presented on a corrected, footing basis: **$20.5M (FY2024)** and **$3.5M (FY2023)**, using audited components (the source documents stated $22.8M and $7.6M, which do not foot and use incorrect components).
- **FY2023 revenue split** uses the audited figures (subscription $116.4M / professional services $12.5M), not the CFO memo's split.
- **CTO name** uses "Katerina 'Kate' Litvak" (consistent with the Restated Certificate, the governing document); the Litvak/Litvanova conflict is flagged.
- **Board** reflects seven directors (per the Restated Certificate), with the CTO as a Class III director; the 6-vs-7 conflict is flagged.
- **Lender** uses "Kestridge West Credit Partners"; the "Silicon Valley Credit Partners"/"SVCP" conflict is flagged.
- **Post-IPO beneficial ownership** table rebuilt on a single consistent basis (basic shares + a separate voting-power column).

## Highlights of the issues memorandum

36 open items, categorized by severity, including:
- **High-severity:** Adjusted EBITDA does not foot (FY2024) and uses wrong components (FY2023); FY2023 revenue split conflict; professional services is described as "high-margin" but is actually −0.5% gross margin; CTO surname conflict (Litvak vs. Litvanova); director first-name mismatch in the equity plan workbook; "Sandra Chen" title conflict (GC vs. CRO) and General Counsel identity; board size / CTO directorship conflict; no Board resolution on the controlled-company exemption; Vantara related-party disclosure inconsistency; 409A valuation history inconsistent between the audited financials and the equity plan workbook; equity plan 409A tab references wrong preferred-stock financing terms.
- **Medium:** post-IPO ownership table inconsistent denominators; use-of-proceeds allocation differs across documents; term loan date/draw history and amortization schedule conflicts; lender and transfer-agent name conflicts; Ridgeline fund name; lock-up must bind fund entities; Section 382/NOL study not completed.
- **Disclosure/risk items:** dual-class has no sunset; federal forum selection; RSU double-trigger liquidity condition; cheap-stock/409A grant-pricing risk; preferred stock redemption right if IPO delayed; secured indebtedness over IP; Optivance litigation + $5M term-loan default trigger; 30-day lender IPO-notice obligation; customer/geographic concentration.

A consolidated open-items table and a list of 16 risk factors to confirm in the S-1 are included, along with recommended next steps for the CFO, General Counsel, outside counsel, and auditor.