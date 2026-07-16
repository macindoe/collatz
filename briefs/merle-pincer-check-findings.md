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
