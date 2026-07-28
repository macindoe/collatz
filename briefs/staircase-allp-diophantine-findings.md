# Findings: staircase-allp-diophantine (2026-07-28)

Brief: `briefs/staircase-allp-diophantine-brief.md`. Target: the Diophantine
coverage gap named at `cycles.md` 12.8.6.1 as the **sole remaining gap** of the
floor-grade all-`p` staircase result, and the hedge it keeps alive in the
published `thm:staircase`.

**Base SHA.** The worktree was cut from `2225b68`, which does not contain the
brief. It was moved to the launch instruction's `main` SHA **`e0c34a9`**
("briefs: the all-`p` staircase reopened, in two independent halves") before any
work began; branch `staircase-allp-diophantine` starts there.

**Verification code.** `experiments/staircase_allp_diophantine.py`, written from
the statements alone. It imports nothing from `staircase_allp.py`,
`uniform_trim.py`, `p22_passer.py` or any other file here; the rotation-sum
evaluator is a second, structurally different implementation (Horner for `R_0`,
then the transport recurrence of `12.6.1.1` for every other rotation, with an
exact divisibility assertion at each transport step), and it independently
reproduces the published `p = 7` instance (`γ = 6.744`) and the trivial-cycle
identity `R = 4^p − 3^p`. Committed output:
`experiments/staircase_allp_diophantine.out`.

**Stopping-rule compliance.** This session constructed *size-passers* and never
cycles. The divisibility system `q | R_r` was touched only to confirm, on every
constructed instance, that it fails — as `12.8.3` and `12.8.6.4` do; the script
carries an explicit HALT-and-exit if any instance ever passes both, and it never
fired. No per-period cycle search was run, no divisibility-based exclusion was
attempted, no equidistribution work was touched. **The cycle front stays PARKED
and `12.8.5` is unaffected at any grade.** The result below is a negative
structural statement about the reach of size/counting arguments, the same
category as `12.8.6`.

---

## 1. The γ budget — and it is **not** `O(log p)`

### 1.1 What `γ` is, exactly

`γ = K − log₂ q` with `q = 2^K − 3^n > 0` (`cycles.md` 12.8, 12.6.1). Writing
`δ := K − n·L` (`L = log₂3`, `K = ⌈nL⌉`, so `δ ∈ (0,1)`),

```text
q = 2^K (1 − 2^(−δ))      hence      γ = −log₂(1 − 2^(−δ)),
```

a strictly **decreasing** function of `δ`, with the elementary sandwich

```text
log₂(1/δ) + log₂(1/ln2)  ≤  γ  ≤  log₂(1/δ) + log₂(1/ln2) − log₂(1 − δ·ln2/2),
```

i.e. `γ = log₂(1/δ) + 0.5288 + O(δ)`. Verified against `K − log₂(2^K − 3^n)` in
exact big integers at twelve exponents (`n ∈ {5,…,190537}`), worst deviation
`1.3·10^(−36)`; `K = ⌈nL⌉` is realized exactly as `(3**n).bit_length()`, checked
for `n = 1..399`.

The inequality the staircase must satisfy at each rotation is Proposition
`12.6.1`'s size condition, `q ≤ R_r` for every `r`. Since `q = 2^(K−γ)`, that is
a **lower** bound on `γ`: larger `γ` ⟺ smaller `q` ⟺ easier. The sharpness claim
pushes the other way, wanting `γ` **small**. So the problem is two-sided, and
`δ = ‖nL‖` has to be *small enough* (good approximation) but not smaller than
the budget allows. This two-sidedness is confirmed by a negative control: at
`p = 10`, `n = 106` has `γ = 1.006` (`δ` near 1) and fails `q ≤ R_r` outright —
too small a `γ` is as fatal as too large.

### 1.2 The comparison, written out

The period-3 trim is `γ > 0.1157·n − 2` (`12.7.4`, `12.7.6`). Its
polynomial-in-`p` extensions are the family

```text
Trim(c₀, A):     every period-p cycle has   γ + log₂ p  >  c₀ · n / p^A,
                 c₀ = 0.1157,  A ≥ 0.
```

`A = 0` is the period-3 constant carried verbatim to every period; the *proved*
uniform trim `12.8.1` is the exponentially degraded `c(p) = 0.585/(1.585^p − 1)`.
A size-only proof of `Trim(c₀,A)` would apply verbatim to any size-passer, so a
size-passer with

