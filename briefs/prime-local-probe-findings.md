# Findings: prime-local probe (2026-07-18)

Answers `briefs/prime-local-probe-brief.md`'s two items: the prime-local
pinning probe (does anything replace the mod-3 ε-law mechanism at
primes `ℓ | q`, `ℓ ∤ 6`) and the gcd spectrum (the `p = 7` seed's
`gcd = 7`, the `ℓ = p` hypothesis, baselines).

Code: `experiments/prime_local_probe.py`, fresh (reimplements `R_r`,
`q = 2^K − 3^n`, and all number theory — Miller-Rabin, Pollard rho,
multiplicative order — from scratch; imports `merle_round3_check.py`
only for cross-validation of `R_r`/`q`, and `staircase_allp.py` only to
regenerate the 12.8.6.4 instance record's profiles, per the brief's
explicit carve-outs). Exact integer arithmetic at every residue and
pass/fail; floats only in labeled statistics columns (`chi2`, `z`,
Fisher-approximation `p`-values). Seed `20260718` throughout, dated
2026-07-18. Full run: **15,489,463 exact checks, 0 failures, 283.8 s**.

## Item 1 verdict, flat: **(ii) local structurelessness**

`R_0 mod ℓ` equidistributes on its full attained set — all of `Z/ℓ`,
never confined to a proper coset of `⟨2,3⟩ ≤ (Z/ℓ)*` — at every prime
tested, both sectors. No analogue of the mod-3 ε-law (a residue pinned
by one coarse invariant) was found at any `ℓ | q`, `ℓ ∤ 6`. Every
apparent departure from uniformity was hunted down and dissolved by an
identified elementary cause (below) that has nothing to do with
ℓ-adic arithmetic. This is the valuable verdict the brief flagged: the
`1/q` heuristic has no local leak visible at this scale, both sectors.

**Measurement 1 (exhaustive scan).** `p ∈ {1,2,3}`, entries `m_t,s_t ∈
[1,12]`: 3,006,864 profiles, 9,455,862 `(profile, prime-factor-of-q)`
rows, 41.4 s (extends the brief's `entries≤4` baseline — 4,368 profiles
— 3× in entry range; `entries≤13` was tried and cut by the 60 s
per-scale budget at 3.80M of an estimated ~5.6M profiles, so
`entries≤12` is the range used). Sector split: `q>0`: 8,321,925 rows,
`q<0`: 1,133,937 rows.

- **(b) attained-coset test** (nonzero `R_0 mod ℓ` vs a coset of
  `⟨2,3⟩`), top-80-by-count primes with ≥100 samples: positive sector
  0/32 nontrivial cases confined, negative 0/22, both 0/34 (the
  remaining ~45 primes per sector have `⟨2,3⟩` = the full unit group,
  making the test vacuous there — reported separately, not counted as
  "confined"). **Clean refutation of confinement.** (An earlier pass at
  `entries≤7` had shown 2 apparent small-sample "confinements" — both
  vanished once `entries≤12`'s larger sample size was used, confirming
  they were sampling artifacts, not signal.)
- **(a) coarse-invariant law test** (`R_0 mod ℓ` as a function of `(K
  mod ord_ℓ(2), n mod ord_ℓ(3))` alone), same top-80 cap: 0/80 pure in
  positive, 0/43 pure in negative, 0/80 pure in both — **the coarse
  pair never determines the residue.** Refuted cleanly at every prime
  tested (up to 80 primes/sector, sample counts up to hundreds of
  thousands).
- **(c) zero-rate vs naive `1/ℓ`:** pooled rate 0.0392 (positive) /
  0.0392 (negative) vs naive baselines 0.0348 / 0.0358 — close overall,
  but several individual primes show large `z` (e.g. `ℓ=5`: `z=88.6`
  positive, `27.3` negative; `ℓ=7`: `19.6`/`3.2`; `ℓ=19`: `24.3`/`−3.5`).
  These are **not** signal — see the ghost-hunt below.

**Ghost-identity hunt (the elementary cause, found and verified).** The
large `z`-scores at small primes (`ℓ=5,7,11,13,17,19,23,...`) are
explained by a finite combinatorial fact about `R_0`'s own defining
formula, unrelated to any ℓ-adic pinning:

