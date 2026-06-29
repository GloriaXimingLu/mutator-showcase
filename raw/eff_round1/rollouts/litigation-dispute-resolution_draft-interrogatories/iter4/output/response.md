# Summary

## Deliverable
`output/first-set-interrogatories-to-veridian.docx` — Plaintiff Castillo Medical Technologies, Inc.'s First Set of Interrogatories to Defendant Veridian Health Systems, LLC.

## What I did
1. Read all nine case files in `documents/` (First Amended Complaint, Scheduling Order, TRO Order, Ashcroft Forensics Report, Yilmaz Expert Report, Oshiro NDA, Veridian press releases, litigation hold letter, and CMT internal emails).
2. Identified the procedural posture and constraints: the Scheduling Order (Sept. 4, 2024) caps each party at **25 interrogatories including all discrete subparts**, with strict subpart counting, a service deadline of Jan. 2, 2025, and a proportionality directive focused on the three identified trade secrets (NeuralPath Algorithm, PrecisionDrive System, PathPlanner Module).
3. Drafted 25 interrogatories tailored to the claims against Veridian (DTSA, TUTSA, and tortious interference), each framed as a single unified inquiry so that any subparts are logically/factually related to the primary question.
4. Authored the document in markdown, generated the .docx via Pandoc (`generate_from_md.py`), and validated it with `validate.py` (exit code 0).

## Document structure
- **Caption** — W.D. Tex., Austin Division; Case No. 1:24-cv-03841-RLH; Hon. Rebecca L. Hightower.
- **Introductory paragraph** — invokes Rules 26/33, the Local Rules, and the Scheduling Order; states the 30-day response deadline.
- **General Instructions** (9) — Rule 33 obligations, duty of reasonable inquiry, incomplete answers, objections, persons supplying information, documents, continuing duty, scope, and the 25-interrogatory certification.
- **Definitions** (24) — defined terms including CMT Trade Secrets, SynapticEdge, NDA, USB Drive (CX-8827491), VaultDrive, CMT Files, the three engineers, Thorncastle Ventures, and the standard "identify" variants for persons/documents/communications.
- **25 Interrogatories** organized by topic:
  - SynapticEdge development timeline & state as of Oshiro's start (Nos. 1–2)
  - Personnel and documentary evidence of pre-Oshiro development (Nos. 3–4) — directly tracks the Court's TRO directives for the PI hearing
  - The five overlapping technical features (No. 5)
  - Oshiro's contributions, duties, and materials brought from CMT (Nos. 6–8)
  - Receipt/use of CMT files and the USB Drive (Nos. 9–10)
  - Knowledge of CMT trade secrets (No. 11)
  - Recruitment of Oshiro, discussions about CMT, knowledge of the NDA, and compensation (Nos. 12–15)
  - Information barriers / clean-room protocols and independent-development contention (Nos. 16–17)
  - Recruitment of Furukawa, Briggs, and Moreno and non-solicitation knowledge (Nos. 18–19)
  - Commercialization, revenues, Series C investor communications (Nos. 20–21)
  - Prior product history / neurosurgical capability (No. 22)
  - Litigation hold and preservation compliance (No. 23)
  - Defenses and unjust-enrichment/profits computation (Nos. 24–25)
- **Signature block** and **Certificate of Service** (served on Stephen Osei for Veridian and Patricia Dominguez for Oshiro).

## Validation
`python skills/docx/scripts/validate.py output/first-set-interrogatories-to-veridian.docx` → **OK: valid** (exit code 0). ZIP integrity, XML well-formedness, content-type registration, and relationship consistency all confirmed.