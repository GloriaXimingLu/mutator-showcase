---
name: deliverable-file-not-cover-note
description: GLM failure — agent writes a cover-note/work-summary to the output file and defers the real deliverable content to the chat message; grader reads the file, so content trapped in chat scores as absent.
metadata:
  type: feedback
---

**What I changed (v0, this iteration):** Sharpened §1 of `harness/skill/initial_skill.md`. The grader reads the **file written to `output/`**, not the final chat message — so that file must be the full deliverable prose. Added an explicit rule forbidding the "cover note / response.md / deliverables summary" pattern (writing a short file that says the real content "follows below" / "is set out in the final text output," with the actual memo/markup only in the chat). Moved the §1 self-check to read the `output/` file itself.

**Failure mode targeted (from my analysis of `rollouts/`):** capital-markets S-1 (ens 0.756 but 22 failed criteria, deliverable.md = 8 lines). The agent did the full analysis — final chat message was 109 KB containing the complete S-1 + 33-issue memo with severity ratings — but wrote a 1424-byte *cover note* to `output/response.md`. The eval captured that cover note as the deliverable, so all substance was graded absent. Compare environmental (1436-line memo written to `output/memo-draft.md`, captured correctly) and trusts/employment/cyber/litigation/H-1B (full memo written to a single `output/*.md`, captured). The differentiator is *what the agent writes to the output file*, not whether it did the analysis.

**Why it generalizes:** method, not memorization — "the output file is the deliverable; never defer content to chat" applies to any file-producing task (S-1, markup, settlement statement, findings memo) regardless of practice area, and reads no task-specific facts. This refines [[emit-deliverable-not-work-summary]]: that earlier lesson fixed "summary instead of memo" *in the captured file*; this one fixes the inverse trap where the file is a summary but the memo lives only in chat.