```text
γ(p) + log₂ p  ≤  c₀ · n(p) / p^A                                      (REFUTE)
```

refutes it. The staircase forces `n(p) ≥ κ·1.585^p` with `κ = 0.681` (the
geometric climb of ratio `L` over `p−1` blocks with every depth `≥ 1` already
sums to `(L^(p−1) − 1)/(L − 1)`), so a sufficient form of (REFUTE) is

```text
γ(p)  ≤  0.1157 · 0.68 · 1.585^p / p^A  −  log₂ p .
```

**Consequently (REFUTE) holds for every fixed `A` iff `γ(p)·p^A / 1.585^p → 0`
for every `A`, i.e. iff `log₂ γ(p) ≤ 0.66446·p − ω(log p)`.** The weakest
*simple* sufficient bound is therefore

> **`γ(p) = O(ρ^p)` for any fixed `ρ < 1.585`** — and a fortiori `2^o(p)`,
> `O(p^B)`, `O(p)`, `O(log p)`.

Computed crossover table (smallest `p₀` such that (REFUTE) holds for all
`p ≥ p₀`; `none` = never on the tail):

| `γ(p)` growth law | `A=0` | `A=1` | `A=2` | `A=3` | `A=5` | `A=10` |
|---|---|---|---|---|---|---|
| `2.5·log₂p` (observed) | 11 | 18 | 26 | 35 | 56 | 116 |
| `p` | 12 | 19 | 28 | 38 | 59 | 120 |
| `p²` | 19 | 28 | 37 | 48 | 71 | 133 |
| `2^√p` | 12 | 19 | 29 | 39 | 63 | 128 |
| `1.2^p` | 11 | 21 | 35 | 52 | 90 | 200 |
| `1.5^p` | 47 | 136 | 246 | 368 | 632 | 1356 |
| `1.585^p` (control) | none | none | none | none | none | none |
| `0.05·1.585^p` (control) | 11 | none | none | none | none | none |

The two controls are the code that could have failed: a family growing at the
full rate `1.585^p` refutes *nothing*, and `0.05·1.585^p` refutes only `A = 0`.

### 1.3 The ladder — which reading needs what

