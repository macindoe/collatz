# Findings: staircase-gamma-upper (gate P1) — 2026-07-28

Brief: `briefs/staircase-gamma-upper-brief.md`. Branch `staircase-gamma-upper`.
**Base SHA `cec521c`** — the worktree was cut from `2225b68`, which does not
contain the brief; the branch was re-cut at `cec521c` before any work began.

Verification code: `experiments/staircase_gamma_upper.py` (fresh; imports nothing
from `staircase_allp.py`, `staircase_allp_construction.py`,
`staircase_allp_diophantine.py`, `p22_passer.py` or `uniform_trim.py`).
Committed output: `experiments/staircase_gamma_upper_output.txt` — **45 checks,
0 failures**, 19 s (`python experiments/staircase_gamma_upper.py 30` extends the
end-to-end table to `p = 30`, 173 s).

**Verdict.** **`γ = O(1)` is now proved** — indeed `γ ≤ 5.1403`, an absolute
constant, for every period `p ≥ 16`, with the finite tail `3 ≤ p ≤ 15` covered by
exhibition and `p ∈ {2, 4}` outside Construction B's reach. The exact arithmetic
does **not** eat the margin: the exact `δ_hi` comes out *above* the record's
rounded `0.116939`, and (H0) is not merely satisfied at the smallest `p` — it is
implied by the scale alone, with margin `≈ 900`. `p₀ = 16` is unchanged.

**Stopping-rule compliance.** Size-passers only, never cycles. The divisibility
system is touched only to confirm that every constructed instance **fails** it
(23 periods, all rotations, zero divisible). No per-period cycle search was run;
no divisibility-based exclusion was attempted. **The cycle front stays PARKED and
`12.8.5` is unaffected at any grade.** `cycles.md`, `README.md`,
`publication.md`, `paper/` and `sources/` are untouched — §8 is a recommendation
for the main session, not an edit.

---

## 0. The gap, and what closes it

Theorem B (`briefs/staircase-allp-construction-findings.md` §5) needs
`γ(n) ≥ Γ(p,n)` — **larger `γ` is easier**. Lemma D
(`briefs/staircase-allp-diophantine-findings.md` §6.3) supplies `δ` small, hence
`γ` large, and says nothing above. Sharpness wants `γ` *small*, so the delivered
witness could be arbitrarily bad: at `p = 26` the first Lemma-D witness has
`δ ≈ 10⁻⁵` and `γ = 17.058`.

The repair is to replace the half-line `δ ≤ δ_hi` by a two-sided **arc**
`δ_lo ≤ δ ≤ δ_hi`, exactly as `briefs/staircase-status-audit-findings.md` §0.1
proposed. This session re-derived the whole chain in certified arithmetic,
supplied the two things the sketch did not settle ((H0) and an honest `p₀`),
optimised the constant, and ran the required negative controls.

Notation throughout, as in `12.6.1`/`12.8` and Theorem B:

```text
L = log_2 3,   delta(n) = ceil(nL) - nL in (0,1),   gamma(n) = -log_2(1 - 2^-delta(n)),
theta = 8 - 5L,   K = ceil(nL),   S = K - n,   q = 2^K - 3^n,   kappa = n / L^p.
```

`gamma` is strictly decreasing in `delta`, and `delta ↦ gamma` is its own inverse:
`gamma(n) ≥ G ⟺ delta(n) ≤ −log₂(1 − 2^{−G})`. That involution is the hinge of
everything below.

---

## 1. The arithmetic discipline

A proof whose margin depends on a truncated decimal is not a proof, so nothing
here is a float.

* **`L`** is enclosed in an exact rational interval of width `< 10^{-135}` by the
  series `ln 2 = 2 atanh(1/3)`, `ln(3/2) = 2 atanh(1/5)` with an explicit
  remainder bound, all in `Fraction`. Cross-certified three ways: against exact
  big-integer comparisons `3^b` vs `2^a` at nine continued-fraction convergents
  of `L` (the only fully elementary certification available, good to `~10^{-9}`),
  and against `mpmath.iv`, which is directed-rounding interval arithmetic.
