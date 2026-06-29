# Deliverables Summary

## Task
Draft an OFAC specific license application package and an internal issues memo from the attached source documents, output as `ofac-specific-license-application.docx` and `issues-memorandum.docx`.

## Source documents reviewed
- `client-email-transaction-summary.eml` — Halsted (Meridian GC) brain-dump to Ashford & Whitmore (Bellingham / Osei-Mensah), June 24, 2024.
- `compliance-screening-memo.docx` — Dunleavy (Meridian CCO) screening memo, June 10, 2024 (screening completed June 3, 2024). Identifies the two SDN findings.
- `dcuh-purchase-order.docx` — DCUH PO No. PO-DCUH-2024-0743, June 17, 2024.
- `graystone-audit-summary.docx` — Graystone Compliance Partners audit executive summary, Sept 29, 2023.
- `prior-ofac-license-syr-2021.docx` — Prior Specific License SYR-2021-384712, Sept 14, 2021.
- `product-technical-datasheets.docx` — Combined TDS TDS-2024-0347, March 15, 2024.
- `shipping-logistics-plan.docx` — Pinnacle Freight logistics plan, June 25, 2024.
- `who-syria-needs-assessment.docx` — WHO Syria needs assessment, Jan 2024, §4.7.

## Deliverable 1 — `ofac-specific-license-application.docx`
A formal OFAC specific license application on Ashford & Whitmore LLP letterhead, addressed to the Director, OFAC Licensing Division, dated July 8, 2024, requesting a specific license under the Syrian Sanctions Regulations (31 C.F.R. Part 542) / E.O. 13582 / IEEPA for the export of 500 CancerDetect RX-700 Reagent Kits, 4 CalibPro 3100 Calibration Units, and 40 hours of remote training to DCUH (total $1,280,000), with a requested term of Sept 1, 2024 – Feb 28, 2026. Contains 15 numbered sections (applicant info; requested authorization; transaction description; goods/services; end-user/end-use; parties/logistics; payment; full SDN disclosure of the Khoury/ARMPC 30% shareholder and the CBS remitting bank with 50 Percent Rule analysis and mitigation; humanitarian justification anchored to the WHO assessment; compliance program and prior-license track record; requested license conditions; exhibit list A–I; and certification/signature blocks).

## Deliverable 2 — `issues-memorandum.docx`
A privileged internal attorney work-product memorandum from David Osei-Mensah (Senior Associate) to Catherine Bellingham (Partner) and the file, dated July 8, 2024. Contains executive summary; factual background; legal framework (SSR, E.O. 13582, 50 Percent Rule, GL vs. SL, recordkeeping, EAR/Country Group E:1, OFAC Compliance Commitments); issue analysis of seven issues (governmental end-user; ARMPC/Khoury SDN nexus; CBS SDN remitting bank; product classification/firmware encryption/technology transfer; transshipment and Bab al-Hawa route feasibility; compliance program and end-use monitoring; timing/term); recommended application strategy; risk assessment (moderate-to-favorable); client and counsel action items; and open items.

## Key analytical positions taken
- **Specific license required** (not a general license): commercial sale (not donation) to a blocked Government of Syria instrumentality, with SDN nexuses.
- **CBS (SDN remitting bank):** will not be used; propose non-SDN Syrian commercial bank or third-country bank; license conditioned to bar CBS routing — mirroring the prior license's identical condition.
- **ARMPC / Khoury (SDN 30% shareholder):** full disclosure; 50 Percent Rule does not block ARMPC (30% < 50%), but SDN-adjacent risk is material; primary structure substitutes a screened, non-SDN customs clearance agent; alternative request seeks specific authorization for ARMPC's ministerial role only if OFAC requires.
- **Governmental end-user (DCUH / Ministry of Health):** disclosed; authorization requested notwithstanding instrumentality status; precedent from SYR-2021-384712 (Al-Mujtahid Hospital).
- **Technology transfer:** remote training included in OFAC authorization scope; no controlled technology above EAR99; firmware updates treated as separate transactions; encryption-classification analysis to be documented.
- **Bab al-Hawa route feasibility** flagged for client/logistics confirmation.

## Validation
Both .docx files passed `skills/docx/scripts/validate.py` (ZIP integrity, XML well-formedness, ECMA-376 schema validation, content-type registration, relationship consistency). Generated via Pandoc from markdown using a Times New Roman legal-style reference template.