# Key-Terms Extraction Memo — Summary

**Deliverable:** `output/key-terms-extraction-memo.docx` (28 pages, validated against ECMA-376 WordprocessingML schemas)

## What was reviewed
- `kbi-whitmore-term-sheet.docx` — non-binding term sheet (16 sections + Exhibits A/B) for a PredictIQ technology license from Whitmore Analytics Inc. (licensor) to Kessler-Brandt Industrial GmbH (licensee), dated May 29, 2025.
- `kbi-mfc-side-letter.docx` — Most-Favored-Customer pricing side letter from KBI to Whitmore, dated May 29, 2025.
- `whitmore-internal-emails.eml` — June 3, 2025 internal thread (CEO Rajesh Malhotra, GC Sarah Yin, VP Sales Tom Kendrick) flagging concerns and instructing outside counsel to prepare a board-ready memo by June 16 for the June 18 board meeting.

## Memo framing
Prepared from the perspective of Whitmore's outside counsel (Ferndale Hale & Seward LLP) for Whitmore's board, per the instructions in the internal emails. Marked privileged & confidential / attorney work product.

## Structure of the memo
1. **Executive summary** — deal snapshot, bottom-line recommendation, top-risks-at-a-glance table.
2. **Transaction overview** — parties/advisors, deal structure, timeline.
3. **Key commercial terms** — fee schedule, 5-year contract value (~$24.55M), cash-flow timing concern.
4. **Key legal terms extraction** — all 16 term-sheet sections summarized by topic.
5. **MFC side letter** — key terms and analysis (no sunset, no carve-outs, retroactive look-back, etc.).
6. **Risk flags** — 16 prioritized risks (3 Critical, 6 High, 7 Medium/Low), each with provision, issue, risk, management position, and recommendation.
7. **Negotiation recommendations** — red lines, high-priority counter-proposals, commercial/structural fixes, and terms to preserve.
8. **Negotiation posture & process.**
9. **Open items for specialist review** (German law, cross-border tax, technical validation, ASC 606, etc.).
10. **Appendices A–D** — 5-year fee schedule, key dates, Exhibit B competitors, internal-concerns cross-reference.

## Key analytical findings woven in
- **Three dealbreakers** aligned with management's red lines: exclusivity scope (§12), data-training ban + Output Data ownership (§§4.2–4.3), and the MFC side letter.
- **Notable catch:** the term sheet provides a *perpetual* wind-down license at the *full* maintenance fee (§13.5) — more onerous than the "24-month/reduced-fee" characterization in the internal email.
- **Notable catch:** the MFC side letter contains no temporal limit on its retroactive look-back (broader than the "since January 1, 2024" framing in the internal email).
- **Housekeeping flag:** the side letter references "Fenwick Hale & Seward LLP" while internal communications use "Ferndale Hale & Seward LLP" — likely a typo to confirm.
- Concrete counter-proposals (e.g., 40/30/30 license split, separate implementation SOW, capped IP indemnity, narrowed exclusivity to 18 months/named companies, restructured Output Data ownership, sunset/carve-outs for the MFC).

## Production method
Authored as structured markdown, rendered to .docx via Pandoc with a custom python-docx reference template (Calibri, navy headings, 1" margins, confidentiality footer with page-number field), then post-processed to set fixed-layout tables with proportional column widths. Final schema validation passed (exit 0).