* **Per-`n` decisions** — `K = ⌈nL⌉`, and `δ(n)` against any rational threshold —
  are exact integer comparisons against a `2^{256}`-scaled integer enclosure of
  `L`. A decision the enclosure cannot resolve **raises**; it is never guessed.
  Canary: `K` from the enclosure equals `bit_length(3^n)` at 405 values of `n`.
* **Transcendental constants** are computed in `mpmath.iv` and immediately
  converted to exact rational endpoints; every inequality the theorem rests on is
  then checked as an exact rational inequality, and every printed decimal is
  truncated (never rounded up) so that a printed bound is always a true bound.
* **Construction B and every `R_r`** are exact big integers throughout.

---

## 2. `sup Γ`, and the exact `δ_hi`

`Γ(p,n)`'s displayed form (Theorem B §5) contains `β = 1 + η`,
`η = −log₂(1 − 2^{−s_crash})`. Writing `u = L−1`, `D = L^{p−1}`, the `β`-terms of
the numerator are exactly `βu(D−1)` and the denominator is `u(D−1)`, so

```text
Gamma(p,n) = Gamma_0(p,n) + eta          (eta enters with coefficient exactly 1),
Gamma_0(p,n) = [ (n-1)u^2 + D - (p-2)u - L ] / [ u(D-1) ]  +  1 .
```

Checked numerically to `10^{-40}` at four `(p,n)`. Everywhere the theorem is
applied `s_crash ≥ 900`, so `η < 2^{-900}` and is carried as an explicit rational
cap, not dropped.

**The supremum is proved algebraically, not tabulated.** Substituting
`n ≤ 1.05·L·D` and separating `D/(D−1) = 1 + 1/(D−1)`:

```text
Gamma_0(p,n)  <=  1.05*L*u + 1/u + 1  +  B(p)/(D - 1),
B(p) := 1.05*L*u + 1/u - u - (p-2) - L/u .
```

`B(2) ≤ −0.6114616914 < 0` and `B` decreases in `p`, so the correction term is
negative for every `p ≥ 2`. Hence, with

```text
Gamma*  :=  1.05*L*(L-1) + 1/(L-1) + 1 + eta   <=  3.683012100722 ,
```

**`Γ(p,n) < Γ*` for every `p ≥ 2` and every `n ≤ 1.05·L^p`** — the value
`3.683012…` the record quotes as a supremum over `p = 6…2000` really is the
`p → ∞` limit, approached from below and never attained. (Both halves are
re-checked numerically over `p ∈ {2,…,199, 300, 500, 1000, 2000}`; at large `p`
the gap is `~10^{-400}`, far below any interval engine, which is exactly why the
strictness must come from `B(p) < 0` and not from a table.)

The induced upper end of the arc is

```text
delta_hi := -log_2(1 - 2^-Gamma*)   >=  0.116939066509 .
```

**Answer to the brief's item 1: the exact `sup Γ` does *not* push `δ_hi` below
`0.116939`.** It puts it fractionally *above*, at `0.11693906650…`, so the
record's rounded `0.116939` is a safe (conservative) threshold and Lemma D as
recorded is unaffected. The margin the whole result depends on survives exact
arithmetic.

---

## 3. Lemma G — the two-sided sweep, in its sharp form

Lemma D's mechanism is that `5L = 8 − θ`, so `n → n+5` advances `δ` by exactly
`θ` (mod 1): the values `δ(N), δ(N+5), …, δ(N+5J)` are `δ(N) + jθ`. The recorded
lemma then argues "`14θ ≥ 1`, so the 15 points lie around a full turn, so any arc
longer than `θ` contains one". That is a *sufficient* condition, and it is not
the one that governs. The sharp criterion is:

> **Lemma G.** Let `A ⊆ ℝ/ℤ` be a closed arc of length `ℓ`. The `J+1` points
> `{δ(N) + jθ : 0 ≤ j ≤ J}` meet `A` **for every** starting phase `δ(N)`
> **if and only if**
>
> ```text
> maxgap{ j*theta mod 1 : 0 <= j <= J }  <=  ell .
> ```
>
> For `Jθ < 1` that maximal gap is `max(θ, 1 − Jθ)`, so for `ℓ > θ` the minimal
> sweep is `J = ⌈(1 − ℓ)/θ⌉`, and the guarantee covers any `5J + 1` consecutive
> integers.

