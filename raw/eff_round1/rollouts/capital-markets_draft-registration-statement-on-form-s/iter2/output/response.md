# Response Summary

## Task
Draft a Form S-1 registration statement for the proposed IPO of Crestline Software, Inc. using the attached source documents, and prepare a memo flagging inconsistencies and risks found.

## Deliverables (in `output/`)
- **`draft-form-s1.docx`** — A draft Form S-1 registration statement (prospectus + Part II) for the proposed IPO of Crestline Software, Inc. (Nasdaq: CRST), prepared by issuer's counsel. Includes cover/summary, risk factors, use of proceeds, dilution, MD&A (with a corrected non-GAAP Adjusted EBITDA reconciliation), business, management, executive compensation, related-party transactions, principal stockholders, description of capital stock, condensed financial statements, underwriting, and Part II signature/exhibit items. Uses `[●]` placeholders for items not yet determined.
- **`issues-memorandum.docx`** — A privileged issues memorandum from Thorncroft & Wexler LLP flagging 37 inconsistencies and risks (16 High, 17 Medium, 4 Low) found across the source documents, with a summary table and recommended actions.

## Source documents reviewed
Audited financial statements (FY2023–2024); CFO IPO readiness memo; amended charter & bylaws; equity plan summary & grants (xlsx); D&O questionnaire responses; term loan summary; underwriting term sheet & lock-up; draft roadshow presentation.

## Key approach
- Used the **audited financial statements as the authoritative source** for all financial figures in the S-1.
- The S-1 reflects **corrected** figures where internal materials contained errors (e.g., Adjusted EBITDA reconciles to $20.5M FY2024 / $3.5M FY2023 using audited inputs, rather than the erroneous $22.8M / $7.6M in the CFO memo and roadshow).
- The issues memorandum documents every discrepancy between the source documents and recommends resolution, prioritized by severity.

## Most significant findings flagged in the memo
1. Adjusted EBITDA reconciliation does not foot ($22.8M stated vs. $20.5M computed); FY2023 add-backs do not match the audited financials.
2. Term loan balance ($40.0M at both year-ends) does not reconcile to the cash flow statement ($5.0M FY2024 repayment, $15.0M FY2023 borrowings).
3. Term loan date (June 2023 vs. Dec 15, 2022) and lender name (Kestridge West vs. Silicon Valley) inconsistent across documents.
4. 409A valuation history and option/RSU activity inconsistent between the audited financials and the equity plan spreadsheet; cheap-stock risk on Q1 2023 grants priced at $9.50 before a $14.20 valuation and $24.00 Series D.
5. Board size inconsistent (charter: 7; only 6 identified); controlled-company exemption not formally elected; dual-class has no sunset.
6. Vantara Logistics related-party relationship omitted from the CFO memo and roadshow; Aldersgate Capital (Series B) ownership unconfirmed.
7. Filing-date / audit-report-date sequencing issue (Note 17 says filed Feb 2025; audit report dated "March __, 2025"; CFO memo targets March 2025).

## Validation
Both `.docx` files passed the docx skill's `validate.py` (ZIP integrity, XML well-formedness, relationship consistency).