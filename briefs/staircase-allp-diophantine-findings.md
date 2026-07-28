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
`24 ≤ p ≤ 712`; Theorem C alone for `p ≥ 713` (where it delivers `3.643·log₂p`,
more than needed). Nothing about the partial quotients of `L` is assumed
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
                                                         for p >= 713 (Thm C);
   (ii) gamma(n) prescribable to within 1.28 bits anywhere in
        [1.77, 3.358 * log2 p]                        -- three distances (Thm B).

No hypothesis on the partial quotients of log2 3 is used anywhere.
```

---

## 3. The empirical test at `p = 24…36`

PLACEHOLDER — running.

## 4. Status of the lemma

PLACEHOLDER.

## 5. Recommendation on the published hedge

PLACEHOLDER.