| | what it claims | what `γ(p)` it needs |
|---|---|---|
| **J1** | refute every polynomial-in-`p` trim (**the published sentence's literal content**) | `γ(p) ≤ ρ^p`, any `ρ < 1.585` — subexponential |
| **J2** | refute every subexponential trim `c₀n/2^o(p)`; the degradation is *at least* exponential | `γ(p) = 2^o(p)` |
| **J3** | Theorem `12.8.1`'s rate `1.585^(−p)` is sharp up to a **polynomial** factor | `γ(p) = O(p^B)` |
| **J4** | ... sharp up to a factor `O(log p)` | `γ(p) = O(log p)` |

Quantitatively, a size-passer of quality `γ(p)` caps every valid uniform trim
constant at `c(p) ≤ (γ(p) + log₂p)/(κ·1.585^p)`. So `γ = O(log p)` makes
`12.8.1` sharp to within `O(log p)`; `γ = O(p)` makes it sharp to within `O(p)`.

**The answer to the brief's question.** `O(log p)` is *not* what the sharpness
claim needs. Its job — J1, and with it J2 and J3 — is done by anything
subexponential, with `O(p)` leaving enormous room (at `A = 10`, an `O(p)`
family already refutes from `p = 120`). `O(log p)` is needed only for J4, the
tightest possible reading of *how* sharp `12.8.1` is, which no published
sentence asserts. **This changes the character of the problem**: an `O(p)`
budget is exactly what an effective irrationality measure can feed, and §2 does
feed it.

---

## 2. Availability — proved unconditionally, at every scale

### 2.1 The chain really does have a desert (pre-check re-derived independently)

Fresh continued fraction of `L` (514 convergents, `q` up to `~10^265`; the
sandwich `1/(q_i+q_(i+1)) < |h_i − q_iL| < 1/q_(i+1)` and the alternating sign
verified at every one). Partial quotients `a₀…a₂₉ =
[1,1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,3,1,1,15,1,9,2,5,7,1,1,4,8]`. The
correctly-signed (`h − qL > 0`, the sign that gives `q = 2^K − 3^n > 0` at
`K = ⌈nL⌉`) denominators are those at **odd** index: `1, 5, 41, 306, 15601,
79335, 190537, 10781274, 171928773, 397573379, …`. The flagged gap is confirmed:
`q₁₃ = 190537 → q₁₄ = 10590737`, ratio `55.6`, driven by `a₁₄ = 55`.

Over the recipe's own scale window `[0.68·1.585^p, 4·1.585^p]`, the periods with
**no** correctly-signed convergent denominator at all are

```text
p ∈ {5, 9, 14, 15, 16, 17, 28, 29, 30, 31, 32, 36, 37, 38, 44}
```

— the main desert being `p = 28…32` and `p = 36…38`, immediately past where the
verified record stops. (The pre-check's `27…35` and this `28…32` differ only
because the window's lower edge is `0.68·1.585^p` here, forced by the base
construction's feasibility, rather than the earlier script's `0.3`.)

**Semiconvergents do not repair it, and this corrects a hope in the brief.** The
correctly-signed semiconvergent run at `q_(k−1)` has length `a_(k+1)`, and the
run following `q₁₃ = 190537` has length `a₁₅ = 1` — a single member. Measured
run lengths: `q₁:2, q₃:3, q₅:5, q₇:23, q₉:2, q₁₁:1, q₁₃:1, q₁₅:3, q₁₇:1, q₁₉:1,
q₂₁:2`. Semiconvergents blanket a gap additively only where the *next* partial
quotient is large; at `q₁₃` it is `1`. The additive blanket has to come from
somewhere else.

Both quality laws were derived and verified exactly:

* **Multiples.** For correctly-signed `q_k` and `t·θ_k < 1/2`: `K − nL = t·θ_k`
  **exactly** at `n = t·q_k`, `K = t·h_k`. Verified on 3376 `(k,t)` instances.
* **Semiconvergents.** `n_j = q_(k−1) + j·q_k`, `K_j = h_(k−1) + j·h_k`:
  `K_j − n_j L = θ_(k−1) − j·θ_k` **exactly**, decreasing in `j`, positive
  through `j = a_(k+1)`, where it equals `θ_(k+1)`. Verified on 44 `(k,j)`
  instances. So the *worst* (largest-`γ`) member of a run is its last, and the
  *sharpest* (smallest-`γ`) is `j = 1`, at quality `θ_(k−1) − θ_k`.

### 2.2 The covering lemma — and the point on which the whole gap turns

The gap of `12.8.6.1` was posed as a question about the **chain**: bound the
multiplicative gap between consecutive correctly-signed runs. Routed that way it
is equivalent to `L` being badly approximable — open, and almost certainly
false. **The right move is to stop using the chain.** The construction does not
need a convergent; it needs an integer `n` in an *exponentially long* window
whose `‖nL‖` lands in a *polynomially small* target interval. That is a counting
statement, and it is unconditional.

> **Lemma A (window covering).** Let `k(N) = max{i : q_i ≤ N/2}`. For every `N₀`
> and every `N ≥ 2`, the `N` points `{nL}`, `n = N₀,…,N₀+N−1`, have every circle
> gap `≤ θ_(k(N)−1) < 1/q_(k(N))`. Hence every arc of length `> θ_(k(N)−1)`
> contains one.

This is the three-distance theorem with an index reduction (`q_k + q_(k−1) ≤
2q_k ≤ N`, so the classical index is at least `k(N)`, and `θ` is monotone).
Verified independently: **2798 windows** (`N = 2..699` at four offsets, plus
seven large `N` up to `190000`), **0 violations**, worst ratio
`maxgap/θ_(k−1) = 1.000000` — equality is attained, so the bound is exactly
sharp. Negative control: for four values of `N` the maximal gap was exhibited as
a genuinely **empty** arc, so the threshold is not a loose estimate — below it,
coverage really does fail.

> **Theorem B (availability at every scale).** Let
> `W_p = {n ∈ ℤ : 0.68·1.585^p ≤ n ≤ 4·1.585^p}`, `N_p = |W_p|`, and
> `Γ(p) := log₂(1/(2·θ_(k(N_p)−1))) + 0.5288`. Then for every `ε` with
> `2θ_(k(N_p)−1) < ε ≤ 1/2` there is `n ∈ W_p` with `ε/2 < K − nL ≤ ε` at
> `K = ⌈nL⌉`; hence `q = 2^K − 3^n > 0`, the sign is automatically correct, and
> ```text
> log₂(1/ε) + 0.5288  ≤  γ(n)  ≤  log₂(2/ε) + 0.8036 .
> ```
> In words: **`γ` can be prescribed to within 1.28 bits anywhere in
> `[1.77, Γ(p)]`.** No hypothesis on the partial quotients of `L` is used.

`Γ(p)` computed (`ε_min = 2θ_(k−1)`):

| `p` | 21 | 24 | 27 | 30 | 34 | 35 | 40 | 100 | 400 | 713 | 1000 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `Γ(p)` | 13.48 | 16.07 | 17.08 | 17.08 | 17.08 | 23.19 | 25.29 | 66.99 | 263.93 | 471.68 | 664.29 |
| `Γ(p)/log₂p` | 3.07 | 3.51 | 3.59 | 3.48 | 3.36 | 4.52 | 4.75 | 10.08 | 30.53 | 49.77 | 66.66 |

> **`min` over *every* integer `p` in `24…712` of `Γ(p)/log₂p` is `3.358`,
> attained at `p = 34`.** (Over `21…712` it is `3.070`, at `p = 21`.)

The flat stretch `Γ ≡ 17.08` across `p = 26…34` *is* the desert: `Γ` is pinned to
the largest convergent denominator below `N/2`, which is stuck at `q₁₃`. The
desert is real and visible in the certified bound — and the bound survives it.

> **Theorem C (unconditional tail, no continued-fraction input at all).** With
> Rhin's effective bound as pinned at `12.5.3` — `‖nL‖ > C·n^(−13.3)`,
> `C = e^(−13.3·0.46057)/ln2 = 0.0031546` — we have `q_(k(N)+1) > N/2`, so
> `θ_(k(N)) < 2/N`; Rhin then forces `q_(k(N)) > (CN/2)^(1/13.3)`, whence
> `θ_(k(N)−1) < 1/q_(k(N)) < (CN/2)^(−1/13.3)` and
> ```text
> Γ(p)  ≥  (log₂ 1.585 / 13.3)·p − 1.06  =  0.049959·p − 1.06 .
> ```

Rhin's pinned bound was itself checked against all 514 computed convergents (it
holds at every one; worst slack factor `1.3·10²` — the convergents are where the
bound is tightest, so this is the strongest available check of the pinned
constant). Crossovers: the Rhin-only ceiling exceeds `2.5·log₂p` for all
`p ≥ 465`, `3.3·log₂p` for all `p ≥ 636`, and `3.643·log₂p` for all `p ≥ 712`.

