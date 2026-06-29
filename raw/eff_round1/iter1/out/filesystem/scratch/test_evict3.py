import sys, json, importlib.util, types
for m,attrs in [("harness",{}),("harness.adapters",{}),
                ("harness.adapters.base",{"ModelAdapter":object,"ModelResponse":object}),
                ("harness.tools",{"ToolExecutor":object,"get_all_tool_definitions":(lambda:[])})]:
    mod=types.ModuleType(m); [setattr(mod,k,v) for k,v in attrs.items()]; sys.modules[m]=mod
spec=importlib.util.spec_from_file_location("agent_loop","harness/agent_loop.py")
al=importlib.util.module_from_spec(spec); spec.loader.exec_module(al)
print("window",al._RECENT_WINDOW,"minchars",al._MIN_EVICT_CHARS,"sizegate",al._SIZE_GATE_CHARS)
BIG="X"*120000  # 120k chars, one big doc
def anth(pairs): return [{"role":"user","content":[{"type":"tool_result","tool_use_id":t,"content":r} for t,r in pairs]}]

# --- 1. SIZE GATE: small task (resident < gate) -> NO eviction ---
msgs=[{"role":"system","content":"s"}]; tl=[]; ev=set(); st=set()
small=anth([("a","Y"*100000)])  # 100k < 500k gate
msgs.extend(small); tl.append({"turn":2,"messages":small,"items":[{"name":"read","args":{"file_path":"a.docx"},"full":"Y"*100000,"evicted":False}]})
al._evict_aged_results(tl,20,st,ev)  # way past window, but under gate
assert "Y"*100000 in json.dumps(msgs), "under size gate must NOT evict"
print("SIZE-GATE OK: small task untouched (bare behavior, zero accuracy risk)")

# --- 2. big task (resident > gate) -> evicts aged ---
msgs=[{"role":"system","content":"s"}]; tl=[]; ev=set(); st=set()
for i in range(5):  # 5*120k = 600k > 500k gate
    r=anth([(f"d{i}",BIG)]); msgs.extend(r)
    tl.append({"turn":2+i,"messages":r,"items":[{"name":"read","args":{"file_path":f"doc{i}.docx"},"full":BIG,"evicted":False}]})
al._evict_aged_results(tl,2+4+8,st,ev)  # turn 14: docs at turns2-6 aged (>=7)
blob=json.dumps(msgs)
assert "context-saver" in blob and blob.count(BIG)<=1, f"over gate should evict aged docs, {blob.count(BIG)} big left"
assert len(ev)>=4, f"evicted keys tracked: {ev}"
print(f"OVER-GATE OK: evicted aged docs, evicted_keys={sorted(ev)}")

# --- 3. BASENAME stickiness across path spellings ---
msgs=[{"role":"system","content":"s"}]; tl=[]; ev=set(); st=set()
# fill over gate with filler so eviction runs
fr=anth([("f","Z"*500000)]); msgs.extend(fr); tl.append({"turn":1,"messages":fr,"items":[{"name":"bash","args":{"command":"cat big"},"full":"Z"*500000,"evicted":False}]})
r1=anth([("x",BIG)]); msgs.extend(r1); tl.append({"turn":2,"messages":r1,"items":[{"name":"read","args":{"file_path":"documents/agreement.docx"},"full":BIG,"evicted":False}]})
al._evict_aged_results(tl,12,st,ev)  # evict agreement -> ev has basename
assert "agreement.docx" in ev, f"basename tracked: {ev}"
# agent re-reads with DIFFERENT spelling (absolute path) -> should become sticky
key=al._read_key({"file_path":"/workspace/documents/agreement.docx"})
assert key=="agreement.docx" and key in ev, "different spelling maps to same basename"
st.add(key)  # mimic loop marking sticky
r2=anth([("y",BIG)]); msgs.extend(r2); tl.append({"turn":13,"messages":r2,"items":[{"name":"read","args":{"file_path":"/workspace/documents/agreement.docx"},"full":BIG,"evicted":False}]})
al._evict_aged_results(tl,25,st,ev)  # turn25: re-read aged, but sticky -> stays
assert json.dumps(msgs).count(BIG)==1, "sticky (basename) re-read must stay resident across spellings"
print("BASENAME-STICKY OK: re-read under any path spelling pins the doc, no churn")
print("ALL PASS")
