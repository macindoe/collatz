# Findings: the cut, the weighting, and the clock (v3 round 3, delegate C)

**Task:** `briefs/v3r3-cut-weighting-brief.md`. Read-only round; the only file written is this one.
**Read at:** `main` = `dc61306`, working tree clean apart from the round-3 briefs.
**Inputs used as settled:** `briefs/v3r3-aeh-object-findings.md` (delegate A, Option 1a chosen by the
author) and `briefs/v3r3-inselmann-horizon-findings.md` (delegate B, the `1/β` conversion refuted).
Neither is reopened. Where my design changes text that A or B also rewrote, §9 says so explicitly and
says which version wins.
**New computation this session:** `experiments/aeh_symbolic.py`'s flagship protocol was re-run in a
standalone replication (§4). It reproduces the record's `154,389` bulk visits **exactly**, and it
establishes that the bulk cut **does bind** in that run — contradicting `aeh.md` L48 and the script's
own docstring. Every number in §4 is from that run.

---

## 0. Verdict, in one paragraph

The reviewer is right on the arithmetic and understates the problem. `ν_{k,N}(x)` is normalized by
`Q_N(x)`, the orbit's own count of qualifying visits, so each qualifying visit does carry weight
`1/Q_N(x)`; and the deeper defect is not that the weight is orbit-dependent but that the **inclusion
rule is a function of the observable being tallied**: `x_exit(n) = (3^{d_n}ω_n − 1)/2^{s_n}`, so cutting
on `x_exit(n) > X_N` censors on `s_n`, a coordinate of `W_{k,D}(n)` and the subject of the ledger; and
cutting on `ω_+` censors on `s_n`, `m_{+,n}` **and** `a_{+,n}`, three of the five coordinates. Measured
in the record's own flagship run: the uncensored mean of `s` is `1.9999`, the `ω_+`-censored mean is
`1.9871`, and the `s ≥ 6` tail is depressed by `3.4 %` relative — the cut biases the ledger in exactly
the direction the geometry predicts. The repair is the author's clock directive, and it is decisive
rather than cosmetic: **move the horizon into total-exponent time, where the altitude bound
`log₂ x_exit(n) ≥ log₂ x − S_n` is an identity with no exceptional set, so a horizon stated as a digit
budget makes the cut non-binding by construction and the inclusion rule *predictable* — measurable with
respect to blocks strictly earlier than the one being tallied.** With the budget in place the
normalization is the reviewer's cemetery option, and it becomes clean: the denominator is the
deterministic block horizon `T_N`, every block of every orbit carries weight exactly `1/T_N`, `13.4`'s
safety criterion is satisfied verbatim at every rate, `Q_N(x) = 0` cannot arise, and the one clause that
is not a theorem — that the tallied blocks fit inside the budget — is precisely `E_B[m + r] = 4`, B's
disputed conversion, now visible inside the hypothesis instead of hidden in a side condition. "Admissible"
becomes two named clauses: *protected* (`τ < 1` deterministically; `τ < 4.8188…` by Inselmann) and
*consistent* (`4θ < τ`, which is the conversion). `θ` survives as a derived symbol only:
`θ = τ/E_B[m + r]`, and the record's two thresholds fall out of one inequality chain,
`4θ < τ < 1` giving `θ < 1/4` and `4θ < τ < 4.8188…` giving `θ < 1/β = 1.2047…`. **No proof that the
cut is non-binding past `θ = 1/4` in block units was found, and §7.4 records why one cannot come from
Inselmann.** The ceiling `τ* = (1 − log₂√3)^{-1} = 4.8188…` is not a limitation of technique: by
Inselmann's two-sided envelope it *is* the descent time, so past it there is no orbit left to sample.

---

## 1. The weighting, adjudicated

### 1.1 Is each qualifying visit weighted `1/Q_N(x)`? Yes.

`aeh.md` L30 defines `ν_{k,N}(x)` as "the unweighted empirical distribution of the depth-`k` window
states over the **bulk visits** among the first `T = ⌈θ log₂ N⌉`". An empirical distribution over a set
of items is normalized by the number of items. Writing

```text
Q_N(x) := #{ n < T_N : x_exit(n) > X_N },
```

we have `ν_{k,N}(x)(w) = #{n < T_N : bulk and W(n) = w} / Q_N(x)`. **Each qualifying visit therefore
carries weight `1/Q_N(x)`, and `Q_N(x)` varies from orbit to orbit.** The reviewer's arithmetic is
correct.

The paper's L247–250 is *ambiguous* where the wiki is not: "the empirical distribution of the depth-$k$
windows of the first $T$ visits, restricted to the \emph{bulk} visits". "Restricted to" admits a second
reading — the restriction as a sub-probability measure, denominator `T`, which is already the cemetery
normalization. The two texts do not currently say the same thing. Recording this because it is a live
discrepancy between the two statements of one hypothesis, and because the paper's reading is the one
this findings file recommends adopting everywhere.

### 1.2 What "no per-orbit reweighting" actually means, and whether it is defensible

`aeh.md` L30 says "each qualifying visit counted once, with no per-orbit reweighting (`13.5`)"; the paper
L249–250 says "each qualifying visit counted once and no visit reweighted by the orbit it came from".
The clause is denying a specific thing, and the thing it denies is real: `13.5`'s artifact
(L63) is an **across-orbit average of per-orbit ratios**, in which a visit belonging to an orbit with few
qualifying visits receives a larger weight than a visit in an orbit with many.

There are two levels and the record's sentence conflates them.

* **Across orbits.** The pooled estimator `Σ_x (visits to w) / Σ_x Q_N(x)` gives every visit the same
  weight; the per-orbit average `(1/#x) Σ_x ν_{k,N}(x)` gives a visit in orbit `x` weight
  `1/(#x · Q_N(x))`. `13.5` forbids the second. `13.2.1` is quenched — it averages nothing across
  orbits — so `13.5`'s bias does not by itself refute it.
* **Within one orbit.** Every qualifying visit of a given orbit gets the same weight `1/Q_N(x)`. So *within*
  an orbit the sentence is true by construction and says nothing.

So read charitably the sentence is about the across-orbit level, where it is true, and read literally it
is about the weight a visit carries, where it is true **exactly when `Q_N(x)` does not depend on the
orbit** — that is, exactly when the cut does not bind. That condition is stated one section later, at
`13.4` L48: "a per-orbit mean is safe exactly when its denominator is deterministic — fixed horizon, no
stopping rule, a cut that does not bind — and unsafe when the denominator is the random count of
qualifying visits, which is the ratio estimator `13.5` forbids." **`13.2.1` quantifies over every
`θ > 0`; the condition that makes its own sentence true is asserted only for `θ < 1/β` at L32; and B has
established that the `θ < 1/β` claim has no external support.** The tension is exactly as the brief
describes it, and it is the record's own.

### 1.3 Where the reviewer understates it: the cut censors on the observable

The sharper objection is not about the denominator at all.

```text
x_exit(n) = A_n / 2^(s_n),   A_n = 3^(d_n) ω_n − 1        (def:reduced; aeh.md 13.2)
```

