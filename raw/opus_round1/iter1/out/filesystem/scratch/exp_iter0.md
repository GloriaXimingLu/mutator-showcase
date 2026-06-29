# Iter0 experiment: system_prompt method addition (issue-spotting census + cross-doc + scope)
proxy_eval (single judge gpt-5-mini), candidate harness:
task                                   candidate
employment/draft-markup-settlement     0.615
immigration/identify-h1b               0.846
immigration/compare-immigration        0.791
arbitration/arbitrator-disclosure      1.000
healthcare/identify-issues-fda         0.830
environmental/phase-one-esa            0.113
(bare scores pending - same tasks, same grader)

## RESULTS (candidate vs bare, same proxy grader, single seed)
task                              bare    cand    delta
employment/draft-markup          0.500   0.615   +0.115
immigration/compare              0.721   0.791   +0.070
arbitration/disclosure           0.974   1.000   +0.026
environmental/phase-one          0.094   0.113   +0.019
immigration/h1b                  0.872   0.846   -0.026
healthcare/fda                   0.915   0.830   -0.085
NET MEAN                         0.679   0.699   +0.020  (wins 4/6)
turns comparable (cand 15-28 vs bare 13-28) -> no runaway (prose-only anyway)
COMMITTED: system_prompt.md method section.