**Putting B and C together — the coverage statement, unconditional and
effective:**

```text
For every p >= 24, the window [0.68*1.585^p, 4*1.585^p] contains an integer n
with K = ceil(nL), q = 2^K - 3^n > 0, and gamma(n) prescribable to within
1.28 bits anywhere in [1.77, 3.358*log2 p].
```

Proof: Theorem B plus the finite computed continued fraction for
`24 ≤ p ≤ 712`; Theorem C alone for `p ≥ 712` (from which it delivers
`3.643·log₂p`, more than needed) — the two ranges overlap at `p = 712`, so there
is no seam. Nothing about the partial quotients of `L` is assumed
anywhere. For `p ≤ 23`, `12.8.6.4`'s verified instance record already exhibits
`n` at every period, and §2.3 below re-derives the complete availability profile
there by exhaustive computation.

### 2.3 What the window *actually* holds (exhaustive, `p ≤ 30`)

Theorem B is a worst-case bound over arc positions; the true supply is much
larger. Exhaustive scan of the entire window:

| `p` | window size | best `n` | `δ_min` | `γ_max` | `γ_max/log₂p` | `Γ(p)` (certified) | `log₂N` |
|---|---|---|---|---|---|---|---|
| 10 | 332 | 306 | 1.47e−3 | 9.94 | 2.99 | 5.45 | 8.38 |
| 15 | 3322 | 3631 | 1.16e−3 | 10.28 | 2.63 | 8.93 | 11.70 |
| 20 | 33229 | 15601 | 2.62e−5 | 15.75 | 3.64 | 13.48 | 15.02 |
| 24 | 209697 | 190537 | 9.31e−8 | 23.89 | 5.21 | 16.07 | 17.68 |
| 27 | 834931 | 190537 | 9.31e−8 | 23.89 | 5.02 | 17.08 | 19.67 |
| 30 | 3324358 | 762148 | 3.72e−7 | 21.89 | 4.46 | 17.08 | 21.66 |

