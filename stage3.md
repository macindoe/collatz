---
status: closed at the valuation level, per reduced step, all residue classes
scope: monolith 11.8.6
updated: 2026-07-06
source: sources/drafts/collatz_reduction_rewrite_v078.md (last monolith)
---

> **Current state.** Stage 3: decomposition of C. The 3-adic absorption law for a_+, the target-shift lemma, the entry-depth law for m_+ on all six residue-parity classes, and the per-step depth law d_+ = m_+ + a_+. Independently re-verified numerically (62,937 states in the note; 8,000 random states re-checked 2026-07-06).

### 11.8.6. Stage 3: First Decomposition of `C`

Stage 2 classified the first dynamical consequence of the valuation

```text
s = v_2(3^dω - 1),
```

namely whether the next odd seed gains a factor of `3`. The next stage is to move from the parity of `s` to the actual depth evolution of the next reduced state. By the increment identity of `11.8.5.6`, this stage carries double weight: the anchor increment `ΔM` is a deterministic function of `C`, so controlling `C` is simultaneously the fiber-to-orbit bridge for the whole anchor formalism.

Recall that the reduced map is governed by

```text
A = 3^dω - 1,
s = v_2(A),
C = A + 2^s,
```

with

```text
d_+ = v_2(C) - s + v_3(C).
```

Thus Stage 3 does not begin by trying to classify the full odd core `ω_+`. It begins by decomposing the next depth into its two valuation components:

```text
m_+ = v_2(C) - s,
a_+ = v_3(C),
d_+ = m_+ + a_+.
```

This separates the Stage 3 problem into two parts:

```text
2-adic entry-depth problem:      m_+ = v_2(C) - s,
3-adic absorption problem:       a_+ = v_3(C).
```

The second of these is more immediately accessible, because `C` can also be written as

```text
C = 3^dω + (2^s - 1),
```

which exposes its `3`-adic structure. The first remains the harder entry-depth problem, since it asks how close the odd exit lies to `-1` in the `2`-adic sense.

The purpose of this section is therefore to make the first decomposition of `C` explicit, then isolate the part of Stage 3 that can be attacked before attempting a full classification of `d_+`.

#### 11.8.6.1. Exit-unit normalization of `C`

Let

```text
A = 3^dω - 1,
s = v_2(A),
x_exit = A / 2^s.
```

Then

```text
A = 2^s x_exit.
```

Since

```text
C = A + 2^s,
```

one obtains

```text
C = 2^s x_exit + 2^s
  = 2^s(x_exit + 1).
```

Therefore

```text
v_2(C) = s + v_2(x_exit + 1),
```

and hence

```text
v_2(C) - s = v_2(x_exit + 1).
```

But the next-entry depth is exactly

```text
m_+ = v_2(x_exit + 1),
```

so this recovers

```text
m_+ = v_2(C) - s.
```

Likewise, since multiplication by `2^s` does not affect `3`-adic valuation,

```text
v_3(C) = v_3(x_exit + 1).
```

Thus the next `3`-adic absorption is

```text
a_+ = v_3(C) = v_3(x_exit + 1).
```

Combining these gives the normalized depth formula

```text
d_+ = v_2(x_exit + 1) + v_3(x_exit + 1).
```

Equivalently,

```text
d_+ = m_+ + a_+,
```

where

```text
m_+ = v_2(x_exit + 1),
a_+ = v_3(x_exit + 1).
```

This normalization shows that Stage 3 is not merely a problem about the formal expression

```text
C = 3^dω - 1 + 2^s.
```

It is the problem of understanding the arithmetic of the next entry quantity

```text
x_exit + 1.
```

In particular:

```text
m_+ = v_2(x_exit + 1)
```

measures the `2`-adic proximity of the odd exit to `-1`, while

```text
a_+ = v_3(x_exit + 1)
```

measures how much `3`-adic content is absorbed into the next reduced depth.

So the first Stage 3 decomposition is:

```text
Stage 3A: classify v_3(C), equivalently v_3(x_exit + 1);
Stage 3B: classify v_2(C) - s, equivalently v_2(x_exit + 1).
```

The next subsection begins with Stage 3A, because the identity

```text
C = 3^dω + (2^s - 1)
```

