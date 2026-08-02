# Findings: does Inselmann's horizon convert to `1/β` reduced blocks? (v3 round 3, delegate B)

**Task:** `briefs/v3r3-inselmann-horizon-brief.md`. Read-only round; the only file written is this one.
**Read at:** `main` = `dc61306`, working tree clean apart from the round-3 briefs.
**Sources obtained and read this session, from the primary PDFs:**

* Inselmann, arXiv:2402.03276**v3** (13 Aug 2024), pp. 1–30 read page by page (`https://arxiv.org/pdf/2402.03276v3`).
* Tao, arXiv:1909.03562**v7**, pp. 5–14 and 54–57 read page by page (`https://arxiv.org/pdf/1909.03562v7`); journal ref. *Forum Math. Pi* **10** (2022) e12.

Everything marked **[P]** below is transcribed from those pages. Nothing here is reconstructed from memory, from an abstract, or from `briefs/v3r2-contraction-literature-findings.md`.

---

## 0. Verdict, in one sentence

**The conversion is circular: Inselmann's horizons are theorems in *step* time, and reading his `α = 2(log(4/3))^{-1}` as `θ = 1/β` *reduced blocks per bit* divides by `E[m] = 2` Syracuse steps per block — the frequency with which a Syracuse step ends a block, a pair statistic of the parity word that neither his Theorem 1.10 nor his Theorem 1.6 supplies and that Hypothesis 13.2.1 itself asserts — so the repository's unconditional horizon in block units remains `θ < 1/4`, and it comes from the repository's own cylinder count, not from Inselmann.**

Answer to the brief's Part 1 item 4: **(b), with the exact remainder that (c) holds at `θ < 1/4`.** The reviewer's objection is correct as stated, and is sharper than stated: the conversion runs not through `E[m] = 2` as a first moment but through `P(s ≥ 2) = 1/2`, a two-letter statistic of the parity word, and the only unconditional source for that statistic in the literature is Terras's exact cylinder count, whose range is *exactly* the `θ < 1/4` frontier the conversion was invoked to cross.

Two things do survive intact and should be kept (§5): the **extension factor** `4.8188…`, which is the same number in either time and is unconditional; and the **`α = (log 2)^{-1} ↔ θ = 1/4` end**, which matches for a reason the repository can prove.

---

## 1. The source statements, verbatim

### 1.1 Inselmann's map, his `log`, and his density notions **[P]**

Abstract, p. 1: "*Define the map `T` on the positive integers by `T(m) = m/2` if `m` is even and by `T(m) = (3m+1)/2` if `m` is odd.*" The abstract's `α log m` uses **natural** log; the theorem statements in the body use `log₂`.

p. 2: "*the main result of this paper is that the approximation `T^k(m) ≈ (√3/2)^k m` is indeed correct for `0 ≤ k ≤ log₂ m/(1 − log₂√3)` on a set of natural density 1 (where a set `A ⊆ ℤ⁺` is of **natural density** 1 if `liminf_{n→∞} #{m ∈ A | m ≤ n}/n = 1`).*"

Definition 1.2(3), p. 2: "*To each `m ∈ ℤ⁺`, we associate its **parity sequence** `(p(m)_k)_{k∈ℕ}`, which is defined by `p(m)_k = 0` if `T^k(m)` is even, `1` if `T^k(m)` is odd.*"

Definition 2.6, p. 8: "*Suppose that `C > 0`, `0 < D ≤ 1`, and `S ⊆ ℤ⁺`. Then `S` has `(C,D)`-**density** if `μ_{[1…N]}(S ∩ [1…N]) ≥ 1 − C/N^D` for every `N ∈ ℤ⁺`. … we say that `S ⊆ ℤ⁺` is `∗`-**dense** if `S` has `D`-density for some `0 < D ≤ 1`.*"
p. 2: "*Note that any `∗`-dense set `S ⊆ ℤ⁺` is of natural density 1*"; p. 3: "*Note that sets of natural density 1 do not have this property.*"

### 1.2 Theorem 1.1 (p. 2) **[P]**

> *Suppose that `ε > 0`. Then the set*
> `{ m ∈ ℤ⁺ | ∀0 ≤ k ≤ log₂ m/(1 − log₂√3) : (√3/2)^k m^{1−ε} ≤ T^k(m) ≤ (√3/2)^k m^{1+ε} }`
> *is of natural density `1`.*

`k` counts **`T`-steps** (the one-division map). `(1 − log₂√3)^{-1} = 4.818841679306416`.

### 1.3 Theorem 1.3 and Corollary 1.4 (p. 4) **[P]**

> **Theorem 1.3.** *Suppose that `ε > 0`. Then the set `{ m ∈ ℤ⁺ | ∀λ ∈ [0,1] : m^{λ−ε} ≤ T^{⌊((1−λ)/(1−log₂√3)) log₂ m⌋}(m) ≤ m^{λ+ε} }` is of natural density `1`.*

> **Corollary 1.4.** *Suppose that `ε > 0`. Then the set `{ m ∈ ℤ⁺ | T^{⌊log₂ m/(1−log₂√3)⌋}(m) ≤ m^ε }` is of natural density `1`.*

**Corollary 1.4 is a `T`-time statement**, at `T`-time `⌊log₂ m/(1−log₂√3)⌋`, not a Syracuse-time or block-time statement. (`aeh.md` L42 attaches it to the Syracuse sentence with the word "there"; see §6.1.)

### 1.4 Theorem 1.6 (p. 5) **[P]**

> *Let `ε > 0`. Then the set*
> `{ m ∈ ℤ⁺ | ∀0 ≤ k ≤ log₂ m/(1 − log₂√3) : −ε log₂ m ≤ Σ_{i=0}^{k−1} p(m)_i − k/2 ≤ ε log₂ m }`
> *is of natural density `1`.*

This is the **running count of odd `T`-steps** — a single-letter statistic of the parity word. It is not a run-length statement and carries no information about consecutive parities.

### 1.5 The Syracuse map, the heuristic preceding Theorem 1.10, and Theorem 1.10 (p. 5) **[P]**

