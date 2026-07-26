# Findings: our own proof of the margin inequality at the true constant `c_gen`

**Status: the inequality is PROVED, for all `n ≥ 1`, at the true constant `c_gen`, with a
uniform positive surplus — and the proof needs no Stirling term and no external citation.**
The Robbins refinement the brief sketched is also carried out; it is not load-bearing for the
headline, but it upgrades the surplus from a constant to `(1/2)log₂ n + 2.1217…`. Scope is
wider than the brief asked for: the argument covers the whole **south shore** as well as the
tuned north cell, and the first few cells above it. The gap that remains is named in §9.

Verification: `experiments/margin_inequality_proof_check.py` (+ committed output). Written
from scratch; stdlib + mpmath only; nothing imported from any earlier check in this repo.

---

## 1. Notation and the exact constant

`β := log₂ 3`. `h(x) := −x·log₂ x − (1−x)·log₂(1−x)` on `(0,1)`.

For `n ≥ 1`,
- `K = K(n) := ⌈nβ⌉`, `θ = θ(n) := K − nβ`,
- `m := K−2`, `k := n−1`, `j := m−k = K−n−1`, `p := k/m`,
- **`margin(n) := K − log₂ C(K−2, n−1)`.**

Auxiliary constants, all exact:

> `Λ := log₂(β−1)`  (`= h′(1/β)`, negative),
> `L := log₂(β/(β−1)) = log₂ β − Λ`,
> `H := h(1/β)`.

**Fact 1 (the `c_gen` identity, proved).** `h(1/β) = log₂ β − ((β−1)/β)·log₂(β−1)`, and
therefore

> **`c_gen := β·(1 − h(1/β)) = β − β·log₂ β + (β−1)·log₂(β−1)`.**

*Proof.* `h(1/β) = (1/β)log₂β − ((β−1)/β)·log₂((β−1)/β)`
`= (1/β)log₂β − ((β−1)/β)[log₂(β−1) − log₂β] = log₂β·[1/β + (β−1)/β] − ((β−1)/β)log₂(β−1)`
`= log₂β − ((β−1)/β)log₂(β−1)`. Multiply by `β` and subtract from `β`. ∎

This is the round-8 (B) closed form and the entropic form simultaneously; they are the same
expression, not two numbers that agree to twelve places. Consequently, with the Junction
constant `γ := 1 − h(1/β)`, **`γ·β = c_gen` is an algebraic identity** (this re-derives §3 of
`merle-la7-close-check-findings.md` independently — same expansion, same conclusion).
Nothing below uses a decimal value of `c_gen`; see §8 for why that matters.

**Fact 2 (the only facts about `β` the proof uses).** Each is an exact integer comparison:

| fact | equivalent integer statement | used for |
|---|---|---|
| `β < 2` | `3 < 4` | `L > 1`, i.e. `1 − L < 0` |
| `β > 3/2` | `3² > 2³` | `j ≥ 1` for `n ≥ 2` |
| `β > 10/7` | `3⁷ > 2¹⁰` | `7β − 10 > 0` (Lemma 5) |
| `β ≥ 291/184` | `3¹⁸⁴ ≥ 2²⁹¹` | `q(8) ≥ 0` (Lemma 5) |
| `β ∉ ℚ`, indeed `nβ ∉ ℤ` for `n ≥ 1` | `2^a = 3^b` is impossible for `a,b ≥ 1` (parity) | `θ ∈ (0,1)` strictly |

The last one gives `K = ⌊nβ⌋ + 1 = ⌈nβ⌉` and `0 < θ < 1` **strictly**, which is what makes
the final inequality strict.

**Fact 3 (`K` is pinned, and `C(K−2,n−1)` is the L-A7 word count).** `K = ⌈nβ⌉` is the unique
integer with `3ⁿ ≤ 2^K < 2·3ⁿ`, and equals `bitlength(3ⁿ)`. *Proof:* `3ⁿ ≤ 2^K ⟺ nβ ≤ K`;
`2^K < 2·3ⁿ ⟺ K < nβ + 1`; so `K` is the unique integer in `[nβ, nβ+1)`. ∎ The count
`C(K−2, n−1)` is the general-family word count at the cell `(n, S)`, `K = n+S`, by Vandermonde
(`Σ_r C(n−1,r−1)C(S−1,r−1) = C(n+S−2, n−1)`) — established in round 8 and re-checked here at
all `n,S ≤ 14`. So `margin(n)` is exactly the quantity ledger entry L-A7 consumes.

