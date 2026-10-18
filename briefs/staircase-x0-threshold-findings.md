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