> *let `ν₂(m)` denote the maximal natural number `k` such that `2^k` divides `m`. Then define the **Syracuse map** … by `Syr : D⁺ → ℤ⁺; m ↦ (3m+1)/2^{ν₂(3m+1)}`.*
> *Heuristically, the probability that `ν₂(3m + 1)` equals `k`, is `2^{−k}` for `k ≥ 1`. Thus, `log₂(Syr(m)/m) ≈ log₂3 − k` with probability `2^{−k}`. Therefore, one expects `log₂(Syr(m)/m)` to be `Σ_{k=1}^∞ (log₂3 − k)2^{−k} = log₂3 − 2 = log₂(3/4)`. Thus, heuristically, `Syr^k(m) ≈ (3/4)^k m` for `0 ≤ k ≤ (log₂(4/3))^{-1} log₂ m`. We show that this heuristic is indeed correct. For this theorem, define a set `A ⊆ D⁺` to be of natural density 1 in `D⁺` if `liminf_{n→∞} #{m ∈ A | m ≤ 2n+1}/(n+1) = 1`.*

> **Theorem 1.10.** *Suppose that `ε > 0`. Then the set*
> `{ m ∈ D⁺ | ∀0 ≤ k ≤ (log₂(4/3))^{-1} log₂ m : (3/4)^k m^{1−ε} ≤ Syr^k(m) ≤ (3/4)^k m^{1+ε} }`
> *is of natural density `1` in `D⁺`.*

`k` counts **Syracuse steps** (odd-to-odd). `(log₂(4/3))^{-1} = 2.4094208396532095`.

### 1.6 Theorem 1.9 (p. 5) and the `Col` horizon **[P]**

> *Suppose that `ε > 0`. Then the set `{ m ∈ ℤ⁺ | ∀0 ≤ k ≤ 3 log₂ m/(2 − log₂3) : (∛(3/4))^k m^{1−ε} ≤ Col^k(m) ≤ (∛(3/4))^k m^{1+ε} }` is of natural density `1`.*

`3/(2 − log₂3) = 7.2282625189596255` raw `Col`-steps per bit.

### 1.7 How Inselmann himself passes from `T`-time to Syracuse time (Theorem 3.8, pp. 29–30) **[P]**

The `∗`-density version of Theorem 1.10 is Theorem 3.8. Its proof takes `Q` from Theorem 2.18 (the `T`-envelope) and `S` from **Theorem 3.3 (= Theorem 1.6)**, and then:

> *Note that, by definition of `Syr`, if `m ∈ D⁺`, `j ∈ ℕ`, and `p(m)_j = 1`, then*
> `Syr^{Σ_{i=0}^{j−1} p(m)_i}(m) = T^j(m)`.  (3.20)

> *Define `k₀ = ⌊(log₂ 4/3)^{-1} log₂ m⌋`, `L₀ = ⌊log₂ m/(1 − log₂√3)⌋`, and `k_max = Σ_{i=0}^{L₀} p(m)_i − 1`.*

and then (3.22)–(3.24) give `k₀ − k_max ≤ δ log₂ m + 1`.

**This is the decisive structural fact.** Inselmann's Syracuse horizon is his `T` horizon *divided by 2*, and the "2" is `E[s] = 2` `T`-steps per Syracuse step, which he **proves** (Theorem 1.6, applied through (3.20)). His `k₀ = L₀/2` up to `δ log₂ m` because `2(1 − log₂√3) = 2 − log₂3 = log₂(4/3)` — an identity, and the theorem is what licenses using it as a time change.

### 1.8 What statistical input the whole paper uses **[P]**

Read cover to cover through §3: the *only* distributional inputs are

* **Proposition 2.4** (p. 7), attributed to Terras [12, Thm. 1.2] and Everett [4, Thm. 1]: "*Suppose that `M ∈ ℤ⁺` and `N ∈ ℕ`. Then the push-forward measure of the uniform measure on `[M…M + 2^N)` under the map `m ↦ (p(m)_i)_{0≤i<N}` is the uniform measure on `{0,1}^{[0…N)}`.*" — the full cylinder law, but valid only on the **classical range** `N ≤ log₂(window)`;
* **Lemma 2.5** (p. 7), Hoeffding applied to `|Σ_{k<N} p(m)_k − N/2|`;
* **Lemma 2.9** (p. 9) and **Lemma 2.17** (p. 17), both bounding `Σ_{i<k} p(m)_i − k/2`.

**Nowhere in the paper is any pattern of length `≥ 2` in the parity word counted, and no run-length distribution appears.** Everything past the classical range is a statement about the running *sum* of parities plus the offset bound `r_k(m)`; the `∗`-density transport (Lemmas 2.13–2.16) transports set membership, not word statistics.

---

## 2. The time parameterization, exactly

### 2.1 What the repository's `F`-block is, in Syracuse steps

From `paper/collatz-reduced-v3.tex` Definition L64–67 and Proposition L70–73, and from `aeh.md` `13.6.1`/`13.6.3`(i):

Let `x` be odd, `x + 1 = 2^m u`, `u = 3^a ω` with `3 ∤ ω`, `(ω, d) = R(x)`, `d = m + a`. The proposition gives `x_j + 1 = 2^{m−j}3^j u` for `j = 0,…,m−1`. Each transition `x_j → x_{j+1}` has `ν₂(3x_j + 1) = 1`; the last, `x_{m−1} → x_exit`, has `ν₂(3x_{m−1} + 1) = 1 + s` with `s = ν₂(3^dω − 1) ≥ 1`. Hence, verified against the paper's own definitions:

```text
one F-block  =  exactly m Syracuse steps:  (m − 1) with valuation 1,
                then one with valuation 1 + s ≥ 2.
             =  exactly m + s raw T-steps (= the letter's total exponent).
```

So **an `F`-block is a renewal interval of the Syracuse orbit, ending exactly at a Syracuse step of valuation `≥ 2`.** `aeh.md` `13.6.3`(i)(b)'s "letter `n` occupies exactly `m_n` raw `T`-steps (`G = T^m`)" is a statement in the wiki's `T` = the *odd-to-odd* map; in Inselmann's `T` (one division per step) a block occupies `m + r` steps. The two readings differ by exactly the factor at issue, and the round-2 conversion table used both (`E[m] = 2` Syracuse steps and `σ = 4` `T`-steps per block) without saying so.

