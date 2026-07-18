# Findings: merle-round5-check (2026-07-19)

Answers `briefs/merle-round5-check-brief.md` items 1-6: the Catalan lock
(anchored loops, the `|q| = 1` free stock), the Benford side-asymmetry,
the exhaustive `k <= 10` map, the folklore adjudication with verified
citations, and his commit `a67970f`.

Code: `experiments/merle_round5_check.py`, fresh per AGENTS.md — imports
nothing from any committed project script; exact integer arithmetic at
every pass/fail decision; high-precision decimal only in section 2's
labeled density displays and threshold guards. Deterministic, no RNG.
Full run (`python experiments/merle_round5_check.py all`): **211,047
checks, 0 failures** (section 1: 336; section 2: 209,004; section 3:
1,707; ~3.5 minutes, dominated by the exact `k <= 10^5` big-integer
pass). Date: 2026-07-19 (thread date; the environment clock runs a day
behind the thread — git order authoritative, per the brief).

Frame, pinned once: the T-map on nonzero odd integers, `T(x) =
(3x+1)/2^{v2(3x+1)}`. A `k`-cycle with exponent word `s = (s_0..s_{k-1})`
and `m = sum(s)` satisfies `x_r * q = R_r`, `q = 2^m - 3^k`, `R_r =
sum_i 3^{k-1-i} 2^{S_i}` on the rotated word. This is his `(k, m)`
labelling; under the block dictionary it is `cycles.md` 12.6.1's `(n, K)`,
and the transport recurrence / gcd rotation-invariance (Remark 12.6.1.1
= reverse.md 14.15.9.2, his L-A1) applies verbatim.

## Summary for the reply (verdicts, liftable; register flat)

1. **The anchor table is exact.** All four cycles, from fresh orbits:
   `+1:(1,2,+1)`, `−1:(1,1,−1)`, `−5:(2,3,−1)` on 8-vs-9,
   `−17:(7,11,−139)`; cycle equation at every rotation. His −17 numbers:
   `gcd(q, R_0) = 139`, prime, rotation-invariant, word primitive — the
   lottery-win reading is arithmetically accurate.
2. **The lock is real and free, and it is 14th-century.**
   `|2^a − 3^b| = 1` has exactly the three solutions 2-3, 4-3, 9-8
   (exhaustive to `a <= 200, b <= 130`; elementary mod-8 + factoring
   proof written out). At `|q| = 1` every composition at the anchor
   `(k, m)` yields a genuine integer cycle — verified exhaustively at
   all three anchors. **Cite Gersonides 1342/43, not Mihailescu**: the
   2-vs-3 case is elementary and ancient; Catalan is overkill and
   invites the referee reaction he fears. His ticket split (one north,
   two south) is exact.
3. **The envelope and the Benford fraction are right, with one
   refinement.** `q+ + q− = 2^{floor(kL)}` proved (one line) and exact
   to `k = 3000`. The side-asymmetry is confirmed: negative side wins
   iff `frac(kL) < log2(3/2)`; exact to `k = 10^5` (58,496/99,999 =
   0.5849658), high-precision to `k = 10^7` (0.5849626 vs 0.5849625007),
   every decision guarded; closest call `k = 190,538` at `9.3·10^{−8}`.
   It is the base-2 Benford second-digit law of `3^k` — "exact Benford"
   is exactly right — and his machine's 50/50 first draft was the
   correct answer to the *ratio* question; the additive one is the
   cycle-relevant one (divisibility lives on `q` as an integer). The
   refinement: **`k = 1` is an exact tie** (`q+ = q− = 1`; the only tie
   at any `k`), so the law reads "for `k >= 2`".
4. **His `k <= 10` map replicates exactly.** 250,952 profiles
   (244,994 +, 5,958 −), bounds re-derived, zero silent skips, one
   divisibility test per profile via L-A1: 37 divisible, all 37 genuine
   cycles, all realizing known houses — **cycles exactly `{+1}` and
   `{−1, −5, −17}`**. His false survivor is the `B^5` trivial word
   (`q_P = 781`, `gcd = 781 = |q_P|`, `q_red(base) = 1`), flagged a
   priori by the repeated-word law, which was verified on all 384
   repeated words in the sweep. His 256/243 sweep is the `(5,8)`,
   `q = 13` slice — 35 profiles, none divisible — subsumed.
5. **Folklore verdicts.** (a) The Catalan-lock reading: folklore with
   citable homes (Steiner 1977 through Simons–de Weger 2005; Lagarias
   surveys; Gersonides for the lock itself — all verified live, item 4);
   his instinct not to re-announce is right; the *packaging* (spent
   finite stock ⇒ every future candidate needs the finite-place ×
   archimedean coupling) appears to be his. (b) The Benford fraction:
   no prior statement found in the Collatz/cycle context (searched:
   arXiv, OEIS, the Lagarias bibliographies, the Benford-Collatz
   papers); nearest neighbors are Kontorovich–Miller 2005 /
   Lagarias–Soundararajan 2006 (Benford for *iterates*) and the
   Sturmian gap density (same constant, different event). Honest grade:
   "not found stated", a legitimate small brick with neighbors cited.
