# Findings: staircase-allp-construction (gap B) — 2026-07-28

> **Pre-rewrite numbering.** Sub-numbers here are pre-rewrite: "12.8.6.2" in this file is the pure-geometric profile, now `cycles.md` 12.8.6.3; the Construction B it proves is now numbered 12.8.6.2 (applied with deviations — see `briefs/staircase-status-apply-findings.md`).

Brief: `briefs/staircase-allp-construction-brief.md`. Branch
`staircase-allp-construction`. **Base SHA `e0c34a9`** — the worktree was cut
from `2225b68`, which did not contain the brief; the branch was re-cut at
`e0c34a9` before any work began.

Verification code: `experiments/staircase_allp_construction.py` (fresh, imports
nothing from `staircase_allp.py`, `p22_passer.py` or `uniform_trim.py`; every
pass/fail decision is an exact big-integer comparison). Committed output:
`experiments/staircase_allp_construction_output.txt`.

**Headline.** Route (ii) succeeded. There is an explicit integer profile whose
*p* size conditions `q ≤ R_r` hold **by construction**, with no correction step,
under a single stated hypothesis on the candidate `n`. Algorithm `12.8.6.3` can
be **removed** from the argument, not merely bounded. The `γ` achieved is
**`O(1)` — bounded, with no `p`-dependence at all** — which is strictly stronger
than the published `O(log p)` and correspondingly *weakens* what the sibling
session must supply: the Diophantine input consumed is a **constant-quality
density condition**, not a continued-fraction convergent.

**Stopping-rule compliance.** This is a negative structural result about the
reach of size/counting arguments, the same category as `12.8.6`: the session
constructs **size-passers, never cycles**, and touches the divisibility system
only to confirm — as `12.8.3` and `12.8.6.4` do for theirs — that every
constructed configuration **fails** it (checked at all `p ∈ {2,…,32}`, all
rotations, zero divisible). No per-period cycle search was run; no
divisibility-based exclusion was attempted. **The cycle front stays PARKED and
`12.8.5` is unaffected at any grade.** `cycles.md`, `paper/` and
`publication.md` are untouched — §8 below is a recommendation for the main
session, not an edit.

---

## 1. The target inequality, exactly

Notation as in `12.6.1` and `12.8`: profile `(m_t, s_t)_{t ∈ Z/pZ}` with entries
`≥ 1`, `σ_t = s_t + m_{t+1}`, `n = Σ m_t`, `K = Σ s_t + n`, `q = 2^K − 3^n`,
`L = log_2 3`, `γ = K − log_2 q` (so `q = 2^{K−γ}`), and

```text
R_r = Σ_{t=0}^{p−1} 3^{M_t} · 2^{S_t} · (2^{s_t} − 1),
M_t = Σ_{j>t} m_j,   S_t = Σ_{j<t} σ_j     (indices in rotation order from r).
```

`12.8.1`'s exact exponent identity `e_t − K = (L−1)M_t − m_r − Σ_{j>t} s_j` says
that term `t` equals `2^K · 2^{w(A_t) − m_r} · (1 − 2^{−s_t})`, where `A_t` is the
arc of blocks strictly after position `t`, i.e. **the arcs ending at block
`r−1`**, and `w(A) = (L−1)·m(A) − s(A)` is `12.8`'s arc weight. Hence, exactly,

```text
(★)   q ≤ R_r    ⟺    γ ≥ m_r − Ψ_r ,
      Ψ_r := log_2 Σ_{t} 2^{w(A_t)} (1 − 2^{−s_t}) .
```

This is worth recording in its own right: **the size condition is the summed,
sharpened form of the block bound `m_r < γ' + Φ_r` that Theorem `12.8.1` proves**
(`Ψ_r ≥ Φ_r + log_2(1 − 2^{−s})` for the maximising arc). The trim theorem is
`(★)` relaxed to its largest term with `p` absorbed into `log_2 p`; that is why
the staircase can sit so close to the trim without violating it.

### Specialisation to the staircase, and the binding rotations

