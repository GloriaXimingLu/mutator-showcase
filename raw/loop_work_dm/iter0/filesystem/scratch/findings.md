# Mutator findings — glm_headheadroom30 rollouts

## Pass rates (asc)
0.17 environmental (44 fail) | 0.60 employment (21) | 0.74 immigration-h1b (10) | 0.77 trusts-exhibits (14)
... up to 0.98 ip-licensing (1). Top half all >0.9.

## DOMINANT MODE (confirmed across low scorers): "work-summary instead of deliverable prose"
- environmental (0.17, 27 lines): deliverable.md = "Environmental Issues Memo — Work Summary / What I did" — DESCRIBES a memo written to .docx, lists issue COUNTS not the issues themselves. Rubric grades 53 specific content criteria → 44 fail.
- employment (0.60, 23 lines): "Settlement Agreement Review — Summary", bullet teasers ("added carve-outs to release (§4)") but NOT the substance; fails specific items (WC carve-out, 409A, mutual conf., tax indemnity, IP assignment).
- trusts-exhibits (0.77, 26 lines): "Response Summary / What the memo does" — describes a .docx.
- CONTRAST high scorers emit the MEMO itself: arbitration-disclosure 0.97 (796 lines), capital-mkts 0.79 (1142), immigration-h1b 0.74 (611).

## Why it costs points
Judge grades deliverable.md text. Content locked in a generated .docx, or reduced to "I addressed X" bullets, can't match rubric criteria keyed to specific substance. Even where agent DID the analysis, it isn't on the page as the deliverable's own prose.

## EDIT (one generic rule): final text output must BE the deliverable's full substantive prose (memo/markup/findings/recommendations), not a summary/description of a file it wrote. If a file artifact is also produced, the same substance must appear in the text. Self-check: each required element/issue/recommendation must appear as its own prose, not as "I addressed <topic>".