*Proof.* The set of starting phases the sweep catches is the union of the `J+1`
translates `A − jθ`. Their left endpoints are a translate of `{−jθ mod 1}`, which
has the same gap multiset as `{jθ mod 1}` (reflection is an isometry). A union of
closed arcs of common length `ℓ` covers the circle iff every gap between
consecutive left endpoints is `≤ ℓ`; and if some gap `g > ℓ`, the phase
`a + ℓ + ε` (`ℓ + ε < g`) lies in no translate. ∎

**Consequences, both certified in Part 2 of the script.**

| arc | length `ℓ` | minimal `J` | consecutive integers |
|---|---|---|---|
| one-sided (recorded Lemma D) `[0, δ_hi]` | `0.116939066509` | **12** | **61** |
| two-sided (this result) `[δ_lo, δ_hi]` | `0.075439066509` | **13** | **66** |

So the record's "among any 71 consecutive integers" is **true but not minimal**
(61 suffice), and the audit's "the identical 71-integer argument" is **true but
not derived** — the two-sided arc needs 66, and 66 ≤ 71, so its conclusion stands
while its stated reason does not. The genuinely binding inequality in both cases
is the one the audit did check, `ℓ > θ`; the span condition it invoked is not the
criterion.

`J = 12` (61 integers) is verified to be genuinely insufficient for the two-sided
arc: `maxgap(12) = 0.097750043269 > 0.075439066509`, and 447 of the first 20,000
starting values `N` are actual counterexamples (first at `N = 22`).

---

## 4. Theorem G, with its exact constants

> **Theorem G (the `γ` bracket).** Let `p ≥ 16`. With
>
> ```text
> Gamma*   = 1.05*L*(L-1) + 1/(L-1) + 1 + eta   <=  3.683012100722
> delta_hi = -log_2(1 - 2^-Gamma*)              >=  0.116939066509
> theta    = 8 - 5L                             <=  0.075187496395
> delta_lo = 0.0415       (any value < delta_hi - theta = 0.041751570114 will do)
> ```
>
> the arc `[δ_lo, δ_hi]` has length `0.075439066509 > θ` (certified margin
> `0.000251570114`), so by Lemma G every 66 consecutive integers contain an `n`
> with `δ_lo ≤ δ(n) ≤ δ_hi`. The window `[L^p, 1.05·L^p]` contains at least 66
> consecutive integers for every `p ≥ 16`, and **(H0) holds at every integer of
> that window**. For such an `n`,
>
> ```text
> Gamma(p,n)  <  Gamma*  <=  gamma(n)  <=  5.140211486072 ,
> ```
>
> so Theorem B applies and Construction B returns a period-`p` profile passing all
> `p` size conditions `q ≤ R_r` with crash depth `1` and
>
> ```text
> 3.683012  <=  gamma  <=  5.140212        uniformly in p.
> ```

*Proof.* §2 gives `Γ(p,n) < Γ*` for `n ≤ 1.05L^p`; the involution turns
`δ(n) ≤ δ_hi` into `γ(n) ≥ Γ* > Γ(p,n)`, which is (H1) (the clause `γ ≥ 2 + η` is
implied, `Γ* > 2`). `δ(n) ≥ δ_lo` turns into `γ(n) ≤ −log₂(1 − 2^{−δ_lo})`, the
stated constant. Lemma G supplies such an `n` in 66 consecutive integers; §5
supplies the window count and (H0). Theorem B then does the rest. ∎

The lower end is not slack that could be given away: `δ ≤ δ_hi` is *exactly*
Theorem B's hypothesis at the conservative threshold, so `γ ≥ Γ*` is forced. The
witness's `γ` lives in a bracket of width `1.457` bits, and both ends are
absolute constants with no `p` in them.

---

## 5. `p₀`, the window count, and the finite tail

The two-sided condition raises the sweep requirement from 61 to 66 consecutive
integers. **It does not move `p₀`.** Exact integer counts of the window
`[L^p, 1.05·L^p]` (certified endpoints):

| `p` | 13 | 14 | **15** | **16** | 17 | 18 | 20 | 24 |
|---|---|---|---|---|---|---|---|---|
| integers in window | 20 | 31 | **50** | **79** | 126 | 199 | 501 | 3159 |

