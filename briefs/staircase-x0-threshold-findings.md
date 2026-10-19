# Findings: the staircase at a size threshold `X₀` (Rozier 1991 p. 11, Simons–de Weger 2005 p. 69)

**Task:** `briefs/staircase-x0-threshold-brief.md`. Branch `staircase-x0-threshold`, base **`6bb473a`**. The worktree was cut at `946e0d8` and fast-forwarded to `6bb473a` before any work. Sources were read 2026-10-19: Simons–de Weger v1.44 (2010) from `math.deweger.net`, and Rozier 1991 (*Singularité* 2(5), pp. 8–11, scan from `probleme-syracuse.fr`, read from the page images). Both downloads are in the session scratchpad, outside the repo. Nothing outward was done.

**Stopping rules.** This is a size-only construction serving the uniform trim. It runs no cycle search, no divisibility test (`q | R_r` is never evaluated), and no per-period exclusion run.

## 1. The formulation (fixed before any proof)

### 1.1 Objects

The notation is that of `cycles.md` 12.1, 12.6.1 and 12.8. A *configuration* has `p` blocks with entry depths `m_t ≥ 1` and exit valuations `s_t ≥ 1`. Put `n = Σ m_t`, `K = n + Σ s_t`, `q = 2^K − 3^n > 0`, `γ = K − log₂ q`, and `ε_p := (L−1)/(L^p − 1)` with `L = log₂ 3`. `R_r` is the rotation numerator of 12.6.1. Put

```text
a_r := R_r / q ,        x_r := 2^{m_r} · a_r − 1 .
```

`x_r` is the start of block `r` (a local minimum) in the rational Terras cycle that the configuration defines. `a_r` is Simons–de Weger's `a_i` in `x_i = 2^{k_i} a_i − 1` (SdW v1.44 §2.1, p. 5; the dictionary is that of `briefs/ceiling-novelty-refresh-findings.md` §1, checked afresh here in Part C of the script). Let `x_min := min_r x_r`, the smallest element of the cycle. The odd run climbs from `x_r` and the even run descends to `x_{r+1}`, so the minimum over block starts is the minimum over all elements. Also `Λ = K ln 2 − n ln 3 = −ln(1 − 2^{−γ})`.

### 1.2 The threshold condition, as Simons–de Weger pose it

SdW's Lemma 7 (v1.44 p. 8; 2005 p. 58) is stated for `m`-cycles. Its proof uses exactly two size facts: `a_i ≥ 1` (Lemma 6, from integrality) and `x_i ≥ X₀` (Lemmas 6, 7, through `b = 2^{−1/δ}(1 + X₀^{−1})`). The threshold version of a size-passer is therefore:

* **(S)** `q ≤ R_r` for every rotation `r`, i.e. `a_r ≥ 1` (12.8.6's condition, threshold `1`);
* **(X)** `x_min ≥ X₀`, i.e. `(X₀ + 1)·q ≤ 2^{m_r} R_r` for every `r`.

**The brief's parenthetical needs a correction.** It writes "`X₀·q ≤ R_r` (equivalently rational cycle elements `≥ X₀`)". That gloss is wrong: `R_r/q = a_r = (x_r + 1)/2^{m_r}` is not a cycle element. The condition `X₀ q ≤ R_r`, here called **(X′)**, says `a_r ≥ X₀`. It implies (X), since `x_r ≥ 2a_r − 1 ≥ 2X₀ − 1 ≥ X₀`, and it is strictly stronger. It is not SdW's hypothesis. (X) is the primary condition here. (X′) is treated in a remark (§4.4), because the two conditions turn out to have different `X₀`-costs: they combine with the trim's `ε_p n` term as a maximum and as a sum respectively.

### 1.3 What "sharp" must mean for Simons–de Weger p. 69

The sentence (2005 p. 69; v1.44 p. 16): "Computational and heuristical evidence indicates that for given `m` and `K` the worst case values for `k_i` and `l_i` can be estimated … We believe that Lemma 7 is almost sharp for the worst case, in the sense that at best we expect that the factor `m c_m` may be improved to a constant, but the exponential dependence on `m` in the term `2^{−((δ−1)/(δ^m−1))K}` seems unavoidable." In the record's dictionary, SdW's `m` is `p` and SdW's `K` is `n`.

Two facts fix the meaning.

1. `Λ` depends only on `(n, K)`, not on the configuration. And `γ > 1` forces `K = ⌈nL⌉`, since `K ≥ ⌈nL⌉ + 1` gives `q ≥ 2^{K−1}`. So at given `(p, n)` the "worst case over `k_i, l_i`" is not a maximisation of `Λ`. It is the question **whether any configuration satisfying (S) and (X) exists** at that `(p, n)`, given its `Λ`.
2. SdW's Lemma 7 is Corollary 5 (`Λ < m/x_min`) composed with the chaining bound `x_min > c_m^{−1} 2^{ε K}`. At threshold `X₀`, Corollary 5 already gives `Λ < m/X₀`, so Lemma 7 is the operative bound only where `2^{ε_p n} ≳ X₀`. A family at the canonical scale `n ≈ L^p` (`ε_p n ≈ 0.6`) with `x_min ≥ X₀` large tests Corollary 5, not Lemma 7.

**Statement S (SdW, as posed).** There are absolute constants `C₁, C₂` such that for every `X₀ ≥ 1` and every period `p ≥ p₁(X₀)`, at every scale `n` with `ε_p n ≳ log₂ X₀` that the Diophantine supply allows, some configuration satisfies (S) and (X) with `Λ ≥ 2^{−C₁}·2^{−ε_p n}`, i.e. `γ ≤ ε_p n + C₂`. The companion statement is two-sided at given `(p, n)`: existence is decided by `γ(n)` against `max(ε_p n, log₂ X₀)`, to within `O(1) + log₂ p`.

S settles both halves of the p. 69 sentence. "Exponential dependence unavoidable": no bound `Λ < f(p)·2^{−g(p)·n}` with `g(p)/ε_p → ∞` survives the family. "At best a constant": the family puts a floor `2^{−C₁}` under any constant that could replace `m c_m`. Whether `m c_m` can be lowered *to* a constant, i.e. whether the `log₂ p` slack in the necessity direction can be removed, is SdW's own "at best we expect". S does not claim it.

### 1.4 What "integer realization" must mean for Rozier p. 11

Rozier's Lemme 3 (p. 10) gives one inequality per minimum `j`, written in block order from the smallest element `U₀`. Its leading term is `(2/a)^{M_{j−1}} 2^{m_j}`. Lemme 4 (p. 11) bounds `max_j` of these below by `2^{((α−1)/(α^n−1))M}` (here `a = 3`, `α = L`, his `n` = `p`, his `M` = `n`). His remark: this is the minimum of the maxima over positive **real** tuples with fixed sum, attained when all terms are equal, i.e. `m_j = c·α^{j−1}` with `c = ε_p M`; so the lemma is "optimal si l'on part du lemme 3 et si l'on ne prend pas en compte d'autres propriétés éventuelles des `(m_i)`".

**Statement R (Rozier).** There is an absolute `C₃` such that for every `p ≥ p₁` there are **integer** configurations satisfying (S) at **every** rotation, not just Lemme 3's single relaxed inequality per minimum, whose Rozier quantity

```text
ρ := max_j ( m_j − (L−1)·M_{j−1} )        (block order from the minimum)
```

satisfies `ε_p n ≤ ρ ≤ ε_p n + C₃`. The lower bound holds for every real tuple in every order (the minimax). R thus says that the real extremal is realised by integers satisfying all `p` size conditions, to within an additive absolute constant in the exponent.

### 1.5 How the two differ, and the statement that answers both

R is a statement about the **profile** at threshold `1` (Rozier uses no `X₀`). S is a statement about **`Λ`** (equivalently `γ`) at threshold `X₀`. They are linked through `ρ ≤ γ` and `log₂(x_min + 1) ≥ γ − 1`. One family answers both if its configurations satisfy (S) and (X), have `ε_p n ≤ ρ ≤ γ ≤ ε_p n + C`, and have `x_min ≥ X₀`. That is the target. Its `X₀`-dependence is to be derived, not assumed. The brief's working guess was `γ ≤ log₂ X₀ + C`. A matching lower bound is required.

A third sense is kept separate. At the canonical scale `n ≈ L^p` the staircase "as built" (12.8.6.2) can carry the threshold by Diophantine quality alone. That tests Corollary 5, not Lemma 7 (§1.3, fact 2). It is recorded as a corollary and not offered as the answer to S.

## 2. Verdict

**Proved** (grade: theorem; independent exact check below), with one obstruction recorded exactly.

1. **The `X₀`-dependence, derived.** In every configuration (any `p`, any `n`, `q > 0`), `γ − 1 ≤ log₂(x_min + 1) < γ + log₂ p`. So the threshold (X) costs exactly `log₂ X₀` in `γ`, up to `[−log₂ p, +1]`. It combines with the trim's `ε_p n` as a **maximum**, not a sum. At given `(p, n)`, an (S)+(X) configuration exists if `γ(n) ≥ max(ε_p n + L/(L−1) + η, log₂(X₀+1) + 1)`, and none exists if `γ(n) ≤ max(ε_p n, log₂(X₀+1)) − log₂ p` (§3, §4).
2. **The staircase at threshold `X₀`.** Construction B of 12.8.6.2 is used unchanged, under a weaker hypothesis (H1′). Its crash block then goes **deep**: the last block continues the geometric climb instead of being a unit block. That is Rozier's real extremal `m_j = c·L^{j−1}` realised in integers. At every `X₀ ≥ 1` and every period `p ≥ p₁(X₀)`, it gives configurations meeting all `p` size conditions with `x_min ≥ X₀` and
   ```text
   g ≤ γ ≤ g + 1,   λ ≤ γ − ε_p n ≤ λ + 1.5,   ε_p n ≤ ρ = m_0 ≤ γ,   γ − 1 ≤ log₂(x_min+1) ≤ γ + 1.87447,
   g := 1 + max(log₂(X₀+1), λ),   λ := L/(L−1) + 2^{−20} = 2.7095122 .
   ```
   For `X₀ ≥ 5.5411` this is `log₂(X₀+1) + 1 ≤ γ ≤ log₂(X₀+1) + 2`. The brief's guess `γ ≤ log₂ X₀ + C` holds, with `C = 2` against `log₂(X₀+1)`. The matching lower bound is `γ > log₂(X₀+1) − log₂ p` for **every** (S)+(X) configuration. The coefficient of `log₂ X₀` is therefore exactly `1`, on both sides (§5).
3. **The period range.** `p₁(X₀)` is explicit through the continued fraction of `L`. It is tabulated for `X₀ = 2^j`, `j ≤ 200`: `p₁ = log_L X₀ + [2.784, 10.629]` (over every `j ≤ 200`; `[2.92, 10.42]` over the tabulated rows only), with `p₁ = 10` for `X₀ ≤ 16`, `p₁ = 98` at SdW's `X₀ = 5·2^{60}` and `p₁ = 110` at `2^{71}`. A closed form uniform in `X₀` would need a bound on the partial quotients of `L` or an effective irrationality measure; none is claimed (§5.3).
4. **The obstruction for the staircase as built.** Every size-passer with a unit block (crash depth `1`, the shape of 12.8.6.2 under (H1)) obeys `γ + log₂ p > (L−1)(n − L^{p−1})/(L^{p−1} − 1) ≈ L·ε_p n − (L−1)`. At the scale where Lemma 7 binds, that is a factor `L` too much. So the crash-depth-1 staircase cannot answer SdW at the threshold scale once `ε_p n > (λ + 2.09 + log₂ p)/(L−1)`. In the tabulated rows this holds from `X₀ = 2^{20}` on. The deep crash is forced, not chosen (§6).
5. **Simons–de Weger p. 69.** At every `X₀` and `p ≥ p₁(X₀)` the family has `Λ ≥ 2^{−(λ+1.5)}·2^{−ε_p n} = 0.05405…·2^{−ε_p n} > 0.054·2^{−ε_p n}`, from the crossover scale upward. The crossover is the scale at which their Lemma 7 (`Λ < p c_p 2^{−ε_p n}`) and their Corollary 5 (`Λ < p/X₀`) agree to within `c_p·2^{λ−1/2}`, which tends to `√2` as `c_p → c_∞`. At every higher level, Lemma 7 is the operative bound. The exponential dependence on `m` is attained. The factor `m c_m` cannot be lowered below the constant `0.054`. Whether it can be lowered *to* a constant is the `log₂ p` gap that remains (§7.2).
6. **Rozier p. 11.** The family realises his minimax in integers, with every rotation's exact size condition met: `ε_p n ≤ ρ ≤ ε_p n + λ + 1.5`. His Lemme 4 itself carries the additive `−2^p` and is vacuous throughout the family's range (`ε_p n < p` there). What is realised is the optimality remark, not the inequality (§7.1).

No cycle search, no divisibility test, no exclusion run. Every configuration built is a size-passer only. `q | R_r` was not evaluated, so unlike 12.8.6 the record here does not say "all fail divisibility". It says nothing about divisibility at all. 12.8.5 is unaffected.

## 3. Necessity: every configuration (Proposition 12.8.7.1)

Let a configuration have `q > 0`. Write `w(A) = (L−1)·m(A) − s(A)` (12.8). For the rotation from `r`, let `A_t` be the blocks strictly after position `t`, i.e. the arcs ending at block `r − 1`, including the empty arc at `t = p − 1`.

**(i) The element identity and the sandwich.**
```text
x_r + 1 = 2^γ · Σ_t 2^{w(A_t)} (1 − 2^{−s_t})     for every r,   hence   γ − 1 ≤ log₂(x_min + 1) < γ + log₂ p .
```
*Proof.* 12.8.1's exponent identity says term `t` of `R_r` equals `2^{K − m_r + w(A_t)}(1 − 2^{−s_t})`. Re-derived here: `S_t + s_t = (S − Σ_{j>t} s_j) + (n − m_r − M_t)`. Multiply by `2^{m_r}/q = 2^{m_r}·2^{γ−K}`. The empty-arc term is `1 − 2^{−s_{r−1}} ≥ 1/2`, so every `x_r + 1 ≥ 2^{γ−1}`. For the upper bound, let `W_j` be the partial weights, so `W_0 = 0` and `W_p = nL − K < 0`. Let `j*` minimise `W_j` over `1 ≤ j ≤ p` and put `r₀ = j* mod p`. Every non-wrapping arc ending at `r₀ − 1` then has weight `W_{j*} − W_i ≤ 0`, using `W_0 = 0 > W_{j*}`. Every wrapping arc has weight `W_p + W_{j*} − W_i < 0`. So all `p` terms are `< 1`, and `x_{r₀} + 1 < p·2^γ`. ∎

The lower end is tight: it is approached to within `10^{−6}` in the random sample (printed to six decimals). The upper end is approached to `0.0014` bits. Its `log₂ p` is real: repeating one block `p` times gives `log₂(x_min+1) − γ → log₂ p − O(1)`, as in Part C's repeated-block table. Neither bound needs (S). The threshold condition is thus controlled by `γ` alone: `γ ≥ log₂(X₀+1) + 1` forces `x_min ≥ X₀` in any configuration, and `x_min ≥ X₀` forces `γ > log₂(X₀+1) − log₂ p`.

**(ii) The trim**, exactly as 12.8.1 proves it. Its proof uses only (S): every size-passer has `γ + log₂ p > ε_p n`. This is SdW's Lemma 7 and Rozier's Lemme 4 in this record's coordinates (the subsumption is recorded in `briefs/ceiling-novelty-refresh-findings.md` and `briefs/ceiling-ccchallenge-sweep-findings.md`). It is not new.

**(iii) The unit-block bound (new).** If (S) holds, `p ≥ 2`, and some `m_t = 1`, then `γ + log₂ p > (L−1)(n − L^{p−1})/(L^{p−1} − 1)`.
*Proof.* Walk 12.8.1's recursion from the reset `r₀`: `T_0 < γ'` and `T_j < L T_{j−1} + γ'`, with `γ' = γ + log₂ p`. At the unit block's position `j₁`, use `T_{j₁} = T_{j₁−1} + 1` instead. Before `j₁`, `T_j < γ'(L^{j+1} − 1)/(L − 1)`. After it, iterating gives `n = T_{p−1} < γ'(L^{p−1} − 1)/(L−1) + L^{p−1−j₁} ≤ γ'(L^{p−1} − 1)/(L−1) + L^{p−1}`. ∎
At `n = κL^p` the right side is `L(L−1)κ − (L−1) + o(1) = L·ε_p n − 0.585`. A unit block costs a factor `L` in the slope.

**(iv) Rozier's minimax.** For any positive reals `m_j` in any cyclic order, `ρ = max_j(m_j − (L−1)M_{j−1}) ≥ ε_p·Σm_j`. If every term were `< c`, then `M_j < L M_{j−1} + c` and `Σm < c(L^p − 1)/(L − 1)`. Rozier states this (p. 11). It is recorded here because the family is measured against it.

## 4. The construction under a weaker hypothesis: the deep crash (Theorem 12.8.7.2)

Construction B and every symbol are as in 12.8.6.2. Replace (H1) by

```text
(H1′)   γ ≥ max( 2 + η , Γ′(p, n) ),
        Γ′(p, n) := 1 + η + [ L^p − L² − (L−1)(p−2) + (L−1)² n ] / [ (L−1)(L^p − 1) ]
                  = ε_p n + Γ′₀(p) + η,      Γ′₀(p) < L/(L−1) = 2.7095113 .
```

The bound on `Γ′₀` is elementary: `Γ′₀(p) < 1 + 1/(L−1)` is equivalent to `L² + (L−1)(p−2) > 1`. The `n`-coefficient is exactly `ε_p`, the trim's exponent.
(H0) is unchanged. **Claim:** the profile has all entries `≥ 1` and `Σ m = n`, and its crash depth `c = n − T_{p−2}` satisfies `c ≥ 1`. It satisfies `q ≤ R_r` at **every** rotation. Its Rozier quantity from block 0 is `ρ₀ = m_0 ≤ γ − η`. If `γ ≥ log₂(X₀+1) + 1`, then also `x_min ≥ X₀`.

*Proof.*
- **Well-definedness and climb rotations.** Steps (a) and (e) of 12.8.6.2 are used verbatim: (a) uses only `γ ≥ 2 + η` and (H0); (e) shows that for `r ≤ p − 2`, `m_r ≤ cap_r` is one term of `R_r`. The budget gives `T_{p−2} ≤ n − 1`.
- **The crash rotation.** The new step: `R_{p−1}` contains the term `3^{T_{p−2}}(2^{s_c} − 1)`, at position `0` in rotation order from `p − 1`, with `M_0 = T_{p−2}` and `S_0 = 0`. So (S) at `r = p − 1` follows from `q ≤ 3^{T_{p−2}}(2^{s_c} − 1)`, i.e. `L·T_{p−2} ≥ n + p − 1 − γ + η` (call it (D)), using `s_c = K − n − p + 1`.
  - *Case 1: the budget never binds.* Then `T = T̂`, and `T̂_{p−2} > A_{p−2}` by 12.8.6.2 (b). Clearing the closed form (c) gives the identity `L·A_{p−2} − (n + p − 1 − γ + η) = [(L−1)(L^p − 1)/(L−1)²]·(γ − Γ′(p, n))`, checked exactly in Part B. So (H1′) gives (D).
  - *Case 2: the budget binds.* Then `T_{p−2} = n − 1` and `c = 1`, by 12.8.6.2 (d)'s first half. (D) reads `(L−1)n ≥ L + p − 1 − γ + η`. (H0) gives `(L−1)n ≥ Lp − γ + η`, which suffices because `(L−1)(p−1) ≥ 0`.
- **`ρ₀ = m_0 ≤ γ − η`.** For climb blocks `r ≥ 1`, `m_r − (L−1)T_{r−1} ≤ γ − r − η < ⌊γ − η⌋`. For the crash in Case 1, `c − (L−1)T_{p−2} = n − L T_{p−2} < γ + 1 − p − η`. In Case 2 it is `1 − (L−1)(n−1) ≤ 0`. The maximum is the first block.
- **`x_min ≥ X₀`** is §3 (i).

∎

Where `γ < Γ(p, n)`, the record's own demand, Case 1 occurs and the crash is deep. `Γ(p,n)` has `n`-slope `(L−1)/(L^{p−1} − 1) ≈ L·ε_p`, against `Γ′`'s `ε_p` (Part B prints the ratio, `1.585` at `p = 20, 30`). In the check, (H1) fails at 83 of 95 runs and the crash is deep at 66 of 95.

**Uniform cap on the minimum element** (used in §5). For these profiles `x_0 + 1 = 2^γ[(1 − 2^{−s_c}) + ½Σ_{t ≤ p−2} 2^{−e_t − δ}]`, where `e_t = (L−1)T_t − t − 1` and `δ = δ(n)`. Before the budget binds, `m_t ≥ 2`, so `e_t ≥ e_0 + (2L − 3)t`. After it binds, `T_t ≥ n − p + 1`. Hence
`log₂(x_min + 1) ≤ log₂(x_0 + 1) ≤ γ + log₂(1 + 2^{−(L−1)m_0}/(1 − 2^{−(2L−3)}) + (p−1)·2^{p−1−(L−1)(n−p+1)})`.

### 4.4 The stronger condition (X′) `X₀ q ≤ R_r`

The same proof with `q` replaced by `Q = X₀ q` throughout the caps, i.e. `γ` by `γ − log₂ X₀`, gives (X′) under `γ − log₂ X₀ ≥ max(2 + η, Γ′(p, n))` and (H0) with `γ − log₂ X₀`. The trim's proof with `Q` gives the necessity `γ + log₂ p > log₂ X₀ + ε_p n`. So (X′) costs `log₂ X₀ + ε_p n`, a **sum**: two-sided again, with slack `[−log₂ p, L/(L−1) + η]`. Six exact runs at `X₀ ∈ {2, 16, 100}` gave `γ − log₂ X₀ − ε_p n ∈ [3.07, 3.67]`. (X′) is not SdW's hypothesis (§1.2). It is recorded so that the brief's parenthetical has its correct answer.

## 5. Availability: every period `p ≥ p₁(X₀)` (Theorem 12.8.7.4)

### 5.1 Statement

For real `X₀ ≥ 1`:
- put `g := 1 + max(log₂(X₀+1), λ)`;
- write `δ(x) := −log₂(1 − 2^{−x})`, the involution with `γ(n) = δ(δ(n))`;
- put `ℓ := δ(g) − δ(g + 1)`;
- let `θ_j := |q_j L − p_j|` be the convergent distances;
- put `N := q_k + q_{k−1}` for the least `k ≥ 1` with `θ_{k−1} ≤ ℓ`;
- define `p₁(X₀)` as the least `p` with `(L^p − 1)/(2(L−1)) ≥ max(N, 3p + 40)`.

Then for every `p ≥ p₁(X₀)`, the window `W = [n* − N + 1, n*]`, with `n* = ⌊(g − λ)/ε_p⌋`, contains an `n` with `δ(n) ∈ [δ(g+1), δ(g)]`. At that `n`, Construction B satisfies (S) at every rotation and (X), and

```text
g ≤ γ ≤ g + 1,   λ ≤ γ − ε_p n ≤ λ + 1.5,   ε_p n ≤ ρ₀ = m_0 ≤ γ,   γ − 1 ≤ log₂(x_min + 1) ≤ γ + Ψ̄,
Ψ̄ := log₂(1 + 2^{−3(L−1)}/(1 − 2^{−(2L−3)}) + 2^{−30}) = 1.874469… ≤ 1.87447 .
```

The window may sit anywhere below `n*` and above `3p + 40`, since the proof only uses `ε_p n + λ ≤ g` on `W`. Higher levels `g′ > g` work the same way: "every scale".

### 5.2 Proof

- **The window.** On `W`, `ε_p n ≤ g − λ`. The bottom satisfies `n* − N + 1 > 1/ε_p − N ≥ 1/(2ε_p) ≥ 3p + 40`, using `g − λ ≥ 1` and `N ≤ 1/(2ε_p)`. At `n ≥ 3p + 40`, `S > (L−1)n` gives `S ≥ p`, `S − p + 1 ≥ 21` and so `η ≤ 2^{−20}`, and `(L−1)(n − p) ≥ p + 1`, so (H0) holds.
- **The sweep.** `δ(n₀ + j) = δ(n₀) − jL mod 1`. So `N` consecutive `n` give a reflected translate of `{jL mod 1 : 0 ≤ j < N}`, with the same gaps. By the three-distance theorem in its two-length case (Sós 1958; Świerczkowski, Fund. Math. 46, 1958), at `N = q_k + q_{k−1}` the gaps are `θ_{k−1}` (`q_k` times) and `θ_k` (`q_{k−1}` times). `q_k θ_{k−1} + q_{k−1} θ_k = 1` was checked exactly, and the structure itself was checked exactly for `k ≤ 13` (`N ≤ 301,739`). The maximal gap is `θ_{k−1} ≤ ℓ`. A closed arc of length `ℓ` that contained no point would lie inside a gap longer than `ℓ`. So some `n ∈ W` lands in the arc, i.e. `g ≤ γ(n) ≤ g + 1`.
- **Hypotheses.** `γ ≥ g ≥ ε_p n + λ ≥ Γ′(p, n)`, since `η ≤ 2^{−20}`. Also `γ ≥ 2 + η` and `γ ≥ log₂(X₀+1) + 1`. §4 applies.
- **Brackets.** `γ − ε_p n ≤ g + 1 − ε_p(n* − N + 1) < λ + 1 + ε_p N ≤ λ + 1.5`. Next, `m_0 = ⌊γ − η⌋ ≥ 3`. At `p ≥ 10` and `n ≥ 1/(2ε_p)`, the tail term is `≤ 2^{−30}` (checked for `p ≤ 399`; it decreases super-exponentially after that), which gives `Ψ̄`.

∎

### 5.3 The period threshold `p₁(X₀)` (Part E)

| `X₀` | `1`–`16` | `2^5`, `2^6` | `2^7` | `2^8`–`2^12` | `2^13` | `2^14`, `2^15` | `2^16` | `2^17`–`2^20` | `2^30` | `2^40` | `2^50` | `2^60` | `5·2^60` | `2^70`, `2^71` | `2^100` | `2^200` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `p₁` | 10 | 14 | 16 | 22 | 24 | 26 | 27 | 36 | 50 | 65 | 80 | 94 | 98 | 110 | 159 | 309 |

Over the table, `p₁ − log_L X₀ ∈ [2.784, 10.629]` over every `j ≤ 200`. The excess comes from large partial quotients of `L`: the jump at `2^{17}` is `a_14 = 55`, where `q_13 = 190537` is followed by `q_14 = 10590737` (the record's indexing, 12.8.6.1). **Consistency with SdW:** at their `X₀ = 5·2^{60}` they prove no `m`-cycles for `m ≤ 75` (v1.44 §1.5). Their argument uses only the size facts of §1.2, so it applies to size-passers. A `p₁ ≤ 75` there would have been a contradiction. `p₁ = 98`. That is consistent, and it is a check on the construction, not an exclusion run. **What is not claimed:** a closed form for `p₁` uniform in `X₀`. That needs a bound on the partial quotients of `L` (badly-approximable, open) or an effective irrationality measure. With Rhin's measure via SdW Lemma 12 it would be `O(log X₀)` with a poor constant, and the measure's exact hypotheses were not held this session. Also not claimed: a matching *necessary* period threshold. Its shape is SdW's Lemma 10 (Crandall) mechanism. Computing it would be a per-period exclusion, which the stopping rules forbid.

## 6. The obstruction for the staircase as built

The brief asked: "If the staircase fails at the threshold, record the obstruction exactly." Two separate statements.

1. **At the canonical scale it does not fail.** Here `n ≈ L^p`, (H1) holds and the crash is a unit block. Any window there gives (S)+(X) at `γ ∈ [g, g+1]`: six runs at `X₀ ∈ {100, 1000, 4096}`. But `γ − ε_p n ∈ [7.19, 13.16]` grows like `log₂ X₀`. That family tests Corollary 5, not Lemma 7, and does not answer S.
2. **At the scale where Lemma 7 binds, crash depth 1 fails, provably.** That scale is `ε_p n ≈ log₂ X₀`. §3 (iii) gives `γ > L·ε_p n − (L−1) − log₂ p − o(1)` for any size-passer with a unit block. The family's ceiling is `γ ≤ ε_p n + λ + 1.5`. So no unit-block size-passer exists at any `γ` the family uses once `(L−1)ε_p n > λ + 2.09 + log₂ p`. The G5 table finds this from `X₀ = 2^{20}` (`p = 36`) on, at `p₁` and at `p₁ + 20`, through `2^{200}`. Below that, the necessity bound's `log₂ p` slack leaves crash-depth-1 undecided. The record's sufficient condition (H1) fails there anyway (83 of 95 runs).

Since `log₂ p` grows without bound, at fixed `X₀` and `p → ∞` the unit-block exclusion eventually stops applying. The precise statement is "excluded wherever `ε_p n/log₂ p` is large enough". The repair costs nothing: the same construction under (H1′) lands deep.

## 7. Relation to the two sources, exactly

### 7.1 Rozier 1991, p. 11

- **Anticipated, and not claimed:** the inequality. Lemme 4, `2^{ε_p M} − 2^p ≤ u_0`, is the trim (§3 (ii)). The minimax argument (§3 (iv)) and the real extremal `m_j = c·L^{j−1}`, `c = ε_p M`, are his, with the word "optimal" for the relaxed system.
- **What this adds:** an integer realisation meeting every rotation's exact size condition (S). Lemme 3 is one relaxed inequality per minimum against `U₀`, with the exits dropped. The family has Rozier's quantity `ρ = m_0 ∈ [ε_p n, ε_p n + λ + 1.5]`, attained at the first block in order from the minimum. The minimum sits at block 0 in all 95 runs, and `ρ = m_0` in all 95. The deep crash is what makes the integer profile Rozier's: the last block continues the geometric climb instead of collapsing to `1`. The family also brackets `x_min`: `log₂(x_min + 1) ∈ [ε_p n + λ − 1, ε_p n + λ + 1.5 + Ψ̄]`, measured `[2.87, 3.89] + ε_p n`.
- **Exactly what is not realised:** Lemme 4's own inequality is vacuous on the whole family. Its additive `2^p` exceeds `2^{ε_p n}`, because `ε_p n ≤ g − λ < p` wherever `p ≥ p₁`. So "Rozier's bound is attained" would be false as stated. What is attained is his minimax value, the content of his optimality remark.
- Rozier works at threshold `1` only. The `X₀` form is SdW's.

### 7.2 Simons–de Weger 2005, p. 69

- **Their sentence:** "We believe that Lemma 7 is almost sharp for the worst case, in the sense that at best we expect that the factor `m c_m` may be improved to a constant, but the exponential dependence on `m` … seems unavoidable."
- **Proved here, for size-only configurations meeting their hypotheses** (`a_i ≥ 1`, `x_i ≥ X₀`): at every `X₀ ≥ 1` and every `m = p ≥ p₁(X₀)`, there are configurations with `Λ ≥ 2^{−γ} ≥ 0.05405·2^{−ε_p n}`. This holds at every level `g ≥ 1 + max(log₂(X₀+1), λ)`, including the one where Lemma 7 overtakes Corollary 5. At the minimal level `ε_p n ≥ g − λ − 1/2`, so Lemma 7's bound is at most `c_p·2^{λ−1/2}` times Corollary 5's `p/X₀`. That factor tends to `√2` as `c_p → c_∞ = 2^{−1/(L−1)}`. The `1/(L−1)` in SdW's `c_∞` is the same one that sits in `λ = 1 + 1/(L−1) + 2^{−20}`. This is the crossover scale. At every higher level `g′ > g`, Lemma 7 is the operative bound.
  - (a) **The exponential dependence on `m` is attained.** A bound `Λ < C_p 2^{−ε′_p n}` valid at threshold `X₀` must have `(ε′_p − ε_p)·n ≤ log₂ C_p + 4.21` along the family.
  - (b) **The factor `m c_m` cannot be lowered below `0.054`.** Lemma 7's bound exceeds the family's `Λ` by a factor in `[34.9, 682.1]`, i.e. `[2.22, 23.35]·p` (all 95 runs). The theorem bounds it by `p c_p 2^{4.21}`.
- **Open, as SdW themselves leave it:** whether `m c_m` can be lowered *to* a constant. On our side this is the `log₂ p` in the necessity (§3 (i), (ii)). Part C shows that this `log₂ p` is genuinely attained by some configurations (repeated blocks), but at `n` far below the Lemma 7 scale. Nothing here decides it at the Lemma 7 scale.
- **Their quantifier, "for given `m` and `K`":** answered by the sandwich of §2 item 1. At given `(p, n)`, existence is decided by `γ(n) − max(ε_p n, log₂(X₀+1))` up to `(−log₂ p, L/(L−1) + η]`. Since `Λ` is a function of `n` alone, this is the whole of "the worst case for given `m` and `K`".
- **Not claimed:** that any of this bears on cycle *existence*. It is a statement about the reach of size arguments, exactly as 12.8.6 is.

## 8. Verification record

`experiments/staircase_x0_threshold.py`, fresh code, 2026-10-19. It imports nothing from `staircase_allp*.py`, `staircase_gamma_upper.py`, `uniform_trim.py` or `ceiling_novelty_check.py`; Construction B is transcribed from 12.8.6.2's statement. One command, about 3 minutes, reproduces the committed output:

```text
python experiments/staircase_x0_threshold.py > experiments/staircase_x0_threshold_output.txt
```

The committed output has **188 checks, 0 failures**. A second run of the same command was byte-identical modulo line endings (2026-10-19). Exact integers and rationals decide every size condition, threshold condition and witness. Floats appear only in reported logarithms and in margin-guarded comparisons, which print UNDECIDED rather than guess; none were undecided.

- **A. `L`:** enclosed to width `< 2^{−1380}` by an integer `atanh` series with explicit remainder; 399 certified partial quotients; signs cross-checked against exact `3^q` vs `2^p` at all 14 convergents with `q ≤ 2·10^5`; `q_k θ_{k−1} + q_{k−1} θ_k = 1` bracketed for `k ≤ 59`.
- **B. Algebra:** the `A_r` closed form, the crash identity, `Γ′₀(p) < L/(L−1)` (`p ≤ 159`, both ends of the `L` interval), and `Γ′`'s `n`-slope `= ε_p`, all checked in exact rationals.
- **C. Random configurations:** 30,000 with `q > 0`, of which 1,429 are size-passers and 548 have a unit block.
  - Rotation recurrence at every rotation of all 30,000.
  - Terras iteration and the product identity on 4,000.
  - Sandwich, exactly, on all 30,000.
  - Trim on all size-passers (minimum margin `1.0000`); unit-block bound on all unit-block passers (minimum margin `1.7776`).
  - Rozier minimax in every rotation order.
- **D. Sweep:**
  - The two-distance structure exactly at `k = 1..13`.
  - `δ(n)` decided at every `n ≤ 3,000,000`, with the longest run missing each theorem arc at most `N − 1` for all six `X₀`. Two runs meet the bound exactly: `52 = 53 − 1` at `X₀ = 10`, `358 = 359 − 1` at `X₀ = 100`.
  - Control: arcs of length `0.9 θ_{k−1}` are missed for longer (93, 664).
- **E. `p₁`:** `X₀ = 2^j`, `j ≤ 200`, with the monotone condition checked to `p₁ + 60`; `p₁(5·2^{60}) = 98 ≥ 76`; the tail term `≤ 2^{−30}` for `p ∈ [10, 399]`.
- **F. Construction end to end:** 95 runs at `X₀ ∈ {1, 10, 31, 100, 1000, 4096}`.
  - Coverage: every `p` from `p₁(X₀)` until `n* > 4.5·10^6` (`p` up to 32), plus 8 runs at higher levels. The largest is `n = 4,412,888` (`X₀ = 4096`, `p = 27`).
  - Each run checks: the witness inside the window; the shape; `R_0` by definition and `R_1, …, R_{p−1}` by the rotation recurrence, closing exactly back to `R_0` (all `R_r` by definition as well for `n ≤ 30,000`); all `p` conditions (S); (X); (H0) and (H1′); `Γ′ ≤ γ`; growth `T > A_r` and the crash term exactly in the deep case; `γ ∈ [g, g+1]`; `γ − ε_p n ∈ [λ, λ + 1.5]`; `ε_p n ≤ ρ₀ ≤ γ − η`; `Ψ₀ ≤ Ψ̄`; the sandwich; SdW Lemma 7 and Corollary 5 both hold; the trim.
  - Measured: `γ − ε_p n ∈ [2.7532, 3.8267]`; for `X₀ ≥ 6`, `γ − log₂(X₀+1) ∈ [1.0439, 1.9980]`; `log₂(x_min+1) − ε_p n ∈ [2.8704, 3.8925]`; `Ψ₀ ≤ 0.5027`.
  - Also: 6 (X′) runs and 6 canonical-scale runs.
- **G. Negative controls:**
  - G1, necessity bites: 3,142 `n` at `p = 8..16` with `γ(n) < ε_p n − log₂ p`; Construction B passes at 0.
  - G2, sufficiency is not necessity: 2 of 455 gap-region `n` pass.
  - G3, the threshold is load-bearing: 16 of 16 `X₀ = 1` witnesses fail `x_min ≥ 1024`.
  - G4, caps saturated: `+1` or `+2` depth on any climb block breaks a size condition, 273 of 273.
  - G5: the unit-block table of §6.

The check stops at `n ≈ 4.4·10^6` on big-integer cost. Constructions at `X₀ ≥ 2^{14}` are beyond it. That is a limit on the check, not on the theorem. The theorem's inputs at large `X₀` (the continued fraction, `N`, `p₁`) are certified to `X₀ = 2^{200}`.

## 9. What paper 1 v4 can say

Proposed wording for a sentence after the `thm:staircase` status paragraph, or in the v4 sharpness section:

> The sharpness extends to the threshold at which Simons and de Weger pose it. Every configuration with all cycle elements at least `X₀` has `γ > max(ε_p n, log₂(X₀+1)) − log₂ p`, with `ε_p = (log₂3 − 1)/((log₂3)^p − 1)`. Conversely, for every `X₀ ≥ 1` and every `p ≥ p₁(X₀)`, with `p₁(X₀)` computed from the continued fraction of `log₂ 3` (within `log_{log₂3} X₀ + 11` for every `X₀ = 2^j ≤ 2^{200}`; no uniform closed form is claimed), the staircase with its crash block continuing the climb meets every rotation's size condition with all elements `≥ X₀` and `γ ≤ max(log₂(X₀+1), 2.71) + 2`, at the scale `ε_p n ≥ log₂(X₀+1) − 2.21` where Lemma 7 of [SdW] is the operative bound. There `Λ ≥ 0.054·2^{−ε_p n}`. The exponential dependence on the number of local minima is attained, and the factor `m c_m` of [SdW, Lemma 7] can at best be lowered to a constant no smaller than `0.054`. The integer profile realises the real extremal of Rozier's optimality remark [Rozier 1991, p. 11] under every rotation's exact size condition. The record is `cycles.md` §12.8.7.

What v4 must **not** say:
- that the trim is new (it is Rozier 1991 / SdW 2005);
- that Rozier's Lemme 4 inequality is attained (it is vacuous in the range; the minimax value is what is attained);
- that SdW's "at best a constant" is settled (the `log₂ p` gap is open);
- that the unit-block staircase works at the threshold scale (it provably does not, from `ε_p n ≳ 8.2 + 1.71 log₂ p`);
- anything about exclusion.

## 10. For the main session

**`cycles.md`:** a new subsection 12.8.7 was added after 12.8.6 (no renumbering), with its own current-state clause and a one-line verification record. Nothing else in the page was touched. These are left for the main session:

- `cycles.md` front matter (`status`, `updated: 2026-10-19`) and the page's Current-state paragraph: one clause for 12.8.7.
- `index.md`: the resolver row for 12.8.7 and the status summary.
- `README.md` scoreboard: "constructed at every period" → "and at the size threshold `X₀`" (optional).
- `TOUR.md` dictionary: `x_r = 2^{m_r} R_r/q − 1` (block start = local minimum), against the brief's "rational cycle elements" gloss on `R_r/q` (§1.2).
- `publication.md` 12.8 line: the residue now includes the threshold form. The Rozier and SdW wording per §7.
- `paper/` v4 items per §9.
- `open-problems.md`: no entry posed the threshold question (searched), so no closure note. If wanted, a new entry: "Can SdW's `m c_m` be lowered to a constant at the Lemma 7 scale, i.e. can the `log₂ p` in 12.8.7.1 (i)–(ii) be removed for size-passers with `ε_p n ≥ log₂ X₀`?" It is stated so that closure is checkable. Whether it serves the uniform trim lemma enough to be posed under the stopping rules is the author's call.

**For the author to decide:**
1. Whether paper 1 v4 carries the threshold form (§9) and the deep-crash remark. It is a strengthening of Theorem 4.6's sharpness, not a correction.
2. Whether the canonical-scale family (§6, item 1) is mentioned at all, or only as the reason the threshold needs the rescaled family.
3. Whether to pose the `log₂ p` question (§10) as an open problem, or leave it as SdW's.

## 11. Scope and non-claims

- Size-only; no divisibility test run. No statement about any configuration being or not being a cycle.
- `p₁(X₀)` is explicit per `X₀` but has no proved closed form uniform in `X₀`. Below `p₁(X₀)` nothing is claimed in either direction.
- The two-distance theorem is cited (Sós; Świerczkowski) and checked for `k ≤ 13`. It was not re-proved.
- The unit-block exclusion holds only where `(L−1)ε_p n > λ + 2.09 + log₂ p`. Elsewhere crash depth 1 is undecided.
- (X′) is answered (§4.4), but it is not SdW's condition.
