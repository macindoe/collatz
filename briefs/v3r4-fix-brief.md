# Brief: the round-4 fix pass (v3 round 4, closing)

**Branch.** `v3r4-review-round4`, at `3c30b61`. Work directly in `c:\Users\Ace\Documents\Collatz` on that branch. **Do not create a worktree.**

Work order: `briefs/v3r4-verify-findings.md`, defects D1–D10. The verify pass recommends **do not merge as-is**, and the author has authorized this pass to close it.

## The blocker, and how to approach it

The retracted claim survives in the paper. Round 4 removed it from `aeh.md` and from §5, and the paper now contains **both** the claim and its retraction — `tex` L397–400 says the conversion is "neither a theorem nor a consequence of Hypothesis~\ref{hyp:aeh}", while L59 (*Related work*, page 4) says the divisor "is itself part of what Hypothesis~\ref{hyp:aeh} asserts" and L42 (the version note, page 2) calls the block reading "a consequence of Hypothesis~\ref{hyp:aeh}". L432–433 is a third instance.

**Do not patch the three named lines. Sweep the document.** Site lists are exactly what failed here: the design wave and the apply wave both worked from the lines the external reviewer happened to cite, and two of the three instances were named by neither. Read `paper/collatz-reduced-v3.tex` for the *claim*, in any wording — that AEH supplies the mean exponent, that it converts a horizon into blocks per bit, that the block-unit endpoint is a consequence of or part of the hypothesis, that zero cemetery mass gives the budget. Report every instance you find, including any beyond the three.

The correct statement, already in the document at L397–400 and in `aeh.md` `13.2.3`/`13.2.4`(g): the conversion is a **theorem where the cylinder count runs** (`θ < 1/4`), and past it is neither a theorem nor a consequence of the hypothesis.

## The rest

- **D2.** `aeh.md` `13.3.2`: "the endpoint `1/β` in block units is this page's own hypothesis, not his theorem" is a surviving instance and contradicts L67 and L94 on its own page. The apply wave froze `13.3.2` because the *design's* drop-in for it was the deferred prefix clause; this repair is subtractive and needs nothing deferred, so the freeze does not cover it. Fix the sentence and **change nothing else in `13.3.2`** — the deferral stands.
- **D3.** `13.2.4`(g)'s parenthetical says the offset is absorbed by `δ_N`. It is not: the exceptional mass is `Θ(1/log N)` against `δ_N = e^(−Θ(b))`. Verify supplies the one-line repair (bound by `s_0` alone rather than `max_n s_n`). Corollary `13.2.4.1`'s "density `e^(−Θ(b))`" inherits the same error — fix both, consistently. **This is a proof step; get it right rather than quickly, and if the repair does not close, say so rather than papering it.**
- **D5.** "positive precisely for `τ > 4θ`" is false of the expression — it is positive on both sides of `4θ` and undefined for `τ ≤ 2θ`. What is true is that it is the Cramér rate on `τ > 4θ` and that the tail vanishes only there. Restate.
- **D6.** "the two clauses of admissibility are exactly the two terms of (a)" over-claims, since admissible `τ ∈ [1, 4.8188…)` exists. `aeh.md` self-corrects in the following clause; the paper does not. Fix the paper's version.
- **D7.** `paper` L321 cites Inselmann Thm 1.10 — a Syracuse-time result — for a protection statement made in `T_1`-time, inside a sentence that says "the same unit, nothing converted". **The verify delegate did not read Inselmann**; its theorem numbers come from `briefs/v3r3-inselmann-horizon-findings.md`, which did read the source. Check the citation against that findings file. If which theorem applies is not unambiguous there, restate the sentence so it does not depend on the theorem number, rather than guessing.
- **D8–D10.** `publication.md` L41's implicature; `aeh.md` L8, which is not wrong but does not carry the correction; `open-problems.md` 11.11, which restates the deferred argument where it should point at it. Small; apply judgement and record what you did.

## The verification line for `13.2.4`(g)

`13.2.4`'s Verified line covers none of (g)'s new content, which is an `AGENTS.md` violation for material stated as proved. Close it:

- **Write and run your own check with fresh code.** Verify has numbers in its findings; **do not quote them.** The whole point of the rule is an independent implementation. Cover at minimum: the exact tail identity at new parameters, the rate's value at the printed `θ`s and its reduction at `τ = 1`, the budget bound on real odd starts with the exponent mean, and a negative control at `τ < 4θ`.
- Land the script in `experiments/` with a header naming the page and result it supports, and add the verification line to `13.2.4` in the form the page's other Verified lines use — a single current line, overwriting rather than appending.

## Order, and the pin

Record fixes first, then the paper, then the pin as a separate final commit. The pin currently names `e634513`; because both record and paper move, it must be re-pointed to the new commit containing them. Verify its claim before committing, positively and negatively, including the `cycles.md` sections the last apply check omitted.

Rebuild: three `pdflatex -halt-on-error` passes. Report passes, box warnings, unresolved references, page count, and confirm from the built PDF's text that the surviving claim is gone from the artifact.

## Constraints

- **Branch `v3r4-review-round4` only.** You may `git add` and `git commit`. **No push, no merge, no rebase, no branch switching, no worktree.**
- Write files with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes this repo's `≤`, `—`, `ε`, `θ`, `τ`, `†`, `β`.
- **Do not prune.** Deferred to a separate round by the author.
- **Do not claim the deferred prefix result**, and change nothing else in `13.3.2`.
- No change logs or dated journals in tracked pages. Do not renumber any anchor.
- No numbered theorem's claim strengthened, weakened, or renumbered.
- Every number verified against the file or recomputed, not recalled.
- **Do not fix anything not on this list** — except further instances of the blocking claim, which you are explicitly told to hunt. Report anything else.

## Deliverable

The edits committed, plus `briefs/v3r4-fix-findings.md`: every instance of the retracted claim you found and how each was resolved (including any beyond the three named), the disposition of D2–D10, the `13.2.4`(g) repair with your reasoning, your verification script and its numbers, the build report, the pin and its verification, and anything you found and did not fix.

Your final message: the sweep result, what landed, the build, the pin, and anything you stopped on.