Blocks `0,…,p−2` are *climb* blocks with `s_j = 1`; block `p−1` is the *crash*
block, `m_{p−1} = c`, `s_{p−1} = S − (p−1)`, `S = K − n`. Write
`T_r = m_0 + … + m_r`, `T_{−1} = 0`, `T_{p−1} = n`.

Two structural facts fix the picture.

*The cycle's total weight is within one unit of zero.*
`Σ_j w_j = (L−1)n − S = nL − ⌈nL⌉ = −x_n ∈ (−1, 0]`, with
`x_n := ⌈nL⌉ − nL` the **quality parameter**. So an arc and its complement have
almost exactly opposite weights: no arc is negligible by accident, and the only
thing that makes an arc bad is crossing the crash block.

*The maximal arc ending at `r−1` is the maximal climb prefix `{0,…,r−1}`.*
Longer arcs must cross the crash block and pay its exit valuation
`S − (p−1) ≈ 0.585n`; shorter ones drop a climb block of positive weight
`w_j = (L−1)m_j − 1 > 0` (true as soon as `m_j ≥ 2`). Its weight is
`(L−1)T_{r−1} − r`.

Keeping only that one term of `R_r` — the term at position `t = p−1−r`, whose
exit factor is the crash block's `(2^{S−p+1} − 1)` — gives, for every
`r = 0,…,p−1`, the **sufficient condition**

```text
(C_r)     m_r + r + η  ≤  γ + (L−1)·T_{r−1} ,      η := −log_2(1 − 2^{−(S−p+1)}) ,
```

which as a pure integer inequality (no floating point anywhere) is

```text
(C_r)^Z   q · 2^{m_r}  ≤  3^{T_{r−1}} · 2^{n − T_{r−1} + p − 1 − r} · (2^{S−p+1} − 1) .
```

`η` is utterly negligible (`S − p + 1 ≈ 0.585n`), and the whole argument below is
one-sided: **it never needs to know which term of `R_r` dominates**, only that
all terms are positive.

**Which rotations bind, and why they cluster at the crash.** In `(C_r)` the left
side grows twice over along the climb: `m_r` is largest at the end (geometric
growth) *and* `r` counts the unit exits already spent since the last reset. The
right side grows only through `(L−1)T_{r−1}`, which at ratio exactly `L` keeps
pace with `m_r` and pays nothing towards `r`. The crash block is the only place
where the arc maximum resets. So **every climb rotation must pay for all the
unit exits accumulated since the crash, and those payments accumulate linearly
along the climb** — the binding rotations are `r = p−2, p−3, …`, immediately
before the crash. That is the "cluster near the crash block" of the record,
with its reason attached.

---

## 2. The shortfall of Construction `12.8.6.2` — it is `Θ(p)`

For the exact-real *pure geometric* climb `m_j = a·L^j` of total `N = n − c`,

```text
(L−1)·T_{r−1} = a·L^r − a = m_r − m_0,
```

so `(C_r)`'s deficit is

```text
D_r := m_r + r + η − γ − (L−1)T_{r−1}  =  m_0 + r + η − γ ,
```

*independent of everything but `m_0`, `r` and `γ`*. Adding `12.8.6.2`'s
partial-sum rounding (prefix error `≤ 1/2`, hence `≤ 1` on `m_r` and
`≤ (L−1)/2` on `(L−1)T_{r−1}`):

```text
D_max  ≤  n(L−1)/(L^{p−1} − 1)  +  (p − 2)  −  γ  +  1 + (L−1)/2 + η
       ≈  0.927·κ + p − 2 − γ + 1.29        (κ := n / L^p)
```

**This is linear in `p` at fixed `γ`.** Verified in Part 2 of the script at
every period in the table: the measured single-term deficit never exceeds the
derived bound and tracks its `p`-linear slope (`p = 7`: `2.83` measured against
`4.45` predicted; `p = 14`: `9.10` / `10.73`; `p = 22`: `17.02` / `18.55`;
`p = 30`: `25.83` / `26.37`). The one non-monotone row is instructive rather
than anomalous: at `p = 26` the first passer happens to be a convergent
denominator with `γ = 17.06`, and the deficit collapses to `8.52` — the base
construction's shortfall is `Θ(p)` *at fixed `γ`*, and buying it off costs
`Θ(p)` bits of Diophantine quality, i.e. `x_n` exponentially small in `p`.
That is the same trade the record was unknowingly making.

