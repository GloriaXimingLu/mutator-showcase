import sys, json, importlib.util, types
mod = types.ModuleType("harness"); sys.modules["harness"]=mod
adp = types.ModuleType("harness.adapters"); sys.modules["harness.adapters"]=adp
base = types.ModuleType("harness.adapters.base"); base.ModelAdapter=object; base.ModelResponse=object
sys.modules["harness.adapters.base"]=base
tools = types.ModuleType("harness.tools"); tools.ToolExecutor=object; tools.get_all_tool_definitions=lambda: []
sys.modules["harness.tools"]=tools
spec = importlib.util.spec_from_file_location("agent_loop", "harness/agent_loop.py")
al = importlib.util.module_from_spec(spec); spec.loader.exec_module(al)
print("window=",al._RECENT_WINDOW,"minchars=",al._MIN_EVICT_CHARS)
BIG="X"*60000
def anth(pairs): return [{"role":"user","content":[{"type":"tool_result","tool_use_id":t,"content":r} for t,r in pairs]}]

# --- stickiness test ---
messages=[{"role":"system","content":"sys"},{"role":"user","content":"task"}]
tool_log=[]; evicted=set(); sticky=set()
def rec(turn,name,fp,full,tid):
    rms=anth([(tid,full)]); messages.extend(rms)
    # mimic loop: mark sticky if re-read of evicted
    if name=="read" and fp in evicted: sticky.add(fp)
    tool_log.append({"turn":turn,"messages":rms,"items":[{"name":name,"args":{"file_path":fp},"full":full,"evicted":False}]})

rec(2,"read","documents/agreement.docx",BIG,"a")   # first read
al._evict_aged_results(tool_log,7,sticky,evicted)   # turn7: age=5>=5 -> evict, evicted={agreement}
assert "context-saver" in json.dumps(messages) and BIG not in json.dumps(messages), "first read evicted"
assert "documents/agreement.docx" in evicted
# agent re-reads at turn 8 (saw stub)
rec(8,"read","documents/agreement.docx",BIG,"b")
assert "documents/agreement.docx" in sticky, "re-read -> sticky"
# now age out the re-read at turn 14 (14-8=6>=5) -> must STAY (sticky)
al._evict_aged_results(tool_log,14,sticky,evicted)
blob=json.dumps(messages)
assert blob.count(BIG)==1, f"sticky re-read must stay resident, found {blob.count(BIG)} copies"
print("STICKY OK: doc evicted once, re-read stays resident; no churn")

# --- non-sticky doc still evicts (read once, never re-read) ---
messages2=[{"role":"system","content":"s"}]; tl2=[]; ev2=set(); st2=set()
rms=anth([("z",BIG)]); messages2.extend(rms)
tl2.append({"turn":2,"messages":rms,"items":[{"name":"read","args":{"file_path":"documents/once.docx"},"full":BIG,"evicted":False}]})
al._evict_aged_results(tl2,9,st2,ev2)
assert BIG not in json.dumps(messages2), "read-once doc must evict"
print("EVICT-ONCE OK: read-once doc still evicted (big win preserved)")
print("ALL PASS")
