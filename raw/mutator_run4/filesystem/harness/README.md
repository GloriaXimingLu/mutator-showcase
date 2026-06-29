# Harvey harness scaffold

This directory is the **Harvey agent's harness** — the scaffold the legal agent runs inside.
It is the thing you (the mutator) optimize.

**Runtime shape (today):**
- The Harvey agent runs in a **Podman sandbox** with **6 shell tools**: `bash`, `read`,
  `write`, `edit`, `glob`, `grep`. That is the entire toolset.
- The control flow is a **flat agent loop** — no compaction, no planner, no sub-agents.
  The agent reads the matter's documents, does the legal work, and writes the deliverable.
- The **skill** in `harness/skill/` is the agent's playbook. It is injected into the agent's
  **system prompt** via the `HARVEY_PLAYBOOK` hook (one skill file selected per run).

**What is editable:**
- **Now:** the **skill prose** in `harness/skill/*.md`. This is the only lever for v0.
- **Later (not yet):** the **tool set** and the **control-flow scaffold** (e.g. adding
  compaction, a planner, or per-item loops). Do not touch these in v0.

So: edit `harness/skill/` to make the Harvey agent produce more complete, higher-scoring
legal deliverables. Everything else here is context for the shape you may later change.
