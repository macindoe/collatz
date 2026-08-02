# Brief: the letter indexing, narrowly (v3 round 4, closing pass)

**Branch.** `v3r4-review-round4`, at `2ec9702`. Work in `c:\Users\Ace\Documents\Collatz` on that branch. **Do not create a worktree.**

Two statements, plus one open item. **Nothing else.** The round is otherwise closed and the author has authorized only this.

## The two statements

`briefs/v3r4-fix-findings.md` reports both; read its detail before starting, then verify each against the current files rather than inheriting the finding.

**1. `aeh.md` `13.2.3` (L69): "The gap is exactly `s_n − s_0`".** This is material round 4 itself added, as part of the `O(1) → O_P(1)` repair. It is true if the letter's components are `(m_i, r_i)` with `r_i = s_{i+1}` — the `m` terms then cancel — and false if the letter is `(m_{+,i}, s_{i+1})`, where they do not and the gap is `(m_0 + s_0) − (m_n + s_n)`. The fix delegate reports the latter is what `13.2.1` and `13.2.4` actually use, and measured the two formulas agreeing on 87 of 300 starts, exactly where `m_0 = m_n`.

**2. `13.2.4`'s `ℓ_n = stratum(G^(n+1)(x))`** is off by one against (a)'s own proof, which invokes `14.15.1.5` on the letter word of `x` itself. The fix delegate calls it harmless to every conclusion and the source of item 1.

## The task

**Trace the indexing from the definitions**, not from any findings file: `13.2.1`, `13.2.4`, `13.6.3`(i), and the seam identification at reverse.md `14.14.6`. Establish which convention each statement is actually using.

Then make both statements true. You may fix the identity, fix the definition, or restate either so it does not depend on the convention — whichever is smallest and leaves the surrounding argument untouched. Say which you chose and why.

**Check nothing downstream moves.** `13.2.4`(g)'s repair was deliberately written to hold under all three indexings the record carries; confirm that is still so after your edit, and that `13.2.4`(a)–(f), Corollary `13.2.4.1` and `13.6.4` are unaffected. If any of them does move, stop and report — that would put this outside the authorized scope.

**Do not attempt the wider cleanup.** The record carries three different letter indexings and reconciling them is a round in its own right, touching `13.2`, `13.6.3` and everything citing them. Log it in `open-problems.md` as one checkable item: which indexing the record should standardize on, and what would have to change. Point at `briefs/v3r4-fix-findings.md` for the evidence.

## The pin, and the build

The paper names `aeh.md` §13.2.3, so the pin cannot keep naming a commit whose `13.2.3` is the pre-fix text.

1. Commit the record fix.
2. Re-point Appendix A's pin to that commit, in its own commit.
3. Rebuild — three `pdflatex -halt-on-error` passes — and verify the pin's claim before committing: every `aeh.md` section and script the paper names, present and correct at that commit, checked with `git show`, positively and negatively.

Report passes, box warnings, unresolved references and page count. The paper must otherwise be untouched: **no prose change beyond the pin token.**

## Constraints

- **Branch `v3r4-review-round4` only.** `git add` and `git commit` are permitted. **No push, no merge, no rebase, no branch switching, no worktree.**
- Write files with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes `≤`, `—`, `ε`, `θ`, `τ`, `†`, `β`.
- Do not renumber any anchor. Do not prune. Do not claim the deferred prefix result. Change nothing in `13.3.2`.
- No change logs or dated journals in tracked pages.
- Every number verified against the file or recomputed, not recalled.
- **Fix only these two statements.** Report anything else you find.

## Deliverable

The edits committed, plus `briefs/v3r4-indexing-findings.md`: the indexing as you traced it, which repair you chose and why, your confirmation that nothing downstream moved, the open item as landed, the pin verification and the build report, and anything you found and did not fix.

Your final message: the indexing verdict, what you changed, confirmation nothing downstream moved, the pin and build, and anything you stopped on.
