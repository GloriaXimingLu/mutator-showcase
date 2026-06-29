# Harvey harness (bare — this is what you optimize)

This directory holds the **editable surface of the bare Harvey harness** — no skill, no
playbook. It is seeded from the canonical harness (`baseline-submodules/harvey-labs`, the same
checkout that produced the bare baseline) before each run, so three files appear here:

| File | What it is | What an edit does |
|---|---|---|
| `system_prompt.md` | The agent's **system-prompt preamble** (workspace layout + tool conventions), prepended to every run; the file-format skill manuals (.docx/.xlsx/.pptx) are appended after it. | The prose lever — add standing method/guidance (this is where a "playbook" would now live, but you decide if prose is the highest-leverage change). |
| `tools.py` | The **tools the Harvey agent calls** during a run — today 6 shell tools (`bash read write edit glob grep`) over a sandbox. | Add a new action the agent can take, or sharpen a tool. |
| `agent_loop.py` | The **control flow**: call the model, run its tool calls, repeat until it stops or hits `max_turns`. Today a flat loop. | Add structure — compaction (a running `memo.md`), a plan→execute pass, a validate→revise step. |

You **start from bare and discover what to add** — there is no seed skill. Edit these files in
place; at rollout time the full harness is reconstituted from the submodule (the model adapters,
`run.py`, the sandbox, the tasks) and **your edited files are overlaid on top**, so a change here
takes effect in the run and is what gets scored.

You do **not** run this harness code in your own container — `run_harvey_agent` executes it
host-side on a real task and returns the deliverable + score. Edit the files; validate with an
experiment.

**Routing rule:** a tool the **Harvey agent** uses during its run → here (`harness/tools.py`). A
tool that helps **you** optimize (run an experiment, grade a draft, check budget) →
`.claude/tools/`. Only `harness/**` is scored.
