# Findings: the mod-`q` spectrum of the rotation numerator (2026-09-08)

Answers `briefs/modq-spectrum-brief.md`: the joint law behind the parked
condition `q | R_0`, measured as the characteristic function `phi(xi)`
of `R_0` over the whole profile family, at the fourteen cells the brief
specifies. Global sequel to `briefs/prime-local-probe-findings.md`,
which found the local marginals `R_0 mod ell` flat at every prime
tested; this brief asks the cross-prime question the local probe could
not.

**Revised after coordinator review (2026-09-08, same date, second
pass):** two corrections from the review are folded in throughout this
file and in the committed output: (1) the script is now reproducible
end to end from a single command (see "Reproducibility" below); (2) the
four `xi = +-1` dissolutions originally labeled "coincides with a
monomial `2^0*3^0` character" — a classification, not a cause — are
relabeled to their actual cause, a magnitude effect (**hunt 6** below),
after the coordinator's independent check with fresh code found the
first harmonic tracks `2^K/|q|`, not the shore. Two more `xi=+-1`
signals that an earlier, over-permissive `<2,3>`-orbit dedup step had
silently merged into two *different* (correctly small-entry-pushforward
-caused) candidate groups at `(12,+)` and `(17,+)` are split out and
separately confirmed by the same hunt. The `cycles.md` sentence is
rewritten to state this rather than "came back flat at every cell",
which overstated the earlier result once the harmonic is acknowledged.

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
throughout, dated 2026-09-08.

## Reproducibility

**Single command, reproduces the committed output end to end:**

```bash
python -u experiments/modq_spectrum.py all > experiments/modq_spectrum_output.txt
```

