import json, sys, glob, os
from collections import defaultdict

def analyze(path, window=12, min_turn=28, min_evict_chars=6000):
    rows=[]
    with open(path) as f:
        for line in f:
            rows.append(json.loads(line))
    # build per-turn messages
    sys_sz=user_sz=0
    # assistant msgs: turn -> (text_chars, toolcall_chars split by write/edit vs other)
    asst=defaultdict(lambda:{"text":0,"write_edit":0,"other_tc":0})
    # tool results: turn -> list of (name, chars)
    toolres=defaultdict(list)
    maxturn=0
    for r in rows:
        role=r.get("role")
        t=r.get("turn",0)
        maxturn=max(maxturn,t)
        if role=="system": sys_sz=len(r.get("text") or "")
        elif role=="user": user_sz=len(r.get("text") or "")
        elif role=="assistant":
            asst[t]["text"]+=len(r.get("text") or "")
            for tc in (r.get("tool_calls") or []):
                args=tc.get("arguments")
                s=len(args if isinstance(args,str) else json.dumps(args))
                if tc.get("name") in ("write","edit"): asst[t]["write_edit"]+=s
                else: asst[t]["other_tc"]+=s
        elif role=="tool":
            res=r.get("result") or ""
            toolres[t].append((r.get("tool_name"), len(res)))
    T=maxturn
    # cumulative carried input attribution (chars * times carried)
    cat=defaultdict(int)
    cat["system"]=sys_sz*T
    cat["user"]=user_sz*T
    for t in range(1,T+1):
        carried=T-t  # times this turn's msgs appear in later prompts
        cat["asst_text"]+=asst[t]["text"]*carried
        cat["asst_write_edit"]+=asst[t]["write_edit"]*carried
        cat["asst_other_tc"]+=asst[t]["other_tc"]*carried
        for name,sz in toolres[t]:
            evictable = name in ("read","bash","grep","glob")
            # simulate iter2 eviction: evictable, big, aged beyond window, run>min_turn
            key = "toolres_evictable" if evictable else "toolres_other"
            cat[key]+=sz*carried
            # residual after eviction: kept only for `window` turns if it would be evicted
            if evictable and sz>=min_evict_chars and T>min_turn:
                kept=min(carried, window)
                cat["RESID_evicted_kept"]+=sz*kept
            else:
                cat["RESID_evicted_kept"]+=sz*carried
    total=sum(v for k,v in cat.items() if not k.startswith("RESID"))
    return T, cat, total

for path in sys.argv[1:]:
    T,cat,total=analyze(path)
    name=path.split("/rollouts/")[-1]
    print(f"\n=== {name}  (turns={T}, est_bare_carried≈{total//4//1000}K tok) ===")
    def pct(k): return f"{cat[k]//4//1000:>6}K  {100*cat[k]/total:5.1f}%"
    print(f"  system        {pct('system')}")
    print(f"  user          {pct('user')}")
    print(f"  asst_text     {pct('asst_text')}")
    print(f"  asst_WRITE/EDIT {pct('asst_write_edit')}   <-- agent's own draft bytes (NOT evicted)")
    print(f"  asst_other_tc {pct('asst_other_tc')}")
    print(f"  toolres_evictable {pct('toolres_evictable')}  <-- eviction target")
    print(f"  toolres_other {pct('toolres_other')}")
    # residual after iter2 eviction
    resid_evict=cat["RESID_evicted_kept"]
    nonevict = total - cat["toolres_evictable"]
    resid_total = nonevict + resid_evict
    print(f"  --> est residual AFTER iter2 eviction ≈ {resid_total//4//1000}K tok ({100*resid_total/total:.0f}% of bare); of which write/edit={cat['asst_write_edit']//4//1000}K, recent-window toolres={resid_evict//4//1000}K")
