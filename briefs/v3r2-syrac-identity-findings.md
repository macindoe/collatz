# Findings: `aeh.md` 13.6.5's absorption law **is** Tao's `Syrac(Z_3)`, in a unit rescaling (v3 round 2)

**Task:** `briefs/v3r2-syrac-identity-brief.md`. Read-only round; the only file written is this one.
**Read at:** `main` = `e4dac49`, working tree clean apart from the round-2 briefs.
**Grades.** **[P]** = read by me from the primary source itself. **[C]** = computed by me this session in exact rational arithmetic (`fractions.Fraction`; no floating point anywhere in any comparison below). **[?]** = not established.

---

## 0. Verdict

**(a) Same law, different coordinates.** The dictionary is multiplication by the `3`-adic unit `2^{-1}`:

```text
y_3  =  Syrac(Z_3) / 2        (equality of distributions on Z_3)

equivalently   nu_j(x) = P( Syrac(Z/3^j Z) = 2x ),   for every j.
```

This is **proved**, not merely fitted: it follows in three lines from Tao's own definitions plus `reverse.md` `14.14.4.1`/`14.14.8.2`, and it is confirmed numerically, exactly, at every precision `3^1 … 3^5`, against **the repository's own `nu_exact`** as well as against my independent reimplementation.

Consequently `13.6.5`'s absorption variable is a functional of Tao's variable,

```text
a  =  v_3(y_3 + 1)  =  v_3(Syrac(Z_3) + 2),
```

and **all three of its printed values are direct read-offs of the nine numbers Tao prints**:

```text
P(a = 0)  = 1 - [Syrac(1) + Syrac(4) + Syrac(7)] = 1 - (8+11+2)/63 = 1 - 21/63 = 2/3
P(a = 1)  =     21/63 - 2/63                                                  = 19/63
P(a >= 2) =     Syrac(7)                                                      = 2/63      <-- Tao's own 2/63
```

So the `2/63` that the brief flagged as a suspicious coincidence is not a coincidence at all: it is *literally the same number in the same place*, Tao's mass at residue `7 mod 9`, which is `−2 mod 9`.

**This is a citation-integrity finding, not a correctness one.** Everything the project computed is right — the repo's `nu_exact` reproduces Tao's law under the dictionary to the last digit at `3^5`. What is wrong is only the framing: `aeh.md` `13.6.5` and the paper's Section 5 present this stationary law as computed in the project record, and it has a 2019 primary source.

**The brief's stated crux dissolves, and its partial hand-check is overturned on one point.** See §4 and §6.

---

## 1. Primary source: obtained, and it is the author's own LaTeX

I did **not** work from a rendering, a summary, or memory. I downloaded the arXiv e-print source package:

```text
https://arxiv.org/e-print/1909.03562
  -> tao.tar.gz          sha256 ba81acd6254838251f1ee585256a6f9f223cdc9c73bed0a3c4fd25782d0124ad
  -> collatz.tex         sha256 bfbc39432d4084a276416cb019a592003c868fa32f18e2f90028ac325ae5c19d
                         164,932 bytes, archive mtime 2026-07-16
```

`00README.json` declares `collatz.tex` as the single toplevel source. The arXiv abstract page confirms **v7** is current and the journal reference is *Forum Math. Pi* **10** (2022), Paper No. e12, 56 pp. The mtime matches the v7 submission date (16 Jul 2026) recorded in `briefs/v3r2-contraction-literature-findings.md` §1.4. Everything quoted below is verbatim from that file. **[P]**

**Numbering, derived and cross-checked.** All numbered environments share one counter (`\newtheorem{theorem}{Theorem}[section]`, everything else `[theorem]`). Counting them in order through Section 1 gives: 1.1 Conjecture (Collatz), 1.2 Definition (Almost all), 1.3 Theorem (main), 1.4 Remark, 1.5 Conjecture (Syracuse), 1.6 Theorem (main-syr), 1.7 Definition (Geom), 1.8 Heuristic (Val), 1.9 Proposition (`rach`), 1.10 Remark (`cat`), 1.11 Proposition (`transport`), 1.12 Lemma (`recursive`), **1.13 Remark (the `Syrac(Z_3)` remark)**, 1.14 Proposition (`tv-bound`), 1.15 Remark, 1.16 Remark, 1.17 Proposition (`f-decay`), 1.18 Remark. This is confirmed by four independent cross-checks against C1's reading: Theorem 1.3, Remark 1.4, Proposition 1.14 and Remark 1.16 all land where C1 reported them. **[P]**

**One correction to the brief's bookkeeping.** The nine values are **not inside Remark 1.13**. They are printed in the running text immediately *after Lemma 1.12* and immediately *before* Remark 1.13. Remark 1.13 is the `Z_3` / stationary-measure remark. A citation should therefore read `\cite[Lemma 1.12 and Remark 1.13]{tao}`, or cite the displayed line by its position after Lemma 1.12.

---

## 2. Tao's definitions, verbatim **[P]**