Under `B` (`aeh.md` Lemma `13.6.1`): `m` and `r` independent geometric(1/2), `E[m] = 2`, `E[m + r] = 4`.

### 2.2 The three time scales and the two conversion constants

Computed this session in double precision (`log₂3 = 1.584962500721156`, `β = 2(2 − log₂3) = 0.8300749985576878`, `1/β = 1.204710419826604`):

| horizon | Inselmann's units | value | ÷ by | in blocks/bit |
|---|---|---|---|---|
| classical range, `α = (log 2)^{-1}` | `T`-steps per bit | `1.0` | `E[m+r] = 4` | `0.25 = θ` |
| Thm 1.1 / 2.18, `(1 − log₂√3)^{-1}` | `T`-steps per bit | `4.818841679306416` | `E[m+r] = 4` | `1.204710419826604 = 1/β` |
| Thm 1.10 / 3.8, `(log₂(4/3))^{-1}` | `Syr`-steps per bit | `2.4094208396532095` | `E[m] = 2` | `1.204710419826604 = 1/β` |
| Thm 1.9, `3/(2 − log₂3)` | raw `Col`-steps per bit | `7.2282625189596255` | `6` | `1.204710419826604 = 1/β` |

Both ratios `4.818841679306416` and `4.81884167930642` (= `2(log 4/3)^{-1}/(log 2)^{-1}`) agree to 15 digits, and `(1/β)/(1/4) = 4.818841679306416` — the identity is `4/β = 2/(2 − log₂3) = (1 − log₂√3)^{-1}`.

**The conversion constant is one number, used twice.** Every row divides by a `B`-expectation of a letter component.

### 2.3 Why the division by `2` is a pair statistic, not a first moment

A block ends exactly at a Syracuse step of valuation `≥ 2` (§2.1). Therefore

```text
(Syracuse steps) / (blocks)  →  1 / P(valuation ≥ 2).
```

`E[m] = 2` for geometric(1/2) is the same as `P(valuation ≥ 2) = 1/2`. In Inselmann's parity coordinates a Syracuse step with valuation `1` is an odd `T`-step immediately followed by another odd `T`-step, since `(3x+1)/2` is then odd. So

```text
the needed statistic  =  the frequency of the length-2 pattern "11"
                         in the parity sequence (p(m)_i).
```

Theorem 1.6 controls the frequency of the length-**1** pattern `1`. It says nothing whatever about `11`. A parity word with `Σ p_i = k/2` exactly can have the `11` density anywhere from `0` to nearly `1/2`; the constraint is not implied.

### 2.4 What the two-sided envelope *does* pin, unconditionally

Working on Inselmann's density-one set, with `L = log₂ m`, `K` = Syracuse steps, `S = Σ_{j<K} s_j` = `T`-steps:

* `log₂ Syr^K(m) = L + K log₂3 − S`, and the envelope forces `log₂ Syr^K = L − (2 − log₂3)K ± εL`. Hence **`S = 2K ± εL` unconditionally** — this is `E[s] = 2` in Cesàro form, and it is exactly Theorem 1.6 in Syracuse coordinates.
* Over the first `n` blocks, `S_n = K_n + Σ_{i<n} r_i`, so the envelope also gives **`K_n = Σ_{i<n} r_i ± εL`** — i.e. `Σ m_i = Σ r_i + O(εL)`, the Cesàro form of `E[m] = E[r]`. Genuine unconditional content, and still not `E[m] = 2`.
* Each individual letter is bounded: a run of `t` consecutive valuation-`1` steps costs `0.585t` bits of growth, which the two-sided envelope caps at `2εL + 0.415t`, so `m_i ≤ 2εL + 1` and (same computation on the descent side) `r_i ≤ m_i + 2.53εL`. So every block consumes `O(εL)` exponent — enough to place `Θ(1/ε)` blocks inside the protected window, and no more.

**Nothing in Inselmann's theorems bounds `Σ_{i<n} m_i` above by `2n(1 + o(1))`.** The only unconditional inequality in that direction is `Σ_{i<n} m_i ≥ n`, which is the wrong way round: it says the first `n` blocks occupy *at least* `n` Syracuse steps, hence *at most* `2.4094 log₂ m` blocks can fit in the protected window, not at least `1.2047 log₂ m`.

### 2.5 The circle, closed

The `11`-frequency **is** available unconditionally — from Proposition 2.4 (Terras), which gives *every* finite pattern its exact density `2^{-k}`, but only for parity indices `k ≤ log₂ m`, i.e. only over the classical `T`-range. In the repository's coordinates that range is exactly the event `S_n ≤ log₂ m`, which is exactly the base case's `S + 1 ≤ L`, which is exactly `θ < 1/4`.

So: **the letter statistic needed to convert Inselmann's `1/β`-equivalent horizon into block units is unconditionally available precisely on the range `θ < 1/4`, and precisely nowhere else.** Using it past `1/4` is using AEH.

### 2.6 The exact asymmetry between the two ends

| | `α = (log 2)^{-1} ↔ θ = 1/4` | `α = 2(log 4/3)^{-1} ↔ θ = 1/β` |
|---|---|---|
| conversion needed | `E[m + r] = 4` | `E[m + r] = 4` (same constant) |
| is it available there? | **yes** — the word is *exactly* `B` on `{S+1 ≤ L}` (Terras/`14.15.1.5`), which is where the base case runs | **no** — the word's law past the budget is what `13.2.1` hypothesises |
| status of the identification | a theorem of this repository | an application of the hypothesis |

And one level up, the same manoeuvre is legitimate because Inselmann *proved* his input: his `T → Syr` time change divides by `E[s] = 2` and Theorem 1.6 is exactly that. The repository's `Syr → block` time change divides by `E[m] = 2` and there is no corresponding theorem. The structural parallel is exact and it is the cleanest way to state the finding.

### 2.7 Part 1 item 5 — does the envelope's lower side deliver a non-binding cut?

