# Key-Terms Extraction Memo — Summary of Work

## Deliverable
`output/key-terms-extraction-memo.docx` — a board-ready memorandum (22 pages, ~7,700 words) prepared from the perspective of Whitmore Analytics Inc.'s outside counsel (Ferndale Hale & Seward LLP) for the June 18, 2025 board meeting, as requested in Sarah Yin's internal email. Validated clean against the docx schema/ZIP-integrity gate.

## Source documents reviewed
1. **`kbi-whitmore-term-sheet.docx`** — Non-binding term sheet (May 29, 2025) for a PredictIQ technology license, prepared by KBI's counsel.
2. **`kbi-mfc-side-letter.docx`** — Most-favored-customer side letter (May 29, 2025) from KBI, conditioning the deal on an MFC pricing provision.
3. **`whitmore-internal-emails.eml`** — June 3, 2025 internal Whitmore thread (Tom Kendrick / Sarah Yin / Rajesh Malhotra) flagging concerns and requesting the board-ready memo.

## Memo structure
- **Letterhead + privilege legend + memo header** (TO/FROM/DATE/RE) and basis-of-review note.
- **§1 Executive Summary** — opportunity (~$9.56M first-year; ~$24.55M 5-year TCV; ~20% of FY24 revenue) and the four critical risks.
- **§2 Transaction Overview** — parties, structure, scope, timeline snapshot table.
- **§3 Key Commercial Terms** — fee-structure table, milestones table, economics snapshot.
- **§4 Key Legal Terms — Extraction** — section-by-section extraction of all 16 term-sheet sections.
- **§5 The MFC Side Letter** — key terms and why it is a first-tier concern.
- **§6 Risk Flags** — 4 Critical, 6 High, 10 Medium/Low, each with category tags.
- **§7 Negotiation Recommendations** — 12 subsections of specific counter-positions, with red lines marked.
- **§8 Recommended Negotiation Posture and Red Lines** — absolute red lines, negotiable items, leverage points.
- **§9 Process and Timeline** — action table with owners.
- **Appendix A** — Key Terms at a Glance (color-coded severity).
- **Appendix B** — Five-Year Economics table (verified figures).
- **Appendix C** — full 20-item Risk Register with severity color-coding and cross-references.

## Key analytical findings (verified)
- **First-year revenue ~$9.56M** = license $4.2M + SaaS $2.85M + implementation $1.75M + maintenance $0.756M (≈20.2% of $47.3M FY24).
- **5-year TCV ~$24.55M**; recurring (SaaS+maintenance) ~$18.6M; one-time ~$5.95M.
- **Steady-state liability cap effectively $15M** (2× trailing fees ≈ $7.3M < $15M floor), with the uncapped IP indemnity sitting on top.
- **Four critical risks:** (1) exclusivity/non-compete (open-ended 30% test; 25–30 cos + 3 active prospects worth $4–5M; EU competition exposure); (2) data-training restriction + Output Data ownership of model weights; (3) MFC side letter (no carve-outs/sunset, retroactive, through wind-down); (4) uncapped IP indemnification.
- **Six high risks:** performance warranty penalties, derivative-works joint ownership, feedback/improvements tension, source-code escrow triggers, perpetual wind-down license, implementation cash-flow mismatch (~$0.7–1.2M first-6-month shortfall).
- Noted the **binding 60-day no-shop** (§16.2) that activates if Whitmore signs the term-sheet acknowledgment, and the **perpetual (not 24-month) wind-down license** actually in the term sheet vs. the GC's email characterization.

## Build approach
Authored programmatically with `python-docx` for full control over professional styling (Cambria body, navy headings, color-coded severity cells, shaded table headers, footer with page numbers and privilege legend). Validated with `skills/docx/scripts/validate.py` (exit 0) and visually spot-checked via LibreOffice PDF render.