makes the `3`-adic part of `C` accessible before the harder `2`-adic entry-depth problem is solved.

#### 11.8.6.2. Exact `3`-adic law for `C`

The `3`-adic part of `C` is more accessible than the `2`-adic entry-depth part because

```text
C = A + 2^s
  = 3^dω - 1 + 2^s
  = 3^dω + (2^s - 1).
```

Since `3 ∤ ω`, the first summand has exact `3`-adic valuation

```text
v_3(3^dω) = d.
```

Thus the only additional input needed is the `3`-adic valuation of

```text
2^s - 1.
```

Define

```text
h(s) = v_3(2^s - 1).
```

Then:

```text
h(s) =
    0,              if s is odd,
    1 + v_3(s),     if s is even.
```

Indeed, if `s` is odd, then `2^s ≡ -1 (mod 3)`, so

```text
2^s - 1 ≠ 0 (mod 3),
```

and hence `h(s) = 0`.

If `s` is even, the standard lifting law gives

```text
v_3(2^s - 1) = v_3(2^2 - 1) + v_3(s/2)
             = v_3(3) + v_3(s)
             = 1 + v_3(s).
```

This gives an exact comparison law for the `3`-adic contribution to the next depth.

**Proposition 11.8.6.2.1 (exact `3`-adic law for `C`).**
Let

```text
A = 3^dω - 1,
s = v_2(A),
C = A + 2^s.
```

Assume `3 ∤ ω`, and define

```text
h(s) = v_3(2^s - 1).
```

Then:

1. if

   ```text
   h(s) < d,
   ```

   then

   ```text
   v_3(C) = h(s);
   ```

2. if

   ```text
   h(s) > d,
   ```

   then

   ```text
   v_3(C) = d;
   ```

3. if

   ```text
   h(s) = d,
   ```

   then

   ```text
   v_3(C) = d + v_3(ω + β),
   ```

   where

   ```text
   β = (2^s - 1)/3^d.
   ```

**Proof.**
Using

```text
C = 3^dω + (2^s - 1),
```

the two summands have `3`-adic valuations

```text
v_3(3^dω) = d
```

and

```text
v_3(2^s - 1) = h(s).
```

If `h(s) < d`, the two summands have distinct `3`-adic valuations, and the smaller valuation dominates. Therefore

```text
v_3(C) = h(s).
```

If `h(s) > d`, the same argument gives

```text
v_3(C) = d.
```

It remains only to consider the resonant case

```text
h(s) = d.
```

Then both summands are divisible by exactly `3^d` before possible cancellation. Since `3 ∤ ω`, and since

```text
β = (2^s - 1)/3^d
```

is an integer, one may factor

```text
C = 3^dω + (2^s - 1)
  = 3^d(ω + β).
```

Hence

```text
v_3(C) = d + v_3(ω + β).
```

This proves the trichotomy. ∎

Since

```text
a_+ = v_3(C),
```

this proposition gives an exact law for the `3`-adic absorption component of the next reduced depth.

In particular, away from the resonant comparison

```text
h(s) = d,
```

the next `3`-adic absorption is simply

```text
a_+ = min(d, h(s)).
```

The only case in which additional `3`-adic cancellation can occur is the resonant case

```text
h(s) = d,
```

where the residual unit

```text
ω + (2^s - 1)/3^d
```

must be examined.

**Corollary 11.8.6.2.2 (non-resonant `3`-gain magnitude).**
If `s` is even and

```text
1 + v_3(s) < d,
```

then

```text
v_3(C) = 1 + v_3(s).
```

Equivalently, in this non-resonant range,

```text
a_+ = 1 + v_3(s).
```

**Proof.**
If `s` is even, then

```text
h(s) = v_3(2^s - 1) = 1 + v_3(s).
```

The hypothesis says exactly that

```text
h(s) < d.
```

Therefore Proposition `11.8.6.2.1` gives

```text
v_3(C) = h(s) = 1 + v_3(s).
```

Since `a_+ = v_3(C)`, the result follows. ∎

**Corollary 11.8.6.2.3 (no `3`-absorption when `s` is odd).**
If `s` is odd, then

```text
v_3(C) = 0.
```

Equivalently, the next odd seed gains no factor of `3`.

**Proof.**
If `s` is odd, then