6. **His commit is real and does what the letter says.** `a67970f` in
   `one-obstruction-three-faces-lean`, 2026-07-18: REQ-MATH-010/011 as
   described (item 5), self-catch disclosed in-code. One cosmetic flag:
   the act-C header comment still says ~50/50 while the code below
   prints the corrected 58.5% — worth one friendly line.
7. **Stopping rules.** The spent-stock claim excludes nothing (a
   sufficient mechanism exhausted, not an obstruction); the `k <= 10`
   map was replicated once, bounded, and is closed; the cycle front
   stays parked.

## Item 1: the anchored loops and the `|q| = 1` lock — VERIFIED

**(a) The anchor table, from fresh forward iteration.** All four known
cycles of `3x+1` on the nonzero odd integers, computed from the orbit
itself, match his table exactly:

| cycle | elements | k | m | q = 2^m − 3^k | near-miss |
|---|---|---|---|---|---|
| +1 | {1} | 1 | 2 | **+1** | 4-3 |
| −1 | {−1} | 1 | 1 | **−1** | 2-3 |
| −5 | {−5, −7} | 2 | 3 | **−1** | 8-vs-9 (his label) |
| −17 | {−17, −25, −37, −55, −41, −61, −91} | 7 | 11 | **−139** | 2^11 vs 3^7 |

Cycle equation `x_r q = R_r` checked at every rotation of all four
(s-words `(2)`, `(1)`, `(1,2)`, `(1,1,1,2,1,1,4)`).

**(b) `|2^a − 3^b| = 1` exhaustive, `1 <= a <= 200`, `1 <= b <= 130`:**
exactly `{(1,1), (2,1), (3,2)}` — the pairs 2-3, 4-3, 9-8, his "three in
all of history". The finiteness is **elementary, and ancient — Catalan/
Mihailescu is not needed for this case**. The two-part proof, written
out (machine-supported step by step in the script):

* `3^b + 1 = 2^a`: for `b >= 1`, `3^b ≡ 1 or 3 (mod 8)`, so `3^b + 1 ≡
  2 or 4 (mod 8)`, never `0`; hence `a <= 2`, and `a = 2` gives `b = 1`
  (4-3). Solutions: `(2,1)` only.
* `3^b − 1 = 2^a`: if `b` is odd, `3^b − 1 ≡ 2 (mod 8)`, so `a = 1`,
  `b = 1` (2-3). If `b = 2c` is even, `3^b − 1 = (3^c−1)(3^c+1)` — two
  powers of 2 differing by 2, hence 2 and 4, forcing `c = 1`, i.e.
  `b = 2`, `a = 3` (9-8). Solutions: `(1,1)` and `(3,2)`.

This is Gersonides (Levi ben Gerson), *De numeris harmonicis*, 1342/43,
written for Philippe de Vitry — and his method **was** the mod-8
argument (citation verified, item 4). Mihailescu 2004 settles the
general Catalan equation; citing it for the 2-vs-3 case is overkill and
invites exactly the referee reaction he wants to avoid.

**(c) The "free lock" mechanism, stated exactly and verified
exhaustively.** "Free" means: at `|q| = 1` the divisibility condition
`q | R_r` — the only arithmetic obstruction in the cycle equation — is
satisfied by every profile, so **every** composition `s` of `m` into `k`
positive parts yields an integer cycle candidate `x_r = R_r/q` at every
rotation. What is *not* automatic and was checked exhaustively at all
three anchors: integrality at every rotation, oddness, nonvanishing,
constant sign, and forward closure with `v2(3x_i+1) = s_i` exactly. At
`(k,m) = (1,1)` (1 composition), `(1,2)` (1), `(2,3)` (2): **every
composition yields a genuine cycle** — `{−1}`, `{+1}`, and both
rotations of `{−5, −7}` respectively. The lock is genuinely free: no
composition at any of the three anchors fails any bookkeeping condition.

**(d) The ticket mapping and the lottery win.** Near-miss `(a, b)` maps
to cycle shape `(k, m) = (b, a)`: 4-3 → `(1,2)`, `q = +1`, the house
`+1` (north — the only positive ticket); 2-3 → `(1,1)`, `q = −1`, house
`−1`; 9-8 → `(2,3)`, `q = −1`, house `−5` (two south tickets). His
alternation count (one north, two south) is exact. `−17` is the single
known cycle with `|q| > 1`: `q = −139`, `R_0 = 2363 = 17·139`,
`gcd(q, R_0) = 139`, `139` prime, gcd confirmed rotation-invariant at
all 7 rotations, s-word `(1,1,1,2,1,1,4)` primitive. The "lottery win"
reading is arithmetically accurate: `−17` is not a `|q| = 1` freebie but
a nontrivial divisibility event (`139 | R_0` with `139` prime and the
word primitive).

