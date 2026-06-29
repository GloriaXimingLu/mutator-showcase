---
name: run-harvey-agent-must-background
description: run_harvey_agent batches exceed the 10-min Bash tool cap; run them in the background or you pay but lose the deliverables.
metadata:
  type: feedback
---

A `run_harvey_agent` batch of ~5 tasks takes ~15-20 min wall-clock (each rollout ~9-10 min,
broker runs only a few concurrently). The Bash tool **kills the client at 10 min**, but the broker
keeps running and **still charges** — you pay (e.g. $5/5 tasks) and get **zero deliverables**
(nothing written to scratch/runs/). Verified: lost $5 this way on the first BARE batch.

**Why:** the client POSTs and blocks up to 2400s for the broker response; if the shell is killed,
the response (with deliverables) is discarded but the spend already happened.

**How to apply:** ALWAYS launch `run_harvey_agent` with `run_in_background: true` (Bash tool) so the
detached client survives past 10 min and writes deliverables when the broker returns. Run arms
**sequentially** (one 5-task batch at a time) so the broker isn't overloaded and each client finishes
well under its 2400s client timeout. Only swap `harness/` (set_arm.sh) AFTER a batch's client has
posted — the client reads harness/ at startup, so a fresh background launch captures it immediately.
Run arms sequentially (wait for each background batch's completion notification before swapping
harness/ and launching the next). See [[iter2-additive-method-edits-backfire]].
