#!/usr/bin/env bash
# Usage: set_arm.sh BARE|PROSE|LOOP   -> overlays the chosen variant into harness/
set -e
arm="$1"; V=/workspace/scratch/variants; H=/workspace/harness
case "$arm" in
  BARE)  cp $V/system_prompt.BARE.md  $H/system_prompt.md; cp $V/agent_loop.BARE.py $H/agent_loop.py ;;
  PROSE) cp $V/system_prompt.PROSE.md $H/system_prompt.md; cp $V/agent_loop.BARE.py $H/agent_loop.py ;;
  LOOP)  cp $V/system_prompt.BARE.md  $H/system_prompt.md; cp $V/agent_loop.LOOP.py $H/agent_loop.py ;;
  *) echo "unknown arm: $arm" >&2; exit 2 ;;
esac
echo "harness set to arm=$arm"
md5sum $H/system_prompt.md $H/agent_loop.py
