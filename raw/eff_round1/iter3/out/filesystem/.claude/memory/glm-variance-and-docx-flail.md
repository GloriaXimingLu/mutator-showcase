# Lesson — a flagged THRASH may be GLM variance (docx-generation flail), not your edit

**Verified by transcript analysis.** The iter1 "THRASH" on `corporate-ma/review-governance-diligence`
(18→73 turns, 1.37M→7.05M input) was **NOT** an eviction re-fetch loop: the agent did **zero document
re-reads** (all 8 reads once, turns 2-7) and **no eviction stub ever appeared**; the 73 turns were a
**docx-generation flail** — 62 bash calls (24× `python3 -c`, 6× `pdftotext`, 5× `generate_from_md.py`,
plus hand-written compress.py/make_ref.py). That is **glm-5p2 run-to-run variance** while producing the
binary deliverable, largely independent of any harness edit.

## Why it matters
- The per-task THRASH check compares to a **single** bare rollout, so ANY variance-heavy run flags
  THRASH/watch regardless of your edit. Before rejecting, **diagnose**: count re-reads + per-turn context.
  - **Re-fetch LOOP signature** (your edit's fault): per-turn context is ELEVATED vs bare (multiple full
    copies resident from repeated re-reads), turns AND tokens up together. → fix (pin / cap re-fetches).
  - **Variance flail** (not your fault): per-turn context ~bare, but many bash/tool turns (often docx
    generation). Eviction stubs absent or eviction never fired. → noise; an aggressive kill-switch can't
    prevent it and your edit didn't cause it.
- Transcript previews log the result at execution time, so **eviction stubs never show in
  `result_preview`** even when eviction fired — judge eviction by input_tokens/turns, not the preview.

## How to check fast
`rollouts/<task>/iterN/transcript.jsonl`: count reads per basename, count bash first-lines, count
">6000-char tool results". See the one-off script pattern used in iteration 2 (count reads/bash/stubs).
Related: [[eviction-length-gate-and-refetch-killswitch]].
