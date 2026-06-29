import sys, json, importlib.util
# Load the eviction helpers directly from agent_loop without importing harness deps.
import types
# Stub the harness.adapters.base and harness.tools imports.
mod = types.ModuleType("harness"); sys.modules["harness"]=mod
adp = types.ModuleType("harness.adapters"); sys.modules["harness.adapters"]=adp
base = types.ModuleType("harness.adapters.base"); base.ModelAdapter=object; base.ModelResponse=object
sys.modules["harness.adapters.base"]=base
tools = types.ModuleType("harness.tools"); tools.ToolExecutor=object; tools.get_all_tool_definitions=lambda: []
sys.modules["harness.tools"]=tools

spec = importlib.util.spec_from_file_location("agent_loop", "harness/agent_loop.py")
al = importlib.util.module_from_spec(spec); spec.loader.exec_module(al)

BIG = "X"*60000  # ~15k tokens, a "document"
SMALL = "ok"

# ---- Anthropic-style: one user message per turn, content = list of blocks ----
def anth_results(pairs):
    return [{"role":"user","content":[{"type":"tool_result","tool_use_id":tid,"content":res} for tid,res in pairs]}]

# ---- OpenAI-style: one message per tool result ----
def oai_results(pairs):
    return [{"role":"tool","tool_call_id":tid,"content":res} for tid,res in pairs]

for style,builder in [("anthropic",anth_results),("openai",oai_results)]:
    messages=[{"role":"system","content":"sys"},{"role":"user","content":"task"}]
    tool_log=[]
    # turn 2: read big doc + small
    class TC:
        def __init__(s,n,i,a): s.name=n; s.id=i; s.arguments=a
    rms=builder([("t1",BIG),("t2",SMALL)])
    messages.extend(rms)
    tool_log.append({"turn":2,"messages":rms,"items":[
        {"name":"read","args":{"file_path":"documents/big.docx"},"full":BIG,"evicted":False},
        {"name":"read","args":{"file_path":"documents/s.txt"},"full":SMALL,"evicted":False}]})
    # turn 3 bash big
    rms2=builder([("t3",BIG)])
    messages.extend(rms2)
    tool_log.append({"turn":3,"messages":rms2,"items":[
        {"name":"bash","args":{"command":"cat documents/big2"},"full":BIG,"evicted":False}]})

    def total_chars(ms): return len(json.dumps(ms))
    before=total_chars(messages)
    # at turn 5: window=4 -> nothing aged yet (5-2=3 < 4). expect no change.
    al._evict_aged_results(tool_log,5)
    mid=total_chars(messages)
    # at turn 7: 7-2=5>=4 evict turn2 big; 7-3=4>=4 evict turn3 big.
    al._evict_aged_results(tool_log,7)
    after=total_chars(messages)
    # idempotent re-run
    al._evict_aged_results(tool_log,8)
    after2=total_chars(messages)
    blob=json.dumps(messages)
    print(f"[{style}] before={before:,} turn5={mid:,} turn7={after:,} turn8={after2:,}")
    assert mid==before, "should not evict inside window"
    assert after < before*0.2, "should have evicted both big docs"
    assert after2==after, "idempotent"
    assert "context-saver" in blob, "stub present"
    assert BIG not in blob, "big doc fully removed"
    assert SMALL in blob, "small result kept"
    assert "documents/big.docx" in blob, "read handle has filepath"
    assert "cat documents/big2" in blob, "bash handle has command"
    # task + system preserved
    assert any(m.get("role")=="system" for m in messages) and any(m.get("content")=="task" for m in messages)
    print(f"[{style}] OK — evicted to {after/before:.1%} of original, handles + task preserved")
print("ALL TESTS PASSED")
