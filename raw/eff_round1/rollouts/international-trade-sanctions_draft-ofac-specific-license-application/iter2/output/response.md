# Deliverables Summary

## Task
Draft an OFAC specific license application package and an internal issues memo from the attached source documents.

## Source documents reviewed
- `client-email-transaction-summary.eml` — Meridian GC's transaction brain-dump (June 24, 2024)
- `compliance-screening-memo.docx` — Peggy Dunleavy's screening memo (June 10, 2024); flagged two SDN matches
- `dcuh-purchase-order.docx` — PO-DCUH-2024-0743 (June 17, 2024)
- `graystone-audit-summary.docx` — Sept 2023 compliance audit, "Satisfactory with Recommendations"
- `prior-ofac-license-syr-2021.docx` — prior specific license (TB kits to Al-Mujtahid Hospital)
- `product-technical-datasheets.docx` — RX-700 and CalibPro 3100 specs (TDS-2024-0347)
- `shipping-logistics-plan.docx` — Pinnacle 5-leg route plan (June 25, 2024)
- `who-syria-needs-assessment.docx` — WHO Syria HNA §4.7 oncology/cancer diagnostics (Jan 2024)

## Deliverables (in `output/`)

### 1. `ofac-specific-license-application.docx`
A formal specific-license application to OFAC's Licensing Division under E.O. 13582 and 31 C.F.R. Part 542, structured as a filing package with 15 sections plus signature block:
- Applicant/representative info; requested authorization and Sept 1, 2024–Feb 28, 2026 term
- Transaction description ($1,280,000: 500 RX-700 kits, 4 CalibPro 3100 units, 40 hrs remote training)
- Full party table with screening results
- Goods/services detail with EAR99/HTS classifications and firmware/encryption notes
- End-user/end-use (DCUH, governmental instrumentality) with end-use monitoring commitment
- 5-leg shipping route and cold-chain protocol
- **Dedicated disclosure section** for the two SDN issues (Khoury/ARMPC 30% ownership with 50%-Rule analysis and substitution/limited-role mitigation; Central Bank of Calverley payment restructuring to a non-SDN institution)
- Humanitarian justification grounded in the WHO assessment
- Prior-license precedent (SYR-2021-384712) and compliance-program description
- Proposed license conditions and exhibit list (A–I)

### 2. `issues-memorandum.docx`
A privileged attorney work-product memo from Ashford & Whitmore (Bellingham/Osei-Mensah) to Meridian's GC, analyzing 10 issues with analysis and recommendations:
1. Specific license required (no general license covers a commercial sale to a governmental end-user)
2. SDN 30% shareholder of ARMPC (Khoury) — 50% Rule, disclosure, substitution vs. limited-role options
3. SDN remitting bank (Central Bank of Calverley) — payment restructuring
4. Remote training — "services to Syria" prohibition and technology-transfer scope
5. End-use monitoring / diversion risk on the in-country leg
6. Encryption/firmware EAR99 classification confirmation
7. Re-screening and material-change obligations
8. Reporting and recordkeeping conditions
9. Timing vs. the Sept 1, 2024 target (90–180 day OFAC processing)
10. Cold-chain feasibility (operational note)
Plus a recommended application strategy, an open-items/next-steps table, and conclusion.

## Method
Authored both as markdown, converted to .docx via the docx skill's Pandoc generator, and validated with `validate.py` (ZIP integrity, XML well-formedness, relationship consistency — both pass).

## Key judgment calls
- Treated the two SDN findings (Khoury/ARMPC and Central Bank of Calverley) as the central issues and addressed them in both documents: full disclosure plus mitigation in the application; options analysis in the memo.
- Recommended substituting ARMPC with a sanctions-clean agent as the primary path, with limited-role authorization as a fallback.
- Recommended restructuring payment away from CBS to a non-SDN institution, citing the prior license's identical prohibition.
- Scoped the training services as operation/maintenance-level only (no controlled technology, no firmware updates under the license).
- Avoided citing specific general-license subsection numbers where uncertain; stated generally that no existing general license covers this commercial transaction.