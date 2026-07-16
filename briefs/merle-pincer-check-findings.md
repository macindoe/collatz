# Findings: merle-pincer-check (2026-07-17)

Answers `briefs/merle-pincer-check-brief.md` items 1-5: Eric Merle's p = 22
"Diophantine pincer" hypothesis, checked against what our own stack
(`experiments/staircase_allp.py`) actually tried, plus independent
re-verification of his calibration rows, his p = 7 local-global distance
measurement (ledger seed #3), and the continued-fraction hole claim.

Code: `experiments/merle_pincer_check.py`. Section 1 of that script is the
brief's one labeled exception — a verbatim-logic instrumented copy of
`staircase_allp.py`'s candidate enumeration / construction / correction,
never imported, run only to answer "what did our stack try" (item 1).
Every other section (items 2-4) is independently written: its own
rotation-sum implementation (`R_all_fresh`, O(p) per rotation via
suffix/prefix sums, structured differently from the committed script's
`Msuf`/`Spre` accumulator), its own implementation of Construction
12.8.6.2, and its own continued-fraction routine. All pass/fail and
feasibility decisions use exact Python integers; margins are reported two
ways — an exact integer bit-length difference (the corrected diagnostic
of `staircase-allp-findings.md` item 2) and a continuous `log2(R_r) -
log2(q)` (display only, safe for arbitrarily large ints in CPython,
needed to compare against Merle's fractional-bit figures). Range checked:
p in {7, 21, 22, 23}; dates: 2026-07-17.

## Item 1: the p = 22 candidate/margin table (committed script's own logic)

`experiments/staircase_allp.py`'s `__main__` calls
`run(pmin=2, pmax=25, n_tries=6, max_moves=40, wall_clock_budget=75.0)`,
and `find_passer` tries `crash_depths=(1, 2)`. At `p = 22` (scale target
`L^22 = 25143.042`), the full committed search window
(`0.3*target <= n <= 3.5*target`) contains 17 candidates; the top 6 by
log-closeness to target — what the script actually iterates — are:

```text
n        n/L^22   cd  feasible  fail_pre  worst_bits  worst_log2
31867    1.267    1   yes       20        -19         -19.47
31867    1.267    2   yes       20        -18         -18.48
16266    0.647    1   yes       18        -16         -16.71
16266    0.647    2   yes       18        -17         -17.30
15601    0.620    1   NO (rounded climb profile hits a depth-0 block)
15601    0.620    2   NO
14936    0.594    1   NO
14936    0.594    2   NO
14271    0.568    1   NO
14271    0.568    2   NO
13606    0.541    1   NO
13606    0.541    2   NO
```

`fail_pre` = pre-correction count of rotations with `R_r < q` (out of
22); `worst_bits`/`worst_log2` are the worst-rotation margin by the two
diagnostics above. Four of the six candidates the script actually tries
are not merely poorly margined — the base construction (12.8.6.2) cannot
even build a valid profile for them: rounding the geometric climb by
partial sums (`ROUND_HALF_EVEN`) produces a block of depth 0 near the
start of the climb (verified directly: at `n = 15601`, the rounded
profile's second climb block is `0`). This is a distinct failure mode
from a margin shortfall, and it is not visible in a "worst margin in
bits" table alone. Under the shared 75s wall-clock budget (one deadline
for the whole `p = 22` call, matching `find_passer`'s actual semantics,
not 75s per candidate), the script spends the entire budget failing to
correct `n = 31867, cd = 1` and never gets to attempt correction on the
other three feasible/attempted combinations at all ("deadline
exhausted"). None of the six candidates resolves.

**Supplementary wider reconstruction** (approximating
`staircase-allp-findings.md` item 3's "60 moves, no wall-clock cap, a
wider Diophantine candidate set" — the exact candidate list was not
recorded there, so this is a labeled best-effort reconstruction: top 20
candidates by log-closeness within an expanded `[0.15, 5]*target`
window, both crash depths, pre-correction columns only, per the brief's
"report the same columns" — the correction/resolved question for these
is answered directly, per exact n, in item 2 below instead of re-run
here on 20 x 2 candidates at this integer scale):

```text
n        n/L^22   cd  feasible  fail_pre  worst_bits  worst_log2
47468    1.888    1   yes       6         -5          -4.78
47468    1.888    2   yes       6         -4          -3.95
79335    3.155    1   yes       5         -4          -4.93
79335    3.155    2   yes       5         -4          -4.11
111202   4.423    1   yes       21        -23         -23.50
111202   4.423    2   yes       21        -22         -22.69
```

(all other widened-window candidates duplicate the top-6 table's
infeasible entries below `n = 16266`, or are additional infeasible
entries further below scale). Note `n = 47468` — the very next member of
the *sign-filtered* good-n grid after `15601` (item 4) — is markedly
better than anything in the actual top-6, foreshadowing item 4's finding
that the committed script's candidate chain and the lemma's own strict
grid disagree about what "the next good n" is.

## Item 2: the pincer hypothesis, tested against that table

**(a) Every in-scale candidate's pre-correction worst margin falls
materially beyond the -3/-4 bit recovery threshold.** Confirmed, and by
a wide margin, for both of the top-6's feasible candidates (`-16` to
`-19` bits) — nowhere near the `-3/-4` boundary. Going further than the
brief's literal ask: plugging Merle's own two specific n-values directly
into our fresh implementation of Construction 12.8.6.2 (not from our
Diophantine chain — see below) reproduces his numbers **exactly**:

```text
n = 25217 (his "in-scale"), cd=1: fail=9,  worst_bits=-8,  worst_log2=-7.86   (his: 9, -7.86)
n = 31202 (his "off-scale"), cd=1: fail=6,  worst_bits=-5,  worst_log2=-4.80  (his: 6, -4.80)
```

Both match to the stated two decimal places. His measurements are
independently confirmed, exactly, at the n he names.

**(b) No candidate combines a near-threshold margin with in-scale
`δ`.** None found. The two actually-tried feasible candidates (`16266`,
`31867`) are far beyond threshold, not near it; nothing in between them
was tried by the script because nothing exists there in its own
candidate chain (item 1). No refutation of the pincer from this
direction.

**(c) Does the committed window contain candidates inside `(15601,
31202)` other than near-hole edges?** Exactly one: `n = 16266`, which
sits `665` above the left edge (`15601`) — i.e., at the edge, not the
interior. No other candidate lies in that interval.

**A finding beyond what (a)-(c) ask: Merle's specific n-values are not
members of either of our own Diophantine candidate generators.** Neither
`25217` nor `31202` appears in the committed script's raw
(sign-agnostic) chain nor in the lemma-12.8.6.1 sign-filtered "good n"
grid (item 4) — both fall strictly inside the gap those generators leave
open. Checking their local approximation quality directly (`K - n·L`,
exact-precision decimal, display-only): `n=31202` gives `K-nL ≈
5.2e-05` — a genuinely excellent approximant, comparable to `n=15601`'s
`2.6e-05` — while our chain's actual candidate at nearly the same scale,
`n=31867` (only 2% larger), gives `K-nL ≈ 0.99999`, i.e. it approximates
from the *wrong side* entirely (confirmed: `31867` is a negatively-signed
convergent denominator in the CF table below). `n=25217`'s quality
(`K-nL ≈ 6.2e-04`) is decent though not as sharp; it factors as
`15601 + 9616`, and `9616` is itself a member of the *earlier*
(`306`-based) semiconvergent run — i.e. Merle's in-scale point looks like
"the best convergent plus an earlier-scale semiconvergent," and his
off-scale point looks like "twice the best convergent" (`31202 =
2*15601`, and the error term is observed to scale almost exactly by the
same factor: `5.2e-05 ≈ 2 * 2.6e-05`). Neither combination is produced
by lemma 12.8.6.1's own prescribed step (`n_j = q_{k-1} + j*q_k`, stepping
by the *next* convergent, not by re-using or doubling the current one).
This is not a contradiction of anything proved — `staircase-allp-
findings.md` item 4 already recorded, as an open gap, that 12.8.6.1 has
no established bound on the multiplicative gap between correctly-signed
runs, and this is exactly where that gap bites: at `p = 22`'s scale,
simple arithmetic on the best available convergent finds better
candidates than the lemma's own generator supplies.

**Additional check beyond the brief's literal ask, directly relevant to
"the -3/-4 bit recovery threshold":** running the correction algorithm
(12.8.6.3, `max_moves=40`, `40s` deadline, using item 1's instrumented
copy of the algorithm) on Merle's own two n-values, and on our script's
own best actually-tried candidate:

```text
n=31202 (his off-scale), cd=1: NOT resolved (40 moves used)
n=25217 (his in-scale),  cd=1: NOT resolved (40 moves used)
n=16266 (our own top-6's best feasible entry), cd=1: NOT resolved (40 moves used)
```

None resolves — including his off-scale point, whose pre-correction
margin (`-4.80`) sits right at his stated recovery boundary. This
directly supports his empirical `-3/-4` bit threshold claim rather than
finding a counterexample to it.

**Calibration cross-check, fresh code, base construction only (12.8.6.2,
no correction):**

```text
p=21, n=15601 (exact, not glyph-mangled): cd=1: fail=3/21, worst_bits=-3, worst_log2=-2.27
                                                  (Merle: 3, -2.27 -- EXACT MATCH)
                                           cd=2: fail=3/21, worst_bits=-3, worst_log2=-2.85

p=23, n=39468 (brief's flagged approximate/mangled reconstruction):
                                           cd=1: fail=19/23, worst_bits=-19, worst_log2=-19.27
                                                  (Merle: 4, -3.77 -- SHARP DISAGREEMENT)
                                           cd=2: fail=19/23, worst_bits=-19, worst_log2=-18.66
```

The p=21 row matches exactly. The p=23 row does not match at all — not a
rounding-level discrepancy but a completely different regime (19/23
failing vs. his 4/23). Before treating this as a clean disagreement, one
targeted check was made (not a search campaign, per scope): our own
Diophantine chain has *no* candidate anywhere near `39468` at all (its
two neighbors, `31867` and `47468`, are each about `8000` away, i.e.
`39468` sits in the middle of a chain gap — chain gap detail in item 4).
A plausible single-digit transcription of the flagged number,
`n=39488` (an `8`/`6` glyph swap, consistent with the brief's mangled-
numeral warning), was also tried: `fail=10/23, worst_log2=-9.17` for
`cd=1` — closer than `39468` but still nowhere near his `(4, -3.77)`.
**Recorded as an open, precise disagreement**, not resolved further: the
p=23 row does not reproduce under our fresh code at the literal or the
one plausible near-miss value tried. Given the brief's own flag that
this number was reconstructed from scale arithmetic rather than
transmitted cleanly, the most likely explanation is that the true
n differs from both values tried here by more than a one-digit
transcription error — but that is a guess, not a finding.

**Verdict.** The pincer hypothesis is **supported in its core mechanism,
with a precise correction to its stated interval.** Confirmed
independently: (i) a genuine, large Diophantine hole exists at p=22's
scale in our own candidate machinery — but its measured location is
`(16266, 31867)` under the committed script's own (sign-agnostic) chain,
or `(15601, 47468)` under lemma 12.8.6.1's own strict sign-filtered
definition — not `(15601, 31202)` as stated (see item 4 for the exact
numbers and which of ours is the closer match); (ii) every candidate our
own stack's actual top-6 selection supplies at p=22 is either
infeasible outright or has a pre-correction margin far beyond the -3/-4
bit threshold, matching the pincer's predicted severity; (iii) Merle's
own specific measurements are exactly reproduced by our independent
implementation, at his stated n-values, even though those n are not
generated by either of our own candidate machineries — revealing that
his in-scale/off-scale points come from simple arithmetic on the best
convergent (doubling; adding an earlier semiconvergent) that lies outside
lemma 12.8.6.1's prescribed construction, a genuine coverage gap in our
own machinery rather than an error in his numbers. The p=23 calibration
row is a real, unresolved disagreement, most plausibly a residual
transcription issue in the brief's own reconstruction of a mangled
numeral, not chased further here per scope.