```text
h(s) = v_3(2^s - 1) = 0.
```

Since `d >= 1`, one has

```text
h(s) < d.
```

Therefore Proposition `11.8.6.2.1` gives

```text
v_3(C) = h(s) = 0.
```

This is consistent with Lemma `9.3.1`, which states that `3`-gain occurs if and only if `s` is even. ∎

**Interpretation.**
Stage 2 classified whether `3`-gain occurs. Proposition `11.8.6.2.1` begins Stage 3 by classifying how much `3`-adic absorption occurs in the next depth, except for the resonant case where

```text
v_3(2^s - 1) = d.
```

Thus the `3`-adic component of the depth evolution is largely controlled by the comparison

```text
d
    versus
v_3(2^s - 1).
```

Using the explicit law for `h(s)`, this comparison becomes

```text
d
    versus
0
```

when `s` is odd, and

```text
d
    versus
1 + v_3(s)
```

when `s` is even.

So the first part of Stage 3 is now sharply separated from the remaining bottleneck. The `3`-adic absorption term

```text
a_+ = v_3(C)
```

is controlled by this comparison law, while the harder entry-depth term

```text
m_+ = v_2(C) - s = v_2(x_exit + 1)
```

remains the next unresolved target.

#### 11.8.6.3. The target-shift lemma and the entry-depth law

The preceding subsection controls the `3`-adic absorption term `a_+ = v_3(C)` by comparing `d` with `h(s) = v_3(2^s - 1)`. This subsection closes the remaining component of the next-depth formula, the `2`-adic entry-depth term

```text
m_+ = v_2(C) - s = v_2(x_exit + 1).
```

An earlier draft asserted that the identity `C = 3^dω + (2^s - 1)` "does not by itself give an equally transparent law" for this term. That was too pessimistic. Since `C = A + 2^s = 2^s(x_exit + 1)`,

```text
s + m_+ = v_2(C) = v_2(3^dω - (1 - 2^s)),
```

which is the original lifting-branch valuation problem with the target `1` replaced by the shifted target `1 - 2^s`. For `s >= 3` the shifted target satisfies `1 - 2^s ≡ 1 (mod 8)`, so it lies in the group `1 + 8 Z_2` on which the anchor isomorphism is defined — and the entire anchor machinery applies to it unchanged.

**Lemma 11.8.6.3.1 (target shift).** Let `ω ≡ 1 (mod 8)`, let `d = 2n`, and let `c ∈ 1 + 8 Z_2`. If `n - N(ω) + N(c) ≠ 0`, then

```text
v_2(3^d ω - c) = 3 + v_2(n - N(ω) + N(c)).
```

**Proof.** By the defining property of the anchor (`9^(N(u)) = u^(-1)` for `u ∈ 1 + 8 Z_2`), write `ω = 9^(-N(ω))` and `c = 9^(-N(c))`. Then

```text
3^d ω - c = 9^(n - N(ω)) - 9^(-N(c))
          = 9^(-N(c)) · ( 9^(n - N(ω) + N(c)) - 1 ).
```

The prefactor is a `2`-adic unit, so it does not affect the valuation, and the isometry of Lemma `11.8.3.6.5` applied to the bracket (as in the isometry remark following Theorem `11.8.3.6.6`, valid for any nonzero `2`-adic exponent) gives `v_2(9^t - 1) = 3 + v_2(t)` with `t = n - N(ω) + N(c)`. ∎

The case `c = 1` (so `N(c) = 0`) is exactly the global valuation law of `11.8.4.1`: the entire spike–halo synthesis is the `c = 1` instance of the target-shift lemma.

**Definition 11.8.6.3.2 (shift constant).** For `s >= 3`, set

```text
δ_s = N(1 - 2^s) = -log(1 - 2^s) / log 9.
```

Its valuation is exact:

```text
v_2(δ_s) = s - 3,
```

since `v_2((1 - 2^s) - 1) = s`, so by the isometry `v_2(log(1 - 2^s)) = s`, and `v_2(log 9) = 3`. (Log-free derivation: `9^(δ_s) = (1 - 2^s)^(-1)` and `v_2((1 - 2^s)^(-1) - 1) = v_2(2^s / (1 - 2^s)) = s`, so the `c = 1` law gives `s = 3 + v_2(δ_s)`.)

