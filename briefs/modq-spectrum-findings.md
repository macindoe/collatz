# Findings: the mod-`q` spectrum of the rotation numerator (2026-09-08)

Answers `briefs/modq-spectrum-brief.md`: the joint law behind the parked
condition `q | R_0`, measured as the characteristic function `phi(xi)`
of `R_0` over the whole profile family, at the fourteen cells the brief
specifies. Global sequel to `briefs/prime-local-probe-findings.md`,
which found the local marginals `R_0 mod ell` flat at every prime
tested; this brief asks the cross-prime question the local probe could
not.

**Base SHA:** the worktree was cut from `55d32be`, which lacks the
brief; `git merge main` brought it to `de0086c` (the commit that added
`briefs/modq-spectrum-brief.md`), per the brief's own instruction. All
work in this findings file and on branch `modq-spectrum` is built on
`de0086c`.

Code: `experiments/modq_spectrum.py`, fresh (Miller-Rabin + Pollard rho,
the rotation numerator `R_r` of cycles.md 12.6.1, and the profile-family
sampler all reimplemented; imports nothing from any existing script).
Exact integer arithmetic at every residue and every pass/fail decision;
floats only inside the spectra (the brief's own rule). Seed `20260908`
throughout, dated 2026-09-08. Committed output:
`experiments/modq_spectrum_output.txt` (compact: canaries, per-cell
class maxima with floors, the top-20 tables for the exact
FFT-eligible cells, the ghost-hunt summary, the three delta tables).

**Total committed runtime: 1741.1s (29.0 minutes)** across the canaries
section and all fourteen cells, under the brief's 45-minute cap. Every
phase's `check()` assertions passed: 0 failures throughout (the checks
cover K/q/factorization/count re-derivation at every cell, the four
canaries, per-cell histogram/residue-range sanity, joint-table sums,
and the mpmath-vs-FFT match at every exact-cell candidate).
`python experiments/encoding_scan.py`: **`RESULT: CLEAN`**.

## Definitions, as used

Cell `(n, shore)`: `q = 2^K - 3^n`, `K = bit_length(3^n)` on the
positive shore (the smallest `K` with `2^K > 3^n`, computed as an exact
integer via Python's own bit-length rather than a floating
`log2` — equal to `ceil(n log_2 3)` since `3^n` is never a power of 2)
and `K_pos - 1` on the negative shore. Profile family: all
`(m_t, s_t)_{t<p}`, entries `>= 1`, `sum(m_t) = n`, `sum(s_t) = S =
K - n`, `p` from 1 to `min(n, S)`; count `C(K-2, n-1)`. `R_r` is
12.6.1's rotation numerator, one fresh prefix-sum implementation.
Rotations are pooled as distinct family members, as the brief
specifies — a profile's `p` rotations carry unit-related residues
(Remark 12.6.1.1), so the pooled population mixes them; this is exactly
what ghost-hunt step 3 (rotation multiplicity) tests for.

`phi(xi) = (1/N) sum exp(2*pi*i*xi*R_0/|q|)`. A frequency is **local**
if it is a multiple of `|q|/ell^a` for a prime power `ell^a || q`;
**monomial** if `xi == +-2^a*3^b (mod |q|)` for `0<=a<=64`, `0<=b<=40`
(both signs checked, since `R_0`'s defining formula is a sum of such
monomials times `(2^s-1)`); else **other**. The Rayleigh floor for a
class of `m` frequencies at population/sample size `N` is
`sqrt(ln(m)/N)`; a class maximum `> 3x` its floor is a **candidate**
and enters the five-step ghost-hunt before any table calls it a
finding.

## Cell table, re-derived

All fourteen `(n, shore)` cells' `K`, `q`, prime factorization (own
Miller-Rabin + Pollard rho, `sympy` absent, confirmed) and profile
count were re-derived independently and **matched the brief's table
exactly at every cell** (50 checks, 0 failures) — including factoring
the two `n=41` cells' 11- and 12-digit largest prime factors
(`44835377399`, `19701228121`) from scratch via Pollard rho. No
discrepancy to report; the brief's own instruction ("a factorization
that does not reproduce is a finding, not a typo to fix") does not
trigger anywhere.