**Definition 1.7 (Geometric random variable).** "*`Geom(μ)` takes values in `N+1` with `P(Geom(μ) = a) = (1/μ)((μ−1)/μ)^{a−1}` … Thus for instance `P(a = a) = 2^{-a}` whenever `a ≡ Geom(2)` and `a ∈ N+1`.*" So `Geom(2)` is supported on `{1,2,3,…}` with `P(a) = 2^{-a}`.

**The `n`-Syracuse offset map**, eq. `(fn-def)` (line 219–222):

```text
F_n(a_1,…,a_n) = 3^{n-1} 2^{-a_{[1,n]}} + 3^{n-2} 2^{-a_{[2,n]}} + … + 3^1 2^{-a_{[n-1,n]}} + 2^{-a_n}
```

**Definition of the Syracuse random variables**, eq. `(syrac-def)`: "*If we now define the Syracuse random variables `Syrac(Z/3^n Z)` for `n ∈ N` to be random variables on the cyclic group `Z/3^n Z` with the distribution* `Syrac(Z/3^n Z) ≡ F_n(Geom(2)^n) mod 3^n`."

**Lemma 1.12 (Recursive formula for Syracuse random variables).** Verbatim:

> For any `n ∈ N` and `x ∈ Z/3^{n+1}Z`, one has
> `P(Syrac(Z/3^{n+1}Z) = x) = [ Σ_{1 ≤ a ≤ 2×3^n : 2^a x = 1 mod 3} 2^{-a} P(Syrac(Z/3^n Z) = (2^a x − 1)/3) ] / (1 − 2^{-2×3^n})`,
> where `(2^a x − 1)/3` is viewed as an element of `Z/3^n Z`.

Its proof establishes the clean form used below: `Syrac(Z/3^{n+1}Z) ≡ (3·Syrac(Z/3^n Z) + 1)/2^{Geom(2)}`, the two right-hand variables independent.

**The printed values** (line 380–382), verbatim: "*`Syrac(Z/3Z)` takes the values `0,1,2 mod 3` with probabilities `0, 1/3, 2/3` respectively; another application of the above lemma then reveals that `Syrac(Z/3^2Z)` takes the values `0,1,…,8 mod 9` with probabilities*"

```text
0,  8/63,  16/63,  0,  11/63,  4/63,  0,  2/63,  22/63
```

**Remark 1.13**, verbatim (the parts that matter):

> One could view the Syracuse random variables `Syrac(Z/3^n Z)` as projections `Syrac(Z/3^n Z) ≡ Syrac(Z_3) mod 3^n` of a single random variable `Syrac(Z_3)` taking values in the `3`-adics `Z_3 := lim← Z/3^n Z` …, which can for instance be defined as
>
> `Syrac(Z_3) ≡ Σ_{j=0}^∞ 3^j 2^{-a_{[1,j+1]}} = 2^{-a_1} + 3^1 2^{-a_{[1,2]}} + 3^2 2^{-a_{[1,3]}} + …`
>
> where `a_1, a_2, …` are iid copies of `Geom(2)`; note that this series converges in `Z_3` …
>
> One can view the distribution of `Syrac(Z_3)` as the unique stationary measure for the discrete Markov process on `Z_3` that maps each `x ∈ Z_3` to `(3x+1)/2^a` for each `a ∈ N+1` with transition probability `2^{-a}` (this fact is implicit in the proof of Lemma 1.12).

**And — decisively for the brief's crux — Remark 1.13's own footnote**, verbatim:

> As an alternative to reversing the order of the tuple `(a_1,…,a_n)`, one could instead index time by the negative integers `−1,−2,−3,…` rather than the positive integers `1,2,3,…`, viewing `Syrac(Z_3)` as the outcome of an "ancient" Syracuse iteration that extends to arbitrarily large negative times (and whose initial condition is irrelevant). This perspective towards the Syracuse variables is arguably more natural, and could be adopted elsewhere in the paper; however, we have chosen (mostly for aesthetic reasons) to index time by positive integers rather than negative ones, which necessitates some reversal of the labeling at some junctures.

---

## 3. Our object, exactly

From `aeh.md` L118 (`13.6.5`): "*the absorption `a` has the law of `v_3(y_3 + 1)` where `y_3` is the `3`-adic past-limit (itinerary.md `14.15.3.3`), whose distribution `ν_j` at each precision `3^j` is exactly computable … `ν_j` is the exact image of `B^{⊗j}` under the offset formula.*"

From `itinerary.md` `14.15.3.3` **[P, repo]**: for a left-infinite letter word, `B_n` are the composed-affine offsets of `W_{(-n:0)}`, `v_3(B_{n+1} − B_n) = M_n → ∞`, so `B_n → y_3 ∈ Z_3`.

From `reverse.md` `14.14.4.1` / `14.14.8.2` **[P, repo]**: on stratum `(m,r)`, `G` is affine over `Z_3` with

```text
G(x) = alpha·x + beta,     alpha = 3^m 2^{-(m+r)},     beta = (3^m − 2^m) 2^{-(m+r)},
```

equivalently `G(x) = (3^m(x+1) − 2^m)/2^{m+r}`. From `13.6.1`, `P_B(m,r) = 2^{-(m+r)}` with `m, r` iid geometric(1/2) on `{1,2,…}`.

