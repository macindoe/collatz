# Findings: staircase-allp (2026-07-16)

This is not an off-brief findings log in the usual sense — the session stayed
on-brief throughout (Diophantine lemma, explicit construction, bounded
correction, verified instances; no per-period cycle search, no
divisibility-based exclusion attempt, no scope expansion). It records the
diagnostic detail behind cycles.md 12.8.6's Obstruction paragraph, which is
too granular for the wiki page itself but is worth keeping on file — mainly
so a future attempt at the primary theorem does not re-discover the same
dead ends from scratch.

## 1. The obstruction is combinatorial, not Diophantine

The initial working hypothesis (matching the brief's own pre-check note) was
that periods 15–18 were unresolved because of a *search-budget artifact* on
the Diophantine side — not enough candidate `n` tried at the right scale.
This was tested directly and ruled out: a scan of essentially *every*
integer `n` in `[0.15, 12] * 1.585^p` at `p = 15` (about 12,000 values, every
one with `q > 0` since `K = ceil(nL)` always gives that) was tried against
the base construction (12.8.6.2) with no passer found. The Diophantine
choice of `n` was never the binding constraint at any period tested; every
obstruction encountered was in the combinatorial half (getting the profile
`(m_t, s_t)` to actually satisfy `q <= R_r` for every rotation).

## 2. The base construction's shortfall is small, not catastrophic

A second false lead: an early diagnostic comparing `R_r - q` in absolute
terms reported shortfalls of "1500+ bits" at `p = 15`, which looked like a
fundamental mismatch of scale. This was a diagnostic bug, not a real effect
— comparing `bit_length(q - R_r)` conflates "R_r is a large fraction of q"
with "R_r is negligible next to q." Comparing `bit_length(R_r)` against
`bit_length(q)` directly shows the true picture: at `p = 15`, `n = 971`, the
base construction (12.8.6.2, no correction) already passes 11 of 15
rotations comfortably (margins of 2–10 bits) and fails the other 4 by only
1–3 bits. This matches the brief's own pre-check description exactly
("fails ... by only 1–2 bits on one to three rotations") and is the
foundation for the bounded correction algorithm (12.8.6.3): the shortfall is
small enough that a handful of unit-depth moves closes it, when it closes at
all.

## 3. Why p = 22 resists

Supplementary exploratory runs (not the committed script, but the same
algorithm with a much larger budget: up to 60 correction moves, no wall-clock
cap, a wider Diophantine candidate set) still do not close `p = 22`. This is
the strongest evidence in hand that `p = 22` is not simply under-resourced:

- `p = 18, 20`: resolved by the committed script's budget (`<= 40` moves,
  `<= 75` s), needing `8` and `12` moves respectively.
- `p = 22`: **not resolved** even with `60` moves and no time limit, across
  several `n` candidates and both crash depths tried.
- `p = 24, 25`: **not resolved** by the committed script's default budget,
  but **are resolved** by the larger supplementary budget (`8` moves each —
  within the committed *move* cap; it is the `75` s per-period wall clock
  that cuts them off, at their scale of `n`) — i.e. these two are exactly
  the budget artifact `p = 22` is not. (`p = 23` resolves under the
  committed budget itself, `8` moves; it appears in the verified record.)