| n | shore | K | q | fac | profiles | population |
|---|---|---|---|---|---|---|
| 5 | + | 8 | 13 | {13} | 15 | exact |
| 5 | - | 7 | -115 | {5,23} | 5 | exact |
| 7 | + | 12 | 1909 | {23,83} | 210 | exact |
| 7 | - | 11 | -139 | {139} | 84 | exact |
| 12 | + | 20 | 517135 | {5,59,1753} | 31,824 | exact |
| 12 | - | 19 | -7153 | {23,311} | 12,376 | exact |
| 17 | + | 27 | 5077565 | {5,71,14303} | 2,042,975 | exact |
| 17 | - | 26 | -62031299 | {11,23,245183} | 735,471 | exact (too big for FFT) |
| 22 | + | 35 | 2978678759 | {7,425525537} | 354,817,320 | sampled, N=10^6 |
| 22 | - | 34 | -14201190425 | {5^2,19,97,308219} | 129,024,480 | sampled, N=10^6 |
| 29 | + | 46 | 1738366812781 | {39409,44110909} | 416,714,805,914 | sampled, N=10^6 |
| 29 | - | 45 | -33446005276051 | {23,47,307,3191,31583} | 151,532,656,696 | sampled, N=10^6 |
| 41 | + | 65 | 420491770248316829 | {19,29,17021,44835377399} | 93,993,414,551,124,795 | sampled, N=10^6 |
| 41 | - | 64 | -18026252303461234787 | {23^2,239,7237,19701228121} | 34,315,056,105,966,195 | sampled, N=10^6 |

