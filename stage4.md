---
status: open — low-order law (11.8.7.3) and one-step propagation (11.8.7.6) PROVED; unbounded-depth residue split into statistics (orbits) and rigidity (cycles), 11.8.7.7
scope: monolith 11.8.7, plus new material 11.8.7.1–11.8.7.7
updated: 2026-07-07
source: 11.8.7 moved from program.md; 11.8.7.1+ new
---

> **Current state.** Stage 4 — the odd core `ω_+`, equivalently the anchor increment law (`11.8.5.6`) — is the live front. Two results so far. (1) The anchor increment obeys an exact low-order law (Theorem `11.8.7.3.1`): `ΔM mod 2^k` from the state's residues modulo `σ`-graded powers of `2`, moduli fixed per `(s, m_+)` stratum. (2) One-step displacement propagation (Theorem `11.8.7.6.1`): the same window decides the next exit valuation and `3`-gain in an error-free trichotomy, undecided only at rate `≈ 2^(-(k+1))`, and undecided *means* deep cascade ahead. The digit-budget accounting (`11.8.7.7`) shows bounded windows cannot decide infinite horizons: the remaining content of the bridge is the equidistribution hypothesis for typical orbits, and rigidity for cycles. The cycle front is open at cycles.md (§12): periods 1 and 2 closed, reproducing Steiner and the Simons–de Weger 2-cycle case; period `p >= 3` is the live target.

### 11.8.7. Stage 4. Only Then Refine `ω_+`

The final stage is a sharper classification of the odd core

```text
ω_+ = C / (2^(v_2(C)) 3^(v_3(C))).
```

This should be treated as a later objective rather than the first one. The quantity `ω_+` is the most refined part of the next reduced state, and attempts to classify it too early are especially likely to fall into unproductive case-splitting.

Accordingly, the natural order of difficulty is:

1. control `s`,
2. understand `3`-gain,
3. obtain laws for `d_+`,
4. and only then seek a more transparent description of `ω_+`.

Items `1`–`3` are now closed per reduced step (the exact global law of `11.8.4.1`, the `3`-gain law of `11.8.5`, and the entry-depth and absorption laws of `11.8.6.2`–`11.8.6.3`). Stage 4 is thus the live front, and by `11.8.5.6` it coincides with the anchor increment law — the fiber-to-orbit bridge.

#### 11.8.7.1. Pilot experiment: is there a low-order law for `ΔM`?

Sub-question 1 of Question `11.8.5.6.3` asks whether `ΔM` admits an exact law modulo small powers of `2` in terms of low-order state data. Before attempting a derivation, the question was tested empirically (2026-07-06): sample random valid states, compute `ΔM mod 8` exactly, bucket states by candidate low-order keys, and check whether any bucket receives two different values of `ΔM mod 8`. A functional dependence shows up as zero conflicting buckets.

```text
20,000 samples, ω < 10^5, 1 <= d < 60:

key (ω mod 2^10, d mod 2^8,  s, a_+):  10,752 buckets, 318 conflicts
key (ω mod 2^14, d mod 2^12, s, a_+):  13,223 buckets,   1 conflict
```

Two features of the conflict pattern pointed at the correct statement: conflicts shrink monotonically as the key moduli grow, and they concentrate at large `s` — suggesting an exact law whose required modulus grows with the exit valuation rather than a fixed-modulus law with exceptions. The derivation below confirms exactly that, with the correct scale parameter `σ = v_2(C) = s + m_+`.

#### 11.8.7.2. Digit-determinacy lemmas

Three elementary lemmas locate how many digits of the state each quantity needs. Throughout, `σ = v_2(C) = s + m_+` and `a_+ = v_3(C)`.

**Lemma 11.8.7.2.1 (anchor digits).** For `u ≡ 1 (mod 8)`, the truncation `N(u) mod 2^k` depends only on `u mod 2^(k+3)`.

**Proof.** By the congruence definition of the anchor (`11.8.3.6`), `N(u) mod 2^k` is the unique solution `n mod 2^k` of `9^n ≡ u^(-1) (mod 2^(k+3))`, unique because `9` has multiplicative order `2^k` modulo `2^(k+3)`. The congruence depends on `u` only through `u mod 2^(k+3)`. ∎