---

## 2. Statement

> **Theorem A.** For every `n ≥ 1`,
> `margin(n) > c_gen·n + 1 + log₂ β`,
> where `1 + log₂ β = 1.66444870745388938…`.

In particular `margin(n) ≥ c_gen·n` for all `n ≥ 1`, with uniform surplus above `1.664` bits —
the for-all-`n` ingredient flagged in round 9, at the **true** constant.

> **Theorem B′.** For every `n ≥ 2`,
> `margin(n) > c_gen·n + (1/2)·log₂ n + (1/2)·log₂(3π/5) + 1 + log₂ β`,
> the constant being `2.12171397510694569916…`.

> **Theorem A′ (scope).** For every `n ≥ 2` and every integer `K` with
> `n+2 ≤ K ≤ nβ + (2log₂β − Λ)/(L−1) = nβ + 4.79982787…`,
> `K − log₂ C(K−2, n−1) ≥ c_gen·n`; and for `K ≤ ⌈nβ⌉` — i.e. the tuned north cell **and the
> entire south shore** — the surplus `1 + log₂ β` of Theorem A holds verbatim.

---

## 3. The proof of Theorem A

Three lemmas, then two lines of algebra. Nothing is cited.

**Lemma 1 (domain).** For `n ≥ 2`: `k ≥ 1`, `j ≥ 1`, hence `m ≥ 2` and `p ∈ (0,1)`.

*Proof.* `k = n−1 ≥ 1`. And `j = K−n−1 ≥ nβ − n − 1 = n(β−1) − 1 > n/2 − 1 ≥ 0` for `n ≥ 2`,
using `β − 1 > 1/2` (Fact 2). `j` is an integer and `j > 0`, so `j ≥ 1`. ∎

**Lemma 2 (entropy bound on the binomial).** For integers `m ≥ 2`, `1 ≤ k ≤ m−1`, `p = k/m`:

> `C(m,k) ≤ 2^{m·h(p)}`.

*Proof.* All terms of `1 = (p + (1−p))^m = Σ_{i} C(m,i)·p^i(1−p)^{m−i}` are nonnegative, so the
single term `i = k` is at most `1`:  `C(m,k)·p^k(1−p)^{m−k} ≤ 1`, i.e.
`C(m,k) ≤ p^{−k}(1−p)^{−(m−k)}`. Taking `log₂` and using `k = mp`, `m−k = m(1−p)`:
`−k log₂ p − (m−k)log₂(1−p) = m·[−p log₂ p − (1−p)log₂(1−p)] = m·h(p)`. ∎

**Lemma 3 (concavity: the tangent at `1/β`).** For every `p ∈ (0,1)`:

> `h(p) ≤ h(1/β) + log₂(β−1)·(p − 1/β) = H + Λ·(p − 1/β)`.

*Proof.* `h′(x) = log₂((1−x)/x)` and `h″(x) = −1/(x(1−x)·ln 2) < 0` on `(0,1)`, so `h` is
strictly concave and lies below each of its tangent lines. The tangent point is `x = 1/β`,
which lies in `(0,1)` since `β > 1`; and `h′(1/β) = log₂((1 − 1/β)/(1/β)) = log₂(β−1) = Λ`. ∎

Multiplying Lemma 3 by `m > 0` and substituting `p = k/m` (so `m·p = k`):

> **Lemma 3′.**  `m·h(p) ≤ m·H + Λ·(k − m/β)`.

This is the step the brief expected to need a Taylor expansion with an explicit second-order
remainder. It does not: concavity gives the tangent bound **exactly, with no remainder term**,
in one line, and valid for all `p` at once. That is the structural reason the whole argument
survives having under two bits of room. (The discarded second-order term is the "concavity
gap"; measured, it is largest at `n = 2` — `0.102481` bits, where `p = 1/2` is furthest from
`1/β` — and decays like `O(1/n)`, below `10⁻⁴` for every `n ≥ 10 000`. It is never needed:
it is discarded in the safe direction.)

