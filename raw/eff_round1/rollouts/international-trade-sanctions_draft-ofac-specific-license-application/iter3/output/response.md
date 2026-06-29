# Deliverables Summary

## Task
Draft an OFAC specific license application package and an internal issues memo from the attached source documents.

## Source documents reviewed
- `client-email-transaction-summary.eml` — Jon Halsted's June 24, 2024 brain-dump to outside counsel
- `compliance-screening-memo.docx` — Peggy Dunleavy's June 10, 2024 screening memo (flagged the two SDN issues)
- `dcuh-purchase-order.docx` — PO-DCUH-2024-0743 (June 17, 2024)
- `graystone-audit-summary.docx` — Sept 29, 2023 compliance audit ("Satisfactory with Recommendations")
- `prior-ofac-license-syr-2021.docx` — prior specific license (issued Sept 14, 2021; expired Mar 31, 2023)
- `product-technical-datasheets.docx` — TDS-2024-0347 (RX-700, CalibPro 3100, training curriculum)
- `shipping-logistics-plan.docx` — Pinnacle's June 25, 2024 five-leg route plan
- `who-syria-needs-assessment.docx` — WHO Syria 2024 Update, §4.7 oncology/cancer diagnostics

## Deliverables (in `output/`)

### 1. `ofac-specific-license-application.docx`
A complete specific-license application package to OFAC's Licensing Division under 31 C.F.R. Part 542 / E.O. 13582, submitted by Ashford & Whitmore LLP on behalf of Meridian Biotech Solutions, Inc. Structure:
- Part I — Transmittal/cover letter
- Part II — Applicant information (EIN 47-3928104; DUNS 08-471-3920)
- Part III — Summary of requested authorization (18-month term; effective upon issuance through Feb 28, 2026)
- Part IV — Description of goods/services (RX-700 kits, CalibPro 3100 units, remote training; $1,280,000 total)
- Part V — End-user (DCUH) and end-use; governmental-instrumentality disclosure
- Part VI — All parties + screening-results table
- Part VII — Payment terms and the Central Bank of Calverley SDN issue + proposed restructure
- Part VIII — ARMPC/Khoury SDN issue + 50% Rule analysis + proposed substitution (with alternative request)
- Part IX — Prior license history (SYR-2021-384712)
- Part X — Shipping route and logistics (5 legs; cold-chain)
- Part XI — Humanitarian justification (WHO assessment)
- Part XII — Compliance program, end-use monitoring plan, proposed license conditions
- Part XIII — Exhibits A–I
- Certification block

### 2. `issues-memorandum.docx`
Privileged attorney work-product memo from Ashford & Whitmore (Bellingham/Osei-Mensah) to Meridian's GC and CCO analyzing the legal issues. Structure:
- I. Executive summary (two principal restructuring items flagged)
- II. Background/transaction summary
- III. Legal framework (SSR, E.O. 13582, 50% Rule, EAR, § 501.601)
- IV. Issue 1 — Governmental end-user (DCUH/Ministry of Health)
- V. Issue 2 — Parallel BIS authorization under the EAR Syria embargo
- VI. Issue 3 — Technology transfer / deemed export / firmware scope
- VII. Issue 4 — SDN remitting bank (Central Bank of Calverley)
- VIII. Issue 5 — SDN minority shareholder in customs agent (ARMPC/Khoury)
- IX. Issue 6 — Border crossing/routing and diversion diligence
- X. Issue 7 — License term/timing (Sept 1 target likely unachievable)
- XI. Issue 8 — Reporting, recordkeeping, re-screening
- XII. Risk assessment (Moderate, trending favorable) + priority action items
- XIII. Next steps

## Key analytical points captured
- **Two material SDN problems** disclosed and restructured in the application: (1) Central Bank of Calverley (SDN since 8/10/2011) as remitting bank → replaced with a non-SDN institution subject to pre-payment screening; (2) Samir Daoud Khoury (SDN 4/15/2024, "military procurement network") as 30% shareholder of customs agent ARMPC → ARMPC removed and a clean substitute agent required (50% Rule analysis: ARMPC not auto-blocked at 30%, but disclosure + removal recommended).
- **Governmental end-user** (DCUH = instrumentality of GoS under E.O. 13582) requires a specific license; no general license reaches it.
- **Parallel BIS authorization** likely required under the EAR Syria embargo (15 C.F.R. Part 746) even for EAR99 items — flagged as a parallel action item.
- **Technology-transfer/deemed-export** risk from the remote training (proprietary schematics, 287-page software reference manual) and firmware-update scope — addressed in application scoping.
- **License timing**: Sept 1, 2024 effective date likely unachievable given 90–180 day OFAC processing; requested effective-upon-issuance with 18-month window.
- **End-use monitoring, re-screening (90-day), reporting, and recordkeeping** conditions proposed consistent with the prior license and Graystone audit recommendations.

## Validation
Both `.docx` files passed `skills/docx/scripts/validate.py` (ECMA-376 schema validation, ZIP integrity, content-type registration, relationship consistency) with exit code 0. Tables (12 in the application, 1 in the memo) and heading hierarchy rendered correctly via pandoc.