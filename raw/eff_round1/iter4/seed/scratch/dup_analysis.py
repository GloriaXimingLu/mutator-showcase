import json, glob, os, hashlib, sys
from collections import defaultdict

ROOT = "/workspace/rollouts"

def analyze(task_dir, it="iter0"):
    tpath = os.path.join(task_dir, it, "transcript.jsonl")
    if not os.path.exists(tpath): return None
    task = os.path.basename(task_dir.rstrip("/"))
    # collect tool results in order
    reads = defaultdict(list)   # file_path -> list of (turn, len, hash)
    tool_results = []           # (turn, name, args, len, hash)
    for line in open(tpath):
        d = json.loads(line)
        if d.get("role") != "tool": continue
        res = d.get("result") or ""
        h = hashlib.md5(res.encode()).hexdigest()
        nm = d.get("tool_name","")
        args = d.get("arguments","")
        tool_results.append((d.get("turn"), nm, args, len(res), h))
    # find duplicate identical large results
    by_hash = defaultdict(list)
    for turn, nm, args, ln, h in tool_results:
        if ln >= 6000:
            by_hash[h].append((turn, nm, ln, args[:60]))
    dup_bytes = 0
    dup_groups = 0
    for h, occ in by_hash.items():
        if len(occ) > 1:
            dup_groups += 1
            ln = occ[0][2]
            dup_bytes += ln * (len(occ)-1)  # all but newest are redundant
    total_result_bytes = sum(ln for _,_,_,ln,_ in tool_results if ln>=6000)
    return task, len(tool_results), total_result_bytes, dup_groups, dup_bytes, by_hash

# rank all iter0 tasks by dup bytes
rows=[]
for td in sorted(glob.glob(os.path.join(ROOT,"*",""))):
    if os.path.basename(td.rstrip("/"))=="_stats": continue
    r = analyze(td)
    if r: rows.append(r)
rows.sort(key=lambda x:-x[4])
print(f"{'task':52} {'#res':>5} {'bigbytes':>11} {'dupgrp':>6} {'dupbytes':>11} {'dup%':>5}")
for task,nres,tot,dg,db,_ in rows:
    pct = db/tot*100 if tot else 0
    print(f"{task[:52]:52} {nres:>5} {tot:>11,} {dg:>6} {db:>11,} {pct:>4.0f}%")
