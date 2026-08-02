# Findings: the exceptional tail under the two-sided space (v3 round 3, Wave 5a)

**Branch** `v3r3-review-round3` at `fa07929`. Read-only pass; this file is the only repository file written.
Scratch code: `…\scratchpad\aeh_tailbound.py` and `…\scratchpad\deriv_audit.py` (full listing of the first at
Appendix A; see §7 for the one hand-off action this creates).

---

## 0. Headline

**The bound holds. Nothing downstream is invalidated. The base case does not need to come off PROVED.**

`13.6.3`(iv)'s inequality `P(a ≥ j) ≤ 2·(0.93)^j` is **true under `B̂`**, at every `j ≥ 1`, and its existing
proof is a correct computation — it was only mistyped, because under a one-sided `B` the random variable `a`
does not exist at all (`13.6.3`(v) says so in terms). The constant does not move in the direction that would
hurt: it moves *down*. A short self-contained argument in the same style gives

```text
P_B̂(a ≥ j)  ≤  (1/3)·(5/6)^(j−1)        for every j ≥ 1, with equality at j = 1,
```

which is strictly stronger than `2·(0.93)^j` at every `j`. So every downstream use — `13.2.4`(e)'s choice of
`W`, `13.6.4`(⇒)'s exceptional mass — remains valid **as literally written**, and can optionally be sharpened.

The one substantive correction is to **`13.2`'s relocation sentence**, which is accurate about the reconstruction
and about `π_{k,D}` but wrong about where the estimate is used: it is used in `13.2.4`(e) as well as `13.6.4`,
and its qualitative half (`a < ∞` a.s.) is what makes the infinite-past statement true in the first place, so
it is not "relocated out" of `13.2` at all.

---

## 1. Verdicts

### (1) Does `13.6.3`(iv)'s argument transfer to `B̂`? — **It transfers; strictly, it only ever made sense there.**

The proof "condition on the `i` letters nearest `y_n`; prepending one more letter …" is not a construction of a
*finite* past. It is exactly the construction of the past-limit `y_3` of itinerary.md `14.15.3.3`: `B_{i+1} = B_i
+ A_i β'` with `v_3(A_i) = M_i` strictly increasing is `14.15.3.3`'s own Cauchy recursion, and the digit at level
`M_i` being *final* is precisely why `B_i → y_3`. The argument is therefore the two-sided one already; the words
"Under `B`" and the symbol `P_B` are the error, not the mathematics.

They are a real error, not a typo of taste. `13.6.3`(v) states flatly that `a_{n+1} = v_3(y_n + 1)` "is not a
function on odd `Z_2` at all", so `P_B(a ≥ j)` under a one-sided future measure is ill-typed. Under `B̂` it is
well-typed and the statement is the one the page needs.

**And there is a sharper fact that closes the finite-past/infinite-past question outright.** For every `W ≥ 1`,

```text
{a ≥ W}  =  {B_W ≡ −1  (mod 3^W)},
```

an event on the **`W` letters immediately preceding the visit** — because `v_3(y_3 − B_W) ≥ M_W = Σ_{i=1}^{W} m_{n−i}
≥ W` (each `m_i ≥ 1`), so `y_3 ≡ B_W (mod 3^W)`. Consequently the `B̂`-probability of `{a ≥ W}` **equals** the
`B^{⊗W}`-probability of the corresponding finite-window letter event. The finite-past reconstruction of
`13.2.4`(e) and `13.6.4`(⇒) therefore fails on an event of *exactly* the two-sided mass, at the same `W` — no
loss, no separate constant, no "finite-past version of the bound" to prove. Measured directly (§6, rows
`W = 2,3,4,6,8`): the observed failure rate of the finite-past reconstruction on real integer orbits matches
`P_B̂(a ≥ W)` at every tested `W`.

### (2) Is `0.93` still correct? — **Yes, but it is not the argument's own rate and not the truth.** Recommend replacing it.

Three numbers, kept apart:

| | value | status |
|---|---|---|
| the printed constant | `0.93` | true, but slack in two independent ways |
| the renewal argument's exact rate | `5/6 = 0.8333…` | the root of `2ρ − 1 = 2/3`; provable, and proved below |
| the measured decay of `P(a ≥ j)` | `≈ 3^(−j)` | `P(a≥j)·3^j ∈ [0.116, 0.148]` for `6 ≤ j ≤ 11` |

The `0.93` is what the write-up's crude split `E[(2/3)^{I(j)}] ≤ (2/3)^t + (1+√2)^t 2^{−j/2}` at `t = ⌊j/5⌋`
gives; `(2/3)^{1/5} = 0.9221…` is the binding term. I checked that split holds at every `j ≤ 4000` (worst
`lhs/rhs = 0.918`), so the printed inequality is sound — but the same renewal has exact exponential rate `5/6`,
and a direct argument reaches `5/6` with a clean constant. **Recommended replacement:**

```text
P_B̂(a ≥ j)  ≤  (1/3)(5/6)^(j−1)        j ≥ 1,   equality at j = 1.
```

This is tight at `j = 1` (`P(a ≥ 1) = 1/3` exactly), strictly below `2·(0.93)^j` at every `j`, and derived from
the same recursion `13.6.5` already computes `ν_j` by — so it costs the page no new machinery.

### (3) Is `13.2`'s relocation sentence accurate? — **Two of its three clauses are; the third is wrong and should be replaced.**

The sentence (aeh.md L30):

> *…with an infinite past the reconstruction is exact almost surely, so `π_{k,D}` carries no exceptional-set caveat
> and the `2·(0.93)^W` estimate of `13.6.3`(iv) survives only where it belongs, in the finite-past bound of `13.6.4`.*

