---
status: periods 1, 2, 3 CLOSED; uniform trim question RESOLVED (12.8: exists, exponentially weak, sharp at verified instances); all-p sharpness ASSESSED not proved, evidence extended to floor grade (12.8.6); cycle front PARKED per stopping rules
scope: new section 12 (post-monolith; first page with no monolith source)
updated: 2026-07-16
source: new material; builds on 9.8.4 (spine.md) and 11.8.7 (stage4.md)
---

> **Current state.** Cycles in reduced coordinates. Periods 1, 2, and 3 are completely classified: no nontrivial cycles (12.2.3, 12.5.3, 12.7.5). The uniform-trim question is resolved (12.8): a trim uniform in `p` exists (12.8.1) and gives effective finiteness at every period (12.8.2), but its constant degrades like `1.585^(-p)`, and the staircase family (12.8.3) shows size-counting can do no better at the two periods where it was originally checked. Whether that exponential weakness is intrinsic at *every* period (the published paper's `thm:staircase` hedge) is calibrated further at floor grade (12.8.6, 2026-07-16): an explicit per-period construction recipe plus a bounded correction algorithm produce verified instances for `p ∈ {2,...,21} ∪ {23}`, with a combinatorial obstruction precisely located at `p = 22`; the all-`p` claim remains assessed, not proved. The crossover plan is therefore withdrawn and the cycle front is **parked** (12.8.5, unaffected by 12.8.6): the residual content of cycle exclusion is anchor-walk rigidity, the same front as Stage 4. The staircase — a divergent-orbit profile bent into a loop — is evidence the two halves of the residual difficulty are one problem (12.8.4).

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

**Proof.** By Lemma `12.2.2` and exact integer computation, the unique candidate `s` fails the divisibility `q | 2^s - 1` for every `2 <= m <= 20,000`, while `m = 1` forces `s = 1`, `q = 1`, `ω 3^a = 1`, the trivial solution (`12.2.4`). For all `m` unconditionally: by Theorem `9.8.4`, a nontrivial fixed point of `F` corresponds to a `T`-cycle tiled by a single block — one rising phase (`m - 1` odd steps) followed by one falling cascade — that is, a *circuit* in the classical sense. The nonexistence of nontrivial circuits is Steiner's theorem, proved by exactly the Baker-type analysis that Corollary `12.1.2` shows this equation to inhabit. (R. P. Steiner, *A theorem on the Syracuse problem*, Proc. 7th Manitoba Conf., 1977.) ∎

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

**Theorem 12.5.3 (period-2 classification).** No nontrivial period-`2` cycle of `F` has `n = m_0 + m_1 <= 20,000` (exact computation). For `n > 20,000`, Lemma `12.5.2` requires `K log 2 - n log 3 < 2^(6 - n/5)`, which contradicts the effective bound below; hence `F` has no period-`2` cycles at all, i.e., the reduced system has no `2`-block cycles.

**Measure, pinned.** G. Rhin's effective bound (*Approximants de Padé et mesures effectives d'irrationalité*, Progr. Math. 71, Birkhäuser 1987, p. 160), applied exactly as in Simons–de Weger (2005, *Theoretical and computational bounds for m-cycles of the 3n+1-problem*, Acta Arith. 117, Lemma 12, `u_0=0, H=u_1=K+L, u_2=-K` in their notation — their `K` is our `n`, their `K+L` is our `K`) gives, unconditionally,

```text
K log 2 - n log 3 > exp(-13.3·(0.46057 + log n)).
```

At `n = 20,001` this is `> 2^(-198.9)`, while the lemma's requirement is `< 2^(6 - 20001/5) = 2^(-3994.2)` — a contradiction by `~3795` bits, checked numerically (`python`, `2026-07-12`). The threshold is not "far below 20,000" in a hand-waved sense: it is crossed by orders of magnitude at `n = 20,000` itself, so no case is left unaccounted for between the exact search and this bound.

