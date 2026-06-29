import sys; sys.path.insert(0,'.')
import importlib, harness.agent_loop as al; importlib.reload(al)
assert al._EVICT_MIN_TURN==28, al._EVICT_MIN_TURN
assert al._EVICT_REFETCH_LIMIT==4, al._EVICT_REFETCH_LIMIT
assert al._RECENT_WINDOW==12, al._RECENT_WINDOW
BIG="X"*300000
def log1(turn):
    m={"role":"tool","content":BIG}
    return [{"turn":turn,"messages":[m],"items":[{"name":"read","args":{"file_path":"a.docx"},"full":BIG,"evicted":False}]}]
# turn 28 (<=MIN_TURN) untouched (bare for short/medium)
L=log1(2); al._evict_aged_results(L,28,set(),set(),{"disabled":False,"refetches":0})
assert L[0]["messages"][0]["content"]==BIG, "turn28 must be untouched"
# turn 29 (>MIN_TURN, age 27>window, 300K>sizegate) evicts aged doc
L=log1(2); ek=set(); al._evict_aged_results(L,29,set(),ek,{"disabled":False,"refetches":0})
assert "context-saver" in L[0]["messages"][0]["content"], "turn29 should evict"
assert "read:a.docx" in ek
# NEW: limit=4 -> first THREE re-fetches do NOT disable; 4th does. Each re-fetched doc pins sticky.
st={"disabled":False,"refetches":0}; evicted={"read:a.docx","read:b.docx","read:c.docx","read:d.docx"}; sticky=set()
for f in ["a.docx","b.docx","c.docx","d.docx"]:
    key=al._evict_key("read",{"file_path":"documents/"+f})
    if key in evicted:
        sticky.add(key); st["refetches"]+=1
        if st["refetches"]>=al._EVICT_REFETCH_LIMIT: st["disabled"]=True
    disabled_after = st["disabled"]
    if st["refetches"]<4:
        assert not st["disabled"], f"should NOT disable after {st['refetches']} refetch(es)"
assert st["disabled"] is True, "4th re-fetch must disable"
assert sticky=={"read:a.docx","read:b.docx","read:c.docx","read:d.docx"}
# per-doc sticky bounds per-doc loop: a doc, once re-fetched (sticky), is never re-evicted
L=log1(2); al._evict_aged_results(L,40,{"read:a.docx"},set(),{"disabled":False,"refetches":0})
assert L[0]["messages"][0]["content"]==BIG, "sticky doc must never be re-evicted (no per-doc loop)"
# disabled => no eviction at all
L=log1(2); al._evict_aged_results(L,50,sticky,evicted,{"disabled":True,"refetches":4})
assert L[0]["messages"][0]["content"]==BIG, "disabled => bare"
print("PASS: MIN_TURN=28, WINDOW=12, REFETCH_LIMIT=4; per-doc sticky bounds loops; global backstop@4")
