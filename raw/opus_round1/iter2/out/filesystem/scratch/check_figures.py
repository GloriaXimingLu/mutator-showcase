#!/usr/bin/env python3
"""Private triage: count how many rubric-correct figures appear in a deliverable.

Usage: check_figures.py <task_id> <deliverable_path>
Normalizes numbers (strips $ , whitespace) so "$2,558.40" matches "2558.40".
A figure with a trailing ".00" also matches the integer form and vice-versa.
"""
import json, re, sys

TARGETS = json.load(open("/workspace/scratch/numeric_targets.json"))

def norm(s):
    return re.sub(r"[,\s$]", "", s)

def variants(t):
    t = norm(t)
    out = {t}
    if t.endswith(".00"):
        out.add(t[:-3])
    if "." not in t:
        out.add(t + ".00")
    return out

def main():
    task, path = sys.argv[1], sys.argv[2]
    spec = TARGETS.get(task)
    if not spec:
        print(f"no targets for {task}"); return
    text = norm(open(path, encoding="utf-8", errors="replace").read())
    hits, miss = [], []
    for tgt in spec["targets"]:
        if any(v in text for v in variants(tgt)):
            hits.append(tgt)
        else:
            miss.append(tgt)
    print(f"{task}: {len(hits)}/{len(spec['targets'])} target figures present")
    print(f"  hit : {hits}")
    print(f"  MISS: {miss}")

if __name__ == "__main__":
    main()
