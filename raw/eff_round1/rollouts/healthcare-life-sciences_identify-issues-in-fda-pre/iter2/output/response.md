# Task Complete — Prioritized Issue Memorandum

**Deliverable:** `output/presub-issue-memorandum.docx` (validated, 32 KB, Microsoft Word 2007+)

## What I did

Reviewed all seven documents in the draft Pre-Submission (Q-Sub) package for the VascuClear 3000 catheter-based thrombectomy device:

1. Pre-Submission Cover Letter
2. Device Description and Predicate Comparison
3. Proposed Testing Plan
4. Clinical Study Synopsis
5. Draft Instructions for Use
6. ThrombEx 200 (K192847) 510(k) Summary (predicate)
7. Internal email chain on regulatory strategy

I cross-checked the package documents against each other and against the predicate's 510(k) summary, and prepared a prioritized issue memorandum in the voice of Daniel J. Yoo (Senior Associate, Hargrove, Templeton & Bliss LLP), dated May 19, 2025, consistent with the internal review deadline referenced in the email chain. The memorandum is marked privileged/confidential (attorney-client / work product).

## Key findings (21 issues across 4 priority tiers)

**Priority 1 — Critical (5):**
- Combination-product classification unresolved and not raised with FDA (device has a purpose-built tPA delivery lumen and a co-primary drug-delivery claim; predicate has none)
- IDE requirement / "post-clearance" contradiction (study labeled post-clearance but scheduled before clearance and intended to support the 510(k))
- Substantial equivalence at risk (predicate is purely mechanical aspiration with no drug delivery and no rotating element; NQSE exposure)
- Biocompatibility contact-duration mismatch (testing based on <24h "limited" contact while the IFU permits 72-hour indwell = "prolonged")
- Impeller fatigue testing grossly inadequate (500 revolutions at 12,000 RPM ≈ 2.5 seconds)

**Priority 2 — High (5):** software documentation level ("Minor" likely too low; 2005 guidance outdated; predicate was "Moderate"); drug-delivery characterization uses saline only with no drug-device interaction testing; pharmacomechanical bench testing absent; clinical study design weaknesses (unjustified performance goal, 30-day follow-up too short for PTS, tPA dosing controls); timeline infeasibility (CSR Q4 2026 vs. Dec. 31, 2025 clearance milestone).

**Priority 3 — Medium (5):** EMC testing omitted; shelf-life/packaging validation omitted; MRI safety testing incomplete; dynamic hemolysis not tested; multiple internal inconsistencies (console size/weight, predicate indication in Table A-1, impeller material stainless vs. nitinol, aspiration pressure, IFU materials).

**Priority 4 — Lower (6):** cover letter omits counsel's recommended questions; SE "narrowing" argument misstates drug delivery as a narrowing; aspiration-pressure magnitude difference unaddressed; bench vs. clinical threshold disconnect; applied-part classification to confirm; coating/adhesive chemistries undefined.

The memorandum closes with a gating decision (whether to add the combination-product and IDE questions to the cover letter), a pre-filing action list, and a strategic/commercial workstream flagging the timeline risk to management and corporate counsel (Kendrick & Hale).

## Method

Authored the memorandum as markdown, then generated the .docx via the docx skill's `generate_from_md.py` (Pandoc) and validated it with `validate.py` (ZIP integrity, XML well-formedness, content-type and relationship consistency — exit 0).