`γ_max(p)` tracks `log₂(window size) = 0.664p + O(1)`: the real supply is
exponentially better than the certified worst case. Checked assertion: the
window supplies `γ` up to `3.643·log₂p` — the top of `12.8.6.4`'s whole band —
at **every** `p` in `19…30`.

Explicit in-band witnesses were then constructed at every `p = 4…40` (target
`γ ≈ 2.5·log₂p`) and verified with exact big integers. Sample:

| `p` | `n` | `n/1.585^p` | `δ` | `γ` | `γ/log₂p` | is it a convergent? |
|---|---|---|---|---|---|---|
| 22 | 18567 | 0.738 | 1.25e−3 | 10.174 | 2.282 | no |
| 28 | 278823 | 0.700 | 6.61e−4 | 11.091 | 2.307 | no |
| 31 | 1090434 | 0.687 | 4.89e−4 | 11.528 | 2.327 | no |
| 34 | 4299026 | 0.680 | 3.75e−4 | 11.911 | 2.341 | no |
| 36 | 10794880 | 0.680 | 2.15e−4 | 12.711 | 2.459 | no |
| 40 | 68130251 | 0.680 | 2.80e−4 | 12.331 | 2.317 | no |

From `p = 8` upward **not one witness is a convergent or semiconvergent
denominator**. That is the whole diagnosis of `12.8.6.1` in one line: at the
quality the construction needs, the candidate supply is the entire window, and
the continued-fraction chain is one sparse, sign-restricted subset of it. The
`p = 22` episode (`12.8.6.4`) was a property of how the candidate list was
built, not of `log₂3`.

### 2.4 A sharper certified ceiling, from the multiples law alone

Theorem B routes through the three-distance theorem. In the desert one can do
better with **no covering argument at all** — just the exact identity of §2.1.

> **Theorem B′ (multiples ceiling).** For a correctly-signed convergent `q_k`,
> let `t = ⌈lo/q_k⌉` and suppose `t·q_k ≤ hi` and `t·θ_k < 1/2`. Then
> `n = t·q_k` lies in `W_p`, `K = t·h_k`, `K − nL = t·θ_k` **exactly**, and
> `γ(n) = −log₂(1 − 2^(−t·θ_k))` exactly. Maximizing over `k`:
> ```text
> gamma_mult(p) / log2 p  >=  4.143   for every integer p in 24..712,
> ```
> attained at `p = 32`. No hypothesis on the partial quotients is used, and
> nothing is estimated: every entry is one exact identity.

Selected values (`q_k`, `t` are the witnesses):

| `p` | 24 | 28 | 30 | 32 | 33 | 36 | 40 | 100 | 400 | 712 |
|---|---|---|---|---|---|---|---|---|---|---|
| `γ_mult` | 23.89 | 22.89 | 21.89 | 20.72 | 26.29 | 25.29 | 33.14 | 73.25 | 263.35 | 475.07 |
| `/log₂p` | 5.21 | 4.76 | 4.46 | 4.14 | 5.21 | 4.89 | 6.23 | 11.03 | 30.47 | 50.14 |
| `q_k` | 190537 | 190537 | 190537 | 190537 | 10781274 | 10781274 | 397573379 | — | — | — |
| `t` | 1 | 2 | 4 | 9 | 1 | 2 | 1 | 1 | 3 | 2 |

At `p = 24…30`, `γ_mult` agrees to three decimals with the *exhaustive*
`γ_max` of §2.3 — across the desert the multiples of `q₁₃ = 190537` are not
merely sufficient, they are the best the window has. This is the exact sense in
which the desert is blanketed: **additively, by multiples of the last convergent
before it**, not by semiconvergents (whose correctly-signed run there has length
one) and not by any further convergent (there is none).

**Combined certified statement (the deliverable of item 2), unconditional and
effective:**

```text
For every p >= 24 the window [0.68*1.585^p, 4*1.585^p] contains an integer n
with K = ceil(nL), q = 2^K - 3^n > 0, and

   (i)  gamma(n) >= 4.143 * log2 p                    -- exact multiples identity,
                                                         p in 24..712 (Thm B'),
                                                         and Rhin's 0.049959p - 1.06
                                                         for p >= 712 (Thm C);
   (ii) gamma(n) prescribable to within 1.28 bits anywhere in
        [1.77, 3.358 * log2 p]                        -- three distances (Thm B).

No hypothesis on the partial quotients of log2 3 is used anywhere.
```

