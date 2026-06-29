# Plaintiff's First Set of Interrogatories to Defendant Veridian Health Systems, LLC

## Deliverable
`output/first-set-interrogatories-to-veridian.docx` — a 9-page, court-formatted set of interrogatories propounded by Plaintiff Castillo Medical Technologies, Inc. ("CMT") upon Defendant Veridian Health Systems, LLC. The document passed ECMA-376 schema validation and renders cleanly (verified via PDF render).

## How it was built
- Reviewed all nine case files: the First Amended Complaint, Scheduling Order, TRO Order, Oshiro NDA, Ashcroft forensics report, Yilmaz preliminary expert report, Veridian press release, litigation-hold letter, and CMT internal emails.
- Built the pleading programmatically with `python-docx` for precise control over the court caption (table with § dividers), numbered interrogatories, definitions, signature block, and certificate of service. Times New Roman 12 pt, 1" margins, letter size.
- Validated with `skills/docx/scripts/validate.py` (exit 0) and visually QA'd via a LibreOffice PDF render.

## Key drafting constraints applied
- **25-interrogatory cap (Fed. R. Civ. P. 33(a)(1))**: The Scheduling Order strictly enforces the 25-limit *including discrete subparts*, counting unrelated subparts as separate interrogatories. The set contains exactly 25 interrogatories. Where subparts appear (Nos. 2, 4, 8), they are natural components of a single, unified inquiry (e.g., "for each person, state name, title, dates, and contributions"), so each counts as one.
- **Proportionality (Fed. R. Civ. P. 26(b)(1))**: Every interrogatory is tied to the three identified trade secrets (NeuralPath Algorithm, PrecisionDrive System, PathPlanner Module), the SynapticEdge platform, the recruitment/solicitation facts, or the claims/defenses — not to Veridian's general business or unrelated product lines.
- **Directed to Veridian only**: The claims against Veridian are DTSA misappropriation, TUTSA misappropriation, and tortious interference; the interrogatories target Veridian's knowledge, use, development history, and intent.

## Organization of the 25 interrogatories
| Topic | Nos. | Purpose |
|---|---|---|
| SynapticEdge development / independent-development defense | 1–8 | Development history, personnel, Oshiro's contributions, per-feature origins, independent-development evidence, pre-Oshiro neurosurgical R&D, source-code/version-control systems, team size/structure |
| Knowledge & use of CMT trade secrets / USB drive | 9–13 | CMT files in Veridian's possession, USB drive CX-8827491, use of trade secrets in SynapticEdge, information barriers/clean-room measures, CMT info from non-Oshiro sources |
| Tortious interference — customers | 14 | Hospitals/customers contacted re: SynapticEdge (the 28-hospital licensing disruption) |
| Recruitment & hiring of Oshiro | 15–19 | Full recruitment history, decision-makers, awareness of NDA obligations, compensation rationale, Trent–Oshiro communications |
| Solicitation of CMT engineers | 20–22 | Recruitment of Furukawa/Briggs/Moreno, Oshiro's role, awareness of non-solicitation obligation |
| Damages / financial | 23–24 | SynapticEdge revenue/projections, $60M Thorncastle Series C investment |
| Defenses | 25 | Factual/legal basis for each defense + supporting documents/witnesses |

## Supporting structure
- **Caption**: W.D. Tex. Austin Division, Case No. 1:24-cv-03841-RLH, Hon. Rebecca L. Hightower.
- **Preamble**: Invokes Rules 26 & 33, the Sept. 4, 2024 Scheduling Order, and the 30-day response deadline.
- **Instructions (12)**: Continuing-duty, full-and-fair-answer, identification conventions for documents/persons/communications, objection particularity, and privilege-log requirements.
- **Definitions (A–M)**: CMT, CMT Trade Secrets, Communication, Document, Former CMT Engineers, the three trade secrets, Oshiro, SynapticEdge, USB Drive, VaultDrive, and "You/Veridian."
- **Signature block & certificate of service**: Hargrove, Pell & Sutton LLP (Meg Hargrove / Kevin Nakamura); service on Stephen Osei (Veridian's counsel) and Patricia Dominguez (Oshiro's counsel).