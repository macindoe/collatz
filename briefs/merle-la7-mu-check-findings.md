# Findings: L-A7 μ-source check + replication (merle-la7-mu-check)

Delegated session, 2026-07-25. Brief: `briefs/merle-la7-mu-check-brief.md` (commit `34296e8`).
Branch `merle-la7-mu-check`, base commit `34296e8` (the brief commit; worktree cut from it directly).
Register: flat; discrepancies recorded, not disputed; every replication number below is from this
session's own code (`experiments/merle_la7_check.py`), not from his script, which was read for
operational definitions only and never run.

**No pushes anywhere; shared repo and Merle's repo cloned read-only into the scratchpad; web access
used for item 2 (μ-source literature) only.**

## 1. The entry, the artifact, and the operational definitions

**Clones (read-only).** Shared repo `github.com/macindoe/one-obstruction-three-faces`, HEAD
**`81431c7`** — exactly the expected commit ("Seed L-A7 draft: the torsion ruler …"). Merle's
repo `github.com/ericmerle3789/one-obstruction-three-faces-lean`, HEAD `97b57d7` (his stack has
moved past the L-A7 artifact: REQ-MATH-030..034 exist, out of this session's scope); the L-A7
artifact `experiments/test_REQ-MATH-029_regle_de_torsion.py` + `experiments/OUT_REQ-MATH-029.txt`
entered at his commit **`f550147`** and are byte-unchanged at his HEAD (single commit in their
`git log`).

**The ledger entry, verbatim (LEDGER.md at `81431c7`, entry L-A7 in full):**

> ## L-A7 — The torsion ruler: the lottery's total ticket mass is effectively finite, at every scale (Merle, correspondence 2026-07-24)
>
> **DRAFT — one key (Merle; theorem-grade modulo two published ingredients); Macindoe key invited.**
>
> The instrument fuses the two rulers this program already owns: the **(B) counting constant** `c_gen = 0.0793186` (crowd-side, finite places) and the **effective irrationality measure of `log₂3`** (exponent `μ = 5.125`, Salikhov as documented in the Merle v2 corpus §5 — *primary source to be re-checked before any publication*). The second is an **individual-grade** Diophantine statement — true for *every* `n`, no averaging — i.e. exactly the archimedean component of the "individual resolver" that NOTE §6's residual gap calls for, wired to the counting for the first time in this frame.
>
> **Statement (verified `n ≤ 2000`, canary-anchored):** for the best north cell at scale `n`, `R(n) = log₂(#words) − log₂ q ≤ −c_gen·n + (μ−1)·log₂ n + C₀`, with `C₀ = −5.77` exhibited (max at `n = 2`); the ingredient inequality has enormous slack (`min_n ε_n·n^{μ−1} ≈ 14.5`). Canaries: anchors `(5,8) → q = 13`, `(7,12) → q = 1909`; the `n ≤ 14` word-budgets reproduce the census exactly (`6.17` north / `3.41` south). **Consequence, effective and scale-free:** the tickets' total mass beyond `n = 600` is provably `< 5.2·10⁻⁴` (both shores; word units, which upper-bound necklace units), and everything below `n = 600` is exact finite computation. **The kiosk provably closes:** L-A6's tail is no longer "computed to `n = 200`" but bounded for all `n` by two published constants and elementary algebra.
>
> **Honest scope:** this bounds the *expectation*, not the truth — the model→certainty step remains the ×2×3 gap, unchanged. The bound is slack at small `n` (Salikhov's exponent is worst-case) and crosses below one ticket near `n ≈ 550`; sharper measures only improve `C₀`.
>
> **Artifacts — Merle (2026-07-24):** `experiments/test_REQ-MATH-029_regle_de_torsion.py` (+ committed output), predictions written before measurement. Open for co-editing.

**Operational definitions, read from the script (`f550147`), recorded — the script was never run:**

- **Cell:** a pair `(n, S)`, `K = n + S`, `q = 2^K − 3^n`, cells with `|q| ≤ 1` excluded. Shore =
  sign of `q` (north `q > 0`, south `q < 0`).
- **`#words` per cell:** the general-family profile count `C(n+S−2, n−1)` (the Vandermonde closed
  form of 12.6.1.5's general family — entries `≥ 1`, `Σm = n`, `Σs = S`), computed in his script
  via `lgamma` floats.
- **Ticket log-mass of a cell:** `R(n,S) = log₂(#words) − log₂|q|`; the cell's *word-unit* mass is
  `2^R = #words/|q|` — the uniform-residue expectation with each **word** (not necklace) as one
  trial of probability `1/|q|`. "Word units upper-bound necklace units" because `gcd(q, R_r)` is
  rotation-invariant (L-A1), so the necklace is the independent trial and the word count over-counts
  each necklace by its orbit size (≥ 1).
- **"Best north cell":** `R(n) = max over S of R(n,S)` restricted to `q > 0`, `S` ranging over
  `1 .. ⌊0.5849625·n⌋ + 3` (i.e. `K ≤ ⌊(β−1)n⌋ + 3 + n`, `β = log₂3` — cells up to ~3 bits past
  tuned; beyond this cap `q ≥ ~8·3^n` and the fixed point `R₀/q` drops below 1, the REQ-MATH-016
  "size artifact" region — the cap is the realizable-ticket domain, inherited from that entry, not
  re-derived in this script).
- **`ε_n`:** `K₀ − n·log₂3` with `K₀ = ⌊n·log₂3⌋ + 1` — the gap from `n·log₂3` up to the tuned
  (north) integer `K`. The "ingredient-inequality slack" is `min_{n ≤ 2000} ε_n · n^{μ−1}`,
  i.e. the factor by which the *actual* gap beats the floor `1/n^{μ−1}` that a measure
  `|log₂3 − K/n| ≥ 1/n^μ` (with `c = 1`) would guarantee. His committed value: `1.45e+01` at
  `n = 2`.
- **Where μ enters:** only in the bound line `−c_gen·n + (μ−1)·log₂n + C₀` and in the slack
  diagnostic; `C₀` is *defined* in the script as the exhibited maximum over `n ≤ 2000` of
  `Δ(n) = R_best(n) + c_gen·n − (μ−1)·log₂n` (committed: `−5.774` at `n = 2`) — it is measured,
  not derived from the source's constant `c`.
- **What the tail sums:** per scale `n`, `mass(n) = Σ_S #words/|q|` over the capped `S` range,
  **both shores**; "exact mass beyond N" = `Σ_{n>N} mass(n)` (computed to `n = 2000`); "provable
  bound beyond N" = `Σ_{n=N+1}^{2000} 2^{−c_gen·n + (μ−1)log₂n + C₀}` plus the analytic
  continuation `2^{bound(2000)}/(c_gen·ln 2)` for `n > 2000`. Committed values: beyond
  `n = 600` exact `3.414e−14`, bound `5.020e−04` (the entry's `< 5.2·10⁻⁴`).
- **Canaries (his):** `(n,K) = (5,8) → q = 13`, `(7,12) → q = 1909` (convergent-adjacent anchor
  cells); `n ≤ 14` word budgets with `S ≤ min(9, 2n)` (the REQ-MATH-022 census domain):
  north `6.17`, south `3.41`.

**Reading of the entry's logical structure, recorded for §3:** the *stated theorem* is a bound on
the **best north cell only**; the *consequence* (total both-shore mass) is the per-`n` bound applied
to `mass(n)`, which his script justifies **numerically on `n ≤ 2000`** (`bd ≥ ex` at seven cut
points), not by the two ingredients alone — the gap between "best cell ≤ bound" and "sum of ~1.17·n
cells over two shores ≤ same bound" is an elementary counting factor but it is not written out in
the entry or the script. See §3(a) for the repair and its cost (an `O(1)` constant, absorbable).

## 2. The μ source (the round's citable record)

All statements below were sourced this session from the primary literature (web, this item only);
every citation was checked against at least one primary or independently published secondary
carrier, named inline. "Merle v2 corpus §5" is his own document, not in our repos, and was not
requested, per the brief.

### 2.1 What Salikhov actually proved

**Salikhov, 2007 — the exponent `5.125` exists in print, but for `ln 3`, not `log₂3`.**
V. Kh. Salikhov, *On the irrationality measure of ln 3*, Dokl. Akad. Nauk **417** (2007), no. 6,
753–755; English transl. *Doklady Mathematics* **76** (2007), no. 3, 955–957
(DOI 10.1134/S1064562407060361). Result: the irrationality measure of `ln 3` satisfies
`μ(ln 3) ≤ 5.125` (= 41/8 exactly) — i.e. `|ln 3 − p/q| > q^(−5.125)` for all integers `p, q` with
`q ≥ q₀`, `q₀` effective (Doklady note; the printed `q₀`/constant were not accessible this session —
the statement's *exponent and subject constant* are confirmed by multiple independent secondary
carriers, including Wu–Wang 2014 below, which cites it exactly as "`μ(log 3) ≤ 5.125` …
V. Kh. Salikhov 2007").

This is the number-theoretic fact behind the entry's `5.125`: it is an irrationality measure for the
*number `ln 3`* (rational approximations `p/q` to `ln 3`), **not** for `log₂3 = ln 3/ln 2`. The two
transfer in neither direction: `log₂3` is not a rational multiple of `ln 3`, and controlling
`|ln 3 − p/q|` says nothing effective about `|n·ln 3 − K·ln 2|`. Salikhov's other celebrated
effective measures (π: `μ(π) ≤ 7.6063…`, Usp. Mat. Nauk 63 (2008); the `ln 2` line is
Rukhadze 1987 → Marcovecchio 2009) are likewise single-number results, none of them about `log₂3`.

**Superseded even for `ln 3`:** Q. Wu and L. Wang, *On the irrationality measure of log 3*,
J. Number Theory **142** (2014), 264–273 (DOI 10.1016/j.jnt.2014.03.007):
`μ(log 3) ≤ 5.1163051`, explicitly improving "`μ(log 3) ≤ 8.616…` (Rhin 1987)" and
"`μ(log 3) ≤ 5.125` (Salikhov 2007)". So even as a `ln 3` citation, `5.125` is not the current best.

### 2.2 What is actually published for `log₂3`

No published effective irrationality measure *of the number `log₂3`* with any exponent near 5
was found — and none is expected: rational approximation of `log₂3` by `K/n` is governed by the
linear form `Λ = K·ln 2 − n·ln 3` in **two** logarithms, which Padé/arithmetic single-number methods
(Salikhov's included) do not reach. What the literature provides:

- **The fully explicit, citable statement (the one the Collatz cycle literature itself uses).**
  G. Rhin, *Approximants de Padé et mesures effectives d'irrationalité*, Séminaire de Théorie des
  Nombres, Paris 1985–86, Progress in Mathematics **71**, Birkhäuser (1987), pp. 155–164 —
  Proposition, p. 160: for all integers `u₀, u₁, u₂` with `H = max(|u₁|, |u₂|)`,

  `|u₀ + u₁·ln 2 + u₂·ln 3| > H^(−13.3)`.

  Carriers of the exact statement (the 1987 volume itself is paywalled; the Proposition is applied,
  with page and parameter detail, in print): J. L. Simons and B. M. M. de Weger, *Theoretical and
  computational bounds for m-cycles of the 3n+1-problem*, Acta Arith. **117** (2005), no. 1, 51–70,
  **Lemma 12**: `Λ = (K+L)·log 2 − K·log 3 > e^(−13.3·(0.46057 + log K))`, "Proof. We apply the
  Proposition on p. 160 of [Rh] with `u₀ = 0`, `H = u₁ = K+L`, `u₂ = −K`" (their `0.46057 = ln δ`,
  `δ = log₂3`, converts `H` to their `K`; read from the published PDF this session, pp. 60–61).
  Independently, the same Proposition with the same exponent and `H = max(|u₁|,|u₂|)` is applied in
  the generalized-Collatz literature (e.g. arXiv:2205.10582, Lemmas 10/12: "`|Λ| ≥ [2K+L]^(−13.3)`…
  we apply Rhin's proposition on p. 160"). Neither published application states a validity threshold
  `H₀`; both apply it from `H` of a few hundred upward. **Flag: the Proposition's own printed
  hypotheses (any `H₀`) should be read from the Progress in Math. volume before publication**; for
  the entry's use (tail beyond `n = 600`, so `H = K₀ ≥ 952`) any plausible threshold is cleared.

  Consequence for `log₂3`, exact: with `u₀ = 0, u₁ = K, u₂ = −n`, `H = K` (for the near-tuned cells
  `K = ⌊nβ⌋ + O(1)`, `β = log₂3`): `ε_n := |K − n·β| = |Λ|/ln 2 > K^(−13.3)/ln 2`, i.e.

  `|log₂3 − K/n| > 1/(ln 2 · K^13.3 · n) ≈ 0.00315/n^14.3` —

  an **effective irrationality-measure statement for `log₂3` with exponent `μ_eff = 14.3`** and
  explicit constant `c = β^(−13.3)/ln 2 = 1/(457.4·ln 2) ≈ 3.15·10⁻³` (asymptotic in the tuned
  window; per-`n` the exact form `ε_n > K₀^(−13.3)/ln 2` needs no `c` at all and is what the
  replication uses).

- **The asymptotic-grade improvement (exponent better, threshold unpinned this session).**
  Rhin (1987, same paper) also gives the *linear independence measure* of `(1, ln 2, ln 3)`
  `ν = 7.616`, improved by Qiang Wu, *On the linear independence measure of logarithms of rational
  numbers*, Math. Comp. **72** (2003), no. 242, 901–911, to **`ν = 7.6155`**: `|u₀ + u₁ ln 2 +
  u₂ ln 3| > H^(−7.6155)` for `H ≥ H₀`. This yields `μ(log₂3) ≤ 8.6155` in the same way (and is the
  source of Wu–Wang's "`μ(log 3) ≤ 8.616` (Rhin)" line with `u₁ = 0`). The AMS full text was not
  retrievable this session (HTTP 403), so **whether Wu's `H₀` is explicit could not be confirmed
  here** — before this exponent is used in an *effective* tail bound at explicit scales, the paper's
  statement must be read; until then it is the asymptotic-grade row of the sensitivity table, not
  the citable effective one.

- **The guaranteed fallback (linear forms in two logarithms, fully explicit, much weaker).**
  N. Gouillon, *Explicit lower bounds for linear forms in two logarithms*, J. Théor. Nombres
  Bordeaux **18** (2006), no. 1, 125–146, Corollary 2.3 (read from the published PDF this session):
  for multiplicatively independent real `α₁, α₂ > 0`,
  `log|Λ| ≥ −7200·(3.409 + 1.705/D + 0.946·log D)·D⁴·h·log A₁·log A₂` with
  `h = max{log b + 3.1, 1000/D, 512 + 256/D + 142·log D}`, `b = b₁/(D·log A₂) + b₂/(D·log A₁)`.
  At `α₁ = 3, α₂ = 2, D = 1` (`log A₁ = ln 3`, `log A₂ = 1`, `b ≈ n + K/ln 3 ≈ 2.44·n`):
  `log|Λ| ≥ −36 821·1.0986·h ≈ −40 452·h`, and `h = 1000` for all `b < e^996.9` (i.e. all
  `n < ~10^430`). So the certain two-log floor is the **constant** `|Λ| ≥ e^(−4.045·10⁷)` up to
  astronomical scales — effective, published, and enormously weaker than Rhin's 13.3. (The
  Laurent–Mignotte–Nesterenko route, J. Number Theory 55 (1995) 285–321, gives the `(log B)²` form
  with smaller constants; same character. Recent holonomy-bound work (Calegari–Dimitrov–Tang,
  arXiv:2510.04156) was checked and does not treat `log 2, log 3`.)

### 2.3 Adjudication of `μ = 5.125`

**Verdict: misattributed — a transplanted exponent.** `5.125` is Salikhov's 2007 effective
irrationality measure of **`ln 3`** (real, correctly attributed to Salikhov as a number), applied in
the entry to **`log₂3`**, a different number for which no such measure is published. This is exactly
the citation slip the check was commissioned for, and his own flag ("primary source to be re-checked
before any publication") was warranted. Consequences:

- The *shape* of the entry's bound is right (an effective measure with some `(μ_eff − 1)·log₂ n`
  correction term does exist for `log₂3`), but the sourced exponent is `μ_eff = 14.3` (Rhin 1987,
  explicit, the Simons–de Weger chain) — not `5.125`; the asymptotic-grade `8.6155` (Wu 2003) may
  become usable if its `H₀` is pinned; the guaranteed two-log fallback (Gouillon 2006) is a constant
  floor `e^(−4.045·10⁷)` out to `n ~ 10^430`.
- The entry's numerical verification is untouched by this (it never exercises the measure — the
  slack diagnostic `ε_n·n^(μ−1)` uses the *actual* `ε_n`, whose empirical floor on `n ≤ 2000` is
  set by the continued fraction of `log₂3`, min `ε_n ≈ 6.4·10⁻⁵` at `n = 665`); what changes is the
  *theorem-grade tail*, quantified in the sensitivity table (§4).
- Implicit-constant note: the entry's bound and slack treat the measure as `|log₂3 − K/n| ≥ 1/n^μ`
  with `c = 1` and no validity floor. A real measure statement carries `(c, q₀)`; both enter `C₀`
  (as `−log₂ c`, and via exact computation below the floor). With Rhin's Proposition the per-`n`
  form `ε_n > K₀^(−13.3)/ln 2` is constant-free, which is why the sensitivity table uses it.

## 3. Replication (`experiments/merle_la7_check.py`, committed output alongside; 0 failures)

Fresh code; exact integer arithmetic for every `q` and word count (incremental exact binomials,
spot-checked against `math.comb` and against brute-force profile enumeration); `K₀ = bitlength(3^n)`
exactly (no floating floor anywhere); `log₂` of exact integers at ≤ 2 ulp; every pass/fail carries a
stated tolerance ≥ 10⁶ × the accumulated float error (robustness statements printed in the output;
the tightest ε-decision has margin > 10⁷ × the error, since `min_{n ≤ 2000} ε_n = 1.349·10⁻³` at
`n = 1636`). μ is a parameter throughout. His script was never run.

### 3(a) The derivation, written out (and where it is short of theorem-grade)

Best north cell at scale `n`: `K₀ = ⌊nβ⌋ + 1 = bitlength(3^n)`, `β = log₂3`, and
`q = 2^(K₀) − 3^n = 3^n·(2^(ε_n) − 1)` with `ε_n = K₀ − nβ ∈ (0,1)`. Two lines, exact:

1. `2^ε − 1 ≥ ε·ln 2` (convexity, equality at 0), so
   `log₂ q ≥ n·β + log₂ ε_n + log₂ ln 2`. An irrationality measure `|β − K/n| ≥ c/n^μ` (any
   integer `K`) gives `ε_n = n·|β − K₀/n| ≥ c/n^(μ−1)` — **this is where the exponent lands as
   `(μ−1)`**: one power of `n` is spent converting the measure on the number into a floor on the
   integer-gap `ε_n`.
2. `log₂(#words) = log₂ C(K₀−2, n−1) = K₀ − margin(n) ≤ K₀ − c_gen·n` *provided*
   `margin(n) ≥ c_gen·n` (see ingredient (ii) below). Subtracting: `R(n) = log₂#words − log₂ q
   ≤ (K₀ − c_gen·n) − (nβ + log₂ ε_n + log₂ ln 2) = −c_gen·n + ε_n − log₂ ε_n − log₂ ln 2`, and
   with `ε_n ≤ 1` and the measure floor,

   `R(n) ≤ −c_gen·n + (μ−1)·log₂ n + C₀`, with `C₀ = 1 − log₂ c − log₂ ln 2` —

   **this is where `c` enters `C₀`** (`c = 1` gives `C₀ = 1.53`; his exhibited `−5.77` is the
   *empirical* max of `Δ(n) = R_best(n) + c_gen·n − (μ−1)log₂ n`, a fit on `n ≤ 2000`, not the
   ingredient constant). In the linear-form frame (Rhin) the floor is `ε_n > K₀^(−ν)/ln 2` and the
   log term is `ν·log₂ K₀ = ν·(log₂ n + log₂ β + o(1))` with `C₀ = 1 − 2·log₂ ln 2 = 2.06`.

Grade of each ingredient, honestly:
- (i) the measure for `log₂3`: **misattributed** as entered (§2); sourced versions in §2.2.
- (ii) `margin(n) ≥ c_gen·n` for **all** `n`: the (B) asymptote (12.6.1.5) is a *limit* with
  monotone-from-above convergence *observed* (grid to 163,840); the for-all-`n` inequality the bound
  consumes is verified here exactly on `n ≤ 2000` (min `margin(n) − c_gen·n = 2.84` at `n = 2`) but
  is not yet a proved statement. Elementary to prove (entropy bound plus a Stirling cushion), not
  yet written anywhere. A third unlisted ingredient, flagged.
- (iii) best-cell → total-mass: the entry's stated theorem bounds the **best north cell**; the
  consequence sums a whole two-shore column. The repair is elementary and `O(1)`: within the cap the
  north has ≤ 3–4 cells above tuned (each with `|q| ≥ 3^n`, no measure needed), the south column
  decays geometrically away from its near-tuned cell (factor `(β−1)/β ≈ 0.37` per step at
  essentially constant `|q|`), and the south near-cell needs the measure floor on the **other side**
  (`ε'_n = nβ − ⌊nβ⌋`), which the measure provides but **his script never checks** (his slack
  diagnostic is north-only). Measured on `n ≤ 2000`: `mass(n) ≤ 1.92·(2^(R_best_north) +
  2^(R_best_south))`, so the repair costs `< 1.94` bits (the sensitivity table budgets 3).

### 3(b) Replication results vs his committed numbers (μ = 5.125 as entered)

| quantity | his | ours (exact-count path) | verdict |
|---|---|---|---|
| anchor canaries `(5,8)`, `(7,12)` | `13`, `1909` | `13`, `1909` exact | match |
| word budgets `n ≤ 14` (S ≤ min(9,2n)) | `6.17` N / `3.41` S | `6.1726` / `3.4134` | match (2 dp) |
| `C₀` = max Δ | `−5.774` at `n = 2` | `−5.774` at `n = 2` (tol 2·10⁻³) | match |
| north ingredient slack `min ε_n·n^(μ−1)` | `1.45e+01` at `n = 2` | `14.483` at `n = 2` | match |
| tail table (7 cuts, exact and bound) | e.g. `3.414e−14` / `5.020e−4` at 600 | all seven digit-consistent (rel ≤ 1.5·10⁻³) | match |
| headline cut | `< 5.2·10⁻⁴` beyond 600 | min `N` for `< 5.2·10⁻⁴` = **600** exactly | match |
| crossing "≈ 550" | `n ≈ 550` | per-`n` bound < 1 ticket at `n = 372`; cumulative tail < 1 at `N = 440` | **no reading reproduces 550** — flagged, not disputed |

Additional facts his script does not print, recorded flat: south-side slack
`min ε'_n·n^(μ−1) = 70.1` at `n = 3` (needed for the both-shore consequence; unchecked in
REQ-MATH-029); the best north cell is the tuned `K₀` at 1876/1999 scales (123 exceptions, all
`K₀ + 2`, at `ε_n` near 1 — covered by the (iii) repair); pointwise `mass(n) ≤ 2^(bound(n))` holds
for all `n ≥ 3` but fails at `n = 2` by a factor 1.71 (the exhibited `C₀` is a best-*cell*
constant, not a mass constant — absorbed by (iii)); his analytic continuation beyond `n = 2000`
uses rate `c_gen` where the rigorous rate is `c_gen − (μ−1)/(2000·ln 2) = 0.0763` — immaterial at
these values (`~2^(−119)` term), cosmetic flag. Unit reconciliation with L-A6: the `n ≤ 14` word
budgets are `2.34×` (north) and `3.05×` (south) the L-A6 necklace budgets `2.64`/`1.12` — the
word/necklace over-count ratio, consistent with "word units upper-bound necklace units."

### 3(c) Sensitivity table (the consequence under the sourced values of §2)

Bound form per row: `mass(n) ≤ 2^(−c_gen·n + T(n) + C₀ + 3)` (3 bits = the (iii) repair, measured
1.94). "min N" = smallest `N` with provable tail `< 5.2·10⁻⁴` (the entry's headline number).

| scenario | source status for `log₂3` | `T(n)` | crossing `n*` (bound < 1 ticket) | tail bound beyond 600 | min `N` |
|---|---|---|---|---|---|
| E: entry as committed (`μ = 5.125`, `C₀ = −5.77` empirical) | **none** (transplant + fitted constant) | `4.125·log₂n` | 372 | `5.02·10⁻⁴` | **600** |
| T1: `μ = 5.125`, theorem-form `c = 1` | none (transplant) | `4.125·log₂n` | 528 | `0.63` (fails) | 746 |
| T2: `μ = 5.1163051` (Wu–Wang 2014 — a measure of `ln 3`, not `log₂3`) | comparison only | `4.116·log₂n` | 527 | `0.60` (fails) | 744 |
| A: `ν = 7.6155` (Wu 2003, asymptotic; `H₀` unpinned) | asymptotic grade | `7.6155·log₂K₀` | 1098 | `1.7·10¹¹` (vacuous) | 1315 |
| **R: `ν = 13.3` (Rhin 1987 Prop. p. 160, fully explicit)** | **citable effective** | `13.3·log₂K₀` | 2016 | `2^(+94)` (vacuous) | **2233** |
| G: Gouillon 2006 Cor. 2.3 (guaranteed two-log floor) | citable effective (weak) | `5.84·10⁷` const | `7.36·10⁸` | vacuous | `~7.36·10⁸` |

**Plain statement:** the headline "`< 5.2·10⁻⁴` beyond `n = 600`" survives **only** under the
transplanted, unsourced exponent with the fitted constant. Under the best citable effective
ingredient (row R) the *same construction still closes the kiosk effectively* — the corrected
headline is: **total ticket mass beyond `n ≈ 2233` provably `< 5.2·10⁻⁴`; below that, exact finite
computation** (of which `n ≤ 2000` already exists, in his script and ours; the exact mass beyond
600 is `3.4·10⁻¹⁴`, so the *computed* picture is unchanged — only the "provable for all `n`" label
moves from 600 to ~2233). If Wu 2003's `H₀` can be pinned, row A brings that to ~1315. The
structural claim "effectively finite at every scale" is TRUE under every sourced row, including the
guaranteed floor G.

## 4. Key recommendation and offered co-edit content

**Recommendation: do not turn the key on the entry as written; turn-with-offer.** The algebra and
the numerics are confirmed digit-exact; the self-grade "theorem-grade modulo two published
ingredients" fails on exactly the ingredient he himself flagged: μ = 5.125 is not a published
ingredient *for `log₂3`* (§2.3 verdict: misattributed/transplanted — it is Salikhov's `ln 3`
measure). Adjudicated precisely, the entry is theorem-grade modulo:
1. the effective measure for `log₂3` — sourced replacement: Rhin 1987 (Prop. p. 160, exponent
   13.3; Simons–de Weger 2005 Lemma 12 is the printed Collatz-side precedent), giving
   `(μ_eff − 1) = 13.3` on `log₂ K₀` and the corrected headline scale `n ≈ 2233`;
2. the for-all-`n` margin inequality `margin(n) ≥ c_gen·n` (in-house, elementary, currently
   verified-not-proved — 12.6.1.5 states a limit, not a pointwise inequality);
3. the best-cell → both-shore-mass step (elementary `O(1)` repair, needs the south-side floor
   `ε'_n`, currently unchecked in his artifact; our measurement: factor ≤ 1.92 on the range).

Offered co-edit shape (drafting is a later session's job; content per this record): replace the
ingredient line by the Rhin/Simons–de Weger citation with `μ_eff = 14.3`/`ν = 13.3`; restate the
bound as `R(n) ≤ −c_gen·n + 13.3·log₂ K₀ + C₀` with explicit `C₀ ≈ 2.06 (+3` repair bits`)`;
restate the consequence as "provably `< 5.2·10⁻⁴` beyond `n ≈ 2233`, exact computation below"
(exact to 2000 exists; the 2000→2233 strip is a finite computation of the same kind); keep his
honest-scope paragraph unchanged (it is correct, including "sharper measures only improve `C₀`" —
which the sensitivity table now quantifies); optionally keep 5.125 in a remark as the aspirational
value *if* a measure for `log₂3` of that strength is ever published. The `n ≈ 550` crossing
sentence should be re-derived or dropped (no reading reproduces it; our two readings give 372/440).

The fusion idea itself — counting constant × individual Diophantine floor, the first trans-scale
piece — survives re-sourcing intact and is, in our judgment, the entry's real content. The finding
is delivered as: the instrument is right, the ruler's label is wrong, and the sourced ruler moves
the provable-below-one-ticket line from ~600 to ~2233 without changing anything computed.

## Flags, collected

1. μ = 5.125 **misattributed** (Salikhov 2007 proves it for `ln 3`, not `log₂3`); his own re-check
   flag was warranted; sourced alternatives and consequences in §2/§3(c).
2. Rhin's Proposition (Progress in Math. 71, p. 160): exact printed hypotheses (`H₀`, if any) not
   directly readable this session (volume paywalled); two independent published applications apply
   it unconditionally from `H` of a few hundred; for the corrected tail statement only `H ≥ 952`
   matters. Confirm from the volume before publication.
3. Wu 2003 (Math. Comp.) full text 403-blocked this session; its `H₀` explicitness unconfirmed —
   row A is asymptotic-grade until read.
4. The entry's "crosses below one ticket near `n ≈ 550`": not reproduced under either natural
   reading (372 per-scale, 440 cumulative). Recorded, not disputed.
5. His slack diagnostic is north-only; the both-shore consequence also needs the south floor
   (`ε'_n`; our min slack 70.1 at `n = 3` — passes, but was unchecked).
6. `C₀ = −5.77` is an empirical fit (max Δ on `n ≤ 2000`), not derivable from any ingredient
   constant; the pointwise mass bound with it fails at `n = 2` (factor 1.71) — both absorbed once
   the theorem-form constants are used.
7. The margin for-all-`n` inequality is a third, unlisted ingredient (verified `n ≤ 2000` here,
   `min = 2.84` at `n = 2`; provable-elementary, unproved).
8. Cosmetic: his analytic continuation term uses rate `c_gen` instead of the rigorous
   `c_gen − (μ−1)/(2000 ln 2)`; immaterial at these values.
9. His `n ≤ 14` budget canary uses the REQ-022 domain `S ≤ min(9, 2n)` while the main sweep caps at
   `S ≤ ⌊0.5849625·n⌋ + 3` — for `n = 13,14` the domains differ slightly; both replicated on their
   own domains, no consequence.
10. No pushes anywhere; clones read-only in the scratchpad; web used for item 2 only. Stopping
    rules: no cycle search, no proof effort on the open condition; the cycles front stays PARKED —
    this entry concerns the *model's* tail mass and the findings keep that framing.
