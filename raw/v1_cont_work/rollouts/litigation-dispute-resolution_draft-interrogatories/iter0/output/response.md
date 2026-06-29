# Plaintiff's First Set of Interrogatories to Defendant Veridian Health Systems, LLC

## Deliverable

`output/first-set-interrogatories-to-veridian.docx` — a complete, court-ready set of interrogatories served by Plaintiff Castillo Medical Technologies, Inc. ("CMT") upon Defendant Veridian Health Systems, LLC ("Veridian") in *Castillo Medical Technologies, Inc. v. Oshiro & Veridian Health Systems, LLC*, No. 1:24-cv-03841-RLH (W.D. Tex. Austin Div., Hon. Rebecca L. Hightower).

## Source materials reviewed

All nine case files in the workspace were read and synthesized:

- **First Amended Complaint** — operative pleading; four counts (DTSA, TUTSA, breach of NDA, tortious interference); $82M actual + up to $164M exemplary damages.
- **Scheduling Order (Sept. 4, 2024)** — governs the interrogatories: **25-interrogatory cap including discrete subparts**; subparts counted separately unless logically/factually related to a single unified inquiry; proportionality focus on the three identified trade secrets; service deadline Jan. 2, 2025; responses due 30 days after service.
- **TRO Order (Aug. 2, 2024)** — granted in part; the Court expressly directed Veridian to address SynapticEdge's development history/timeline at the preliminary-injunction stage.
- **Oshiro NDA (Mar. 5, 2018)** — 24-month non-disclosure, 18-month non-solicitation, invention-assignment; no non-compete.
- **Ashcroft Forensics Report (May 15, 2024)** — ~4,700 files / 38.4 GB exfiltrated to USB drive CX-8827491; attempted log deletion.
- **Yilmaz Preliminary Expert Report (Aug. 20, 2024)** — five areas of technical overlap; "extraordinarily low" probability of independent development.
- **Veridian Press Release (June 11, 2024)** — SynapticEdge announcement; $60M Series C from Thorncastle Ventures.
- **Litigation Hold Letter (June 28, 2024)** — preservation demands to Veridian.
- **CMT Internal Emails (Feb. 2024)** — contemporaneous notes on the VaultDrive audit and solicitation reports.

## How the interrogatories were tailored

The set is directed solely at Veridian (per the file name) and targets the three claims against it — DTSA misappropriation, TUTSA misappropriation, and tortious interference — while probing Veridian's likely defenses (independent development, public-source/reverse-engineering). The 25 interrogatories are organized into seven thematic clusters:

1. **SynapticEdge development & independent-development defense (Nos. 1–6)** — commencement date, personnel, Oshiro's contributions, documentary evidence of independent development, the five overlapping features, and source-code/version-control repositories.
2. **Recruitment & hiring of Oshiro (Nos. 7–11)** — Trent's LinkedIn solicitation, discussions of CMT technology, knowledge of Oshiro's NDA obligations, the compensation premium, and the targeted job posting.
3. **Receipt, possession & use of CMT files/trade secrets (Nos. 12–15)** — the USB drive and CMT Files, use in SynapticEdge, information barriers/clean-room protocols, and Veridian's knowledge of the specific trade secrets.
4. **Recruitment of the Former CMT Engineers (Nos. 16–17)** — Furukawa, Briggs, and Moreno; Oshiro's role; knowledge of non-solicitation obligations; their current assignments.
5. **Commercial exploitation & damages (Nos. 18–20)** — SynapticEdge commercialization/customers/revenue, the Thorncastle Series C representations, and Veridian's prior neurosurgical-robotics products.
6. **Defenses & contentions (Nos. 21–23)** — independent development, public-source/reverse-engineering, and knowledge of improper acquisition.
7. **Preservation & spoliation (Nos. 24–25)** — response to the litigation-hold letter and TRO; current location/status of the USB drive and CMT Files.

## Compliance with the Scheduling Order

- **Exactly 25 interrogatories** (Nos. 1–25), within the Rule 33(a)(1) / Scheduling Order cap.
- **Subparts are logically and factually related** to each primary interrogatory (e.g., No. 5's (a)–(e) all concern the development history of the five overlapping features; No. 16's (a)–(d) all concern the recruitment circumstances of the three engineers), so they count as components of single unified inquiries rather than separate interrogatories.
- **Proportionality**: every interrogatory is tied to the identified trade secrets (NeuralPath Algorithm, PrecisionDrive System, PathPlanner Module) or to the specific claims/defenses, avoiding general business operations or unrelated product lines as the Order cautions.
- **Service date** of November 14, 2024 is before the Jan. 2, 2025 deadline; responses due December 14, 2024, well within the April 30, 2025 discovery close.

## Document features

- Standard federal caption (borderless two-column table), centered bold-underlined title, "TO:" and Rule 33 introductory paragraph.
- Eight **Instructions** (full-answer obligation, document identification, objection particularity, supplementation, privilege-log, protective-order handling).
- Sixteen **Definitions** keyed to the case facts (CMT Trade Secrets, CMT Files, USB Drive, SynapticEdge, Former CMT Engineers, NDA, and the standard "Identify"/"State"/"Document"/"Communication" terms).
- Signature block for Hargrove, Pell & Sutton LLP and a **Certificate of Service** on Veridian's counsel (Stephen Osei, Drummond & Wakefield LLP) with a copy to Oshiro's counsel (Patricia Dominguez, Barlow & Crane PLLC).
- Times New Roman 12pt, 1" margins, justified body, hanging-indent numbered items, and a footer with the case number and "Page X of Y."

## Validation

- `skills/docx/scripts/validate.py` → **valid** (exit 0; ZIP integrity, XML well-formedness, content-type and relationship consistency all pass).
- Rendered to PDF via LibreOffice: 11 pages, letter size; caption, title, footer page numbers, and all sections confirmed present and correctly laid out.