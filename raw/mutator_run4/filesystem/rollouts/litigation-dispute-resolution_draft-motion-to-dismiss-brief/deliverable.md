# Rule 12(b)(6) Motion Package — Work Summary

**Matter:** *Arcadia Health Systems, LLC v. Meridian Cloud Solutions, Inc.*, No. 1:23-cv-00847-CMA (W.D. Tex., Austin Division; Hon. Catherine M. Alvarez)

**Deliverables (all in `output/`, validated against ECMA-376 / OOXML):**

| File | Pages | Purpose |
|---|---|---|
| `motion-to-dismiss.docx` | 25 | Defendant's Rule 12(b)(6) motion to dismiss all five counts of the First Amended Complaint |
| `proposed-order.docx` | 2 | Self-executing proposed order granting the motion (separate filing per Standing Order § 3.5) |
| `cover-memo.docx` | 5 | Privileged internal memo flagging threshold issues for the lead partner before filing |

## How the documents were built

I read the full case file — the First Amended Complaint, the MSLSA and SOW-1, Meridian's Answer, the defense research/case-law memo, the Notice of Removal, the Scheduling Order, Judge Alvarez's Standing Order, and Arcadia's operating agreement — then generated the three `.docx` files with `python-docx` for precise control over Judge Alvarez's formatting requirements (12-pt Times New Roman, double-spaced, 1-inch margins, page numbers centered in the footer, compliant caption/signature/certificates). Each file was run through `skills/docx/scripts/validate.py` (all pass) and rendered to PDF to confirm page counts and that the Table of Authorities page numbers match the actual citation pages.

## Motion to Dismiss — argument structure

The motion is a post-answer Rule 12(b)(6) motion (defense preserved in Meridian's Answer, First Affirmative Defense and Part III; permitted by the Standing Order § 3.4 and the Scheduling Order). It is limited to the FAC's own allegations plus the MSLSA, SOW-1, Change Orders, and the Dec. 9, 2021 proposal (all referenced in and central to the FAC, so consider-able under *Lormand* without conversion). It deliberately does **not** rely on facts appearing only in the Answer/discovery (Poletti's notes, the PM gap, the API-spec delay, Linden Park's errors) — those are preserved for summary judgment.

- **Count V (DTPA)** — dismissed on the dispositive § 17.49(f) transaction exemption: Arcadia is an LLC (not an individual) and total consideration is $17.05M (> $500K threshold by 34×). *PPG Industries.*
- **Count IV (Unjust Enrichment)** — barred because an express contract (the MSLSA) governs the same subject matter; Arcadia sues *on* the contract and does not allege it is void. *Fortune Production; Excess Underwriters.*
- **Count II (Fraud)** — four independent grounds: (1) Rule 9(b) "why" failure (post-hoc product failure ≠ falsity when made; "on information and belief" knowledge allegations lack a factual basis; *Benchmark; Flaherty; Dorsey*); (2) non-actionable puffery ("industry-leading," "30-40% improvement," "seamless," "proven"; *Pizza Hut; Castrol; Presidio*); (3) economic loss doctrine under both Delaware (*Brasby; Kuhn*) and Texas (*Sharyland; Chapman*) law; (4) integration clause / no justifiable reliance (§ 12.1; Arcadia's own admissions of disclaimers, due diligence, and counsel; *Eagle Industries; SIGA; Hollcroft*).
- **Count III (Negligent Misrepresentation)** — no independent duty (*McCamish*); economic loss doctrine; benefit-of-the-bargain damages not recoverable in tort (*Sloane*); Rule 9(b) applies (*Benchmark*).
- **Count I (Breach of Contract)** — primary: deemed acceptance under § 5.3 (Go-Live 1/15/23 → 30-day window closed 2/14/23; first written complaint 3/8/23, 22 days late; *Simulados; Precision Healthcare*) and the expired, exclusive § 9.1 warranty (*Kana Software*). Alternative: §§ 8.1/8.2/8.5 cap and waive the consequential damages that make up the bulk of the $47.3M demand (*Dresser-Rand*).

Choice of law is handled in the alternative: Delaware governs the contract (§ 12.7); the tort claims are argued to fail under **both** Delaware and Texas law. A note in the Legal Standard satisfies Standing Order § 1.4 (binding vs. persuasive authority). The brief includes a certificate of conference (Jan. 9, 2024 telephone conferral) and certificate of service.

## Cover Memo — threshold issues flagged

The lead issue is a **likely defect in subject-matter jurisdiction**. The Notice of Removal asserted Arcadia is a citizen of Texas only (based on managing member Okonkwo), but an LLC's citizenship runs through *all* members (*Harvey; Carden*). Per the operating agreement, Arcadia's members include Apex Medical Ventures, LP (a Delaware LP) whose general partner is a Delaware corporation — so Arcadia is a citizen of **both Texas and Delaware**, the same two states as Meridian (Delaware incorporation + Texas principal place of business). Complete diversity appears destroyed (*Strawbridge*); jurisdiction cannot be waived and may be raised sua sponte (*Arbaugh*). The memo lays out the analysis, the irrevocable/revocable-trust discrepancy (which does not change the outcome), the candor-to-the-tribunal implications of proceeding, the federal-vs.-state forum trade-offs (including the § 12.9 jury waiver already enforced in federal court), and four options (proceed / disclose concurrently / move to remand / investigate further), with a recommendation to resolve the citizenship question before filing.

The memo also flags: the 12(b)(6)-vs.-12(c) labeling conflict between the Standing and Scheduling Orders; the aggressive posture of fully dismissing Count I (with damages limitation as the safer alternative); the Rule 12(d) conversion risk; choice-of-law strategy; the § 8.1 "event giving rise to liability" ambiguity (needs billing records); the § 8.4(e) willful-misconduct exception; the requirement to docket the certificate of conference separately and to actually confer by phone; the 25-page / 10-page-reply limits; the need to update the proposed order's docket number after filing; a bar-number discrepancy between the Notice of Removal and the Answer; and the jury-waiver status.

## Notes for the filer

- The proposed order uses `[Dkt. No. __]` placeholders that must be updated with the motion's docket number within one business day of filing (Standing Order § 3.5).
- The certificate of conference is included in the motion for convenience but should be docketed as a **separate** document (Standing Order § 3.1); confirm the actual telephone conferral with opposing counsel occurred.
- Bar numbers in the motion follow the Answer (Calloway 24037891; Arsenault 24098254); confirm against firm records given the discrepancy with the Notice of Removal.
- The jurisdictional issue in the cover memo is gating and should be resolved before the January 15, 2024 deadline.