# IP License Renewal Analysis Memo — Summary

## Deliverable
`output/ip-license-renewal-analysis-memo.docx` — a privileged, licensee-side (Greenfield Biosciences) renewal analysis memorandum, generated from markdown via Pandoc and validated against the ECMA-376 WordprocessingML schema (validation passed).

## Documents reviewed
- **License A** — CRISPR-Ag Suite IP License (NT-GF-2015-001, eff. 7/1/2015)
- **License B** — TraitForge Plant Trait Expression Platform License (eff. 1/1/2018)
- **License C** — GenoMap Pro Software License (eff. 3/1/2020)
- **NovaTrait Consolidated Renewal Proposal** (dated 10/14/2024, Parts I–VIII)
- **Prairielands Sublicense Agreement** (eff. 5/1/2021, soybean drought tolerance, Argentina/Brazil)
- **Clarendon IP Consulting — Patent Landscape Analysis** (Exec. Summary, 9/14/2020)
- **Ridgemont/Oakvale Advisory Group — Financial Impact Analysis** (Feb 2025; JSON + XLSX, 14 sheets)

## Memo structure (13 sections)
Executive Summary → Background → Critical Timing/Procedural Status → Aggregate Financial Impact → License A analysis → License B analysis → License C analysis → Cross-Cutting Issues (Net Sales redefinition & rate cap, improvements reversal, Prairielands implications, market comparables, term misalignment) → Switching-Cost/BATNA → Ranked Negotiation Priorities (14 items) → Recommended Counter-Proposal Term Sheet → Timeline & Action Items → Conclusion. Includes 9 comparison tables.

## Key conclusions
1. **Timing is the dominant risk** — License B expired 12/31/2024 and is in a §12.6 standstill ending 6/29/2025; License C expires 2/28/2025; License A expires 6/30/2025 (notice due 3/31/2025).
2. **Aggregate cost rises ~50%** (~$18.6M → ~$27.95M; 4.81% → 7.22% of revenue); every proposed rate/fee exceeds market comparables.
3. **Net Sales redefinition is a hidden second rate increase** — License A effective rate 6.70% (148.9% of current), barely inside the §14.3 150% cap.
4. **Differentiated strategy by license**: renew/re-price License B (irreplaceable, 4.25%); re-price License A to 5.0% with a step-down at the 3/12/2028 foundational-patent expiry and retention of insect resistance; aggressively re-price or replace License C toward the $3.5–4.0M market range.
5. **Reject material adverse terms**: improvements ownership reversal, GenoMap Pro source-code elimination and derivative-data ownership grab, 30-day biological-materials return, insect-resistance scope removal.
6. **Prairielands sublicense** is co-terminus with License B (expired), needs parallel renewal, and any new 40% pass-through should be resisted (counter 20% with phase-in).

## Method
Authored the memo as structured markdown, converted with `skills/docx/scripts/generate_from_md.py` (Pandoc), and validated with `skills/docx/scripts/validate.py` (exit code 0). Intermediate markdown was removed; the output directory contains only the final `.docx`.