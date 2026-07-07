---
status: periods 1 and 2 CLOSED (12.2 Steiner contact; 12.5 Simons–de Weger 2-cycle contact); general framework stated (12.1, 12.3); translation dividend recorded (12.4)
scope: new section 12 (post-monolith; first page with no monolith source)
updated: 2026-07-07
source: new material, 2026-07-07; builds on 9.8.4 (spine.md) and 11.8.7 (stage4.md)
---

> **Current state.** Cycles in reduced coordinates. The reduced cycle equation (12.1) reproduces the classical `2^K`-vs-`3^n` balance in four lines. Period 1 is completely classified (Theorem 12.2.3): the fixed-point equation reproduces Steiner's circuit theorem. Period 2 is completely classified (Theorem 12.5.3): the two-step elimination pair plus the size-trim lemma collapse the `n <= 20,000` search to eleven divisibility tests, all failing — matching the Simons–de Weger 2-cycle case with strikingly little apparatus. The open front is period `p >= 3` via the same elimination schema (12.5.5): the first place the program could exceed the classical results rather than match them.

# 12. Cycles in Reduced Coordinates

By Theorem `9.8.4`, projection by `R` is a bijection between nontrivial cycles of the odd Collatz map `T` and cycles of the reduced map `F` other than the fixed point `(1,1)`. This section studies `F`-cycles directly. Throughout, a period-`p` cycle is a sequence of valid states `(ω_t, d_t)`, `t ∈ Z/pZ`, with `F(ω_t, d_t) = (ω_(t+1), d_(t+1))`, and each step carries its data `s_t`, `σ_t = v_2(C_t)`, `a_t = v_3(C_t)`, and entry depth `m_(t+1) = σ_t - s_t`.

## 12.1. The Reduced Cycle Equation

**Proposition 12.1.1 (cycle product equation).** Let `(ω_t, d_t)` be a period-`p` cycle with `n = Σ_t m_t` and `K = Σ_t σ_t = Σ_t s_t + n`. Then

```text
2^K = 3^n · Π_t (1 + ε_t),      ε_t = (2^(s_t) - 1) / (3^(d_t) ω_t) > 0.
```

**Proof.** The step identity `2^(σ_t) 3^(a_t) ω_(t+1) = C_t = 3^(d_t) ω_t + (2^(s_t) - 1)` multiplied around the cycle gives `2^K 3^(Σ a_t) Π ω_t = Π 3^(d_t) ω_t (1 + ε_t)`. The `ω`-products cancel cyclically, and `Σ d_t = Σ (m_(t+1) + a_t) = n + Σ a_t` cancels the `3`-powers down to `3^n`. ∎

**Corollary 12.1.2 (size balance).** `3^n < 2^K`, and

```text
0 < K·log 2 - n·log 3 = Σ_t log(1 + ε_t) < Σ_t ε_t < Σ_t 1/x_t,
```

where `x_t = x_exit(ω_t, d_t)` are the block exits. In particular, if every element of the cycle exceeds `X`, then `0 < K·log 2 - n·log 3 < p/X`: large cycles force the linear form `K log 2 - n log 3` to be abnormally small, which is the regime of effective Baker bounds. This is the classical cycle-exclusion engine (`11.8.3.11`), obtained here in four lines from the reduced step identity — the reduced coordinates carry it natively.

## 12.2. Period 1: Complete Classification

**Proposition 12.2.1 (fixed-point equation).** `(ω, d)` is a fixed point of `F` if and only if, writing `m = σ - s >= 1` and `a = v_3(C)` (so `d = m + a`),

```text
ω · 3^a · (2^(s+m) - 3^m) = 2^s - 1.
```

**Proof.** Fixed point means `C = 2^σ 3^a ω` and `d = σ - s + a`. Substituting `C = 3^d ω - 1 + 2^s` and `d = m + a` gives the displayed equation. Conversely, a solution with `m >= 1`, `s >= 1`, `3 ∤ ω` reconstructs a valid fixed state: `A = 2^s(2^m 3^a ω - 1)` has `v_2 = s` exactly (the bracket is odd since `m >= 1`), and `C = 2^(s+m) 3^a ω` has `v_2 = s + m`, `v_3 = a` exactly. ∎

**Lemma 12.2.2 (window: at most one candidate `s` per `m`).** For the equation of `12.2.1` to have a solution, `q = 2^(s+m) - 3^m` must be positive and at most `2^s - 1`. Equivalently

```text
(3/2)^m < 2^s <= (3^m - 1)/(2^m - 1),
```

and the ratio of the window's endpoints is `(1 - 3^(-m))/(1 - 2^(-m)) < 2` for every `m >= 1`. Hence the window contains at most one power of `2`: for each `m` there is at most one candidate exponent `s`, which must additionally satisfy the divisibility `q | 2^s - 1`. ∎

**Theorem 12.2.3 (period-1 classification).** The only fixed point of `F` is `(1, 1)`.