**Lemma 4 (the algebraic collapse — why `1/β` is the right tangent point).** For all real
`K, n` with `m = K−2`, `k = n−1`:

> `K − [m·H + Λ·(k − m/β)] = (βA − Λ)·n + A·θ + (2H − 2Λ/β + Λ)`, where `A := 1 − H + Λ/β`
> and `θ = K − nβ`;
>
> and moreover **`βA − Λ = c_gen`**, **`A = 1 − L`**, **`2H − 2Λ/β + Λ = 2log₂β − Λ`**.

*Proof.* Expand `K − mH − Λk + Λm/β = K(1 − H + Λ/β) + 2H − 2Λ/β − Λ(n−1)`; substitute
`K = nβ + θ` and collect. The three identifications:
- `βA − Λ = β − βH + Λ − Λ = β(1 − H) = c_gen` (definition of `c_gen`);
- by Fact 1, `H = log₂β − ((β−1)/β)Λ`, so
  `A = 1 − log₂β + ((β−1)/β)Λ + Λ/β = 1 − log₂β + Λ·((β−1)+1)/β = 1 − log₂β + Λ = 1 − L`;
- `2H − 2Λ/β + Λ = 2log₂β − 2((β−1)/β)Λ − 2Λ/β + Λ = 2log₂β − 2Λ + Λ = 2log₂β − Λ`. ∎

The first identification is the load-bearing one: **the linear-in-`n` coefficient of the bound
is `c_gen` identically**, because the tangent point `1/β` is exactly the entropy-optimal ratio.
At any other tangent point `p₀` the coefficient is strictly smaller than `c_gen` and the bound
drifts negative — verified as negative control NC3/NC3b (§7).

**Fact 4.** `L > 1`, hence `1 − L < 0`. *Proof.* `L > 1 ⟺ β/(β−1) > 2 ⟺ β < 2` (Fact 2). ∎

**Proof of Theorem A.**

*Case `n = 1`.* `K = 2`, `m = k = 0`, `C(0,0) = 1`, so `margin(1) = 2`. The claim is
`2 > c_gen + 1 + log₂β`, i.e. `1 > c_gen + log₂β`. By Fact 1,
`c_gen + log₂β = β − (β−1)log₂β + (β−1)log₂(β−1) = β − (β−1)·L`, so the claim is
`β − (β−1)L < 1 ⟺ (β−1)L > β−1 ⟺ L > 1`, which is Fact 4. ∎

*Case `n ≥ 2`.* By Lemma 1 the domain hypotheses hold. Chain:

> `log₂ C(m,k) ≤ m·h(p)`                        (Lemma 2)
> `           ≤ m·H + Λ·(k − m/β)`              (Lemma 3′)

so, subtracting from `K` and applying Lemma 4,

> `margin(n) = K − log₂ C(m,k) ≥ c_gen·n + (1−L)·θ + 2log₂β − Λ.`   (★)

Since `1 − L < 0` (Fact 4) and `θ < 1` **strictly** (Fact 2), `(1−L)·θ > (1−L)`. Hence

> `margin(n) > c_gen·n + (1−L) + 2log₂β − Λ = c_gen·n + 1 + log₂β`,

using `−L + 2log₂β − Λ = −(log₂β − Λ) + 2log₂β − Λ = log₂β`. ∎

**Remark (sharpness).** `(★)` shows the crude-route surplus `K − m·h(p) − c_gen·n` lies in
`(1 + log₂β, 2log₂β − Λ] + O(1/n)`, i.e. in `(1.66444…, 2.10248…]`; the lower end is the
infimum, approached as `θ(n) → 1⁻`. That `θ(n)` comes arbitrarily close to `1` infinitely
often is Weyl equidistribution of `{nβ}` — **not used in the proof**, recorded only to say the
constant `1 + log₂β` cannot be improved by this route. §8 shows the empirical minimum of the
crude route sits `4.7·10⁻⁶` above it, which is the numerical face of the same statement.

---

## 4. The Robbins refinement (Theorem B)

