# Plaintiff's First Set of Interrogatories to Defendant Veridian Health Systems, LLC

**Deliverable:** `first-set-interrogatories-to-veridian.docx`

## Task

Draft a first set of interrogatories from Plaintiff Castillo Medical Technologies, Inc. ("CMT") to Defendant Veridian Health Systems, LLC ("Veridian") in *Castillo Medical Technologies, Inc. v. Oshiro et al.*, No. 1:24-cv-03841-RLH (W.D. Tex. Austin Div.) (Hon. Rebecca L. Hightower).

## Source records reviewed

- First Amended Complaint (operative pleading; four counts — DTSA, TUTSA, breach of NDA, tortious interference)
- Oshiro NDA (March 5, 2018) — 24-month non-disclosure, 18-month non-solicitation, 12-month invention assignment, no non-compete
- Scheduling Order (Sept. 4, 2024) — governs discovery
- TRO Order (Aug. 2, 2024) — narrowed injunction to SynapticEdge neural-mapping feature; directed Veridian to address SynapticEdge development history
- Ashcroft Digital Forensics Report (May 15, 2024) — ~4,700 files / 38.4 GB to USB drive CX-8827491; log-deletion attempt
- Yilmaz Preliminary Expert Report (Aug. 20, 2024) — five technical overlaps
- Veridian press releases (SynapticEdge, June 11, 2024; Oshiro hiring, March 18, 2024)
- Litigation hold letter (June 28, 2024)
- CMT internal emails (Feb. 2024) — solicitation reports

## Key constraints applied

- **25-interrogatory cap, including discrete subparts** (Scheduling Order § II.B.1). The set uses exactly 25 interrogatories; every subpart is a logically/factually related component of a single unified inquiry on the same subject matter, as the Order requires. An instruction (No. 7) flags this compliance.
- **Proportionality / relevance to the three identified trade secrets** (NeuralPath Algorithm, PrecisionDrive System, PathPlanner Module) (Scheduling Order § II.B.3; Fed. R. Civ. P. 26(b)(1)). Each interrogatory is tied to a claim, defense, or specifically alleged fact.
- **Service deadline Jan. 2, 2025; responses due 30 days after service** (Fed. R. Civ. P. 33(b)(2)). Set is dated Nov. 1, 2024 (within the discovery window opened by the Scheduling Order and after the protective-order/ESI-protocol deadlines).

## Coverage (25 interrogatories)

| # | Topic | Grounded in |
|---|---|---|
| 1 | Corporate structure / members / officers (diversity) | Complaint ¶¶ 17–19 |
| 2 | Recruitment of Oshiro (Trent's Dec. 3, 2023 LinkedIn message; CMT-tech discussions) | Complaint ¶¶ 42–45 |
| 3 | Knowledge of Oshiro's CMT role, trade-secret access, and NDA obligations | Complaint ¶ 50 |
| 4 | Oshiro's Veridian employment terms (compensation premium) | Complaint ¶ 49 |
| 5 | USB Drive CX-8827491 — possession, connection to Veridian systems, current location | Ashcroft Report; TRO Order § V.B |
| 6 | CMT files/materials in Veridian's possession | Ashcroft Report |
| 7 | SynapticEdge development history/timeline (commencement, five features, personnel, sources) | TRO Order § V.D directive; press release |
| 8 | Use/incorporation of CMT trade secrets in SynapticEdge | Complaint ¶ 68; Yilmaz Report |
| 9 | Independent-development / "in development prior to Oshiro" contention | TRO Order (Veridian's Aug. 1 representation) |
| 10 | Oshiro's specific contributions to SynapticEdge | TRO Order § V.D(iv) |
| 11 | Contentions re: five Yilmaz technical overlaps | Yilmaz Report § VI |
| 12 | Information barriers / clean-room / screening protocols | Litigation hold letter § 4.5 |
| 13 | Onboarding/screening of hires from competitors | Complaint ¶ 50; hold letter § 4.2 |
| 14 | Recruitment of Furukawa, Briggs, Moreno (Oshiro's role; knowledge of non-solicitation) | Complaint ¶¶ 69–72 |
| 15 | Commercialization of SynapticEdge (customers, revenue, regulatory) | Press release |
| 16 | Communications with CMT hospital customers | Complaint ¶¶ 75(a), 103–105 |
| 17 | $60M Series C / Thorncastle / total funding | Complaint ¶ 67; press release |
| 18 | Unjust enrichment / financial benefit / avoided R&D | Complaint Prayer; TUTSA § 134A.004 |
| 19 | Litigation hold / preservation / any spoliation since June 28, 2024 | Hold letter; TRO Order § V.B; Scheduling Order § VI |
| 20 | Trade-secret-status contention (DTSA/TUTSA) | Counts I–II |
| 21 | Willful-and-malicious contention | Complaint ¶¶ 77, 86; 18 U.S.C. § 1836(b)(3)(C) |
| 22 | Tortious-interference element contentions | Count IV |
| 23 | Damages contention ($82M breakdown) | Complaint ¶¶ 75–76 |
| 24 | Persons with knowledge | — |
| 25 | Expert witnesses (FRE 702/703/705) | — |

## Form features

- Full federal caption (case no., judge, jury demand), title, and introductory paragraph citing Rules 26/33 and the Scheduling Order.
- General Instructions (continuing obligation, full answers, objections, privilege log, scope, supporting persons/documents, subpart compliance, proportionality, protective order, defined terms).
- Definitions (A–Q) for all key terms, including "Identify" for persons/documents/communications.
- Signature block for Hargrove, Pell & Sutton LLP (Hargrove / Nakamura) and a Certificate of Service on Veridian's counsel (Stephen Osei, Drummond & Wakefield LLP) and Oshiro's counsel (Patricia Dominguez, Barlow & Crane PLLC).

## Validation

`skills/docx/scripts/validate.py` → **OK, valid** (ZIP integrity, XML well-formedness, content-type registration, relationship consistency). Dollar amounts and signature lines render as literal characters (no stray escape artifacts).