**Remark 12.5.4 (numerical record; pruning power).** The raw parameter space for `n <= 20,000` — quadruples `(m_0, m_1, s_0, s_1)` with `m_0 + m_1 = n`, `s_0 + s_1 = K - n` — has on the order of `10^12` cells. The window prune (`q` is pinned by `(n, K)` with no free exponent to slide, so `q <= R_t` bounds `min(m_0, m_1)` from below) leaves open windows at only `19` values of `n` — the small range `n <= 17` plus the `log_2 3` near-convergents `n = 20, 22, 29` — and exact size tests pass for only `11` quadruples in the entire range. All fail divisibility except the degenerate `(m_0, m_1, s_0, s_1) = (1, 1, 1, 1)`, which reconstructs the fixed point `(1,1)` twice, not a `2`-cycle. Search and identity checks: `experiments/period2_cycles.py`. (Method note: the first run of the search carried an off-by-one in the power of `3`; it was caught by an internal consistency check on the `s`-split and corrected before this record. The recorded run passes the sanity assertions.)

**Remark 12.5.5 (what the second benchmark point shows).** The two-block case lands the same way as period 1: the reduced coordinates compress the problem to a single displayed elimination pair plus a window argument, reproducing the known `2`-cycle exclusion with strikingly little apparatus — eleven divisibility tests where the classical analysis runs lattice reduction. The schema visibly extends: for period `p`, the elimination yields `p` cyclic equations `ω_t · 3^(·) · (2^K - 3^n) = R_t` with `R_t` explicit in the `2p` shallow parameters, and the same double-sided size trim applies. Whether the reduced pruning stays this sharp as `p` grows — where Simons–de Weger's analysis becomes heavy — is now a concrete, testable question, and it is the first place the program could *exceed* the classical results rather than match them.

**Method note (K-completeness, added after 12.6).** The searches of `12.5.4` and `12.7` take `K = ⌈n·log_2 3⌉`. That this loses no generality is not automatic — `K = Σ s_t + n` could a priori exceed the ceiling — and is supplied by the ceiling lemma `12.6.2`: any cycle with larger `K` contains an odd exit value below `p/ln 2`, and for `p <= 5` all such values (`1, 3, 5, 7`) reach `1` by direct iteration. The period-2 search was run before this lemma was isolated; the lemma retroactively completes its proof.

## 12.6. The General Elimination and the Ceiling Lemma

**Proposition 12.6.1 (period-`p` elimination).** Let `(ω_t, d_t)`, `t ∈ Z/pZ`, be a period-`p` cycle with entry depths `m_t` and exit valuations `s_t`, and let `n = Σ m_t`, `K = Σ s_t + n`, `q = 2^K - 3^n`. Then for every rotation `r`,

```text
ω_r · 3^(a_(r-1)) · q = R_r := Σ_(t=0)^(p-1) 3^(M_t) · 2^(S_t) · (2^(s_t) - 1),
```

where, reading indices in rotation order starting at `r`: `M_t = Σ_(j>t) m_j` and `S_t = Σ_(j<t) σ_j`. In particular `q > 0` divides all `p` numbers `R_r`, and `q <= min_r R_r`.

**Proof.** Unrolling the step identity `p` times gives, for any state, `ω_p · 2^(Σσ) 3^(Σa) = 3^(Σd) ω_0 + Σ_t 3^(D_t + A_t) 2^(S_t) (2^(s_t) - 1)` with `D_t = Σ_(j>t) d_j`, `A_t = Σ_(j<t) a_j` — verified numerically for `p = 3, 4, 5` on random orbits, zero failures. Imposing closure and substituting `d_j = m_j + a_(j-1)` gives `D_t + A_t = M_t + Σ a - a_(p-1)`; cancelling `3^(Σa - a_(p-1))` yields the displayed equation, and rotations give the rest. Positivity: the right side is positive. ∎

