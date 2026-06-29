# Mutator Showcase — On-Disk Data Formats

Reference for the showcase build. Documents the exact on-disk layout and field
schemas of (A) the **mutator's own Claude-Code session**, (B) a **Harvey-task
rollout** trajectory, and (C) the **standard-eval results** files. All paths are
relative to `showcase/raw/<run>/`.

The Harvey LAB benchmark is public (github.com/harveyai/harvey-labs); no content
restrictions. This doc records structure/schemas/sizes only.

---

## 0. Run families & directory layouts

Two on-disk shapes exist. **Which shape a run uses determines where the mutator
session and rollouts live.**

### v1 / continuity family — per-iteration `iterN/{seed,out}` layout
Runs: `eff_round1`, `opus_round1`, `v1_cont_work`.

```
<run>/
  series.json                 # train/val combined_score per iter (the headline curve)
  full_stats.json             # best_by_val / best_by_train / overfit_iters
  broker_ledger.json          # final cost ledger of mutator experiments
  broker_ledger.iterN.json    # per-iter snapshot of the ledger
  *.log                       # mutator console logs (run.log, eff_round1.log, run_iter2*.log, ...)
  results/                    # standard_eval_<prefix>_<split>_iterN.json  (see §C)
  rollouts/                   # HARVESTED Harvey-task trajectories (see §B) — the big dir
    <task_slug>/iterN/{transcript.jsonl, task.md, metrics.json, grade.json,
                       deliverable.md?, output/<name>.docx ...}
    _stats/  README.md
  iterN/
    seed/                     # the carried-IN harness state this iter started from
      harness/  CLAUDE.md  .claude/{memory,tools,skills}  scratch/
      rollouts/               # (carried copy — EXCLUDED from the pull)
    out/                      # the harness state this iter PRODUCED + the mutator session
      filesystem/             # mutated workspace: harness/ CLAUDE.md .claude/ scratch/
                              #   (filesystem/rollouts/ carried copy — EXCLUDED from the pull)
      reward.json             # what the mutator changed this iter (see §A.4)
      trajectory.json         # NanoRollout wrapper trajectory of the mutator (see §A.2)
      trial.log               # 3-line runner log (start env / run / run eval)
      agent/                  # <<< THE MUTATOR'S OWN CLAUDE-CODE SESSION  (see §A) >>>
        claude-code.txt       #   stream-json console log (JSONL)
        trajectory.json       #   agent-adapter export (same messages[], extra session_id/agent)
        sessions/projects/-workspace/<session-uuid>.jsonl   # canonical CC session transcript
        sessions/projects/-workspace/<uuid>/subagents/agent-*.jsonl  # nested Task subagents (if any)
    mutated_ws.txt            # 1 line: absolute path of out/filesystem on the VM
```

### v0 family — single-workspace, optional multi-iter (NO `out/` wrapper)
Runs: `mutator_run1..4` (single shot), `loop_work_dm` (multi-iter `iter0..2`).

```
<run>/                                 # mutator_runN: files directly here
  reward.json  trajectory.json  trial.log  <run>.log
  filesystem/   harness/skill/initial_skill.md  CLAUDE.md  .claude/{memory,skills}  rollouts/(carried)
  agent/        claude-code.txt  trajectory.json  sessions/projects/-workspace/<uuid>.jsonl

loop_work_dm/iterN/                    # same v0 shape, repeated per iter (no seed/out split)
  reward.json  trajectory.json  trial.log
  filesystem/{harness,CLAUDE.md,.claude,scratch,rollouts(carried)}
  agent/{claude-code.txt, trajectory.json, sessions/projects/-workspace/<uuid>.jsonl}
```

`_bare_harness/` is the unmutated template harness (`run.py`, `agent_loop.py`,
`tools.py`, `system_prompt.md`, `adapters/`, `skills/{docx,xlsx,pptx}`) — the
iter-0 starting point.

> **Mutator brain per run:** `eff_round1`, `opus_round1` ran on `claude-opus-4-8`;
> the v0 runs (`mutator_run1..4`, `loop_work_dm`) and `v1_cont_work` rollouts ran
> the mutator on `glm-5p2`. (See `model` field in each `trajectory.json`.)

---

## A. MUTATOR SESSION TRAJECTORY

The mutator is a Claude-Code agent operating on `/workspace`. Its session is
recorded in **THREE parallel representations**, all under the iter's agent dir.

**Canonical example iter: `eff_round1/iter2/out/agent/`** (mutator = claude-opus-4-8)

