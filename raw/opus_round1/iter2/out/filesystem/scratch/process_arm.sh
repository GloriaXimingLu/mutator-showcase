#!/usr/bin/env bash
# Usage: process_arm.sh <ARM> <task_id ...>
# After a run_harvey_agent batch, proxy_eval each task and archive deliverable+score+turns
# into scratch/arms/<ARM>/<task_underscored>/. Prints a per-task summary line.
set -u
ARM="$1"; shift
DEST=/workspace/scratch/arms/$ARM
mkdir -p "$DEST"
for task in "$@"; do
  u=$(echo "$task" | tr '/' '_')
  run=/workspace/scratch/runs/$u
  if [ ! -f "$run/deliverable.md" ]; then echo "  [$ARM] $task : NO DELIVERABLE"; continue; fi
  # proxy grade (writes proxy_score.json next to deliverable)
  /workspace/.claude/tools/proxy_eval "$task" "$run/deliverable.md" >/dev/null 2>"$DEST/.proxyerr"
  od="$DEST/$u"; mkdir -p "$od"
  cp "$run/deliverable.md" "$od/" 2>/dev/null
  cp "$run/proxy_score.json" "$od/" 2>/dev/null
  cp "$run/turns.txt" "$od/" 2>/dev/null
  pr=$(python3 -c "import json,sys;print('%.3f'%json.load(open('$od/proxy_score.json'))['pass_rate'])" 2>/dev/null || echo "NA")
  tn=$(cat "$od/turns.txt" 2>/dev/null || echo "?")
  echo "  [$ARM] $task : proxy=$pr turns=$tn"
done
