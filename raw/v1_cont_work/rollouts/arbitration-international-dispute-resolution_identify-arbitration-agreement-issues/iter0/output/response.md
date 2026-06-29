# Arbitration & Dispute Resolution Issues Memo — Summary

**Deliverable:** `output/arbitration-issues-memo.docx` (21 pages, schema-validated)

## What was done

Reviewed the arbitration and dispute resolution provisions across all five attached documents:

1. **Exclusive Supply Agreement (SA)** — Article 14 (ICC arbitration; Singapore seat; London venue; New York law) plus related liability/indemnity/survival provisions.
2. **Quality Assurance Side Letter (QA Letter)** — Section 7 (SIAC expert determination → arbitration; Singapore law).
3. **IP License Agreement (IPLA)** — Section 9 (LCIA arbitration; London seat; English law; consolidation clause).
4. **Harmon & Grey LLP summary memorandum** — Pacifica's counsel's rationale for the architecture (including the 2023 "pathological clause" enforcement experience).
5. **Internal Greenleaf/Ridgeway email chain** — Greenleaf's negotiating priorities (consequential damages, joinder, cross-document consistency, enforceability, limitation period, discovery).

The memo is framed as Whitfield & Crane LLP's severity-rated issues memo to Greenleaf/Ridgeway, with an executive-summary issue register, detailed analysis, and concrete recommendations for each issue.

## Issues identified (18 total)

| Severity | Count | Highlights |
|---|---|---|
| **Critical** | 3 | C1 — Conflicting consolidation/coordination provisions (IPLA §9.3 vs SA §15.8 vs QA §8.1 vs IPLA §10.3) recreate "pathological clause" risk; C2 — Consequential damages waiver (SA §14.11) + exclusivity + recall-cost subordination + internal conflict with §11.2 (deal-level risk); C3 — Appeal-on-law provision (SA §14.6) based on a legal error (Singapore has no English Arbitration Act s.69 equivalent by default; likely a nullity). |
| **High** | 5 | H1 Fragmented architecture (3 institutions/seats/laws); H2 No joinder mechanism for co-manufacturers; H3 Blanket no-discovery bar; H4 One-year limitation period (UCC floor, accrual inconsistency, latent-defect/indemnification cutoff); H5 Expert-determination "challenge" trigger undermines finality. |
| **Medium** | 5 | M1 Cost allocation inconsistency; M2 Arbitrator number/unilateral trigger; M3 Interim relief (overbroad in SA, absent in IPLA/QA); M4 Expert scope includes legal allocation; M5 Law of the arbitration agreement unspecified. |
| **Low** | 5 | L1 Confidentiality gap; L2 "General principles" gap-filler; L3 QA survival; L4 Seat/venue split; L5 Service mechanics. |

## Key cross-cutting recommendation

Adopt a single, unified dispute resolution architecture (one institution, one seat, one governing law) across all three Transaction Documents — which resolves the Critical and High structural issues simultaneously — followed by reconciling the consequential-damages, limitation-period, and expert-determination provisions. A recommended negotiating sequence is included.

## Build notes

- Generated with `python-docx` for precise control over letterhead, memo header block, color-coded severity ratings, and the executive-summary table.
- Validated with `skills/docx/scripts/validate.py` (ECMA-376 schema-valid; ZIP/XML integrity confirmed).
- Rendered to PDF (21 pages, US Letter) to confirm layout.