No structural reason for `p = 22` specifically was found. Candidate
explanations not pursued further (out of scope for this session, and each
would need its own construction variant to test): the crash block's
placement is fixed at the end of the block sequence — trying other
placements was not attempted; the profile always closes with exactly one
crash block of depth 1 or 2 — a second small crash block, or non-unit exit
valuations on the last few climb blocks, were not attempted as a general
recipe (only as part of the bounded correction's per-instance unit moves).
Any of these could plausibly be the "clean explicit profile with provable
slack" the brief anticipated as the likely location of difficulty — none was
built out to a general, provable form in this session.

## 4. The Diophantine lemma's coverage gap (12.8.6.1)

The lemma as stated gives, for a correctly-signed continued-fraction run
`(q_{k-1}, q_k, a_{k+1})`, an upper bound on `gamma` that holds uniformly
across the whole run, and semiconvergents covering `n` from `q_{k-1}+q_k` up
to `q_{k+1}` in steps of `q_k`. What was *not* established is a general,
unconditional bound on the multiplicative gap between the end of one
correctly-signed run and the start of the next (this depends on the next
partial quotient `a_{k+2}`, which is not boundedly small in general, even
though it happens to stay small enough for `log_2 3` across the whole range
actually needed here). Coverage was instead verified computationally: every
period from 2 to 25 had at least one candidate `n` available from the
continued-fraction chain within the search window. This is not the same as
a proof that no period is ever skipped; it is the honest, checked
substitute the session's remaining time allowed. A cleaner treatment
(e.g. citing the three-distance theorem's windowed form directly, if a
correctly-signed one exists in the literature at the needed generality)
would close this gap without new computation.

## 5. What a future attempt at the primary theorem should try first

In order of how promising the (untested) leads look, given what failed:

1. **Second crash block.** Splitting the single huge-exit crash block into
   two smaller ones gives one more free parameter (a split point) without
   changing the overall shape's spirit; it may be enough to remove the
   `p = 22`-style resistance without ad hoc unit-shifting.
2. **Non-unit climb exits near the crash.** Allowing `s_t in {1, 2}` (not
   fixed at `1`) for the last few climb blocks before the crash gives slack
   exactly where the shortfall concentrates (rotations adjacent to the
   crash), at the cost of a slightly larger `gamma` budget to track.
3. **A closed-form bound on the correction's move count.** If the bounded
   correction of 12.8.6.3 can be shown analytically to need `O(1)` or
   `O(log p)` moves (rather than the empirically bounded-but-unproven count
   observed here: `0` at small `p`, up to a few dozen by `p ~ 20`), that
   alone would upgrade the floor-grade result to a genuine proof at the
   achieved construction shape (fallback A or B territory, depending on the
   exact bound), without needing a structurally different profile at all.

None of these were built out in this session; they are recorded as the
concrete next steps rather than left implicit.

## Update (2026-07-17): item 3 ("Why p = 22 resists") superseded

Item 3 above is **superseded**, not deleted: `p = 22`'s resistance was a
candidate-generation gap, not a structural property of the construction
recipe. A second exchange with Eric Merle (correspondence 2026-07-16/17)
named two candidates outside this session's own Diophantine chain
(`n = 25217`, `n = 31202` — simple arithmetic on the continued fraction's
best convergent at this scale, `15601`) at which the unmodified recipe of
`12.8.6.2`–`12.8.6.3` resolves `p = 22` in `13` and `8` correction moves
respectively — well inside the budgets this session's own supplementary
exploration (`60` moves, no wall-clock cap) already used without finding
a passer, because none of the candidates *tried* there were the ones that
work. The "no structural reason for `p = 22` specifically was found"
conclusion of item 3 stands as a *negative* result about the candidates
actually tried; it does not extend to "no candidate resolves `p = 22`",
which is now known to be false.

Full diagnosis, independent re-verification, and the resolved obstruction
paragraph: `briefs/merle-pincer-check-findings.md`, and `cycles.md`
12.8.6 (Obstruction (`p = 22`) — resolved (2026-07-17)). Standalone
verifier: `experiments/p22_passer.py`.

**Item 1 is also superseded, more than item 3 alone.** Item 1's title
claim — "the Diophantine choice of `n` was never the binding constraint
**at any period tested**" — was established there by the `p = 15`
exhaustive scan and then stated as a general conclusion across the
periods this session tried. `briefs/merle-pincer-check-findings.md` item
5 found the opposite at `p = 22`: candidate availability was *exactly*
the binding constraint there. Item 1's `p = 15` content is untouched and
still correct as a statement about `p = 15`; its generalization to "any
period tested" is refuted at `p = 22`, and `cycles.md` 12.8.6.1's status
paragraph now scopes the claim to `p = 15` explicitly.

Item 4 above (the Diophantine lemma's coverage gap) is **not**
superseded — it is exactly the gap that bit at `p = 22`, and it remains
open (now the sole remaining gap of the floor-grade result, per
`cycles.md` 12.8.6.1's status paragraph). Items 2 and 5 above are
unaffected by this update.
