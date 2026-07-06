---
status: open — low-order law PROVED (11.8.7.3); displacement propagation and full increment law open
scope: monolith 11.8.7, plus new material 11.8.7.1–11.8.7.5 (first post-split addition)
updated: 2026-07-07
source: 11.8.7 moved from program.md; 11.8.7.1+ new
---

> **Current state.** Stage 4 — the odd core `ω_+`, equivalently the anchor increment law (`11.8.5.6`) — is the live front. First result: the anchor increment `ΔM` obeys an exact low-order law (Theorem `11.8.7.3.1`): `ΔM mod 2^k` is an explicit function of the state's residue modulo `2^(σ+k+2)` in `ω` and `2^(σ+k)` in `d`, together with `a_+ mod 2^k`, where `σ = v_2(C)`. Guardrail-compliant: modulus fixed in advance per `(s, m_+)` stratum. What remains open is sub-question 2 of `11.8.5.6.3` (displacement propagation), which requires `ΔM` to unbounded depth.

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

1. **Displacement propagation on the generic stratum**: bound `v_2(d_+ - M(ω_+))` from below-threshold data, accepting an exceptional set priced by the ledger.
2. **The cycle benchmark**: a nontrivial cycle is a closed anchor walk with `Σ ΔM_t = 0` (`9.8.4`, anchor form); the low-order law makes every cycle candidate satisfy an explicit finite congruence system per stratum sequence. Test whether this reproduces or sharpens the known cycle-length constraints (`11.8.3.11`).