The one external ingredient in this document, and it is used only for Theorem B/B′:

> **Robbins (1955).** For every integer `N ≥ 1`, `N! = √(2πN)·(N/e)^N·e^{r_N}` with
> `1/(12N+1) < r_N < 1/(12N)`.  *(Cited, not reproved. Theorem A does not use it.)*

**Lemma 6 (Stirling as a credit).** For integers `k, j ≥ 1`, `m = k+j`, `p = k/m`:

> `log₂ C(m,k) < m·h(p) − (1/2)·log₂(2π·k·j/m)`.

*Proof.* Substituting Robbins three times,

> `C(m,k) = m!/(k!·j!) = √(m/(2π·k·j)) · m^m/(k^k·j^j) · e^{r_m − r_k − r_j}`,

an exact identity. Two observations. First,
`log₂(m^m/(k^k j^j)) = m log₂ m − k log₂ k − j log₂ j = m·h(k/m)` by direct expansion. Second,
`r_m − r_k − r_j < 1/(12m) − 1/(12k+1) − 1/(12j+1) < −1/(12j+1) < 0`: since `j ≥ 1` we have
`12k + 1 < 12k + 12j = 12m`, so `1/(12k+1) > 1/(12m)` and the first two terms already cancel
to something negative, while `−1/(12j+1) < 0`. Hence
`e^{r_m−r_k−r_j} < 1`, and taking `log₂` of the identity gives the claim, since
`log₂√(m/(2πkj)) = −(1/2)log₂(2πkj/m)`. ∎

Note the direction: the `√(2πm)` from the numerator is **outweighed** by the two
`√(2πk)`, `√(2πj)` from the denominator, which is exactly why the Stirling factor is a credit
of size `≈ (1/2)log₂ n` and not a debt. The brief's sketch is confirmed on this point.

**Theorem B.** For `n ≥ 2`: `margin(n) > c_gen·n + (1/2)·log₂(2π·k·j/m) + 1 + log₂β`.

*Proof.* Replace Lemma 2 by Lemma 6 in the proof of Theorem A; Lemmas 3′, 4 and Fact 4 are
unchanged. ∎

**Lemma 5 (the credit is at least `(1/2)log₂ n + const`).** For `n ≥ 8`: `k·j/m ≥ 3n/10`.

*Proof.* `k·j/m = kj/(k+j)` is strictly increasing in `j` (`∂/∂j = k²/(k+j)² > 0`). By Lemma 1's
estimate `j ≥ J := n(β−1) − 1 > 0`, and `k + J = nβ − 2 > 0` for `n ≥ 2` (Fact 2), so

> `k·j/m ≥ (n−1)·J/((n−1)+J) = (n−1)(n(β−1)−1)/(nβ−2)`.

The claim `(n−1)(n(β−1)−1)/(nβ−2) ≥ 3n/10` clears denominators to
`10(n−1)(n(β−1)−1) − 3n(nβ−2) ≥ 0`, i.e.

> `q(n) := (7β−10)·n² − (10β−6)·n + 10 ≥ 0`.

`7β − 10 > 0` by Fact 2 (`3⁷ > 2¹⁰`), so `q` is an upward parabola; its vertex sits at
`n* = (10β−6)/(2(7β−10)) ≤ 8 ⟺ 10β − 6 ≤ 112β − 160 ⟺ β ≥ 154/102 = 77/51`, which follows from
`β ≥ 291/184` (Fact 2, since `291/184 > 77/51`). Hence `q` is nondecreasing on `[8,∞)` and it
suffices that `q(8) = 368β − 582 ≥ 0`, i.e. `β ≥ 582/368 = 291/184` — Fact 2 again. ∎

**Corollary B′.** For every `n ≥ 2`:
`margin(n) > c_gen·n + (1/2)log₂ n + (1/2)log₂(3π/5) + 1 + log₂β`.

*Proof.* For `n ≥ 8`, Lemma 5 gives `2πkj/m ≥ 3πn/5`, so
`(1/2)log₂(2πkj/m) ≥ (1/2)log₂ n + (1/2)log₂(3π/5)`; apply Theorem B. For `n ∈ {2,…,7}` the
claim is decided by exact finite computation — exact integer binomials, rigorous `log₂`
enclosures — and the six slacks are all positive:

| `n` | `K` | `C(K−2,n−1)` | `margin(n)` | RHS | slack |
|---|---|---|---|---|---|
| 2 | 4 | 2 | 3.000000000 | 2.780351201 | 0.2196488 |
| 3 | 5 | 3 | 3.415037499 | 3.152151064 | 0.2628864 |
| 4 | 7 | 10 | 3.678071905 | 3.438988426 | 0.2390835 |
| 5 | 8 | 15 | 4.093109404 | 3.679271086 | 0.4138383 |
| 6 | 10 | 56 | 4.192645078 | 3.890106902 | 0.3025382 |
| 7 | 12 | 210 | 4.285754482 | 4.080621726 | 0.2051328 |

∎

So the analytic argument needs `n₀ = 8`, and the finite closure is six cases. (For Theorem A
there is no `n₀` at all: it is analytic for every `n ≥ 1`.)

---

## 5. Scope: which cells (Theorem A′)

`(★)` was derived without ever using that `K` is the tuned cell — Lemma 4 is an identity in
`K` and `n`. Written in `K` directly, the same chain gives, for `n ≥ 2` and any integer
`K ≥ n+2`:

> `K − log₂ C(K−2, n−1) ≥ (1−L)·K − Λ·n + 2log₂β − Λ = c_gen·n + (1−L)(K − nβ) + 2log₂β − Λ.`

Since `1 − L < 0`, this is **decreasing in `K`**: the bound is best on the south shore and
degrades as one climbs north. Two consequences:

- **`K ≤ ⌈nβ⌉` (the tuned north cell and every south-shore cell):** `K − nβ ≤ θ < 1`, so the
  full Theorem A surplus `1 + log₂β` holds verbatim. This covers the entire south shore down to
  `K = n+2`. (`K = n+1` gives `C(n−1,n−1) = 1` and `margin = n+1 > c_gen·n` trivially; `K ≤ n`
  gives `C(K−2,n−1) = 0`, no words at all.)
- **`nβ < K ≤ nβ + (2log₂β − Λ)/(L−1) = nβ + 4.79982787…`:** the bound stays `≥ c_gen·n`,
  with the surplus shrinking linearly to `0`. So the tuned cell plus the next three or four
  north cells are covered.

This is strictly wider than the `marginTarget` scope the round-10 audit recorded for the Lean
artifact (tuned north cell only). The south-shore half of the audit's stated coverage gap is
closed by this argument; the far-north half is not (§9).

**Proposition C (every cell, unconditional but not linear).** For `n ≥ 2` and any integer
`K ≥ n+2`, Lemma 2 alone gives `K − log₂C(K−2,n−1) ≥ 2 + (K−2)·(1 − h((n−1)/(K−2))) ≥ 2`,
since `h ≤ 1` (equality only at `p = 1/2`). Bounded below by `2` at every cell; linear in `n`
only where `(n−1)/(K−2)` is bounded away from `1/2`.

---

## 6. Assessment of the brief's route sketch

The sketch is **correct, and verified** — Robbins does turn the `(1/2)log₂ n` Stirling factor
from a debt into a credit, exactly as described (Lemma 6, with the sign traced explicitly).
Two corrections to its expectations, both in the favourable direction:

1. **The Stirling credit is not needed for the headline.** The premise that the crude bound
   "leaves an asymptotically constant margin … because it discards the `(1/2)log₂ n` factor"
   is right about the mechanism but treats a *constant* surplus as a shortage. The constant is
   `+1.664…` bits, provably positive and provably uniform. So the crude entropy bound closes
   the inequality on its own (Theorem A) — with no Stirling, no citation, and no `n₀`. Robbins
   then upgrades the surplus from `1.664` to `(1/2)log₂ n + 2.122`, which is worth having but
   is a refinement, not the proof.