**Lemma 11.8.7.2.2 (derived-quantity digits).** For `q >= 3`, the truncation `C mod 2^q` is determined by `ω mod 2^q`, `d mod 2^(q-2)`, and `s`.

**Proof.** `C = 3^d ω - 1 + 2^s`, and `3` has multiplicative order `2^(q-2)` modulo `2^q`, so `3^d mod 2^q` depends only on `d mod 2^(q-2)`. ∎

**Lemma 11.8.7.2.3 (odd-core digits).** For `r >= 3`, the truncation `ω_+ mod 2^r` is determined by `C mod 2^(σ+r)`, `σ`, and `a_+ mod 2^(r-2)`.

**Proof.** `ω_+ = (C / 2^σ) · 3^(-a_+)`. Division by `2^σ` is exact, so `C mod 2^(σ+r)` determines `C/2^σ mod 2^r`. Multiplication by `3^(-a_+) mod 2^r` depends on `a_+` only modulo the order of `3` modulo `2^r`, which is `2^(r-2)`. ∎

#### 11.8.7.3. The low-order anchor-increment law

**Theorem 11.8.7.3.1 (low-order law for `ΔM`).** Let `(ω, d)` be a valid reduced state with exit valuation `s`, `σ = v_2(C)`, and absorption `a_+ = v_3(C)`. Then for every `k >= 1`, the truncation

```text
ΔM mod 2^k
```

is determined by — and explicitly computable from —

```text
ω mod 2^(σ+k+2),    d mod 2^(σ+k),    a_+ mod 2^k.
```

Moreover the stratum data `(s, σ)` are themselves determined by the same truncations, so the statement is self-consistent: two states agreeing on these residues (and on `a_+ mod 2^k`) have equal `ΔM mod 2^k`.

**Proof.** By the increment identity (`11.8.5.6`), `ΔM = N((ω_+/ω)^2)`. By Lemma `11.8.7.2.1` this truncation needs `(ω_+/ω)^2 mod 2^(k+3)`, hence `ω_+ mod 2^(k+2)` and `ω mod 2^(k+2)` (a residue modulo `2^(k+2)` determines its square modulo `2^(k+3)`). By Lemma `11.8.7.2.3` with `r = k + 2`, the core truncation needs `C mod 2^(σ+k+2)` and `a_+ mod 2^k`. By Lemma `11.8.7.2.2` with `q = σ + k + 2`, that needs `ω mod 2^(σ+k+2)` and `d mod 2^(σ+k)`. Finally, `s <= σ`, so `A mod 2^(σ+1)` — determined by the same truncations — exhibits `s = v_2(A)`, and `C mod 2^(σ+1)` exhibits `σ = v_2(C)`. ∎

**Corollary 11.8.7.3.2 (parity of `ΔM`; lifting parity of the next state).** `ΔM mod 2` is determined by `ω mod 2^(σ+3)`, `d mod 2^(σ+1)`, and `a_+ mod 2`. By the parity statement of Proposition `11.8.5.6.2` (`M(ω)` is even iff `ω ≡ ±1 (mod 8)`), this determines whether the next state's anchor parity — hence its lifting depth-parity class — flips.

**Remark (guardrail compliance).** On each stratum `(s, m_+)` the moduli `2^(σ+k+2)`, `2^(σ+k)` are fixed in advance, so this is a classification with modulus fixed in advance in the sense of guardrail clause 2, not residue-chasing: no refinement is ever introduced to rescue a failing pattern. The generic stratum (`s <= 2`, `m_+ = 1`) needs only `ω mod 2^(k+5)`, `d mod 2^(k+3)`. Deep strata need proportionally more digits — and the frequency ledger (`11.8.4.4`) prices exactly how rarely they occur.

**Remark (the finite-state skeleton).** Composing this law with the entry-depth law (`11.8.6.3`) and the absorption law (`11.8.6.2`) yields, on every stratum, an exact finite-modulus transition law for the truncated state `(ω mod 2^j, d mod 2^j)` together with the shell labels. This is the sharp answer to the finite-state-shadow question of `11.6` (open-problems.md): the reduced dynamics admits an exact countable-state chart — finite-modulus states indexed by shells — whose only unresolved inputs are the shell labels themselves at unbounded depth.

#### 11.8.7.4. Numerical verification

