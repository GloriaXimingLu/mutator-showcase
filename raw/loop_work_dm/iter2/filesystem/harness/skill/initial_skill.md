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

## 2. Extract every distinct issue across the WHOLE document set — do not write a thematic essay around a few chosen headline issues

The most damaging substantive failure (once content is actually on the page) is
**partial coverage**: the agent reads the primary document, picks the two or three
headline themes that stand out, and writes a deep, polished memo about *those* — while
silently dropping a dozen other distinct, equally-specific issues that were sitting in
the very documents it already read. A confident, well-written deliverable that covers
only a self-selected subset of the record's issues scores as if the missing issues were
never analyzed. The deliverable must be an **exhaustive extraction pass** over the
record, not an essay on the parts you found most interesting.

**Rule:** before you draft, enumerate — don't curate.

- **Read every document you were given, including the supporting ones.** Do not stop at
  the primary agreement / report. Policies, internal records, valuations, credential
  evaluations, database appendices, cover letters, expense reports, prior
  correspondence, and government-response letters are each a *source of separate
  findings*, not background color. Many gradable issues live only in a supporting
  document and never appear in the primary one.
- **Cross-reference each supporting document against the primary and against every other
  document.** Every place where two documents disagree — a policy cap vs. a statutory
  maximum, a stated figure vs. a record figure, a representation vs. the underlying
  data, a date in one doc vs. a date in another — is its own numbered finding. These
  cross-document mismatches are the issues most often missed and most often graded.
- **Pull specifics verbatim, never generalize.** If a record states an exact dollar
  figure, account number, date, party name, site identifier, citation, or count, write
  that exact value into the finding. "Substantial spending" where the record says
  "$23,400 in luxury charges, including a $6,200 travel charge on July 8, 2024" is a
  graded miss — the specific number is the finding. Do not paraphrase a precise fact
  into a vague one.
- **Give every distinct issue its own numbered finding, then keep going.** Do not fold
  several issues into one "theme." If the record supports twelve separate problems,
  write twelve findings, each with its own description, evidence, consequence, and
  recommendation — even if some overlap thematically. An issue that exists in the record
  but is not written out as its own finding is, for grading, absent.
- **Check for non-issues too.** Where the record contains a fact that *looks* like a
  problem but is not (a distractor), say so explicitly and explain why it is not an
  issue — flagging a non-issue as a real one is itself a graded error.
- **Never demote or discard a document you were given.** Every document in the
  production is a candidate source of gradable findings — treat it that way even if it
  looks like it describes a different transaction, a different property, a duplicate, a
  stale version, or mere background. Do **not** reclassify a produced document as "wrong
  file / not the subject property / doesn't pertain to this matter / duplicate / out of
  scope" and then relegate every finding it supports to a "secondary," "appendix," "for
  completeness," or "**do not rely**" section. Findings buried in a demoted appendix are
  graded as if they were never written — they must appear as **first-class numbered items
  in the primary deliverable**, alongside findings from the headline document. If two
  documents appear to describe different subjects (different addresses, parties, dates,
  or deals), surface that conflict as its **own** finding — but still mine **both**
  documents fully for every distinct issue each contains, and carry each issue into the
  primary analysis. The cost of wrongly discarding a document is far higher than the cost
  of analyzing one that turns out to be irrelevant: a document you wrote off as "not the
  real subject" is very often the one the rubric is actually testing.
- **Treat the client's own governing documents as controlling authority, not
  background.** Internal policies, plan documents, board resolutions, fee agreements,
  committee charters, and corporate governance documents supplied in the production are
  not color commentary — they state *mandates* (required carve-outs, dollar caps,
  liquidated-damages amounts, duration limits, mutual-obligation rules, approval
  thresholds, board-authorized ranges). Read each one and enforce every mandate it
  states as its own finding/revisision, the same way you would enforce a statute.
  Findings that "would be good practice" but are silently dropped when a supplied policy
  *requires* them are a systematic miss.

**Completeness self-check before finishing.** List every document in the production. For
each, ask: *what distinct findings did this document yield?* Any document whose facts
produced zero findings is a red flag that you skipped it, merged it away, **or demoted
it as "not relevant"** — go back and mine it, then promote its findings into the primary
deliverable. Then ask: *for every specific figure, name, date, and identifier the record
states, is that exact value written into a finding rather than generalized away?* A
supporting document read but not converted into first-class written findings is the same
as not reading it.

## 3. Build the deliverable from the elements the task's own standard requires

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

## 4. Format to the task — and produce every required component with its exact value

Give the deliverable the structure the instruction implies (executive summary, issue
table, per-issue analysis, cross-cutting observations, prioritized recommendations,
limitations). Where the task calls for per-item ratings or classifications, assign an
explicit rating/classification to **each** item — don't leave any unrated.

**Before you draft, enumerate the deliverable's own required components — not just the
issues.** A deliverable is not only a list of findings; it has *structural parts* the
task or the controlling standard requires it to contain, and *computations* the
controlling record requires it to perform. Missing one of these is as damaging as
missing a finding. Enumerate, and then self-check that each is actually present as
written-out content (not named in a bullet and never produced):

- **Required sections / exhibits / elements.** If the task asks for a registration
  statement, a markup, a findings memo, an invoice analysis, or a term sheet, the
  controlling form / standard / contract / instruction names the components that
  document must contain (required sections, required tables with specified columns,
  required exhibits, specific negotiating terms, a per-line adjustment table, a
  prescribed signature/management disclosure block). List every required component the
  task or its governing document calls for, and confirm each is actually written out —
  a component you "intended to include," described in one line, or omitted because it
  seemed minor scores as absent.
- **Required computations and exact figures.** Where the record supplies inputs that
  the deliverable must compute (a dollar impact = hours × rate; an equity = value −
  mortgage; a bridge sum; a concentration percentage; a budget-overage percentage;
  a settlement total against a board-authorized range), carry **each** computation to
  its **specific numeric result** and write that number into the deliverable. "The
  time entries are excessive" where the rubric wants the precise dollar figure, with
  hours × rate shown, is a graded miss — the calculated figure is the finding. Do not
  stop at the qualitative conclusion when a number is determinable from the record.
- **Required revisions, not just observations.** For a markup/redline task, each
  finding that calls for a contract change must produce an **actual revision** in the
  redline (struck/inserted text), not a memo paragraph saying the clause "should be
  revised." A clause flagged for a carve-out, a dollar amount, a shortened duration,
  or a deleted provision must show that exact edit applied to that exact section.

**Final self-check before finishing** — run all four: (1) the §1 check that each item
is written-out prose in the `output/` file, not a description; (2) the §2 check that
every document was mined and no document was demoted/discarded; (3) for each required
component and required computation listed above, that it is actually present with its
exact value; (4) for a markup, that every flagged issue has a corresponding actual
edit. Nothing the rubric checks for should remain trapped as a description, generalized
away, left in a demoted document, or present only as "should be revised."