2. **The perturbation step needs no Taylor remainder.** The sketch proposed comparing
   `m·h(p)` against `nβ·h(1/β)` "with an explicit second-order remainder … `h″(p)` bounded on
   the relevant `p`-interval". Concavity does it in one line with no remainder and no interval
   hypothesis (Lemma 3), which is why "under two bits of room" turned out not to be a problem:
   the only inequality in the whole chain that spends anything material is Lemma 2, whose
   measured minimum spend is `1.0` bit (at `n = 2`), while the concavity step spends `O(1/n)`.

The `p`-interval the sketch asked for is still worth recording, as an **exact identity** rather
than a hypothesis: for `n ≥ 2`,

> `p − 1/β = (2 − β − θ)/(β·m)`,  hence  `1/β − 1/(βm) < p < 1/β + (2−β)/(βm)`,

so `p → 1/β` at rate exactly `Θ(1/n)`. Nothing in the proof depends on it.

**The conjugate point, as the brief asked.** `h′(1/β) = log₂(β−1) = −log₂ x*` with
`x* = 1/(β−1) = 1.70951129135…`. This is the same optimum that the round-10 findings recovered
as the maximiser of `c(x) = β − β log₂(1+x) + log₂ x`, and the same point Merle's elementary
route approximates by the rational `12/7 = 1.71428571429…`. In our chain it appears as the
*slope of the tangent line* in Lemma 3; his rational route replaces that slope by a nearby
rational, which is precisely why his constant lands slightly below `c_gen` (his own numerics:
`0.0793165` against `c_gen = 0.0793186`, a loss of `2.1·10⁻⁶`; the further drop to `1/13` is
the rounding to a safe rational, not the tangent choice). Two routes, one optimum, described
in two vocabularies.

---

## 7. Verification

`experiments/margin_inequality_proof_check.py`, output committed as
`experiments/margin_inequality_proof_check_output.txt`. Independent implementation; imports
nothing from earlier checks; stdlib + mpmath only.

**Method.** `K(n) = bitlength(3ⁿ)` from exact integer powers. `C(K−2,n−1)` an exact Python
integer. Its `log₂` is never taken as a float: with `b = C.bit_length()`, `s = max(0, b−200)`,
`lo = C >> s`, we have `lo·2^s ≤ C < (lo+1)·2^s` with `lo < 2²⁰⁰` exactly representable at
`mp.dps = 80`, giving a rigorous enclosure `log₂ lo + s ≤ log₂ C < log₂(lo+1) + s`; when `s = 0`
the integer is exact and the enclosure collapses to a point. Every inequality is decided with
the conservative end of the enclosure. The widest enclosure used over the sweep is
`1.7956·10⁻⁶⁰` bits, against a smallest decided slack of `3.4362·10⁻¹⁴` bits — a ratio of
`1.9·10⁴⁶`, so no decision is anywhere near the precision floor. As an extra control, the fifty
tightest Theorem-A cases were recomputed at `mp.dps = 160`; maximum disagreement `1.0·10⁻⁷⁰`.

**Each link checked separately over `n = 1..20 000`** (so that a broken link cannot be masked
by slack elsewhere), with minimum slack and its location:

| step | claim | min slack | at |
|---|---|---|---|
| S1a | `min(k,j) ≥ 1` for `n ≥ 2` (Lemma 1) | `0` (i.e. holds) | `n = 2` |
| S1b/c | `p` inside `[1/β − 1/(βm), 1/β + (2−β)/(βm)]` | `8.3·10⁻⁶` / `6.7·10⁻¹⁰` | `19950` / `15601` |
| S1d | the `p` identity `p − 1/β = (2−β−θ)/(βm)` | residual `< 1.3·10⁻⁸¹` | — |
| S2 | `m·h(p) − log₂C(m,k) ≥ 0` (Lemma 2) | `1.0` | `n = 2` |
| S3 | tangent `≥ m·h(p)` (Lemma 3′) — the concavity gap | `3.4·10⁻¹⁴` | `n = 15602` |
| S4 | Lemma 4 is an identity | residual `< 4.8·10⁻⁷⁷` | — |
| S5 | `K − m·h(p) − c_gen·n − (1+log₂β) > 0` | `3.245471471·10⁻⁵` | `n = 16266` |
| S7 | Robbins step (Lemma 6) | `1.249520094·10⁻⁵` | `n = 20000` |
| S8a | `k·j/m ≥ 3n/10` for `n ≥ 8` (Lemma 5) | `0.1454545455` | `n = 8` |
| S8b | **Theorem B′** | `0.1494979158` | `n = 16266` |
| S6 | **Theorem A** | `0.2562326798` | `n = 1` |
| S9 | `margin(n) ≥ c_gen·n`, `n ≥ 1` | `1.920681387` | `n = 1` |
| S9b | `margin(n) ≥ c_gen·n`, `n ≥ 2` (L-A7 cell domain) | `2.841362774` | `n = 2` |

