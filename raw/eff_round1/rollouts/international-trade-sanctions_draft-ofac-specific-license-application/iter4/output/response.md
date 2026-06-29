# Deliverables Summary

## Task
Draft an OFAC specific license application package and an internal issues memo from the attached source documents.

## Source documents reviewed
- `client-email-transaction-summary.eml` — Jon Halsted (Meridian GC) brain dump to Ashford & Whitmore (June 24, 2024)
- `compliance-screening-memo.docx` — Peggy Dunleavy CCO screening memo (June 10, 2024)
- `dcuh-purchase-order.docx` — DCUH PO-DCUH-2024-0743 (June 17, 2024)
- `graystone-audit-summary.docx` — Graystone Compliance Partners audit (Sept 29, 2023)
- `prior-ofac-license-syr-2021.docx` — Prior Specific License SYR-2021-384712
- `product-technical-datasheets.docx` — TDS-2024-0347 (RX-700, CalibPro 3100, training)
- `shipping-logistics-plan.docx` — Pinnacle Freight logistics plan (June 25, 2024)
- `who-syria-needs-assessment.docx` — WHO Syria HNA 2024, Section 4.7

## Deliverables (in `output/`)

### 1. `ofac-specific-license-application.docx`
A formal specific license application to OFAC's Licensing Division, drafted on Ashford & Whitmore LLP letterhead on behalf of Meridian Biotech Solutions, Inc., under E.O. 13582 and 31 C.F.R. Part 542. Contains 15 numbered sections: applicant information; transaction description; goods/services (RX-700 kits, CalibPro 3100 units, remote training; $1,280,000 total); end-user/end-use (DCUH); humanitarian justification (WHO assessment); parties & screening table; shipping route (5-leg, cold-chain); payment terms; full disclosure of the two SDN matters with mitigation; prior license history (SYR-2021-384712); compliance program (Graystone audit); export classification; requested license terms/conditions (Sept 1, 2024 – Feb 28, 2026); certifications; and an exhibits list (A–I).

### 2. `issues-memorandum.docx`
A privileged attorney work-product memo from Ashford & Whitmore (Bellingham/Osei-Mensah) to Meridian's GC, dated June 28, 2024. Analyzes nine issues: (1) authorization framework / specific license required; (2) SDN-adjacent customs agent ARMPC/Khoury (50 Percent Rule, indirect-benefit risk, removal recommendation); (3) SDN-listed remitting bank CBS (restructure to non-SDN bank per prior-license precedent); (4) product classification, technology transfer, deemed exports, firmware scope; (5) transaction structure/intermediaries/routing (contrast with prior license's no-intermediary condition; Bab al-Hawa routing); (6) end-use monitoring/diversion (Graystone Finding 2); (7) license scope/term/conditions; (8) timing/processing risk; (9) ongoing re-screening. Includes an executive summary, an action-items table, and an open-information-requests list.

## Key analytical positions reflected in both documents
- **Specific license required** — transaction prohibited under 31 C.F.R. §§ 542.201 and 542.211 (DCUH is an instrumentality of the Government of Syria); no general license covers a commercial sale to a governmental end-user with SDN-adjacent parties.
- **ARMPC/Khoury** — Khoury (30% shareholder, SDN-designated April 15, 2024 for a military procurement network) is below the 50 Percent Rule threshold, but indirect-benefit risk and the designation basis warrant **removal of ARMPC** and substitution of a pre-cleared agent, with full disclosure.
- **CBS payment** — SDN-listed since Aug 10, 2011; **restructure payment through a non-SDN Syrian commercial bank**, mirroring the express prohibition on CBS routing in prior license SYR-2021-384712.
- **Firmware** — license limited to factory firmware v4.2.1; updates excluded as separate transactions.
- **End-use monitoring & re-screening** — incorporated as proposed conditions/undertakings, addressing Graystone Findings 1 and 2.

## Method
Both documents were authored in markdown and converted to .docx via the docx skill's `generate_from_md.py` (Pandoc). Both passed `validate.py` (ZIP integrity, XML well-formedness, content-type and relationship consistency). Intermediate markdown files were removed; the output directory contains only the two .docx deliverables.