`p = 16` is the first period whose window holds 66 consecutive integers, so
**`p₀ = 16`** — the same crossing as Theorem D's, and the margin there is real but
not large (79 against 66). `p = 15` genuinely falls short, so the finite tail is a
finite tail and not a vacuous clause.

**The tail, `3 ≤ p ≤ 15`, by exhibition.** The window is widened (the hypothesis
is evaluated per-`n`, so the larger `Γ` at larger `κ` is paid for exactly), and
the *same* two-sided bracket is met at an explicit `n` at every period:

| `p` | 3 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `n` | 5 | 17 | 17 | 34 | 46 | 70 | 111 | 164 | 258 | 405 | 646 | 1005 |
| `κ` | 1.256 | 1.700 | 1.072 | 1.353 | 1.155 | 1.109 | 1.110 | 1.034 | 1.027 | 1.017 | 1.023 | 1.004 |
| `γ(n)` | 4.299 | 4.724 | 4.724 | 3.752 | 4.021 | 4.803 | 4.417 | 4.480 | 4.218 | 4.045 | 3.716 | 3.734 |
| `Γ(p,n)` | 3.934 | 3.750 | 3.256 | 3.605 | 3.510 | 3.543 | 3.600 | 3.571 | 3.594 | 3.606 | 3.626 | 3.619 |

Every row satisfies (H0), (H1) and `γ ≤ 5.1403`, all certified, and every row was
run end to end (§7).

**`p ∈ {2, 4}` are outside Construction B's reach**, and the reason is sharper
than "the required quality outruns the integers": `Γ(2,n) = n + η` and
`Γ(4,n) ≈ 0.196n + 1.507`, so `γ ≤ C` caps `n` at `5` and `18` respectively, and
no integer in those ranges meets the arc together with (H0). Their canonical
windows `[L^2, 1.05L^2] = [2.51, 2.64]` and `[L^4, 1.05L^4] = [6.31, 6.63]`
contain no integer at all. This matches the sibling's own §9 scope limit and is
not a new exclusion.

---

## 6. (H0) at the smallest `p` — the item the audit flagged and did not check

(H0) is `S ≥ p` **and** `(L−1)(n−p) + γ ≥ p + η`. The audit's worry was that the
two-sided condition, by *capping* `γ`, might remove the slack (H0) needs. It does
not, and the reason is that (H0) is a scale condition, not a quality condition:

```text
S = ceil(nL) - n >= (L-1)*n >= (L-1)*L^p ,      and   gamma >= Gamma* > 3.683 ,
```

so both clauses follow from `n ≥ L^p` alone, for every `p ≥ 16`, with no
reference to which `n` in the window the sweep happens to deliver. Certified for
`p ∈ {16,…,399, 1000, 2000}`. At the smallest case `p = 16` the two margins are

```text
(L-1)*L^16 - 16                    =  911.75
(L-1)*(L^16 - 16) + Gamma* - 16    =  906.07
```

— not marginal by any reading. The `γ` cap is worth `≈ 1.46` bits and the margin
is `≈ 900`; the interaction the audit could not rule out is three orders of
magnitude from being real. **(H0) verdict: holds unconditionally for every
`p ≥ 16` and every `n` in the window.** For the tail it is checked per witness
(all pass); the clause that actually fails at tiny `p` is the first one,
`(L−1)L^p ≥ p`, which is false at `p = 2` (`1.4694 < 2`) — consistent with §5.

---

## 7. Verification, end to end, and the negative controls

`experiments/staircase_gamma_upper.py`, 45 checks, 0 failures.

**Canaries.** The trivial cycle read as a fake period-`p` cycle gives
`R_r = q = 4^p − 3^p` at `p ∈ {1,2,3,4,7,11}`; `12.6.1.1`'s transport recurrence
holds at every rotation of 120 random profiles (used to *audit* the numerator
code, never to compute it); and `12.8.3`'s published `p = 7` staircase
`m = (4,7,9,15,23,35,1)` reproduces `γ = 6.744`, passes all seven size conditions
and fails divisibility at all seven. The `σ` convention is `σ_j = s_j + m_{j+1}`
throughout (Prop `12.6.1`, canaried in `experiments/record_defects_check.py`); the
`p = 7` reproduction is what discriminates it.