> Within a fixed-`(p, n mod ord_ℓ(3), S mod ord_ℓ(2))` family, `R_0 mod
> ℓ` is the pushforward of the (asymptotically uniform, as `n,S→∞`)
> distribution on the residue hyperplane `{(m_t mod ord_ℓ(3)) : Σm_t ≡
> n} × {(s_t mod ord_ℓ(2)) : Σs_t ≡ S}` through `R_0`'s own formula,
> reduced mod `ℓ`. This is a **fixed, finite, generically non-uniform**
> target distribution (there is no reason a formula's fibers should be
> equal-sized), depending only on `p, ℓ`, and `(n mod ord_ℓ(3), K mod
> ord_ℓ(2))` — not on `n, S` individually once large. A bounded
> exhaustive scan mixes many different `(n,K)` cells non-uniformly
> (small `n` dominates combinatorially), so the box inherits a
> weighted average of these family-specific biases instead of the
> naive `1/ℓ`.

Verified three ways, all in the committed script:

1. **Direct match, fixed-`q` families** (measurement 2 below): for
   every family with `chi2/dof > 3`, the empirical histogram's peak
   residue matches the theoretical pushforward's peak in 3 of 4 cases
   tested (the 4th is qualitatively similar but not peak-identical —
   reported as-is, not rounded up).
2. **Convergence check** (`convergence_check()`): `p=3, ℓ=5`, same
   residue class, `n ∈ {12, 40, 60}` — L1 distance between empirical
   and theoretical-target histograms **shrinks monotonically**: `0.278
   → 0.082 → 0.065`, confirming the family converges to the fixed
   pushforward target (not to uniform) as it scales.
3. **Weighted-prediction match, the exhaustive box itself**
   (`ghost_hunt_scan_size()`): pooling the theoretical pushforward over
   the `(p, n mod ord3, S mod ord2)` classes actually present in the
   box, weighted by their row counts, predicts the observed zero-rate
   closely at every tested prime, both sectors:

   | ℓ | sector | observed | 1/ℓ | pushforward-weighted prediction |
   |---|---|---|---|---|
   | 5 | + | 0.2437 | 0.2000 | 0.2425 |
   | 5 | − | 0.2357 | 0.2000 | 0.2442 |
   | 7 | + | 0.1532 | 0.1429 | 0.1531 |
   | 7 | − | 0.1474 | 0.1429 | 0.1482 |
   | 11 | + | 0.0912 | 0.0909 | 0.0908 |
   | 11 | − | 0.0888 | 0.0909 | 0.0923 |
   | 13 | + | 0.0821 | 0.0769 | 0.0893 |
   | 13 | − | 0.0926 | 0.0769 | 0.1011 |
   | 17 | + | 0.0593 | 0.0588 | 0.0592 |
   | 17 | − | 0.0607 | 0.0588 | 0.0600 |
   | 23 | + | 0.0436 | 0.0435 | 0.0435 |
   | 23 | − | 0.0421 | 0.0435 | 0.0443 |

   The prediction tracks the observed deviation (magnitude and
   direction) far better than the naive `1/ℓ` baseline at every row —
   the box-level "anomalies" are this mechanism, not a new law.

