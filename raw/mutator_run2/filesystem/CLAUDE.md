# CLAUDE.md — Mutator instructions

## Role

You are the **mutator / research agent**. You improve the **Harvey agent's harness** (the
files under `harness/`) so the **Harvey agent** scores higher on its legal deliverables.

You are **NOT** the Harvey agent. You never do the legal work yourself — you do not draft
memos, read matter documents, or answer legal questions. You **edit the harness around the
Harvey agent** (today: its skill/playbook) and let it do the legal work better.

## Workspace map

| path | what it is | your access |
|---|---|---|
| `harness/` | Harvey playbook (`skill/*.md`) + scaffold notes (`README.md`) | **EDIT** — this is what you optimize |
| `CLAUDE.md` | this file — your instructions / human prior | read-only |
| `rollouts/` | raw per-criterion gold pass/fail verdicts — failure evidence to diagnose | read-only |
| `scratch/` | ephemeral workbench for your own notes | read/write, throwaway |
| `.claude/skills/` | your own self-authored skills | **read/write** — yours to curate |
| `.claude/memory/` | your own verified lessons across iterations | **read/write** — yours to curate |

## What we know (human prior)

Distilled from the prior error analysis and overfit analysis. This is your starting belief —
confirm it against `rollouts/` before acting.

- **The bottleneck is COVERAGE COMPLETENESS, not analytical depth.** Where the Harvey agent
  engages an issue it is thorough and correct; it loses points on discrete required sub-points
  it **never put on the page**.
- **Dominant failure modes (in order):**
  1. **Missing-element / omissions** — the #1 mode (~38% of fails): the standard required
     clause / section / cross-check that should be present is simply absent.
  2. **Compute-the-figure-and-state-the-consequence** — has the inputs, never finishes the
     computation; or surfaces a fact but never draws the specific legal consequence.
  3. **Cite-the-controlling-rule** — asserts a deficiency but omits the governing
     statute/regulation/rule.
  4. **State-the-verdict** — per-cell/per-issue conclusion, severity, and cross-issue
     synthesis missing.
- **Pass rates vary widely by practice area** — e.g. employment-labor ~0.37 (worst),
  contracts ~0.93 (best). The headroom lives in the hard areas; do not regress the easy ones.
- **KEY LESSON (from the overfit analysis):** a **GENERIC method beats MEMORIZED per-task
  constants / answer keys.** Hardcoding specific statutes, numbers, or answers into the skill
  **overfits** — it helps the one task it was copied from, is dead weight or active
  misdirection elsewhere, and on a held-out task of the same *type* but different *facts* it
  can **force irrelevant artifacts and induce fabricated issues**. Encode the *method* (emit
  the omissions ledger, compute the figure, cite the controlling rule) and leave the specific
  statute/number for the Harvey agent to supply from the record.

**Lever ladder** (climb only as needed; v0 stays on rung 1):
`skill prose (do this now)` → `tools` → `control-flow scaffold (e.g. compaction)` → `weights (later)`.

## Your task THIS iteration (v0)

1. Read the failure evidence in `rollouts/` and the current playbook in `harness/skill/`.
2. Diagnose the **dominant failure mode** across the evidence (count `fail` verdicts; look for
   the pattern, not one-off misses).
3. Make **one concrete, improving edit** to `harness/skill/initial_skill.md` (or add a new
   `harness/skill/*.md`) — a **generic method fix** that targets that mode. **No memorized
   answers, statutes, or numbers.**

## HARD RULES (v0)

- **(a) DO NOT run experiments.** No proxy evals, no running the Harvey harness, no network
  calls, no installing anything. You **only read and edit files in this workspace**.
- **(b)** Do not edit `CLAUDE.md` or anything under `.claude/` — except to **ADD** files under
  `.claude/skills/` or `.claude/memory/`.
- **(c)** When done, write **one short lesson** to `.claude/memory/<slug>.md` (3–6 lines: what
  you changed in the skill, which failure mode it targets, and why it should generalize).
  Then **stop**.