* **"with an infinite past the reconstruction is exact almost surely" — correct.** The only obstruction is
  `a = ∞`, i.e. `y_3 = −1` in `Z_3`; `P(a ≥ j) ≤ (1/3)(5/6)^(j−1) → 0` gives `P(a = ∞) = 0`. Given `a < ∞`, the
  infinite past determines `a` exactly, and with it `ω_{n+1} mod 2^{k+2} = q_n·3^{−a_{n+1}}`. Verified: the
  reconstruction had `0` state mismatches over `19,760` visits at every past-window tested.
* **"`π_{k,D}` carries no exceptional-set caveat" — correct.** The reconstruction map is defined off a
  `B̂`-null set, so the pushforward is a genuine probability measure on the finite alphabet, with no conditioning
  and no defect mass.
* **"the estimate … survives only where it belongs, in the finite-past bound of `13.6.4`" — wrong twice.**
  (a) It is consumed in **`13.2.4`(e)** as well, which is the lemma the round marked PROVED — naming only
  `13.6.4` understates the dependency and is exactly the sentence that let this gap sit. (b) The estimate is not
  banished from the infinite-past setting: `13.6.3`(iii) itself says "`a < ∞` almost surely **by (iv)**", so
  (iv)'s *qualitative* half is what makes the previous two clauses true. What is confined to the finite-past
  uses is the *quantitative* rate, not the lemma.

  There is also a fourth, quieter inaccuracy: the sentence implies the finite-past bound is a weaker or separate
  thing. It is not — §1(1) above shows the two masses are equal.

### (4) Are `13.2.4`(e) and `13.6.4`(⇒) correct as written? — **Both correct. Neither needs amending; both may be sharpened.**

* **`13.2.4`(e).** `2L(0.93)^W` is a valid bound on the exceptional mass: the `L`-block fails only if some one
  of its `L` visits has `a ≥ W`, mass `≤ L·P(a ≥ W) ≤ L·2(0.93)^W`. The `B`-mass wording is *right* here and
  should not be changed to `B̂`: in (e) the letters really are a finite word approximately `B^{⊗n}`-distributed
  by (a), and by §1(1) the finite-window mass of `{a ≥ W}` equals its `B̂`-mass. The side condition `W ≥ D` is
  needed and is stated: it is what lets `13.6.3`(iii) return the capped depth **with no exception** on
  `{a ≥ W}` (there `d = m + a ≥ W ≥ D`, so `min(d,D) = D`). Verified with `D = 2 ≤ W` at every tested `W`:
  `0` capped-depth failures.
* **`13.6.4`(⇒).** Same structure, same verdict. The exceptional event and the reconstruction's level sets are
  finite-window letter events, so bulk-genericity assigns them their `B`-masses; letting `W → ∞` gives the
  equality. Correct as written.

Two harmless index nits, recorded so they are not rediscovered as bugs (neither changes a conclusion; both are
optional):

* `13.2.4`(e)'s `P = W + L + ⌈(k+1)/2⌉ + 1`. Under `13.6.3`(iii)'s convention (the window at visit `v` reads
  letters `v−1−W … v−1+⌈(k+1)/2⌉`), an `L`-block spans `W + L + ⌈(k+1)/2⌉` consecutive letters. `P` over-counts
  by one, which is the safe direction (`P` only enters through `Λ` and the union bound, both monotone in `P`).
* `13.6.4`(⇒)'s window `n−W..n+L+⌈(k+1)/2⌉` starts one letter later than the visit-`n` window needs, so the
  past depth it actually supplies is `W−1`. Immaterial: `W` is universally quantified there and the conclusion
  is a `W → ∞` limit.

---

## 2. The setting, stated once

Under `B̂ = ⊗_{i∈Z}(geom(1/2) × geom(1/2))` the letters `(m_i, r_i)` are iid with `P(m,r) = 2^{−(m+r)}`
(`13.6.1`). At visit `n` the door's `3`-adic value is the past-limit `y_3` of the left-infinite word
(itinerary.md `14.15.3.3`), and

```text
a  :=  a_{n+1}  =  v_3(y_n + 1)  =  v_3(y_3 + 1),        d_{n+1} = m_n + a_{n+1}.
```

`13.6.5` computes the law of `a` exactly at each precision as `ν_j`, the pushforward of `B^{⊗j}` under the offset
formula, and identifies it as Tao's Syracuse variable in this normalisation. Everything below is a statement
about that same object.

---

## 3. The derivation

### 3.1 The event is a finite-letter event

By itinerary.md `14.15.3.3`, `v_3(B_{i+1} − B_i) = M_i` with `M_i = Σ_{k≤i} m_{n−k}` strictly increasing, so
`v_3(y_3 − B_W) ≥ M_W ≥ W` (each `m ≥ 1`). Hence `y_3 ≡ B_W (mod 3^W)` and

```text
{a ≥ W}  =  {y_3 ≡ −1 (mod 3^W)}  =  {B_W ≡ −1 (mod 3^W)},
```

a function of letters `n−W, …, n−1` — the same `W` letters `13.6.3`(iii) uses for the synchronization. Its
`B̂`-mass equals its `B^{⊗W}`-mass. (This is the one clause the round was missing; it is what makes the
finite-past uses legitimate at the *same* constant, rather than needing a separate finite-past bound.)

### 3.2 The stationary recursion

Add `1` to reverse.md `14.14.4.1` on the stratum `(m,r)`:

```text
G(y) + 1  =  3^m 2^{−(m+r)}(y + 1)  +  (1 − 2^{−r}),
```