**Remark (sanity identity).** For the trivial cycle traversed as a fake period-`p` cycle (`m_t = s_t = 1` for all `t`), the formula gives `R = Σ_t 3^(p-1-t) 4^t = 4^p - 3^p = q` exactly, matching `ω·3^a = 1` — confirmed computationally for `p ∈ {1, 2, 3, 4, 7}`.

**Lemma 12.6.2 (ceiling forcing).** If a period-`p` cycle has `K > ⌈n·log_2 3⌉`, then some block exit satisfies `x_exit < p / ln 2 < 1.443·p`.

**Proof.** `K` above the ceiling gives `2^K / 3^n >= 2`, so by the cycle product equation (`12.1.1`) `Π (1 + ε_t) >= 2`, so some `1 + ε_t >= 2^(1/p)`, hence `ε_t >= 2^(1/p) - 1 >= (ln 2)/p`. Then `3^(d_t) ω_t <= p(2^(s_t) - 1)/ln 2`, and `x_exit,t = (3^(d_t) ω_t - 1)/2^(s_t) < p/ln 2`. ∎

**Corollary 12.6.3 (`K` is the ceiling, unconditionally for `p <= 5`).** For `p <= 5` the bound gives an odd exit `<= 7`; the `T`-orbits of `1, 3, 5, 7` reach `1` by direct iteration, so no nontrivial cycle contains them. Hence every nontrivial cycle of period `p <= 5` has `K = ⌈n·log_2 3⌉`. For general `p` the same conclusion holds whenever `p/ln 2` is below the exhaustively verified range of the conjecture, i.e., for all `p` of any conceivable relevance. (D. Barina, *Improved verification limit for the convergence of the Collatz conjecture*, J. Supercomputing, 2025: all `n < 2^71` converge.)

**Remark (where the trivial cycle lives).** The trivial cycle itself has `K = 2p = ⌈p·log_2 3⌉ + 1` — *above* the ceiling. It is exactly the tiny-element case the lemma routes to, which is a satisfying consistency check: the ceiling searches below never see it, and never need to.

## 12.7. Period 3: Classification to `n <= 20,000`

**Theorem 12.7.1.** No nontrivial period-`3` cycle of `F` has `n = m_0 + m_1 + m_2 <= 20,000`.

**Proof.** By Corollary `12.6.3` (unconditional at `p = 3`), `K = ⌈n·log_2 3⌉`. The exact search then proceeds per `n` with two proved reductions. *Box:* writing `γ = K - log_2 q`, every block satisfies `m_t <= max(0.3691·n + 0.631·γ, 2.41·γ) + O(1)` — each rotation `r` needs some term of `R_r` to reach `q`, and the three term-shapes (`3`-heavy first term, mixed middle term, `2`-heavy last term) each force this bound on the rotation's leading block. *Budget:* summing the per-rotation requirements over the `s`-composition budget `Σ s_t = S` shows candidates require `γ >= 0.098·n - O(1)`, an exponentially strong near-convergent condition on `n·log_2 3` that fails for every `n ∈ (99, 20,000]`. The `76` surviving `n` were enumerated in full: `886` compositions reached exact evaluation, `51` passed the size test `q <= min_r R_r`, and none passed the triple divisibility `q | R_0, R_1, R_2`. ∎

**Remark 12.7.2 (verification record).** Search and audits in `experiments/period3_cycles.py` (2026-07-07). The pruning constants were slack-padded, and audited: `4,798` random cells sampled from the skipped region and from just outside the box boundary all fail the exact size test `min_r R_r >= q`. Two constant errors in the first filter derivation (a one-small-block escape lowering `0.138` to `0.098`, and a missing second branch in the box bound) were caught during this session's soundness review and corrected before this record; the corrected run enlarged the treated set from `62` to `76` values of `n` and changed no outcomes.

