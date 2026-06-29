---
name: emit-deliverable-not-work-summary
description: Dominant GLM failure mode — agent emits a work-summary describing a generated file instead of the deliverable's own prose; skill edit forces emitting full substantive text.
metadata:
  type: feedback
---

**What I changed (v0):** Rewrote `harness/skill/initial_skill.md` (was bare). Added three generic rules: (1) final text output must BE the deliverable's full substantive prose — not a "What I did / Work Summary / Response Summary" describing a `.docx`, with a grader-perspective self-check that each issue/element/recommendation appears as written-out content rather than "I addressed X"; (2) audit the draft element-by-element against the controlling framework named in the task's own source docs, deliberately surfacing omissions/misclassifications and carrying each to consequence+recommendation; (3) format to the task with explicit per-item ratings. No statutes/numbers/answer keys.

**Failure mode targeted (from my analysis of `rollouts/`):** The lowest scorers — environmental ESA 0.17 (27-line "Work Summary"), employment markup 0.60 (23-line "Summary"), trusts exhibits 0.77 (26-line "Response Summary") — wrote the real content to a `.docx` and emitted a meta-summary with bullet teasers. High scorers emit the memo itself (arbitration disclosure 0.97 = 796 lines; capital-markets 0.79 = 1142). Even where the agent did the analysis, substance trapped in a file or reduced to "I redlined §4" can't match rubric criteria keyed to specific content.

**Why it generalizes:** method, not memorization — "emit the deliverable as prose + self-check each gradable item is written out" applies to any memo/markup/findings task regardless of practice area, and reads elements off the source rather than a fixed checklist, so it can't force irrelevant artifacts. See [[findings-scratch]].