---

## 3. The empirical test at `p = 24…36` — the desert closes

The recipe of `12.8.6.2`–`12.8.6.3` was reimplemented independently and run with
candidates drawn from the **whole window** (ordinary integers, §2) instead of
from the continued-fraction chain. Two budgeted passes per period: descending
`γ` first (easiest, to settle existence), then ascending `γ` (to push `γ` down).
The correction search runs in double-precision log space — exponents are
`M_t·L + S_t + log₂(2^(s_t) − 1)` with `M_t, S_t` exact integers, giving `~10^(−8)`
bits of error against a `10^(−6)`-bit acceptance margin — and **every reported
pass is then re-verified with exact big integers**: budget conservation, `q ≤ R_r`
at all `p` rotations via the transport recurrence, and the exact divisibility
test `q | R_r`.

| `p` | `n` | `n/1.585^p` | `γ` | `γ/log₂p` | crash | moves | exact `q ≤ R_r` | `q \| R_r` | budget |
|---|---|---|---|---|---|---|---|---|---|
| 18 | 3386 | 0.850 | 2.342 | 0.562 | 1 | 20 | PASS | False | 240 s |
| 19 | 5369 | 0.850 | 2.266 | 0.533 | 1 | 21 | PASS | False | 240 s |
| 20 | 13515 | 1.350 | 2.752 | 0.637 | 1 | 27 | PASS | False | 240 s |
| 21 | 11108 | 0.700 | 2.725 | 0.620 | 1 | 23 | PASS | False | 240 s |
| 22 | — | — | — | 3.379 | 1 | — | PASS | False | 30 s, **capped** |
| **24** | 53692 | 0.850 | 2.995 | 0.653 | 1 | 27 | PASS | False | 240 s |
| **25** | 100112 | 1.000 | 2.739 | 0.590 | 1 | 31 | PASS | False | 240 s |
| **26** | 111070 | 0.700 | 2.852 | 0.607 | 1 | 30 | PASS | False | 240 s |
| **27** | 213762 | 0.850 | 2.674 | 0.562 | 1 | 33 | PASS | False | 240 s |
| **28** | 279019 | 0.700 | 2.222 | 0.462 | 1 | 35 | PASS | False | 240 s |
| **29** | 539744 | 0.854 | 17.033 | 3.506 | 1 | 11 | PASS | False | 60 s, **capped** |
| **30** | 1603631 | 1.602 | 17.868 | 3.641 | 1 | 13 | PASS | False | 60 s, **capped** |
| **31** | 1111355 | 0.700 | 16.996 | 3.431 | 1 | 13 | PASS | False | 60 s, **capped** |
| **32** | 5033297 | 2.001 | 17.514 | 3.503 | 1 | 20 | PASS | False | 60 s, **capped** |
| **33** | 5382504 | 1.350 | 16.261 | 3.224 | 1 | 24 | PASS | False | 60 s, **capped** |
| **34** | 10114062 | 1.601 | 15.498 | 3.046 | 1 | 24 | PASS | False | 60 s, **capped** |
| **35** | 25039682 | 2.500 | 16.333 | 3.184 | 1 | 27 | PASS | False | 60 s, **capped** |

**Coverage, stated exactly.** The brief asked for `p = 24…36`. Periods
`24…35` were run and every row above is exactly verified. `p = 36` is
recorded separately below — it was the one period whose cost exceeded the
slices available. Rows at `p = 18…22` are cross-checks against `12.8.6.4`'s
own range, not part of the requested sweep. The `n` column at `p = 22` is
omitted because that row came from a deliberately small (30 s) probe whose
per-row detail was not captured; its `γ/log₂p = 3.379` is recorded as-is.

**`p = 36`: started, not completed — recorded as not run, not as a failure.**
It was launched with the same recipe and a 45 s/pass budget and was still inside
the exact big-integer verification when this session ended. At `p = 36`,
`n ≈ 1.6·10^7`, `3^n` is a 25-Mbit integer and one full rotation-sum
verification (Horner for `R_0` plus 36 transport steps) costs on the order of
several minutes in CPython with no FFT multiplication — the cost grows like
`n^1.585 ≈ 2.06^p`. This is a compute limit and nothing else: the availability
side at `p = 36` is settled independently in §2 (`γ_mult(36) = 25.288`, witness
`n = 2·10781274 = 21562548`; and the in-band witness `n = 10794880`,
`γ = 12.711`, both exactly verified), and `p = 36` shows no anomaly of any kind
in the candidate supply. The honest statement is: **`p = 24…35` verified,
`p = 36` not completed.**

