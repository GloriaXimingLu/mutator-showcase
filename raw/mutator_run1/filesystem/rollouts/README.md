# rollouts/ - real GLM-5.2 (default reasoning effort) standard-eval trajectories

Each <task>/ is one real rollout from the glm_headroom30 run (reasoning_effort=null), graded by the ensemble judge:
- deliverable.md   GLM's legal work product
- transcript.jsonl full agent trace
- metrics.json     turns/tokens/cost/documents
- task.md          instruction + rubric criteria + source documents
- grade.json       ensemble pass-rate + per-criterion verdicts + failed_criteria (id/title/match_criteria)

Raw evidence; worst-scoring tasks first. Diagnose the deliverable against failed_criteria.