**Theorem 11.8.6.3.3 (entry-depth law on the lifting branch).** Let the state lie on the lifting branch, with anchor displacement `ε` as in Stage 2: on the even component (`ω ≡ 1 (mod 8)`, `d = 2n`) `ε = n - N(ω)`, and on the odd component (`ω ≡ 3 (mod 8)`, `d = 2n + 1`) `ε = n - N(3ω)`, in both cases with `ε ≠ 0` and `s = 3 + v_2(ε)`. Then

```text
m_+ = 3 - s + v_2(ε + δ_s).
```

**Proof.** On the even component, apply Lemma `11.8.6.3.1` with `c = 1 - 2^s`, obtaining `s + m_+ = 3 + v_2(ε + δ_s)`, and subtract `s`. On the odd component, `3^d ω = 9^n·(3ω)` (Proposition `11.8.1.6.2`), so the same application with parameter `3ω ≡ 1 (mod 8)` gives the identical formula in `ε = n - N(3ω)`. Nondegeneracy: `ε + δ_s = 0` would force `3^d ω = 1 - 2^s` in `Z_2`; the left side is a positive integer, the right a negative integer, and distinct integers remain distinct in `Z_2`. ∎

**Corollary 11.8.6.3.4 (forced carry: `m_+ >= 1` automatically).** On the lifting branch, `v_2(ε) = s - 3 = v_2(δ_s)`, so `ε` and `δ_s` have `2`-adic valuation at the same scale; their sum therefore carries: `v_2(ε + δ_s) >= s - 2`, hence `m_+ >= 1`. This reproves, through the anchor formalism, the structural fact that every BlockEntry has `m >= 1` (Section `6`). Had the formula permitted `m_+ = 0`, something would be wrong; it does not.

**Theorem 11.8.6.3.5 (entry-depth law off the lifting branch).** Let `(ω, d)` be a valid reduced state and `M(ω) = N(ω^2)` the orbit anchor of Definition `11.8.5.6.1`.

If `s = 1` (the classes `(ω ≡ 1, d odd)`, `(ω ≡ 5, d odd)`, `(ω ≡ 7, d even)`, `(ω ≡ 3, d even)` of Proposition `11.8.1.3.1`), then

```text
m_+ = 1 + v_2(d - M(ω)).
```

If `s = 2` (the classes `(ω ≡ 5, d even)`, `(ω ≡ 7, d odd)`), then

```text
m_+ = v_2((d - 1) - M(ω)).
```

**Proof.** Write `X = 3^d ω`. For `s = 1`: the shifted target is `1 - 2 = -1`, so `1 + m_+ = v_2(X + 1)`. Since `s = 1` means `X ≡ 3 (mod 4)`, one has `v_2(X - 1) = 1` and `v_2(X + 1) >= 2`, so

```text
v_2(X + 1) = v_2(X^2 - 1) - v_2(X - 1) = v_2(X^2 - 1) - 1.
```

Now `X^2 = 9^d ω^2 ∈ 1 + 8 Z_2`, so the isometry of Lemma `11.8.3.6.5` applies directly:

```text
v_2(X^2 - 1) = v_2(log(9^d ω^2)) = v_2(log 9 · (d - M(ω))) = 3 + v_2(d - M(ω)),
```

using `log ω^2 = -M(ω)·log 9`. Hence `v_2(X + 1) = 2 + v_2(d - M(ω))` and `m_+ = 1 + v_2(d - M(ω))`.

For `s = 2`: the shifted target is `1 - 4 = -3`, and `3^d ω + 3 = 3·(3^(d-1) ω + 1)`, so `2 + m_+ = v_2(X' + 1)` with `X' = 3^(d-1) ω`. The `s = 2` classification forces `X = 3^d ω ≡ 5 (mod 8)`, hence `X' ≡ 3^(-1)·5 ≡ 7 (mod 8)`, so `v_2(X' - 1) = 1` and the same squaring argument gives `v_2(X' + 1) = 2 + v_2((d-1) - M(ω))`. Subtract `2`.