**In Syracuse time, yes, and uniformly in the time.** Theorem 1.10 is quantified `∀0 ≤ k ≤ (log₂(4/3))^{-1} log₂ m` inside the set, so the lower bound holds simultaneously at every `k` in range. At `k = λ(log₂(4/3))^{-1} log₂ m` it gives `log₂ Syr^k(m) ≥ (1 − ε − λ) log₂ m`, which exceeds `log₂ X_N = o(log₂ N)` for every `λ < 1 − ε`. So for every `λ < 1`, all but a vanishing density of odd starts keep the orbit above `X_N` for the first `λ(log₂(4/3))^{-1} log₂ N` Syracuse steps. Three riders:

1. **At the endpoint the statement is not merely unavailable but false in the intended direction**: Corollary 1.4 puts the orbit *below* `m^ε` at the full horizon, and `X_N = N^{o(1)}` is of the same order, so at `θ = 1/β` exactly the cut is expected to bind. The strict inequality `θ < 1/β` in `aeh.md` L32 is the right shape; the problem is the units, not the strictness.
2. **The density notion transfers to the dyadic block.** `13.2.1` samples uniformly from odd `x ∈ [N, 2N)`, while Inselmann's density is cumulative on `[1, 2n+1]`. This is fine: `#(Aᶜ ∩ [N,2N)) ≤ #(Aᶜ ∩ [1,2N)) = o(N)` and `[N,2N)` holds `N/2` odds, so the relative density of the bad set in the block is `o(1)`. Checked, unconditional, no issue.
3. **The visit datum is right.** `13.6.3`(i)(a) records that the visit datum `x_exit` *is* the door `y_n`, and by §2.1 the doors are genuine Syracuse iterates, so the envelope applies to them directly. (The *code* cuts on `ω_+` rather than `x_exit` — `aeh.md` `13.4` records this — and `log₂ ω_+ = log₂(x_exit + 1) − m_+ − a_+ log₂3`, which the envelope does not control. `13.4` states neither cut binds in the runs, so nothing measured depends on it; but the stronger cut is not covered by Inselmann.)

**The failure is entirely in the time parameterization, and only there.** The lower envelope does exactly the job asked of it — in Syracuse (or `T`) time.

---

## 3. What is actually supportable

**S1 (unconditional, and in-house — Inselmann not required).** For every `θ < 1/4` and every cut with `log X_N = o(log N)`, the cut binds on an exponentially small density of starts. *Proof.* Each `T`-step lowers `log₂` by at most `1`, so `log₂ x_exit(i) ≥ log₂ N − S_i ≥ log₂ N − S_n` for every `i ≤ n`. By `14.15.1.5` the length-`n` word is exactly `B`-distributed on `{S_n + 1 ≤ L}`, so `TV(Law(W_n), B^{⊗n}) ≤ P_B(S_n ≥ L)`; with `E_B[m+r] = 4` and geometric tails, both `P_B(S_n ≥ (1−2ε)L)` and `P_B(S_n ≥ L)` are `e^{−Θ(L)}` at `n = (1/4 − ε)L`. On the complement every one of the first `n` exits exceeds `N^{2ε} ≫ X_N`. ∎

**S2 (unconditional, Inselmann).** For every `ε > 0`, all but a vanishing density of odd `x ∈ [N, 2N)` have `x_exit(i) > X_N` for **every block index `i` whose accumulated total exponent satisfies `S_i ≤ (1 − ε)(1 − log₂√3)^{-1} log₂ N`** — equivalently, for every Syracuse time `k ≤ (1 − ε)(log₂(4/3))^{-1} log₂ N`. This is a genuine `4.8188×` extension of S1's window **in total-exponent time**, and it is uniform in the time. Its block count is orbit-dependent.

**S3 (the honest form of the identification).** Inselmann's two horizons are `1` and `(1 − log₂√3)^{-1} = 4.8188…` `T`-steps per bit. The **ratio** `4.8188…` is the same number in any time units and is unconditional; it equals `(1/β)/(1/4) = 4/β` by the algebraic identity `4/β = 2/(2 − log₂3) = (1 − log₂√3)^{-1}`. The **endpoints** convert to `1/4` and `1/β` blocks per bit under one and the same time change, of rate `E[m + r] = 4`; that rate is a theorem where the classical count runs (`θ < 1/4`) and is part of `13.2.1` where it does not.

**S4 (what `β` itself is).** `β = 2(2 − log₂3)` is the per-*block* drift, and the leading `2` is `E[m] = 2` Syracuse steps per block (`aeh.md` `13.4`: `−0.4150` per odd step, `−0.8301` per block). So "`1/β` blocks per bit" already contains the disputed conversion in its definition. The sentence "the classical frontier and its unconditional crossing are the same two numbers seen from the other side" therefore presents as a substantive coincidence something that is an algebraic tautology *plus* the unproved time change.

**Not supportable:** any statement of the form "Inselmann's horizon is `1/β` reduced blocks per bit", or "the cut binds on a vanishing density of starts for all `θ < 1/β`", offered as unconditional or as external corroboration.

---

## 4. What the round-2 argument actually was, and where it went wrong

`briefs/v3r2-contraction-literature-findings.md` §1.5.1 built the conversion table and closed with: "*The conversions use `σ = 4` parity steps per block and `E[m] = 2` Syracuse steps per block — the same `E[m+r] = 4` accounting as §4. Nothing is approximate here: `1 − β/4 = log₄3` and `(1/β)/(1/4) = 2(log⁴⁄₃)^{-1}/(log 2)^{-1} = 4.8188…` are identities.*"

Both halves of that sentence are true and they do not combine. The two displayed identities are identities; the *conversions* are not, and the sentence's "nothing is approximate here" attaches the certainty of the second clause to the first. The same document had already written the refutation, two sections later, at §3 Q2: "*Inselmann controls a running sum; knowing the mean of the parity bits does not give the distribution of run lengths, and `P(s even) = 1/3` is a run-length statistic.*" `P(s ≥ 2) = 1/2` is a run-length statistic by the identical argument. The document contained both halves and did not join them; §5 item 2 then flagged the distributional gap as open without noticing that the conversion table had already assumed it closed.