**End to end.** For every period in `{3, 5, 6, …, 26}` (23 periods) the `n` the
two-sided argument guarantees was taken, `Γ(p,n) ≤ γ(n) ≤ C` and (H0) confirmed,
Construction B run, and **all `p` rotations verified in this session's own
evaluator built from Proposition `12.6.1`** — every rotation passes `q ≤ R_r`
exactly, every instance has crash depth exactly `1`, and **every instance fails
`q | R_r` at every rotation**. Worst `min_r R_r/q` over the table is `1.258`. The
witness table extends to `p = 40` for (H1)/(H0)/`γ` (the end-to-end big-integer
work stops at `p = 26` by cost, `p = 30` on request).

Selected witnesses, showing the point of the whole exercise:

| `p` | 16 | 20 | 22 | **26** | 30 | 34 | 40 |
|---|---|---|---|---|---|---|---|
| `n` | 1588 | 10009 | 25157 | **158675** | 1001317 | 6318969 | 100175081 |
| offset in window | 1 | 0 | 13 | 5 | 4 | 7 | 9 |
| `γ(n)` | 4.220 | 3.764 | 3.923 | **4.299** | 3.850 | 4.020 | 3.789 |

At `p = 26` the record's one-sided witness (`n = 158670`, `γ = 17.058`) is
replaced by `n = 158675`, `γ = 4.299`. That single row is the exposure the brief
named, closed.

**Negative controls — all four bite.**

* **NC-1 (an arc shorter than `θ` must exhibit an empty maximal gap).** For an arc
  of length `0.9θ` the licensed 14-point sweep has maximal gap `θ > 0.9θ`, so no
  `J ≤ 13` catches it, and the failure is realised: **1,950** of the first 20,000
  starting values `N` have an entirely empty progression. Control on the control:
  the full arc, same sweep, same 20,000 starts — **0** empty. *Recorded honestly:
  the shorter arc is not beyond every `J` — lengthening the sweep to `J = 26`
  (131 integers) recovers it, because the grid refines by three distances. That
  refinement is §8's ladder, and it is why "an arc shorter than `θ` fails" must be
  stated at the licensed sweep length, not unconditionally.*
* **NC-2 (an `n` below `δ_lo` must exceed the `γ` bound).** 60 such `n` across
  `p ∈ {16,…,30}`: **0** have `γ ≤ C`; the largest `γ` seen is `17.057` — the
  `p = 26` row again.
* **NC-3 (an `n` above `δ_hi` must fail Theorem B's hypothesis).** Split, because
  two different statements were being conflated. (a) Above the **exact** threshold
  `−log₂(1 − 2^{−Γ(p,n)})`: 494 tested, **0** still satisfy (H1) — the
  `δ ↔ γ ↔ Γ` conversion is sound end to end. (b) Above the **uniform** `δ_hi`:
  of 495, exactly **1** still satisfies (H1) on the exact `Γ(p,n)` — that single
  instance is the entire price of replacing `Γ(p,n)` by its supremum. Of the 494
  that lose (H1), 452 then fail a size condition and 42 still build a passer;
  those 42 are `Γ`'s known `0.6`–`0.9` bit conservativeness (the sibling's NC-A),
  not a soundness break, since (H1) is sufficient and not necessary.
* **NC-4 (the lower cut is load-bearing).** Drop it and take the first Lemma-D
  witness in each window, `p = 16…40`: the worst `γ` is `17.057` at `p = 26`,
  three times the bound. Without the lower cut there is no bound to have.

**Brute force.** Over `n = 1…3·10⁶` the longest run of consecutive integers
failing the **two-sided** condition is **16**, against the proved bound of 65; the
one-sided longest run is **11**, reproducing Lemma D's own figure and both
delegates' independently observed worst offset. The proved bound is loose by a
factor of four, as one expects from a single-progression argument.

---

## 8. The optimal constant, and how far the method can be pushed

**(a) The optimum at the recorded sweep.** `δ_lo` may be taken anywhere strictly
below `δ_hi − θ = 0.041751570114`; larger `δ_lo` means smaller `γ`. So