since `(3^m − 2^m)2^{−(m+r)} + 1 − 3^m 2^{−(m+r)} = 1 − 2^{−r}`. The composition recursion of `14.15.3.3`
(`B_{n+1}^{(0)} = β_{−1} + α_{−1}B_n^{(−1)}`) passes to the limit, so writing `V := y_3 + 1 ∈ Z_3`,

```text
V  =  (1 − 2^{−r})  +  3^m 2^{−(m+r)} V',
```

with `(m,r)` the preceding door's letter, `V'` that door's own `y_3 + 1`; under `B̂`, `V' ⊥ (m,r)` and `V' =_d V`.
Two immediate sanity readings, both confirmed: mod `3`, `V ≡ 1 − (−1)^r`, so `a ≥ 1` iff `r` is even, of
probability `1/3`; and `v_3(1 − 2^{−r}) = v_3(2^r − 1) = 1 + v_3(r/2)` for even `r`, which is where `2/63` comes
from at `j = 2`.

### 3.3 A uniform bound on the atoms

Put `Q_t := max_{z} P(V ≡ z (mod 3^t))`, with `Q_t := 1` for `t ≤ 0`. Fix a letter `(m,r)`. The congruence
`3^m 2^{−(m+r)}V' ≡ z − 1 + 2^{−r} (mod 3^t)` pins `V'` modulo `3^{t−m}` when it is solvable at all, and it is
solvable only if

```text
2^{−r}  ≡  1 − z   (mod 3^μ),        μ := min(m, t) ≥ 1.
```

`2` is a primitive root modulo every `3^μ`, so this is one residue class of `r` modulo `ord(2 mod 3^μ) = 2·3^{μ−1}
≥ 2` (or none). A single class `{r ≥ 1 : r ≡ c mod P}`, `1 ≤ c ≤ P`, carries `2^{−r}`-mass `2^{−c}/(1 − 2^{−P})
≤ 2^{−1}/(1 − 2^{−2}) = 2/3`. Therefore, uniformly in `z`,

```text
Q_t  ≤  (2/3) Σ_{m≥1} 2^{−m} Q_{t−m},
```

and by induction `Q_t ≤ (5/6)^t`: with `Q_s ≤ (5/6)^s` for `s < t`, the right side equals
`(2/3)[(3/2)(5/6)^t(1 − (3/5)^{t−1}) + 2^{−(t−1)}] = (5/6)^t − (1/3)2^{−t}`. (`5/6` is the root of `2ρ − 1 = 2/3`,
which is the renewal's own exponential rate — the same rate the printed `0.93` is a lossy relaxation of.)

### 3.4 The tail

Specialise to `z = 0`. The solvability condition becomes `2^{−r} ≡ 1 (mod 3^μ)`, i.e. `r ≡ 0 (mod 2·3^{μ−1})`, of
mass

```text
ρ_μ  :=  1/(2^{2·3^{μ−1}} − 1)  :   ρ_1 = 1/3,  ρ_2 = 1/63,  ρ_3 = 1/262143,  ρ_4 = 1/(2^54 − 1).
```

Hence

```text
P(a ≥ j)  ≤  Σ_{m=1}^{j−1} 2^{−m} ρ_m Q_{j−m}  +  2^{−(j−1)} ρ_j.
```

At `j = 1` the sum is empty and the right side is `ρ_1 = 1/3` — exactly `P(a ≥ 1)`, so the chain is tight at the
base. For `j ≥ 2`, using `Q_t ≤ (5/6)^t`, `ρ_m ≤ ρ_2` for `m ≥ 2`, `Σ_{m≥2}(3/5)^m = 9/10` and
`2^{−j} ≤ (9/25)(5/6)^j`:

```text
P(a ≥ j)  ≤  [ 1/5 + (9/10)ρ_2 + (18/25)ρ_2 ] (5/6)^j
          =  0.225714… · (5/6)^j   <   (2/5)(5/6)^j   =   (1/3)(5/6)^{j−1}.