**Proof.** By Lemma `12.2.2` and exact integer computation, the unique candidate `s` fails the divisibility `q | 2^s - 1` for every `2 <= m <= 20,000`, while `m = 1` forces `s = 1`, `q = 1`, `ω 3^a = 1`, the trivial solution (`12.2.4`). For all `m` unconditionally: by Theorem `9.8.4`, a nontrivial fixed point of `F` corresponds to a `T`-cycle tiled by a single block — one rising phase (`m - 1` odd steps) followed by one falling cascade — that is, a *circuit* in the classical sense. The nonexistence of nontrivial circuits is Steiner's theorem, proved by exactly the Baker-type analysis that Corollary `12.1.2` shows this equation to inhabit. [#TODO cite: R. Steiner, *A theorem on the Syracuse problem* (1977).] ∎

**Remark (what the benchmark shows).** This is the program's first contact with an external result, and the contact is exact: the period-1 case of the reduced cycle problem *is* the circuit problem, the fixed-point equation drops out of the block algebra in one substitution, and the window lemma — which reduces the two-parameter search to one divisibility test per `m` — is elementary here. The formalism reproduces the classical result with less apparatus; it does not yet strengthen it. The genuine test of leverage is whether the congruence machinery below prunes higher periods faster than the classical `m`-cycle analysis.

**Remark 12.2.4 (numerical record).** Exact big-integer search, `m <= 20,000`: the unique solution is `(m, s, a, ω) = (1, 1, 0, 1)`, the trivial fixed point. Independent direct search — iterating `F` from all valid states `ω < 3,000`, `d <= 32` with cycle detection — finds only the cycle `{(1,1)}`. Code: `experiments/period1_cycles.py`.

## 12.3. The Stratum-Sequence Congruence System

For period `p >= 2`, the reduced machinery imposes, per hypothesized stratum sequence `(s_t, σ_t, a_t)_(t ∈ Z/pZ)`, a finite closed system of congruences:

1. **Chain conditions (exact):** `d_(t+1) = (σ_t - s_t) + a_t` with every `d_t >= 1`, closing cyclically.
2. **Anchor conditions (exact):** on lifting steps, `s_t = 2 + v_2(d_t - M(ω_t))` forces `d_t ≡ M(ω_t) (mod 2^(s_t - 2))` and `d_t ≢ M(ω_t) (mod 2^(s_t - 1))`; on non-lifting steps, `s_t ∈ {1, 2}` pins the residue-parity class of `(ω_t, d_t)` (`11.8.1.3.1`).
3. **Window propagation (exact):** the depth-`k` window of `(ω_t, d_t)` determines `ω_(t+1) mod 2^(k+2)` (Lemmas `11.8.7.2.2`–`11.8.7.2.3`), so the residues `ω_t mod 2^j` around the walk are not independent unknowns: the whole closed walk is determined by the residue data of one state plus the stratum sequence, and closure (`ω_p ≡ ω_0`, `d_p = d_0`) is a finite congruence check.
4. **Size condition (exact):** the product equation of `12.1.1`, which pins `Σ σ_t` near `n·log_2 3 + n` and prices every deep `s_t` against the cycle's element sizes.

A period-`p` cycle exists only if some stratum sequence admits a solution of the full system. Since deep strata are constrained by condition `4` and the number of shallow stratum sequences is finite for bounded `Σ σ_t`, this is a finite computation per `(p, Σσ)` box — a pruning engine whose efficiency relative to the classical analysis is exactly what remains to be measured. Period 2 is now carried out in full in `12.5`, and the pruning is severe: the entire `n <= 20,000` search collapses to eleven divisibility tests.

## 12.4. Translation Dividend: `m`-Cycles

A block with entry depth `m_t >= 2` contributes exactly one rising phase (`m_t - 1` odd steps) and one local maximum to the `T`-trajectory; a block with `m_t = 1` is a pure fall that merges into the preceding descent. Hence under the bijection of `9.8.4`, a period-`p` reduced cycle is precisely an *`m`-cycle* in the sense of Simons–de Weger with

```text
m = #{ t : m_t >= 2 }  <=  p.
```

Every known `m`-cycle exclusion therefore transfers verbatim: if `m`-cycles are excluded for `m <= M_0`, then no reduced cycle has `#{t : m_t >= 2} <= M_0`; in particular no cycle of period `p <= M_0` exists, and any cycle whatsoever must contain more than `M_0` deep-entry blocks.

## 12.5. Period 2: Complete Classification

**Proposition 12.5.1 (two-step elimination).** Let `(ω_0, d_0), (ω_1, d_1)` be a period-`2` cycle with shallow data `s_0, s_1 >= 1` and entry depths `m_0, m_1 >= 1` (so `d_0 = m_0 + a_1`, `d_1 = m_1 + a_0`), and set `n = m_0 + m_1`, `K = s_0 + s_1 + n`, `q = 2^K - 3^n`. Then `q > 0` and