The prepend recursion in `14.15.3.3`'s proof (`B_{n+1} = A_n β + B_n`, `A_{n+1} = A_n α`) telescopes to

```text
y_3 = beta_{-1} + alpha_{-1}·( beta_{-2} + alpha_{-2}·( beta_{-3} + … ) )
```

so `y_3` satisfies the distributional fixed point `Y =_d beta + alpha·Y'` with `Y'` an independent copy — i.e. **`y_3` is the unique stationary law of the random map that applies the stratum-`(m,r)` branch of `G` with probability `2^{-(m+r)}`.** Since `v_3(alpha) = m ≥ 1`, `y_3 mod 3^j` depends only on the last `j` letters, exactly as `13.6.5` states.

---

## 4. The crux — past-limit versus forward object — **dissolves**

The brief flagged this as the thing that might survive any coordinate dictionary. It does not, and Tao says so himself.

* Our `y_3` is a past-limit by construction (`14.15.3.3`): a limit of offsets along a left-infinite word, the initial door forgotten (`14.14.8.3`).
* Tao's `Syrac(Z_3)` is *presented* forward — `F_n(Geom(2)^n)`, the offset of `n` forward Syracuse steps. But `F_n`'s definition already reverses the tuple (his eq. `(fn-recurse)`, and the phrase "*after reversing the order of the tuple*" in Remark 1.13), and **the footnote quoted in §2 says explicitly that `Syrac(Z_3)` is the outcome of an "ancient" iteration extending to arbitrarily large negative times whose initial condition is irrelevant, and that this backward perspective "is arguably more natural"**; positive indexing was chosen "mostly for aesthetic reasons".

Verified directly **[C]**: expanding the ancient limit of Tao's branch `x ↦ (3x+1)/2^a` (`alpha = 3·2^{-a}`, `beta = 2^{-a}`) by the same telescoping gives `Σ_{i≥1} 3^{i-1} 2^{-(a_{(1)}+…+a_{(i)})}`, which on setting `j = i−1` is Tao's displayed series exactly, with `a_1` the **most recent** step. So Tao's `a_1, a_2, …` already runs backward in time.

**Both objects are past-limits of the same genre.** The crux is not a distinguisher; it is the point of agreement.

---

## 5. The dictionary, proved

### 5.1 The door map's branch is a run of Tao's branches — exactly

Write `Syr_a(x) := (3x+1)/2^a` for Tao's branch. Then, as an identity of affine maps over `Q`:

```text
G_(m,r)  =  Syr_(1+r) ∘ Syr_1 ∘ … ∘ Syr_1        (m − 1 copies of Syr_1)
```

**Proof.** Composing `Syr_{a_1}, …, Syr_{a_m}` gives `x ↦ 3^m 2^{-(a_1+…+a_m)} x + Σ_{i=1}^{m} 3^{m-i} 2^{-(a_i+…+a_m)}`. Take `a_1 = … = a_{m-1} = 1`, `a_m = 1 + r`. Then `a_1+…+a_m = m + r`, matching `alpha`. And `a_i + … + a_m = (m−i) + 1 + r`, so with `k = m−i`,

```text
Σ_{k=0}^{m-1} 3^k 2^{-(k+1+r)} = 2^{-(1+r)} · ((3/2)^m − 1)/((3/2) − 1)
                               = 2^{-r} (3^m − 2^m)/2^m
                               = (3^m − 2^m)/2^{m+r}  =  beta.   ∎
```

Checked exhaustively over all 64 strata `m, r ≤ 8` in exact `Fraction` arithmetic over `Q` (not mod anything): **0 mismatches**. **[C]**

### 5.2 The weights match exactly

Tao's iid `Geom(2)` product weight of the word `(1^{m-1}, 1+r)` is `(2^{-1})^{m-1} · 2^{-(1+r)} = 2^{-(m+r)}` — precisely `13.6.1`'s letter law. Checked over the same 64 strata: **0 mismatches**. **[C]**

So the door alphabet `{(m,r) : m,r ≥ 1}` **is** the set of Tao exponent-words of the form "a run of `1`s followed by a single entry `≥ 2`", and the letter law **is** the renewal decomposition of Tao's iid `Geom(2)` exponent sequence at the entries `≥ 2`. Our `G`-chain is Tao's chain observed at those renewal times.

### 5.3 Where the tilt comes from, and why it is exactly `1/2`

