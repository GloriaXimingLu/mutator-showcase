# Summary of Work

## Deliverables

Two execution-ready Microsoft Word documents have been produced in the output directory and validated for OOXML integrity:

1. **`underwriting-agreement.docx`** — A firm-commitment underwriting agreement for the initial public offering of Meridian Pulse Technologies, Inc., dated March 19, 2025 (Pricing Date), with closing on March 24, 2025.
2. **`issues-memorandum.docx`** — A privileged issues memorandum flagging cross-document discrepancies and open items, prepared from the perspective of Underwriters' Counsel (Ashford & Pine LLP).

## Underwriting Agreement — Structure

The agreement is a complete, execution-ready firm-commitment underwriting instrument among the Company, the three Selling Stockholders (Cascade Kestridge Ventures, LP; Northlight Growth Partners Fund II, LP; and Dr. Anand Krishnamurthy), and the two Underwriters (Hargrove Securities LLC as Representative/Lead Book-Runner at 70%, and Bellweather Capital Markets, Inc. as Co-Manager at 30%). It contains:

- **Article I** — Sale and purchase of 12,000,000 Firm Shares (8,000,000 primary + 4,000,000 secondary) and the 1,800,000-share Over-Allotment Option (Company-only sourcing; 30-day option period expiring April 23, 2025); pricing at $24.00/share (assumed midpoint), 6.0% discount ($1.44/share), $22.56 net.
- **Article II** — 20 Company representations (organization, capitalization, Registration Statement accuracy, financials, no MAC, IP, material contracts, FDA compliance, litigation, tax, FINRA, Nasdaq listing, auditor independence, use of proceeds, etc.).
- **Article III** — 9 Selling Stockholder representations (title, authority, no conflicts, no registration-rights violation, selling-stockholder information, lock-up compliance, FINRA, no brokers).
- **Articles IV–V** — Company and Selling Stockholder covenants (Final Prospectus filing, comfort letter and opinion delivery, use of proceeds/credit-facility prepayment, listing, lock-up compliance).
- **Article VI** — 13 closing conditions (effectiveness, Nasdaq listing, comfort letter, legal opinions, officers'/secretary's certificates, lock-up agreements including the Krishnamurthy springing extension, POAs, questionnaires, no MAC, FINRA clearance, required consents).
- **Articles VII–X** — Closing mechanics, indemnification and contribution (with selling-stockholder and underwriter caps), termination (market-out clauses), and miscellaneous (New York governing law, jury waiver, notices, expenses including the $500,000 non-consummation reimbursement cap).
- **Schedules A–E** — Underwriter allocations, Selling Stockholder shares, form of lock-up, the supplemental springing-extension provision for Dr. Krishnamurthy (Schedule C-1), persons subject to lock-up, and a pricing summary.

Where the source documents conflicted, the agreement adopts reconciled positions (generally favoring the S-1 as the operative disclosure document), with each such choice cross-referenced in the issues memorandum.

## Issues Memorandum — Key Findings

The memorandum identifies **30 issues** ranked by severity (CRITICAL / HIGH / MEDIUM), with a summary table and a pre-execution/pre-closing action checklist. The most significant findings:

- **Credit facility (CRITICAL):** The S-1 and the internal Credit Summary disagree on the lender's identity (Oakvale vs. Ridgemont National Bank), the agreement date (July 15, 2022 vs. June 15, 2023), the maturity (Dec 31, 2026 vs. June 15, 2027), the interest rate (SOFR + 2.50% vs. a 2.25%–3.25% grid), the change-of-control threshold (50% vs. 35%), and the financial covenants. These must be reconciled before execution; if the Credit Summary is correct, the S-1 is materially misstated.
- **Mandatory prepayment (CRITICAL):** The S-1's Risk Factors disclose a ~$15.2M mandatory prepayment, but its Use of Proceeds states only ~$10M — an internal inconsistency understating the obligation by $3.6M–$5.2M.
- **Comfort Letter vs. S-1 (CRITICAL):** The draft Comfort Letter's balance-sheet figures (total equity $198.4M; cash $47.3M; NTBV $4.72/share) do not reconcile with the S-1's Capitalization/Dilution figures (equity $101.4M; cash $38.4M; NTBV $2.17/share).
- **Selling Stockholder identity (CRITICAL):** The general partners, control persons, and addresses for Cascade and Northlight differ across the S-1, the POA, and the Cascade Questionnaire; the POA also misnames Cascade as "Cascade Ridge Ventures, LP."
- **Offering structure (HIGH):** Over-Allotment Option sourcing (Company and/or Selling Stockholders vs. Company only); Dr. Krishnamurthy's share count (500,000 vs. "up to 750,000"); the springing lock-up extension (in the term sheet/POA but absent from the Form Lock-Up and S-1); the early-release threshold; and the "Joint Book-Running Manager" cover-page designation.

Both documents were generated via Pandoc and passed the docx validation gate (ZIP integrity, XML well-formedness, content-type registration, and relationship consistency).