Independent implementation, 2026-07-07, `k ∈ {1, 3, 6}`, random states `ω < 2·10^5`, `1 <= d < 50`:

* **Predictor test** — `ΔM mod 2^k` computed *only* from the truncated residues of Theorem `11.8.7.3.1`, compared against the true value computed with exact integers: `4,046` checks, zero failures.
* **Lift-invariance test** — pairs of states agreeing on the truncated data (constructed by lifting `ω` by multiples of `2^(σ+k+2)` and `d` by multiples of `2^(σ+k)`, subject to validity and equal `a_+ mod 2^k`): `10,092` pairs, equal `ΔM mod 2^k` in every case, and the stratum data `(s, σ)` were preserved by every lift, confirming self-consistency.

Verification code: `experiments/anchor_increment.py`.

#### 11.8.7.5. Scope: what this closes and what it leaves

Sub-question 1 of Question `11.8.5.6.3` is closed in the affirmative, with the refinement that the required modulus is `σ`-graded rather than uniform. What the theorem does **not** deliver is sub-question 2 (displacement propagation): the next `3`-gain decision needs `v_2(d_+ - M(ω_+))`, and when the next displacement is deep this requires `ΔM` to *unbounded* depth — precisely where the low-order law is silent. The residual hardness of Stage 4 is therefore now confined to unbounded-depth digit questions, the same regime as the anchor digit statistics (`11.8.4.2`). The natural next targets, in order:

1. **Displacement propagation on the generic stratum**: bound `v_2(d_+ - M(ω_+))` from below-threshold data, accepting an exceptional set priced by the ledger. *(Achieved in one-step form: Theorem `11.8.7.6.1`. The iterated form is capped by the digit budget — see `11.8.7.7`.)*
2. **The cycle benchmark**: a nontrivial cycle is a closed anchor walk with `Σ ΔM_t = 0` (`9.8.4`, anchor form); the low-order law makes every cycle candidate satisfy an explicit finite congruence system per stratum sequence. Test whether this reproduces or sharpens the known cycle-length constraints (`11.8.3.11`). *(Opened: cycles.md §12. Periods 1 and 2 closed (Theorems `12.2.3`, `12.5.3`); period 3 closed to `n <= 20,000` (Theorem `12.7.1`) via the general-`p` elimination and ceiling lemma (`12.6`). Crossover target: `p > 91`.)*

#### 11.8.7.6. One-step displacement propagation

Fix `k >= 1`. The **depth-`k` window** of a valid state `(ω, d)` consists of the residues

```text
ω mod 2^(σ+k+2),    d mod 2^(σ+k),
```

together with the stratum labels `(s, σ, a_+)`. This is exactly the data of Theorem `11.8.7.3.1`. The result of this subsection is that the window decides the *next* exit valuation — hence the next `3`-gain decision — in a trichotomy that never errs.

**Theorem 11.8.7.6.1 (one-step propagation).** From the depth-`k` window alone, the following are determined:

1. the exact next depth `d_+ = (σ - s) + a_+`, and the next residue-parity class `(ω_+ mod 8, d_+ mod 2)` — in particular, whether the next state lies on the lifting branch;
2. if the next class is **non-lifting**: the exact value `s_+ ∈ {1, 2}` from the class alone (Proposition `11.8.1.3.1`), and with it the next `3`-gain decision (`9.3`);
3. if the next class is **lifting**: the truncation `ε_+ mod 2^k` of the next anchor displacement `ε_+ = d_+ - M(ω_+)`. If `ε_+ ≢ 0 (mod 2^k)`, then `s_+ = 2 + v_2(ε_+)` exactly (Proposition `11.8.5.6.2`) and the next `3`-gain decision is determined. If `ε_+ ≡ 0 (mod 2^k)`, the window is silent — and correctly reports that `s_+ >= k + 2`: the next step is a deep cascade.