Read backward from the present (Tao's own indexing), the concatenated exponent sequence is

```text
(a_1, a_2, a_3, …) = ( 1+r_{-1},  1^{m_{-1}-1},  1+r_{-2},  1^{m_{-2}-1},  … )
```

whose first entry is always `≥ 2`. Its law is exactly iid `Geom(2)` **conditioned on `a_1 ≥ 2`** (a one-line check: the block law `P(l ones, then b) = 2^{-(l+1)}·2^{-(b-1)} = 2^{-(l+b)}` equals the iid law `(1/2)^l·2^{-b}`).

Therefore

```text
y_3  =  (3·S + 1)/2^{a_1},     S ~ Syrac(Z_3),   a_1 ~ Geom(2) | a_1 >= 2,   independent.
```

Now `Geom(2)` on `{1,2,…}` is memoryless: `P(a_1 = 1+k | a_1 ≥ 2) = 2^{-(1+k)}/(1/2) = 2^{-k}`, so `a_1 = 1 + a'` with `a' ~ Geom(2)`. Hence

```text
y_3  =  (1/2) · (3·S + 1)/2^{a'}  =_d  (1/2) · Syrac(Z_3)
```

by stationarity of `Syrac(Z_3)` under Tao's own kernel (Remark 1.13). **∎**

**Reading.** The unit factor `1/2` is not a sign convention and not an arbitrary normalisation. It is the Palm/renewal tilt: our chain looks at the process **only at the moments just after an exponent `≥ 2`**, and conditioning `Geom(2)` on `≥ 2` shifts it by exactly one, which in the `3`-adic coordinate is exactly one division by `2`.

---

## 6. The computations, exact

All in `fractions.Fraction`. Scripts kept in the scratchpad (`syrac_compare.py`, `syrac_confirm.py`); nothing added to `experiments/`.

### 6.1 Tao's side, reproduced from Lemma 1.12 **[C]**

Implementing Lemma 1.12 directly (grouping `a` by residue mod `2·3^n` and summing the geometric series exactly, `Σ_{a ≡ a_0} 2^{-a} = 2^{-a_0}/(1 − 2^{-2·3^n})`):

```text
Syrac(Z/3Z) :  0,  1/3,  2/3                                     -- matches Tao's printed line
Syrac(Z/9Z) :  0,  8/63, 16/63, 0, 11/63, 4/63, 0, 2/63, 22/63   -- matches Tao's printed line exactly
```

Mass sums to `1` at every level. This validates the implementation against the primary source before any comparison is made.

### 6.2 Our side, from the offset formula **[C]**

Iterating the letter kernel `Y ↦ beta + alpha·Y` (exact after `j` steps since `v_3(alpha) = m ≥ 1`):

```text
nu_1 :  0,  2/3,  1/3
nu_2 :  0,  16/63, 11/63, 0, 22/63, 8/63, 0, 4/63, 2/63
```

`nu_1 = (2/3, 1/3)` on `(1,2) mod 3` — exactly as `aeh.md` `13.6.5` states.

### 6.3 The comparison

```text
residue r mod 9  |  0     1      2      3   4      5     6   7     8
-----------------+-----------------------------------------------------
Tao  Syrac       |  0   8/63  16/63    0  11/63  4/63   0  2/63  22/63
ours nu_2        |  0  16/63  11/63    0  22/63  8/63   0  4/63   2/63
```

Not equal. **But** `nu_2(x) = Syrac(2x mod 9)` at every `x`: `nu_2(1) = Syrac(2) = 16/63`; `nu_2(4) = Syrac(8) = 22/63`; `nu_2(8) = Syrac(7) = 2/63`. And `2^{-1} = 5 mod 9`.

**Exhaustive dictionary search.** Over all 54 affine maps `x ↦ u·x + v mod 9` with `u` a unit: **exactly one** carries `Syrac` to `nu_2`, namely `(u,v) = (5,0) = (2^{-1}, 0)`. Over all 486 such maps mod 27: **exactly one**, `(u,v) = (14,0) = (2^{-1}, 0)`. The dictionary is unique and is multiplication by `2^{-1}`. **[C]**

**The named candidates the brief tried, all refuted mod 9** (each computed exactly):

```text
x -> -x     :  0, 22/63,  2/63,  0,  4/63, 11/63,  0, 16/63,  8/63     != nu_2
x -> x+1    : 22/63,   0,  8/63, 16/63,  0, 11/63, 4/63,   0,  2/63    != nu_2  (and puts mass on 0)
x -> -x-1   : 22/63, 2/63,    0,  4/63, 11/63,   0, 16/63, 8/63,   0   != nu_2
nu_2        :  0, 16/63, 11/63,  0, 22/63,  8/63,  0,  4/63,  2/63
```

### 6.4 Confirmation to `3^5`, and against the repository's own code **[C]**

```text
j |  mod 3^j |  2^-1  |  law(Syrac/2) == nu_j (mine) | repo nu_exact == mine | repo nu_exact == Syrac/2
--+----------+--------+------------------------------+-----------------------+-------------------------
1 |        3 |      2 |            True              |         True          |          True
2 |        9 |      5 |            True              |         True          |          True
3 |       27 |     14 |            True              |         True          |          True
4 |       81 |     41 |            True              |         True          |          True
5 |      243 |    122 |            True              |         True          |          True
```

The middle column is the load-bearing one: I imported `nu_exact` from `experiments/aeh_symbolic.py` **unmodified** and compared it to `law(Syrac(Z/3^j Z)/2)` computed from Tao's Lemma 1.12. They agree at every one of the `3 + 9 + 27 + 81 + 243 = 363` residues, as exact rationals. The project's own published computation *is* Tao's law.

(I also independently re-derived `y_3` a third way — as `(3·Syrac + 1)/2^{a_1}` with `a_1 ~ Geom(2)|a_1 ≥ 2` — and it agrees with `nu_2` and `nu_3` exactly, confirming §5.3's derivation route as well as its conclusion.)

The mod-27 tables, for the record:

```text
x  : Syrac(Z/27Z)      nu_3              x  : Syrac(Z/27Z)      nu_3
 0 : 0                 0                14 : 688/37449         1376/37449
 1 : 1376/37449        2752/37449       15 : 0                 0
 2 : 2752/37449        5240/262143      16 : 4316/262143       8632/262143
 3 : 0                 0                17 : 34492/262143      344/37449
 4 : 5240/262143       10480/262143     18 : 0                 0
 5 : 8632/262143       17264/262143     19 : 6392/262143       12784/262143
 6 : 0                 0                20 : 34528/262143      23285/262143
 7 : 344/37449         688/37449        21 : 0                 0
 8 : 10480/262143      4316/262143      22 : 17246/262143      34492/262143
 9 : 0                 0                23 : 3196/262143       6392/262143
10 : 17264/262143      34528/262143     24 : 0                 0
11 : 12784/262143      17246/262143     25 : 1598/262143       3196/262143
12 : 0                 0                26 : 46570/262143      1598/262143
13 : 23285/262143      46570/262143
```

(`nu_3(x) = Syrac(2x mod 27)`; e.g. `nu_3(14) = Syrac(1) = 1376/37449`.)

### 6.5 The absorption and depth laws, read off Tao **[C]**

`a = v_3(y_3 + 1) = v_3(Syrac/2 + 1) = v_3((Syrac + 2)/2) = v_3(Syrac + 2)` (`2` a `3`-adic unit). So:

```text
P(a >= 1) = P(Syrac = -2 = 1 mod 3) = 8/63 + 11/63 + 2/63 = 21/63 = 1/3
P(a >= 2) = P(Syrac = -2 = 7 mod 9) = 2/63                                <-- 13.6.5's 2/63
P(a  = 0) = 1 - 1/3                 = 2/3                                 <-- 13.6.5's 2/3
P(a  = 1) = 21/63 - 2/63            = 19/63                               <-- 13.6.5's 19/63
P(a  = 2) = 6724/262143   (computed at 3^3)
```

Convolving with `m` geometric(1/2), `m ⊥ a`, reproduces `13.6.5`'s depth values exactly: `P(d=1) = 1/3`, `P(d=2) = 20/63`. **Every printed number in `13.6.5`'s exact-values block is a functional of Tao's nine printed numbers.**

**Note on the shared denominator, for honesty.** `63 = 2^6 − 1` is forced by `ord(2 mod 9) = 6` — it is the denominator of the geometric series `1/(1 − 2^{-6})` that any `2^{-a}`-weighted `3`-adic stationary law produces at level `9`. (At level `27` it is `2^{18} − 1 = 262143`, as the table shows.) So the shared denominator that first raised the alarm was, on its own, *weak* evidence — it would have appeared for genuinely different laws of this genre too. The identity is established by §5's proof and §6.4's exact agreement, not by the denominator.

---

## 7. The brief's partial hand-check: what held and what did not

| Brief's finding | Verdict |
|---|---|
| Support matches (both vanish on multiples of `3`) | **Confirmed.** Both are supported on units; preserved by `×2^{-1}`. |
| Mod-3 marginals exactly swapped, `(1/3, 2/3)` vs `(2/3, 1/3)` | **Confirmed as a fact.** |
| "*A sign convention (`x = −y`, or `z = y+1`) would explain this*" | **Overturned.** Negation and shift both fail at mod 9 (§6.3). The true cause is the renewal conditioning `a_1 ≥ 2`, which at mod 3 flips `P(a odd) = 2/3` to `P(a odd) = 1/3` — hence the swap — and globally is `×2^{-1}`. |
| "*No naive identification works … either a subtler coordinate dictionary, or genuinely different objects*" | **First horn.** There is a subtler dictionary, it is unique, and it is `×2^{-1}`. |
| Tao's nine values sum to `1` | Confirmed. |
| Crux: past-limit vs forward object | **Dissolved** — Tao's Remark 1.13 footnote states his object is an ancient (backward) iteration and calls that view "arguably more natural" (§4). |

---

## 8. What in §13.6 is Tao's, and what is not

Checked as the brief asked, against Tao §1.3 and his Syracuse random variables.

* **`13.6.5`'s stationary law `ν` / `y_3` / the absorption marginal — Tao's.** `= Syrac(Z_3)/2`. Attribution owed. **[P + C]**
* **`13.6.1` (letter law).** Its counterpart is **Tao's Remark 1.10**, verbatim: "*As is well known (see e.g., [lag]), the Haar probability measure on `2Z_2+1` is preserved by this map, and if `Haar(2Z_2+1)` is a random element … then it is not difficult … to show that the random variables `ν_2(3 Syr^j(Haar(2Z_2+1)) + 1)` for `j ∈ N` are iid copies of `Geom(2)`.*" Our `13.6.1` is exactly that fact re-encoded by the renewal decomposition of §5.2. **No new debt** — Tao himself calls it well known and cites Lagarias, and `aeh.md` L59/L76 already frames `13.6.1`–`13.6.2` as classical with Terras/Everett/Lagarias/Bernstein–Lagarias pinned. Worth citing Tao's Remark 1.10 as the crispest single statement, but it is optional. **[P]**
* **`13.6.2` (Bernoulli identification).** Tao states Haar-invariance and the iid property (Remark 1.10) but not the measure-isomorphism onto the full shift; he explicitly declines the `2`-adic formalism ("*we will not use this `2`-adic formalism in this paper*"). `aeh.md` L76 already disclaims novelty and attributes the conjugacy classically. **No change needed.** **[P]**
* **`13.6.3`(v) (renewal + product structure of the window-state law).** **No counterpart in Tao.** He has no joint `2`-adic × `3`-adic window law; his Proposition 1.9 (`rach`) is a finite-`n` TV statement about the valuation vector for integer `N`, and his Proposition 1.14 is fine-scale mixing of the offset. The `ω`-residues-Haar-uniform-and-independent-of-depth structure is the project's. **Note however** that the underlying split — the `2`-adic future carries the valuations, the `3`-adic past carries the offset — is precisely Tao's own decomposition of `Syr^n` into valuation vector plus offset map (`s-iter`). Same architecture, independently arrived at; only the joint law is ours. **[P + inference]**
* **`13.6.4`, `13.6.6`, `13.6.7`** — orbit-genericity formulations. No counterpart; Tao makes no orbit-by-orbit genericity claim. **[P]**
* **The paper's Lemma `lem:absorption` (`\label{lem:absorption}`, tex L122).** **Not Tao's, and not the same object.** It is a deterministic per-state valuation identity (`a_+ = v_3(C)` by cases on `s` odd/even and `d` vs `h(s)`), proved by lifting-the-exponent. Different genre entirely from a stationary law. The `1/3` `3`-gain rate that follows from it (`Σ_{j even} 2^{-j}`) is likewise a consequence of that identity plus the `s`-marginal, not of `Syrac`. **No attribution owed here.** **[P]**
* **`13.6.5`'s contrast finding** — that the window chain's stationary law (`P(a=1) = 17/63`, `P(a≥2) = 4/63`) differs from the exact bulk marginal by exactly computed rationals, and that orbit data rejects the chain law at `≈14` pooled standard errors — is about a **project-internal model object** (`13.2`'s parenthetical chain). Tao has no such object. **This finding survives intact and is unaffected.** Only the identity of the *correct* law is Tao's. **[C]**

**Net:** exactly one item needs attribution. It is the one C1 flagged.

---

## 9. What follows for the record — draft text for (a)

### 9.1 Bibliography

The `\bibitem{tao}` already drafted in `briefs/v3r2-contraction-literature-findings.md` §4.1 is correct as written and is needed for this too:

```latex
\bibitem{tao} T.~Tao, \emph{Almost all orbits of the Collatz map attain almost
  bounded values}, Forum Math.\ Pi 10 (2022), Paper No.\ e12, 56 pp.;
  arXiv:1909.03562.
```

Verified this session against the arXiv abstract page (journal ref, article number, page count) and the v7 source. **[P]**

### 9.2 Paper Section 5, replacing the relevant clause of L239

Current text (tex L239) reads, in part: "*…and so receives not Haar measure but the exact renewal law of the depth itself: `\dnext = m_+ + a_+` with `m_+` geometric(1/2) and \emph{independent} of the absorption `a_+`, whose distribution is an explicit convolution computed exactly in the project record (`\texttt{aeh.md}` \S13.6.3(v), with marginal \S13.6.5: `P(a_+ = 0) = 2/3`, `P(a_+ = 1) = 19/63`, `P(a_+ \ge 2) = 2/63`, hence `P(d = 1) = 1/3`, `P(d = 2) = 20/63`).*"

Drop-in replacement (macros `\Z`, `\vth`, `\w`, `\dnext` all exist in the file; `Syrac` is spelled out since there is no macro for it):

```latex
and so receives not Haar measure but the exact renewal law of the depth itself:
$\dnext = m_+ + a_+$ with $m_+$ geometric$(1/2)$ and \emph{independent} of the
absorption $a_+$. The stationary $3$-adic law governing $a_+$ is not new here:
it is Tao's Syracuse random variable $\mathrm{Syrac}(\Z_3)$
\cite[Lemma~1.12 and Remark~1.13]{tao}, in the door normalisation. Precisely,
the past-limit $y_3$ of the door coordinate satisfies
$y_3 = \mathrm{Syrac}(\Z_3)/2$ in distribution --- the two differ by the
$3$-adic unit $2^{-1}$ because one door block is a run of Syracuse steps
terminated by the first exponent $\ge 2$, so that the door chain sees the
Syracuse chain conditioned on that event --- and hence
$a_+ = \vth{\mathrm{Syrac}(\Z_3) + 2}$. The values
$P(a_+ = 0) = \tfrac23$, $P(a_+ = 1) = \tfrac{19}{63}$,
$P(a_+ \ge 2) = \tfrac{2}{63}$, and thence $P(d = 1) = \tfrac13$,
$P(d = 2) = \tfrac{20}{63}$, are read off the nine values of
$\mathrm{Syrac}(\Z/9\Z)$ that Tao computes. What the present coordinates add is
the \emph{joint} law (\texttt{aeh.md} \S13.6.3(v)): the $\w$-residues are
Haar-uniform among odd residues and independent of the depth, with
$\dnext = m_+ + a_+$ and $m_+ \perp a_+$. Let $\pi_k$ denote this product law.
```

Then the existing next sentence ("*The stationary law of the exact window chain is a `~1%`-accurate model…*") follows unchanged, since that contrast is about a different object and is unaffected.

### 9.3 `aeh.md` `13.6.5`, attribution sentence

To be inserted at the head of `13.6.5`'s discussion (after the exact-values block), or as a `**Attribution**` paragraph in the register the page already uses for `13.6.2`'s "Content — framing" note:

```text
**Attribution.** The law computed here is not new. `y_3` is Tao's Syracuse
random variable: `y_3 = Syrac(Z_3)/2` exactly, in distribution, where
`Syrac(Z_3)` is the unique stationary measure of `x ↦ (3x+1)/2^a` with
transition probability `2^{-a}` (Tao, *Almost all orbits of the Collatz map
attain almost bounded values*, Forum Math. Pi 10 (2022) e12, arXiv:1909.03562,
Lemma 1.12 and Remark 1.13). The dictionary is forced and is a unit rescaling:
the stratum-`(m,r)` branch of `G` is exactly `Syr_{1+r} ∘ Syr_1^{m−1}` with
`Syr_a(x) = (3x+1)/2^a`, and the letter weight `2^{-(m+r)}` is exactly the iid
`Geom(2)` weight of the exponent word `(1^{m−1}, 1+r)`; so the letter alphabet
is the renewal decomposition of Tao's exponent sequence at its entries `≥ 2`,
the door chain is Tao's chain observed at those renewal times, and its
stationary law is Tao's conditioned on the most recent exponent being `≥ 2` —
which, `Geom(2)` being memoryless, is exactly division by `2`. Consequently
`a = v_3(y_3+1) = v_3(Syrac(Z_3)+2)`, and the values `2/3`, `19/63`, `2/63`
above are read off Tao's printed `Syrac(Z/9Z) = 0, 8/63, 16/63, 0, 11/63, 4/63,
0, 2/63, 22/63` — his mass `2/63` at residue `7 ≡ −2 (mod 9)` being our
`P(a ≥ 2)`. Verified to precision `3^5` in exact rational arithmetic. What this
proposition contributes is therefore not the law but (i) its identification as
the exact bulk depth marginal in door coordinates, via the synchronization
corollary `14.14.8.3` and the past-limit `14.15.3.3`, and (ii) the finding that
`13.2`'s window chain does *not* have this stationary law, differing from it by
exactly computed rationals (`17/63` vs `19/63`, `4/63` vs `2/63`) — a
discrepancy about a model internal to this record, and unaffected by the
attribution.
```

Also worth a pointer at `13.6.1` (optional, not owed): Tao's Remark 1.10 states the Haar-invariance and the iid `Geom(2)` valuation property directly, and is the crispest citable form of what `13.6.1`/`13.6.2` re-encode.

### 9.4 Related work, and one thing to say out loud

A referee who knows Tao's paper will now find the connection *flattering* rather than damaging, provided the paper says it first: the door coordinate independently rediscovered his Syracuse random variable as the induced chain of his Markov process, and the `(m,r)` alphabet is exactly the renewal decomposition of his `Geom(2)` exponent sequence. Said plainly, that is a point in the coordinate system's favour. Said only by the referee, it is an omission. **Recommendation: say it, in Section 5 and in Related Work.**

---

## 10. Verification table

| Fact | Source, grade |
|---|---|
| arXiv e-print source obtained; `collatz.tex` sha256 `bfbc394…`; v7 current; Forum Math. Pi 10 (2022) e12 | arXiv e-print + abs page, this session — **[P]** |
| Tao Definition 1.7 (`Geom(2)`, `P(a) = 2^{-a}` on `a ≥ 1`) | `collatz.tex` L243–250 — **[P]** |
| Tao eq. `(fn-def)`, `(syrac-def)`, Lemma 1.12 | L219–222, L350–352, L361–364 — **[P]** |
| Printed `Syrac(Z/3Z)` and `Syrac(Z/9Z)` values | L380–382 — **[P]** |
| Remark 1.13 text and its "ancient iteration" footnote | L384–394 — **[P]** |
| Tao Remark 1.10 (Haar-invariance; iid `Geom(2)` valuations; cites Lagarias) | L282 — **[P]** |
| Environment numbering (Remark 1.13 is the `Syrac(Z_3)` remark) | derived from `\newtheorem` at L58–72 + count; cross-checked at Thm 1.3 / Rem 1.4 / Prop 1.14 / Rem 1.16 — **[P]** |
| Nine values sit *after Lemma 1.12*, not inside Remark 1.13 | L380–384 — **[P]** |
| `G` affine constants `alpha, beta` on stratum `(m,r)` | `reverse.md` `14.14.4.1`, `14.14.8.2` — **[P, repo]** |
| `y_3` past-limit definition, prepend recursion | `itinerary.md` `14.15.3.3` — **[P, repo]** |
| letter law `2^{-(m+r)}`, `13.6.5`'s claims | `aeh.md` L63, L118–125 — **[P, repo]** |
| `G_(m,r) = Syr_{1+r} ∘ Syr_1^{m-1}` exactly over `Q` | proved §5.1; checked 64 strata, 0 mismatches — **[C]** |
| letter weight = Tao word weight of `(1^{m-1},1+r)` | checked 64 strata, 0 mismatches — **[C]** |
| Tao's Lemma 1.12 reimplemented; reproduces his printed `Z/3Z` and `Z/9Z` values exactly | — **[C]** |
| `nu_1 = (0, 2/3, 1/3)`; `nu_2 = (0,16/63,11/63,0,22/63,8/63,0,4/63,2/63)` | — **[C]** |
| `y_3 = Syrac(Z_3)/2` — checked at `3^1 … 3^5`, all 363 residues, exact rationals | — **[C]** |
| Repo's own `experiments/aeh_symbolic.py::nu_exact(j)`, imported unmodified, `== law(Syrac/2)` for `j = 1..5` | — **[C]** |
| `y_3 = (3·Syrac+1)/2^{a_1}`, `a_1 ~ Geom(2)\|≥2`, `== nu_2, nu_3` | — **[C]** |
| Unique affine dictionary mod 9 = `(5,0)`; mod 27 = `(14,0)`; both `= (2^{-1},0)` | exhaustive search, 54 and 486 candidates — **[C]** |
| Negation, `+1` shift, `−x−1` all refuted at mod 9 | — **[C]** |
| `P(a=0)=2/3`, `P(a=1)=19/63`, `P(a≥2)=2/63`, `P(d=1)=1/3`, `P(d=2)=20/63` all read off Tao's nine values | — **[C]** |
| Denominator `63 = 2^6 − 1` forced by `ord(2 mod 9) = 6`; `2^{18}−1` at level 27 | — **[C]** |
| `lem:absorption` (paper L122) is a deterministic valuation identity, different object | `paper/collatz-reduced-v3.tex` L122–130 — **[P, repo]** |
| Paper macros `\Z`, `\vt`, `\vth`, `\w`, `\dnext` exist; no `Syrac` macro | ibid. L17–23 — **[P, repo]** |

**Scripts** (scratchpad only, not added to `experiments/`): `syrac_compare.py` (Tao's Lemma 1.12; our letter kernel; the rebuild via the block dictionary; exhaustive affine search), `syrac_confirm.py` (branch factorisation over `Q`; `Syrac/2` to `3^5`; the read-off table). All exact `Fraction`; every distribution asserted to sum to `1`.

---

## 11. What I did not establish

1. **[?] Whether the `1/2` normalisation is worth changing.** One could redefine the door coordinate so that `y_3` *is* `Syrac(Z_3)` on the nose. I did not investigate what that would cost elsewhere in the record (it would move `13.6.5`'s printed values and every downstream number), and I recommend against it — the attribution sentence is cheaper and more honest than a renormalisation that would obscure the renewal structure that makes the door alphabet what it is.
2. **[?] Whether the identity extends to Tao's Proposition 1.14 (fine-scale mixing).** If `nu_j` is `Syrac(Z/3^j Z)` rescaled, then Tao's superpolynomial oscillation bound transfers verbatim to `nu_j` — a rescaling by a unit is an isometry of `Z_3` and commutes with the `Osc_{m,n}` functional. I believe this is immediate but did **not** work through it; if any part of the record makes a mixing or equidistribution claim about `nu_j`, it should be checked against Prop 1.14 before being asserted as new. **I flag this as the natural successor question to this round.**
3. **Not attempted:** whether `13.6.3`(v)'s joint product law has a counterpart anywhere else in the literature (I checked only Tao). C1's residue item 2 (the distributional ledger past the digit budget) is untouched by this round.
4. **Not attempted, and the largest thing I am leaving on the table.** Tao's own Remark 1.13 footnote points at two references for related `3`-adic Markov structure, which I resolved in his bibliography but did **not** read:

   * **G. Wirsching**, *The Dynamical System Generated by the `3n+1` Function*, Lecture Notes in Math. **1681**, Springer, Berlin, 1998 — Tao's words: "*This Markov process may possibly be related to the `3`-adic Markov process for the **inverse** Collatz map studied in [wirsch].*"
   * **A. Thomas**, *A non-uniform distribution property of most orbits, in case the `3x+1` conjecture is true*, Acta Arith. **178** (2017), no. 2, 125–134 — "*a recent investigation of `3`-adic irregularities of the Collatz iteration*".

   Our `y_3` is a **past**-limit built from predecessor chains (`14.15.3.3`, `14.15.3.4`), which is precisely the inverse-map setting Wirsching's monograph treats. A `3`-adic Markov process for the inverse map is therefore a *closer* structural neighbour to our object than Tao's forward presentation is, and it is 1998, not 2019. **This should be checked before the AEH section is finalized** — the round just completed closes the item C1 flagged, but Wirsching is a plausible second, earlier contact for the same law, and possibly for `13.6.3`(v)'s renewal structure too. A monograph is a bigger read than this round had scope for; it wants its own brief.