**Consequence — item 5.3 of `briefs/staircase-allp-findings.md` is refuted as
stated, and gap B is thereby diagnosed rather than closed by force.** That item
proposed proving the correction algorithm needs `O(1)` or `O(log p)` moves. Each
move of `12.8.6.3` shifts one unit of depth and buys `O(1)` bits of the worst
rotation's margin, while the base profile's deficit is `Θ(p)`. So the move count
is `Θ(p)` at fixed `γ`, and **no `O(1)` or `O(log p)` bound on `12.8.6.3` exists
to be proved at the base profile of `12.8.6.2`.** The observed growth (`0` moves
at small `p`, `8` at `p ∈ {18, 23, 24, 25}`, `13` at `p = 22`) is that linear
law, partially masked by the larger `γ` the record's convergent-quality
candidates happened to carry. The right move is not to bound the algorithm; it
is to remove the shortfall.

---

## 3. Why the shortfall exists: the profile is wrong by an additive constant

Ask for a real profile making `D_r` *constant in `r`*. Put
`T_r = C·L^r + r/(L−1) + b`. Then

```text
m_r = T_r − T_{r−1} = C(L−1)L^{r−1} + 1/(L−1),
m_r + r − (L−1)T_{r−1} = 1/(L−1) + 1 − (L−1)b        (constant in r).
```

So **the correct staircase is geometric *plus a fixed additive offset*
`1/(L−1) = 1.70951` per block**, and the offset's meaning is exact and
mechanical: at the exchange rate `L−1 = log_2(3/2)`, an extra `1/(L−1)` units of
standing depth generate `(L−1)·1/(L−1) = 1` extra bit of credit per block —
precisely the one unit of exit valuation each climb block spends.
`12.8.6.2`'s pure geometric profile carries no such offset, so it runs a deficit
of **exactly one bit per block**. That single missing constant is the whole of
gap B.

Pinning `C, b` by `T_{−1} = 0`, `T_{p−2} = n − c` gives the continuous
requirement `γ ≥ 1/(L−1) + 1 − (L−1)b + η`, i.e. for `n = κL^p`, `c = 1`, `p`
large,

```text
γ  ≥  0.92714·κ + 1.70951 + η .
```

The integer construction below pays one further unit for rounding, landing at
`0.92714·κ + 2.70951 + η`.

---

## 4. The construction (exact integers; no correction step)

Rather than round the closed form of §3, saturate `(C_r)^Z` directly.

> **Construction B.** Given a period `p ≥ 2` and an integer `n` with
> `K := ⌈nL⌉`, `S := K − n ≥ p`, `q := 2^K − 3^n`, `s_crash := S − (p−1)`:
> set `T_{−1} = 0` and for `r = 0, …, p−2`
>
> ```text
> X_r      = 3^{T_{r−1}} · 2^{n − T_{r−1} + p − 1 − r} · (2^{s_crash} − 1)
> cap_r    = max{ m ≥ 0 : q·2^m ≤ X_r }        ( = bitlength(⌊X_r/q⌋) − 1 )
> budget_r = n − 1 − T_{r−1} − (p − 2 − r)
> m_r      = min(cap_r, budget_r)
> T_r      = T_{r−1} + m_r
> ```
>
> and `m_{p−1} = c := n − T_{p−2}`, `s_j = 1` for `j ≤ p−2`,
> `s_{p−1} = s_crash`.

`cap_r` is exactly `⌊γ + (L−1)T_{r−1} − r − η⌋`; the displayed form computes it
with integer division and `bit_length` alone. `budget_r` reserves one unit of
depth for every climb block still to come and one for the crash block. **No
floating point occurs anywhere in the construction or in its verification.**

`K = ⌈nL⌉` is likewise computed exactly and without floats, as
`bit_length(3^n)` (`L` is irrational, so `nL` is never an integer).