**Proof.** By Lemma `11.8.7.2.2` with `q = σ + k + 2`, the window determines `C mod 2^(σ+k+2)`; by Lemma `11.8.7.2.3` with `r = k + 2`, it determines `ω_+ mod 2^(k+2)`, hence the class in `1` (`k >= 1` gives at least `mod 8`), while `d_+ = v_2(C) - s + v_3(C) = (σ - s) + a_+` is exact from the labels. Case `2` is the first-layer classification. For case `3`, Lemma `11.8.7.2.1` applied to `ω_+^2 mod 2^(k+3)` (determined by `ω_+ mod 2^(k+2)`) gives `M(ω_+) mod 2^k`, hence `ε_+ mod 2^k` with `d_+` exact. If the truncation is nonzero its `2`-adic valuation is visible and the unified depth-side law gives `s_+`; if zero, `v_2(ε_+) >= k` and `s_+ = 2 + v_2(ε_+) >= k + 2`. ∎

**Remark (failure is not error).** The trichotomy is decide-exactly / decide-exactly / report-deep. The window never outputs a wrong value of `s_+`: its only failure mode is an explicit flag, and the flag itself carries content — `s_+ >= k + 2` is precisely a deep-cascade prediction, the rare events the frequency ledger (`11.8.4.4`) prices at `2^(-s)`.

**Remark (undecided rate).** The undecided event is *next class lifting* ∧ `2^k | ε_+`. On the lifting branch `v_2(ε_+) >= 1` automatically (parity match, `11.8.5.6.2`), so under the uniformity heuristic the rate is `P(lifting) · 2^(-(k-1)) ≈ (1/4) · 2^(-(k-1)) = 2^(-(k+1))`. Measured along real orbits: `0.0275` vs. predicted `0.03125` at `k = 4`; `0.0019` vs. `0.00195` at `k = 8`.

**Remark (relation to the increment law).** The proof runs through `ω_+ mod 2^(k+2)` directly and never needs `ΔM` itself; equivalently one may compute `M(ω_+) mod 2^k = (M(ω) + ΔM) mod 2^k` by Theorem `11.8.7.3.1`. The two routes are the same lemmas in different order. The `ΔM` form is the one that iterates — and iteration is exactly where the budget of `11.8.7.7` bites.

**Numerical verification (2026-07-07).** Window-only decision procedure along real orbits, `k ∈ {4, 8}`, `21,296` steps: `21,000` decided with **zero errors**, `296` undecided with **zero violations** of the bound `s_+ >= k + 2`. Code: `experiments/one_step_propagation.py`.

#### 11.8.7.7. The digit budget: finite horizons, and where the residual difficulty lives

Deciding one step at depth `k` consumes the state's `2`-adic data to depth `σ + k + 2`. Along real orbits the mean consumption is `E[σ] ≈ 4.0` digits per step (measured; consistent with `E[s] ≈ 2`, `E[m_+] ≈ 2` from the ledger). Nothing regenerates this supply: the anchors of later states are deterministic functions of the *full* initial state, not of any bounded window. A window of `W` initial digits therefore supports on the order of `W / (E[σ] + k + 2) ≈ W / (k + 6)` decided steps, after which every further step is formally undecided. The conclusion does not depend on the constant: bounded-window determinism along an infinite orbit is impossible in principle, because the orbit's decision sequence consumes unboundedly many digits and consults nothing else.

This accounting fixes the shape of everything downstream of Theorem `11.8.7.6.1`:

* **What is provable at bounded depth is now proved.** One-step (and, by iteration until exhaustion, finite-horizon) propagation is the complete deterministic content of sub-question `2` of `11.8.5.6.3`.
* **For typical orbits**, the unbounded-depth residue is irreducibly statistical: it is sub-question `3` — do the successive anchors equidistribute in `Z_2`? The fair-coin digit model (`11.8.4.2`) is no longer merely an empirical observation about anchor digits; it is now the exact form of the missing hypothesis for orbit-level control.
* **For cycles**, the unbounded-depth residue is rigidity-theoretic, not statistical: a cycle is a finite closed anchor walk with `Σ ΔM_t = 0` (`9.8.4`, anchor form), a regime where effective `p`-adic tools already operate (`11.8.3.11`). This is the one place where finite data can beat unbounded depth, and it is the recommended next front.

In reduced coordinates, then, the entire difficulty of the problem has been localized to the digit supply of the anchors — which is where `11.8.4.2` said it should be. The program's honest claim is unchanged from `11.8.4.4`: Route A converts rare-event structure from heuristic to exact; convergence itself requires either the statistical hypothesis or rigidity, and the two now have precise statements.