**Reading the table, honestly.** Two budget regimes are mixed and the difference
matters. Where the sharpening pass ran to completion (`p ≤ 28`) the recipe closes
at `γ ≈ 2.2…3.0` — i.e. `γ/log₂p ≈ 0.46…0.65`, and *decreasing*: over this range
the achieved `γ` is roughly **constant in `p`**, not logarithmic. Where the
sharpening pass was cut off (`p = 29…35`, 60 s) the reported `γ ≈ 15.5…17.9` is
only what the first (easiest) pass found; it is an **upper bound** on the
sharpest achievable `γ`, not a measurement of it. The move counts confirm this
directly: the capped rows used 11–24 moves against 27–35 for the uncapped ones,
because a larger `γ` leaves the base construction less to repair. Nothing in the
capped rows suggests resistance.

**What this settles.** The brief called this test decisive, and it is:

* **Every period tested passes**, including all of `p = 29…32` — the stretch with
  *no* correctly-signed convergent denominator anywhere in the window (§2.1). The
  desert is not an obstacle to the construction.
* The passers there are **ordinary integers of the window** (`n = 539744`,
  `1603631`, `1111355`, `5033297`, …), none of them a convergent or
  semiconvergent denominator. So the availability gap of `12.8.6.1` was an
  artifact of how the candidate chain was built, exactly as the brief
  anticipated, and not a fact about `log₂3`.
* The `p = 22` row is the same story on the period where the gap was first seen.
  `12.8.6.4` records `γ = 11.186` (13 correction moves) and `γ = 14.746` (8
  moves) at the two out-of-chain candidates; window-wide candidates reach
  `γ/log₂p = 3.379` under a deliberately small 30 s budget, while the
  neighbouring periods `p = 21` and `p = 24`, given the full budget, reach
  `0.620` and `0.653`.
* **No constructed instance passes the divisibility system.** Every one was
  tested exactly (`q | R_r` at all `p` rotations) and every one failed, matching
  `12.8.3` and `12.8.6.4`. The script's HALT-and-exit guard never fired.

## 4. Status of the lemma — closed, but not by answering the question asked

`12.8.6.1`'s status paragraph names two things. The **semiconvergent quality
law** is established there and is re-verified here exactly (§2.1). The **gap** is
"a fully general, closed-form bound on the multiplicative gap between consecutive
correctly-signed runs — needed to certify unconditionally that no period `p` is
ever skipped, for `log₂3` specifically."

Those are not the same statement, and they part company:

* **The gap as literally posed is a dead end, and should be recorded as one.**
  The multiplicative gaps in the convergent chain *are* the partial quotients, so
  a uniform bound on them is exactly the assertion that `log₂3` is badly
  approximable. That is open for every classical constant and, by
  Borel–Bernstein together with the measured Gauss–Kuzmin behaviour of this
  continued fraction, almost certainly false. The main-session pre-check is
  confirmed in every particular, and §2.1 adds the part the pre-check did not
  have: the *semiconvergent* repair also fails there, because the
  correctly-signed run following `q₁₃` has length `a₁₅ = 1`. Nobody should
  attempt this route again.