so `x_exit(n)` is a strictly decreasing function of `s_n` at fixed `(ω_n, d_n)`. The inclusion rule
`x_exit(n) > X_N` therefore **selects against large `s_n`** — and `s_n` is a coordinate of A's observable
`W_{k,D}(n)` (§3.1 of A's findings) and is the subject of `13.3.1`'s ledger `P(s = j) = 2^{-j}`. The core
cut is worse:

```text
log₂ ω_(+,n) = log₂(x_exit(n) + 1) − m_(+,n) − a_(+,n)·log₂3        (aeh.md L48's identity)
```

so `ω_+ > X_N` selects against large `s_n`, large `m_{+,n}` **and** large `a_{+,n}` — three of the five
coordinates of `W_{k,D}`, including the two whose geometric tails are the whole of `13.6.5`'s depth law.
`aeh.md` L48 calls the `ω_+` cut "the strictly stronger cut"; it is also the strictly more *correlated*
one, and "stronger" is the wrong axis on which to compare them. §4 measures both.

**This is why a better cut is not the repair.** Any altitude threshold is a function of the current
block's own letter. The repair has to make the inclusion rule *predictable* — a function of strictly
earlier blocks. The exponent budget is exactly that (§5).

### 1.4 One consequence of `13.2.1` worth naming, because it is a strong claim nobody has stated

`ν` is a probability measure, so `‖ν − π‖_TV ≤ 1`; `13.2.1` says `‖ν − π‖_TV > ε` on a set of vanishing
density; hence by bounded convergence `E_x[ν_{k,N}(x)] → π_{k,D}`. **`13.2.1` therefore asserts that the
across-orbit average of per-orbit ratios — the estimator `13.5` forbids — is asymptotically unbiased.**
That is a legitimate assertion and not a contradiction, but it should be on the page, because it is the
precise sense in which the hypothesis and the standing rule interact: the rule forbids the estimator at
finite `N`, and the hypothesis asserts its bias vanishes.

---

## 2. `13.4`'s reconciliation sentence, checked against the code

The sentence at L48 is stated as one rule covering the hypothesis and the campaign. Against the code it
covers neither cleanly.

| protocol | denominator | deterministic? |
|---|---|---|
| `aeh_calibration.py` L358–372 (the four cells, incl. `pair43`) | `h[kk][0]`, the orbit's count of visits to the conditioning class, gated by `h[kk][0] >= 2` | **no** |
| `aeh_calibration.py` L400–406 (the `2^40` recheck that produced the `5σ`) | `den`, gated by `den >= 2` | **no** |
| `aeh_symbolic.py` L564–599 (`check_orbit_texture`, the flagship) | `nvis`, pooled across all orbits | deterministic only if the cut never binds — and it binds (§4) |
| `aeh_symbolic.py` L582–583, L604–605 (`per_orbit_w3`) | `o_w3[0]`, gated by `o_w3[0] > 10` | **no** — used for the across-orbit SE only |

Three findings, all verified above:

1. **`13.4`'s criterion condemns `13.4`'s own cell statistics.** Every per-orbit cell mean in
   `aeh_calibration.py` has a random denominator (a conditional cell's denominator is a class-visit
   count, random whatever the cut does). The criterion as written is about `13.2.1`'s bulk-visit
   denominator; it does not distinguish that from a conditioning denominator, and as a general rule it is
   too strong. The fix is to state it about the two objects separately (§8, drop-in).
2. **The flagship point estimates are pooled, not per-orbit.** `letter_hist`, `dhist`, `mod3_cond` and
   `nvis` in `check_orbit_texture` are global counters; only the standard error is across orbits
   (`per_orbit_w3`, L604–606). So `13.4`'s "`13.2.1` is a per-start (quenched) statement and therefore
   needs per-orbit statistics" describes the earlier rounds, while the run that resolved `13.5` and that
   `13.6.5` adjudicates against pools per visit. **The flagship run measures the annealed consequence of
   §1.4, not the quenched statement.** That is a real narrowing of what the campaign tests, and it is
   independent of A's `L ≤ 2` ceiling: the campaign is silent on both the block length above `2` and the
   quenched-versus-annealed axis. Measuring the quenched form needs the *distribution across orbits* of
   `‖ν(x) − π‖`, which nothing currently computes.
3. **`13.5`'s standing rule is the correct rule and survives untouched.** "Fixed-horizon, unweighted,
   per-visit sampling from uniform starts. Ratio estimators over correlated visit sequences are
   forbidden" (L65). Nothing here weakens it; §5's design is the first formulation of `13.2.1` that
   literally instantiates it.

---

## 3. The clock — the directive checked, and found correct

The directive is an accounting claim and it holds. Three verifications.

**(a) Total exponent is Inselmann's step count, exactly.** Inselmann's map is `T(m) = m/2` for `m` even,
`(3m+1)/2` for `m` odd (B §1.1, transcribed from his p. 1). A Syracuse step of valuation `v` is `v` of his
steps. An `F`-block from `(ω_n, d_n)` runs `m_n − 1` Syracuse steps of valuation `1` and one of valuation
`1 + s_n` (`prop:block`(i)–(ii); B §2.1), so it is `m_n + s_n` of his steps. Hence, writing

```text
S_n := Σ_{i<n} ( m_i + s_i ),      m_i = v_2(x_i + 1),  s_i = v_2(3^(d_i) ω_i − 1),
```

we have `x_exit(n−1) = T^{S_n}(x)` in **Inselmann's** `T`. The record's letter-word total
`S = Σ(m_i + r_i)` of L34 differs from this by `s_n − s_0` (one letter at each end, since `r_i = s_{i+1}`),
which is the one-index offset `13.6.3`(i)(a) already declares irrelevant to Cesàro limits.

**(b) The altitude bound is an identity, with no exceptional set.** For every `y ≥ 1`, Inselmann's
`T(y) ≥ y/2` (halving, or `(3y+1)/2 ≥ y`). Therefore, **for every odd `x` and every `n`, with no
hypothesis and no density caveat:**

```text
log₂ x_exit(n−1)  ≥  log₂ x − S_n.
```

Consequently, if `S_n < (1 − ε) log₂ N` then `x_exit(n−1) > N^ε`, which exceeds any `X_N` with
`log X_N = o(log N)` for `N` large. **Inside a digit budget of `(1 − ε)` of the start's own bits, the
bulk cut cannot bind — for every start, not merely density-one many.** This upgrades B's S1 from a
density-one statement with an `e^{−Θ(log N)}` exceptional set to a universal one; the exceptional set in
S1 came entirely from converting a block count into an exponent, and in exponent time there is nothing to
convert.

**(c) The three quantities are already commensurable, and the record already uses this clock.** In
exponent time, per bit of start: the cylinder base case at `1`; Inselmann's protected window at
`(1 − log₂√3)^{-1} = 4.818841679306416`; the digit budget of `paper` L168 and `stage4.md` `11.8.7.7` at
`1`, since it is stated in `2`-adic depth. `aeh.md` L34's own numbers are *already* exponent-time
numbers: the flagship run's "`2.29 ×` the budget, with `23` of its `30` tallied blocks beyond it" is
`(10 + 30)` blocks at `σ ≈ 4` against `70` bits, i.e. `160/70 = 2.2857…`; my replication measures the
consumed exponent directly as `4.0017` per block and `≈ 160` total (§4), reproducing both `2.29` and the
`23`-of-`30` crossing with no conversion at all. The conversion the record performs is only ever *out*
of this clock into blocks.

**(d) The naming hazard, disambiguated once.** Three maps have worn the letter `T`:

```text
paper L50, aeh.md throughout   T(x) = (3x+1)/2^(v_2(3x+1))    odd-to-odd (Syracuse); G = T^m (14.14.7.1)
Inselmann                      T(m) = m/2 or (3m+1)/2         one division per step
aeh.md L94 "raw T-steps"       = the first of these           so a letter is m_n of them, not m_n + r_n
```

`aeh.md` L94's "letter `n` occupies exactly `m_n` raw `T`-steps" is correct **in the page's own `T`** and
is off by the factor at issue if read in Inselmann's. B's §2.1 says the same. Wherever a horizon is
stated, name the map: this document uses **total exponent `S`** and never "`T`-steps".

---

## 4. Does the cut bind? — measured, not assumed

Standalone replication of `experiments/aeh_symbolic.py` `check_orbit_texture` (seed `31005`,
`NORB = 8000`, `BURN = 10`, `HOR = 30`, `CUT = 2^30`, starts uniform odd in `[2^70, 2^71)`, `w % 3 == 0`
skipped), using the script's own `F_step`. It reproduces the record's bulk-visit count exactly, which is
the check that the replication is faithful:

```text
orbits kept                       5,286          attempted visits 158,580
omega_+ > 2^30   bulk visits    154,389   below     4,191   (2.64 %)   <-- aeh.md L139's 154,389
x_exit  > 2^30   bulk visits    155,927   below     2,653   (1.67 %)
orbits with Q_N = 30 : omega_+ cut 4,466 / 5,286 (84.5 %) ;  x_exit cut 4,814 / 5,286 (91.1 %)
Q_N range (omega_+ cut): min 8, median 30 ;  orbits with Q_N = 0: none
total exponent over the 30 tallied blocks: mean 120.05 (4.0017 per block), min 83, max 177
```

**Findings.**

1. **`aeh.md` L48's "in these runs neither binds, so no number below depends on the choice" is false for
   the flagship run**, and so is `aeh_symbolic.py` L541–544's docstring "the bulk cut omega > 2^30 never
   binds within the burn-in + horizon (no survivorship selection at finite size; `13.2.1`'s limit regime
   realized directly)". The `ω_+` cut binds on **15.5 % of orbits** and removes **2.64 %** of visits; the
   door cut binds on **8.9 %** and removes **1.67 %**. `Q_N(x)` ranges over `8 … 30`. The tally
   denominator in the record's own flagship run is genuinely random.
2. **The two cut coordinates disagree on `1,538` visits** (`4,191 − 2,653`), so the choice is not
   immaterial even at the level of which visits are counted.
3. **The censoring is in the predicted direction and it hits the ledger.** Same run, mean of `s` and the
   `s`-marginal over the tallied blocks:

   ```text
                       n        mean s    P(s=1)    P(s=2)    P(s>=6)
   no censoring     158,580     1.9999    0.50069   0.24805   0.03118
   omega_+ cut      154,389     1.9871    0.50432   0.24717   0.03012
   x_exit  cut      155,927     1.9930    0.50225   0.24816   0.03055
   exponent budget  158,577     1.9999    0.50069   0.24806   0.03118      (tau = 2.29, the run's own)
   ```

   The uncensored mean is `E_B[s] = 2` to four places. Both altitude cuts pull it down, the `ω_+` cut
   about twice as far as the door cut, and both depress the `s ≥ 6` tail (`−3.4 %` and `−2.0 %`
   relative). Visits within an orbit are correlated, so these are directional rather than significance
   statements; the point is the sign, which is forced by §1.3's geometry, and the last row, in which the
   **predictable** exponent rule at the run's own budget reproduces the uncensored ledger to five
   decimals while excluding `3` blocks out of `158,580`.
4. **The flagship run sits at `τ ≈ 2.29`, i.e. at `47.5 %` of Inselmann's unconditional exponent
   window** `4.8188…`. So the entire calibration campaign is inside the range where the door's altitude
   is unconditionally controlled at natural density one — a fact the record cannot currently state,
   because it has no exponent-time horizon to state it in. The residual `8.9 %` door-cut binding is
   finite-size: at `L = 70` the descent's fluctuation is `≈ ±10` bits about a `≈ 33`-bit drop.

---

## 5. The normalization: chosen, with its cost

### 5.1 Chosen — the reviewer's option 2 (cemetery), keyed to an exponent budget rather than an altitude

**The horizon is a deterministic block count `T_N = ⌈θ log₂ N⌉`. The inclusion rule is a deterministic
exponent budget `Λ_N = ⌈τ log₂ N⌉`. Block `n` is tallied at its own letter if the exponent spent before
it satisfies `S_n < Λ_N`, and at a single cemetery symbol `†` otherwise. The denominator is `T_N`.**

Six properties, each of which is the failure of some other option:

1. **The denominator is deterministic at every rate.** Every block of every orbit carries weight exactly
   `1/T_N`. `13.4`'s criterion — "safe exactly when its denominator is deterministic" — is satisfied
   verbatim, for all `θ`, with nothing assumed.
2. **The inclusion rule is predictable.** `S_n` is a function of blocks `0, …, n−1` only. The decision to
   tally block `n` is measurable with respect to its strict past, so it cannot censor on the letter being
   tallied. This is the property no altitude cut has (§1.3), and it is measured in §4 item 3.
3. **The bulk cut is deleted from the statement.** By §3(b) the budget implies the altitude bound
   deterministically for `τ < 1` and, by B's S2 (Inselmann Thm 1.1/1.10), at natural density one for
   `τ < 4.8188…`. The sequence `(X_N)` and the condition `log X_N = o(log N)` disappear from the
   hypothesis, and with them the second admissibility question.
4. **`Q_N(x) = 0` cannot arise** (§6.2).
5. **The hypothesis adjudicates the below-budget mass itself.** `π_{k,D}(†) = 0` and `B[w] = 0` for any
   word containing `†`, so `‖ν − π‖_TV < ε` forces the cemetery frequency below `ε`. The clause "the
   first `T_N` blocks fit inside the budget" is asserted, not assumed.
6. **The conversion B refuted becomes visible.** That clause says `S_{T_N} < Λ_N`, i.e.
   `θ·E_B[m + r] < τ`, i.e. `4θ < τ`. B's disputed division by `E[m + r] = 4` is now one printed
   inequality inside the hypothesis instead of a hidden step in a side condition. It is a theorem where
   the cylinder count runs (`τ < 1`) and part of the assertion where it does not — exactly B's verdict,
   given a place to live.

**The cost, stated plainly.**

* **The hypothesis is strictly stronger than the current one.** It now also asserts `4θ < τ` — that the
  first `⌈θ log₂ N⌉` blocks consume less than `⌈τ log₂ N⌉` of exponent for density-one starts. Under the
  stopped normalization that assertion was not made; the cut simply threw away whatever did not fit.
* **A second rate appears.** `τ` and `θ` are two parameters where the record had one. §7 argues `τ` is the
  primitive and `θ` the derived one, which recovers a single free parameter in practice; but the pair is
  what the honest statement quantifies over.
* **Statements that used to be about "bulk blocks" become statements about "in-budget blocks."** That is a
  wording change in `13.3.1`, `13.3.2`, `13.6.4` and `13.6.6`, itemized in §10.
* **A cemetery symbol is one more letter.** Checked against A's alphabet in §9.1: it does not break
  anything of A's.

### 5.2 The rejected options, with why

* **Reviewer's option 1 — restrict "admissible" to regimes where `Q_N = T_N` on a density-one set, and
  state the condition rather than its threshold.** Correct as far as it goes, and it is half of what §6.1
  does. Rejected as the *whole* answer for two reasons. It leaves the condition unverifiable — nothing in
  §4's protocol can check "`Q_N = T_N` on a density-one set" at finite `N`, and §4 shows it is false at
  finite `N` — and it leaves the altitude cut in place, so §1.3's censoring on `s`, `m_+`, `a_+` survives
  untouched. It fixes the denominator and not the selection.
* **Reviewer's option 3 — keep stopped normalization for all `θ`, but stop identifying it with the
  unbiased calibration protocol.** This is the cheapest option and it is defensible: `13.2.1` is a limit
  statement, and a denominator that concentrates costs a limit statement nothing. Rejected because it
  gives up the record's most valuable structural feature — that the hypothesis and the protocol are one
  rule — in exchange for keeping a formulation whose inclusion rule is correlated with its own
  observable. It would also require `13.4` to say that the flagship run measures something the hypothesis
  does not assert, which §2 item 2 shows is already half true and should be reduced, not enlarged.
* **A budget horizon with the block count as denominator** (tally exactly the in-budget blocks, normalize
  by their number). One parameter instead of two, and the inclusion rule is still predictable — but the
  denominator is a renewal count of the very letters being tallied, so it is random again, with an
  inspection-paradox bias of order `1/n`. It trades the whole point away to save a symbol.
* **Weighting each block by its own exponent and normalizing by `Λ_N`.** Genuinely elegant: deterministic
  denominator, one parameter, and each block's weight a function of nothing but itself. Rejected because
  the comparison object becomes the exponent-size-biased letter law `(m+r)2^{−(m+r)}/4` rather than `B`,
  which changes A's fixed `π_{k,D}` and does not match anything the calibration measures.

---

## 6. The definitions

### 6.1 "Admissible"

Currently undefined at `aeh.md` L30 and `paper` L256; grepped, no section supplies it. It becomes two
clauses on the pair `(τ, θ)`.

**Definition (admissible).** A budget rate `τ > 0` is **protected** if for every cut `X_N → ∞` with
`log X_N = o(log N)`, all but a vanishing density of odd `x ∈ [N, 2N)` satisfy `x_exit(n) > X_N` for
every `n` with `S_n(x) < τ log₂ N`. A pair `(τ, θ)` is **consistent** if `θ · E_B[m + r] < τ`, i.e.
`4θ < τ`. **Admissible** = protected and consistent.

What is known about each clause, with the source of each number:

| clause | range | status |
|---|---|---|
| protected | every `τ < 1` | **theorem, and universal**: `log₂ x_exit(n) ≥ log₂ x − S_n` holds for every start, no exceptional set (§3(b)) |
| protected | every `τ < (1 − log₂√3)^{-1} = 4.818841679306416` | **theorem at natural density one**, Inselmann Thm 1.1 / Thm 1.10 (B's S2). Sharp: Cor. 1.4 puts the orbit below `m^ε` at exactly that time |
| protected | `τ ≥ 4.8188…` | **false**. By Inselmann's *two-sided* envelope the altitude at budget `τ` is `(1 − τ/4.8188…) log₂ N ± ε log₂ N`, so the orbit has descended and the bottom regime of `13.1` enters the tally |
| consistent | `4θ < τ` | **theorem for `τ < 1`** by the cylinder count of L34; **part of the hypothesis** for `τ ≥ 1`. This is B's `E[m + r] = 4` conversion, and it is the only clause that is not a theorem |

**Two corollaries the record should print, because they replace the sentence B refuted.**

```text
4θ < τ < 1          <=>  θ < 1/4                      the unconditional range; everything is a theorem
4θ < τ < 4.8188...  <=>  θ < 4.8188.../4 = 1/beta     the admissible range; the "4" is the hypothesis's own
```

`1/β = 1.204710419826604` and `4/β = (1 − log₂√3)^{-1} = 4.818841679306416` are the same identity B
records at S3. So the record's `1/β` **survives, in the right role**: it is the block-time image of the
descent horizon, hence the admissibility ceiling, and its block reading visibly carries AEH's own
conversion. What does not survive is `1/β` as the range over which the cut's non-binding is externally
supported *in block units*. The number was always the descent time; only its job was wrong.

**The ceiling is not modesty.** `τ* = 4.8188…` is the descent itself. Past it the orbit is at `O(1)`,
`13.1`'s bottom regime supplies the letters, and `13.6.6` already records that the unrestricted statement
is *false* on every convergent orbit. So there is nothing to hope for above the ceiling, and the
hypothesis should not quantify above it.

### 6.2 `Q_N(x) = 0`

**Under §5.1 the case cannot arise.** Every block `n < T_N` contributes exactly one tallied symbol —
its letter, or `†` — so `ν` is a probability measure on the extended alphabet for every start and every
`N`, with no convention required. An orbit every one of whose blocks exceeds the budget gives `ν = δ_†`,
hence `‖ν − π‖_TV = 1 > ε`, hence membership in the exceptional set, which is where such a start belongs.

Recorded for completeness, since the current text does need an answer until the change is applied: under
the *present* formulation `Q_N(x) = 0` requires `x_exit(0) ≤ X_N`, i.e. a first block dropping from `≥ N`
to `N^{o(1)}`, which by `x_exit = (3^{d}ω − 1)/2^{s}` needs `s ≳ (1 − o(1)) log₂ N`. That has density
`N^{−1+o(1)}` — vanishing but nonzero at every `N`, so the case is not vacuous and `ν` is genuinely
undefined on a nonempty set. §4 finds no such orbit in `5,286` samples at `L = 70`, as expected.

### 6.3 The cut coordinate: the door, and then neither

**Settled: cut on the door `x_exit`, never on the core `ω_+`; and in the hypothesis, cut on neither —
bound the budget.** Four reasons, in order of weight.

1. **The budget controls the door and cannot control the core.** `log₂ x_exit(n) ≥ log₂ x − S_n` is an
   identity (§3(b)). No analogous bound holds for `ω_+`: `log₂ ω_+ = log₂(x_exit + 1) − m_+ − a_+ log₂3`
   and `a_+` is not bounded by any exponent budget — the budget is `2`-adic and `a_+` is `3`-adic. So the
   core cut cannot be made deterministic by any device in this clock.
2. **The bottom regime is a set of small integers, and `x_exit` is the integer.** `13.1` defines the
   bottom as "the fixed, finite drainage basin of small integers"; `13.6.3`(i)(a) records that "the visit
   datum `x_exit` **is** the door `y_n`". A state at high altitude with a large `m_+` or `a_+` has a small
   core and is not in the drainage basin; the `ω_+` cut discards it anyway.
3. **The `ω_+` cut censors three coordinates of the observable, the door cut one** (§1.3), and §4
   measures the `ω_+` cut's ledger bias at roughly twice the door cut's, in the same direction.
   "Strictly stronger" (L48) is true and is the wrong comparison: it is strictly more correlated with what
   is being measured.
4. **Only the door is covered by the literature.** B's §2.7 rider 3: Inselmann's envelope applies to
   Syracuse iterates, and the doors are genuine Syracuse iterates; it does not control `ω_+`.

**What the calibration record then supports.** The recorded numbers were produced with the `ω_+` cut, so
strictly they support statements about the `ω_+`-censored family. §4 quantifies the gap: `1,538` visits of
`158,580` (`0.97 %`) differ between the two rules, and the induced ledger difference is `≈ 0.007` in mean
`s`. That is small, and it is not zero, and L48's "no number below depends on the choice" is not what the
run shows. The honest sentence is: the cut binds on `2.6 %` of visits and `15.5 %` of orbits, the two cut
rules differ on `1.0 %` of visits, and the resulting bias in the `s`-marginal is at the third decimal and
in the direction the geometry predicts.

**The cut survives as a finite-size device, not as part of the statement.** Below the budget it is
provably redundant asymptotically, but §4 shows it does real work at `L = 70` — the deterministic bound is
vacuous at `τ = 2.29 > 1` and Inselmann's is asymptotic. So the protocol should keep an altitude guard, on
the **door**, and **report its binding rate every run** rather than assert it does not bind. This is
exactly the status A's §3.6 item 3 gives the burn-in of `10`: a finite-size device, absent from the
hypothesis.

---

## 7. `θ`'s fate under the exponent clock

**`θ` survives as a symbol and is demoted from primitive to derived.**

* **The primitive is `τ`, the budget rate, in units of the start's own digits.** It is the cascade's own
  currency: `τ = 1` is the classical digit budget of `11.8.7.7`, `τ = 4.8188…` is Inselmann's window,
  `τ = 2.29` is the flagship run (`aeh.md` L34's own number). No conversion is performed anywhere in that
  list. `τ` is free at `aeh.md` and in the paper (grepped: `τ` absent from `aeh.md`, `\tau` and `\Lambda`
  absent from the paper; `λ` is taken at `aeh.md` L53 for a transfer-matrix eigenvalue, so `τ` and not
  `λ`).
* **`θ` remains the block horizon rate**, because block frequencies are what the hypothesis is about and
  the tally must run over a definite number of blocks to have a deterministic denominator. But it no
  longer carries the horizon: it is constrained by `4θ < τ`, and where a single rate is wanted the record
  should fix `τ` and read `θ = τ/E_B[m + r] = τ/4` **with the division named as AEH's own content**.
* **`T` becomes two objects and both should be printed.** The **budget** `Λ_N = ⌈τ log₂ N⌉`, in total
  exponent, is the horizon in the sense of "how far past the digit budget"; the **block horizon**
  `T_N = ⌈θ log₂ N⌉` is the tally length. The record's single `T = ⌈θ log₂ N⌉` was doing both jobs.
* **Should the hypothesis be quantified over an exponent budget rather than a block count? Yes — over
  both, with the budget primary.** The budget is what the base case bounds (`S + 1 ≤ L`), what Inselmann
  bounds, what the digit-budget theorem spends, and what the altitude identity uses. The block count is
  what the observable is indexed by. Quantifying over only one of them is what forced the conversion.

---

## 8. Drop-in text

All of it assumes A's Option 1a and A's definitions block. Collisions are listed in §9.

### 8.1 `aeh.md` — Hypothesis `13.2.1`, replacing A's §7.4 version of it

````markdown
**Hypothesis 13.2.1 (AEH, ensemble form).** Fix a **budget rate** `τ > 0` and a **block horizon rate** `θ > 0`. For each `N` put `L = ⌊log₂ N⌋`, `Λ_N = ⌈τL⌉` and `T_N = ⌈θL⌉`. Draw `x` uniformly from the odd integers of `[N, 2N)`, set `(ω_0, d_0) = R(x)` and `(ω_{n+1}, d_{n+1}) = F(ω_n, d_n)`, and let the **letter** at block `n` be `ℓ_n = (m_(+,n), s_(n+1))` (`13.6.3`(i); reverse.md `14.14.6`). Let `S_n = Σ_(i<n) (m_i + s_i)` be the **exponent spent** before block `n` — the number of `2`'s divided out from `x` to `x_exit(n−1)`, so that `x_exit(n−1) = T_1^(S_n)(x)` for the one-division map `T_1(y) = y/2` or `(3y+1)/2`. Assign to block `n` the **tallied symbol**

```text
ℓ̃_n = ℓ_n            if S_n < Λ_N        (the block is within budget),
ℓ̃_n = †              otherwise           (the cemetery symbol).
```

For a finite word `w = (w_1, …, w_ℓ)` of letters, let `f_N(w, x)` be the frequency of `w` among the `T_N − ℓ + 1` blocks `(ℓ̃_n, …, ℓ̃_(n+ℓ−1))`, `0 ≤ n ≤ T_N − ℓ`: **every block counted exactly once, at weight `1/(T_N − ℓ + 1)` — the same number for every block of every orbit, so no visit is reweighted by the orbit it came from and no denominator is random (`13.4`, `13.5`).** Then for **every finite word `w`** and every `ε > 0`, the density of starts `x ∈ [N, 2N)` with `|f_N(w, x) − B[w]| > ε` tends to `0` as `N → ∞`, where `B[w] = Π_i 2^-(m_i + r_i)` and `B[w] = 0` for any `w` containing `†`, for every **admissible** `(τ, θ)` in the sense of `13.2.3`.
````

The budget clause is **predictable**: `S_n` depends on blocks `0, …, n−1` only, so whether block `n` is
tallied is decided before its own letter is read. That is what an altitude cut cannot do — `x_exit(n)`
is `(3^(d_n)ω_n − 1)/2^(s_n)`, so a cut on it selects against large `s_n`, and a cut on `ω_+` selects
against large `s_n`, `m_(+,n)` and `a_(+,n)` at once. There is no bulk cut in this statement and no
sequence `(X_N)`: by `13.2.3` the budget bounds the door from below without one.

### 8.2 `aeh.md` — Hypothesis `13.2.2`, amending A's §7.4 version

Replace A's opening "Same sampling and same bulk blocks" and its tally clause with:

````markdown
**Hypothesis 13.2.2 (the window form; equivalent).** Same sampling, same budget, same tallied blocks. For every `k`, `D` and `ℓ`, let `ν^(ℓ)_{k,D,N}(x)` be the empirical distribution of the `ℓ`-blocks `(W̃_n, …, W̃_(n+ℓ−1))`, `0 ≤ n ≤ T_N − ℓ`, where `W̃_n = W_{k,D}(n)` if `S_n < Λ_N` and `W̃_n = †` otherwise — every block at weight `1/(T_N − ℓ + 1)`. Then for every `ε > 0` the density of starts with `‖ν^(ℓ)_{k,D,N}(x) − π^(ℓ)_{k,D}‖_TV > ε` tends to `0`, where `‖·‖_TV` is total variation on the finite alphabet of `W_{k,D}` together with `†`, `‖μ − π‖_TV = ½ Σ_w |μ(w) − π(w)|`, and `π^(ℓ)_{k,D}` gives `†` mass `0`. `13.2.1 ⟺ 13.2.2` is Theorem `13.6.4`. The case `ℓ = 1` — the empirical law of single window states against `π_{k,D}` — is the marginal form that `13.3.1` and `13.3.2` consume; it is strictly weaker than either hypothesis, by (q1).
````

### 8.3 `aeh.md` §13.2 — appended anchor `13.2.3` (new; nothing renumbered)

````markdown
**13.2.3 (the clock, and what "admissible" means).** Horizons on this page are stated in **total exponent** — the number of `2`'s the cascade divides out, which is the cascade's own currency and the unit the digit budget of stage4.md `11.8.7.7` is stated in. One block of `(ω, d)` is `m` Syracuse steps and `m + s` divisions, so `S_n = Σ_(i<n)(m_i + s_i)` counts divisions and `x_exit(n−1) = T_1^(S_n)(x)` exactly, `T_1` being the one-division map `y ↦ y/2` (`y` even), `y ↦ (3y+1)/2` (`y` odd). Three readings of the letter `T` are in play and are kept apart here: this page's `T` is the odd-to-odd map, with `G = T^m` (`14.14.7.1`) and a letter occupying `m_n` of its steps (`13.6.3`(i)(b)); `T_1` is the one-division map, of which a letter occupies `m_n + r_n`; and `T_N` is the block horizon above.

**The altitude bound.** `T_1(y) ≥ y/2` for every `y ≥ 1`, so **for every odd `x` and every `n`, with no hypothesis and no exceptional set,**

```text
log₂ x_exit(n−1)  ≥  log₂ x − S_n.
```

Hence if `S_n < (1 − ε)log₂ N` then `x_exit(n−1) > N^ε`: inside a budget of `(1 − ε)` of the start's own bits, no visit can be near the bottom regime of `13.1`, and any cut with `log X_N = o(log N)` is vacuous. This is why `13.2.1` needs no bulk cut.

**Admissible.** A budget rate `τ` is **protected** if for every `X_N → ∞` with `log X_N = o(log N)`, all but a vanishing density of odd `x ∈ [N, 2N)` have `x_exit(n) > X_N` at every `n` with `S_n < τ log₂ N`. A pair `(τ, θ)` is **consistent** if `θ·E_B[m + r] < τ`, i.e. `4θ < τ`. **Admissible** means both.

* Every `τ < 1` is protected, by the altitude bound, for *every* start.
* Every `τ < (1 − log₂√3)^(-1) = 4.8188…` is protected at natural density `1`, unconditionally (Inselmann Thm `1.1`/`1.10`; `13.3.2`). This is a `4.8188 ×` extension of the first range, in the same unit, with nothing converted.
* No `τ ≥ 4.8188…` is protected, and this is sharp rather than a gap in technique: Inselmann's envelope is two-sided, so at budget `τ` the altitude is `(1 − τ/4.8188…)log₂ N ± ε log₂ N` and the orbit has descended. `13.6.6` records that the unrestricted statement is false on a convergent orbit. Above the ceiling there is no orbit left to sample.
* Consistency is a theorem for `τ < 1` — it is the base case's cylinder count — and is **part of what `13.2.1` asserts** for `τ ≥ 1`: `π_{k,D}` gives `†` no mass, so the hypothesis says the first `T_N` blocks fit inside the budget, which is exactly `E_B[m + r] = 4` in Cesàro form.

Reading the two ranges in blocks per bit is therefore a use of the hypothesis, not an input to it:

```text
4θ < τ < 1          <=>  θ < 1/4        every clause a theorem (base case)
4θ < τ < 4.8188...  <=>  θ < 1/beta     the admissible range; the divisor 4 is 13.2.1's own content
```

with `1/β = 1.2047…`, `β = 2(2 − log₂3) = 0.8301…`, and `4/β = (1 − log₂√3)^(-1)` an identity. `β`'s leading factor `2` is `E[m] = 2` Syracuse steps per block, so "`1/β` blocks per bit" carries the same conversion inside its own definition.
````

### 8.4 `aeh.md` L32 — replacing the whole "Why the ensemble" paragraph

````markdown
**Why the ensemble, and what the horizon is now for.** There is one limit, `N → ∞`; the sample grows because the sampling scale grows, not because any orbit is run forever. No single-orbit form is available: above a fixed cut a convergent orbit supplies finitely many qualifying visits and, once the cut exceeds its maximum, none, so a limit in orbit length is empty rather than delicate — in either order, and for a diagonal cut `X(n)` too. The horizon does the job the bulk cut used to do, and does it without a cut: by `13.2.3` an exponent budget bounds every tallied exit from below, `log₂ x_exit(n−1) ≥ log₂ x − S_n`, deterministically, so within the budget no visit is near the bottom regime of `13.1` and there is nothing to excise. That matters because every altitude cut is a selection on the observable being tallied — `x_exit(n) = (3^(d_n)ω_n − 1)/2^(s_n)` censors large `s_n`, and the stronger cut on the core censors large `s_n`, `m_(+,n)` and `a_(+,n)` together — while the budget clause `S_n < Λ_N` is *predictable*, decided by blocks strictly earlier than the one it admits. The denominator is the deterministic `T_N = ⌈θ log₂ N⌉` at every rate, every block carries weight `1/T_N`, and `13.5`'s standing rule is satisfied as written with nothing assumed about where the cut binds. The sample space is starting *values*, not states: natural density on pairs `(ω,d)` is not canonical, and the integer form is the one with an exact base case below. Because the bad density vanishes at every scale, the union of the bad sets has natural density zero in the integers — so the statement does deliver "almost every integer", for a finite-horizon property, with the exceptional set depending on `ε`, `τ` and `θ`.
````

### 8.5 `aeh.md` L34 — the base case, restated in the same clock

Keep A's §7.4 addendum sentence and B's §5.2 replacement of the Inselmann clause, and replace the two
sentences beginning "**Hypothesis 13.2.1 is therefore a theorem for every `θ < 1/4`.**" and ending
"…`23` of its `30` tallied blocks beyond it." with:

````markdown
**Hypothesis `13.2.1` is therefore a theorem for every admissible `(τ, θ)` with `τ < 1`** — equivalently, by `13.2.3`, for every `θ < 1/4` — the cylinder count supplying consistency and the altitude bound supplying protection, both unconditionally. A full descent spends `(1 − log₂√3)^(-1) = 4.8188…` of exponent per bit of start, `4.8188` budgets, which is `1/β = 1.2047…` blocks per bit once one divides by `E[m + r] = 4`; the hypothesis is precisely the assertion that equidistribution survives past the first budget, and its admissible ceiling is the descent itself. The calibration record is measured well past the first budget and well inside the ceiling: the flagship run (starts `[2^70, 2^71)`, burn-in `10`, horizon `30`) spends `≈ 160` of exponent against `70` bits of start, i.e. `τ ≈ 2.29` — `2.29 ×` the budget and `47 %` of the descent — with `23` of its `30` tallied blocks past the first budget. Its measured exponent per block is `4.0017`.
````

### 8.6 `aeh.md` L48 — the reconciliation sentence and the cut-coordinate note

Replace from "This and `13.5`'s standing rule are one rule…" through "…so no number below depends on the
choice." with:

````markdown
This and `13.5`'s standing rule are one rule, and the reconciliation is load-bearing now that `13.2.1` is a per-start (quenched) statement. Two denominators must be kept apart. **The hypothesis's** denominator is the block horizon `T_N`, which is deterministic by construction (`13.2.1`: every block tallied once, at or below budget, at weight `1/T_N`), so the quenched statement is not a ratio estimator at any rate. **An estimator's** denominator is whatever the cell conditions on, and a per-orbit mean is safe exactly when that denominator is deterministic — fixed horizon, no stopping rule, no data-dependent gate — and unsafe when it is the random count of visits satisfying a condition, which is the ratio estimator `13.5` forbids. The cell statistics below are per-orbit means over conditional counts (`aeh_calibration.py`: `h[cell][0]`, gated at `>= 2`), so they are of the second kind and are reported with across-orbit standard errors; the fixed-horizon protocol of `13.5` and `13.6.5` pools per visit (`aeh_symbolic.py` `check_orbit_texture`), which is of the first kind and is the one that adjudicates. Pooling measures the across-orbit average of the per-orbit frequencies; `13.2.1` implies that average converges, so the pooled runs test a consequence of the hypothesis rather than the quenched statement itself. The quenched form would be tested by the distribution across orbits of `‖ν(x) − π_{k,D}‖`, which no run currently reports.

One protocol gap, recorded with its size: the statements tally within an exponent budget (`13.2.3`), which bounds every tallied exit from below without a cut, while the code cuts on the core, `ω_+ > X` (`aeh_calibration.py` L360, L402; `aeh_symbolic.py` L566). The core is the wrong coordinate — `log₂ ω_+ = log₂(x_exit + 1) − m_+ − a_+·log₂3`, so cutting on it censors `s`, `m_+` and `a_+` at once, and no exponent budget controls `a_+`, which is `3`-adic — and the cut does bind: in the flagship run it removes `4,191` of `158,580` visits (`2.6 %`) and binds on `15.5 %` of orbits, against `2,653` (`1.7 %`) and `8.9 %` for the door cut `x_exit > X`, the two rules disagreeing on `1,538` visits. The censoring is in the direction the geometry predicts: mean `s` is `1.9999` uncensored, `1.9930` under the door cut and `1.9871` under the core cut, with the `s ≥ 6` tail depressed by `2.0 %` and `3.4 %` relative. The effect is at the third decimal and the numbers below are unaffected at their quoted precision, but "neither binds" is not what the run shows. An altitude guard remains appropriate as a finite-size device, on the **door** and with its binding rate reported each run; the budget of `13.2.3` is what the statement uses.
````

### 8.7 `paper/collatz-reduced-v3.tex` — replacing `hypothesis` (L243–257), amending A's §7.2

```latex
\begin{hypothesis}[AEH, ensemble form]\label{hyp:aeh}
Fix a \emph{budget rate} $\tau > 0$ and a \emph{block horizon rate} $\theta > 0$;
for each $N$ put $L = \lfloor\log_2 N\rfloor$, $\Lambda_N = \lceil \tau L\rceil$
and $T_N = \lceil \theta L\rceil$. Draw $x$ uniformly from the odd integers of
$[N, 2N)$; put $(\w_0,d_0) = R(x)$ and $(\w_{n+1},d_{n+1}) = F(\w_n,d_n)$; let the
\emph{letter} at block $n$ be $\ell_n = (m_{+,n},\,s_{n+1})$, and let
$S_n = \sum_{i<n}(m_i + s_i)$ be the \emph{exponent spent} before block $n$ ---
the number of $2$'s divided out from $x$ to $x_{\mathrm{exit}}(n-1)$. Tally block
$n$ at the symbol
\[
  \tilde\ell_n \;=\; \ell_n \ \text{ if } S_n < \Lambda_N, \qquad
  \tilde\ell_n \;=\; \dagger \ \text{ otherwise.}
\]
For a finite word $w = (w_1,\dots,w_\ell)$ of letters, let $f_N(w,x)$ be the
frequency of $w$ among the $T_N - \ell + 1$ blocks
$(\tilde\ell_n,\dots,\tilde\ell_{n+\ell-1})$, $0 \le n \le T_N - \ell$: every
block counted exactly once, at weight $1/(T_N-\ell+1)$ --- the same number for
every block of every orbit, so no block is reweighted by the orbit it came from
and no denominator is random. Then for every finite word $w$ and every
$\varepsilon > 0$,
\[
  \frac{2}{N}\,\#\bigl\{\, x \text{ odd},\ N \le x < 2N \;:\;
  \bigl| f_N(w,x) - B[w] \bigr| > \varepsilon \,\bigr\}
  \;\longrightarrow\; 0 \qquad (N \to \infty),
\]
where $B[w] = \prod_{i} 2^{-(m_i + r_i)}$ and $B[w] = 0$ for any $w$ containing
$\dagger$, for every admissible pair $(\tau,\theta)$.
\end{hypothesis}
```

A's second paragraph (the window equivalence) follows verbatim except for two substitutions: "over the
same bulk blocks" becomes "over the same tallied blocks, with $\dagger$ carried through and given mass
$0$ by $\pi^{(\ell)}_{k,D}$", and "$T \to \infty$" becomes "$T_N \to \infty$".

### 8.8 `paper/collatz-reduced-v3.tex` L270–277 — replacing the cut sentence, superseding B's §5.4

```latex
The horizon does the job a bulk cut would do, and does it without one. A step of
the one-division map $y \mapsto y/2$ or $(3y+1)/2$ never lowers $\log_2$ by more
than $1$, so $\log_2 x_{\mathrm{exit}}(n-1) \ge \log_2 x - S_n$ for every start and
every $n$, with no exceptional set; inside a budget $\tau < 1$ of the start's own
bits every tallied exit therefore exceeds $N^{1-\tau}$, far above the
\emph{bottom regime} of \texttt{aeh.md} \S13.1. That matters because any altitude
threshold is a selection on the observable itself:
$x_{\mathrm{exit}} = (3^{d}\w - 1)/2^{s}$, so a cut on it censors large $s$, and a
cut on the core $\wnext$ censors large $s$, $m_+$ and $a_+$ together. The budget
clause $S_n < \Lambda_N$ is instead \emph{predictable} --- decided by blocks
strictly earlier than the one it admits --- and the tally denominator is the
deterministic $T_N = \lceil\theta\log_2 N\rceil$ that \texttt{aeh.md} \S13.5's
standing rule --- fixed horizon, unweighted, per-visit sampling from uniform
starts --- was written to secure. Call $\tau$ \emph{protected} when all but a
vanishing density of starts keep every in-budget exit above any $X_N$ with
$\log X_N = o(\log N)$, and $(\tau,\theta)$ \emph{consistent} when
$\theta\,\mathbb{E}_B[m+r] < \tau$; \emph{admissible} means both. Every
$\tau < 1$ is protected outright by the bound above, and every
$\tau < (1-\log_2\sqrt3)^{-1} = 4.8188\ldots$ is protected at natural density one
by Inselmann \cite[Thm.~1.10]{inselmann} --- the same unit, nothing converted.
Consistency is a theorem where the cylinder count runs and is part of
Hypothesis~\ref{hyp:aeh} where it does not, since $\pi_{k,D}$ gives $\dagger$ no
mass; it says exactly that blocks average $\mathbb{E}_B[m+r] = 4$ of exponent.
Hence $4\theta < \tau < 1$ is $\theta < 1/4$ and $4\theta < \tau < 4.8188\ldots$
is $\theta < 1/\beta = 1.2047\ldots$, where $\beta = 2(2-\LL) = 0.8301\ldots$ is
the classical per-block contraction rate and $4/\beta = (1-\log_2\sqrt3)^{-1}$ is
an identity: the block reading of either threshold divides by a mean the
hypothesis itself supplies.
```

Requires `\newcommand{\dagger}` — none needed, `\dagger` is standard LaTeX. `\mathbb{E}` needs
`amssymb`/`amsmath`, already loaded for `\mathbb{Z}` (macro `\Z`, L17).

### 8.9 `paper/collatz-reduced-v3.tex` L286–293 — the base-case sentences, in the same clock

Replace from "Since $S$ accumulates at mean rate $4$ per block" through "some $4.8$ times as long." with:

```latex
Since the cylinder count is a statement about the itinerary's total exponent, it
is a statement about the budget directly: it makes Hypothesis~\ref{hyp:aeh} a
\emph{theorem} at every $\tau < 1$, hence --- consistency being a theorem there
too --- at every horizon rate $\theta < 1/4$. A descent from $N$ to $O(1)$ spends
$(1-\log_2\sqrt3)^{-1} = 4.8188\ldots$ of exponent per bit, some $4.8$ budgets,
which is $1/\beta = 1.2047\ldots$ blocks per bit after dividing by the mean
exponent per block --- the $\sigma \approx 4.0$ of Heuristic~\ref{prop:budget},
exactly $2+2$ under $\pi_{k,D}$.
```

### 8.10 `paper/collatz-reduced-v3.tex` L301–304 — one clause of A's §7.3

In A's §7.3 replacement, "along their first $\lceil\theta\log_2 x\rceil$ bulk blocks" becomes "along
their first $\lceil\theta\log_2 x\rceil$ blocks, all of them within the budget". Nothing else in A's
§7.3 moves.

### 8.11 `aeh.md` §13.5 (L55–67) — unchanged, with one added clause

`13.5` survives verbatim, including the standing rule at L65. Add to the end of L65:

````markdown
`13.2.1` is written to instantiate this rule rather than to require it as a side condition: its horizon is a fixed block count, its inclusion rule is predictable, and its denominator is deterministic at every admissible rate (`13.2.3`).
````

---

## 9. Reconciliation with A's and B's drop-ins

Every overlap, and which version wins.

### 9.1 With A

| A's site | overlap | resolution |
|---|---|---|
| A §3.1 `W_{k,D}` | none — `W_{k,D}` unchanged. The cemetery `†` is a **tallied symbol**, not a value of `W_{k,D}`: `W̃_n` is `W_{k,D}(n)` or `†` | **A wins outright**; `W_{k,D}` is untouched |
| A §3.1 alphabet size `2^{k+1}D^3(D+1)` | the tallied alphabet is that **plus one** | A's sentence stands; `13.2.2` and the paper's hypothesis say "together with `†`". No consequence: finite plus one is finite |
| A §3.2 the cap `D` | none | A wins |
| A §3.3 `π_{k,D}` | `π_{k,D}` is extended to the tallied alphabet by `π_{k,D}(†) = 0`. **No value moves** — `†` is not in the range of `W_{k,D}` under `B̂` | A wins; one clause added where `π` is introduced |
| A §3.4 total variation | none — TV on a finite alphabet plus one symbol is still TV | A wins |
| A §3.5 two-sided `B̂` | none | A wins |
| A §3.6 the segment boundary | none. The `O(1)`-block transient argument is unchanged; `O(1/T_N)` still `→ 0` | A wins |
| **A §7.2 (`paper` L243–257) and A §7.4's Hypothesis `13.2.1`** | **direct collision.** A's text has "a cut sequence `X_N → ∞`", "Call block `n` a bulk block if `x_exit(n) > X_N`", "every index bulk", "for every admissible `θ` and `(X_N)`" | **§8.1 and §8.7 win.** A's letter-primary shape, `ℓ_n = (m_{+,n}, s_{n+1})`, `B[w] = Π 2^{-(m_i+r_i)}`, the density-of-starts conclusion and the `L`-word quantifier are all preserved verbatim; what changes is the horizon, the inclusion rule and the denominator, which are my scope and not among A's six fixed objects |
| A §7.4's `13.2.2` | same collision, same resolution | §8.2 wins; A's `π^(ℓ)_{k,D}`, TV and `ℓ = 1` marginal clause preserved |
| A §7.4's segment-boundary paragraph | "`T = ⌈θ log₂ N⌉ → ∞`" still holds | A wins verbatim |
| A §7.4's L34 addendum ("the bound is on the joint law of the whole length-`n` word…") | none | A wins; §8.5 sits alongside it |
| A §7.1 (`paper` L241, the `π_k` paragraph) | none | A wins verbatim |
| **A §7.3 (`paper` L301–304)** | one clause, "first `⌈θ log₂ x⌉` bulk blocks" | §8.10: A's paragraph wins with that clause amended |
| A §7.5 (`13.6.4` and (q1)), §7.6 (L2 status), §7.7 (`itinerary.md`), §7.8 | none | A wins |
| A §4.4 item 3 / §4.5 (the `L ≤ 2` calibration ceiling) | **compounds**: §2 item 2 adds a *second* ceiling, quenched versus annealed | Both must be printed. A's ceiling is on block length; mine is on which statement the pooled runs test. They are independent |

**Nothing of A's is contradicted.** The one place I extend A is the tallied alphabet, and it is an
extension of the *statement's* symbol set, not of A's observable. Flagged here rather than absorbed
because the round exists to stop objects accumulating under one name.

### 9.2 With B

| B's site | overlap | resolution |
|---|---|---|
| B §0, §2.5, §2.6, §3 (S1–S4) — the verdict | none; adopted throughout | B wins. §6.1 gives the conversion a named home rather than reopening it |
| B's S1 (`θ < 1/4` unconditional) | §3(b) **strengthens** it: in exponent time the altitude bound is universal, not density-one. B's exceptional set came from the block→exponent conversion, which the clock removes | Both stand; §8.3 states the universal form and the base case still supplies consistency |
| B's S2 (Inselmann in exponent time) | adopted verbatim as the "protected" clause at `τ < 4.8188…` | B wins |
| B's S3, S4 | adopted; §6.1's table is their consequence | B wins |
| **B §5.1 (`aeh.md` L32)** | **direct collision.** B's replacement keeps the bulk cut and the sentence "Past the digit budget the protected window is still `S_n ≤ …` unconditionally … but that is a bound on consumed exponent, not on block count" | **§8.4 wins.** B's mathematical content is fully preserved and relocated: the elementary altitude argument moves to `13.2.3` (in universal form), the exponent-versus-block-count point becomes the consistency clause, and the "past `1/4` the cut's non-binding is carried by the hypothesis" verdict becomes `13.2.3`'s last display. B's paragraph presumes a cut that §8.4 removes, so the two cannot both stand |
| B §5.2 (`aeh.md` L34 Inselmann clause) | adjacent, compatible | **B wins**; §8.5 replaces different sentences of the same line |
| B §5.3 (`aeh.md` L42, `13.3.2`) | none — `13.3.2` is B's site | **B wins verbatim.** One optional addition: the flagship run sits at `τ ≈ 2.29`, `47 %` of Inselmann's window |
| **B §5.4 (`paper` L273–277)** | **direct collision**, same sentence | **§8.8 wins**, on the same terms as L32: B's content preserved, the cut removed, the two admissibility clauses named |
| B §5.5 (`paper` L296–299), §5.6 (L307–313) | none | B wins verbatim |
| B §5.7, §5.8 (`publication.md`) | none | B wins |
| B §2.7 rider 3 (the `ω_+`/`x_exit` gap, recorded not resolved) | **resolved here** — §6.3, with §4's measurements | B's rider is discharged; its statement that the envelope does not control `ω_+` is confirmed and becomes reason 4 of §6.3 |
| B §7 item 4 ("no number depends on it") | **contradicted by measurement** | §4: the cut binds, the two rules differ on `1,538` visits, and the `s`-marginal moves at the third decimal. B was quoting `aeh.md` L48; the error is L48's |

**Three-way check.** A's §7.2/§7.4 and B's §5.1/§5.4 do **not** collide with each other — A rewrites the
hypothesis environment and L32's paragraph is B's — but both presume the bulk cut, and §8 removes it.
So the apply order is: A's object repairs first, then B's Inselmann corrections, then §8's horizon
replacement, which is the only one of the three that deletes text the other two rely on.

### 9.3 With the parallel Wave 2 delegate (`briefs/v3r3-basecase-density-brief.md`)

That brief assigns the base-case lemma and the exceptional set, and states that this brief owns the clock.
Three points of contact, none of them a conflict, all of which the two findings files should agree on:

1. **Their item (iv) is B's S1, which they are asked to verify.** §3(b) here shows S1's exceptional set
   is an artifact of block time: `log₂ x_exit(n−1) ≥ log₂ x − S_n` holds for **every** start, so in
   exponent time the non-binding of the cut needs no density statement at all. They should verify the
   inequality rather than S1's probabilistic wrapper, and the wrapper survives only where a *block* count
   is wanted.
2. **`{S + 1 ≤ L}` is already an exponent-budget event**, and under §6.1 it is exactly the range
   `τ < 1`. Their base case therefore proves both admissibility clauses at once there — protection by the
   altitude bound, consistency by the cylinder count — which is the cleanest statement of "the base case
   is a theorem for every `θ < 1/4`".
3. **The exceptional set now has a third source**, and their triangular-array bookkeeping should carry it:
   besides the equidistribution failure and the cylinder-count remainder, `13.2.1` under §8.1 admits the
   starts whose tally overflows the budget (`ν(†) > ε`). Below `τ = 1` that set is empty up to the
   cylinder-count remainder they are already tracking; above it, it is the consistency clause and belongs
   to the hypothesis, not to the lemma.

---

## 10. Consequence trace

| # | Item | Verdict | Note |
|---|---|---|---|
| 1 | `13.4`'s reconciliation sentence (L48) | **Fails as written; survives restated** | As written it condemns `13.4`'s own per-orbit cell means, whose denominators are conditional counts gated at `>= 2` (`aeh_calibration.py` L358–372, L400–406). Split into the hypothesis's denominator (deterministic by construction) and an estimator's (deterministic when nothing gates it). §8.6 |
| 2 | `13.4`'s "in these runs neither binds" (L48) | **Fails; the measurement contradicts it** | §4: `2.64 %` of visits and `15.5 %` of orbits under the core cut. Replaced with the measured rates and the direction of the induced bias. §8.6 |
| 3 | `13.4`'s cell numbers (L50) | **Survive** | The censoring moves the `s`-marginal at the third decimal; `0.2533`, `0.5017`, `0.1277` are unaffected at their quoted precision. The `(4,3)` pair cell keeps A's `L = 2` reading |
| 4 | `13.5`'s standing rule (L65) | **Survives verbatim, and is strengthened** | `13.2.1` now instantiates it rather than requiring it. One clause added. §8.11 |
| 5 | `13.5`'s artifact analysis (L63) and Lemma `13.5.1` | **Survive verbatim** | The mechanism is a cut correlated with the dynamics; §1.3 generalizes it from one cell to any altitude threshold, which is a strengthening of `13.5`'s own diagnosis |
| 6 | `13.3.1` (ledger) | **Survives restated** | "first `⌈θ log₂ N⌉` bulk blocks" → "first `⌈θ log₂ N⌉` blocks, all within budget". A's retirement of the `O(2^{-k})` error is unaffected. One gain: the ledger is no longer read off a censored sample (§4 item 3) |
| 7 | `13.3.2` (the `1/3` rate) | **Survives restated** | Same wording change. A's cap error `O(2^{-D})` unaffected |
| 8 | `13.3.2` (the drift non-consequence) | **Survives verbatim** | Untouched. Note in passing that the censored sample of §4 would have *helped* a drift claim by suppressing large `s`; the non-claim is unaffected either way |
| 9 | `13.3.2`'s Inselmann paragraph | **B's §5.3 wins verbatim** | Optional one-clause addition: `τ ≈ 2.29` places the campaign at `47 %` of the cited window |
| 10 | `13.3.3` (scope) | **Survives verbatim** | Nothing here touches density-of-starts, non-iteration or the staircase tails |
| 11 | `13.6.4`'s "visit family … together with a bulk cut" (L113) | **Survives restated** | One clause: "together with a rule selecting which blocks are tallied". The theorem never inspects the family ("the dictionary below is deterministic"), so the proof is untouched |
| 12 | `13.6.4`'s proof, (q1), (q2) | **Survive verbatim** | A's §7.5 governs |
| 13 | `13.6.6`'s "the cut keeps the narrower job of excising the bottom regime" | **Survives restated** | The budget keeps that job. The rest of the remark — including "*some* restriction to the bulk is necessary", which the budget supplies — is unaffected |
| 14 | `13.6.3`(i)(a) "the bulk cut is literally the same on both sides" | **Survives restated** | Becomes the reason the door is the right coordinate (§6.3 reason 2) rather than a statement about a cut the hypothesis has |
| 15 | `13.6.5`'s orbit adjudication (L139) | **Survives; one qualifier** | Its `154,389` bulk visits are `ω_+`-censored (`2.6 %` of visits removed). The discriminating cell `P(ω_+ ≡ 1 mod 3 \| a_+ = 0) = 0.6662` is a conditional on `a_+ = 0`, the coordinate the core cut censors hardest, so the qualifier belongs on the page even though the measured value is `0.3σ` from `2/3` |
| 16 | `paper` L243–257 `hyp:aeh` | **Restated in place** | §8.7 |
| 17 | `paper` L259–277 (A: "unchanged and remains correct") | **Fails from L270** | A's judgement was made before B's verdict; L273–277 is B's site and §8.8's. L259–270 survives verbatim |
| 18 | `paper` L279–299 (base case) | **Survives restated at L286–293** | §8.9. B's §5.5 governs L296–299 |
| 19 | `paper` L301–313 | **A's §7.3 + B's §5.6 win**, one clause amended | §8.10 |
| 20 | `paper` L326–332 (Calibration paragraph) | **Survives; one sentence narrows** | "Bulk uniformity stands unqualified at all tested depths" gains A's `L ≤ 2` and, separately, the pooled-versus-quenched note of §2 item 2 |
| 21 | `experiments/aeh_symbolic.py` L541–544 docstring | **False as written** | "the bulk cut omega > 2^30 never binds within the burn-in + horizon (no survivorship selection at finite size)". It binds on `15.5 %` of orbits. Code fix, phase 2; flagged, not made here |
| 22 | Appendix A commit pin `c2d465a` (`paper` L339) | **Dies on any `aeh.md` edit** | Phase-2 mechanic, as A records |

---

## 11. Is there a proof that the cut is non-binding past `θ = 1/4`? — no, and why not

Asked because the brief requires it to be flagged if found. **It was not found, and there is a structural
reason.**

In block units the required statement is an *upper* bound on `S_n` in terms of `n` — that the first
`θ log₂ N` blocks consume at most `τ log₂ N` of exponent. Unconditionally the available inequalities all
run the other way:

* `S_n ≥ 2n` always (each letter has `m, r ≥ 1`), which bounds the block count above by `Λ_N/2` and says
  nothing about it below;
* B's §2.4, from Inselmann's two-sided envelope: `S = 2K ± εL` where `K` is the Syracuse count, and
  `K_n = Σ_{i<n} m_i` with each `m_i ≤ 2εL + 1`. So `K_n ≤ n(2εL + 1)` — vacuous;
* Inselmann Thm 1.6 controls the density of the one-letter parity pattern `1`, which is `E[s]` in Cesàro
  form. It gives no upper bound on `Σ m_i`.

So the missing object is a Cesàro upper bound on the exponent per block, i.e. `E[m + r] ≤ 4`, which is
B's §2.5 circle: available unconditionally only from Terras's cylinder count, whose range is `τ < 1`.
**In exponent time the question does not arise**, which is the whole point of the clock — and that is why
the design puts the conversion inside the hypothesis rather than trying to prove it.

One thing genuinely gained, recorded so it is not mistaken for a proof of anything larger: §3(b) upgrades
B's S1 from natural density one to **every start**, and it does so with a one-line argument. That is an
improvement in the *kind* of statement, not in its range.

---

## 12. Open questions

1. **Whether `τ` and `θ` should both be quantified, or `θ` fixed as `τ/4` with a slack.** §7 recommends
   quantifying both with the consistency clause relating them, because that keeps the conversion visible.
   The alternative — define `T_N := ⌈(1−δ)Λ_N/4⌉` and quantify over `(τ, δ)` — is one symbol cheaper and
   prints the `4` in the definition of the horizon instead of in the admissibility clause. I did not find
   a decisive argument; the author's taste should settle it.
2. **The upper edge of "protected".** `τ < 4.8188…` is protected and `τ ≥ 4.8188…` is not. What happens
   *at* the endpoint depends on Inselmann's `ε`, and I did not chase the uniformity. Nothing on the page
   needs the endpoint.
3. **Whether the cemetery clause should be stated with a strict or non-strict budget.** I used
   `S_n < Λ_N` (predictable, strict). `S_{n+1} ≤ Λ_N` would tally the block that straddles the budget.
   The difference is one block in `T_N` and vanishes; I chose predictability.
4. **Whether the `ω_+` cut has ever mattered to a recorded number.** §4 measures the induced bias at the
   third decimal in the `s`-marginal for the flagship run. I did not re-run the eight
   `aeh_calibration.py` rounds under the door cut, so the `13.4` cell values at L50 are checked for
   *plausible* insensitivity, not verified insensitive. That is a one-run item for the apply phase.
5. **The quenched form is untested.** §2 item 2. Measuring it needs the distribution across orbits of
   `‖ν(x) − π_{k,D}‖_TV`, which is a new statistic, not a re-analysis. Whether the author wants that
   before or after the restatement is a scheduling question.
6. **`13.6.5`'s adjudication cells under the core cut** (trace item 15). The measured `0.6662 ± 0.0015`
   is `0.3σ` from `2/3` and `112σ` from `1/2`, so no conclusion is at risk; but the cell conditions on
   `a_+ = 0` and the core cut censors `a_+`, so the cleanest fix is to re-run that one check under the
   door cut or the budget. Not done here.
7. **Whether "protected" should be defined with `x_exit` or with the state's own core.** I settled it for
   the door (§6.3), and the argument is complete for the hypothesis. Whether any *consequence* elsewhere
   in the repository silently needs a core bound I did not audit beyond `13.3` and `13.6`.

---

## 13. Verification table — every number and quotation read or computed, not recalled

| Item | Source |
|---|---|
| `13.2.1`'s text: "unweighted empirical distribution … over the **bulk visits** among the first `T = ⌈θ log₂ N⌉` — those with `x_exit > X_N` — each qualifying visit counted once, with no per-orbit reweighting"; "for every admissible `θ` and `(X_N)`" | `aeh.md` L30 |
| "For `θ < 1/β`, `β = 2(2 − log₂3) = 0.8301…`, the cut binds on a vanishing density of starts, the tally denominator is the deterministic `⌈θ log₂ N⌉`" | `aeh.md` L32 |
| base case `S = Σ(m_i + r_i)`; `TV(Law(W_n), B^{⊗n}) ≤ P_B(S_n ≥ L)`; "theorem for every `θ < 1/4`"; `1/β = 1.2047…`; "`2.29 ×` the budget, with `23` of its `30` tallied blocks beyond it" | `aeh.md` L34 |
| `13.3.1`'s "first `⌈θ log₂ N⌉` bulk blocks" | `aeh.md` L40 |
| "a per-orbit mean is safe exactly when its denominator is deterministic … unsafe when the denominator is the random count of qualifying visits"; "the statements cut on `x_exit > X` while the code cuts on the core, `ω_+ > X` (`aeh_calibration.py` L361/L402, `aeh_symbolic.py` L566)"; "in these runs neither binds, so no number below depends on the choice"; `x_exit + 1 = 2^(m_+)3^(a_+)ω_+` | `aeh.md` L48 |
| cell values `0.2533`, `0.5017`, `0.1277` vs `0.128` | `aeh.md` L50 |
| `λ₂` used for a transfer-matrix eigenvalue (so `λ` is not free) | `aeh.md` L53 |
| `13.5`'s artifact: "took per-orbit *ratios* over each orbit's qualifying visits, with early stopping"; the standing rule "fixed-horizon, unweighted, per-visit sampling … Ratio estimators over correlated visit sequences are forbidden" | `aeh.md` L63, L65 |
| `E[m] = 2`, `P(m = j) = P(r = j) = 2^{-j}` | `aeh.md` L75 (`13.6.1`) |
| "letter `n` occupies exactly `m_n` raw `T`-steps (`G = T^m`)"; "The bulk cut is literally the same on both sides: the visit datum `x_exit` **is** the door `y_n`" | `aeh.md` L94 (`13.6.3`(i)) |
| `13.6.4`'s "visit family … together with a bulk cut"; "the dictionary below is deterministic and never inspects the family" | `aeh.md` L113 |
| orbit adjudication: `154,389` bulk visits, seed `31005`, `P(ω_+ ≡ 1 mod 3 \| a_+ = 0) = 0.6662 ± 0.0015` | `aeh.md` L139 |
| `13.6.6`: "the cut keeps the narrower job of excising the bottom regime"; "*some* restriction to the bulk is necessary" | `aeh.md` L143 |
| `T(x) = (3x+1)/2^{v_2(3x+1)}` — the paper's `T` is odd-to-odd | `paper` L50 |
| `def:reduced`: `A = 3^dω − 1`, `s = v_2(A)`, `x_exit = A/2^s`, `m_+ = σ − s`, `d_+ = m_+ + a_+` | `paper` L64–67 |
| `prop:block`(i)–(ii): the next `m − 1` iterates, then `T(x_{m−1}) = A/2^s` | `paper` L70–80 |
| "the empirical distribution … **restricted to** the bulk visits … each qualifying visit counted once and no visit reweighted by the orbit it came from"; "for every admissible `θ` and `(X_N)`" | `paper` L247–256 |
| "for $\theta < 1/\beta$ … the cut binds on a vanishing density of starts and the tally denominator is the deterministic $\lceil\theta\log_2 N\rceil$" | `paper` L272–277 |
| "$S$ accumulates at mean rate $4$ per block — the $\sigma \approx 4.0$ of Heuristic~\ref{prop:budget}, exactly $2+2$"; "a theorem for every horizon rate $\theta < 1/4$"; "$1/\beta = 1.2047\ldots$ blocks per bit, some $4.8$ times as long" | `paper` L286–290 |
| "all but a set of starting values of natural density zero carry those frequencies along their first $\lceil\theta\log_2 x\rceil$ bulk blocks" | `paper` L301–304 |
| macros `\Z`, `\vt`, `\vth`, `\w`, `\wnext`, `\dnext`, `\LL`; `\tau`, `\Lambda`, `\lambda`, `\dagger` all unused | `paper` L17–23; grep |
| cut on the core: `big = w > CUT` | `aeh_calibration.py` **L360** (L48 cites L361, which is the `use =` line one below) |
| cut on the core, `2^40` recheck: `if w > CUT and w % 8 == 1 and d == 1`; per-orbit ratio `num/den` gated `if den >= 2` | `aeh_calibration.py` L402, L403, L406 |
| cut on the core: `if w1 > CUT` | `aeh_symbolic.py` **L566** (exact) |
| flagship protocol `seed=31005, NORB=8000, BURN=10, HOR=30, CUT=1 << 30`, starts `[2^70, 2^71)` | `aeh_symbolic.py` L539, L555 |
| docstring "the bulk cut omega > 2^30 never binds within the burn-in + horizon" | `aeh_symbolic.py` L541–544 |
| pooled counters `nvis`, `letter_hist`, `dhist`, `mod3_cond`; `per_orbit_w3` gated `if o_w3[0] > 10` (L582–583) and used only for the SE (L604–605) | `aeh_symbolic.py` L567–583, L604–605 |
| per-orbit cell gate `if h[kk][0] >= 2` and the mean/SE over per-orbit ratios | `aeh_calibration.py` L371–372, L380–381 |
| **replication**: `5,286` orbits, `158,580` attempted visits, `154,389` bulk (`ω_+`), `4,191` below (`2.64 %`), `15.5 %` of orbits bind; `155,927` bulk (door), `2,653` below (`1.67 %`), `8.9 %` of orbits; `Q_N ∈ [8, 30]`, no `Q_N = 0`; exponent `120.05` over `30` blocks = `4.0017`/block | this session, standalone re-implementation of `check_orbit_texture` using its own `F_step`; reproduces `aeh.md` L139's `154,389` exactly |
| **replication**: mean `s` = `1.9999` / `1.9930` (door) / `1.9871` (core) / `1.9999` (budget at `τ = 2.29`); `P(s=1)` = `0.50069 / 0.50225 / 0.50432 / 0.50069`; `P(s ≥ 6)` = `0.03118 / 0.03055 / 0.03012 / 0.03118` | same run |
| `log₂3 = 1.584962500721156`; `log₂√3 = 0.792481250360578`; `(1 − log₂√3)^{-1} = 4.818841679306416`; `(log₂(4/3))^{-1} = 2.4094208396532095`; `β = 0.8300749985576878`; `1/β = 1.204710419826604`; `4/β = 4.818841679306416`; `4.818841679306416/4 = 1.204710419826604`; `160/70 = 2.2857…`; `2.29/4.8188… = 0.475` | computed this session in double precision |
| Inselmann Thm 1.1, Thm 1.6, Thm 1.10, Cor. 1.4, his `T(m) = m/2` or `(3m+1)/2`, Thm 3.8 eq. (3.20) | `briefs/v3r3-inselmann-horizon-findings.md` §1.1–§1.7 (transcribed from the source by delegate B; not re-read here) |
| A's `W_{k,D}`, cap `D`, `π_{k,D}`, TV, `B̂`, the segment boundary, alphabet bound `2^{k+1}D^3(D+1)` | `briefs/v3r3-aeh-object-findings.md` §3, §7 |
| round 2's parked item 4 ("for `θ ≥ 1/β` … a formulation that is clean *and* covers `θ ≥ 1/β` with a deterministic denominator eluded me") | `briefs/v3r2-aeh-formulation-findings.md` §9 item 4, as quoted in the brief |
