# .claude/skills/ — the mutator's own skills

**Reusable procedures you (the mutator) write for yourself** — your own playbook for optimizing
the Harvey harness. When you find a workflow worth repeating (a way to triage a deliverable, a
checklist for validating a new Harvey-agent tool before it graduates into `harness/`, an
error-analysis routine over `rollouts/`), write it here so future iterations reuse it instead of
re-deriving it.

These are **your** procedures, distinct from `harness/` (the bare Harvey harness the agent runs).
Writable and yours to curate; tracked as mutator state, **not** part of the scored artifact —
only `harness/**` is scored.