**Remark 12.7.3 (scaling picture and honest scope).** Growth across periods is mild: candidate `n` values `19 → 76`, exact evaluations `11 → 886` from `p = 2` to `p = 3`, against a raw space growing by a factor `~n·S`. The engine — ceiling lemma, box, budget filter, divisibility — is `p`-generic, and running `p = 4, 5` is now an engineering exercise. By the translation of `12.4`, all `p <= 68` remain subsumed by Simons–de Weger, so the schema's claim is efficiency and self-containedness, not yet new exclusions. The crossover target is `p > 91` — beyond the current `m`-cycle record — where the per-`n` collapse observed here, if it persists, would produce genuinely new results with modest computation. (Current record: C. Hercher, *There are no Collatz-m-Cycles with m ≤ 91*, arXiv:2201.00406, 2022/23.)

**Lemma 12.7.4 (period-3 trim).** Any nontrivial period-`3` cycle satisfies, with `γ = K - log_2 q`,

```text
γ > 0.1157·n - 2,      equivalently      0 < K - n·log_2 3 < 2^(3 - 0.115·n)   for n >= 26.
```

**Proof.** For each rotation `r`, `q <= R_r < 3·2^(e_r)` with `e_r` the largest of the three term exponents, so one of three routes holds: (A_r) `s_r > S - 0.585n + log_2 3·m_r - γ - 1.585` (first term dominates), (B_r) `s_r + s_(r+1) > S + m_r - 0.585·m_(r+2) - γ - 1.585` (middle term), or (C_r) `m_r < γ + 1.585` (last term). Both (A) and (B) imply the unified pair bound `s_r + s_(r+1) > S - 0.585n + log_2 3·m_r - γ - 2.2`, since (B)'s excess over it is `0.585·m_(r+1) + 0.6 > 0`. Now split by the number of (C)-rotations (tiny leading blocks). *None:* summing the pair bounds over the three rotations counts each `s_j` twice: `2S > 3S - 0.17n - 3γ - 6.6`, and with `S > 0.585n - 1` this gives `γ > 0.138n - 2.2`. *One* (block `c`): the other two pair bounds sum to at most `2S`: `0 > 0.415n - log_2 3·m_c - 2γ - 4.4` with `m_c < γ + 1.585`, giving `γ > 0.1157n - 2`. *Two:* the big block has `m > n - 2γ - 3.2` and its rotation's pair bound is at most `S - 1`, giving `γ > 0.24n - 1.5`. *Three:* `n < 3γ + 5`. The minimum over cases is the stated bound; the equivalent `λ`-form uses `K - n·log_2 3 = -log_2(1 - 2^(-γ)) < 2^(1-γ)` for `γ >= 1`. ∎

**Theorem 12.7.5 (period-3 classification, complete).** `F` has no nontrivial period-`3` cycles: the reduced system has no `3`-block cycles.

**Proof.** For `n <= 20,000`, Theorem `12.7.1`. For `n > 20,000`, Lemma `12.7.4` demands `0 < K - n·log_2 3 < 2^(3 - 0.115n) < 2^(-2297.1)` at `n = 20,001`, which contradicts G. Rhin's effective bound (pinned at `12.5.3`: `K log 2 - n log 3 > exp(-13.3·(0.46057+log n))`, giving `> 2^(-198.9)` at `n = 20,001`) by `~2098` bits. This is the `3`-cycle analogue of Simons–de Weger's own Lemma 12, and the same numeric check (`2026-07-12`) confirms it closes every `n > 20,000`, since the gap only widens as `n` grows (the trim's exponential term dominates Rhin's logarithmic one). ∎

**Remark 12.7.6 (verification; subsumption).** The trim lemma was checked against every composition passing the exact size test in the search range: all `51` size-passers satisfy `γ > 0.1157n - 2`, worst margin `+3.1` bits (at `n = 6`, balanced blocks). Code: `experiments/period3_cycles.py` (trim section). Two structural notes: the lemma's proof nowhere assumes `K = ⌈n log_2 3⌉` — for `K` above the ceiling `γ < 1`, so the lemma itself excludes `n >= 26` there, subsuming the ceiling lemma at `p = 3`; and the binding case (one tiny block) is exactly the configuration the corrected search filter guards, so the search constant `0.098` sits safely below the proved `0.1157`.