S5's minimum `3.2·10⁻⁵` at `n = 16266` is the sharpness of Theorem A's constant showing up
numerically: `θ(16266) = 0.99993…`, and the bound `(★)` is `1 + log₂β` in the limit `θ → 1⁻`.
The inequality is strict for every `n` because `θ < 1` strictly (Fact 2), and the code confirms
it never touches zero.

**Theorem A′ (cell scope)** was checked separately over `n = 2..600` and every integer `K` in
`[n+2, ⌊nβ + 4.7998278717⌋]` — **107 444 cells**: `margin(n,K) ≥ c_gen·n` at every one,
minimum slack `2.84136277445` at `(n,K) = (2,4)`; for `K ≤ ⌈nβ⌉` (south shore + tuned cell) the
surplus form holds with minimum `1.176914067`, also at `(2,4)`; and **zero violations** of the
`K`-form bound `margin(n,K) ≥ (1−L)K − Λn + 2log₂β − Λ` itself. Control NC-A′: three cells above
the window edge the `K`-form bound no longer reaches `c_gen·n` for any `n ≤ 200`, so the edge is
real and not an artefact of slack.

**The finite closure of Corollary B′ at `n = 2..7`** is printed by the script as its own
section (the table in §4), since it is part of the proof rather than a confirmation of it.

**Negative controls (each must fail, and does).**