Nothing else in the round-2 document is affected. Its readings of Terras, Korec, Tao and of Inselmann's *statements* are confirmed against the source wherever I could check them (§6.3).

---

## 5. Drop-in replacements

Every replacement below preserves the surrounding sentence boundaries; the current text is quoted first so the apply step is mechanical. Numbers in the replacements are the ones computed in §2.2.

### 5.1 `aeh.md` L32 — replace this sentence

> For `θ < 1/β`, `β = 2(2 − log₂3) = 0.8301…`, the cut binds on a vanishing density of starts, the tally denominator is the deterministic `⌈θ log₂ N⌉`, and `13.5`'s standing rule is satisfied as written.

with

```markdown
For `θ < 1/4` the cut binds on a vanishing density of starts, unconditionally and for an elementary reason: a `T`-step lowers `log₂` by at most `1`, so `log₂ x_exit(i) ≥ log₂ N − S_n` for every `i ≤ n`, and the base case below gives `S_n ≤ (1 − 2ε)log₂ N` for all but `e^{−Θ(log N)}` of starts at `n = ⌈θ log₂ N⌉` — every one of those exits clears `N^{2ε} ≫ X_N`. There the tally denominator is the deterministic `⌈θ log₂ N⌉` and `13.5`'s standing rule is satisfied as written. Past the digit budget the protected window is still `S_n ≤ (1 − ε)(1 − log₂√3)^{-1} log₂ N` unconditionally (Inselmann; `13.3.2`), but that is a bound on *consumed exponent*, not on block count: reading it as `1/β = 1.2047…` blocks per bit, `β = 2(2 − log₂3) = 0.8301…`, asserts that blocks average `E[m + r] = 4` of exponent, which past the budget is part of this hypothesis rather than an input to it. So for `θ ≥ 1/4` the cut's non-binding is carried by the hypothesis and by the calibration record (`13.4`: in every run neither cut binds), not by an external theorem.
```

### 5.2 `aeh.md` L34 — replace this clause

> for the *trajectory envelope* and for the ledger's *first moment* it has been crossed unconditionally at natural density `1`, out to exactly `1/β` (Inselmann; `13.3.2`), by a different technique.

with

```markdown
for the *trajectory envelope* and for the ledger's *first moment* it has been crossed unconditionally at natural density `1` (Inselmann; `13.3.2`), by a different technique — but in step time: out to `(1 − log₂√3)^{-1} = 4.8188…` `T`-steps per bit, which is `4.8188 ×` the classical `log₂ m`. That window is `1/β` blocks per bit exactly on words whose blocks average `E[m + r] = 4` of exponent, so its block-per-bit reading is a consequence of the letter statistics asserted here, not independent corroboration of them.
```

### 5.3 `aeh.md` L42 (§13.3.2) — replace this sentence

> His `α = (log 2)^{-1}` is `13.2.1`'s `θ = 1/4` and his `α = 2(log(4/3))^{-1}` is `θ = 1/β`; the classical frontier and its unconditional crossing are the same two numbers seen from the other side.

with

```markdown
His horizons are in step time and the passage to this page's block time is not free. His classical range `α = (log 2)^{-1}` is `1` `T`-step per bit — the event `S_n ≤ log₂ m` on which `13.2`'s base case is a theorem — so that end does correspond to `θ = 1/4`, for the same reason the base case works: `E[m + r] = 4` holds exactly where the word is exactly `B`. His extension `α = 2(log(4/3))^{-1}` is `4.8188…` `T`-steps per bit, equivalently `(log₂(4/3))^{-1} = 2.4094…` `Syr`-steps per bit (Thm `1.10`); calling that `1/β` divides by `E[m] = 2` `Syr`-steps per block, i.e. asserts `P(s ≥ 2) = 1/2` — the frequency with which a `Syr`-step ends a block, which in parity coordinates is the density of the pattern `11` and is a two-letter statistic. Thm `1.6` bounds the density of the one-letter pattern `1` and gives nothing about `11`; the exact source for `11` is Terras's cylinder count, whose range is precisely the `θ < 1/4` frontier. Inselmann makes the analogous time change one level up and *proves* his input: his `Syr` horizon is his `T` horizon halved via Thm `1.6` (his Thm `3.8`, eq. `(3.20)`: `Syr^{Σ_{i<j} p(m)_i}(m) = T^j(m)`). The step this page needs, one level further down, has no such theorem behind it. Unconditionally, then: what Inselmann crosses is the `T`-step frontier, by the factor `(1 − log₂√3)^{-1} = 4.8188…`; the *ratio* is the same number in either time and is `(1/β)/(1/4)` by the identity `4/β = 2/(2 − log₂3)`, but the endpoint `1/β` in block units is this page's own hypothesis, not his theorem.
```

Two further precision fixes in the same paragraph, independent of the verdict:

* "*and his Corollary `1.4` gives descent below `m^ε` there*" — Cor. 1.4 is a `T`-time statement, at `T`-time `⌊log₂ m/(1 − log₂√3)⌋`. Amend to "*and his Corollary `1.4` gives descent below `m^ε` at the corresponding `T`-time `⌊log₂ m/(1 − log₂√3)⌋`*".
* "*extending Korec's `x^{0.7924}` … to every exponent*" — confirmed verbatim from Inselmann p. 4, who writes Korec's threshold as `θ > log₂√3`; `log₂√3 = 0.792481250360578`. No change needed.

### 5.4 `paper/collatz-reduced-v3.tex` L273–277 — replace

```latex
$\theta < 1/\beta$, where $\beta = 2(2-\LL) = 0.8301\ldots$ is the classical
per-block contraction rate, the cut binds on a vanishing density of starts and the
tally denominator is the deterministic $\lceil\theta\log_2 N\rceil$ that
\texttt{aeh.md} \S13.5's standing rule --- fixed horizon, unweighted, per-visit
sampling from uniform starts --- was written to secure.
```

with