**Logical status, stated precisely (stopping-rule compliance).** The
"spent stock" claim excludes nothing: it says one *sufficient* mechanism
(`|q| = 1`, divisibility free) is exhausted — three tickets, all dealt,
never another by Gersonides-level arithmetic — so every further
candidate must satisfy `q | R_0` nontrivially, which is exactly the
parked front's condition. It is a reframing brick for the note, not an
obstruction, and no extension of it was attempted here.

## Item 2: the envelope and the Benford side-asymmetry — VERIFIED, with one refinement (the k = 1 tie)

**(a) The envelope identity, proved and verified.** Since `kL` (`L =
log2 3`) is never an integer (`2^m = 3^k` is impossible), `ceil(kL) =
floor(kL) + 1`, so

    q+ + q− = (2^{floor(kL)+1} − 3^k) + (3^k − 2^{floor(kL)}) = 2^{floor(kL)}.

Verified exactly (big integers) for `k = 1..3000`, with `q+, q− > 0`
throughout. His identity is exact as stated.

**(b) The two distance notions, pinned before measuring.**

* **Absolute** (integer) distance: the negative side wins iff `q− < q+`
  iff `2·3^k < 3·2^{floor(kL)}` iff `2^{frac(kL)} < 3/2` iff `frac(kL) <
  log2(3/2)`. Density `log2(3/2) = 0.5849625007...` by Weyl
  equidistribution (`L` irrational).
* **Ratio** (multiplicative) distance: the lower tower is nearer iff
  `2^{frac} < 2^{1−frac}` iff `frac(kL) < 1/2`. Density `1/2`.

**The k = 1 tie — a refinement his letter (and the pre-check) did not
flag.** `2·3^k = 3·2^{floor(kL)}` iff `3^{k−1} = 2^{floor(kL)−1}` iff
`k = 1`. So `k = 1` is an **exact tie** — `q+ = q− = 1`; the near-misses
4-3 and 2-3 sit at equal distance 1 from `3^1` — and it is the *only*
tie at any `k`. "Which side gets the better near-miss" is undefined at
`k = 1` and decided at every `k >= 2`; all counts below are over
`k >= 2` (a measure-zero correction to the density, none to the law).

**Exact verification (big integers), `2 <= k <= 10^5`:** negative side
wins 5,849/9,999 (`0.5849585`) at `k <= 10^4` and **58,496/99,999
(`0.5849658`)** at `k <= 10^5`. No decision by approximation: every
comparison is `2·3^k` vs `3·2^{floor(kL)}` in exact arithmetic, with
`floor(kL)` read off the bit length of `3^k`.

**High-precision pass to `k = 10^7`** (200-bit fractional parts;
labeled measurement, guarded): every decision is safe by a margin
guard — the minimum integer margin over all `k >= 2` is `~1.5·10^53`
ulp at `2^{−200}`, against an accumulated-error bound of `10^7 + 1`
ulp — and the pass agrees with the exact pass at every decade where
both exist (counts equal at `10^5`). Per-decade fractions (absolute
column over `k >= 2`):

| k up to | absolute: frac < log2(3/2) | ratio: frac < 1/2 |
|---|---|---|
| 10 | 0.5555556 | 0.4000000 |
| 100 | 0.5858586 | 0.5000000 |
| 1,000 | 0.5845846 | 0.5000000 |
| 10,000 | 0.5849585 | 0.5004000 |
| 100,000 | 0.5849658 | 0.5000300 |
| 1,000,000 | 0.5849626 | 0.4999980 |
| 10,000,000 | **0.5849626** | **0.5000002** |

`log2(3/2) = 0.5849625007`; the empirical fraction at `10^7` differs
from it by `~1.3·10^{−7}`. Convergence quality: measurement, labeled —
no discrepancy bound is proved or claimed.