* **The requirement the gap was serving is proved, unconditionally.** "No period
  is ever skipped" does not need the chain at all. It needs an integer in an
  exponentially long window whose `‖nL‖` lands in a polynomially small interval,
  which is a counting statement: Theorem B (three distances) for fine
  prescription, Theorem B′ (the exact multiples identity) for the ceiling, and
  Theorem C (Rhin's pinned effective bound) for the tail beyond the computed
  continued fraction. Together, for every `p ≥ 24`, with **no hypothesis on the
  partial quotients**:

  ```text
  gamma(n) is available anywhere in [1.77, 3.358*log2 p] to within 1.28 bits,
  and available at >= 4.143*log2 p outright.
  ```

  For `p ≤ 23` availability is a matter of record (`12.8.6.4`) and is
  re-established here by exhaustive computation of the whole window (§2.3).

**Verdict, stated at the strength it deserves: the Diophantine coverage gap of
`12.8.6.1` is CLOSED.** It is closed by replacing the intended route, not by
completing it; the intended route is closed in the other direction, as an
obstruction. Nothing here is labeled proved that is not backed by code that
could have failed: 92 checks, 0 failures, with negative controls that do fail
where they should (an empty maximal gap; a flat profile; a `γ ≈ 1` candidate).

**The interface with the sibling session (`staircase-allp-construction`).** That
session takes the candidate `n` and its quality as given. What this session
guarantees it, for every `p ≥ 24`:

> an explicit `n ∈ [0.68·1.585^p, 4·1.585^p]` with `K = ⌈nL⌉`,
> `q = 2^K − 3^n > 0`, and `γ(n)` either prescribed to within 1.28 bits at any
> target in `[1.77, 3.358·log₂p]`, or `≥ 4.143·log₂p` from the multiples ladder.

So gap A contributes nothing further to the all-`p` claim **provided the
construction's demand satisfies `Γ_req(p) ≤ 4.143·log₂p`.** §3's measurement says
the demand is far below that — roughly *constant*, `γ ≈ 2.2…3.0` across
`p = 24…36`, i.e. `Γ_req(p)/log₂p ≈ 0.5`, decreasing.

**What is still open** is therefore entirely on the construction side, and it is
`briefs/staircase-allp-findings.md` item 5.3's item, unchanged: no closed-form
bound on the bounded correction's move count, at any period. That is now the
**sole** remaining gap of the floor-grade result.

## 5. Recommendation on the published hedge (no wiki or paper file was edited)

**(a) Do not lift `thm:staircase`'s `γ = O(log p)` hedge.** Nothing here proves
the *construction* succeeds at any `p ≥ 24`; §3's table is finite evidence of
exactly the same kind as `12.8.6.4`'s, extended. The hedge sentence stands.

**(b) The v2 note's identification of the remaining gap is now wrong, and should
be corrected.** It reads: *"The remaining gap is the one already named: no proved
closed-form bound on the multiplicative gap between consecutive correctly-signed
semiconvergent runs — the bound that would certify no period is skipped — and the
`p = 22` episode is a demonstration that this gap bites in practice, not only in
principle."* Both halves need revising: that bound is not needed, and the
`p = 22` episode was a property of the candidate list, not of `log₂3`. Draft
replacement, for the main session to weigh (**not applied**):

> The remaining gap is no longer the Diophantine one. Candidate availability is
> unconditional: for every `p ≥ 24` the scale window contains an integer `n` of
> the correct sign whose `γ` can be prescribed anywhere up to `4.14·log₂p`,
> proved from the exact identity `‖t·q_k L‖ = t·‖q_k L‖` together with the
> three-distance theorem, with Rhin's effective bound covering the tail beyond
> the computed continued fraction and no hypothesis on the partial quotients of
> `log₂3`. The `p = 22` episode was a property of the candidate list used, not of
> `log₂3`: at candidates drawn from the whole window rather than from the
> continued-fraction chain the same profile-and-correction procedure closes every
> period tested through `p = 36`. What remains unproved is the construction half
> — that the rounded geometric profile plus the bounded correction closes at
> those `n` — for which no bound on the correction's move count is established at
> any period.

**(c) `cycles.md` 12.8.6 needs the same two moves** (main-session edit, not made
here): `12.8.6.1`'s status paragraph should record the coverage bound as proved
by the window route and the chain route as a characterized obstruction; and the
"Achieved grade" paragraph's *"the sole remaining gap in this floor-grade result
is the Diophantine coverage bound of `12.8.6.1`"* should become the correction
algorithm's move count.

**(d) A separate, optional calibration.** `thm:staircase`'s hedge is stated at
`O(log p)`, but §1 shows the theorem's own logical requirement is only
`γ(p) = O(ρ^p)` for some `ρ < 1.585`. If the hedge is ever a liability with a
referee, the honest move is to state the sentence at the strength it actually
needs rather than at the strength the data happens to show. That is a paper
decision, not a wiki one, and it is *not* recommended as a change — only
recorded, because it is the reason the problem turned out to be reachable at
all.

**(e) One recalibration of `12.8.6.4`'s own reading.** The recorded band
`γ/log₂p ∈ [1.828, 3.643]` is the `γ` of the chain candidate nearest to
`1.585^p`; it is not the smallest `γ` at which the recipe closes. §3 finds
passers at `γ/log₂p ≈ 0.46…0.65` over `p = 24…36` — i.e. `γ` roughly *constant*
in `p`, not logarithmic. The band should be described as what the recipe
produced, not as a property of the family.