| file | bytes | format | what it is |
|---|---|---|---|
| `sessions/projects/-workspace/42682c88-…b7d3.jsonl` | 958 KB | **JSONL** (Claude-Code session) | **Primary transcript** — reasoning, tool calls, tool results, token usage. Use this. |
| `claude-code.txt` | 1.16 MB | **JSONL** (stream-json) | Live console event stream (incl. `thinking_tokens`, subagent task events). |
| `trajectory.json` | 528 KB | JSON object | Agent-adapter export: `messages[]` + `session_id`, `agent`, `llm_metrics`. |
| `../trajectory.json` (i.e. `out/trajectory.json`) | 531 KB | JSON object | NanoRollout wrapper of the same `messages[]` (+ `instance_id`, `wall_time_sec`, `exit_status`). |

For v1/continuity runs the agent dir is `iterN/out/agent/`. For v0 runs it is
`<run>/agent/` (or `loop_work_dm/iterN/agent/`). **All curated runs have the
session JSONL present** — see §A.5 for two non-standard placements.

### A.1 Primary session JSONL — `sessions/projects/-workspace/<uuid>.jsonl`

One JSON object per line. Line `type` ∈ `{user, assistant, attachment,
queue-operation, last-prompt}`. Example file: 394 lines.

Common envelope fields on `user`/`assistant`/`attachment` lines:
`parentUuid, isSidechain, type, message, uuid, timestamp, cwd, sessionId,
version, gitBranch, userType, entrypoint` (+ `promptId, promptSource,
permissionMode` on `user`, `requestId` on `assistant`).

**`assistant` line** — `.message` is an Anthropic Messages API object:
```
.message = {
  role: "assistant", model: "claude-opus-4-8", id, stop_reason: "tool_use",
  content: [ <blocks> ],
  usage: { input_tokens, output_tokens, cache_creation_input_tokens,
           cache_read_input_tokens, service_tier, ... }
}
```
`content[]` blocks (the unit to render):
- `{type:"thinking", thinking:"…"}` — extended-thinking reasoning.
- `{type:"text", text:"…"}` — the mutator's prose / narration.
- `{type:"tool_use", id:"toolu_…", name:"Bash"|"Write"|"Edit"|"Read"|"Task", input:{…}}`

