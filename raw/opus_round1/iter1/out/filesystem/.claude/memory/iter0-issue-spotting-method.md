---
name: iter0-issue-spotting-method
description: Iter0 committed a system_prompt method section targeting issue-spotting under-coverage on review tasks; validated +0.02 net proxy across 6 tasks.
metadata:
  type: project
---

**Iter0 (bare baseline, train mean 0.8423).** Dominant fixable mode: on review /
"identify-issues" / audit / diligence tasks the agent under-covers the rubric's
ISSUE_001…N census — it finds obvious issues but misses ones needing (a)
section-by-section coverage and (b) **cross-referencing one document against another**
(e.g. a contract term vs. an internal policy cap; a résumé date vs. a PERM requirement).
The bare `system_prompt.md` had **zero task method** — only workspace/tool conventions.
A separate trap: `environmental-esg/phase-one-esa` (stuck 0.17) is a **scoping error** —
the agent analyzed the wrong property and discarded the rubric's documents as "out of scope"
(idiosyncratic, not the generic mode — don't overfit to it).

**Committed:** a generic "Approach to the work" section in `harness/system_prompt.md` —
read all docs fully then fix scope deliberately; build a complete issue census
(section-by-section + cross-reference every doc against policy/standard/requirements docs);
develop each issue fully (identify+cite / why-it-matters / recommendation / classification);
stay grounded, don't fabricate. Method, not memorized statutes/numbers.

**Evidence (candidate vs bare, same proxy grader, single seed, 6 tasks):**
net mean 0.679→0.699 (+0.020), wins 4/6. Gains land where diagnosis predicted headroom —
employment/draft-markup +0.115, immigration/compare +0.070; dips were healthcare/fda −0.085
and immigration/h1b −0.026 (both already-high, single-seed noise). Turns 15–28 (no runaway).

**Why it should generalize:** encodes review *method* applicable to any matter; helps where
coverage had room, ~neutral where already strong.

**Next iteration:** prose is now spent on this mode. If issue-spotting under-coverage persists
in `rollouts/_stats/`, climb a rung — an **enforced** `agent_loop.py` step (a bounded
coverage/cross-reference self-check before finishing, hard-capped + `check_runaway`'d), or a
`tools.py` capability, rather than louder prose. Watch the healthcare/already-high tasks for any
over-coverage/fabrication regression from the census push.
