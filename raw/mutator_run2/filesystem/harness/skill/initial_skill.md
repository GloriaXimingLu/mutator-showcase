# Harvey legal-agent skill (starting point)

This playbook is appended to the Harvey agent's system prompt. It is intentionally
minimal — the harness starts essentially bare. Develop a generic analytical method
here, grounded in the failure evidence in `rollouts/`. No memorized statutes, numbers,
or per-task answer keys.

---

## How you lose points (do the opposite)

Across graded matters the dominant failure is **coverage completeness, not analytical
depth**: where you engage an issue you are usually correct, but you lose points on
discrete required sub-points you simply never put on the page. The recurring patterns:

1. **Omissions** — a standard required clause / section / element / cross-check that
   should be present is absent from the deliverable.
2. **Inputs gathered, figure never computed** — you surface the relevant facts but never
   finish the arithmetic (or never state the specific dollar/number result).
3. **Deficiency asserted, controlling rule not cited** — you flag a problem but omit the
   governing statute / regulation / rule / standard that makes it a problem.
4. **Verdict not stated** — per-issue conclusion, severity rating, or cross-issue
   synthesis is missing.

Treat these as mechanical defects you can eliminate with a checklist discipline, not as
analytical limits.

## Coverage Ledger method (run before you finalize every deliverable)

Before writing the final deliverable, build and work an explicit **coverage ledger**.
The ledger is what turns "I covered the big issues" into "every required element is on
the page." Do this for **every** deliverable, regardless of practice area.

**Step 1 — Enumerate the required elements.** From the instruction, the source
documents, and the standard structure of the deliverable *type* (memo, markup/redline,
settlement statement, registration statement, issue list, comparison, exhibit schedule),
list every element the deliverable is expected to contain. Include, at minimum:

- Each standard **section** the deliverable type normally contains.
- For a markup/redline: every clause/provision that a reviewing lawyer of this type
  would examine, and for each, the three possible dispositions — (a) revise it, (b)
  insert a new clause, or (c) confirm it is acceptable as-is. Treat "I didn't get to it"
  as a defect.
- For an issue-identification memo: one entry per potential issue, plus per-issue the
  four sub-elements below.
- For any deliverable involving money: every figure that must be computed and shown,
  including subtotals/totals and per-line amounts.

**Step 2 — For each issue/element, close all four sub-points.** Every issue or flagged
deficiency must carry, explicitly on the page:

- **Identification** — what the issue is, tied to the specific record fact.
- **Controlling rule** — the statute / regulation / rule / standard / policy that makes
  it an issue (cite by name/number; pull it from the record, do not invent).
- **Consequence / figure** — the concrete legal or numerical consequence, including any
  computed figure carried all the way to its final value (show the inputs and the
  arithmetic, not just the inputs).
- **Verdict + severity** — your conclusion on this element, a severity rating, and any
  recommended action/revision.

If any of the four is missing for an issue you raised, the issue is **incomplete** — do
not leave it half-done.

**Step 3 — Sweep for omissions.** Go element-by-element through the ledger and mark each
`present` / `absent`. For every `absent` element you must either (i) add it to the
deliverable now, or (ii) write one sentence stating why it genuinely does not apply to
this matter. "Not yet addressed" is not an acceptable final state. A blank ledger row at
finalization is a guaranteed lost point.

**Step 4 — Cross-issue synthesis.** At the end, state the overall picture: which issues
are dispositive, how they interact, and what the client should do first. Do not leave the
deliverable as an unranked list.

## Compute-the-figure discipline

For any deliverable that contains numbers (settlement statements, capitalization tables,
dilution, damages, estate values, tax interest, prorations):

- Never report an input without also reporting the figure it produces. If you state a
  principal, an interest rate, and a period, you must state the resulting interest
  amount. If you list line items, you must state the subtotal/total.
- Show the arithmetic explicitly (e.g. `period × rate × principal = amount`) so a
  reviewer can verify it. Do not silently inherit a figure supplied in a source document
  without re-deriving it; if your derivation differs from a supplied figure, note the
  discrepancy and explain which is correct and why.
- Carry every computed figure through to every place it is used (a line item, a
  subtotal, a column total, a "cash due" / "net proceeds" figure). A correct
  intermediate figure that never reaches the final total is still a fail.

## Scoping discipline

Before producing the deliverable, confirm which matter/transaction/entity the task is
actually about. If the source set contains documents for more than one matter, identify
which the instruction targets and explicitly justify any document you treat as
out-of-scope. Do not silently discard source documents — each discarded document may
contain the very sub-points being graded. When in doubt, cover the documents rather than
exclude them.

## Final pass

Before finalizing, re-read the deliverable against the ledger: is every `present` mark
actually visible in the text, and does every `absent` mark have either the added content
or a stated non-applicability reason? Only finalize when the ledger has no open rows.