```text
ω_0 · 3^(a_1) · q = R_0 := 3^(m_1)(2^(s_0) - 1) + 2^(s_0 + m_1)(2^(s_1) - 1),
ω_1 · 3^(a_0) · q = R_1 := 3^(m_0)(2^(s_1) - 1) + 2^(s_1 + m_0)(2^(s_0) - 1).
```

In particular `q` divides both `R_0` and `R_1`, and `q <= min(R_0, R_1)`.

**Proof.** Unrolling two steps of the identity `2^(σ_t) 3^(a_t) ω_(t+1) = 3^(d_t) ω_t + (2^(s_t) - 1)` gives, for *any* state (no cycle assumption),

```text
2^(σ_0 + σ_1) 3^(a_0 + a_1) ω_2 = 3^(d_0 + d_1) ω_0 + 3^(d_1)(2^(s_0) - 1) + 2^(σ_0) 3^(a_0)(2^(s_1) - 1),
```

verified numerically on `3,000` random orbit pairs with zero failures. Imposing closure `ω_2 = ω_0`, substituting `d_0 + d_1 = n + a_0 + a_1`, `d_1 = m_1 + a_0`, `σ_0 = s_0 + m_1`, and cancelling `3^(a_0 + a_1)` yields the first equation; the second is its cyclic image. Positivity of `q` follows since the right side is positive. Conversely, any solution in positive integers with `ω_t` odd, `3 ∤ ω_t` reconstructs a genuine period-`2` cycle: as in `12.2.1`, the valuations `s_t`, `σ_t`, `a_t` are automatic. ∎

**Lemma 12.5.2 (size trim).** For any period-`2` cycle,

```text
0 < K·log 2 - n·log 3 < 2^(6 - n/5).
```

**Proof sketch.** From `q <= R_0` and `q <= R_1`, `q^2 <= R_0 R_1`. Expanding, `R_0 R_1 < 2^(S+2) · (3^n + 3^(m_1) 2^(m_0+s_0) + 3^(m_0) 2^(m_1+s_1) + 2^K)` with `S = s_0 + s_1`. Each of the four terms is at most `2^(K+S+2)` (the mixed terms via `3^m < 2^(1.585 m)` and `0.585 n < S + 2`, which follows from `3^n < 2^K`). Hence `q <= 2^((2S + K)/2 + 3)`, so `q / 2^K <= 2^((S - n)/2 + 3) <= 2^(5 - n/5)` using `S <= 0.585 n + 1`, and `K log 2 - n log 3 = -log(1 - q/2^K) < 2 q/2^K` once `q/2^K < 1/2` (smaller `n` are covered by the search below). ∎

**Theorem 12.5.3 (period-2 classification).** No nontrivial period-`2` cycle of `F` has `n = m_0 + m_1 <= 20,000` (exact computation). For `n > 20,000`, Lemma `12.5.2` requires `K log 2 - n log 3 < 2^(6 - n/5)`, which contradicts any effective irrationality measure for `log 3 / log 2` beyond an explicit threshold far below `20,000`; hence `F` has no period-`2` cycles at all, i.e., the reduced system has no `2`-block cycles. [#TODO pin measure and threshold: effective irrationality measures for log 3/log 2 (Rhin-type); this matches the `2`-cycle case of Simons–de Weger.]

**Remark 12.5.4 (numerical record; pruning power).** The raw parameter space for `n <= 20,000` — quadruples `(m_0, m_1, s_0, s_1)` with `m_0 + m_1 = n`, `s_0 + s_1 = K - n` — has on the order of `10^12` cells. The window prune (`q` is pinned by `(n, K)` with no free exponent to slide, so `q <= R_t` bounds `min(m_0, m_1)` from below) leaves open windows at only `19` values of `n` — the small range `n <= 17` plus the `log_2 3` near-convergents `n = 20, 22, 29` — and exact size tests pass for only `11` quadruples in the entire range. All fail divisibility except the degenerate `(m_0, m_1, s_0, s_1) = (1, 1, 1, 1)`, which reconstructs the fixed point `(1,1)` twice, not a `2`-cycle. Search and identity checks: `experiments/period2_cycles.py`. (Method note: the first run of the search carried an off-by-one in the power of `3`; it was caught by an internal consistency check on the `s`-split and corrected before this record. The recorded run passes the sanity assertions.)

**Remark 12.5.5 (what the second benchmark point shows).** The two-block case lands the same way as period 1: the reduced coordinates compress the problem to a single displayed elimination pair plus a window argument, reproducing the known `2`-cycle exclusion with strikingly little apparatus — eleven divisibility tests where the classical analysis runs lattice reduction. The schema visibly extends: for period `p`, the elimination yields `p` cyclic equations `ω_t · 3^(·) · (2^K - 3^n) = R_t` with `R_t` explicit in the `2p` shallow parameters, and the same double-sided size trim applies. Whether the reduced pruning stays this sharp as `p` grows — where Simons–de Weger's analysis becomes heavy — is now a concrete, testable question, and it is the first place the program could *exceed* the classical results rather than match them.