## 12.8. The Uniform Trim: Resolution of the Question

This section resolves the uniform-in-`p` trim question posed in `12.7.3` and in the program strategy (README): a uniform trim **exists** (Theorem `12.8.1`), its constant degrades **exponentially** in `p`, and that degradation is **intrinsic** — a explicit family of configurations shows size-counting arguments cannot do better (Remark `12.8.3`). The strategic consequence is recorded in `12.8.5`.

Throughout, `γ = K - log_2 q` and `γ' = γ + log_2 p`. For an arc `A` of consecutive blocks define the weight `w(A) = (log_2 3 - 1)·m(A) - s(A)` — its `m`-mass at exchange rate `0.585`, minus its `s`-mass.

**Theorem 12.8.1 (uniform trim, all `p`).** Every nontrivial period-`p` cycle of `F` satisfies

```text
γ + log_2 p  >  0.585·n / (1.585^p - 1).
```

**Proof.** For each rotation `r`, `q <= R_r < p·2^(max_t e_t)`, and the exact exponent identity `e_t - K = (log_2 3 - 1)·M_t - m_r - Σ_(j>t) s_j` turns this into: for every block `r`,

```text
m_r < γ' + Φ_r,        Φ_r = max( 0, max { w(A) : arcs A ending at block r-1 } ).
```

The arc maxima satisfy the cyclic recursion `Φ_r = max(0, Φ_(r-1) + w_(r-1))` with `w_j = 0.585·m_j - s_j`. Since `q > 0` gives `2^K > 3^n`, the total weight `Σ w_j = 0.585n - S` is negative, so the recursion resets somewhere: `Φ_(r_0) = 0`. Walking forward from the reset with `T_j` the partial `m`-sums and using `Φ <= 0.585·T` termwise, the block bound gives `T_j < (log_2 3)·T_(j-1) + γ'`, hence `n = T_(p-1) < γ'·(1.585^p - 1)/0.585`. ∎

**Corollary 12.8.2 (uniform effective finiteness).** Combined with G. Rhin's effective bound (pinned at `12.5.3`), Theorem `12.8.1` bounds `n` explicitly for every period: any period-`p` cycle has `n <= n_0(p)`, the unique solution (in `n`) of

```text
0.585·n / (1.585^p - 1)  =  log_2(p) + (p + 13.3·(0.46057 + log n)) / log 2.
```

Cycle exclusion at every single period is therefore a finite, explicitly bounded computation — uniformly in `p`.