**The closest call in the threshold guard:** `k = 190,538`, where
`|frac(kL) − log2(3/2)| = 9.306·10^{−8}` (`1.495·10^{53}` ulp at
`2^{−200}`) — the side (negative wins) confirmed by exact big-integer
comparison of `2·3^{190538}` vs `3·2^{302051}`. Structure note
(measurement): `190,537 = 190,538 − 1` is a continued-fraction
convergent denominator of `L` — the largest below `10^7` (next:
`10,590,737`) — exactly the expected mechanism, since `|frac(kL) −
frac(L)|` = the distance of `(k−1)L` to the nearest integer when no
wraparound occurs; the CF denominators re-derived in-session
(`1, 1, 2, 5, 12, 41, 53, 306, 665, 15601, 31867, 79335, 111202,
190537, ...`, matching 12.8.6.1's chain where they overlap).

**(c) Identification and the self-catch, adjudicated in his terms.**
The statement is the base-2 Benford **second-digit** law: the second
binary digit of `3^k` is 0 iff `3^k < 1.5·2^{floor(kL)}` — verified in
the script to be *the same event* as "negative side wins", per-`k`,
exactly, over the whole exact range — so `P(second binary digit of 3^k
= 0) = log2(3/2)`. His "exact Benford" is exactly right. And his
machine's 50/50 first draft was the correct answer to the **ratio**
question: both numbers are right answers to different questions. The
additive one is the cycle-relevant one because `q+` and `|q−|` are
compared as integers — the divisibility condition `q | R_0` lives on
`q` itself, not on `q/3^k`. (His artifact discloses the self-catch in
the code itself; see item 5 — including one stale header comment from
the first draft, worth a friendly line.)

## Item 3: the exhaustive `k <= 10` map — CONFIRMED EXACTLY

**The m-bounds, re-derived from the per-step bounds.** Around a
`k`-cycle, `prod_i (3x_i + 1)/x_i = 2^m` exactly. Positive sector
(`x >= 1` odd): `(3x+1)/x = 3 + 1/x ∈ (3, 4]`, so `3^k < 2^m <= 4^k`,
i.e. `kL < m <= 2k` (`m = 2k` iff all `x_i = 1`). Negative sector
(`x <= −1` odd): `3 + 1/x ∈ [2, 3)`, so `2^k <= 2^m < 3^k`, i.e.
`k <= m < kL` (`m = k` iff all `x_i = −1`). Integer ranges (`kL` never
integral): positive `ceil(kL) <= m <= 2k`, negative `k <= m <=
floor(kL)`; the sign of `q` matches the sector automatically.

**(a) The enumeration.** All compositions of every feasible `m`, both
sectors, `k = 1..10`; divisibility `q | R_0` tested **once per
profile**, citing rotation-invariance (12.6.1.1 / 14.15.9.2 — his "one
rotation per profile via L-A1"); every divisible profile fully
reconstructed (all `k` rotations computed exactly; integrality at each
rotation doubles as an instance check of the invariance; oddness,
nonvanishing, constant sign, `v2`-exact forward closure). Per-`(k,
sector)` counts, zero silent skips (composition-count identity `sum_m
C(m−1, k−1)` checked per cell):

| k | sector | m-range | profiles | divisible | cycle-realizing |
|---|---|---|---|---|---|
| 1 | + | [2, 2] | 1 | 1 | 1 |
| 1 | − | [1, 1] | 1 | 1 | 1 |
| 2 | + | [4, 4] | 3 | 1 | 1 |
| 2 | − | [2, 3] | 3 | 3 | 3 |
| 3 | + | [5, 6] | 16 | 1 | 1 |
| 3 | − | [3, 4] | 4 | 1 | 1 |
| 4 | + | [7, 8] | 55 | 1 | 1 |
| 4 | − | [4, 6] | 15 | 3 | 3 |
| 5 | + | [8, 10] | 231 | 1 | 1 |
| 5 | − | [5, 7] | 21 | 1 | 1 |
| 6 | + | [10, 12] | 840 | 1 | 1 |
| 6 | − | [6, 9] | 84 | 3 | 3 |
| 7 | + | [12, 14] | 3,102 | 1 | 1 |
| 7 | − | [7, 11] | 330 | 8 | 8 |
| 8 | + | [13, 16] | 12,375 | 1 | 1 |
| 8 | − | [8, 12] | 495 | 3 | 3 |
| 9 | + | [15, 18] | 46,618 | 1 | 1 |
| 9 | − | [9, 14] | 2,002 | 1 | 1 |
| 10 | + | [16, 20] | 181,753 | 1 | 1 |
| 10 | − | [10, 15] | 3,003 | 3 | 3 |

**Grand total: 250,952 profiles (244,994 positive, 5,958 negative); 37
divisible; 37 cycle-realizing; 0 divisible non-cycles.** Every
divisible profile reconstructs to a genuine cycle, and every one
realizes a **known** cycle: positive sector `{+1}` only (the all-2s
word `B^k` of `(2)` at each `k`); negative sector `{−1}` (all-1s,
each `k`), `{−5}` (the two rotations of `(1,2)` repeated, even `k`),
and `{−17}` (the 7 rotations of the primitive word at `k = 7`, `m =
11`). **His claim — cycles exactly `{+1}` and `{−1, −5, −17}` for
`k <= 10` — is confirmed exactly.** No new cycle, no unexplained
survivor.

**(b) The `k = 5` all-2s word (his "false survivor": the element 1
repeated five times).** Confirmed: it is `B^5` of the trivial-cycle
word `(2)`; `q_P = 2^{10} − 3^5 = 781 = 11·71`; base `q_B = 1`, `R_0(B)
= 1`, so `q_red(base) = 1`; `gcd(q_P, R_0) = 781 = |q_P|` — it **is**
divisible, and it realizes the trivial cycle traversed five times
(`y = 1`), not a new cycle. (In his artifact it "survives" the
divisibility filter and is then rejected by his primitivity check —
matching his letter's account; item 5.) What the repeated-word law
sweeps, stated precisely: for every `P = B^j` (`j >= 2`), `gcd(q_P,
R_0(P)) = |q_P|/q_red(B)` with `q_red(B) = |q_B|/gcd(q_B, R_0(B))` —
so a repeated word is divisible **iff its base is**, and then it
realizes the base's cycle traversed `j` times, never a new cycle:
every `B^j` is decided *before any enumeration*. Verified across the
enumeration: **384 repeated words occur in the `k <= 10` sweep**
(every non-primitive profile), and on every one the geometric identity
`R_0(P)·q_B = R_0(B)·q_P`, the exact gcd law, and `gcd > 1` all hold
(1,536 checks inside the section total). Consistent with the closed
law of `briefs/prime-local-probe-findings.md` (there verified on 30
recorded + 60 random repeated words; sign-blind, forced `> 1` for
`j >= 2`).

**(c) His 256/243 sweep.** Confirmed as the `(k, m) = (5, 8)`, `q =
2^8 − 3^5 = 13` slice of (a): 35 profiles (`C(7,4)`), 0 divisible, no
cycle — subsumed by the full map. (His own script sweeps `k = 5`, `K =
8..12` — 771 profiles, a superset of the proven positive-sector range
`m <= 2k = 10`; the extra `m = 11, 12` rows are outside the cycle
bounds and harmless. Item 5.)

**(d) L-A2.** His proposal — elevate the repeated-word gcd law to
ledger entry L-A2 rather than a footnote — is recorded. The law is
verified (here on all 384 in-sweep repeated words; closed in review
with complete elementary cause in `briefs/prime-local-probe-findings.md`),
and it did real work in his `k = 5` sweep (it flags his one false
survivor a priori). Elevation is the author's decision (decision list,
item 6).

## Item 4: literature — the folklore adjudication, citations verified

Every citation below was verified against a live source this session
(WebSearch/WebFetch; title, venue, year as listed). Nothing is cited
from memory.

**(a) The Catalan lock: folklore, yes — with citable homes.** The
correspondence "known cycles ↔ good rational approximations of `log2 3`
/ small `|2^m − 3^k|`" is the standard engine of the cycle-bounds
literature; the anchor observation itself is not new, though we found
no prior statement of his *packaging* (below). Verified citations:

* R. P. Steiner, *A theorem on the Syracuse problem*, Proc. 7th
  Manitoba Conf. on Numerical Mathematics and Computing (1977),
  Utilitas Mathematica, Winnipeg, 553–559. (The 1-circuit theorem —
  cycle exclusion via the linear form in logarithms / continued-fraction
  structure of `log2 3`.)
* R. E. Crandall, *On the "3x+1" problem*, Math. Comp. 32 (1978),
  no. 144, 1281–1292.
* S. Eliahou, *The 3x+1 problem: new lower bounds on nontrivial cycle
  lengths*, Discrete Math. 118 (1993), 45–56 (DOI
  10.1016/0012-365X(93)90052-U; cycle length >= 17,087,915 from the
  convergents of `log2 3`).
* L. Halbeisen, N. Hungerbühler, *Optimal bounds for the length of
  rational Collatz cycles*, Acta Arith. 78 (1997), no. 3, 227–239 (the
  rational-cycle frame in which the negative/`3x−1` cycles live).
* J. L. Simons, *On the nonexistence of 2-cycles for the 3x+1 problem*,
  Math. Comp. 74 (2005), 1565–1572 (extends Steiner's method; uses
  convergents of `log2 3` explicitly).
* J. L. Simons, B. M. M. de Weger, *Theoretical and computational
  bounds for m-cycles of the 3n+1-problem*, Acta Arith. 117 (2005),
  no. 1, 51–70 (DOI 10.4064/aa117-1-3; no m-cycles for m <= 68).
* Surveyed in: J. C. Lagarias, *The 3x+1 problem and its
  generalizations*, Amer. Math. Monthly 92 (1985), 3–23; and the two
  Lagarias annotated bibliographies, arXiv:math/0309224 (1963–1999)
  and arXiv:math/0608208 (2000–2009).

The `|2^a − 3^b| = 1` finiteness: **Gersonides (Levi ben Gerson),
*De numeris harmonicis*, 1342/43**, commissioned by Philippe de Vitry —
proves the only pairs of harmonic numbers (`2^a 3^b`) differing by 1
are (1,2), (2,3), (3,4), (8,9), by the mod-8 argument (the same one
item 1(b) writes out; the treatise survives in Latin translation).
Modern accounts: S. Simonson, *The Mathematics of Levi ben Gershon,
the Ralbag* (live at u.cs.biu.ac.il/~tsaban/Pdf/MathofLevi.pdf);
P. Ribenboim, *Catalan's Conjecture*, Academic Press, 1994 (ISBN
0-12-587170-8, treats Gersonides' 1342 result). P. Mihailescu, *Primary
cyclotomic units and a proof of Catalan's conjecture*, J. Reine Angew.
Math. 572 (2004), 167–195 (DOI 10.1515/crll.2004.048; proof completed
2002) settles the general Catalan equation but **is not needed** for
the 2-vs-3 case.

**Verdict for the reply (his question (a)):** his instinct not to
re-announce is right. The *ingredients* are folklore-with-references —
the anchor correspondence is the standard cycle-bounds engine, and the
`|q| = 1` finiteness is 14th-century. What may genuinely be his is the
**packaging**: "the free stock is finite and spent (three tickets, one
north, two south, dealt by 1342-level arithmetic), so every remaining
candidate needs the finite-place x archimedean coupling" — a framing
brick that joins his arithmetic wall to the prime-local probe's
structureless verdict. Recommended citation posture for the note:
Gersonides for the lock (with Ribenboim as the modern account),
Mihailescu only as a remark that the general case is also closed;
Steiner/Simons–de Weger/Lagarias for the anchor correspondence.

**(b) The Benford fraction: no prior statement found in the
Collatz/cycle context.** Searched this session (arXiv via web, OEIS,
the Lagarias bibliographies' titles via web, the Benford-Collatz
literature, math blogs): no statement was found of the side-asymmetry —
`P(negative side gets the better near-miss in absolute distance) =
log2(3/2)`, equivalently the second-binary-digit law of `3^k`, read as
the sign-side asymmetry of the near-miss sequence. What **does** exist,
verified, and should be cited as neighbors:

* A. V. Kontorovich, S. J. Miller, *Benford's law, values of
  L-functions and the 3x+1 problem*, Acta Arith. 120 (2005), no. 3,
  269–297 (DOI 10.4064/aa120-3-4) — Benford behavior of `3x+1`
  **iterates** (forward orbits), not of the near-miss sequence.
* J. C. Lagarias, K. Soundararajan, *Benford's law for the 3x+1
  function*, J. London Math. Soc. 74 (2006), 289–303
  (arXiv:math/0509175) — same subject, discrepancy bounds for most
  starting values.
* The Weyl equidistribution of `{k log2 3}` is classical, and the
  base-2 Benford law for `3^k` (first-digit trivial, second-digit
  `log2(3/2)`) is a direct corollary — textbook-level, but we found no
  source *stating* the second-digit form for `3^k`, let alone tying it
  to cycle near-misses.
* Nearest classical neighbor (same constant, different event): the
  gap structure of powers of 2 between consecutive powers of 3 is
  Sturmian — OEIS A020914 (`1 + floor(k log2 3)` = binary length of
  `3^k`), A056576, A022921 (first differences) — where the density of
  "two powers of 2 in the gap" is `log2(3/2)` for the *gap* event
  `{kL} > 2 − L`, not his *side* event `{kL} < L − 1`. Same constant
  by symmetry of the uniform measure; different statement.

**Verdict (his question (b)):** the fraction is a two-line corollary of
Weyl-classical facts, so "new" in the strong sense is not claimable —
but *as a statement about the near-miss sequence in the cycle context*
we searched and found no prior occurrence; "not found stated, at
measured grade" is the honest phrasing. It is a legitimate small brick
for the note with the neighbors cited, and his self-catch (the 50/50
first draft was the right answer to the ratio question) belongs in it
under the protocol's visibility rule. One refinement from item 2 to
carry into any write-up: `k = 1` is an exact tie (the only one), so the
law reads "for `k >= 2`".

## Item 5: his artifacts — commit `a67970f` FOUND and read (GitHub API, read-only)

**Located:** `ericmerle3789/one-obstruction-three-faces-lean`, commit
`a67970f2971097b06b567bbd2566b01ce3a1a95b`, dated 2026-07-18T11:36:02Z,
message "Add sign-question scripts (REQ-MATH-010, 011)" (trailer:
Co-Authored-By: Claude Opus 4.8 — consistent with his disclosed A.R.E.S.
protocol). Files: `experiments/README.md` (his script index, updated),
`experiments/test_REQ-MATH-010_kangourous_cycles_reels.py`,
`experiments/test_REQ-MATH-011_pourquoi_le_signe.py`. Both scripts were
read via the API; **neither was run** (per the brief). French-language,
canary-checked per his README convention (exit 0 iff the exit criterion
passes).

**REQ-MATH-010 ("kangourous, cycles réels")** — four acts: (A) `2^a =
3^b` never (parity; a <= 300, b <= 190 swept), irrationality of
`log2 3` as corollary; (B) the four real cycles detected by iteration
and anchored: `x_0(2^K − 3^k) = R` exactly, his Steiner-form `R`
matching our `R_0`; (C) the 256/243 near-miss (`q = +13`): exhaustive
composition sweep at `k = 5`, `K ∈ {8..12}` — 771 profiles, one
rotation per profile via L-A1 — no cycle. Note: his `K` range is a
*superset* of the proven positive-sector bound (`m <= 2k = 10`); the
extra `K = 11, 12` rows are outside the cycle bounds (item 3's
derivation) and harmless. Our (5,8) slice — 35 profiles, 0 divisible —
sits inside his 771 and agrees. (D) the "proof canary" moral: any
simple speed/parity argument forbidding loops would forbid the four
real ones — proves too much.

**REQ-MATH-011 ("pourquoi le signe")** — five acts: (A) the mirror
conjugation `T_{3x+1}(−m) = −T_{3x−1}(m)` verified on 10^4 odds (the
negative world of `3x+1` is the positive world of `3x−1`); (B) the
envelope `q+ + q− = 2^{floor(kL)}` exact for `k = 1..50` (ours:
`1..3000`); (C) the side-asymmetry measured at `k <= 5000` with the
**self-catch disclosed in the code**: a comment block marked
"CORRECTION ARES (le premier jet de ce script annonçait '~50/50' — la
mesure a dit non)" states the corrected law `q− < q+ ⟺ {kL} <
log2(3/2) = 0.58496` and prints measured vs theory; (D) the three
Catalan free-locks `(1,1), (2,1), (3,2)` with the north/south ticket
split, Mihailescu 2002 cited for "never another"; (E) the exhaustive
`k <= 10` map, both sectors, bounds derived (`kL < K <= 2k` positive,
`k <= K < kL` negative — same derivation route as ours), divisibility
on one rotation via L-A1, candidates filtered by parity/nonzero then
checked against the real T-map with a **primitivity requirement**
(`len(seen) == k`) — expected map `{+1}` and `{−1, −5, −17}`, exit
criterion PASS.

Two flat observations for the reply:

1. **The stale header.** REQ-MATH-011's act-C *header comment* (line
   "C. EQUIDISTRIBUTION: le meilleur frôlement tombe ~50/50 de chaque
   côté" and act-B's "AUCUNE asymétrie structurelle") still carries the
   first draft's 50/50 reading, while the code below it computes and
   prints the corrected 58.5% with the ARES correction note. Cosmetic —
   the computation and the printed conclusion are right — but the
   header contradicts the output; worth one friendly line so his
   artifact matches his letter.
2. **His "false survivor" mechanism, confirmed in code.** His
   enumeration filters `n_0` even/zero *silently* and rejects
   non-primitive loops via `real_cycle_check` — so the `k = 5` all-ones
   (element) word survives divisibility and dies at the primitivity
   check, exactly as his letter describes. The repeated-word law (his
   L-A2 candidate) replaces that a-posteriori rejection with an a-priori
   sweep: `B^j` is divisible iff its base is, and never new (item 3(b)).
   His account is accurate; the law genuinely upgrades his filter.

His anchor table, envelope identity, ticket mapping, Benford fraction,
and `k <= 10` map — every claim his letter puts weight on — are
independently confirmed by items 1–3 with fresh code at larger ranges.

## Item 6: proposal lines (drafted, NOT applied) and the author-decision list

No wiki page is touched by this session. The following are candidates
only; application is the author's decision, per the round-3 pattern
(decisions first, then apply, then the reply).

**(i) Candidate `cycles.md` remark (suggest: Remark 12.6.1.2, under the
transport recurrence), record-only, front stays parked:**

> **Remark 12.6.1.2 (the near-miss anchors of the known cycles; the
> `|q| = 1` stock; the side-asymmetry).** In the odd-step frame
> (`k` odd steps, `m` halvings, `q = 2^m − 3^k`), the four known cycles
> of `3x+1` on the nonzero odd integers are each anchored to a
> near-miss of the two towers: `+1: (k,m,q) = (1,2,+1)` (4-3),
> `−1: (1,1,−1)` (2-3), `−5: (2,3,−1)` (8-vs-9), `−17: (7,11,−139)`.
> At `|q| = 1` divisibility is free: every composition of `m` into `k`
> parts yields an integer cycle (verified exhaustively at the three
> anchors), and `|2^a − 3^b| = 1` has exactly the solutions
> `(a,b) ∈ {(1,1),(2,1),(3,2)}` — elementary (mod 8 plus a two-line
> factoring), and ancient: Gersonides, *De numeris harmonicis*,
> 1342/43 (Mihailescu 2004 settles the general Catalan case but is not
> needed here). So the `|q| = 1` mechanism is a finite stock, spent;
> every further cycle must satisfy `q | R_0` nontrivially — exactly
> this front's parked condition; `−17` (`gcd(q, R_0) = 139`, prime,
> word primitive) is the one known nontrivial instance. Two exact side
> facts (verified to the stated ranges, `experiments/
> merle_round5_check.py`, 2026-07-19): the envelope `q_+ + q_− =
> 2^{⌊kL⌋}` (`L = log₂3`; `k = 1..3000`), and the side-asymmetry — the
> negative side holds the nearer tower in absolute distance iff
> `{kL} < log₂(3/2)`, density `log₂(3/2) ≈ 0.585` (Weyl; the base-2
> Benford second-digit law of `3^k`), exact to `k = 10^5`, measured to
> `k = 10^7` at `0.5849626`; `k = 1` is an exact tie (`q_+ = q_− = 1`),
> the only one. In ratio distance the split is 50/50 — both answers are
> right, to different questions; the additive one is the cycle-relevant
> one since divisibility lives on `q` as an integer. Exhaustive
> replication for `k ≤ 10`, both sectors (250,952 profiles, one
> rotation per profile via Remark 12.6.1.1): cycles exactly `{+1}` and
> `{−1, −5, −17}`. Joint with Eric Merle (correspondence 2026-07-19,
> his commit `a67970f`, scripts REQ-MATH-010/011; [credit phrasing per
> the author]). Excludes nothing: the spent stock is a sufficient
> mechanism exhausted, not an obstruction; the front stays parked.

**(ii) Candidate ledger lines (shared repo — NOT touched here; for the
author to place in LEDGER.md if adopted):**

> **L-A2 (the repeated-word gcd law; his proposal, round 5).** For
> every profile `P = B^j` (`j ≥ 2`): `gcd(q_P, R_0(P)) =
> |q_P|/q_red(B)`, `q_red(B) = |q_B|/gcd(q_B, R_0(B))` — forced `> 1`,
> sign-blind; a repeated word is divisible iff its base is, and then
> realizes the base's cycle traversed `j` times, never a new one.
> Closed with complete elementary cause (fixed-point invariance under
> repetition + the seam identity), `briefs/prime-local-probe-findings.md`
> (2026-07-18); re-verified on all 384 repeated words of the `k ≤ 10`
> map (round-5 check). Did real work in his `k = 5` sweep (swept the
> one false survivor a priori). Keys: [his scripts; our
> `experiments/prime_local_probe.py` + `merle_round5_check.py`].

And, our suggestion rather than his (decision 5 below):

> **L-A3 (candidate: the anchored loops, the spent `|q| = 1` stock,
> and the Benford side-asymmetry).** The four known cycles anchored to
> tower near-misses; the `|q| = 1` lock free and its stock exactly
> three (Gersonides 1342/43; Mihailescu not needed); `−17` the single
> nontrivial-divisibility instance; the envelope `q_+ + q_− = 2^{⌊kL⌋}`;
> the side-asymmetry `log₂(3/2)` (absolute) vs 50/50 (ratio), with the
> `k = 1` exact tie; the exhaustive `k ≤ 10` map = `{+1}` ∪
> `{−1, −5, −17}`. Keys: his `a67970f` (REQ-MATH-010/011) + our
> `experiments/merle_round5_check.py` (211,047 checks, 0 failures).
> Framing clause (the note's brick): the finite-pure mechanism is a
> spent finite stock, so every remaining candidate needs the
> finite-place × archimedean coupling — consistent with, and joined
> to, the prime-local structureless verdict.

**(iii) The author-decision list (nothing decided here):**

1. **L-A2 elevation** — his proposal: ledger entry, not a footnote.
   The law is verified and closed; elevation is a placement/credit
   call. (If yes: the L-A2 draft above; both sides hold keys.)
2. **The gateway-viz plan change** — his proposal: each side builds its
   own cycle-side gateway viz and cross-links ("let's each build one
   and cross-link"), vs our recorded round-4 plan (we build the
   cycle-side gateway). Accept, decline, or accept-with-scope; nothing
   was computed on this.
3. **Whether the Benford brick and the spent-stock framing enter the
   note**, and under what credit language. The evidence supports:
   ingredients folklore-with-references (both flags adjudicated, item
   4); the packaging his; the fraction "not found stated" in the
   cycle context; his self-catch included under the protocol's
   visibility rule (his (b) flag; the 50/50 draft was the right answer
   to the ratio question). The `k = 1` tie and the Gersonides-not-
   Mihailescu citation posture should ride along if the brick enters.
4. **Whether to mention the stale ~50/50 header** in his REQ-MATH-011
   (cosmetic; one friendly line; item 5).
5. **L-A3 (or equivalent) creation** for the anchored-loops/Benford
   material — suggested here, not his proposal; his artifacts + our
   key would both attach.

## Compliance

Verification, replication, and literature adjudication only. No cycle
search beyond the brief's bounded `k <= 10` replication (run once,
exact, closed); no larger `k`, no Baker/linear-forms development, no
new statistics campaigns beyond item 2's mandated measurement, no Lean
work, no edits to any wiki page or to the shared repo's PROTOCOL.md /
LEDGER.md (proposal lines live in this file only). GitHub API use was
read-only. Off-brief observations, logged and stopped: (i) the `k = 1`
exact tie (recorded in item 2; a refinement, not an anomaly); (ii) the
closest-call structure `k − 1 = 190,537` = the largest CF denominator
of `L` below `10^7` (measurement-support note, item 2); (iii) his
stale header comment (item 5). The script runs clean end-to-end from a
fresh checkout (`python experiments/merle_round5_check.py all`,
211,047 checks, 0 failures, ~3.5 min). The cycle front stays parked;
nothing here reopens it.
