import sys; sys.path.insert(0, '.')
import harness.agent_loop as al

# ---- _evict_key generalization ----
assert al._evict_key("read", {"file_path":"documents/x.docx"}) == "read:x.docx"
assert al._evict_key("read", {"file_path":"/abs/path/x.docx"}) == "read:x.docx"
assert al._evict_key("bash", {"command":"  pdftotext a.pdf  "}) == "bash:pdftotext a.pdf"
assert al._evict_key("grep", {"pattern":"foo","path":"docs"}) == "grep:foo:docs"
assert al._evict_key("read", {}) is None
print("evict_key OK")

def make_msg(text): return {"role":"tool","content":text}

def build_log(reads):
    # reads: list of (turn, name, args, fulltext)
    log=[]
    for turn,name,args,full in reads:
        msg=make_msg(full)
        log.append({"turn":turn,"messages":[msg],
                    "items":[{"name":name,"args":args,"full":full,"evicted":False}]})
    return log

BIG = "X"*300000  # 300k chars, over size gate, over minchars

# ---- task-length gate: short task (<=MIN_TURN) never evicts ----
log = build_log([(2,"read",{"file_path":"a.docx"},BIG)])
st={"disabled":False,"refetches":0}
al._evict_aged_results(log, current_turn=18, sticky_keys=set(), evicted_keys=set(), evict_state=st)
assert log[0]["messages"][0]["content"] == BIG, "short task should be untouched"
assert log[0]["items"][0]["evicted"] is False
print("min-turn gate OK (short task untouched)")

# ---- long task past gate: aged big doc gets evicted to a stub ----
log = build_log([(2,"read",{"file_path":"a.docx"},BIG)])
ek=set()
al._evict_aged_results(log, current_turn=30, sticky_keys=set(), evicted_keys=ek, evict_state={"disabled":False,"refetches":0})
assert "context-saver" in log[0]["messages"][0]["content"], "aged doc should be evicted"
assert "read:a.docx" in ek
print("long task eviction OK")

# ---- recent window: doc within window stays full even on long task ----
log = build_log([(25,"read",{"file_path":"a.docx"},BIG)])
al._evict_aged_results(log, current_turn=30, sticky_keys=set(), evicted_keys=set(), evict_state={"disabled":False,"refetches":0})
assert log[0]["messages"][0]["content"] == BIG, "doc within window should stay full"
print("window OK")

# ---- sticky: a key in sticky_keys is never evicted ----
log = build_log([(2,"read",{"file_path":"a.docx"},BIG)])
al._evict_aged_results(log, current_turn=30, sticky_keys={"read:a.docx"}, evicted_keys=set(), evict_state={"disabled":False,"refetches":0})
assert log[0]["messages"][0]["content"] == BIG, "sticky doc stays full"
print("sticky OK")

# ---- kill-switch: disabled state short-circuits ----
log = build_log([(2,"read",{"file_path":"a.docx"},BIG)])
al._evict_aged_results(log, current_turn=30, sticky_keys=set(), evicted_keys=set(), evict_state={"disabled":True,"refetches":2})
assert log[0]["messages"][0]["content"] == BIG, "disabled => no eviction"
print("kill-switch disabled OK")

print("ALL LOGIC TESTS PASSED")