---

## 5. The theorem

Put `β := 1 + η` and

```text
Γ(p, n) := [ (n−1)(L−1)² + L^{p−1}·(1 + β(L−1)) − (p−2+β)(L−1) − L ]
           ────────────────────────────────────────────────────────
                          (L−1)·(L^{p−1} − 1)
```

**Theorem B.** Let `p ≥ 2`, `n ≥ 1` be integers, `K = ⌈nL⌉`, `S = K − n`,
`γ = K − log_2(2^K − 3^n)`, and assume

* **(H0)** `S ≥ p` and `(L−1)(n − p) + γ ≥ p + η`;
* **(H1)** `γ ≥ max( 2 + η , Γ(p, n) )`.

(H0) is a scale side-condition and is automatic at the canonical scale:
`S = ⌈nL⌉ − n ≈ 0.585n` and `(L−1)(n−p) ≈ 0.585n`, both `≫ p` once
`n ≳ 2.71p`, which holds for every `p ≥ 6` at `n ≈ L^p`. It is used twice and
only twice: to keep `cap_j ≥ 1` in the flat tail after the landing budget
binds, and to give `(C_{p−1})` at `c = 1`.

(The `2 + η` clause is free wherever the theorem is used: `Γ(p,n) ≥ 2 + η`
already holds for every `(p, n)` satisfying (H0) in the whole verified range,
and `Γ → 2.7095 + η` from above as `p` grows. It is written into the hypothesis
rather than derived because `Γ(p,n)` *does* dip below `2` at the few tiny
`(p, n)` that (H0) already excludes — e.g. `Γ(3,2) ≈ 1.77` — and the proof of
step (a) needs `γ ≥ 2 + η` outright.)

Then Construction B returns a period-`p` profile with all entries `≥ 1`,
`Σ m_t = n`, `Σ s_t + n = K`, **crash depth exactly `1`**, satisfying
`q ≤ R_r` for **every** rotation `r` — with no correction step.

*Proof.*

**(a) Well-definedness.** Let `f_r := γ + (L−1)T_{r−1} − r − η`, so
`cap_r = ⌊f_r⌋`. Run first the *uncapped* greedy (`m̂_r = cap_r` always). Then
`f̂_{r+1} − f̂_r = (L−1)·cap_r − 1 ≥ 2(L−1) − 1 = 0.1699 > 0` whenever
`cap_r ≥ 2`. (H1) gives `f̂_0 = γ − η ≥ 2`, so `cap_0 ≥ 2`, and induction gives
`cap_r ≥ 2` for every `r`: **`γ ≥ 2 + η` alone makes the greedy run to
completion — it can never die.** For the capped greedy, `m_r ≤ cap_r` and
`cap_r` is nondecreasing in `T_{r−1}` (because `X_r` is), so `T_r ≤ T̂_r` by
induction; once the budget binds, `T_j` is within `p` of `n` and
`cap_j ≥ 1` follows from (H0). Each `budget_r ≥ 1` by induction, so every
`m_r ≥ 1`.

**(b) Growth.** `m̂_r = ⌊f̂_r⌋ > f̂_r − 1` gives
`T̂_r > L·T̂_{r−1} + γ − r − β`. Let `A_{−1} = 0`,
`A_r = L·A_{r−1} + γ − r − β`. Then `T̂_r > A_r` for all `r ≥ 0`.

**(c) Closed form.** Summing the recursion,
`A_r = Σ_{j=0}^{r} L^{r−j}(γ − β − j)`, and the two geometric sums give

```text
A_r = [ L^{r+1}·((γ−β)(L−1) − 1) + (r + β − γ)(L−1) + L ] / (L−1)² ,
```

whence `A_{p−2} ≥ n − 1` is, after clearing denominators, **exactly**
`γ ≥ Γ(p, n)`. Note in passing that `A_r` grows geometrically iff
`(γ−β)(L−1) > 1`, i.e. `γ > β + 1/(L−1) = 2.7095 + η` — which is precisely the
constant term of `Γ`, so (H1) supplies it wherever `Γ` has reached its
asymptote; the proof itself does not need it (step (c) is an identity), and
step (a) already guarantees the greedy cannot die.