**Proof.** Write `q = 2^(K-γ)` (the definition of `γ = K - log_2 q`, `12.8`) and `Λ = K log 2 - n log 3` (Rhin's linear form, `12.5.3`). Since `2^K = 3^n + q` (`12.1.1`), `Λ = log(1 + q/3^n)`. Using `log(1+x) < x` for `x > 0`, and `q/3^n = 2^(K - γ - n log_2 3) = 2^(Λ/log2 - γ)` (because `Λ/log 2 = K - n log_2 3` exactly):

```text
Λ  <  2^(Λ/log2 - γ).                                                              (i)
```

By Corollary `12.1.2`, `Λ < Σ_t 1/x_t <= p` unconditionally (every `x_t >= 1`), so `Λ/log 2 < p/log 2`; substituting into `(i)` (the right side is increasing in its exponent):

```text
Λ  <  2^(p/log2 - γ)  =  exp(p - γ·log 2).                                          (ii)
```

Combining `(ii)` with Rhin's lower bound `Λ > exp(-13.3(0.46057+log n))` (`12.5.3`) gives, for any period-`p` cycle,

```text
γ  <  (p + 13.3·(0.46057 + log n)) / log 2.                                        (iii)
```

But Theorem `12.8.1` forces `γ > 0.585n/(1.585^p-1) - log_2 p` for every such cycle. When the trim's lower bound on `γ` meets or exceeds `(iii)`'s upper bound — i.e. at and beyond the `n` solving the displayed equation — no `γ` can satisfy both, a contradiction; hence no cycle with that `n` exists. ∎

**Verification.** Solved numerically (`python`, this session) for representative periods, and checked that the contradiction persists (widens) for all `n` beyond the threshold, not just nearby it — `n_0(p)` is a genuine ceiling, not a local artifact:

```text
p =   4:  n_0 ~ 1.41 * 10^3
p =   5:  n_0 ~ 2.61 * 10^3
p =  10:  n_0 ~ 3.88 * 10^4
p =  20:  n_0 ~ 5.84 * 10^6
p =  50:  n_0 ~ 1.14 * 10^13
p =  91:  n_0 ~ 2.99 * 10^21
p =  92:  n_0 ~ 4.78 * 10^21
p = 100:  n_0 ~ 2.05 * 10^23
```

This is a genuine `n_0(p)`, not merely the `O(p·1.585^p)` shape — the ratio `n_0(p) / (p·1.585^p)` is `~39` at `p=10`, falling to `~20` by `p=100` (still decreasing; the extra factor over `1.585^p` alone comes from Rhin's own `13.3·log n` cost, and `log(n_0(p)) ~ p·log(1.585)`, so the self-reference in `(iii)`'s `log n` term is consistent, not circular — no closed-form limiting constant is claimed here, only the checked table above). At `p = 91` the crossover target, `n_0(91) ~ 3*10^21` — far beyond any feasible search, consistent with `12.8.5`'s withdrawal of the crossover plan; this corollary's contribution is that the withdrawal is now backed by a checked number, not just a shape.

**Remark 12.8.3 (sharpness: the staircase family).** The exponential loss is not an artifact. Consider blocks growing geometrically at ratio `≈ log_2 3` with shallow exits (`s = 1`), closed by one block of tiny depth and enormous exit valuation — a long climb and a single crash. Such configurations satisfy *every* rotation's exact size condition `q <= R_r` with `γ` far below any polynomial-in-`p` trim: at `p = 7`, `n = 94`, the staircase `m = (4, 7, 9, 15, 23, 35, 1)` passes all seven size tests with `γ = 6.74`, where the period-3 constant `0.1157n - 2 = 8.9` would forbid it; `84` further staircase size-passers exist at `p = 6` alone. All fail the divisibility conditions `q | R_r` — none is a cycle — and all respect Theorem `12.8.1` (worst ratio `0.23`). Code: `experiments/uniform_trim.py`. The instance record is substantially extended, and the construction generalized to an explicit per-period recipe with a documented combinatorial obstruction, at `12.8.6`; this Remark's own recorded instances are unchanged.

**Remark 12.8.4 (what the staircase means).** The staircase is a divergent-orbit profile bent into a loop: geometric depth growth with shallow exits is exactly the growth regime of the size ledger (`11.8.4.4` — `log x` grows when `s < 0.585m`). Size analysis cannot forbid it as a cycle for the same reason drift analysis cannot forbid divergence: both are rare-event arithmetic questions, not counting questions. What *must* kill the staircase is the `p`-fold divisibility system — equivalently, in anchor coordinates, the rigidity of closed anchor walks (`11.8.5.6`, `9.8.4` anchor form). The two halves of the conjecture's residual difficulty (statistics for orbits, rigidity for cycles) meet in this one configuration, which is strong evidence they are the same problem.

**Consequence 12.8.5 (strategy; the stopping rule fires).** The crossover plan — reach `p > 91` via trim plus search — is withdrawn: by `12.8.2` the search bound at `p = 92` is `n_0 ~ 10^18`, infeasible, and by `12.8.3` no size-level lemma can lower it. Per the stopping rules (README), the cycle ladder is retired and the cycle front is parked: periods `1`–`3` closed, the uniform question answered, and the remaining content of cycle exclusion precisely identified as anchor-walk rigidity — the same front as Stage 4. No further per-period searches will run. **This conclusion is unchanged by `12.8.6` below, at any grade** — that subsection only recalibrates the sharpness evidence of `12.8.3`; it settles nothing about exclusion.

## 12.8.6. Diophantine Input and the Explicit Staircase Recipe (floor grade)

This subsection attempts to upgrade `12.8.3`'s sharpness assessment (`γ = O(log p)` at *every* period, verified there only at `p ∈ {6, 7}`) from assessed to proved — the same hedge recorded in the published paper's Theorem `thm:staircase`. The attempt packages an external suggestion (Eric Merle, correspondence 2026-07-16), pre-checked and delegated per `briefs/staircase-allp-brief.md`; stopping-rule compliance is recorded there (this is a negative structural result about size arguments, not a cycle search or a divisibility-based exclusion attempt). It reaches the **floor grade**: a general per-period construction recipe, a verified instance record substantially larger than `12.8.3`'s two points, and a precisely located combinatorial obstruction beyond it. The primary theorem and both fallback gradations of the brief remain open; `12.8.5`'s strategic conclusion is unaffected.

**Lemma 12.8.6.1 (Diophantine input).** Let `L = log_2 3` and let `h_k/q_k` be its continued-fraction convergents (`h_k` the numerator, to avoid clashing with the period `p`). For an index `k` with `h_(k-1) - q_(k-1)L > 0` (the sign giving `q = 2^K - 3^n > 0` for `K = ⌈nL⌉`), the semiconvergents `n_j = q_(k-1) + j·q_k` (`j = 1, ..., a_(k+1)`, `a_(k+1)` the next partial quotient) inherit that sign for every `j` in the run, and

```text
0  <  h_(k+1) - q_(k+1)L  <=  K_j - n_j L  <=  h_(k-1) - q_(k-1)L        for every j = 1, ..., a_(k+1)
```

(exactly: `K_j - n_j L = (h_(k-1) - q_(k-1)L) - j·(q_k L - h_k)`, decreasing in `j`, with the left equality at `j = a_(k+1)` — the next correctly-signed convergent). Since `γ = K - log_2(2^K - 3^n) = -log_2(1 - 2^(-(K - nL)))` is *decreasing* in `K - nL`, it is the *left* inequality that bounds `γ` above — by `-log_2(1 - 2^(-(h_(k+1) - q_(k+1)L)))`, a quantity fixed within the run (not growing with `j`) — while `n_j` ranges up to `q_(k+1)` in steps of `q_k`. This is the mechanism the main-session pre-check flagged: `n = 41` and `n = 306` are full convergent denominators of `L`, and `n = 94 = 53 + 41`, `n = 971 = 665 + 306` are the first semiconvergent denominators following the next convergent (`53` and `665` respectively) — both re-derived independently here via an exact continued-fraction expansion of `L`, matching the pre-check's throwaway computation.

*Status of this lemma.* That a correctly-signed run exists at every scale is classical (continued-fraction density / the three-distance theorem), but a fully general, closed-form bound on the multiplicative gap between consecutive correctly-signed runs — needed to certify unconditionally that no period `p` is ever skipped, for `log_2 3` specifically — was not established in this session; this is recorded as a gap, not asserted away. What *is* established: exact coverage (a suitable `n` was found) held for every period actually tested below, and the Diophantine step was never the binding constraint — every obstruction hit below is combinatorial, not Diophantine.

**Construction 12.8.6.2 (explicit profile).** Given `p` and a candidate `n` from `12.8.6.1` with `K = ⌈nL⌉`, `S = K - n`: fix a crash depth `c ∈ {1, 2}`, set the crash block `m_(p-1) = c`, `s_(p-1) = S - (p - 1)`; for the `p - 1` climb blocks `j = 0, ..., p-2` set `s_j = 1` and round the geometric profile `m_j ∝ L^j` (total `n - c`) to integers by rounding the *partial sums* to the nearest integer at every prefix, then differencing, rather than rounding each `m_j` independently — this bounds the rounding error at `1/2` at every prefix instead of letting per-block errors accumulate additively over `p` terms (`experiments/staircase_allp.py` Part C). The shape matches `12.8.3`'s description (geometric climb at ratio `≈ L`, unit exits, one crash block) exactly; it is not claimed to reproduce any *specific* recorded instance (see the cross-check below).

**Algorithm 12.8.6.3 (bounded correction).** The base construction of `12.8.6.2` typically falls short of `q <= R_r` on one to a few rotations near the crash block, by a small margin — a handful of bits, not the profile's overall scale. A deterministic, auditable local search closes this in every case it closes at all: repeatedly locate the worst (minimal-`R_r`) rotation, then move one unit of climb depth from a donor block to a recipient block (the crash block's depth is never touched), accepting whichever single move most improves the worst-rotation margin, until every rotation passes or a move/time budget is exhausted (`experiments/staircase_allp.py` Part D). This is not a cycle search: it constructs one witness configuration per period from an explicit starting point, every move is logged, and it never touches the divisibility system.