| `δ_lo` | `γ ≤` | note |
|---|---|---|
| `0.0400000` | `5.192576` | the audit's instance, margin `0.00175` |
| `0.0415000` | `5.140211` | **recommended headline**, margin `0.000252` |
| `0.0417500` | `5.131671` | |
| `0.0417515…` | `5.131617…` | **infimum of the method; not attained** |

The infimum `5.1316175` is the best this sweep allows, and the margin is a
certified rational inequality, not a decimal, at every row.

**(b) Using `Γ(p,n)` exactly rather than `Γ*`.** The brief asked whether this
widens the arc at large `p`. **It does the opposite, and the sign is worth
recording:** `Γ` *increases* in `p` toward `Γ*`, so the exact `Γ` helps only at
*small* `p`.

| `p` | 16 | 20 | 24 | 30 | 60 | 200 |
|---|---|---|---|---|---|---|
| `Γ(p, n_max)` | 3.668218 | 3.680047 | 3.682443 | 3.682966 | 3.683012 | 3.683012 |
| best `γ` bound | 5.089481 | 5.123107 | 5.129982 | 5.131486 | 5.131617 | 5.131617 |
| gain over the uniform optimum | `0.042` | `0.0085` | `0.0016` | `0.0001` | `0` | `0` |

`0.042` bits at `p = 16`, nothing asymptotically, in exchange for a `p`-dependent
clause in the statement. **Not worth it.**

**(c) The refinement ladder — the real trade-off.** Lengthening the *same* step-5
sweep past `Jθ > 1` refines the grid by three distances, so its maximal gap falls
below `θ` and the arc may be shortened to match. A smaller `γ` costs a longer
window, hence a larger `p₀`:

| sweep `J` | consecutive integers | maximal gap | `γ ≤` | `p₀` |
|---|---|---|---|---|
| 13 | 66 | `0.0751874963` | `5.131617` | 16 |
| 39 | 196 | `0.0300624026` | `4.096874` | 18 |
| 52 | 261 | `0.0225625468` | `3.981125` | 19 |
| 92 | 461 | `0.0150626911` | `3.874513` | 20 |
| 132 | 661 | `0.0075628353` | `3.775737` | 21 |
| 13073 | 65366 | `0.0013908375` | `3.699587` | 31 |
| 15866 | 79331 | `0.0000682666` | `3.683820` | 31 |
| 15999 | 79996 | `0.0000629796` | `3.683758` | 32 |

So **for every `ε > 0` there is a `p₀(ε)` beyond which the family achieves
`γ ≤ Γ* + ε`** — the achieved `γ` can be driven to the demand `Γ* = 3.683012`
itself. The headline `γ ≤ 5.1403` at `p₀ = 16` and the asymptotic `γ → 3.6831` are
the two ends of one ladder, and the wiki should state the first and mention the
second.