```latex
$\theta < 1/4$ the cut binds on a vanishing density of starts, unconditionally: a
$T$-step lowers $\log_2$ by at most $1$, so no exit among the first $n$ blocks sits
below $\log_2 N - S_n$ with $S_n$ the accumulated exponent, and the cylinder count
below puts $S_n \le (1-2\varepsilon)\log_2 N$ for all but $e^{-\Theta(\log N)}$ of
the starts at $n = \lceil\theta\log_2 N\rceil$. The tally denominator is then the
deterministic $\lceil\theta\log_2 N\rceil$ that \texttt{aeh.md} \S13.5's standing
rule --- fixed horizon, unweighted, per-visit sampling from uniform starts --- was
written to secure. Past that budget the protected window is still
$S_n \le (1-\varepsilon)(1-\log_2\sqrt3)^{-1}\log_2 N$ unconditionally
(Inselmann \cite[Thm.~1.10]{inselmann}), but it bounds consumed exponent rather
than block count; reading it as $1/\beta = 1.2047\ldots$ blocks per bit, where
$\beta = 2(2-\LL) = 0.8301\ldots$ is the classical per-block contraction rate,
asserts that blocks average $4$ of exponent, which past the budget is part of
Hypothesis~\ref{hyp:aeh} rather than an input to it.
```

### 5.5 `paper/collatz-reduced-v3.tex` L296–299 — replace

```latex
not of the problem --- Inselmann \cite{inselmann} crosses it unconditionally for the
trajectory envelope and the first moment, by an argument that buys the missing
iteration invariance from a density notion stronger than natural density rather than
from a sharper count.
```

with

```latex
not of the problem --- Inselmann \cite{inselmann} crosses it unconditionally for the
trajectory envelope and the first moment, by an argument that buys the missing
iteration invariance from a density notion stronger than natural density
($*$-density: every initial segment carries all but $O(N^{-D})$ of its mass, which
sets of natural density one need not do) rather than from a sharper count. His
horizons are in step time: he starts from the classical range of $\log_2 m$ steps of
$T$ and extends it by the factor $(1-\log_2\sqrt3)^{-1} = 4.8188\ldots$. That factor
is $(1/\beta)/(1/4)$ --- the identity $4/\beta = 2/(2-\LL)$ --- and is the same
number in any time units; the endpoints read as $1/4$ and $1/\beta$ blocks per bit
only after dividing by the mean exponent per block, which is a theorem where the
cylinder count runs and is Hypothesis~\ref{hyp:aeh} where it does not.
```

### 5.6 `paper/collatz-reduced-v3.tex` L307–313 — replace

```latex
within $O(\log x)$ blocks is Inselmann \cite[Cor.~1.4]{inselmann}; his
\cite[Thm.~1.10]{inselmann} is stronger than anything Hypothesis~\ref{hyp:aeh} yields
here, being two-sided, uniform in the time, and unconditional, and it already runs to
the full descent horizon $1/\beta$ blocks per bit rather than the $1/4$ at which the
cylinder count of Section~\ref{sec:aeh} stops. The first entry of the ledger --- that
odd steps occupy half the schedule to the same horizon --- is likewise unconditional
\cite[Thm.~1.6]{inselmann}.
```

with

```latex
within $(1-\log_2\sqrt3)^{-1}\log_2 x$ steps of $T$, hence within $O(\log x)$
blocks, is Inselmann \cite[Cor.~1.4]{inselmann}; his \cite[Thm.~1.10]{inselmann} is
stronger than anything Hypothesis~\ref{hyp:aeh} yields here, being two-sided,
uniform in the time, and unconditional, and it runs to
$(\log_2\tfrac43)^{-1}\log_2 m$ Syracuse steps --- $4.8188\ldots$ times the
classical range at which the cylinder count of Section~\ref{sec:aeh} stops, the two
measured in the same units. The first entry of the ledger --- that odd steps occupy
half the schedule to the same horizon --- is likewise unconditional
\cite[Thm.~1.6]{inselmann}, and is exactly what carries his own passage from
$T$-time to Syracuse time. The further passage to block time needs the frequency
with which a Syracuse step ends a block, a two-letter statistic of the parity word
that neither theorem supplies and that $\pi_k$ does; it is therefore a consequence
of Hypothesis~\ref{hyp:aeh} and not available to underwrite it.
```

### 5.7 `publication.md`, "The 2024–26 landscape" item 4 — replace

> His two horizons are exactly aeh.md `13.2.1`'s own: `α = (log 2)^{-1}` is `θ = 1/4` block per bit (the digit budget) and `α = 2(log(4/3))^{-1}` is `θ = 1/β` (a full descent), ratio `4.8188` both ways.

with

```markdown
His horizons are in step time and do not convert to aeh.md `13.2.1`'s block time for free. `α = (log 2)^{-1}` is `1` `T`-step per bit — the event `S_n ≤ log₂ m` on which `13.2`'s base case is a theorem — so that end does correspond to `θ = 1/4` block per bit (the digit budget). `α = 2(log(4/3))^{-1}` is `4.8188…` `T`-steps per bit, equivalently `2.4094…` `Syr`-steps per bit (Thm 1.10); calling it `θ = 1/β` divides by `E[m + r] = 4`, i.e. asserts that half of `Syr`-steps end a block — the density of the parity pattern `11`, a two-letter statistic that Thm 1.6 does not give and that `13.2.1` itself asserts. What is unconditional is the *ratio* `4.8188 = (1 − log₂√3)^{-1} = 4/β`, the same number in either time; the endpoint identification `1/β` is not. Note also that `β = 2(2 − log₂3)`'s leading `2` is itself `E[m] = 2` `Syr`-steps per block, so "`1/β` blocks per bit" contains the conversion in its definition. Source read page by page, 2026-08-02: `briefs/v3r3-inselmann-horizon-findings.md`.
```

### 5.8 `publication.md`, "Verdicts, claim by claim", AEH descent bullet — two small amendments

The bullet as written ("*Thm 1.10 and Cor. 1.4: a two-sided envelope `(3/4)^k m^{1±ε}` simultaneously for all `k` out to `(log₂(4/3))^{-1} log₂ m`, and descent below `m^ε` there, both at natural density 1*") is **correct against the source** and needs no verdict change — the descent/contraction consequence *is* unconditional, and `13.3.2` correctly claims none. Two precision edits only:

* after "simultaneously for all `k`", insert "(`k` in **Syracuse** steps)";
* replace "and descent below `m^ε` there" with "and descent below `m^ε` at the corresponding `T`-time `⌊log₂ m/(1 − log₂√3)⌋` (Cor. 1.4 is stated for `T`)".

Add one sentence to the same bullet: "The horizons are unconditional in step time; their reading as `1/β` blocks per bit is not — see the landscape item above."

---

## 6. Part 2 — Tao, Remark 1.13, reported separately

### 6.1 Remark 1.13, verbatim (p. 11) **[P]**

> **Remark 1.13.** *One could view the Syracuse random variables `Syrac(ℤ/3ⁿℤ)` as projections*
> `Syrac(ℤ/3ⁿℤ) ≡ Syrac(ℤ₃) mod 3ⁿ`  (1.25)
> *of a single random variable `Syrac(ℤ₃)` taking values in the 3-adics `ℤ₃ := lim← ℤ/3ⁿℤ` (equipped with the usual metric `d(x,y) := 3^{−ν₃(x−y)}`), which can for instance be defined as*
> `Syrac(ℤ₃) ≡ Σ_{j=0}^∞ 3^j 2^{−a_{[1,j+1]}} = 2^{−a₁} + 3¹2^{−a_{[1,2]}} + 3²2^{−a_{[1,3]}} + …`
> *where `a₁, a₂, …` are iid copies of `Geom(2)`; note that this series converges in `ℤ₃`, and the equivalence of distribution (1.25) follows from (1.22), (1.5) after reversing⁴ the order of the tuple `(a₁,…,aₙ)` (cf. (1.24)). **One can view the distribution of `Syrac(ℤ₃)` as the unique stationary measure for the discrete Markov process⁵ on `ℤ₃` that maps each `x ∈ ℤ₃` to `(3x+1)/2^a` for each `a ∈ ℕ+1` with transition probability `2^{−a}`** (this fact is implicit in the proof of Lemma 1.12). However, we will not explicitly adopt the 3-adic perspective in this paper, preferring to work instead with the finite projections `Syrac(ℤ/3ⁿℤ)` of `Syrac(ℤ₃)`.*

**Footnote 4** (attached to "*after reversing*"), verbatim:

> *As an alternative to reversing the order of the tuple `(a₁,…,aₙ)`, one could instead index time by the negative integers `−1, −2, −3, …` rather than the positive integers `1, 2, 3, …`, viewing `Syrac(ℤ₃)` as the outcome of an "ancient" Syracuse iteration that extends to arbitrarily large negative times (and whose initial condition is irrelevant). This perspective towards the Syracuse variables is arguably more natural, and could be adopted elsewhere in the paper; however, we have chosen (mostly for aesthetic reasons) to index time by positive integers rather than negative ones, which necessitates some reversal of the labeling at some junctures.*

**Footnote 5**, verbatim: "*This Markov process may possibly be related to the 3-adic Markov process for the inverse Collatz map studied in [24]. See also a recent investigation of 3-adic irregularities of the Collatz iteration in [23].*" Checked in Tao's reference list (p. 57): **[23] = A. Thomas**, *A non-uniform distribution property of most orbits, in case the `3x+1` conjecture is true*, Acta Arith. **178** (2017), no. 2, 125–134; **[24] = G. Wirsching**, *The Dynamical System Generated by the `3n+1` Function*, LNM 1681, Springer 1998. The paper's L59 sentence "Tao's paper carries a footnote to two further `3`-adic studies" is correct and the two are exactly the ones already checked.

### 6.2 Does Remark 1.13 support the "ancient iteration" reading?

**Yes, unambiguously, and the word "ancient" is Tao's own.** Footnote 4 states in terms that the stationary Syracuse variable may be defined by indexing time over the negative integers, as an iteration extending to arbitrarily large negative times whose initial condition is irrelevant — which is exactly the "define the stationary law from an infinite past" construction. Tao goes further than merely permitting it: he calls it "arguably more natural" and says his positive-time indexing was chosen "mostly for aesthetic reasons". The reviewer's statement is correct as written.

This bears directly on `13.6.5`, which builds `a = ν₃(y₃ + 1)` from `y₃`, "the `3`-adic past-limit (itinerary.md `14.15.3.3`)" — i.e. from exactly Tao's ancient iteration, in door coordinates.

### 6.3 Is the attribution at `aeh.md` L137 correct as to what each item is cited *for*?

**Yes.** The clause carrying the cite is: "*where `Syrac(Z_3)` is the unique stationary measure of `x ↦ (3x+1)/2^a` with transition probability `2^{-a}` (Tao, …, Lemma 1.12 and Remark 1.13)*". Fine-grained locations in the source:

| item | where it is in Tao |
|---|---|
| `Syrac(ℤ/3ⁿℤ)` defined | eq. (1.22), §1.4, p. 9 |
| the recursion for `Syrac(ℤ/3^{n+1}ℤ)` | **Lemma 1.12**, p. 10 |
| the printed `Syrac(ℤ/9ℤ)` values | paragraph after the proof of Lemma 1.12, p. 10 |
| `Syrac(ℤ₃)` as a single `3`-adic variable; the explicit series | **Remark 1.13**, eq. (1.25) and display, p. 11 |
| the **stationary-measure characterization** | **Remark 1.13**, p. 11 — with Tao's own pointer "*this fact is implicit in the proof of Lemma 1.12*" |
| the negative-time / "ancient" reading | **Remark 1.13, footnote 4**, p. 11 |

So the joint cite "Lemma 1.12 and Remark 1.13" is correct: the characterization is Remark 1.13's sentence, the values are Lemma 1.12's worked consequence, and Tao himself links the two in the same direction. Nothing at L137 is mis-attributed.

**Would a two-sided formulation owe further attribution? Yes — one narrow item.** `13.6.5` currently cites Remark 1.13 only for the stationary-measure phrase, while the object it actually constructs is the past-limit `y₃`. If the two-sided/probability-space delegate writes that construction up as "the law defined from an infinite past", the precise prior statement is **Remark 1.13's footnote 4**, and it should be cited *for that*, not folded into the stationary-measure cite. No further attribution beyond that footnote appears to be owed: Tao does not construct the two-sided space, does not develop the `3`-adic perspective (he says so explicitly), and the door-coordinate renewal dictionary at L137 is the repository's.