```

Audited in exact rationals: the induction step holds at every `t ≤ 59` with slack exactly `(1/3)2^{−t}`, and the
tail chain holds at every `j ≤ 59` (evaluated ratio to target `1.000` at `j = 1`, `0.514` beyond).

### 3.5 Why this rather than "cite the exact law"

The brief asks whether the honest move is to cite `13.6.5`'s exact law instead of porting an estimate. **It is
not sufficient, and here is the precise reason.** `13.2.4`(e) and `13.6.4`(⇒) do not need the tail at any one
`j`; they *choose* `W` as a function of `ε` and need a bound valid at **every** `W`. `13.6.5` gives `ν_j` as "a
finite rational computation" per `j` — closed values at `j ≤ 3` and a recipe above that — with no formula in
`j` and no monotone envelope. A uniform geometric bound is exactly the thing `ν_j` does not supply.

So the honest move is the middle one, and it is what §3 does: **derive the geometric bound from the same
recursion `ν_j` is computed by**, so the page carries one object rather than two, and state the exact values
alongside as the reference point. The bound is then tight at `j = 1` and correct in rate to within `(5/6)` vs
`(1/3)` — with the residual gap named honestly in §7.

---

## 4. Exact drop-in Markdown

Four sites, all in `aeh.md`; no other tracked file carries the constant (checked by `git grep` over
`*.md`/`*.py`/`*.tex`, excluding `briefs/`, `sources/`, `archive/`; the paper does not carry it). No anchor is
renumbered.

### 4.1 `aeh.md` L178 — `13.6.3`(iv), **required** (this is the mistyped statement)

Replace the whole paragraph:

```markdown
**(iv) The exceptional tail.** `P_B̂(a ≥ j) ≤ (1/3)·(5/6)^{j−1}` for every `j ≥ 1`, with equality at `j = 1`; the exact values are far smaller (`1/3, 2/63, 1598/262143 ≈ 0.0061, …`; `13.6.5`), the computed decay being `≈ 3^{−j}`. The event is a **finite-letter** one: `{a ≥ j} = {B_j ≡ −1 (mod 3^j)}`, a function of the `j` letters preceding the visit, so its `B̂`-mass is exactly its `B^{⊗j}`-mass — which is the form the finite-past bounds of `13.2.4`(e) and `13.6.4` consume, at the same constant and with nothing lost. **Proof.** *The event.* By `14.15.3.3`, `v_3(y_3 − B_j) ≥ M_j = Σ_{i=1}^{j} m_{n−i} ≥ j`, so `y_3 ≡ B_j (mod 3^j)` and `{a ≥ j}` is read off the same `j` letters `(iii)` uses. *The recursion.* Adding `1` to `14.14.4.1` gives `G(y) + 1 = 3^m 2^{−(m+r)}(y+1) + (1 − 2^{−r})` on the stratum `(m,r)`; in the limit of `14.15.3.3`'s composition recursion, `V := y_3 + 1` satisfies `V = (1 − 2^{−r}) + 3^m 2^{−(m+r)} V'` with `(m,r)` the preceding letter, `V'` its own past-limit, `V' ⊥ (m,r)` and `V' =_d V`. *The atoms.* Put `Q_t := max_z P(V ≡ z (mod 3^t))`, `Q_t := 1` for `t ≤ 0`. Given a letter, `3^m 2^{−(m+r)}V' ≡ z − 1 + 2^{−r} (mod 3^t)` pins `V'` mod `3^{t−m}` when solvable, and is solvable only if `2^{−r} ≡ 1 − z (mod 3^μ)`, `μ = min(m,t)` — one class of `r` mod `ord(2 mod 3^μ) = 2·3^{μ−1} ≥ 2` (`2` is a primitive root mod every `3^μ`), of mass `≤ 2^{−1}/(1 − 2^{−2}) = 2/3`. So `Q_t ≤ (2/3)Σ_{m≥1} 2^{−m}Q_{t−m}`, whose right side under `Q_s ≤ (5/6)^s` evaluates to `(5/6)^t − (1/3)2^{−t}`: by induction `Q_t ≤ (5/6)^t`, `5/6` being the root of `2ρ − 1 = 2/3`. *The tail.* At `z = 0` solvability reads `r ≡ 0 (mod 2·3^{μ−1})`, of mass `ρ_μ = 1/(2^{2·3^{μ−1}} − 1)` (`1/3`, `1/63`, `1/262143`, …), so `P(a ≥ j) ≤ Σ_{m=1}^{j−1} 2^{−m}ρ_m Q_{j−m} + 2^{−(j−1)}ρ_j`. At `j = 1` this is `ρ_1 = 1/3` exactly; for `j ≥ 2`, `ρ_m ≤ ρ_2` (`m ≥ 2`) and `Σ_{m≥2}(3/5)^m = 9/10` give `≤ [1/5 + (9/10)ρ_2 + (18/25)ρ_2](5/6)^j < (2/5)(5/6)^j`. ∎
```

*(No "was/now" prose, per AGENTS.md: the paragraph states the current answer only. The old renewal estimate
`E[(2/3)^{I(j)}] ≤ 2(0.93)^j` is true under `B̂` too and weaker at every `j`, so nothing that cited it is
invalidated — that observation belongs in this findings file, not on the page.)*

### 4.2 `aeh.md` L30 — `13.2`'s relocation sentence, **required**

Replace the clause running from `with an infinite past` to the end of the sentence:

```markdown
with an infinite past the reconstruction is exact almost surely — `a < ∞` almost surely, by `13.6.3`(iv) — so `π_{k,D}` carries no exceptional-set caveat, and (iv)'s *quantitative* tail `(1/3)(5/6)^(W−1)` is consumed only where a **finite** past is read: the past-window bounds of `13.2.4`(e) and of `13.6.4`'s (⇒) direction. Nothing is weakened there. `{a ≥ W}` is an event on the `W` letters before the visit (`13.6.3`(iii)–(iv)), so its finite-window `B`-mass is exactly its `B̂`-mass.
```

### 4.3 `aeh.md` L101 — `13.2.4`(e), **optional** (the text is already correct)

If the round wants one constant on the page rather than two, replace exactly

```markdown
Choose the letter past-window `W ≥ D` with `2L(0.93)^W < ε'/8`,
```

by

```markdown
Choose the letter past-window `W ≥ D` with `(L/3)(5/6)^(W−1) < ε'/8`,
```

and leave the rest of (e) untouched — in particular leave `off an event of `B`-mass `< ε'/8``, which is right
(§1(4)).

### 4.4 `aeh.md` L199 — `13.6.4`'s proof, (⇒) direction, **optional** (the text is already correct)

Two substitutions in the (⇒) sentence:

```markdown
off an exceptional event of `B`-mass `≤ 2L(0.93)^W`      ->   off an exceptional event of `B`-mass `≤ (L/3)(5/6)^(W−1)`
to within `2L(0.93)^W + ε` of the `13.6.3`(v) value      ->   to within `(L/3)(5/6)^(W−1) + ε` of the `13.6.3`(v) value
```

**4.3 and 4.4 must be landed together or not at all** — landing 4.1 alone leaves two live references to a
constant the lemma no longer prints, which is exactly the kind of drift the wiki's one-fact-one-place rule
exists to prevent. Landing neither is also consistent (both bounds are true); landing only one is not.

---

## 5. Verification record, in the page's form

To be placed as the `**Verified**` line for `13.6.3` (the section currently carries its verification under
`13.6.2` at L168 and `13.6.5` at L219; this is a third, for the dictionary lemma). **It names a script that does
not yet exist in the repository — see §7, item H1.**

```markdown
**Verified** — `experiments/aeh_tailbound.py`, fresh code (imports nothing from `aeh_symbolic.py`, `aeh_calibration.py`, `aeh_basecase.py` or `itinerary_coding.py`), 2026-08-02. The law of `y_3 + 1` modulo `3^j` computed from the prepend recursion in exact rational arithmetic at `j ≤ 5` — `P(a ≥ 1) = 1/3`, `P(a = 1) = 19/63`, `P(a ≥ 2) = 2/63`, `P(a ≥ 3) = 1598/262143 = 0.00609593…`, `P(a ≥ 4) = 32767500859970/(2^54 − 1) = 0.00181897…` — and in floating point to `j = 11`, agreeing with the exact values to `7.8 × 10^{−16}`: the bound `(1/3)(5/6)^{j−1}` holds at every `j`, the measured decay being `P(a ≥ j)·3^j ∈ [0.116, 0.148]` for `6 ≤ j ≤ 11`. The atom bound `Q_t ≤ (5/6)^t` holds at every `t ≤ 11` (`Q_11 = 7.13 × 10^{−4}` against `(5/6)^11 = 0.1346`), and its induction step in exact rationals to `t = 59` with slack exactly `(1/3)2^{−t}`. An independent Monte Carlo on the composed-affine offset recursion (`14.14.8.2`) — `400,000` words at `j ≤ 6` (seed `51001`) and at `j ≤ 8` (seed `51002`) — matches the computed tail at worst `z = 1.62`. On real integer orbits (`260` orbits, `220`-bit starts, `90` blocks, first `8` discarded, `19,760` tallied visits, seed `52001`) the absorption law matches the `B̂` tail at worst `z = 1.61` over `j ≤ 6`, and the finite-past reconstruction of `(ω mod 2^5, min(d, 2))` from letters alone at past-windows `W = 2, 3, 4, 6, 8` gives `0` synchronization failures, `0` state mismatches and `0` capped-depth failures, with measured exceptional rates `3.14×10^{−2}, 5.72×10^{−3}, 1.77×10^{−3}, 1.01×10^{−4}, 0` against `P_B̂(a ≥ W) = 3.17×10^{−2}, 6.10×10^{−3}, 1.82×10^{−3}, 1.66×10^{−4}, 1.89×10^{−5}`.
```

---

## 6. What was actually run

All fresh; nothing imported from `experiments/`. Two scripts, both in the scratchpad (Appendix A lists the first
in full).

**`aeh_tailbound.py`** — all checks pass, `0` failures.

| check | result |
|---|---|
| exact `P(a ≥ j)`, `j ≤ 5`, rationals, backward recursion | `1/3`, `2/63`, `1598/262143`, `32767500859970/(2^54−1)`, `3607…/5846…`; `P(a=1) = 19/63`, `P(a=0) = 2/3` — matches `13.6.5` in every printed digit |
| float tail to `j = 11` vs exact | max `\|diff\|` `7.8×10^{−16}` over `j ≤ 5` |
| `P(a ≥ j) ≤ (1/3)(5/6)^{j−1}` | holds at every `j ≤ 11` |
| `P(a ≥ j) ≤ 2(0.93)^j` (the printed bound) | holds at every `j ≤ 11` |
| `P(a ≥ j)·3^j`, `j = 6…11` | `0.121, 0.116, 0.124, 0.148, 0.126, 0.148` |
| `Q_t ≤ (5/6)^t` | holds at every `t ≤ 11`; ratio falls `0.80 → 0.0053` |
| MC on `14.14.8.2` offsets, `400,000` words, seeds `51001`/`51002` | worst `z = 1.62` / `1.48` |
| orbit absorption law, `19,760` visits, seed `52001` | worst `z = 1.61` over `j ≤ 6` |
| finite-past reconstruction, `W = 2,3,4,6,8`, `k = 3`, `D = 2` | `0` sync, `0` state, `0` capped failures; exceptional rates match `P_B̂(a ≥ W)` |

**`deriv_audit.py`** — exact rationals.

| check | result |
|---|---|
| `Q_t` induction step `≤ (5/6)^t` | holds `t ≤ 59`, slack identically `(1/3)2^{−t}` |
| tail chain `≤ (1/3)(5/6)^{j−1}` | holds `j ≤ 59`; ratio `1.000` at `j = 1`, `0.514` beyond |
| the printed chain `(2/3)^{⌊j/5⌋} + (1+√2)^{⌊j/5⌋}2^{−j/2} ≤ 2(0.93)^j` | holds `j ≤ 4000`, worst `lhs/rhs = 0.918` |
| `E[2^{m/2}] = 1 + √2` | `2.4142135624` both sides |

---

## 7. What I could not settle, and the one hand-off action

**H1 (action, not a finding).** The verification line in §5 names `experiments/aeh_tailbound.py`, which is **not
in the repository** — the brief forbade me from writing anywhere but this file. The fix delegate must copy
Appendix A to `experiments/aeh_tailbound.py` and re-run it before landing §5's line; the two must land in the
same commit. If the round prefers not to add a script, §5's line must be reworded to name no file, which would
put `13.6.3` out of compliance with AGENTS.md's proved-claim rule — I recommend landing the script.

**U1. The true rate.** The proved rate is `5/6`. The measured rate is `≈ 1/3` (`P(a ≥ j)·3^j` oscillates in
`[0.116, 0.148]` out to `j = 11` with no drift). Closing that gap means proving that the Syracuse law's atoms at
precision `3^t` are `O(3^{−t})` up to a subexponential factor — i.e. an equidistribution/Fourier input on
`Syrac(Z/3^t Z)` of the kind Tao proves, not an elementary consequence of the recursion. **Not attempted**, and
not needed: `5/6` is comfortably enough for every use on the page. Recording it so nobody mistakes `5/6` for the
truth.

**U2. `{a = ∞}`.** Whether `y_3 = −1` is attained by any left-infinite word is not settled; it is `B̂`-null
either way, which is all `13.2` and `13.6.3` need.

**U3. `13.2.4`(e)'s remaining bookkeeping.** I verified the exceptional-mass clause, the `W ≥ D` side condition,
and the capped-depth-with-no-exception clause. I did **not** re-derive `ε' = 2ε/|A_{k,D}|^L`, the `Λ` truncation
`P·2^(1−Λ) < ε'/8`, or the union bound over `≤ |A_{k,D}|^L·Λ^(2P)` events — that is the verify delegate's open
item 7 and remains open exactly as it was.