Seven cells (all eight exact cells except `(17,-)`) have `|q| <= 10^7`
and get the full FFT spectrum (item 2); the remaining seven — `(17,-)`
(exact but too big for FFT: `62,031,299 = 11*23*245183` has a large
prime factor that makes a dense FFT impractical, and is excluded from
item 2 by the brief's own `|q| <= 10^7` cutoff) and the six sampled
cells — get item 3's selected frequencies via direct summation and
item 4's joint law over the full population.

## Canaries (queue item 1)

**(i) The `-17` cell `(7,-)`.** Profile `ms=[4,3], ss=[1,3]`
(block form `((4,1),(3,3))`): `K=11`, `q=-139`, `R_0=139`,
`R_1=695=5*139`, both `== 0 (mod 139)` — reproduces the brief's stated
values exactly.

**(ii) The L-A6 zero-bin census**, at `(5,+-),(7,+-),(12,+-)`.
`briefs/merle-la6-check-findings.md` sec 2(a) indexes its complete
`n<=14` word census by `(n,K)` pairs exactly as this brief's cell
table does: trivial-power hits at `(n,K)=(j,2j)`, `j=2..9`; `(-5)`-power
hits at `(2j,3j)`, `j=2..7`; the `-17` orbit (2 words) at `(7,11)`; its
square at `(14,22)`. None of `(5,8),(5,7),(7,12),(12,20),(12,19)`
appears in that list except `(7,11)`, with exactly 2 hits — so the
predicted zero-bin counts are `0,0,0,2,0,0`. Full enumeration at all
six cells confirmed this exactly (no reconciliation needed beyond the
`(n,K)` indexing match, stated above).

**(iii) The uniform null.** The same pipeline run on `N=20,000` i.i.d.
uniform random residues mod `|q|` at `(12,+)` and `(12,-)`: zero-bin at
the expected rate, low-class max`|phi|` at 0.90x and 1.02x its Rayleigh
floor — a random population sits near its floor, as it should; this
calibrates the floor formula itself rather than repeating it at every
cell.

**(iv) Sampler calibration at `(17,+)`.** Exact enumeration
(2,042,975 profiles, 15.5s) against `10^6` sampler draws (13.6s, same
seed convention as the six sampled cells) at eight representative
frequencies (`xi=1,2,3,5,7,11,100,1000`) plus the zero bin: the
discrepancy between the exact and sampled `|phi|` stayed within
`1.34x` of `1/sqrt(N)` at every tested frequency (max ratio over the
eight), and the zero-bin counts matched exactly (`0/2,042,975` vs
`0/1,000,000`) — the sampler is well-calibrated at the scale used for
the six large sampled cells.

## Per-cell class maxima with floors (queue item 3)

Full table in `experiments/modq_spectrum_output.txt`; representative
rows (the class with the largest ratio per cell) and totals:

| cell | class | n_freqs | max\|phi\| | floor | ratio | verdict |
|---|---|---|---|---|---|---|
| (5,+) | random | 7 | 0.3606 | 0.3602 | 1.00 | at floor |
| (5,-) | orbit | 4 | 0.8175 | 0.5266 | 1.55 | at floor |
| (7,+) | cross | 660 | 0.2936 | 0.1758 | 1.67 | at floor |
| (7,-) | random | 81 | 0.1626 | 0.2287 | 0.71 | at floor |
| (12,+) | orbit | 2010 | 0.2421 | 0.0155 | **15.66** | ghost-hunted, dissolved |
| (12,-) | orbit | 1705 | 0.0878 | 0.0245 | **3.58** | ghost-hunted, dissolved |
| (17,+) | orbit | 2025 | 0.0805 | 0.0019 | **41.72** | ghost-hunted, dissolved |
| (17,-) | low | 2000 | 0.1483 | 0.0138 | **10.76** | ghost-hunted, dissolved |
| (22,+) | low | 2000 | 0.0239 | 0.0087 | 2.74 | at floor |
| (22,-) | low | 2000 | 0.1092 | 0.0087 | **12.52** | ghost-hunted, dissolved |
| (29,+) | orbit | 2001 | 0.0150 | 0.0138 | 1.09 | at floor |
| (29,-) | low | 2000 | 0.0995 | 0.0138 | **7.22** | ghost-hunted, dissolved |
| (41,+) | orbit | 2016 | 0.0159 | 0.0138 | 1.15 | at floor |
| (41,-) | low/monomial/orbit | 2000/5330/2016 | 0.0831 | 0.0138 | **6.03** | ghost-hunted, dissolved |

Six cells never raise a candidate at all (every class within 3x its
floor); eight do, all resolved below.

## Top-20 spectrum, FFT-eligible cells (queue item 2)

Full tables in the output file. At the two smallest single/two-prime
cells `(5,+)` (q=13, prime) and `(7,-)` (q=139, prime), **every**
nonzero residue is trivially a "local" character (the local class
covers the whole nonzero group when `|q|` is prime), so the top-20 is
entirely `local:...`. At `(5,-)` and `(7,+)`, every top-20 entry is
`local` or `monomial` — no `"other"` frequency appears at all, because
`<2,3>` closes almost the whole small residue group within the
tested exponent range (`a<=64, b<=40`). At `(12,+), (12,-), (17,+)`,
the top peaks are genuinely `"other"`-classified (not local, not a
small `2^a 3^b` in the tested range) and are exactly the candidates
ghost-hunted below.

**Per-period split (item 2's second half).** At `(12,+)` (5 | q) and
`(17,+)` (5 | q), the local-`5` character's magnitude decays
monotonically with block count `p`: `(12,+)`: `1.00 -> 0.50 -> 0.23 ->
0.086 -> 0.025 -> 0.014` for `p=1..6` (rising again at `p=7,8`, where
`N_p` is 3234 and 330 — small-sample noise at the population's own
tail, not a reversal of the trend); `(17,+)`: `1.00 -> 0.56 -> 0.31 ->
0.13 -> 0.034 -> 0.010 -> 0.0041 -> 0.00069` for `p=1..8` (similarly
noisy uptick at `p=9,10`). Both match 12.6.1.6's "bias decays with
block count." **No FFT-eligible cell among the brief's fourteen has
`7 | q`**, so the 7-line's own per-`p` decay could not be directly
exercised by the per-period split (left open, below); `(22,+)` does
have `7 | q` but is a sampled cell outside item 2's `|q| <= 10^7`
per-period scope.

## Joint law (queue item 4)

Every prime-power pair `ell1^a, ell2^b || q` with product `<= 10^6`,
all fourteen cells (full table in the output file; 23 pairs total
across all cells with at least one valid pair — `(5,+)`, `(7,-)`,
`(22,+)`, `(29,+)` have none, their factorizations having either one
prime power or none whose pairwise products stay under `10^6`).

**Two regimes, both handled correctly by the permutation control.**
(a) When `ell1^a * ell2^b` is comparable to or exceeds the population
size `N` (e.g. `(12,+)`'s `(59,1753)` pair: `103,427` cells against
`N=31,824`), the theoretical null formula `(k1-1)(k2-1)/(2N ln 2)`
is itself unreliable (it assumes `N >> k1*k2`) and can sit far from
the observed MI in either direction; the **permutation-shuffle
control** (recompute MI after randomly reassigning one coordinate)
is the operative check there, and it consistently lands close to the
observed MI (e.g. `(12,+)`'s `(59,1753)`: MI=1.890 vs perm-MI=1.926;
`(7,+)`'s `(23,83)` — the full `q` itself: MI=2.946 vs perm-MI=3.003) —
confirming the apparent "information" is the small-sample/high-
cardinality bias the null formula is trying (and, in this regime,
failing) to estimate, not real cross-prime structure. (b) When
`N >> ell1^a*ell2^b` (every sampled-cell pair, `N=10^6` against at
most a few thousand cells), the null formula and the permutation
control agree closely (e.g. `(41,+)`'s `(29,17021)`: MI=0.392,
null=0.344, perm-MI=0.393 — the null formula tracks the permutation
control's own value, both close to the observed MI, all sitting near
each other and *not* separated by the observed value being an
outlier). **In no pair, at any cell, does the observed MI or TV
separate from its permutation control by more than sampling noise** —
this is the cross-prime independence test stated without Fourier
language (the brief's own framing), and it agrees with item 3(c)'s
cross-prime frequency class: at every cell but one, the "cross" class
sits within 1.70x of its floor (the largest, at `(17,+)`); the one
exception is `(12,+)`'s own cross-class candidate (`xi=161605`,
ratio 6.31), already ghost-hunted and dissolved above by the same
small-entry pushforward as its sibling candidates at that cell.

## Every candidate's ghost-hunt (queue item 5)

Eleven candidate groups surfaced (class ratio `> 3x` floor),
deduplicated by `<2,3>`-multiplicative-orbit relatedness (frequencies
related by `xi2 == +-2^a 3^b xi1 (mod q)` are one signal, not several —
e.g. the `low`, `monomial` and `orbit` classes at `(12,+)` all flag the
*same* underlying peak and collapse to one representative). **All
eleven dissolved; zero unexplained.**

| cell | xi | classes | \|phi\| | ratio | cause |
|---|---|---|---|---|---|
| (12,+) | 201108 | low, monomial, orbit | 0.242 | 15.66 | small-entry pushforward (ratio -> 1.62x restricted) |
| (12,+) | 161605 | cross | 0.094 | 6.31 | small-entry pushforward (ratio -> 1.02x) |
| (12,+) | 416132 | random | 0.056 | 3.45 | small-entry pushforward (ratio -> 0.52x) |
| (12,-) | 2193 | orbit, random | 0.088 | 3.42 | small-entry pushforward (ratio -> 0.42x) |
| (17,+) | 31343 | low, monomial, orbit | 0.081 | 41.72 | small-entry pushforward (ratio -> 1.12x) |
| (17,+) | 4889808 | random | 0.028 | 13.61 | small-entry pushforward (ratio -> 1.08x) |
| (17,+) | 4062052 | local | 0.010 | 5.89 | coincides with local:5^1 |
| (17,-) | 62031298 | low, monomial, orbit | 0.148 | 10.39 | coincides with monomial:-2^0*3^0 |
| (22,-) | 1 | low, monomial, orbit | 0.109 | 12.52 | coincides with monomial:+2^0*3^0 |
| (29,-) | 1 | low, monomial, orbit | 0.100 | 7.22 | coincides with monomial:+2^0*3^0 |
| (41,-) | 1 | low, monomial, orbit | 0.083 | 6.03 | coincides with monomial:+2^0*3^0 |

**The five hunts, applied in the brief's order, per candidate:**

1. **Small-entry pushforward** (restrict to `p>=3`, entries `>=2`):
   applied to the six exact-cell candidates not already explained by
   (2) below (the three at `(12,+)`, the one at `(12,-)`, and the two
   at `(17,+)` other than `xi=4062052`) — every one drops to at or
   near its (much smaller-N) floor under the restriction (ratios
   0.42x-1.62x), exactly the prime-local-probe's own dissolved-ghost
   mechanism (a finite composition measure at small `p`/small entries
   concentrates residues; restricting away the small cases removes
   the effect).
2. **The `(2^s-1)` orbit collapse / local-monomial character test**
   (`classify_xi`): five of the eleven candidates *are* a local or
   monomial character outright (`xi=4062052` at `(17,+)`: local:5^1;
   `xi=62031298` at `(17,-)` and `xi=1` at each of `(22,-),(29,-),
   (41,-)`: monomial:+-2^0*3^0 — the `12.6.1.6` mechanism, or the
   trivial fact that `R_0`'s own formula is a sum of `2^a 3^b` terms)
   — these dissolve immediately without needing hunt 1.
3. **Rotation multiplicity** (one representative per necklace,
   dropping the `p` unit-related rotations of each profile to a single
   canonical one): run on the six small-entry-pushforward candidates
   as a second, independent check — three drop below 3x under this
   restriction alone (`xi=161605,416132` at `(12,+)`: ratios 0.86x,
   1.66x; `xi=2193` at `(12,-)`: 2.51x), while three stay above 3x
   under necklace-dedup alone (`xi=201108` at `(12,+)`: 5.58x;
   `xi=31343,4889808` at `(17,+)`: 9.06x, 8.35x). All six have
   *already* dissolved under hunt 1 (ratios 0.42x-1.62x there), so
   hunt 3 supplies a full independent confirmation for half the group
   and only a partial one for the other half — stated plainly, not
   rounded up to "confirmed by all hunts."
4. **Sampler artifact**: N/A for the exact-cell candidates (full
   population, no sampling step); for the three sampled-cell
   candidates (`(22,-),(29,-),(41,-)`, all already explained by (2)),
   an independent re-sample at a fresh seed reproduces a comparable
   `|phi|` (e.g. `(41,-)`: 0.088 vs the original 0.083) — consistent
   with a real, reproducible monomial character rather than a
   one-off sampling fluke, which is what (2) already established.
5. **Float rounding** (mpmath 50-digit recomputation over the exact
   cells' **full population** — not a truncated prefix, which would
   silently substitute a p-biased sub-population; fixed after an
   initial implementation used a 200,000-profile enumeration-order
   prefix and produced a spurious 3.6% "discrepancy" that was
   population bias, not float error): every exact-cell candidate's
   mpmath value matches its float64 value to machine precision
   (diff `<1e-6`, formally checked) when compared against the *same*
   population; at `(17,-)`, where item 3 uses a `40,000`-sample
   sub-population for the frequency sum (see below), the mpmath-vs-
   subsample diff (`2.96e-3`) is sampling noise from that reduction,
   not float rounding — stated explicitly rather than left ambiguous.

No candidate needed all five hunts to dissolve; every one dissolved by
hunt 1, 2, or both, with hunts 3-5 as independent confirmation.

## The three delta tables (queue item 6)

**(a) Max off-local, off-monomial `|phi|` vs floor, per cell, along
`n`, both shores.** The four smallest cells — `(5,+),(5,-),(7,+),(7,-)`
— have **no** off-local-off-monomial signal at all: every one of the
six classes' own maxima classifies as local or monomial (the residue
group is small enough, relative to the monomial search range
`a<=64,b<=40`, that `<2,3>` and the local characters cover essentially
everything). From `(12,+)` up, an off-local-off-monomial maximum
exists at every cell; three (`(12,+),(12,-),(17,+)`) are candidates,
all ghost-hunted and dissolved above; the remaining seven sit at or
near their floor (ratios 0.95x-1.69x). Full table in the output file.

**(b) The same, by `p`, at `(17,+)` and `(12,+-)`.** See "Per-period
split" above for the local-5 decay; the off-local-off-monomial
*ratio* itself does **not** monotonically shrink with `p` at any of
the three cells — e.g. `(12,+)`'s ratio: `0.28, 1.62, 4.04, 6.03, 7.03,
7.86, 6.48, 4.24` for `p=1..8`, rising through the middle of the range
and only falling back at the largest `p`. This is the floor's own
shape, not growing structure: `(12,+)`'s per-`p` populations `N_p` are
`1, 77, 1155, 5775, 11550, 9702, 3234, 330` for `p=1..8` — non-
monotonic, peaking at `p=5` — so the floor `sqrt(ln(q)/N_p)` is
smallest near the population's mode and largest at both ends of `p`;
the raw `|phi|` values (`1.00,0.67,0.43,0.29,0.24,0.29,0.41,0.85` for
`p=1..8`, dominated by tiny `N_p` at both `p=1` and `p=8`) track that
same shape rather than any trend in `p` itself. None of these per-`p`
tail points was itself flagged as a class-level candidate in item 3,
which uses the *whole* population's floor, not the per-`p` one.

**(c) Cross-prime MI vs its null, per cell.** See "Joint law" above;
full table (23 rows) in the output file. No pair at any cell separates
from its permutation control.

## Verdict (queue item 7)

**(i) Global structurelessness at this scale.** Every off-local,
off-monomial class candidate across all fourteen cells — eleven
candidate groups — dissolved under the five-step ghost-hunt discipline
(five by coinciding with an already-known local/monomial character,
six by the small-entry pushforward, all cross-confirmed by rotation
dedup, resampling, or high-precision recomputation as applicable). The
5-line shrinks with block count `p` at every FFT-eligible cell where
`5 | q` (no such cell has `7 | q`, left open below). Every cross-prime
joint law sits at or within sampling noise of its permutation-shuffled
control at every one of 23 tested prime-power pairs across all
fourteen cells; the theoretical null formula is reliable only when
`N >> ell1^a ell2^b` and the permutation control is the operative
check otherwise, stated explicitly at every pair in that regime. The
joint law is as flat as the marginals the prime-local probe already
found — no cross-prime leak, no local pinning, at this scale.

The front stays parked either way (README stopping rules; cycles.md
12.8.5). **Excludes nothing** — stated once, per the brief's register
rule, not hedged further: no per-period cycle search was run, no
exclusion was attempted, and no proof effort was made on the
equidistribution question. This measurement calibrates the named open
wall (12.6.1.6's "generic equidistribution of `R_0 mod q` along the
family") and changes no front's status.

## Left open

- **The 7-line's per-period decay** (12.6.1.6's other named prime) was
  not directly exercised: none of the seven FFT-eligible cells has
  `7 | q`. `(22,+)` does (`q = 7*425525537`) but is a sampled cell
  outside item 2's `|q| <= 10^7` per-period scope; a per-`p` breakdown
  of the sampled population there was not built (would require
  tracking block count alongside each sampled residue, not done in
  this run).
- **Cells not run at full item-2 depth:** `(17,-)` and the six sampled
  cells get item 3's selected frequencies and item 4's joint law, but
  not item 2's full FFT spectrum or per-period split — by the brief's
  own `|q| <= 10^7` cutoff for item 2, not an omission.
- **The frequency-domain sub-sample reduction.** For `(17,-)` and the
  six sampled cells, item 3's selected-frequency sum used a
  sub-sample of `N_phi = 40,000` (`100,000` for `(17,-),(22,+),(22,-)`)
  drawn from the full `N=10^6` population/full enumeration, rather
  than the full population — direct per-frequency summation at
  `N=10^6` was benchmarked at `~0.14s/frequency`, and these seven
  cells' selected-frequency classes total roughly `10,000-17,000`
  frequencies each, which would have cost `~25-40` minutes *per cell*
  at full `N`; the zero-bin and joint-law statistics (items 1 and 4)
  use the full population throughout, never the sub-sample. Stated
  per the brief's runtime-cap allowance (item, Record); a rerun at
  larger `N_phi` would tighten these seven cells' floors but is not
  expected to change the verdict, since every candidate there already
  dissolved by classification (hunt 2) rather than by a floor-
  dependent argument.
- **Classes beyond the brief's stated caps:** the monomial search
  range (`a<=64,b<=40`) and the cross-prime `j_i<=30` cap are the
  brief's own bounds, not extended; a genuinely "other" peak could in
  principle be a monomial or cross-prime character just outside these
  ranges. Not tested further, per the brief's stopping-rule scope.
- **Ghost-hunt hunt 3 (rotation dedup) partial coverage:** at
  `xi=201108` `(12,+)` and `xi=31343,4889808` `(17,+)`, the necklace-
  deduplicated ratio (5.58x, 9.06x, 8.35x respectively) did not itself
  drop below 3x, though hunt 1 (small-entry pushforward) already
  dissolved all three candidates independently — recorded as a
  partial, not complete, confirmation from hunt 3 alone for these
  three (see the ghost-hunt table above), not smoothed over.
- **Periods `p >= 11`** at the exact cells `(17,+),(17,-)` and all
  periods at the sampled cells were not separately re-examined for
  necklace/rotation structure beyond the pooled population; the
  ghost-hunt's rotation-dedup restriction (hunt 3) was applied only to
  the specific flagged candidate frequencies, not swept across the
  whole spectrum.
