# Key-Terms Extraction Memo — Work Summary

## Deliverable
- **`output/key-terms-extraction-memo.docx`** — board-ready key-terms extraction memo with risk flags and negotiation recommendations, prepared as outside counsel (Ferndale Hale & Seward LLP) for the Whitmore Analytics Inc. Board of Directors, dated June 16, 2025 (two days before the June 18, 2025 board meeting, per the engagement described in the internal emails). Validated against ECMA-376 WordprocessingML schemas (exit code 0).

## Documents reviewed
1. `kbi-whitmore-term-sheet.docx` — non-binding term sheet (May 29, 2025), 16 sections + Exhibits A & B.
2. `kbi-mfc-side-letter.docx` — most-favored-customer pricing side letter (May 29, 2025).
3. `whitmore-internal-emails.eml` — June 3, 2025 thread among Tom Kendrick (VP Sales), Sarah Yin (GC), and Rajesh Malhotra (CEO).

## Memo structure (10 sections)
- **I. Executive Summary** — commercial significance (~$9.556M first-year revenue; ~20% of FY 2024 revenue) and the five critical dealbreaker issues.
- **II. Documents Reviewed** (with caveat + signature-status note).
- **III. Transaction Overview & Parties** (table, incl. Whitmore founded 2017 / FY 2024 ~$47.3M).
- **IV. Key Commercial Terms** — fees, milestones, and term/termination tables (all figures verified against the term sheet).
- **V. Key-Terms Extraction** — section-by-section extraction of all 16 sections, Exhibits A & B (all 12 named competitors), and the side letter, each cross-referenced to the risk register.
- **VI. Risk Flags** — 44 distinct flags in four tiers: 5 Critical (C-1–C-5), 10 High (H-1–H-10), 11 Medium (M-1–M-11), 18 Lower/Missing Provisions (L-1–L-18).
- **VII. Negotiation Recommendations** — 26 issue-by-issue recommendations, incorporating management's stated positions (Malhotra/Yin/Kendrick) plus outside-counsel counter-terms.
- **VIII. Process, Timeline & Next Steps** (table with owners).
- **IX. Items Requiring Further Diligence** (11 open questions).
- **X. Reservations & Limitations.**

## Completeness audit (performed as real tool calls)
Re-read all three source documents, enumerated every distinct issue, and cross-checked the deliverable by content search. Gaps found and filled:
1. **Liquidated-damages discrepancy** — Sarah Yin's email cites "termination for cause and liquidated damages" as exclusivity-breach remedies, but the term sheet (§12.5) provides only injunctive relief. Added to C-1, recommendation #1(e), and open-question #11.
2. **Uncapped fee escalations over a perpetual term** (new flag M-11) — 3% SaaS / 4% maintenance escalations compounding indefinitely with no cap/collar over a perpetual term and perpetual wind-down. Added as a distinct Medium flag, with a recommendation (#25) and exec-summary mention.
3. **Whitmore founded 2017** — added to the Section III parties/background table.
4. **Signature status** — KBI signed the term sheet (May 29, 2025) as to binding provisions only; Whitmore's blocks and the side-letter acknowledgment are blank. Added as a note in Section II.
5. **MFC trigger breadth** — "any agreement, amendment, or arrangement" (informal arrangements/pilots/LOIs/amendments could trigger parity). Added to C-4 and recommendation #4(f).
6. **Side-letter's own confidentiality** (§5) restricting disclosure of the MFC's existence/terms — tension with the audit right and Whitmore's ability to brief auditors/board/investors. Added to C-4 and recommendation #4(g).
7. **Cash-absorb context** — Raj's confirmation that Whitmore can absorb the shortfall but prefers to restructure. Added to H-1.
8. Fixed an internal inconsistency ("four critical issues" → "five critical issues" in the negotiation-posture paragraph).

Verified after edits: all 44 risk flags defined; recommendations numbered 1–26 sequentially; all 16 Section-V cross-references point to defined flags; all 12 named competitors present; document re-validates (exit 0).

## Key issues captured (non-exhaustive)
- Overbroad 3-year exclusivity with open-ended 30%-revenue catch-all (25–30 additional companies; 3 active prospects; $4–5M recurring); plus the liquidated-damages discrepancy.
- Data-training restriction + Output Data ownership (model weights/parameters claimed by KBI).
- Perpetual, no-sunset, no-carve-out, retroactive, auditable MFC side letter (incl. trigger breadth and own-confidentiality tension).
- Uncapped IP indemnification with no KBI-modification carve-outs.
- Cash-flow mismatch (first-6-month ~$1.843M inflows vs. $2.5–3M costs; Whitmore can absorb but prefers to restructure).
- 92% performance warranty with financial penalties and termination trigger.
- Broad source-code escrow with low release triggers and perpetual royalty-free post-release license.
- Perpetual wind-down license; one-sided termination for convenience and assignment; German governing law; uncapped fee escalations over a perpetual term.
- 18 missing provisions (DPA/security, cross-border transfer mechanics, OSS, export controls, insurance, no-hire, force majeure, KBI data-lawfulness warranty, etc.).
- Three internal-document discrepancies flagged (Fenwick vs. Ferndale firm name; 24-month vs. perpetual wind-down characterization; Jan 1, 2024 MFC look-back not present in side-letter text).

## Method
Authored as markdown, converted to .docx via Pandoc (`skills/docx/scripts/generate_from_md.py`), and validated via `skills/docx/scripts/validate.py`. Cross-references between the section-by-section extraction and the risk register were verified programmatically (all present and consistent).