Nondegeneracy: `d - M(ω) = 0` would force `9^d ω^2 = 1`, hence `(ω, d) = (1, 0)`, not a valid state; `(d-1) - M(ω) = 0` would force `(ω, d) = (1, 1)`, which has `s = 1` and is excluded from the `s = 2` case. ∎

**Corollary 11.8.6.3.6 (per-step depth law on every residue class).** For every valid reduced state,

```text
d_+ = m_+ + a_+,
```

with `m_+` given exactly by Theorems `11.8.6.3.3` and `11.8.6.3.5` on all six residue-parity classes, and `a_+ = v_3(C)` given exactly by the `3`-adic absorption law of `11.8.6.2`. Stage 3 is therefore closed at the valuation level, per reduced step, on the entire state space.

**Interpretation.** Three readings of the entry-depth law deserve emphasis.

First, `m_+` is a digit-matching depth. On the lifting branch it counts how far the binary expansion of the anchor displacement `ε` agrees with that of `-δ_s` beyond the single forced leading match of Corollary `11.8.6.3.4`; generic mismatch gives `m_+ = 1`, and large `m_+` requires the anchor error to coincidentally track the digits of the shift constant. Off the lifting branch the same reading applies with the orbit anchor `M(ω)` in the depth variable.

Second, the apparent self-reference — `δ_s` depends on `s`, which depends on `ε` — is stratified, not circular. On the dyadic shell `v_2(ε) = j`, the value `s = 3 + j` is constant, and `δ_(3+j)` is a single fixed reference constant for the entire shell. One computes `s` first, then `δ_s`, then `m_+`; one shift closes the problem, with no regress. The earlier draft language ("no transparent law") suggested otherwise and is hereby retired.

Third, the shift constant explains the boundary shell. `v_2(δ_s) = s - 3` is exactly the boundary-shell scale of `11.8.3.3`: the scale at which all off-spike excess was shown to concentrate is the scale at which the shifted target sits. Both phenomena — the boundary-shell localization and the forced carry `m_+ >= 1` — are instances of the same mechanism in the additive coordinate: adding two `2`-adic quantities of equal valuation. This retrospectively unifies the boundary-shell analysis of `11.8.3.3`–`11.8.3.4` with the entry-depth law as two faces of the target-shift lemma.

**Numerical verification.** The laws were checked against direct computation of `v_2(x_exit + 1)` over all valid states with `ω < 3000`, `1 <= d < 64` — `62,937` states covering all six residue-parity classes — with zero discrepancies (entry depths up to `m_+ = 17` occurred). The forced-carry bound of Corollary `11.8.6.3.4` held without exception, and `v_2(δ_s) = s - 3` was confirmed for `3 <= s <= 29`. Two worked cases: `(ω, d) = (1, 4)` has `A = 80`, `s = 4`, `x_exit = 5`, `m_+ = 1`; anchor side `ε = 2`, `δ_4 ≡ 2 (mod 8)`, `v_2(ε + δ_4) = 2`, and `3 - 4 + 2 = 1` ✓. `(ω, d) = (17, 2)` has `A = 152`, `s = 3`, `x_exit = 19`, `m_+ = 2`; anchor side `N(17) ≡ 6 (mod 8)`, `ε ≡ 3 (mod 8)`, `δ_3 ≡ 1 (mod 8)`, `v_2(ε + δ_3) = 2`, and `3 - 3 + 2 = 2` ✓.

**Scope caveats.** The laws are per reduced step: along an orbit, `ω` changes and the anchors `N(ω_+)`, `M(ω_+)` must be recomputed; no relation between successive anchors is established, and that fiber-to-orbit bridge (`11.8.5.6`) — not any valuation term — is now the terminal open problem at the valuation level. Under the guardrail of `11.8`, the present result is admissible: an exact theorem on infinite families, reducing `m_+` to the standard valuation mechanism already in use. Chasing the digits of `δ_s` or of the anchors beyond what the theorems need would be residue-chasing and is not proposed.

Accordingly, the status of Stage 3 is now:

```text
formal, per reduced step, all residue classes:
    a_+ = v_3(C)                        (11.8.6.2)
    m_+ = v_2(C) - s                    (11.8.6.3)
    d_+ = m_+ + a_+                     (corollary)

open:
    the odd core ω_+ of C  (Stage 4)
    ⟺ the anchor increment law (11.8.5.6)
```

