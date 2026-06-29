# Deliverables: Rule 12(b)(6) Motion to Dismiss Package

**Matter:** *Arcadia Health Systems, LLC v. Meridian Cloud Solutions, Inc.*, No. 1:23-cv-00847-CMA (W.D. Tex., Austin Div., Hon. Catherine M. Alvarez)

## Files produced (in `output/`)

| File | What it is | Length |
|---|---|---|
| `motion-to-dismiss.docx` | Defendant's Rule 12(b)(6) motion to dismiss all five counts of the First Amended Complaint | 21 pp. (limit: 25) |
| `proposed-order.docx` | Proposed order granting the motion (self-executing, per Standing Order § 3.5) | 2 pp. |
| `cover-memo.docx` | Privileged internal memo flagging threshold issues for the lead partner | 10 pp. |

All three were schema-validated (`skills/docx/scripts/validate.py`) and formatted to Judge Alvarez's Standing Order: 12-pt Times New Roman, double-spaced, 1" margins, single-spaced indented block quotes (50+ words), bottom-centered page numbers, full caption, signature block, and certificates of conference/service.

## The motion — arguments by count

The brief leads with the cleanest, most dispositive grounds and relies only on documents cognizable at the pleading stage (the FAC's own allegations plus the MSLSA, SOW-1, and Change Orders, which are referenced in and central to the claims under *Lormand v. US Unwired*, 565 F.3d 228 (5th Cir. 2009)).

- **Count V (DTPA)** — Barred by the Tex. Bus. & Com. Code § 17.49(f) transaction exemption: total consideration $17,050,000 ≫ $500,000 threshold and Arcadia is an LLC, not an individual. Alternative grounds: not a "consumer"; warranty theory barred by §§ 9.4/9.1; puffery cannot be a producing cause.
- **Count IV (Unjust Enrichment)** — Barred because an express, valid contract (the MSLSA) governs the same subject matter. *Fortune Production*; *Excess Underwriters*. Arcadia sues on the contract in Count I, so it cannot plead unjust enrichment in the alternative.
- **Count II (Fraud)** — Four independent bars: (1) Rule 9(b) failure (no "why"/falsity-when-made; conclusory "information and belief" scienter; impermissible lumping); (2) economic loss doctrine under both Delaware (*Brasby*; *Kuhn*) and Texas (*Sharyland*; *Chapman*) law; (3) puffery (*Pizza Hut*; *Castrol*; *Presidio*); (4) the § 12.1 integration clause + anti-reliance acknowledgment (*Eagle Industries*; *SIGA*), reinforced by the Dec. 9, 2021 proposal disclaimers and Arcadia's own due diligence/counsel.
- **Count III (Negligent Misrepresentation)** — No independent duty (*McCamish*); benefit-of-the-bargain damages sound in contract (*Sloane*); economic loss doctrine; Rule 9(b) applies to claims sounding in fraud.
- **Count I (Breach of Contract)** — Primary: deemed acceptance under § 5.3 (FAC's own dates show the first written complaint came 22 days after the 30-day window closed) plus the expired 90-day warranty (§ 9.1) channel remedies to the contract; the data-migration breach allegations are contradicted by SOW-1 § 3.2 / Ex. C § C.2, which assign migration solely to Arcadia. Alternative: even if a claim survives, $30.1M of the $47.3M demand is consequential damages barred by § 8.2, and aggregate liability is capped by § 8.1 (*Dresser-Rand*; *Kana Software*).

## The proposed order

Grants the motion; dismisses all five counts with prejudice; enters judgment for Meridian; denies all relief; addresses costs; declares finality and directs the Clerk to close the case. Identifies the motion by title and docket-number placeholder `[__]` (to be updated within one business day of filing, per § 3.5). No argumentative recitals.

## The cover memo — threshold issues flagged (in order of urgency)

1. **Subject-matter jurisdiction — likely complete-diversity defect (CRITICAL).** The Notice of Removal alleged Arcadia is a citizen of Texas only (tracing only Dr. Okonkwo). But Arcadia is an LLC (*Harvey v. Grey Wolf Drilling*), and its member Apex Medical Ventures, LP is a limited partnership whose general partner, Apex Medical Ventures GP, Inc., is a **Delaware** corporation (*Carden v. Arkoma*). So Arcadia is a citizen of Delaware *and* Texas — the same as Meridian. **Complete diversity is destroyed**, the defect is apparent on the face of the FAC (¶¶ 7–8), jurisdiction cannot be waived, and the Court may raise it sua sponte (*Arbaugh*; 28 U.S.C. § 1447(c)). The memo recommends confirming the analysis with the Apex partnership agreement and deciding whether to file the motion while candidly flagging jurisdiction (or move to remand), noting the duty of candor and that the merits arguments travel to state court. Also flags the "irrevocable" (FAC) vs. "revocable" (Operating Agreement) trust discrepancy.
2. **Post-answer posture — 12(b)(6) vs. 12(c).** The Standing Order (§ 3.4) and the Scheduling Order conflict on how the post-answer motion is treated; the standard is identical (Twombly/Iqbal), but it affects what the Court may consider. Brief is built to survive either characterization.
3. **Choice of law for torts (Delaware vs. Texas).** Affects the strength of the economic-loss and anti-reliance arguments; brief argues both in the alternative.
4. **Count I — full dismissal is aggressive.** Recommends leading with deemed acceptance but preserving the damages-limitation alternative; flags that the § 8.1 cap calculation needs Meridian's billing records.
5. **DTPA § 17.49(f) — confirm operative statutory text.** The Answer pleads a $25M asset threshold the research memo omitted; both thresholds are met (Arcadia's own expert concedes ~$41M assets). Also flags a possible § 17.505 pre-suit-notice timing issue to verify.
6. **With vs. without prejudice.** Counts IV/V are with-prejudice (uncurable); Counts II/III may draw leave to amend under Rule 9(b).
7. **Procedural housekeeping** — Jan. 15, 2024 deadline; 25-page limit; separate certificate of conference and proposed-order filings; exhibit selection (avoid conversion); the § 12.9 jury waiver / bench-trial posture.

## Notes on scope and judgment calls

- The brief deliberately avoids relying on facts that appear only in Meridian's answer or in non-pleading documents (the Aug. 25, 2022 project status report, the support-ticket summary, the negotiation emails). Those are powerful summary-judgment evidence but would invite conversion at the 12(b)(6) stage; the cover memo flags them as reserved for later.
- The motion is styled as a Rule 12(b)(6) motion (consistent with the Standing Order and the Answer's preservation) while the cover memo addresses the Scheduling Order's 12(c) characterization.
- The single most important strategic recommendation in the cover memo is to resolve the diversity-jurisdiction defect *before* filing, because it may determine whether the motion is filed in this Court at all.