# Brief: propagate the shifted word into the paper (v3 round 5)

**Branch.** Cut a branch `v3r5-shifted-word` from `main` at `6b9716a` and work on it, directly in `c:\Users\Ace\Documents\Collatz`. **Do not create a worktree.**

Small, sharp pass. Two repairs, one declined recommendation, then re-pin and rebuild. **Do not prune** — that is the next round, and it will run against the paper you leave.

## Verify before you edit

Round 4 corrected this exact line twice, and **both corrections were wrong** — each assumed a letter indexing the record does not use. Before changing anything, establish from the definitions themselves which word the paper's display is about: `paper` L253 (`ℓ_n = (m_{+,n}, s_{n+1})`), L254 (`S_n = Σ_{i<n}(m_i + s_i)`), and `aeh.md` `13.2.4`'s own preamble and part (a). If the analysis below is wrong, say so and stop.

## Repair 1 — the paper's finite bound

`paper/collatz-reduced-v3.tex` L348–362. The paragraph invokes the cylinder fact for "the first `n` blocks of a start" — the itinerary beginning at the sampled `x` — and then displays the bound for `Law(ℓ_0, …, ℓ_{n−1})`, whose first letter is `stratum(G(x))`, one `G`-step later. The cylinder count must also pay for the start's own letter, so the word is `n + 1` letters long.

`aeh.md` `13.2.4`(a) already carries the corrected form, proved by exact total variation over every odd start at four scales: the printed `S_n` bound is exceeded in 15 of 18 cells, the `S_(n+1)` bound holds in all 18.

So the display becomes `2^(J+2)/N + P_B(S_(n+1) ≥ J)`, with the identity `P_B(S_(n+1) ≥ J) = P(Bin(J−1, 1/2) < 2(n+1))`, and the trailing clause — currently "`S_n` is the waiting time for the `2n`-th head" — takes the same shift.

**Also fix the explanation.** The paragraph must say that the theorem is applied to the extended `(n+1)`-letter word beginning at `x`, rather than invoking it for one word and displaying it for another. That silent step is what let the error stand.

**Note for your own check:** in the paper's `S` — the budget sum `Σ(m_i + s_i)` — the extended word covering `ℓ_0 … ℓ_(n−1)` is letters `0 … n`, of exponent exactly `S_(n+1)`. The paper's existing notation is therefore already correct for the repaired display. Confirm that; it is why no new symbol is needed (see the declined item below).

## Repair 2 — `13.2.4`(g)'s proof source

`aeh.md` `13.2.4`(g) estimates the start's own exponent `m_0 + s_0` and attributes it to "(a) at `n = 1`". After round 4's indexing repair, (a) is about `stratum(G(x))`, so at `n = 1` it gives the law of `ℓ_0`, not of the start's own block. **The estimate is fine; its stated source no longer supplies it.**

Repair the attribution: apply the one-letter cylinder/residue law directly to the sampled `x` (`itinerary.md` `14.15.1.3`(i)/`14.15.1.5` at length one on `x`'s own word), from which the geometric tail and the exponentially small interval-boundary error follow.

**This is a citation swap, not a new estimate — but confirm the replacement source actually covers the start's own letter, and prove it rather than assert it.** A short numerical check suffices: the law of `stratum(x)` for `x` uniform on `[N, 2N)` against the geometric weights, at two or three scales, with the boundary error visible. Extend `experiments/aeh_word_shift.py` or `aeh_budget_clause.py` if either is the natural home — say which you chose — and update the owning Verified line as a single current line.

Check while you are there whether any other clause in `13.2.4` or elsewhere cites (a) for something about the start's own block. This defect is a second-order consequence of round 4's repair; there may be another instance.

## Declined — do not implement

The reviewer also recommends distinct notation for two exponent sums, saying the paper calls both `S_n`. **The author has declined this and you must not implement it.** The paper defines exactly one sum; its only use of `r_i` is at L273, naming a generic letter's components inside the Bernoulli weight `B[w]`. There is no second sum in the paper to collide with, and as noted above the single existing `S` makes the corrected display come out right. The distinction is one the *wiki* needs — `13.2.3` carries both counts because the base case and the budget clause use different ones — and importing it into the paper immediately before a pruning round would add a symbol the paper never needs.

Record this in your findings with the evidence, in a form that can be used to answer the reviewer.

## The pin and the build

The paper names `aeh.md` `13.2.4`. Commit the record repair first, then the paper, then re-point Appendix A's pin to the commit containing both, in its own commit. Verify the pin's claim with `git show` — never the working tree — positively and negatively. Rebuild with three `pdflatex -halt-on-error` passes; report passes, box warnings, unresolved references and page count, and confirm from the built PDF's text that the corrected display is in the artifact.

## Constraints

- **Branch `v3r5-shifted-word` only.** `git add` and `git commit` permitted. **No push, no merge, no rebase, no branch switching, no worktree.**
- Write files with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes `≤`, `—`, `ε`, `θ`, `τ`, `†`, `β`.
- **Do not prune.** Do not renumber any anchor. Do not attempt the indexing standardization (open at `open-problems.md` 11.12). Do not claim the deferred prefix result. Change nothing in `13.3.2`.
- No numbered theorem's claim strengthened, weakened, or renumbered.
- No change logs or dated journals in tracked pages.
- Every number verified against the file or recomputed, not recalled.
- **Fix only what is above.** Report anything else.

## Deliverable

The edits committed, plus `briefs/v3r5-shifted-word-findings.md`: which word the display is about and how you established it, the two repairs, your numerical check for repair 2 with its numbers, any further instance of the (a) mis-citation, the declined recommendation with its evidence, the pin verification, the build report, and anything found and not fixed.

Your final message: whether the index analysis held, what you changed, the check's numbers, the pin and build, and anything you stopped on.
