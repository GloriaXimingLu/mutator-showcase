# Key-Terms Extraction Memo — Summary of Work

## Deliverable
`output/key-terms-extraction-memo.docx` — a board-ready key-terms extraction memo with risk flags and negotiation recommendations, prepared as outside counsel (Ferndale Hale & Seward LLP) for the Board of Whitmore Analytics Inc., in connection with the proposed PredictIQ technology license to Kessler-Brandt Industrial GmbH (KBI).

## Source documents reviewed
- `kbi-whitmore-term-sheet.docx` — non-binding term sheet (May 29, 2025), prepared by KBI's counsel.
- `kbi-mfc-side-letter.docx` — most-favored-customer pricing side letter (May 29, 2025).
- `whitmore-internal-emails.eml` — internal Whitmore email thread (Kendrick/Yin/Malhotra, June 3, 2025) flagging concerns and requesting the board-ready memo for the June 18 board meeting.

## Framing
Whitmore is the **licensor** of PredictIQ; KBI is the **licensee**. The term sheet and side letter are KBI-drafted and KBI-favorable. The memo is written from Whitmore's perspective to support the Board's approval of a negotiation framework before Whitmore responds to KBI by the June 23, 2025 deadline.

## Memo structure (9 sections, 8 tables)
1. **Executive Summary** — opportunity, problem, recommendation, severity-at-a-glance.
2. **Transaction Overview** — parties, technology, structure, key dates, strategic context.
3. **Key Commercial Terms — Extraction** — 64-row table extracting every principal term (license grant, IP, data rights, fees, implementation, support, warranties, indemnity, liability, escrow, exclusivity, term/termination, governing law, confidentiality, misc., and the full MFC side letter).
4. **Economic Summary** — one-time/recurring fee tables, headline figures, illustrative 5-year total (~$24.5M), with caveats on recurring-revenue durability and ASC 606.
5. **Risk Flags** — summary table + detailed discussion of **17 risk flags** rated Critical/High/Medium/Low:
   - **Critical (3):** data-training ban + Output Data ownership (§4.2/4.3); open-ended 3-year exclusivity (§12); MFC side letter (no carve-outs/sunset, retroactive, perpetual via wind-down).
   - **High (6):** uncapped IP indemnity; perpetual license + perpetual wind-down eroding recurring revenue; IP-ownership cluster (joint derivatives, feedback/improvements tension, Output Data); 92% performance warranty with penalties; source-code escrow triggers + post-release license; German governing law.
   - **Medium (4):** implementation cash-flow mismatch; termination/assignment asymmetries; expansion-pricing/MFC interaction; 60-day no-shop.
   - **Low (4):** SLA/warranty inconsistency; sublicensing breadth; cross-border tax/VAT; late-payment interest.
6. **Negotiation Recommendations** — 25 specific counter-proposals mapped to the risk flags.
7. **Recommended Negotiation Posture & Red Lines** — 4 red lines (with management positions) vs. high-priority vs. negotiable.
8. **Process and Next Steps** — owner/target table aligned to the June 18 board meeting and June 23 response deadline.
9. **Conclusion** + privilege legend.

## Notable analytical points
- Flagged that the wind-down license is **perpetual** (not "24-month … at reduced fees" as internal counsel initially read), making it more adverse than characterized, and that it erodes the recurring SaaS economics central to the Series C narrative.
- Flagged the interaction of the perpetual license + perpetual wind-down + KBI-only convenience termination as a structural threat to recurring revenue.
- Flagged the §3.4/§3.5 feedback-vs-KBI-Inspired-Improvements tension and the joint-ownership-of-derivatives risk.
- Aligned recommendations with management's stated red lines (anonymized/aggregated data use non-negotiable; 30% exclusivity test must go; Output Data ownership must be struck) and specific counter-proposals (40/30/30 payment split, 18-month named-only exclusivity, bounded MFC with carve-outs/sunset, separate implementation SOW).

## Production method
Authored as structured markdown, converted to .docx via Pandoc with a custom reference template (Times New Roman, 11pt body) for a classic legal-memo appearance. Validated with `skills/docx/scripts/validate.py` (ECMA-376 schema-valid, ZIP/XML integrity, relationship consistency). Final file: 169 paragraphs, 8 tables, validates clean.