**(d) The climb lands on `n − 1`.** `T_{p−2} ≤ n − 1` always, by `budget`.
Suppose `T_{p−2} < n − 1`. If the budget had bound at some `r*`, then
`T_{r*} = n − 1 − (p−2−r*)` and every later `m_j = 1`, giving `T_{p−2} = n − 1`
— contradiction. So the budget never bound, `m_r = cap_r` for all `r`,
`T = T̂`, and by (b), (c), (H1), `T_{p−2} = T̂_{p−2} > A_{p−2} ≥ n − 1` —
contradiction. Hence `T_{p−2} = n − 1` and `c = 1`.

**(e) The size conditions.** For `r ≤ p−2`, `m_r ≤ cap_r` *is* `(C_r)^Z`, i.e.
`q ≤ 3^{T_{r−1}}·2^{n − T_r + p − 1 − r}·(2^{S−p+1} − 1)`, which is one term of
`R_r`; every term of `R_r` is positive, so `q ≤ R_r`. For `r = p−1`, `(C_{p−1})`
reads `c·L ≤ γ + (L−1)n − (p−1) − η` with `c = 1`, implied by (H0). ∎

### The exact hypothesis on `n` — the interface to the sibling result

This is the deliverable's most important line, so it is stated on its own.

> **Construction B consumes exactly one property of the candidate `n`:**
>
> ```text
>       ⌈n·log_2 3⌉ − n·log_2 3   ≤   −log_2( 1 − 2^{−Γ(p,n)} )
> ```
>
> **equivalently `γ(n) ≥ Γ(p,n)`, together with the scale side-condition (H0).
> Nothing else about `n` is used** — not that it is a convergent denominator,
> not that it is a semiconvergent, not any continued-fraction structure, not a
> sign condition on a run, not membership in any chain.