**U4. The composite five-coordinate reconstruction.** My orbit check reconstructs `(ω mod 2^{k+2}, min(d,D))`,
the same two coordinates `aeh_symbolic.check_two_sided_reconstruction` does — not the full labelled `W_{k,D}`
with `min(s,D), min(σ,D), min(a_+,D)`. That is Delegate A's open question 4 and this pass does not close it. It
does not touch the tail bound: the exceptional event is the same `{a ≥ W}` for any coordinate set.

**U5. The index nits of §1(4).** I judged both harmless and did not write drop-ins for them, to keep the fix
delegate's diff minimal. If the author wants them fixed, `13.6.4`(⇒)'s window should read
`n−1−W..n+L−2+⌈(k+1)/2⌉` and `13.2.4`(e)'s `P` should read `W + L + ⌈(k+1)/2⌉` — but both edits are no-ops for
the conclusions and I do not recommend spending the churn.

---

## Appendix A. `experiments/aeh_tailbound.py` (land verbatim; §7 H1)

```python
"""Verification for aeh.md 13.6.3(iv): the exceptional tail P(a >= j) under B-hat.

Supports: aeh.md 13.6.3(iii)-(iv), 13.6.5, 13.2.4(e), 13.6.4.
Fresh code -- imports nothing from aeh_symbolic.py, aeh_calibration.py,
aeh_basecase.py, aeh_anomaly.py or itinerary_coding.py.  Everything is
re-derived from the seam formulas as printed in reverse.md 14.14.4.1 /
14.14.8.2 and itinerary.md 14.15.3.3.

Objects
-------
letter      (m, r), m = v2(y+1), r = v2(3^m q - 1), q = (y+1)/2^m; P = 2^-(m+r)
door map    G(y) = (3^m (y+1)/2^m - 1)/2^r = 3^m 2^-(m+r) y + (3^m - 2^m) 2^-(m+r)
past limit  y3 = lim_n B_n, B_n the composed affine offset of the last n letters
absorption  a = v3(y3 + 1)

The law is computed from the *backward* (prepend) form, which is independent of
the forward kernel used in aeh_symbolic.nu_exact:

    W := y3 + 1     satisfies     W = (1 - 2^-r) + 3^m 2^-(m+r) W' ,

with (m, r) the letter of the preceding door and W' that door's own y3 + 1,
independent of (m, r) under B-hat and equal to W in law by stationarity.

Checks
------
 1. exact rational law of W mod 3^J, J <= 5     -> P(a >= j) against 13.6.5
 2. float law of W mod 3^J, J = 11              -> tail table against both bounds
 3. max atom Q_t = max_z P(W = z mod 3^t)       -> against Q_t <= (5/6)^t
 4. Monte Carlo on the composed-affine offsets  -> independent code path
 5. real integer orbits                         -> P(v3(y_n + 1) >= j) along orbits
 6. finite-past reconstruction of the capped window at several past-windows W
"""

import random
from collections import defaultdict
from fractions import Fraction

import numpy as np

FAILS = []


def check(name, ok, detail=""):
    if not ok:
        FAILS.append(name)
    print(f"  [{'ok  ' if ok else 'FAIL'}] {name}" + (f"   ({detail})" if detail else ""))


# ---- elementary valuations, the stratum and the door map --------------------

def v2(n):
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


def v3(n):
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return k


def stratum(y):
    m = v2(y + 1)
    q = (y + 1) >> m
    return m, v2(3 ** m * q - 1)


def G(y):
    m = v2(y + 1)
    q = (y + 1) >> m
    z = 3 ** m * q - 1
    return z >> v2(z)


def state_of_door(y):
    """(omega, d) with y + 1 = 2^m 3^a omega and d = m + a  (reverse.md 14.14.7)."""
    m = v2(y + 1)
    rest = (y + 1) >> m
    a = v3(rest)
    return rest // 3 ** a, m + a


# ---- 1. exact law of W = y3 + 1 mod 3^J ------------------------------------

def mu_exact(J):
    """Exact law of W mod 3^J, {residue: Fraction}.

    r is lumped by residue class mod ord(2 mod 3^J) = 2*3^(J-1) with the exact
    geometric mass 2^-c/(1 - 2^-P) of {r >= 1 : r == c mod P}; m is enumerated
    1..J-1 with m >= J lumped (3^m == 0 mod 3^J there).  After J applications of
    the kernel the answer is independent of the start, the accumulated
    multiplier having 3-adic valuation sum(m_i) >= J.
    """
    mod = 3 ** J
    P = 2 * 3 ** (J - 1)
    inv2 = pow(2, -1, mod)
    wr = {c: Fraction(1, 2 ** c) / (1 - Fraction(1, 2 ** P)) for c in range(1, P + 1)}
    i2 = [1] * (P + 1)
    for c in range(1, P + 1):
        i2[c] = (i2[c - 1] * inv2) % mod

    dist = {0: Fraction(1)}
    for _ in range(J):
        nxt = defaultdict(Fraction)
        for m in range(1, J):
            sub = 3 ** (J - m)
            fold = defaultdict(Fraction)
            for u, p in dist.items():
                fold[u % sub] += p
            pm, p3, invm = Fraction(1, 2 ** m), 3 ** m, pow(inv2, m, mod)
            for c, wc in wr.items():
                B = (1 - i2[c]) % mod
                unit = (invm * i2[c]) % sub
                w = pm * wc
                for u, p in fold.items():
                    nxt[(B + p3 * ((unit * u) % sub)) % mod] += p * w
        pm = Fraction(1, 2 ** (J - 1))                       # P(m >= J)
        for c, wc in wr.items():
            nxt[(1 - i2[c]) % mod] += pm * wc
        dist = dict(nxt)
    assert sum(dist.values()) == 1
    return dist


def mu_float(J, RCAP=90):
    """The same law in floating point, r truncated at RCAP (tail mass < 2^-RCAP)."""
    mod = 3 ** J
    inv2 = pow(2, -1, mod)
    i2 = [1] * (RCAP + 1)
    for c in range(1, RCAP + 1):
        i2[c] = (i2[c - 1] * inv2) % mod

    dist = np.zeros(mod)
    dist[0] = 1.0
    for _ in range(J):
        nxt = np.zeros(mod)
        for m in range(1, J):
            sub = 3 ** (J - m)
            fold = dist.reshape(-1, sub).sum(axis=0)          # u -> u % sub
            idx = np.arange(sub)
            pm, p3, invm = 2.0 ** -m, 3 ** m, pow(inv2, m, mod)
            for c in range(1, RCAP + 1):
                B = (1 - i2[c]) % mod
                unit = (invm * i2[c]) % sub
                np.add.at(nxt, (B + p3 * ((unit * idx) % sub)) % mod,
                          fold * (pm * 2.0 ** -c))
        pm = 2.0 ** -(J - 1)
        for c in range(1, RCAP + 1):
            nxt[(1 - i2[c]) % mod] += pm * 2.0 ** -c
        dist = nxt
    return dist


# ---- 4. Monte Carlo on the composed-affine offset recursion ----------------

def mc_tail(J, N, seed):
    """Draw J iid letters, build the offset by 14.14.8.2, read a = v3(B_J + 1)."""
    rng = random.Random(seed)
    mod = 3 ** J
    cnt = [0] * (J + 1)

    def geo():
        k = 1
        while rng.random() < 0.5:
            k += 1
        return k

    for _ in range(N):
        A, B = 1, 0
        for _ in range(J):
            m, r = geo(), geo()
            inv = pow(pow(2, m + r, mod), -1, mod)
            al = (pow(3, m, mod) * inv) % mod
            be = ((pow(3, m, mod) - pow(2, m, mod)) * inv) % mod
            A, B = (al * A) % mod, (al * B + be) % mod
        w = (B + 1) % mod
        a = J if w == 0 else v3(w)
        for j in range(min(a, J) + 1):
            cnt[j] += 1
    return [c / N for c in cnt]


# ---- 5/6. real orbits: the absorption law and the finite-past reconstruction

def offset_from_letters(letters, mod):
    """B_n mod `mod` for `letters` in forward order (14.14.8.2)."""
    A, B = 1, 0
    for (m, r) in letters:
        inv = pow(pow(2, m + r, mod), -1, mod)
        al = (pow(3, m, mod) * inv) % mod
        be = ((pow(3, m, mod) - pow(2, m, mod)) * inv) % mod
        A, B = (al * A) % mod, (al * B + be) % mod
    return B


def orbit_run(seed, NORB, L, BITS, Ws, k, D):
    rng = random.Random(seed)
    tail = defaultdict(int)
    nvis = 0
    stat = {W: dict(n=0, exc=0, bad_sync=0, bad_state=0, bad_capped=0) for W in Ws}
    Wmax = max(Ws)
    for _ in range(NORB):
        y = rng.randrange(1 << (BITS - 1), 1 << BITS) | 1
        while y % 3 == 0:
            y = rng.randrange(1 << (BITS - 1), 1 << BITS) | 1
        doors = [y]
        for _ in range(L):
            doors.append(G(doors[-1]))
        letters = [stratum(t) for t in doors]
        for n in range(Wmax, L - 6):
            a = v3(doors[n] + 1)
            nvis += 1
            for j in range(min(a, 12) + 1):
                tail[j] += 1
        for W in Ws:
            mod3 = 3 ** W
            st = stat[W]
            for n in range(Wmax, L - 6):
                st["n"] += 1
                B = offset_from_letters(letters[n - W:n], mod3)
                if doors[n] % mod3 != B % mod3:
                    st["bad_sync"] += 1
                    continue
                w = (B + 1) % mod3
                a_rec = W if w == 0 else v3(w)
                true_om, true_d = state_of_door(doors[n])
                true_state = (true_om % (1 << (k + 2)), min(true_d, D))
                if a_rec >= W:
                    st["exc"] += 1
                    if min(true_d, D) != D:        # W >= D forces the cap to saturate
                        st["bad_capped"] += 1
                    continue
                m_n = letters[n][0]
                mk = 1 << (k + 2)
                q = ((doors[n] + 1) >> m_n) % mk
                om_rec = (q * pow(pow(3, a_rec, mk), -1, mk)) % mk
                if (om_rec, min(m_n + a_rec, D)) != true_state:
                    st["bad_state"] += 1
    return tail, nvis, stat


# ---------------------------------------------------------------------------

def main():
    print("== 1. exact law of W = y3 + 1 mod 3^J (backward recursion, rationals) ==")
    d5 = mu_exact(5)
    t5 = [sum(p for u, p in d5.items() if u % 3 ** j == 0) for j in range(6)]
    for j in range(1, 6):
        print(f"    P(a >= {j}) = {t5[j]} = {float(t5[j]):.8f}")
    check("P(a >= 1) = 1/3 exactly (13.6.5)", t5[1] == Fraction(1, 3))
    check("P(a >= 2) = 2/63 exactly (13.6.5)", t5[2] == Fraction(2, 63))
    check("P(a = 1) = 19/63 exactly (13.6.5)", t5[1] - t5[2] == Fraction(19, 63))
    check("P(a = 0) = 2/3 exactly (13.6.5)", 1 - t5[1] == Fraction(2, 3))
    check("P(a >= 3) ~ 0.0061 (13.6.5)", abs(float(t5[3]) - 0.0061) < 5e-5,
          f"{t5[3]}")

    print("\n== 2. tail to J = 11 (float, r truncated at 90) vs the bounds ==")
    J = 11
    df = mu_float(J)
    tf = [float(df[::3 ** j].sum()) for j in range(J + 1)]
    print(f"  {'j':>3} {'P(a>=j)':>12} {'(1/3)(5/6)^(j-1)':>18} {'2(0.93)^j':>12}"
          f" {'P(a>=j)*3^j':>13}")
    ok_new = ok_old = True
    for j in range(1, J + 1):
        bn, bo = float(Fraction(1, 3) * Fraction(5, 6) ** (j - 1)), 2 * 0.93 ** j
        ok_new &= tf[j] <= bn
        ok_old &= tf[j] <= bo
        print(f"  {j:>3} {tf[j]:>12.4e} {bn:>18.4e} {bo:>12.4e} {tf[j]*3.0**j:>13.4f}")
    check("P(a >= j) <= (1/3)(5/6)^(j-1) at every j <= 11", ok_new)
    check("P(a >= j) <= 2*(0.93)^j at every j <= 11", ok_old)
    check("float tail matches the exact tail for j <= 5",
          max(abs(tf[j] - float(t5[j])) for j in range(6)) < 1e-12,
          f"max |diff| = {max(abs(tf[j]-float(t5[j])) for j in range(6)):.1e}")

    print("\n== 3. max atom Q_t = max_z P(W = z mod 3^t) vs (5/6)^t ==")
    okQ = True
    for t in range(J + 1):
        Q = 1.0 if t == 0 else float(df.reshape(-1, 3 ** t).sum(axis=0).max())
        b = (5 / 6) ** t
        okQ &= Q <= b + 1e-15
        print(f"    t = {t:>2}:  Q_t = {Q:.10f}   (5/6)^t = {b:.10f}   ratio {Q/b:.5f}")
    check("Q_t <= (5/6)^t at every t <= 11", okQ)

    print("\n== 4. Monte Carlo on the composed-affine offsets (independent path) ==")
    for (Jm, N, sd) in ((6, 400000, 51001), (8, 400000, 51002)):
        mc = mc_tail(Jm, N, sd)
        worst = max(abs(mc[j] - tf[j]) / max((tf[j] / N) ** 0.5, 1e-12)
                    for j in range(1, Jm + 1))
        for j in range(1, Jm + 1):
            print(f"    j = {j}:  MC {mc[j]:.6f}   computed {tf[j]:.6f}")
        check(f"MC tail agrees with the computed tail, J = {Jm}, N = {N}, seed {sd}",
              worst < 4.0, f"worst z = {worst:.2f}")

    print("\n== 5/6. real integer orbits ==")
    Ws, k, D = [2, 3, 4, 6, 8], 3, 2
    tail, nvis, stat = orbit_run(52001, 260, 90, 220, Ws, k, D)
    print(f"  {nvis} tallied visits (260 orbits, 220-bit starts, 90 blocks, first 8 dropped)")
    okorb = True
    for j in range(1, 7):
        emp = tail[j] / nvis
        z = abs(emp - tf[j]) / max((tf[j] * (1 - tf[j]) / nvis) ** 0.5, 1e-12)
        okorb &= z < 4.5
        print(f"    j = {j}:  orbit {emp:.6f}   B-hat {tf[j]:.6f}   z = {z:.2f}")
    check("orbit absorption law matches the B-hat tail (j <= 6)", okorb)

    print(f"\n  finite-past reconstruction of (omega mod 2^{k+2}, min(d,{D})):")
    print(f"  {'W':>3} {'visits':>8} {'exc':>6} {'rate':>11} {'P(a>=W)':>11}"
          f" {'sync':>6} {'state':>6} {'capped':>7}")
    ok_rec = ok_rate = True
    for W in Ws:
        s = stat[W]
        rate = s["exc"] / s["n"]
        ok_rec &= (s["bad_sync"] == 0 and s["bad_state"] == 0 and s["bad_capped"] == 0)
        ok_rate &= abs(rate - tf[W]) < 4.5 * (tf[W] / s["n"]) ** 0.5 + 1e-9
        print(f"  {W:>3} {s['n']:>8} {s['exc']:>6} {rate:>11.3e} {tf[W]:>11.3e}"
              f" {s['bad_sync']:>6} {s['bad_state']:>6} {s['bad_capped']:>7}")
    check("reconstruction exact off {a >= W}: 0 sync, 0 state, 0 capped failures", ok_rec)
    check("measured failure rate = P_B-hat(a >= W) at every tested W", ok_rate)

    print("\nFAILURES:", FAILS if FAILS else "none")


if __name__ == "__main__":
    main()
```