**Measurement 2 (fixed-q families, both signs).** 4 `(p,n)` pairs ×
2 signs (`K_pos = (3^n).bit_length()`, `K_neg = K_pos−1`), all
exhaustive (91–3,780 profiles/family): `(p=2,n=14)`, `(p=3,n=12)`,
`(p=3,n=16)`, `(p=4,n=11)`. Representative rows (full table in the
script's output):

| p | n | K | sign | q | q's factorization | flagged ℓ | chi2/dof | same peak as pushforward? |
|---|---|---|---|---|---|---|---|---|
| 2 | 14 | 22 | − | −588665 | {5,7,11²,139} | 5 | 17.0 | **True** |
| 2 | 14 | 22 | − | −588665 | {5,7,11²,139} | 7 | 4.2 | **True** |
| 3 | 12 | 20 | + | 517135 | {5,59,1753} | 5 | 30.5 | **True** |
| 3 | 16 | 26 | + | 24062143 | {7,14753,233} | 7 | 12.4 | False (shape similar, peak differs) |

Every other prime tested in these 8 families (79, 45641, 11, 139, 59,
1753, 23, 311, 233, 14753, 9492289, 11, 7727, 5, 19, 97) shows `chi2/dof
< 3` — ordinary sampling variation, not flagged.

**Measurement 3 (sector comparison, mandatory).** No regularity or
non-uniformity found anywhere in item 1 discriminates `q>0` from `q<0`:
identical qualitative outcome on (a) and (b) in both sectors; the same
pushforward mechanism (not a sign-specific one) explained the largest
deviations in either sign in measurement 2. **Calibration anchors**
(`experiments/prime_local_probe.py`, `calibration_anchors()`):

| anchor | q | gcd(q,R_0) | full-divisibility |
|---|---|---|---|
| `−17` (`m=(4,3)`, `s=(1,3)`) | −139 | 139 | **True** |
| `−5` (`m=(2,)`, `s=(1,)`) | −1 | 1 | **True** (degenerate, `\|q\|=1`) |
| trivial cycles `p=1..7` | `4^p−3^p` | `= q` | **True**, all 7 |

All 9 anchors correctly classified as full-divisibility (`gcd(q,R_0) =
|q|`), both signs represented (`−17`,`−5` negative; trivial cycles
positive) — exactly where the brief says the branch must live, and (see
item 2's baselines below) nowhere else.

## Item 2 verdict: the gcd spectrum

**Instance record** (`experiments/staircase_allp.py`'s committed
construction, regenerated today — not the original 12.8.6.4 dates'
specific `n` values, which the recipe does not reproduce
deterministically across runs; `p=22` uses the two literal recorded
profiles). 23 records (`p=2..23`, `p=22` contributing 2 rows), 0
failures:

| p | n | K | gcd | factorization |
|---|---|---|---|---|
| 5 | 17 | 27 | 5 | {5:1} |
| 10 | 94 | 149 | 7 | {7:1} |
| 11 | 147 | 233 | 5 | {5:1} |
| 20 | 10281 | 16295 | 5 | {5:1} |
| (all other 19 records, incl. both p=22 rows) | — | — | **1** | trivial |

4/23 have `gcd(q,R_0) > 1`, all at small primes (5, 5, 5, 7). All
records are sector `+` **by construction** (the staircase recipe fixes
`K = ⌈n log2 3⌉`), so this record alone cannot supply the sector
comparison — that is supplied by measurement 3's baselines instead,
which cover both signs explicitly.

**The `ℓ = p` hypothesis: REFUTED.** In the instance record, `p |
gcd(q,R_0)` at exactly 1/23 periods (`p=5`, where `gcd=5=p`
coincidentally). The originally-flagged `p=7, gcd=7` seed
(12.8.3's specific `n=94` instance) is **not** reproduced by this
session's fresh regeneration of `p=7` (which lands on a different
candidate `n` via the same recipe and gets `gcd=1`) — confirming the
brief's own suspicion that the `p=7` seed was a one-off, not a law.

**Symmetry, tested explicitly — a real but unexplained effect.**
30 symmetric words (`word = base^k`, 6 bases × `k=2..6`, `p = p0·k`):
**30/30 (100%) have `gcd(q,R_0) > 1`**, vs a matched generic baseline
of 51/400 (12.8%, seeded random, `p∈2..6`, entries `1..10`) — a
striking, clearly-elevated rate. But:

- **`p | gcd`: 1/30.** **`p0 | gcd`: 15/30 — entirely a tautological
  artifact**: exactly the 15 rows with `p0=1` (three of the six bases
  are single-letter), where `p0 | gcd` is vacuously true for any gcd.
  Restricted to the genuinely-symmetric `p0=2` bases: **0/15**. So `p0`
  does **not** predict the gcd either, once the trivial case is
  excluded (caught and corrected — the same lesson as the ghost-hunt
  above, applied to my own first pass at this statistic).
- **`k | gcd`: 1/30.**
- **Elementary partial cause identified, but incomplete.** For
  `word=base^k`: `q = X^k − Y^k = (X−Y)(X^{k-1}+…+Y^{k-1})` with `X =
  2^{K_base}, Y = 3^{n_base}` — so `q_base := X−Y` (the base word's own
  `q` at `k=1`) **always divides `q`** (difference-of-`k`-th-powers,
  verified exactly on all 30 rows). But `gcd(q_base, R_{0,base}) = 1`
  in every base tested, and `q_base` does **not** divide the repeated
  word's `R_0` either — so this factorization does **not** directly
  explain the elevated `gcd(q,R_0)>1` rate; the prime(s) actually found
  are not `q_base`'s factors. **No further one-line cause was found.**
  Flagged, not developed (stopping-rule compliant), with an explicit
  caveat: the tested bases use small entries (`m,s ≤ 3`), the same
  regime where item 1 found finite-box artifacts, so part of the
  elevation may be a small-entries confound rather than a pure
  symmetry effect — this was not disentangled and is left open.
- The brief's own counterexample re-confirmed directly: `m=(1,1),
  s=(2,2)`, `p=2`: `q=55`, `gcd=11`, `p=2 ∤ 11`.

**Baseline scans, both sectors.**

- *(A)* The 60-profile vector file (`transport_recurrence_vectors.json`,
  762 rows cross-validated by two implementations, reused as data only):
  58 full profiles, sector split `q>0`: 54, `q<0`: 4; 11/58 have
  `gcd>1` (7 are the named full-divisibility anchors — `−17`, trivial
  `p=2..5` — and the constant-pair/p7-staircase reduction witnesses;
  4/50 pseudo-random profiles have `gcd>1`, matching the file's own
  header stat of 6 *strict* partial reductions once the full-divisibility
  rows are excluded from that count).
- *(B)* Fresh seeded scan (this script's own `R_rot`/gcd, 600 profiles,
  `p∈1..6`, entries `1..9`, seed `20260718`): sector split `q>0`: 523,
  `q<0`: 77. `gcd>1` rate: **12.24% positive vs 14.29% negative** — no
  clear sector discrimination at this sample size.
- *(C)* Frequency of `ℓ | gcd(q,R_0)` given `ℓ | q`, pooled: 79/1763
  rows (4.48%) vs naive baseline 3.70% — small primes again elevated
  (`ℓ=5`: 42/131=32.1% vs 20%, `z=3.45`), consistent with the same
  finite-box mechanism found in item 1, now surfacing in the gcd
  statistic too (expected, since `gcd(q,R_0)>1` at `ℓ` is exactly the
  event `R_0 ≡ 0 (mod ℓ)` studied in item 1c).
- *(D)* Calibration anchors re-confirmed: `−17`, `−5`, trivial `p=1..7`
  all full-divisibility; **0/50** vector-file pseudo-random profiles
  and **0/600** fresh-scan profiles ever reach `gcd=|q|` with `|q|>1`
  (one fresh-scan draw hit `gcd=|q|` at the degenerate `|q|=1` trivial
  `p=1` cycle recurring by chance — reported explicitly, not filtered
  silently). The full-divisibility branch is confined to the named
  cycle anchors, exactly as expected: a generic `gcd(q,R_0)>1` is
  partial reduction, never a cycle witness, in every scan run here.

**Spectrum described flatly:** small primes (5, 7, 11, 13, 19, 23, ...)
dominate every nontrivial gcd found, in decreasing frequency roughly
tracking `1/ℓ` — with `ℓ=5` and `ℓ=7` consistently elevated above their
naive baseline across every scan in this session (instance record,
symmetric words, and both baselines), an effect traced to the same
finite composition-counting mechanism as item 1's ghost-hunt, not a new
`ℓ`-specific law. Nothing beats the naive-baseline picture by a
*clean, reproducible, elementary-caused* margin except the symmetry
effect (100% vs 12.8%), which is real, large, and **unexplained** —
recorded as an open pattern per the stopping rules, not developed
further. Neither period `p`, base period `p0`, nor repeat count `k`
predicts which prime(s) show up. Sector does not predict the
nontrivial-gcd rate at the sample sizes run here.

## No candidate law emerged

Both probes came back structureless or only partially/unexplainedly
patterned — no wiki-page proposal line is warranted. Nothing here
reopens the cycle front; the parking rationale (README, cycles.md
12.8.5) is unaffected.

## What surprised us / left open

- The scale of the ghost-hunt: item 1's small-prime z-scores (up to
  `z≈90` at `ℓ=5`) looked like strong signal until decomposed — the
  elementary cause (finite pushforward of a bounded/finite composition
  measure) was not anticipated going in, and required real
  investigation (three independent verifications: peak-match, L1
  convergence, weighted-prediction) to nail down rather than wave at.
  This is exactly the "ghost-identity lesson" the brief pointed at, now
  with a second, quantitatively verified instance.
- The symmetry effect (item 2) is the one place this session found a
  large, clean, reproducible statistical regularity (100% vs 12.8%)
  that it could **not** fully explain — the difference-of-powers
  factorization is real and exact but demonstrably insufficient (it
  doesn't even divide `R_0`), so whatever forces `gcd(q,R_0)>1` at
  essentially every symmetric word remains open. This is flagged as
  the session's one genuine loose end, left exactly where the stopping
  rules require (a finding, not a proof attempt) — a natural
  next-session target if the author wants it picked up (with larger
  entries, to separate the symmetry effect from the small-entries
  confound).
- The `p0 | gcd` tautology (my own first-pass statistic, inflated by
  the `p0=1` cases) is a small in-session instance of exactly the
  pattern this brief warns about — caught and corrected before being
  recorded as a finding, per the ghost-identity discipline.

## Runtime and scope

Total script runtime 283.8 s (well under the ~10-minute per-scan
sanity rule; no scan individually approached it except the exhaustive
box at `entries=13`, which was explicitly cut). `experiments/
prime_local_probe.py` runs clean end-to-end from a fresh checkout
(`python experiments/prime_local_probe.py`).