| control | result |
|---|---|
| NC1 `margin(n) ≥ c·n` at `c = c_gen + 0.001` | fails first at `n = 8857` |
| NC1 at `c = c_gen + 0.00075` | fails first at `n = 12076` |
| NC1 at `c = 2/25 = 0.08` (Merle's own control) | fails first at `n = 13406` |
| NC1b at `c = c_gen` itself | **no** failure (control of the control) |
| NC2 Theorem-A surplus inflated by `0.26` | fails at `n = 1` (constant near-sharp there) |
| NC2b using the `θ→0` end `2log₂β − Λ` as if uniform | fails first at `n = 2` |
| NC3 tangent point `p₀ ∈ {0.55, 0.60, 0.65}` | slope strictly `< c_gen` in every case |
| NC3 tangent point `p₀ = 1/β` | slope `= c_gen` to `5.3·10⁻⁸²` |
| NC3b the `p₀ = 0.60` bound | drifts below `c_gen·n` at `n = 383` |
| NC4 Stirling credit doubled | breaks the Robbins step at `n = 2` |
| NC5 `p`-window narrowed 10× | fails at `n = 2` (S1b/c not vacuous) |
| NC6 Lemma 5 constant raised `3/10 → 4/10` | fails at `n = 8` |

NC3 is the structural one: it demonstrates that `1/β` is the unique tangent point at which the
linear coefficient equals `c_gen`, i.e. that Lemma 4's cancellation is doing the work and there
is no slack hiding elsewhere.

---

## 8. Cross-check against the round's published figures — and one correction

- **Min slack `2.8414` at `n = 2`** (L-A7 / REQ-MATH-036): reproduced, `2.841362774` at `n = 2`
  over `2 ≤ n ≤ 20000`. At `n = 1` — the spent-stock `q = 1` cell, outside the L-A7 cell
  domain — the slack is `1.920681387`, which is why the recorded minimum is at `n = 2`.
- **The crude-route figures.** With the Stirling credit discarded, our bound `(★)` predicts the
  crude-route surplus lies in `(1.66444871, 2.10248137]` up to an `O(1/n)` concavity gap.
  Measured over `n ≤ 200 000` **with the exact `c_gen`**: minimum `1.664453377` at
  `n = 111202`, maximum `2.102482029` at `n = 190537` — the minimum sits `4.7·10⁻⁶` above the
  proved floor `1 + log₂β`, and the maximum `6.6·10⁻⁷` above the `θ→0` end (that excess *is*
  the concavity gap, which is positive). The proved interval is confirmed to six decimals from
  both sides.
- **One flat correction, no dispute.** The ledger's crude-route figures — `1.6647` at
  `n = 16266` and `2.10492` at `n = 190537` — are **not** what the exact constant gives. They
  are what one gets by taking `c_gen` as the **7-digit decimal `0.0793186`** instead of the
  exact `β(1 − h(1/β)) = 0.07931861277485538…`. The difference `1.2775·10⁻⁸` is invisible at
  small `n` and worth `0.0024` bits by `n = 190537`. Re-running our sweep with that decimal
  reproduces both published figures digit-exactly: minimum `1.664689` at `n = 16266`, maximum
  `2.104916` at `n = 190537`. So: his numbers are correct for the constant he used, the argmin
  `n = 16266` is an artefact of the truncation (the true argmin over `n ≤ 200 000` is
  `n = 111202`), and nothing about the conclusion changes. It is worth one clause in the ledger
  because the true minimum `1.664453…` is the one that matches the proved floor `1 + log₂β`,
  and the coincidence is the whole point.
- **`margin(n)/n` approaching `c_gen` from above** (NUMERICAL, not part of the proof):
  `0.137384` (`n = 100`), `0.086994` (`1000`), `0.081073` (`5000`), `0.079795` (`20000`),
  against `c_gen = 0.0793186`. Consistent with the round-8 asymptote, and with `(★)`: the
  excess is `≈ ((1/2)log₂n + 2.1)/n`.

---

## 9. What this does not cover

1. **Far-north cells.** Theorem A′ covers `K ≤ nβ + 4.79982787…`. For cells further above the
   tuned one the tangent-at-`1/β` bound degrades linearly in `K` and eventually gives nothing;
   Proposition C still gives `margin > 2` there, but not `c_gen·n`. Recovering a linear rate
   for those cells needs a tangent at `p₀ = n/K` instead, with a rate `1 − h(n/K)` that depends
   on the cell — not attempted here. In the L-A7 accounting those cells are handled by the
   best-cell → both-shore repair (`|q| ≥ 3ⁿ` above tuned, geometric decay), not by this bound.
2. **The rest of L-A7.** This is ingredient (ii) — the counting half — and only that. The
   Diophantine input (Rhin 1987 / Simons–de Weger 2005), the best-cell → both-shore repair, and
   the south floor `ε′_n` are untouched and remain exactly where the ledger says they are.
3. **The odd-step stratum.** Only the general-family count `C(K−2,n−1)` is treated. The
   stratified constant `c_strat = 0.2667875…` is not addressed.
4. **One citation, in Theorem B/B′ only.** Robbins' inequalities are cited, not reproved.
   Theorem A, Theorem A′ and Proposition C use nothing external.
5. **No claim of novelty.** `C(m,k) ≤ 2^{m h(k/m)}` is textbook (Cover–Thomas Lemma 17.5.1) and
   the tangent-line trick is standard convexity. The content here is that this particular
   tangent point makes the linear term cancel *identically* at `c_gen`, so that the crude bound
   suffices, and the accounting of what is left over.

---

## 10. Summary for the record

**Proved, our side, independently written and independently verified:** for all `n ≥ 1`, at the
tuned north cell `K = ⌈n·log₂3⌉`,

> `margin(n) = K − log₂ C(K−2, n−1) > c_gen·n + 1 + log₂(log₂ 3)`,  `c_gen = β(1 − h(1/β))`,

and, for `n ≥ 2`, the refined form `margin(n) > c_gen·n + (1/2)log₂ n + 2.12171397510694…`.
The same argument covers every south-shore cell and the first three or four cells above the
tuned one (Theorem A′). This is the for-all-`n` margin inequality that round 9 flagged as an
unproved ingredient of L-A7 — now at the **true** constant rather than `3%` below it, by the
entropic route that connects to the published Junction form, with the Stirling term handled
explicitly (and shown to be a credit, not a debt, and not needed for the headline).