Concretely, at the canonical scale: **for every `n` in `[L^p, 1.05·L^p]` with
`⌈nL⌉ − nL ≤ 0.117`, Construction B passes all `p` size conditions.** Since
`−log_2(1 − 2^{−Γ}) ≈ 1.4427·2^{−Γ}` and `Γ → 3.637` at `κ = 1`, that is a
**density-`0.117` condition** on `n`, uniform in `p`. The window
`[L^p, 1.05·L^p]` holds `0.05·L^p` integers, which exceeds the reciprocal
density `8.6` once `p ≥ 12`; below that, widen the window (`κ ≤ 2` still only
asks `x_n ≤ 0.064`) or check the period directly. Existence then follows from
any effective form of Weyl equidistribution or the three-distance theorem — no
sign condition, no run structure. Empirically the first `n ≥ round(L^p)`
meeting the hypothesis sits at offset `≤ 11` (mean `3.6`) at **every**
`p ∈ {2,…,30}` except `p ∈ {2, 4}` (§9 records why those two are outside the
theorem's reach).

---

## 6. The `γ` formula

`Γ(p,n)`'s exact form is displayed in §5. Its asymptotics, with `κ := n/L^p`:

```text
Γ(p,n)  =  (L−1)·n / L^{p−1}  +  1/(L−1)  +  β  +  O(p·L^{−p})
        =  0.92714·κ  +  2.70951 + η  +  O(p·L^{−p}) .
```

**Growth in `p`: none. `γ = O(1)`.** At `κ = 1`, `Γ` rises to `3.637` and stays
there — `3.589` at `p = 13`, `3.635` at `p = 22`, `3.637` at `p = 30` and at
`p = 32`, never exceeding `3.64`. The `γ` actually achieved at the first passer
found ranges over `[2.91, 17.06]` across `p = 2..32` with **no upward trend**
(the large values are accidents of which `n` came first — `p = 26`'s
`γ = 17.06` is a convergent denominator; nothing needed it), and
`γ / log_2 p` **decreases** with `p`: `4.30` at `p = 2`, `0.97` at `p = 10`,
`0.82` at `p = 22`, `0.79` at `p = 30`, `0.61` at `p = 31` — against the
record's `γ/log_2 p ∈ [1.828, 3.643]`.

Read in the other direction, the quality actually consumed is

```text
x_n  ≤  −log_2(1 − 2^{−Γ})  ≈  1.4427 · 2^{−(0.92714·κ + 2.70951)} ,
```

so the Diophantine demand is **constant in `p`** and degrades only in `κ`,
exponentially: `κ = 1 → x_n ≤ 0.121`; `κ = 2 → 0.064`; `κ = 4 → 0.017`;
`κ = 8 → 0.0013`. All four rates were confirmed against the first passer found
(NC-E), with the search window sized from the predicted density so that a
"no passer" would have been a result and not a budget artifact.

**This is strictly stronger than the `O(log p)` the published `thm:staircase`
assesses, and it means the sibling's budget is much weaker than `O(log p)` too.**
`O(log p)` would license `x_n` shrinking polynomially in `p`; the construction
needs no shrinkage at all.

---

## 7. Verification and negative controls

`experiments/staircase_allp_construction.py`, exact big-integer arithmetic;
`experiments/staircase_allp_construction_output.txt` is the committed run
(`python experiments/staircase_allp_construction.py 30`, ~7 minutes).

**Canaries (Part 0).** The trivial cycle read as a fake period-`p` cycle gives
`R_r = q = 4^p − 3^p` at `p ∈ {1,2,3,4,7,11}`; the transport recurrence of
Remark `12.6.1.1` holds at all rotations of `200` random profiles (used as an
*audit* of the numerator code, never to compute it); and `12.8.3`'s published
`p = 7` staircase `m = (4,7,9,15,23,35,1)` reproduces `γ = 6.744`, passes all
seven size conditions, and fails divisibility at all seven.

**Main table (Part 1).** For every `p ∈ {2,…,30}`, walking `n` upward from
`round(L^p)`: an exact passer at offset `≤ 5` (mean `1.8`), and a
*theorem-certified* `n` (one satisfying (H1), hence covered by the proof rather
than by exhibition) at offset `≤ 11` (mean `3.6`) for every `p` except
`p ∈ {2,4}`. Every certified instance was independently re-verified through
`R_r` computed from `12.6.1` — all `p` rotations, exact — and every one has
crash depth exactly `1`, as the theorem asserts.

**Beyond the record (Part 4).** `p = 31` (`n = 1,587,045`, `γ = 3.033`) and
`p = 32` (`n = 2,515,409`, `γ = 4.594`) — past `12.8.6.4`'s `p ≤ 23`.

**Proof steps checked (Part 3).** Each step of §5 is checked separately over a
grid of `(p, n)`: the big-integer `cap_r` agrees with
`⌊γ + (L−1)T_{r−1} − r − η⌋` at every one of `~1{,}800` greedy steps (step a);
`γ ≥ 2 + η` keeps `cap_r ≥ 2` throughout (step a); `T̂_r > A_r` at every step of
the **uncapped** greedy (step b); the closed form of `A_r` matches the recursion
and the equivalence `A_{p−2} ≥ n−1 ⟺ γ ≥ Γ(p,n)` holds (step c); and every
certified `n` yields **crash depth exactly `1`** (step d), `42` instances.
Zero violations. Additionally `Γ(p,n) ≥ 2` over all `(p,n)` satisfying (H0) in
the grid, attained with equality at `(p,n) = (2,2)`.

Two bugs in the session's own test harness are recorded rather than smoothed
over, since both produced red checks that had to be diagnosed before anything
could be called verified. (i) The first step-(b) check compared the
*budget-capped* `T_r` against `A_r` and reported `42` violations. `A_r` keeps
growing geometrically after the landing budget binds and `T_r` deliberately does
not, so the comparison was meaningless; the proof bounds `T̂`, and against `T̂`
the check is clean. The violations sat at exactly the rows with `γ ≥ Γ` — where
the budget binds — which is what identified the error. (ii) Fixing (i)
introduced an early exit from the `T̂` loop (once `T̂` passes `n−1`, continuing
would raise `3^{T̂}` past any useful size), and the step-(c) check was still
reading `A` off the end of that loop, so it compared `A_{r*}` against the closed
form at `r = p−2`: `33` spurious failures. `A_r` is a pure real recursion and is
now run over the full `p−1` steps independently of the greedy. Neither bug was
in the construction or in the size test; both were in the scaffolding that
checks the *proof's* algebra, which is exactly the part that had no prior
implementation to disagree with.

**Divisibility.** Every constructed instance at every period, and the `p = 7`
cross-check, was tested for `q | R_r` at all `p` rotations: **none passes**,
matching `12.8.3` and `12.8.6.4`. Every instance also respects Theorem
`12.8.1`, checked as a canary.

### Negative controls (all four required perturbations)

**NC-A — the quality hypothesis bites.** Sweeping `n` over a `64`-wide window at
the canonical scale for `p ∈ {4,7,10,13,16,19,22}`: **soundness**, no `n` with
`γ ≥ Γ` ever fails (0 violations, over `3`–`9` certified `n` per period at
`p ≥ 7`; at `p = 4` there are none, so that row's soundness is vacuous — see §9);
**bite**, `78`–`94%` of the `n` in the window *do* fail (passers `4`–`14` of
`64`), so the hypothesis is very far from vacuous. The largest `γ − Γ` among
failers is negative at every `p` (`−0.72` to `−1.03`), and the smallest among
passers is `−0.60` to `−0.86` for `p ≥ 10`: `Γ` is conservative by roughly
`0.6`–`0.9` bits, which is the price of the one-sided single-term bound `(C_r)`.

**NC-A2 — the `κ`-dependence is not decoration.** Same test at
`p ∈ {8,12,16,20}` with the scale multiplied by `1,2,3,5,8`. Passer counts fall
monotonically at every `p` (at `p = 20`: `13/64 → 10/64 → 6/64 → 4/64 → 0/64`)
exactly as `Γ ≈ 0.927κ + 2.71` predicts, with zero soundness violations in any
of the `20` cells.

**NC-B — the rounding rule is load-bearing.** At the *same* `n`, same shape,
same crash depth, only the integer-rounding rule changed:

| rule | passes |
| --- | --- |
| greedy saturation of `(C_r)^Z` (this work) | **29/29** |
| partial-sum rounding of the *pure* geometric (`12.8.6.2`) | 6/29 |
| per-block rounding of the pure geometric | 6/29 |

and the failures are not marginal: the base construction fails `9` of `14`
rotations at `p = 14`, `21` of `27` at `p = 27`, `24` of `30` at `p = 30`; its
six successes are all at `p ≤ 8`. This isolates the additive
`1/(L−1)` offset of §3 as the entire content of the fix.

**NC-C — the crash depth is load-bearing.** Re-running with the crash depth
forced up to `c = 1,2,4,8,…`, the largest passing `c` and the first failing `c`
bracket the derived ceiling `c_max = (γ + (L−1)n − (p−1))/L ≈ 0.369n` at every
period tested (`p = 6`: pass `4`, fail `8`, ceiling `6.1`; `p = 12`: pass `64`,
fail `128`, ceiling `87.7`; `p = 21`: pass `4096`, fail `8192`, ceiling
`5844`; `p = 27`: pass `65536`, fail `131072`, ceiling `92802`). The first
failing rotation is always `r = p−1`, as `(C_{p−1})` says it must be.

**NC-D — the construction sits on the boundary.** Local perturbation
`m_j += δ`, `m_{j+1} −= δ` (which leaves every other partial sum, and `n, K, q`,
untouched, so it tightens exactly `(C_j)`): the smallest `δ` breaking the
**exact** test `q ≤ R_j` is `1` or `2` at every one of the `102` blocks tested
across `p = 6, 8, …, 22` — never `3` or more. The caps are genuinely
saturated; the slack is the
`≈ 1` bit of floor plus the `≈ 0.5` bit of dropped terms, and nothing more.

**NC-E — the `γ` formula.** Reported in §6.

---

## 8. Verdict, and what to recommend to the main session

**Can `12.8.6.3` be removed from the argument rather than merely bounded? Yes.**
Theorem B has no correction step, no local search, no move budget and no logs.
The recommendation (for the main session to weigh; `cycles.md` untouched here):

1. Replace Construction `12.8.6.2` by Construction B and **delete Algorithm
   `12.8.6.3` from the argument** (keeping it, if wanted, only as the historical
   route in the record).
2. Restate `12.8.6`'s obstruction paragraph: the correction algorithm's
   unbounded move count is **closed**, and closed by removal. What replaces it is
   Theorem B with the interface hypothesis of §5 stated verbatim.
3. **Retarget the sibling's coverage lemma.** `12.8.6.1` currently needs a
   correctly-signed continued-fraction run and a bound on the multiplicative gap
   between consecutive runs. Theorem B needs only: *every interval
   `[N, 1.05N]` contains an `n` with `⌈nL⌉ − nL ≤ 0.117`.* That is a
   three-distance / effective-Weyl statement about `log_2 3` with no sign
   bookkeeping, no convergent structure and no chain, and it should be
   substantially easier than the gap as currently posed. The two results compose
   at exactly this line.
4. `12.8.3`'s "`γ = O(log p)`" and the paper's `thm:staircase` may be
   **strengthened to `γ = O(1)`** at the constructed family, once (3) lands.
   Nothing should move before the sibling's half is in.
5. `12.8.5` and the README stopping rules are unaffected: this is sharper
   evidence that counting arguments cannot do better, and no evidence at all
   about exclusion.

---

## 9. Failures, dead ends and scope limits — recorded, not deleted

* **Item 5.3 of `briefs/staircase-allp-findings.md` is refuted as a target**, not
  merely unachieved: the base profile's shortfall is `Θ(p)` (§2), so the `O(1)`
  or `O(log p)` move bound it proposed does not exist. This is the session's
  principal negative result and it is what made route (ii) mandatory rather than
  merely preferable.
* **Items 5.1 and 5.2 (a second crash block; non-unit climb exits near the
  crash) were not needed and are superseded in motivation.** They were proposed
  as extra degrees of freedom to relieve the observed resistance. The resistance
  was never a shortage of freedom — it was a mis-specified profile, off by the
  additive constant `1/(L−1)` per block. Neither variant was built; neither is
  required. This does not refute them (either might give a smaller `Γ`
  constant); it removes the reason to try.
* **`p ∈ {2, 4}` have no theorem-certified `n` at the canonical scale.** `Γ`'s
  coefficient on `n` is `(L−1)/(L^{p−1} − 1)`, which is `O(L^{−p})` only once
  `L^{p−1} ≫ 1`; at `p = 2, 4` it is large enough that the required quality
  outruns what integers at that tiny scale supply. Both periods have exact
  passers by direct exhibition (Part 1), so they are covered by the finite check
  rather than by the asymptotic hypothesis — but the theorem as stated does not
  reach them, and that is a genuine limit, not a rounding detail.
* **`Γ` is conservative by `0.6`–`0.9` bits** (NC-A), because `(C_r)` keeps one
  term of `R_r` and discards `p−1` positive ones. Sharpening `(C_r)` to `(★)`
  would buy that back; it was not attempted, since the constant is already
  `O(1)` and the gain would not change the growth rate.
* **The `Θ(p)` shortfall law of §2 is derived for the exact-real geometric
  profile plus a rounding envelope**, and verified against the measured deficit
  at every period in the table; it is not an asymptotic claim about the
  *algorithm* `12.8.6.3`, whose move count is bounded above by the shortfall
  divided by the per-move gain but has no proved lower bound here. The precise
  statement is: no `O(1)`/`O(log p)` *upper* bound on the move count can follow
  from the shortfall, because the shortfall it must close is `Θ(p)`.
* **The verification's reach is bounded by big-integer cost**, not by the
  mathematics: `p = 32` means `n ≈ 2.5·10^6` and `3^n` at `4·10^6` bits. Nothing
  in Theorem B degrades with `p`; the table simply stops where the arithmetic
  gets slow.