### 6.4 The printed `Syrac(ℤ/9ℤ)` values — confirmed **[P]**

Tao, p. 10, immediately after the proof of Lemma 1.12, verbatim:

> *Thus for instance, we trivially have `Syrac(ℤ/3⁰ℤ)` takes the value `0 mod 1` with probability `1`; then by the above lemma, `Syrac(ℤ/3ℤ)` takes the values `0, 1, 2 mod 3` with probabilities `0, 1/3, 2/3` respectively; another application of the above lemma then reveals that `Syrac(ℤ/3²ℤ)` takes the values `0, 1, …, 8 mod 9` with probabilities*
> `0, 8/63, 16/63, 0, 11/63, 4/63, 0, 2/63, 22/63`
> *respectively; and so forth.*

* **The nine values are exactly as `aeh.md` L137 prints them, in that order. Confirmed.**
* Indexing is `0,1,…,8`, so **`2/63` sits at residue `7`**, and `7 ≡ −2 (mod 9)`. **Confirmed.**
* The repository's use is consistent: with `y₃ = Syrac(ℤ₃)/2`, `a = ν₃(y₃ + 1) = ν₃(Syrac + 2)` since `2` is a `3`-adic unit; so `{a ≥ 2} = {Syrac ≡ −2 ≡ 7 (mod 9)}`, mass `2/63` — matching L137's `P(a ≥ 2) = 2/63`. Likewise `{a ≥ 1} = {Syrac ≡ 1 (mod 3)}`, mass `1/3` from the mod-3 line, giving `P(a = 0) = 2/3` and `P(a = 1) = 1/3 − 2/63 = 19/63`. All three of L137's quoted values check out against the printed table. **I did not re-verify the `3^5` rational computation of `briefs/v3r2-syrac-identity-findings.md`; only the mod-9 read-off.**

### 6.5 Two further checks at the same site, both clean **[P]**

* **Remark 1.10** (p. 7), verbatim: "*Another standard way in the literature to justify Heuristic 1.8 is to consider the Syracuse dynamics on the 2-adic integers `ℤ₂ := lim← ℤ/2^mℤ`, or more precisely on the odd 2-adics `2ℤ₂ + 1`. … As is well known (see e.g., [14]), the Haar probability measure on `2ℤ₂ + 1` is preserved by this map, and if `Haar(2ℤ₂ + 1)` is a random element of `2ℤ₂ + 1` drawn using this measure, then it is not difficult (basically using the 2-adic analogue of Lemma 2.1 below) to show that the random variables `ν₂(3Syr^j(Haar(2ℤ₂ + 1)) + 1)` for `j ∈ ℕ` are iid copies of `Geom(2)`. However, we will not use this 2-adic formalism in this paper.*" Reference **[14] = J. Lagarias**, *The 3x+1 problem and its generalizations*, Amer. Math. Monthly **92** (1985), no. 1, 3–23 (p. 56). So `aeh.md` L137's "*Tao's Remark 1.10 is likewise the crispest citable form of what `13.6.1`–`13.6.2` re-encode (Haar-invariance and the iid `Geom(2)` valuations, which he calls well known and attributes to Lagarias)*" is **exactly right, reference number included**.
* **A correction for `publication.md` L45.** It says "*Tao's motive for logarithmic density is an iteration property aeh.md `13.3.3` explicitly does not use*". Tao gives **two** stated motives, and the second is not an iteration property: p. 7, after (1.17), "*We remark that the multiplicative inaccuracy of `exp(O(n^{1/2}))` in (1.17) is the main reason why we work with logarithmic density instead of natural density in this paper*" — he calls *that* the main reason. The p. 2 "better approximate multiplicative invariance properties" sentence is the other. The verdict (natural density) is unaffected — Inselmann proves the natural-density version — but "the motive" should become "one of two stated motives, the other being the `exp(O(n^{1/2}))` multiplicative inaccuracy in his heuristic (1.17)".

---

## 7. What I could not obtain or verify

1. **Whether Inselmann's `∗`-density machinery could be pushed to pattern frequencies.** I read the paper cover to cover through §3 and can state as fact that **it does not do so** and that every statistical input is the parity *sum* (§1.8). Whether the transport lemmas 2.13–2.16 would carry two-letter statistics past the classical range is a research question I did not attempt and Inselmann does not address. If they would, the conversion could be *made* unconditional by proving a lemma — but that is a new theorem, not a citation, and until it exists the verdict above stands. This is the same item round 2 left open at its §5 point 2; it is still open, now with the negative half established from the source rather than assumed.
2. **Inselmann's publication status.** arXiv still lists v3 (13 Aug 2024) with no journal reference; I did not re-check for a 2025–26 journal version beyond the arXiv abstract page.
3. **I did not read Inselmann §4** (pp. 31+, if any) or anything after his Theorem 3.8's proof begins on p. 30. Theorem 3.8's proof runs past p. 30 and I read only through the point where (3.20)–(3.25) establish the time change; I did not read its final page. Nothing in the verdict depends on the remainder.
4. **The `ω_+` versus `x_exit` gap** (§2.7 rider 3) is recorded, not resolved. Inselmann's envelope controls `x_exit`; the code's stronger cut on `ω_+` is not covered by it. `13.4` reports neither binds in the runs, so no number depends on it.
5. **`briefs/v3r2-syrac-identity-findings.md`'s exact `3^5` computation** was not re-run. Only the mod-9 read-off from Tao's printed table was checked (§6.4), and it is correct.
6. **Terras and Everett were not read this round.** Inselmann's Proposition 2.4 quotes their result and attributes it to Terras [12, Thm. 1.2] and Everett [4, Thm. 1]; §2.5's use of "the cylinder count gives every finite pattern its exact density on the classical range" rests on Inselmann's Proposition 2.4 as printed and on `itinerary.md` `14.15.1.5`, both read, not on Terras directly.