**`user` line** — carries the tool results:
```
.message.content = [ {type:"tool_result", tool_use_id:"toolu_…",
                      is_error:false, content:"<stdout text>"} ]
```
(The very first `user` line is the mutator's task prompt: "You are the mutator
— a research agent that improves the Harvey agent's harness…".)

**How to extract the three streams the build wants:**
- **(a) reasoning / narration** → `assistant` lines → `content[]` blocks of type
  `thinking` and `text`.
- **(b) tool calls = bash commands** → `assistant` lines → `content[]` blocks of
  type `tool_use` where `name == "Bash"`; the command is `input.command`,
  human label is `input.description`.
- **(c) what it wrote** → `tool_use` blocks where `name ∈ {"Write","Edit"}`
  (`input.file_path`, `input.content`/`old_string`+`new_string`). Pair each
  `tool_use.id` with the matching `tool_result.tool_use_id` (next `user` line)
  to get the result.

Distinct tool names used by the mutator in this iter: `Bash` (60×), `Write`,
`Read`, `Edit`. Among the Bash calls, the mutator's **experiments** are the
broker tools it shells out to:
- `run_harvey_agent` — launch a Harvey rollout on a task (4× this iter).
- `dev_eval` / `proxy_eval` — held-out / proxy scoring (7× / 3×).
- `budget` — check remaining experiment spend.

Short structural samples (our own commands — not sensitive):
```jsonc
// assistant content tool_use block:
{ "type":"tool_use", "name":"Bash",
  "input": { "command":"/workspace/.claude/tools/budget 2>&1 | head -50",
             "description":"Check current budget" } }
// next user line, tool_result:
{ "type":"tool_result", "tool_use_id":"toolu_01JNpN…",
  "is_error": false,
  "content":"budget: spent $0.0000 / cap $160.00  ->  remaining $160.0000 …" }
// a real experiment launch (truncated):
{ "type":"tool_use", "name":"Bash",
  "input": { "command":".claude/tools/run_harvey_agent \"litigation-dispute-resolution/…\"" } }
```

### A.2 `out/trajectory.json` (NanoRollout wrapper) — flattened view

Top-level object:
```
instance_id   "harvey-mutator-v0"
model         "claude-opus-4-8"   (v0/cont runs: "glm-5p2")
api_base, environment ("docker"), success (bool), exit_status ("finished")
iterations    191                 # agent-loop turn count
messages      [192]               # see below
llm_metrics   [76]                # per-LLM-call usage
llm_cost_total  22.4766           # USD for this mutator session
wall_time_sec   11786.34
message       "<final summary text the mutator emitted>"
```
`messages[]` is OpenAI-style and flatter than the session JSONL — each
**assistant** turn bundles its tool call **and** its result:
```
{ role:"assistant",
  content:"<text/thinking concatenated>",
  model:"claude-opus-4-8",
  tool_calls:[ { tool_call_id:"toolu_…", function_name:"Bash",
                 arguments:{command:"…", description:"…"} } ],
  observation:{ results:[ { source_call_id:"toolu_…", content:"<tool stdout>" } ] }
}
```
Role distribution: 191 `assistant`, 1 `user` (the task prompt). `llm_metrics[i]`
= `{model, usage:{prompt_tokens, completion_tokens, cached_tokens, extra:{…}}, cost}`.
`out/agent/trajectory.json` holds the identical `messages[]` but swaps the
wrapper keys for `session_id` + `agent`.

> **Build tip:** for *reasoning + tool I/O paired per turn*, `out/trajectory.json
> .messages[]` is easiest. For *fine-grained blocks* (separate thinking vs text,
> exact write diffs, subagents), use the session JSONL (§A.1).

### A.3 `claude-code.txt` (stream-json console log)

JSONL, one event per line. Example iter2: 946 events.
`type` dist: `system` 673, `assistant` 191, `user` 81, `result` 1.
`system.subtype` ∈ `{init, thinking_tokens (627×), task_started (22×),
task_notification (21×), task_updated}`; `result.subtype == "success"`.
The first line `{type:"system",subtype:"init", cwd, session_id, model, tools:[…]}`
lists the full CC toolset. `assistant`/`user` lines mirror §A.1 message bodies.
Presence of `task_started`/`task_notification` ⇒ the mutator spawned **subagents**
(see §A.5, opus_round1/iter2).

### A.4 `reward.json` — what the iter changed (the diff summary)

v1/continuity shape:
```
resolved:true, resolved_status:"EDITED", reward:1,
files_changed:["/workspace/harness/agent_loop.py"],
files_added:[], files_removed:[], files_emptied:[],
lessons_written:["/workspace/.claude/memory/<lesson>.md", …],
instance_id, error:null, exit_status:"finished"
```
v0 shape uses `skill_files_changed / skill_files_added / skill_files_emptied`
(the v0 action space was the skill file) instead of `files_*`. This is the
machine-readable answer to "what did the mutator edit this iteration."

### A.5 Non-standard session placements (build must handle)

- **`opus_round1/iter2`** — the mutator spawned subagents. Main session is the
  top-level `…/-workspace/ad004501-…b7d3.jsonl` (1.1 MB); two nested subagent
  transcripts live at `…/-workspace/ad004501-…/subagents/agent-*.jsonl`
  (160 KB, 264 KB). Treat top-level `<uuid>.jsonl` as the mutator; render
  `subagents/agent-*.jsonl` as nested Task sub-sessions.
- **`loop_work_dm`** — v0-shaped, so the session is at
  `loop_work_dm/iterN/agent/sessions/projects/-workspace/<uuid>.jsonl` (NOT under
  `out/`, which does not exist for this run). All 3 iters present.

No curated run is missing its mutator-session transcript.

---

## B. HARVEY-TASK ROLLOUT TRAJECTORY

Harvested under `<run>/rollouts/<task_slug>/iterN/`. `<task_slug>` =
practice-area + task name (e.g. `immigration_compare-immigration`); `iterN`
matches the mutator iteration whose harness produced it (iter0 = bare baseline).

Per-iter files:
| file | format | contents |
|---|---|---|
| `transcript.jsonl` | JSONL | the agent run (see schema below) |
| `task.md` | markdown | the task instructions given to the Harvey agent |
| `metrics.json` | JSON | token / turn / doc / file-op counts |
| `grade.json` | JSON | ensemble pass-rate + FAILED criteria |
| `deliverable.md` | markdown | the graded memo (present only on the harvested/representative iter) |
| `output/<name>.docx` (+ `<name>.md` / `response.md`) | docx/md | the actual artifact the agent wrote (always present) |

### B.1 `transcript.jsonl` schema

One object per line. Each carries `turn` (int) + `role`. Example: 39 lines,
roles `{system:1, user:1, assistant:16, tool:21}`.

- `{turn, role:"system", text}` — the harness system prompt.
- `{turn, role:"user", text}` — the task instruction.
- **`{turn, role:"assistant", text, tool_calls[], input_tokens,
  output_tokens, cache_read_input_tokens, cache_creation_input_tokens}`** —
  `tool_calls[] = [{name:"bash", arguments:"<JSON string>"}]` (note `arguments`
  is a JSON-encoded **string**, not an object; tool names are lowercase, e.g.
  `bash`). Per-turn token counts live on the assistant line. The final assistant
  line may have `text:null` / `content:null`.
- **`{turn, role:"tool", tool_name:"bash", arguments:"<JSON string>",
  result_preview, result}`** — `result` = full tool stdout, `result_preview` =
  truncated. The agent writes its deliverable via a `bash` tool call targeting
  `$OUTPUT_DIR` (env vars `$WORKSPACE_DIR/$DOCUMENTS_DIR/$OUTPUT_DIR`).

**Final deliverable** is NOT a transcript field — it's the file written to
`output/` (graded artifact, usually a `.docx`; `metrics.documents_read_list`
includes the written output path). The harvested `deliverable.md` (iter
top-level) is the convenience copy of that memo.

### B.2 `metrics.json`

```
model:"glm-5p2", task:"immigration/compare-immigration",
run_id:"effround1_train_iter2/immigration_compare-immigration__<hash>",
turn_count:16,
input_tokens:636400, output_tokens:32181, total_tokens:668581,
cache_read_input_tokens, cache_creation_input_tokens,
wall_clock_seconds:327.66, finished_cleanly:true, completed_at:"<iso8601>",
documents_read:10, documents_read_list:[…], documents_skipped, documents_skipped_list,
total_documents:9,
bash_commands:9, files_written:1, files_edited:0, glob_searches:0, grep_searches:0
```
(Harvey rollouts are ~98% input tokens — note the in:out ratio here ≈ 20:1.)

### B.3 `grade.json`

```
task:"immigration/compare-immigration",
ens_pass_rate:0.7674,           # ENSEMBLE pass rate = n_passed / n_graded
n_graded:43, n_failed:10,
failed_criteria:[ { id:"C-010",
                    title:"Identifies job title discrepancy …",
                    match_criteria:"PASS if … FAIL if …" }, … ],
error:null
```
> Per-rollout `grade.json` lists **only the FAILED** criteria (id/title/
> match_criteria; no `verdict` field). The **full per-criterion PASS/FAIL verdict
> list** for every task is in the `results/standard_eval_*.json` files — see §C.

---

## C. RESULTS — `results/standard_eval_<prefix>_<split>_iterN.json`

One file per (run, split, iter). `prefix` encodes run+split+iter
(e.g. `effround1_val_iter4`); split ∈ `{train, val, canary}`. Train/val files
≈ 0.75 MB (30 tasks); canary files ≈ 24 KB (smoke subset).

Top-level object:
```
prefix:"effround1_val_iter4",
skill:"/tmp/tmp….md",         # path to the skill/playbook variant evaluated
model:"glm-5p2",
combined_score:0.80798,        # the headline number (mirrors series.json)
n_tasks:30,
tasks: { "<task_slug>": <PerTask>, … }   # dict keyed by task
```

**`<PerTask>`** (the structure the build asked for):
```
pass_rate:0.3091,              # this task's pass rate across its criteria×replicates
n:55,                          # graded judgments for this task
run_dir:"/tmp/harvey_overlay_…/results/<prefix>/<task>…",
criteria:[ { id:"C-001",
             title:"ISSUE_001: Identifies TX/OK/LA reefer as highest-risk submarket",
             match_criteria:"PASS if … FAIL if …",
             verdict:"PASS" | "FAIL" },   # <-- per-criterion verdict (full list, pass AND fail)
           … ]
}
```

So: **`results/standard_eval_*.json` = full per-criterion verdicts** (use for
heatmaps / criterion drill-down); **`rollouts/<task>/iterN/grade.json` =
per-rollout summary + failed criteria only** (use for per-rollout cards). The
two are consistent; `grade.json.ens_pass_rate` and
`standard_eval…tasks[task].pass_rate` measure the same task from the harvested
vs the eval-time runs.

---

## D. Headline curves (for the top-of-page chart)

`<run>/series.json`:
```
{ "train":[ {iter:0, combined_score:0.8423}, … ],
  "val":  [ {iter:0, combined_score:0.7759}, … ] }
```
`<run>/full_stats.json` adds `best_by_val`, `best_by_train`, `overfit_iters`.
`<run>/broker_ledger.json` (+ `broker_ledger.iterN.json`) = the mutator's
experiment-cost ledger:
```
{ cap:160.0, spent:71.12,
  by_source:{ run_harvey_agent:…, proxy_eval:…, dev_eval:… },
  events:[ { source:"run_harvey_agent", cost:1.0,
             task:"corporate-ma/analyze-cim-deal-teaser/scenario-02",
             run_dir, input_tokens, output_tokens, total_tokens,
             cache_read_input_tokens, turns }, … ] }
```
This is the ground truth for "how many experiments / how much money the mutator
spent searching" per iteration.