**(d) Is a better `γ` reachable at all?** Recorded, not searched (README stopping
rules). Three facts bound the question without opening it. (i) Within this method
the floor is `Γ*`, and `Γ ≈ 0.92714κ + 2.70951` with `κ ≥ 1` forced by the scale,
so `3.6366` is the floor even in the limit `κ → 1`. (ii) `Γ` is itself
conservative by `0.6`–`0.9` bits, because Theorem B's `(C_r)` keeps one term of
`R_r` and discards `p−1` positive ones (the sibling's NC-A); sharpening `(C_r)` to
its exact form `(★)` would buy that back and is the only visible route to a
materially smaller constant. (iii) The true minimum `γ` over *all* size-passers is
a different question again — the sibling's own tables show `γ` as low as `2.91`
among first passers at small `p`, and `12.8.3` records 84 size-passers at `p = 6`
alone, so the family is not unique at a period. No search was launched.

---

## 9. Verdict, and what may now be said

**Is `γ = O(1)` proved? Yes**, with the following exact scope, and nothing wider:

> For every period `p ≥ 16` there is an integer `n ∈ [L^p, 1.05·L^p]` such that
> Construction B returns a period-`p` configuration satisfying all `p` size
> conditions `q ≤ R_r`, with crash depth `1` and with
> `3.683012 ≤ γ ≤ 5.140212`. For `3 ≤ p ≤ 15` an explicit `n` achieving the same
> bracket is exhibited. `p ∈ {2, 4}` lie outside Construction B's reach. All
> constants are absolute; none depends on `p`.

Recommendations for the main session (`cycles.md` untouched here):

1. `12.8.6.1` may now state the availability lemma **two-sidedly**: the arc
   `δ ∈ [0.0415, δ_hi]`, `δ_hi = −log₂(1 − 2^{−Γ*}) ≥ 0.116939066509`, with
   `Γ* = 1.05·L(L−1) + 1/(L−1) + 1` proved to be a strict uniform upper bound for
   `Γ(p,n)` by the negative bracket `B(p)`, and Lemma G's sharp sweep criterion
   (66 consecutive integers; 61 for the one-sided form).
2. `12.8.3`'s `γ = O(log p)` and the paper's `thm:staircase` may be **strengthened
   to `γ = O(1)`, with the explicit constant `5.1403`**, at the constructed
   family, for `p ≥ 16`, plus the finite tail. The `{2,4}` exclusion must survive
   every draft.
3. The `p ≤ 15` clause is "proved (finite check)" and the `{2,4}` clause is
   "outside the theorem"; the audit's status vocabulary (§0.2) applies unchanged
   with `γ = O(1)` moved from "pending §0.1" to "proved".
4. The recorded Lemma D and Theorem D need **no correction**: `0.116939` is a safe
   rounding and `71 ≥ 66`. What they need is a *sharper reason*, and Lemma G is
   it. If the wording is revisited, "among any 71" may become "among any 61" for
   the one-sided form.
5. `12.8.5`, the parked cycle front and all three README stopping rules are
   unaffected; this is sharper evidence that counting arguments cannot do better,
   and no evidence at all about exclusion.

---

## 10. Failures, limits and things recorded rather than smoothed over

* **My first formulation of the sweep criterion was wrong and the code caught
  it.** I used the sufficient condition "span `≥ 1 + ℓ`", concluded that the
  two-sided arc needs `J = 15` (76 integers) where the one-sided needs `J = 14`,
  and wrote a negative control asserting that `J = 14` must fail for the
  two-sided arc. The control came back `0/200000` failures, which forced the
  correct analysis: the criterion is the maximal-gap one, it is an iff, and it
  gives `J = 13` and `J = 12`. Both the "76" and the claim that the audit's 71 is
  insufficient were mine and were wrong; the audit's 71 is valid. The check that
  could have failed, failed.
* **A second control was also too strong.** "An arc shorter than `θ` can never be
  caught" is false: `J = 26` catches a `0.9θ` arc. The true statement is at the
  licensed sweep length, and the mechanism behind the exception is the ladder of
  §8(c). Recorded in the code and in §7.
* **The strictness of `Γ < Γ*` cannot be verified numerically at large `p`** — the
  gap is `~10^{-400}` at `p = 2000`, below any interval engine. It comes from
  `B(p) < 0`, which is algebra; the table only confirms the non-strict inequality
  and that the derivation's bound dominates. Stated as such in the check labels.
* **`p₀ = 16` has less headroom than it looks.** The window holds 79 consecutive
  integers against a requirement of 66. Any future tightening of `Γ*` upward — or
  any narrowing of the window below `κ ≤ 1.05` — could move `p₀`, and the finite
  tail would then have to absorb one more period. The tail already covers
  `3 ≤ p ≤ 15` explicitly, so this is a bookkeeping risk, not a mathematical one.
* **The end-to-end table stops at `p = 26` by big-integer cost**, not by
  mathematics; `p = 30` runs in 173 s and passes. Nothing in Theorem G degrades
  with `p`.
* **The finite tail's witnesses sit at `κ` up to `1.70`** (`p = 5`), outside the
  canonical window. This is legitimate — `Γ(p,n)` is evaluated exactly at that
  `n`, and (H1)/(H0)/`γ ≤ C` are all certified there — but it means the tail is
  covered by exhibition at a widened scale, not by the window statement, and the
  wiki wording should say so.
* **Not attempted:** sharpening `(C_r)` to `(★)` to recover `Γ`'s `0.6`–`0.9` bits
  (§8(d)(ii)). It is the only visible route to a materially smaller constant and
  it would not change the growth rate, which is already `O(1)`.
