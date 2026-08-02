# Brief: make Lemma 13.2.4(a) true (v3 round 4, final pass)

**Branch.** `v3r4-review-round4`, at `53975e2`. Work in `c:\Users\Ace\Documents\Collatz` on that branch. **Do not create a worktree.**

**One statement, and it is currently false as printed.** Nothing else. The round is otherwise closed.

## What is wrong

`aeh.md` Lemma `13.2.4`(a) bounds `TV(Law(ℓ_0, …, ℓ_(n−1)), B^(⊗n)) ≤ 2^(J+2)/N + P_B(S_n ≥ J)`.

Round 4 changed that tail term from `P_B(S_(n+1) ≥ J)` to `P_B(S_n ≥ J)`, on the external reviewer's advice that `S_n` was "the natural sharp form". **The reviewer assumed a letter indexing the record does not use, and so did the brief that ordered the change.** Under the indexing `13.2.4` actually defines — letter `i = stratum(y_(i+1)) = (m_(+,i), s_(i+1))`, with `y_i = G^i(x)` — the word `(ℓ_0, …, ℓ_(n−1))` is shifted one step from the word `14.15.1.5` is about, so its total exponent reaches one letter further. `S_(n+1)` accounted for that; `S_n` does not.

`briefs/v3r4-indexing-findings.md` establishes this and prices both repairs. Its counterexample, computed as exact total variation over every odd start in the case (a) singles out (`N = 2^b`, `J = b`, where the first term vanishes):

```text
b = 16:  true TV = 2279/2^20   printed bound = 1/2^11    factor 4.45
b = 20:  true TV =  685/2^21   printed bound = 5/2^17    factor 8.56
```

The factor grows with `b`. On the other reading of the letter word the same quantities lie inside the bound, as the cylinder theorem requires.

## The task

**1. Repair (a).** The narrow repair is to restore the tail term to `P_B(S_(n+1) ≥ J)`. The previous delegate reports nothing in (b)–(g), Corollary `13.2.4.1` or `13.6.4` needs a word as a result. The alternative — moving the letter definition to the `stratum(y_i)` reading — makes (a) true without touching (a) but breaks the corollary's identification, and is **not** authorized here.

Verify the repair before you rely on it, rather than trusting either the previous delegate or this brief: **two corrections to this one line have now both been wrong.** Confirm from the definitions which word (a) is about, then confirm the repaired bound actually holds.

**2. Prove it numerically.** Write fresh code — importing nothing from `experiments/` — and compute the same exact total variation the previous pass did, at minimum at `b = 16` and `b = 20` where the printed bound currently fails, plus at least one larger scale. Show the repaired bound holds at each, with the numbers. If it does **not** hold, stop and report: that would mean neither repair is right and the lemma needs more than an index.

Record the result in `13.2.4`'s Verified line — a single current line, overwriting rather than appending, in the form the page's other Verified lines use. Land the script in `experiments/` with a header naming the page and result it supports, or extend the existing `aeh_budget_clause.py` if that is the natural home; say which you chose.

**3. Resolve the cross-page tension.** `open-problems.md` 11.12 currently records that (a)'s printed bound fails, while `13.2.4` still prints it. After the repair that half is stale and must go. **The indexing-standardization question itself stays open** — three readings, one symbol collision — so keep 11.12 as that question, minus the resolved defect, still pointing at the evidence.

**4. Check `13.2.4`(c).** The previous pass reports its altitude line is short by the same letter, while its conclusion survives because `13.2.3`'s bound covers it with slack. Confirm that, and if the line is wrong as printed, fix it the same way. If fixing it moves anything beyond (c), stop and report.

## The pin and the build

The paper names `aeh.md` `13.2.4`. So: commit the record fix, re-point Appendix A's pin to that commit in its own commit, rebuild with three `pdflatex -halt-on-error` passes, and verify the pin's claim with `git show` — never the working tree — positively and negatively. **No prose change to the paper beyond the pin token.** Report passes, box warnings, unresolved references and page count.

## Constraints

- **Branch `v3r4-review-round4` only.** `git add` and `git commit` permitted. **No push, no merge, no rebase, no branch switching, no worktree.**
- Write files with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes `≤`, `—`, `ε`, `θ`, `τ`, `†`, `β`.
- Do not renumber any anchor. Do not prune. Do not claim the deferred prefix result. Change nothing in `13.3.2`.
- Do not attempt the indexing standardization — it stays an open item.
- No change logs or dated journals in tracked pages.
- **Fix only what is above.** Report anything else.

## Deliverable

The edits committed, plus `briefs/v3r4-lemma-index-findings.md`: which word (a) is about and how you established it, the repair and your numerical proof of it with the numbers, the `13.2.4`(c) verdict, 11.12 as it now reads, the pin verification, the build report, and anything found and not fixed.

Your final message: whether the repaired bound holds and at what numbers, what you changed, the (c) verdict, the pin and build, and anything you stopped on.