**Proposition 12.8.6.4 (verified instance record, 2026-07-16).** By the recipe of `12.8.6.1`–`12.8.6.3`, exact big-integer verification (`experiments/staircase_allp.py`, fresh code, no import from `uniform_trim.py`) produces a configuration satisfying the size-passer condition (all `p` rotations, `q <= R_r`) and the scale condition (`n ~ 1.585^p` by construction) for every period

```text
p  ∈  {2, 3, ..., 21} ∪ {23},        with     γ / log_2 p  ∈  [1.83, 3.64]
```

over that range — consistent with, but not a proof of, the assessed `γ = O(log p)` shape (`12.8.3`, `thm:staircase`). The recipe's own output at `p = 7` (`n = 29`, `γ = 5.339`) is a *different* valid witness from `12.8.3`'s recorded instance (`n = 94`, `γ = 6.744`) — the staircase family is not unique at a given period, as `12.8.3`'s own `84` size-passers at `p = 6` already show. The published `p = 7` instance is separately reproduced and re-verified as a direct cross-check, independent of the general recipe: `m = (4,7,9,15,23,35,1)`, `s = (1,1,1,1,1,1,S-6)`, `γ = 6.744`, matching `12.8.3` to the stated precision, all seven rotations pass. Every constructed instance (recipe output and the cross-check) was checked against the full divisibility system `q | R_r`: none passes, matching `12.8.3`'s own finding for its instances; no halt condition was triggered.

