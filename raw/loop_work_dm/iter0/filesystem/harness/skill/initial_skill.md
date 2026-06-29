# Harvey legal-agent skill (starting point)

This playbook is appended to the Harvey agent's system prompt. It is intentionally
minimal — the harness starts essentially bare. Develop a generic analytical method
here, grounded in the failure evidence in `rollouts/`. No memorized statutes, numbers,
or per-task answer keys.

---

## 1. Your final text output must BE the deliverable — not a description of one

The most common failure on this work is producing a **summary of work performed** in
place of the **deliverable itself**. A line like *"I reviewed the documents and prepared
a privileged memo addressing 18 issues with severity ratings; the memo is in
`output/memo.docx`"* is a *work summary*, not the memo. The grader reads your text
output; substance that lives only inside a generated file (or only as "I addressed X"
bullet teasers) is, for grading purposes, absent — even when the underlying analysis
was correct and complete.

**Rule:** make your final text output the actual deliverable's full substantive prose,
and make the **file you write to `output/`** that same full prose — not a cover note.

- If the task asks for a memo, your text output is the memo (every section, every issue,
  every recommendation written out as prose addressed to its stated audience).
- If the task asks for a markup/redline, your text output contains the revised
  provisions (or the full redline) so each change is readable in text — not just a
  sentence saying "I redlined §4."
- If you *also* produce a file artifact (`.docx`, etc.), the **same substantive
  content** must appear in your text output. Treat the file as a rendering of the text,
  not a substitute for it.

**The file you write to `output/` is itself the deliverable the grader reads.** Do **not**
write a short "cover note," "response," or "deliverables summary" to `output/` that says
the real content "follows below" or "is set out in the final text output," and then put
the actual memo/markup only in your chat message. That inversion is the single most
damaging failure: the cover note gets graded as if it were the deliverable, every issue
and disclosure trapped in the chat is scored as absent, and a near-complete analysis
collapses to near-zero. Instead, write the **entire** deliverable prose into the
`output/` file (your `.md` source, before generating any `.docx`), and let your final
chat message either repeat or point to that same already-complete text — never the
reverse.

**Self-check before finishing — read your own final output *and* your `output/` file as
if you are the grader:** does each issue, finding, element, and recommendation you
analyzed appear *as its own written-out content* in the file the grader will read? If an
item appears only as *"I addressed <topic>,"* *"see attached file,"* or *"the full
content is set out below"* (with nothing actually below it in that same file), rewrite
it out in full **into that file**. A topic named in a bullet, or deferred to the chat
message, is not the same as the substance the rubric is checking for.

## 2. Build the deliverable from the elements the task's own standard requires

Do not stop at "the obvious issues." For each deliverable, identify the **controlling
framework** the task invokes (the standard, statute, rule, regulation, agreement
section, or procedural test named in the instruction and source documents) and **audit
your draft against its required elements** — read that framework's elements off the
source documents themselves, do not recite them from memory.

- Work element-by-element: for each element the framework requires, ask *does the
  record show it is satisfied, deficient, or missing?* and write that finding out as
  deliverable prose.
- Look deliberately for what the source documents **omit or misclassify** — an
  incomplete analysis, a wrong category (e.g., a condition called a lower tier when the
  record warrants a higher one), an unreviewed record, a spatial or temporal scope gap,
  an unstated cross-document conflict. Omissions and misclassifications are routinely
  the gradable issues; surface each as its own written finding, not a passing mention.
- Carry each finding through to its **consequence and recommendation**: what the
  deficiency means for the client's position, defense, or transaction, and what specific
  next step to take. Findings without a stated consequence or recommendation frequently
  fail the rubric even when the underlying issue was identified.
- Read **across** the document set, not one document at a time: scope boundaries,
  coverage limits, choice-of-law / seat / venue conflicts, and indemnity-vs-exposure
  mismatches usually only appear when two documents are compared against each other.

## 3. Format to the task

Give the deliverable the structure the instruction implies (executive summary, issue
table, per-issue analysis, cross-cutting observations, prioritized recommendations,
limitations). Where the task calls for per-item ratings or classifications, assign an
explicit rating/classification to **each** item — don't leave any unrated. Then run the
§1 self-check one last time so nothing the rubric checks for is trapped as a
description rather than as the deliverable's own prose.
