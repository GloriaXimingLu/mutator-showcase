import sys; sys.path.insert(0,'.')
import importlib, harness.agent_loop as al; importlib.reload(al)
assert al._EVICT_MIN_TURN==28, al._EVICT_MIN_TURN
assert al._EVICT_REFETCH_LIMIT==1, al._EVICT_REFETCH_LIMIT
BIG="X"*300000
def log1(turn): 
    m={"role":"tool","content":BIG}
    return [{"turn":turn,"messages":[m],"items":[{"name":"read","args":{"file_path":"a.docx"},"full":BIG,"evicted":False}]}]
# turn 28 (<=MIN_TURN) untouched
L=log1(2); al._evict_aged_results(L,28,set(),set(),{"disabled":False,"refetches":0})
assert L[0]["messages"][0]["content"]==BIG, "turn28 must be untouched"
# turn 29 (>MIN_TURN) evicts aged doc
L=log1(2); ek=set(); al._evict_aged_results(L,29,set(),ek,{"disabled":False,"refetches":0})
assert "context-saver" in L[0]["messages"][0]["content"], "turn29 should evict"
assert "read:a.docx" in ek
# refetch-limit=1: simulate loop logic — one re-fetch disables
st={"disabled":False,"refetches":0}; evicted={"read:a.docx"}; sticky=set()
key=al._evict_key("read",{"file_path":"documents/a.docx"})
if key in evicted:
    sticky.add(key); st["refetches"]+=1
    if st["refetches"]>=al._EVICT_REFETCH_LIMIT: st["disabled"]=True
assert st["disabled"] is True, "first re-fetch must disable"
# disabled => no eviction even on long turn
L=log1(2); al._evict_aged_results(L,40,sticky,evicted,st)
assert L[0]["messages"][0]["content"]==BIG, "disabled after 1 refetch => no eviction"
print("NEW-CONFIG LOGIC TESTS PASSED (MIN_TURN=28, REFETCH_LIMIT=1)")