**Obstruction (`p = 22`).** At `p = 22`, the bounded correction of `12.8.6.3` does not find a passing configuration within the tested budgets: up to `40` correction moves per candidate and `75` s of wall clock per period, six candidate `n` and two crash depths, in the committed script; up to `60` moves with no time limit, across a larger candidate set, in supplementary exploration recorded in `briefs/staircase-allp-findings.md`. `p = 24, 25` are also unresolved under the committed script's default budget but *do* resolve under the larger supplementary one (`8` moves each) — evidence that those two are a budget artifact rather than a structural wall, unlike `p = 22`, which resisted the larger budget too. This is recorded, not forced: whether a different profile (a second crash block, non-unit climb exits, a different rounding rule) closes `p = 22` is open, and is exactly the "clean explicit profile with provable slack, not naive rounding" difficulty the brief anticipated as the likely location of trouble.

**Achieved grade: floor, substantially exceeded.** The brief's floor bar was verified instances to at least `p <= 20` with a documented obstruction; this reaches `p = 21` and `p = 23` (twenty periods beyond `12.8.3`'s original two) via one general, non-per-period construction recipe plus a bounded, auditable (not exhaustive-search) correction algorithm, with the obstruction precisely located at `p = 22`. The primary theorem and both fallback gradations remain open: the all-`p` sharpness claim in `thm:staircase` is calibrated further — two isolated verified instances become a dense, algorithmically generated range with a documented combinatorial limit — but not proved. `12.8.5`'s strategic conclusion (the cycle front stays parked; the residual content of cycle exclusion is anchor-walk rigidity) is unchanged, as recorded above.