This runs every phase in sequence (cell-table re-derivation, canaries,
all seven FFT-eligible cells, all seven "large" cells at the committed
run's `N_phi` sub-sample sizes, then the assemble/summary section) in
one process, and the shell redirection captures the complete transcript
— not a hand-picked "compact" excerpt — into
`experiments/modq_spectrum_output.txt`. **Confirmed**: this exact
command was run and its output committed (not assembled by hand from
separate per-cell invocations); a subsequent isolated re-run of one
cell (`python -u experiments/modq_spectrum.py fft 5+`) reproduced its
section of the committed transcript exactly, character for character
(the enumeration, top-20 table, hunt-6 numbers and check count all
matched) -- consistent with the underlying computation being fully
deterministic under the fixed seed (every count, residue, ratio and
verdict; only wall-clock timing lines vary run to run). An earlier cut of the
`all` phase was not wired up at all (a bare invocation printed a stub
message and exited) — that stub is now removed. A second bug was found
and fixed while wiring this up: `assemble()`'s own internal write to
`experiments/modq_spectrum_output.txt` conflicted with the shell's
redirection to the *same* path, truncating the file mid-stream (the
first attempt at this fix produced a corrupted file with the compact
summary overwritten into the middle of the transcript and garbage
padding after it — caught before committing). `assemble()` now only
prints; the standalone `assemble` CLI phase (for use against a
separately pinned `MODQ_CACHE_DIR`) does the file-write itself, once,
with no redirection race.

The JSON cache defaults to a fresh `tempfile.mkdtemp()` directory every
run (no hand-set path); set `MODQ_CACHE_DIR` to pin a location instead
(e.g. to split the run across the per-cell CLI phases, or to inspect
intermediate per-cell results).

**Runtime: 1522.3s (25.4 minutes)** for the single-command run, under
the brief's 45-minute cap — faster than the 1741.1s the same fourteen
cells took as separate invocations in the first pass, because the
exact (unreduced) `R_0` computation added for hunt 6 (table-lookup
powers of 2 and 3, no per-term modular `pow()`) turned out to be ~4x
faster than the modular-reduction path it replaced (benchmarked: 3.6s
vs 15.5s enumerating `(17,+)`'s 2,042,975 profiles) — more than
offsetting hunt 6's added vectorized cost. **124 checks, 0 failures**
for the whole run (cell-table re-derivation, the four canaries,
per-cell histogram/residue-range sanity, joint-table sums, and the
mpmath-vs-FFT match at every exact-cell ghost-hunt candidate). The
seven "large" cells keep the same `N_phi` sub-sample sizes as the
first pass (`40,000` for `(17,-),(29,+-),(41,+-)`; `100,000` for
`(22,+-)`) to stay under the runtime cap — kept, not tightened, per
the brief's explicit allowance; see "Left open."

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
(2,042,975 profiles, 15.6s) against `10^6` sampler draws (13.4s, same
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

## Every candidate's ghost-hunt (queue item 5, plus hunt 6)

**Revised after coordinator review.** Thirteen candidate groups
surfaced in total (eleven in the first pass; two more split out below).
Eleven class-level candidates (ratio `> 3x` floor) were collapsed by
`<2,3>`-multiplicative-orbit relatedness (frequencies related by
`xi2 == +-2^a 3^b xi1 (mod q)` are one signal, not several) into nine
groups, but the coordinator's review found this dedup test **too
permissive at two cells**: at `(12,+)` and `(17,+)`, the `low` (or
`monomial`) class's own candidate — which independently lands at
`xi=+-1` at *every* cell, per hunt 6 below — happened to be
`<2,3>`-related to a much larger, *unrelated* peak (`xi=201108` at
`(12,+)`, `xi=31343` at `(17,+)`, both genuinely explained by the
small-entry pushforward) purely because the dedup test's search range
(`a<=24,b<=16`, both signs) is wide enough to find *some* small-exponent
relation between many unrelated residue pairs at these moderately-sized
`|q|`. Being `<2,3>`-related is an arithmetic coincidence test, not a
shared-cause claim, and conflating the two here would have hidden the
`xi=+-1` signal's real, different cause behind the pushforward's. Both
are now split out and re-examined on their own. **All thirteen
dissolved; zero unexplained** (nine originally, four relabeled and two
split-and-explained by hunt 6 below).

| cell | xi | classes | \|phi\| | ratio | cause |
|---|---|---|---|---|---|
| (12,+) | 201108 | low, monomial, orbit | 0.242 | 15.66 | small-entry pushforward (ratio -> 1.62x restricted) |
| (12,+) | 517134 | monomial *(split from the 201108 group)* | 0.106 | 6.70 | **hunt 6, magnitude** (below) |
| (12,+) | 161605 | cross | 0.094 | 6.31 | small-entry pushforward (ratio -> 1.02x) |
| (12,+) | 416132 | random | 0.056 | 3.45 | small-entry pushforward (ratio -> 0.52x) |
| (12,-) | 2193 | orbit, random | 0.088 | 3.42 | small-entry pushforward (ratio -> 0.42x) |
| (17,+) | 31343 | low, monomial, orbit | 0.081 | 41.72 | small-entry pushforward (ratio -> 1.12x) |
| (17,+) | 5077564 | monomial *(split from the 31343 group)* | 0.013 | 6.62 | **hunt 6, magnitude** (below) |
| (17,+) | 4889808 | random | 0.028 | 13.61 | small-entry pushforward (ratio -> 1.08x) |
| (17,+) | 4062052 | local | 0.010 | 5.89 | coincides with local:5^1 |
| (17,-) | 62031298 | low, monomial, orbit | 0.148 | 10.39 | **hunt 6, magnitude** (relabeled; was "coincides with monomial:-2^0\*3^0") |
| (22,-) | 1 | low, monomial, orbit | 0.109 | 12.52 | **hunt 6, magnitude** (relabeled; was "coincides with monomial:+2^0\*3^0") |
| (29,-) | 1 | low, monomial, orbit | 0.100 | 7.22 | **hunt 6, magnitude** (relabeled; was "coincides with monomial:+2^0\*3^0") |
| (41,-) | 1 | low, monomial, orbit | 0.083 | 6.03 | **hunt 6, magnitude** (relabeled; was "coincides with monomial:+2^0\*3^0") |

Note `517134 = |q|-1` at `(12,+)` and `5077564 = |q|-1` at `(17,+)`:
both are the conjugate of `xi=1` (`|phi(-1)|=|phi(1)|` for a real-valued
histogram), i.e. the *same* magnitude-1 signal the coordinator's review
names, reached via the `monomial` class's own reporting convention
rather than the `low` class's.

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
   (`classify_xi`): seven of the thirteen candidates *classify* as a
   local or monomial character outright: one, `xi=4062052` at `(17,+)`
   (local:5^1), is a genuine cause — the `12.6.1.6` mechanism, no
   further hunt needed. The other six — `xi=62031298` at `(17,-)`,
   `xi=1` at each of `(22,-),(29,-),(41,-)`, and the two split
   `xi=|q|-1` entries at `(12,+),(17,+)` — are all `monomial:+-2^0*3^0`.
   **Revised**: a monomial label at `a=b=0` is true of `xi=+-1` by
   definition and is a classification, not a cause on its own — the
   coordinator's review caught this. These six are dissolved instead
   by **hunt 6 (magnitude)** below, which supplies the actual
   mechanism; hunt 2's classification is what correctly flagged them
   as needing that separate hunt rather than hunt 1's small-entry
   restriction.
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
   candidates (`(22,-),(29,-),(41,-)`, all `xi=+-1`), an independent
   re-sample at a fresh seed reproduces a comparable `|phi|` (e.g.
   `(41,-)`: 0.088 vs the original 0.083) — consistent with a real,
   reproducible effect rather than a one-off sampling fluke (which
   hunt 6 below then identifies as magnitude, not arithmetic).
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
hunt 1, hunt 2 alone (one candidate), hunt 6 (six candidates, below),
or a combination, with hunts 3-5 as independent confirmation where
applicable.

## Hunt 6 (magnitude) — coordinator review, 2026-09-08

A label is a classification, not a cause: "coincides with a monomial
`2^0*3^0` character" is trivially true of `xi=+-1` at *every* cell (it
is the definition of the `a=b=0` monomial) and says nothing about why
`|phi(1)|` is large. The coordinator's independent check with fresh
code identifies the actual mechanism: `R_0`'s magnitude, not its
residue's arithmetic. `R_0` is always positive (12.6.1's Proposition);
write `R_0 = w\cdot|q| + r` with `w = R_0 // |q|` the number of times
the numerator "wraps" the modulus and `r = R_0 mod |q|` the residue.
At a good near-miss (`2^K` close to `3^n`, i.e. `2^gamma = 2^K/|q|`
close to `1`), `w` is small — the profile lands within the first few
multiples of `|q|` — and the *distribution of `w`* (a decaying profile
over those first few multiples, the size condition's own shadow,
12.6.1.3) forces `R_0/|q|`'s fractional part to be non-uniform too,
because a profile's exact position within its wrap is correlated with
which wrap it is in. This has **zero cross-prime content**: it is a
statement about `R_0`'s size, not about any prime dividing `|q|`.

**Table (a): `2^gamma`, wrap share, `|phi(1)|` and its floor, all
fourteen cells** (own fresh code; `|phi(1)|`'s floor here is the
single-frequency Rayleigh floor `1/sqrt(N)`, not the multi-frequency
class floor `sqrt(ln(m)/N)` used elsewhere in this file — the right
comparison for one named frequency, not a multiple-comparison-corrected
class maximum):

| n | shore | 2^gamma=2^K/\|q\| | share(wraps<=3) | \|phi(1)\| | floor=1/sqrt(N) | ratio |
|---|---|---|---|---|---|---|
| 5 | + | 19.69 | 0.400 | 0.3606 | 0.2582 | 1.40 |
| 5 | - | 1.11 | 1.000 | 0.6821 | 0.4472 | 1.53 |
| 7 | + | 2.15 | 0.967 | 0.1112 | 0.0690 | 1.61 |
| 7 | - | 14.73 | 0.393 | 0.1061 | 0.1091 | 0.97 |
| 12 | + | 2.03 | 0.815 | 0.1055 | 0.0056 | 18.83 |
| 12 | - | 73.30 | 0.093 | 0.0040 | 0.0090 | 0.45 |
| 17 | + | 26.43 | 0.152 | 0.0132 | 0.0007 | 18.91 |
| 17 | - | 1.08 | 0.751 | 0.1453 | 0.0012 | 124.61 |
| 22 | + | 11.54 | 0.214 | 0.0237 | 0.0010 | 23.70 |
| 22 | - | 1.21 | 0.625 | 0.1111 | 0.0010 | 111.10 |
| 29 | + | 40.48 | 0.086 | 0.0107 | 0.0010 | 10.74 |
| 29 | - | 1.05 | 0.553 | 0.0994 | 0.0010 | 99.40 |
| 41 | + | 87.74 | 0.044 | 0.0043 | 0.0010 | 4.32 |
| 41 | - | 1.02 | 0.448 | 0.0772 | 0.0010 | 77.17 |

Four of these fourteen rows reproduce the coordinator's independently-
computed numbers essentially exactly: `(12,-)`: `2^gamma=73.3` (theirs)
vs `73.30` (ours), share `9%` vs `9.3%`, `|phi(1)|=0.0040` vs `0.0040`,
floor `0.0090` vs `0.0090`; `(17,+)`: `26.4`/`26.43`, `15%`/`15.2%`,
`0.0132`/`0.0132`, `0.0007`/`0.0007`; `(12,+)`: `2.03`/`2.03`,
`82%`/`81.5%`, `0.1055`/`0.1055`, `0.0056`/`0.0056`; `(17,-)`:
`1.08`/`1.08`, `75%`/`75.1%`, `0.1453`/`0.1453`, `0.0012`/`0.0012` —
the small differences are rounding on the "share" percentage only. The
monotone relation the coordinator names is cleanest in **share**, which
is `N`-independent: small `2^gamma` (near-misses:
`(5,-),(7,+),(12,+),(17,-),(22,-),(29,-),(41,-)`, `2^gamma` in
`[1.0,2.2]`) pairs with a high wrap share (`45%-100%`); large `2^gamma`
(`(12,-),(29,+),(41,+)`, `2^gamma` in `[40,88]`) pairs with a low wrap
share (`4%-9%`); `(5,+),(7,-),(22,+)` sit at intermediate `gamma`
(`11.5-19.7`) and intermediate share (`21%-40%`). The **ratio** column
tracks the same direction but is not cleanly monotone across cells by
itself, because the floor `1/sqrt(N)` also varies enormously with `N`
(exact cells range `N=5` to `2,042,975`; every sampled cell has
`N=10^6`): `(12,-)` (low share `9.3%`, but `N=10^6`) sits at `0.45x`,
*below* its floor — the cleanest single-cell confirmation that a large
`N` alone does not manufacture a ratio; `(29,+),(41,+)` (also low share,
`8.6%`/`4.4%`, also `N=10^6`) still show modest elevated ratios
(`10.74x`,`4.32x`) despite the low share, because at `N=10^6` the floor
itself is tiny (`0.0010`) and even a weak residual size-law imprint
registers as several floor-widths. The ratio column is therefore a
mix of the magnitude effect's strength (tracked cleanly by share) and
sample size; the clean, single-cell, `N`-independent test for "is this
magnitude" is the synthetic control in (b), not a cross-cell ratio
comparison.

**Synthetic control (b): keep the size law, discard the arithmetic.**
For each profile, bin `x = R_0/|q|` at width `0.1` wraps (and,
separately, at width `1.0` wraps); draw a synthetic `x'` uniformly
within the *same* bin (own fresh code, `numpy.random.RandomState`,
seeded); compute the synthetic `|phi(1)|` from `frac(x')` and compare
to the measured value:

| n | shore | synth(0.1 wrap) | synth(1.0 wrap) | \|diff\| @ 0.1 | reproduced? |
|---|---|---|---|---|---|
| 5 | + | 0.4348 | 0.1647 | 0.0742 | YES |
| 5 | - | 0.6401 | 0.6492 | 0.0420 | YES |
| 7 | + | 0.1183 | 0.0422 | 0.0071 | YES |
| 7 | - | 0.1249 | 0.0318 | 0.0187 | YES |
| 12 | + | 0.1048 | 0.0112 | 0.0007 | YES |
| 12 | - | 0.0025 | 0.0048 | 0.0015 | YES |
| 17 | + | 0.0134 | 0.0003 | 0.0001 | YES |
| 17 | - | 0.1497 | 0.0011 | 0.0043 | YES |
| 22 | + | 0.0238 | 0.0015 | 0.0001 | YES |
| 22 | - | 0.1146 | 0.0015 | 0.0035 | YES |
| 29 | + | 0.0107 | 0.0010 | 0.0000 | YES |
| 29 | - | 0.1028 | 0.0010 | 0.0034 | YES |
| 41 | + | 0.0046 | 0.0013 | 0.0003 | YES |
| 41 | - | 0.0803 | 0.0013 | 0.0031 | YES |

**All fourteen cells reproduce at 0.1-wrap resolution** ("reproduced"
means the 0.1-wrap synthetic value sits within 30% of the measured
value, or within one floor-width, whichever is larger — every one of
the fourteen diffs above is well inside that band, several within
`0.001` in absolute terms). The 1.0-wrap (whole-wrap) control degrades
sharply at every near-miss cell (`(12,+)`: `0.0112` vs measured
`0.1055`; `(17,-)`: `0.0011` vs `0.1453`; `(22,-)`: `0.0015` vs
`0.1111`; `(29,-)`: `0.0010` vs `0.0994`; `(41,-)`: `0.0013` vs
`0.0772`) — collapsing to near the population floor, because
discarding *which fraction of a wrap* a profile sits in (not just
which wrap) throws away exactly the information the harmonic needs.
Read together, the two resolutions localize the effect precisely:
**the harmonic lives at the scale of `|q|` (fractions of a wrap), not
finer** — magnitude, not arithmetic. **Zero of the fourteen cells fail
to reproduce**; none is a surviving candidate.

**(c) Relabeling.** The four straightforward `xi=+-1` dissolutions
(`(17,-),(22,-),(29,-),(41,-)`) and the two split-out ones
(`(12,+),(17,+)`) are relabeled to hunt 6 (magnitude) in the table
above, with the old "coincides with a monomial `2^0*3^0` character"
line kept as the record of how it looked before this review (per the
brief's own rule for a dissolved ghost: recorded with its cause, not
deleted) — visible in the script's own printed verdict for each ("OLD
LABEL ... RELABELED ...") and in `experiments/modq_spectrum_output.txt`.

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
**Note on the harmonic:** by construction, this table excludes `xi=+-1`
outright (`a=b=0` is always `monomial`), so hunt 6's magnitude effect
never appears here — it lives entirely in the `monomial`/`low`/`orbit`
classes this table's own "off-monomial" filter is designed to set
aside, not in the `"other"`-typed residue captured by table (a). The
two are complementary, not in tension: table (a) asks whether anything
*besides* the known local/monomial/harmonic structure survives (no),
and hunt 6 answers what the harmonic itself is (magnitude, not
cross-prime arithmetic).

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

**(i) Flat beyond the first harmonic at small-gamma cells, whose cause
is magnitude.** Every off-local, off-monomial class candidate across
all fourteen cells — thirteen candidate groups in total — dissolves
under the ghost-hunt discipline: seven by coinciding with a known
local/monomial character (one genuinely, `local:5^1`; six of those
seven relabeled to hunt 6, magnitude, below), six by the small-entry
pushforward (`briefs/prime-local-probe-findings.md`'s own dissolved-
ghost mechanism), cross-confirmed by rotation dedup, resampling, or
high-precision recomputation as applicable. **Every one of the
fourteen cells' `xi=+-1` harmonic is explained by hunt 6**: the
residue inherits the shape of `R_0`'s own size law, `2^gamma=2^K/|q|`
(the near-miss quality itself, 12.6.1.3) — small `2^gamma` (a good
near-miss) forces most profiles into the first few multiples of `|q|`,
and a synthetic control that keeps only the coarse size (which
`0.1`-wrap bin a profile falls in) and discards everything finer
reproduces the measured `|phi(1)|` at all fourteen cells, degrading
sharply at the coarser `1.0`-wrap resolution — localizing the effect
to the scale of `|q|`, with zero cross-prime content. The 5-line
shrinks with block count `p` at every FFT-eligible cell where `5 | q`
(matches 12.6.1.6; no such cell has `7 | q`, left open below). Every
cross-prime joint law sits at or within sampling noise of its
permutation-shuffled control at every one of 23 tested prime-power
pairs across all fourteen cells; the theoretical null formula is
reliable only when `N >> ell1^a ell2^b` and the permutation control is
the operative check otherwise, stated explicitly at every pair in that
regime. **Beyond the one harmonic**, the joint law is as flat as the
marginals the prime-local probe already found — no cross-prime leak,
no local pinning, at this scale.

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
  sub-sample of `N_phi = 40,000` (`100,000` for `(22,+),(22,-)`)
  drawn from the full `N=10^6` population/full enumeration, rather
  than the full population — direct per-frequency summation at
  `N=10^6` was benchmarked at `~0.14s/frequency`, and these seven
  cells' selected-frequency classes total roughly `10,000-17,000`
  frequencies each, which would have cost `~25-40` minutes *per cell*
  at full `N`; the zero-bin, joint-law and hunt-6 (magnitude)
  statistics all use the full population throughout, never the
  sub-sample. Stated per the brief's runtime-cap allowance; these same
  `N_phi` values are now the fixed, reproducible choice baked into the
  `all` phase (`LARGE_CELL_PHI_N` in the script) so the single-command
  run stays under the 45-minute cap (**1522.3s = 25.4 minutes**
  measured) — kept rather than tightened, per the coordinator's
  explicit allowance. A rerun at larger `N_phi` would tighten these
  seven cells' floors but is not expected to change the verdict, since
  every candidate there already dissolved by hunt 6 (magnitude, using
  the FULL population) or hunt 1 (small-entry pushforward) rather than
  by a floor-dependent argument on the sub-sample itself.
- **Hunt 6's resolution is `0.1` and `1.0` wraps only**, per the
  coordinator's specification — not a finer grid. All fourteen cells
  reproduce cleanly at `0.1` wraps, so a finer grid was not needed to
  reach a verdict here, but it was not tried, and a genuinely finer-
  than-`0.1`-wrap structure (if any existed) would not have been
  caught by this test.
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
