# Findings: one object named AEH (v3 round 3, both blocking findings)

**Task:** `briefs/v3r3-aeh-object-brief.md`. Read-only round; the only file written is this one.
**Read at:** `main` = `dc61306`, working tree clean.
**Scope note:** the recommendation is a recommendation. The author decides at review. Both options are
costed and both carry drop-in text.

---

## 0. Verdict in one paragraph

Both blocking findings are correct as matters of fact, and they are one defect with one repair. The
repository names **one** hypothesis and **states** three different ones, because the word "window"
denotes three different objects and the word "product law" denotes two different independence claims.
The reviewer's site count is low: **nine** places assert that AEH *is* Bernoulli genericity, not three
(`aeh.md` L2, L8, L36, L71, L143, L145; `itinerary.md` L73; `bridge.md` L69; `HANDOFF.md` L20), while
exactly one place — `aeh.md` L125, qualifier (q1) — says it is the `L = 1` case. That asymmetry is the
main cost input, and it points hard at **Option 1**: strengthen `13.2.1` to all finite `L`, in letter
coordinates, so that nine sentences become true where they stand and one qualifier changes role. The
second decisive input is that the record's own unconditional base case (`aeh.md` L34) already proves
the **strengthened** form — it bounds `TV(Law(W_n), B^{⊗n})`, the joint law of the whole length-`n`
word — so retaining the weaker hypothesis buys no wider provable range. Three sentences fail as
written and are repaired here: `13.2`'s "the cap does one job, keeping the window alphabet finite"
(the labels `(s, σ, a_+)` that `13.6.3`(iii) puts in the same object are unbounded, so the cap must cap
them too); `13.6.4`'s definition of *bulk-equidistributed* ("bulk frequencies given by the product law
of `13.6.3`(v)" — a single-visit law does not determine `L`-block frequencies, and the theorem's own
`(⇐)` direction quietly uses the `L`-block law); and `13.6.3`(v)'s "Under Haar-odd (equivalently `B`)"
(the absorption `a_{n+1} = v_3(y_n+1)` is not a function on odd `Z_2` at all — it needs the `3`-adic
past-limit, hence the two-sided extension). The probability space should be the two-sided `B̂`, and the
reason is sharper than the reviewer's: under `B̂` the reconstruction of `13.6.3`(iii) is exact almost
surely, so **the exceptional event disappears from the definition of the law** and survives only in the
finite-past estimate. **The depth-marginal values do not move** — verified, not assumed, in §10. And the
record does invite the product-law misreading, in the status header and in `13.6.4`'s own definition,
while containing its own refutation two sections earlier (`13.2`'s class chain has *deterministic*
transitions).

---

## 1. Verified site inventory

Every line number below was read at `dc61306`.

### 1.1 Sites asserting that AEH *is* Bernoulli genericity (nine, not three)

| # | Site | Text (verified) |
|---|---|---|
| 1 | `aeh.md` L2 (status front matter) | "symbolic form NAMED and PROVED as an equivalence (13.6, the genericity form)" |
| 2 | `aeh.md` L8 ("Current state") | "AEH is precisely the assertion that the integers — a Haar-null set — inherit that genericity at scale, with the equivalence proved through the seam dictionary" |
| 3 | `aeh.md` L36 (§13.2, supporting facts) | "A symbolic form of the hypothesis is recorded at itinerary.md `14.15.2`: AEH is precisely the statement that the stratum words of the bulk segments of uniformly sampled starting values (`13.2.1`) equidistribute against the itinerary cylinder measure." |
| 4 | `aeh.md` L71 (§13.6 opening) | "is here upgraded to a proved, named equivalence: AEH is the assertion that integer orbits are *generic points* of an explicitly identified Bernoulli system" |
| 5 | `aeh.md` L143 (`13.6.6`) | "The genericity form therefore exhibits AEH as the assertion that **this particular null set inherits genericity at scale**"; and "the forward escape's missing statistical half is bulk `B`-genericity of the integers' letter words" |
| 6 | `aeh.md` L145 (`13.6.7`) | "(1) **AEH's genericity form** (`13.6`): an *orbit-statistics* statement — the letter words of integer orbits are bulk-generic for the Bernoulli law `B`" |
| 7 | `itinerary.md` L73 | "AEH is thereby *precisely* the statement that the stratum words … equidistribute against the cylinder measure — an equivalence named and proved at aeh.md `13.6`" |
| 8 | `bridge.md` L69 (`16.4.3`) | "its symbolic name is the genericity form (aeh.md 13.6): bulk Bernoulli-genericity of the integers' door letter words" |
| 9 | `HANDOFF.md` L20 | "the symbolic form is now a named, proved equivalence (the genericity form, aeh.md 13.6)" |

### 1.2 The one site that says otherwise

`aeh.md` L125, qualifier **(q1)**: "Hypothesis `13.2.1` as literally stated is the `L = 1` case … The
converse from the literal single-visit form is **obstructed, precisely**: the absorption sequence is
`2`-adically invisible … AEH's process (block) form — the form the calibration record has in fact
always measured (`13.4` measures consecutive pairs) — is the form equivalent to genericity."

**Adjudication.** The reviewer and (q1) are right and the nine sites are wrong *about the literal
`13.2.1`*. `13.2.1` (L30) asks for "the unweighted empirical distribution of the depth-`k` window
states over the **bulk visits**" — the empirical measure of *single* states, i.e. the `L = 1` marginal.
Nothing in it quantifies over consecutive blocks. Theorem `13.6.4` is genuinely an equivalence, but
between *bulk-genericity* and the **process** form; the elision is between `13.6.4`'s left-hand object
and `13.2.1`.

**One nuance in the record's favour**, worth recording so the apply phase does not over-edit: site 1
(the front matter) says "symbolic form … PROVED as an equivalence", and `13.6.4` *is* an equivalence.
Read strictly, site 1 alone is defensible. Sites 2, 3, 4, 5, 7, 8 are not: each names `AEH` (or
`13.2.1` explicitly, at site 3) as the thing that is equivalent to genericity.

### 1.3 The paper does not carry the defect

Grepped `paper/collatz-reduced-v3.tex` for `generic|equivalence|equidistribut`: §5 (L239–332) never
calls AEH a genericity statement and never claims an equivalence. The only occurrence of "genericity"
is L58, "the $2$-adic conjugacy … underlies all Haar-genericity heuristics", which is about the
classical literature. **Blocking finding 1 is a wiki defect, not a paper defect.** The paper's §5 does
carry blocking finding 2 (undefined norm at L253; `\pi_k` with no visible cap dependence at L241).

---

## 2. The three objects, verified — and where the reviewer is right and wrong

| Location | Object, as actually written |
|---|---|
| `paper` L159–161 (`thm:onestep`), = `stage4.md` L100–106 (`11.8.7.6`) | `ω mod 2^{σ+k+2}`, `d mod 2^{σ+k}`, **plus exact labels `(s, σ, a_+)`**. Residue depth is state-dependent; `σ` and `a_+` unbounded. **Countably infinite alphabet.** Decides the next step. |
| `aeh.md` L20 (`13.2`) | `(ω mod 2^{k+2}, min(d, D_k))` "together with validity data", **asserted finite**. |
| `aeh.md` L98 (`13.6.3`(iii)) | The `13.2` window "with its stratum labels `(s, σ, a_+)` per stage4.md `11.8.7.6`, **the reading of `13.2`'s 'validity data'**". |

**The dilemma is sound.** `13.2` L20 says "The cap does one job, keeping the window alphabet finite";
`13.6.3`(iii) L98 says the "validity data" *is* `(s, σ, a_+)`. `σ = s + m_+` and `a_+ = v_3(C)` are
unbounded (`13.6.1`: `P(m = j) = P(r = j) = 2^{−j}`; `13.6.3`(iv): `P_B(a ≥ j) ≤ 2·(0.93)^j`, positive
for every `j`). So the alphabet is infinite and the finiteness sentence is false. Conversely, dropping
the labels loses the trichotomy: `11.8.7.6.1`'s proof needs `d_+ = (σ − s) + a_+` "exact from the
labels" (`stage4.md` L114), and needs residues to depth `σ + k + 2`, which `ω mod 2^{k+2}` does not
supply at any fixed `k`. **Both horns are real; the reviewer's dilemma holds.**

Grep results confirming the two smaller gaps:

* **The norm.** `‖` occurs in `aeh.md` exactly once, at L30, inside `13.2.1`. It is never defined
  anywhere in the repository. `paper` L253 has `\lVert \nu_{k,N}(x) - \pi_k \rVert` likewise
  undefined. Total variation occurs in `aeh.md` exactly once, at L34, as `TV(Law(W_n), B^{⊗n})` — a
  distance between *word laws* in the base case, never tied to `13.2.1`'s norm. **Reviewer correct.**
* **`π_k`'s hidden cap dependence.** Confirmed: the window state carries `min(d, D_k)`, so its law is a
  pushforward through the cap, and `π_k` is written throughout `aeh.md` and the paper. **Reviewer
  correct.**

**Where the brief is wrong.** The brief states flatly that "`D_k` itself is never defined in the
repository". That was true at round 2's read (`e4dac49`) and is **no longer true** at `dc61306`:
`aeh.md` L20 now opens "Fix a depth `k` and a **depth cap** `D_k` — any finite cutoff, fixed once
together with `k`", and adds the constraint "whenever `D_k ≤ W`". So `D_k` *is* introduced, as a free
parameter quantified with `k`. What is still missing is (a) that this is a *second* parameter and the
law depends on it, invisibly in the notation `π_k`, and (b) any statement of whether `D_k` is a
function of `k` (the subscript says yes; the prose "any finite cutoff" says no). The repair is
notational, not a missing definition. Round 2's unsettled item 5 was **partially discharged** by the
round-2 apply phase; the brief and the reviewer both read the older text.

---

## 3. The definitions block (identical under both options)

### 3.1 The observable `W_{k,D}`

For a visit `n` of an `F`-orbit with state `(ω_n, d_n)`, write `A_n = 3^{d_n}ω_n − 1`,
`s_n = v_2(A_n)`, `C_n = A_n + 2^{s_n}`, `σ_n = v_2(C_n)`, `a_{+,n} = v_3(C_n)` (spine/stage3
notation, unchanged). Fix two integers `k ≥ 1` and `D ≥ 1`. Define

```text
W_{k,D}(n) := ( ω_n mod 2^(k+2),  min(d_n, D),  min(s_n, D),  min(σ_n, D),  min(a_{+,n}, D) ).
```

* **Are the labels in it?** Yes — **capped**, not excluded and not exact. Capping is what makes the
  alphabet finite, and it is required: the labels are what `13.6.4`'s `(⇐)` direction reads the letters
  off (`letter n = (σ_n − s_n, s_{n+1})`, L121), what `13.3.1`'s ledger is the marginal of, and what
  `13.6.3`(iii) already calls "the reading of `13.2`'s 'validity data'".
* **Alphabet size:** at most `2^{k+1} · D · D · D · (D+1)` — finite. (`ω` is odd, so `2^{k+1}` residues;
  `d, s, σ ∈ {1,…,D}` after capping; `a_+ ∈ {0,…,D}`.)
* **"Validity data" is retired as a phrase.** It appears exactly twice in the repository (`aeh.md`
  L20, L98) and names nothing definite. The five coordinates above replace it.
* **`W_{k,D}` is defined at every visit of every orbit**, from the state and its own step, with no
  reference to any past. The past enters only in identifying its *law*.
* **Redundancy, stated so it is not mistaken for independence:** `s_n`, `σ_n`, `a_{+,n}` are exact
  functions of the *full* state `(ω_n, d_n)`. They are **not** functions of `(ω_n mod 2^{k+2},
  min(d_n,D))`, which is why they carry information. In particular `s_n` is **not** independent of the
  `ω`-residue under `π_{k,D}`; `13.6.3`(v) claims independence of the residue from the *depth* only,
  and that is all it proves.

### 3.2 The cap `D`

**`D` is a free integer parameter, chosen with `k` and quantified universally alongside it.** It is not
determined by `k`. The record's symbol `D_k` should be read as "the cap in force at depth `k`", and the
subscript dropped in favour of the explicit second index on the law. Nothing in any consequence
depends on the choice, because every statement quantifies over all `(k, D)`; the `k`-indexed diagonal
of `13.3.1` becomes a `(k, D)`-indexed diagonal.

*If the author wants one printed value:* `D = k + 2` is the natural pairing — the cap then resolves the
depth to the same precision `2^{k+2}` resolves the core. Nothing rests on it.

*One constraint, already on the page:* `13.6.3`(iii)'s finite-past reconstruction needs a letter
past-window `W ≥ D`. `W` is free there and quantified separately, so this constrains nothing; it is
recorded so the two parameters are not confused.

### 3.3 The law `π_{k,D}`

```text
π_{k,D}  :=  the law of W_{k,D}(0) under B̂,
             i.e. the pushforward of B̂ by the reconstruction map of 13.6.3(iii).
```

Its two proved *within-state* product clauses are `13.6.3`(v) verbatim: the `ω`-residue is Haar-uniform
over the `2^{k+1}` odd residues mod `2^{k+2}` and independent of the depth (indeed of the whole past);
and `d = m + a` with `m` geometric(1/2) independent of `a`, the law of `a` being `13.6.5`'s. **That is
the whole of what "product" means.** `π_{k,D}` is not a product across its five coordinates (see §3.1),
and the process `(W_{k,D}(n))_n` is not a product across time (§11).

The `L`-block law is written `π^{(L)}_{k,D}` — the law of `(W_{k,D}(0), …, W_{k,D}(L−1))` under `B̂`,
which is shift-invariant. `π^{(1)}_{k,D} = π_{k,D}`.

### 3.4 The norm

* On the **finite** window alphabet: **total variation**,
  `‖ν − π‖_TV := ½ Σ_w |ν(w) − π(w)| = max_A |ν(A) − π(A)|`. On a finite alphabet TV is equivalent to
  every other reasonable choice up to alphabet-size constants, and `k, D, L` are fixed before `ε`, so
  the choice is immaterial — say so once and stop.
* On the **countable** letter alphabet (the letter form of the hypothesis): **cellwise**, i.e. one `ε`
  per finite word. This is what "generic point" means, it is what `13.6.4`'s proof uses ("every finite
  letter pattern … has bulk frequency equal to its `B`-probability", L113), and it is strictly weaker
  than TV on an infinite alphabet — hence the safer statement.

Choosing TV also closes a live seam: `13.2`'s base case (L34) is stated in TV and `13.2.1` in an
undefined `‖·‖`. After this they speak one language.

### 3.5 The probability space: two-sided `B̂`

```text
B̂  :=  ⊗_{i ∈ Z} ( geom(1/2) × geom(1/2) )   on   {(m,r) : m,r ≥ 1}^Z,   with the shift.
```

**Four reasons, all checked against the page.**

1. `a_{n+1} := v_3(y_n + 1)` is **not a function on odd `Z_2`**. `13.6.2` identifies `(odd Z_2, Haar,
   G)` with the *one-sided* shift `({(m,r)}^N, B)`; a `2`-adic point has no `3`-adic valuation. The
   absorption exists only through the past-letter offset formula (`13.6.3`(iii)) or, exactly, through
   the `3`-adic past-limit `y_3` (`itinerary.md` `14.15.3.3`). So `13.6.3`(v)'s "Under Haar-odd
   (equivalently `B`)" and `13.6.5`'s "Under `B`" are both compressed past the point of correctness.
   The reviewer is right, and the reason is stronger than stated.
2. **The exceptional event disappears.** `13.6.3`(iii) reconstructs the `ω`-residue only off the event
   `{a ≥ W}` for a finite past-window `W`. Under `B̂` the past is infinite and `a < ∞` almost surely
   (`P_B(a ≥ j) ≤ 2·(0.93)^j`, `13.6.3`(iv)), so `W_{k,D}` is a `B̂`-a.s.-defined function of the
   bi-infinite letter sequence and `π_{k,D}` needs no exceptional-set caveat at all. The
   `2L(0.93)^W` error survives exactly where it belongs — in the finite-past *estimate* used by
   `13.6.4`'s `(⇒)` direction.
3. **Stationarity becomes literal.** Under `B̂` the process `(W_{k,D}(n))_{n∈Z}` is shift-stationary
   and its law at every index is `π_{k,D}`. Under one-sided `B` it is only asymptotically so.
4. **Nothing classical is disturbed.** `B̂` is the natural extension of the one-sided shift of
   `13.6.2`; `13.6.2` itself is untouched, and remains the statement that `(odd Z_2, Haar, G)` is the
   one-sided factor.

### 3.6 The segment boundary — answered, not left implicit

An integer orbit segment has no infinite past at its first visit. Three statements settle it, in order
of decreasing obviousness:

1. **The observable is never undefined.** `W_{k,D}(n)` is computed from `(ω_n, d_n)` and that state's
   own step. Only the *reconstruction from letters* needs a past, and the hypothesis does not
   reconstruct anything.
2. **The transient is real, and quantified.** For a uniform odd start `x`, `a = v_3(x+1)` has
   `P(a = j) = 2·3^{−(j+1)}`, i.e. `(2/3, 2/9, 2/27, …)`; the bulk law is `(2/3, 19/63, 2/63, …)`. They
   agree at `a = 0` and differ at `a = 1` (`0.2222` vs `0.3016`). The mechanism is `13.6.5`'s own: a
   uniform integer is `≡ 0 mod 3` a third of the time, a door never is. One `G`-step fixes the support;
   the remainder relaxes geometrically by `13.6.3`(iv).
3. **It costs nothing in the statement.** The deviation is confined to the first `O(1)` visits of each
   segment while the tally runs to `T_N = ⌈θ log₂ N⌉ → ∞`, so its contribution to any empirical
   frequency is `O(1/T_N) → 0`. **No burn-in parameter is needed in the hypothesis.** The burn-in of
   `10` in `experiments/aeh_symbolic.py` L539 is a finite-size device, exactly as round 2 recorded
   (`v3r2-aeh-formulation-findings.md` L72).

*Available variant, not recommended:* add a burn-in `b_N → ∞` with `b_N = o(T_N)`. Cleaner-looking, one
more quantifier, no change to what is asserted.

### 3.7 The paper's Theorem 3.8 window stays where it is

`thm:onestep`'s labelled window is **not** to be moved. The v3 Version note (paper L42) records its
current form as one of the eight v3 repairs — "Theorem~\ref{thm:onestep} states its depth-$k$ window as
the residues of Theorem~\ref{thm:deltaM} \emph{together with} the stratum labels $(s,\sigma,a_+)$,
matching its own proof" — and reverting it would falsify that note and re-break the proof. It remains a
**separate, countable** object. What is added is one sentence in §5 saying so (§7.1 below).

---

## 4. Option 1 — strengthen to all finite `L`, letter coordinates primary

### 4.1 The statement

Two sub-variants, equivalent by `13.6.4`:

* **1a (recommended): letters primary.** AEH asserts bulk-genericity of the letter word for `B`; every
  window statement is a corollary.
* **1b: windows primary.** AEH asserts, for every `k, D, L`, that the `L`-block window frequencies
  converge to `π^{(L)}_{k,D}`; letter genericity is the corollary.

1a is preferred because (i) the alphabet/cap question does not arise in the primary statement at all,
(ii) the base case (`13.2` L34) is *literally* a letter statement, and (iii) the paper can state it
without new machinery: the letter at block `n` is `(m_{+,n}, s_{n+1})`, and both symbols are already
defined in `def:reduced` (`σ = s + m_+`). The re-pairing is `reverse.md` `14.14.6` verbatim; genericity
for `(ℓ_n)` and for the block-label sequence `(s_n, m_{+,n})` are the same statement with a one-index
offset, irrelevant to Cesàro limits by `13.6.3`(i).

Full drop-in text at §7.

### 4.2 What becomes of `13.6.4` and of (q1)

* `13.6.4` becomes an equivalence **with AEH itself**, which is what §13.6's title has always claimed.
  Its proof is untouched. Its *definition* of "bulk-equidistributed" must be repaired (§9, item 6) —
  that repair is required under both options and is not a cost of this one.
* **(q1) changes role, and stays on the page.** It stops being a qualifier on the identification and
  becomes the statement of *why the hypothesis is stated at all `L`*: the `L = 1` case is strictly
  weaker, the converse is obstructed for an exact reason (the absorption sequence is `2`-adically
  invisible; `a_{+,n+1}` is not a function of any depth-`k` window at visit `n`, at any `k`), and the
  graded correspondence `L`-letter ↔ `(L+1)`-window-block is exact. Every word of its mathematics
  survives; only its framing sentence ("Hypothesis `13.2.1` as literally stated is the `L = 1` case")
  is replaced by a pointer to the appended `13.2.2`, which now *is* the `L = 1` marginal, named.
* A new appended anchor **`13.2.2`** carries the window form. No renumbering.

### 4.3 What the paper's Hypothesis 5.1 becomes

The letter form, stated in the paper's own symbols (§7.1). The `π_k` paragraph (L241) gains: the second
parameter and the notation `π_{k,D}`; the norm; and one sentence separating `thm:onestep`'s window from
the §5 observable. `thm:onestep` itself is unchanged.

### 4.4 The cost

**Newly claimed:** all finite-`L` letter-block frequencies, where previously only `L = 1` window-state
frequencies were asserted. Strictly stronger, by (q1)'s obstruction.

**No longer claimed:** nothing. Every consequence of the old statement is a consequence of the new one.

**Does any consequence weaken?** Not by strengthening the hypothesis. Four things weaken for *other*
reasons, listed unhedged:

1. `13.3.1`'s "error `O(2^-k)`" is **retired as the ledger's error**. Once `s` is a coordinate of the
   observable, the `s`-marginal *is* the ledger — exactly, at every `j < D` — and no trichotomy is
   invoked. The `O(2^{-k})` priced a *prediction* step (`s_+` from the residues) that the hypothesis
   does not require. What survives with an error term is the predictive statement, which belongs to
   `11.8.7.6.1` and not to AEH. This is a loss of apparent derivational content, not of conclusion.
2. The ledger and the `1/3` rate acquire a **cap error `O(2^{−D})`** in place of `O(2^{−k})`: mass
   beyond the cap sits in one cell whose parity split is unknown. Both are exact along the `(k,D) → ∞`
   diagonal. Previously the `1/3` was written as exact with no cap error at all.
3. **The calibration claim weakens in the `L` dimension.** "Bulk uniformity confirmed UNQUALIFIED at
   all tested depths" (L2) is about `k` and cells. The campaign tests `L = 1` and `L = 2` and nothing
   above (§4.5). Under Option 1 that ceiling becomes visible and must be printed.
4. **AEH is now more than the consequences need.** `13.3.1` and `13.3.2` use only the `L = 1` marginal.
   Minimality is preserved by recording it *per consequence* (each cites `13.2.2`) rather than by
   splitting the hypothesis — which is Option 2's whole design.

**Editing cost.** Nine "genericity" sites (§1.1) become true **where they stand**; only site 3
(`aeh.md` L36) needs a light touch because it names `13.2.1` explicitly and can now say so without
qualification. `13.6.4`, `13.6.6`, `13.6.7`, `itinerary.md` L73, `bridge.md` L69, `HANDOFF.md` L20:
untouched in substance.

### 4.5 How the calibration record reads against it

The campaign has always measured `L = 2`. Verified:

* `experiments/aeh_calibration.py` L368: `if use and prev == 4: h["pair43"][0] += 1; h["pair43"][1] += (k == 3)`
  — this is `P(s' = 3 | s = 4)`, tallied per orbit, against the null `0.128` (L374), which the comment
  at L332 identifies as the *measured* unconditional `P(s'=3)` ("`P(s'=3)` unconditional ~ 0.125-0.131;
  use orbit marginal measured separately"). That is `aeh.md` L50's "consecutive-pair cell `(s, s') =
  (4,3)` at `0.1277` vs independent prediction `0.128` (`-0.1σ`)" — a genuine two-block independence
  test. Under `B`, `s_n = r_{n−1}` and `s_{n+1} = r_n` are independent, so the null is `2^{−3}` and the
  test is exactly a test of `L = 2` genericity.
* `experiments/aeh_calibration.py` L28/36/43–48: `pair_s` and an explicit "s-pair dependence" screen
  with the printed verdict "s-sequence looks i.i.d. under uniform measure"; L61/70/76–81 the same on
  real orbits; L37 `ctrans` tallies class *transitions*.
* `experiments/aeh_symbolic.py` L570–571 `pair_hist`, and L597–599 the check "consecutive-letter
  independence: `P((1,1),(1,1))` vs `P(1,1)^2` within 5%" — a letter-level `L = 2` test.

**Verdict.** Under Option 1 the campaign is evidence **for the hypothesis as newly stated, at `L ≤ 2`,
and silent above.** It is not evidence for something weaker; a substantial part of it is currently
evidence for something the literal `13.2.1` does not assert. The honest calibration sentence is: every
tested cell, every tested depth, block length `L ≤ 2`.

---

## 5. Option 2 — retain the single-visit form, demote genericity to a named stronger hypothesis

### 5.1 The statement

`13.2.1` stays the `L = 1` ensemble statement, with the object repairs of §3 applied (capped window,
`π_{k,D}`, TV, `B̂`). A new appended anchor **`13.2.2`** names the process form:

> **Hypothesis 13.2.2 (AEH-P, the process form).** Same sampling; for every `k`, `D` and `L`, the
> `L`-blocks of consecutive capped windows have bulk frequencies `π^{(L)}_{k,D}`. Equivalently
> (`13.6.4`), the letter word is bulk-generic for `B`. **AEH-P ⇒ AEH; the converse is obstructed
> ((q1)).**

Paper label `hyp:aehp` alongside `hyp:aeh`.

### 5.2 What becomes of `13.6.4` and of (q1)

* `13.6.4` becomes an equivalence between **AEH-P** and bulk-genericity. Proof untouched; the same
  definitional repair of "bulk-equidistributed" is required.
* **(q1) is promoted from qualifier to load-bearing statement**: it is the proof that the two named
  hypotheses are distinct, and it is cited everywhere the record previously said "equivalence".

### 5.3 What the paper's Hypothesis 5.1 becomes

`hyp:aeh` keeps its shape, with the object repairs. §5 gains a second hypothesis environment
(`hyp:aehp`) or a remark naming it, because §5 currently states the *only* content the paper claims for
AEH is distributional — and the block content is part of that.

### 5.4 The cost

**Newly claimed:** nothing.

**No longer claimed:** the nine sites of §1.1. Each must be re-pointed at AEH-P. That includes two
pages outside `aeh.md` (`itinerary.md`, `bridge.md`), one operational file (`HANDOFF.md`), and the
front matter.

**Weakenings** 1–3 of §4.4 apply verbatim here too — they are consequences of the *object* repair, not
of the choice.

**The specific cost of Option 2 is that the repository carries two hypotheses under one prefix**, and
every downstream sentence has to declare which. This is a milder form of the very defect the round
exists to remove: it replaces "several objects, one name" with "two objects, two names, and a reader
who must track which each consequence uses". It is honest, and it is more bookkeeping.

**The specific benefit is real and should not be waved away:** AEH becomes exactly the minimal
hypothesis the consequences consume. That is a virtue, and it is the one thing Option 1 must
compensate for by per-consequence annotation.

### 5.5 How the calibration record reads against it

The `L = 2` measurements of §4.5 become evidence for **AEH-P, not for AEH**. The page must then say
that the campaign tests two hypotheses, and that the flagship `L = 2` cells are outside the one the
paper states. That is an awkward sentence to have to write, and it is the honest one.

---

## 6. Recommendation

**Recommend Option 1, sub-variant 1a (letters primary).** Five reasons, in order of weight; the author
decides.

1. **The unconditional base case already proves the strengthened form.** `13.2` L34 bounds
   `TV(Law(W_n), B^{⊗n}) ≤ P_B(S_n ≥ L)` — the joint law of the whole length-`n` word, not any
   marginal — so every finite-`L` pattern frequency concentrates simultaneously, and "Hypothesis
   `13.2.1` is a theorem for every `θ < 1/4`" is true of the strengthened statement without changing a
   symbol. Retaining the weaker hypothesis buys **no wider provable range**. This is the argument I
   consider decisive.
2. **Nine sites versus one.** Option 1 makes nine sentences true where they stand. Option 2 edits nine
   sentences and adds a second named object.
3. **The campaign has always measured it.** (q1) says so; §4.5 verifies it in the code.
4. **`13.6.4` is what §13.6 is for.** Under Option 1 the section's title claim — a named equivalence
   for AEH — is literally what is proved.
5. **Minimality is recoverable without splitting.** Annotate `13.3.1` and `13.3.2` as consuming only
   the `L = 1` marginal (`13.2.2`). That records the same information Option 2 buys, with one clause
   instead of one hypothesis.

**Against the recommendation, stated fairly.** Option 1 asserts strictly more than any consequence on
the page uses, at a moment when the calibration reaches only `L ≤ 2`. A reviewer who values "assume
exactly what you consume" will prefer Option 2, and that preference is defensible. If the author takes
Option 2, §8's drop-ins are sufficient to switch without a further round.

**Independent of the choice:** the two-sided `B̂`, the capped `W_{k,D}`, the notation `π_{k,D}`, total
variation, and the three failed sentences of §9 items 5–7 are settled and apply either way.

---

## 7. Drop-in text — Option 1 (recommended)

### 7.1 `paper/collatz-reduced-v3.tex`, §5 — replacing the `\pi_k` paragraph (L241)

Replace the two sentences beginning "What the present coordinates add is the \emph{joint labelled}
law" and ending "Let $\pi_k$ denote this product law." with:

```latex
What the present coordinates add is the \emph{joint labelled} law
(\texttt{aeh.md} \S13.6.3(v)): the $\w$-residues are Haar-uniform among odd
residues and independent of the depth, with $\dnext = m_+ + a_+$ and
$m_+ \perp a_+$, the whole carried on the residues \emph{together with} the
stratum labels $(s,\sigma,a_+)$ --- $a_+$ being a $3$-adic function of $\w$
(Lemma~\ref{lem:absorption}) which the finite $2$-adic residue window does not
determine. Two integers fix the observable: a depth $k$ and a \emph{cap} $D$,
chosen together and quantified over. The \emph{capped depth-$k$ window} at a
visit is
\[
  W_{k,D} \;=\; \bigl(\, \w \bmod 2^{k+2},\; d \wedge D,\; s \wedge D,\;
  \sigma \wedge D,\; a_+ \wedge D \,\bigr), \qquad u \wedge D := \min(u,D),
\]
a finite alphabet of at most $2^{k+1}D^3(D+1)$ letters; the cap is what bounds
it, and it must cap the labels as well as the depth, since $\sigma$ and $a_+$
are unbounded. This is \emph{not} the window of Theorem~\ref{thm:onestep}: that
object carries residues to the state-dependent depth $\sigma + k + 2$ together
with the \emph{exact} labels, so its alphabet is countably infinite, and it
decides the next step. $W_{k,D}$ decides nothing; it is a statistic, and no
statement in this section asks more of it. Let $\pi_{k,D}$ denote the law of
$W_{k,D}$ under the two-sided Bernoulli measure
$\hat B = \bigotimes_{i \in \Z}(\mathrm{geom}(\tfrac12) \times
\mathrm{geom}(\tfrac12))$ on the door-letter alphabet --- two-sided because the
absorption $a_+$ is a function of the orbit's $3$-adic past and has no
realisation on the one-sided $2$-adic side (\texttt{aeh.md} \S13.6.3(iii),
\S13.6.5). ``Product'' names exactly two clauses of $\pi_{k,D}$ --- residue
$\perp$ depth, and $m_+ \perp a_+$ --- and no others: $\pi_{k,D}$ is not a
product across its coordinates ($s$ is an exact function of the full state), and
the process $(W_{k,D}(n))_n$ is stationary but not independent across time
(e.g.\ from $(\w \equiv 1\ (8),\ d$ odd$)$ the next depth is exactly $1$).
```

### 7.2 `paper/collatz-reduced-v3.tex` — replacing `hypothesis` (L243–257)

```latex
\begin{hypothesis}[AEH, ensemble form]\label{hyp:aeh}
Fix a horizon rate $\theta > 0$ and a cut sequence $X_N \to \infty$ with
$\log X_N = o(\log N)$. For each $N$, draw $x$ uniformly from the odd integers
of $[N,2N)$; put $(\w_0,d_0) = R(x)$ and $(\w_{n+1},d_{n+1}) = F(\w_n,d_n)$;
and let the \emph{letter} at block $n$ be the pair $\ell_n = (m_{+,n},\,s_{n+1})$
of that block's entry depth and the next block's exit valuation. Call block $n$
a \emph{bulk} block if $x_{\mathrm{exit}}(n) > X_N$. For a finite word
$w = (w_1,\dots,w_L)$ of letters, let $f_N(w,x)$ be the unweighted frequency of
$w$ among the blocks $(\ell_n,\dots,\ell_{n+L-1})$ with $n$ among the first
$T = \lceil\theta\log_2 N\rceil$ and every index bulk, each such block counted
once and no block reweighted by the orbit it came from. Then for every finite
word $w$ and every $\varepsilon > 0$,
\[
  \frac{2}{N}\,\#\bigl\{\, x \text{ odd},\ N \le x < 2N \;:\;
  \bigl| f_N(w,x) - B[w] \bigr| > \varepsilon \,\bigr\}
  \;\longrightarrow\; 0 \qquad (N \to \infty),
  \qquad B[w] = \prod_{i=1}^{L} 2^{-(m_i + r_i)},
\]
for every admissible $\theta$ and $(X_N)$.
\end{hypothesis}

Equivalently, and this is the form the calibration measures: for every $k$, $D$
and $L$, the empirical distribution of the $L$-blocks of consecutive capped
windows $W_{k,D}$ over the same bulk blocks converges, in total variation on the
finite window alphabet and off a vanishing density of starts, to
$\pi^{(L)}_{k,D}$, the $L$-block law of the stationary process under $\hat B$.
The equivalence is Theorem 13.6.4 of \texttt{aeh.md}, a deterministic dictionary
between letters and labelled window blocks; the case $L = 1$ recovers
$\pi_{k,D}$, and $\pi^{(L)}_{k,D} \neq \pi_{k,D}^{\otimes L}$. A single sampled
orbit segment has no infinite past at its first block, so the reconstruction of
$W_{k,D}$ from letters is exact only away from the segment's start; the
deviation occupies $O(1)$ blocks of a horizon $T \to \infty$ and contributes
$O(1/T)$ to every frequency above.
```

The paragraph at L259–277 ("There is one limit here…") is unchanged and remains correct.

### 7.3 `paper/collatz-reduced-v3.tex`, L301–304 — the ledger sentence

Replace the opening clause of the "AEH implies the ledger" paragraph:

```latex
AEH implies the ledger, in the form the hypothesis has: $s$ is a coordinate of
the observable, so $P(s = j) = 2^{-j}$ is a marginal of $\pi_{k,D}$ rather than a
deduction, exactly at every $j < D$ and up to the cap's single tail cell above;
and for every $\varepsilon$ and every horizon rate, all but a set of starting
values of natural density zero carry those frequencies along their first
$\lceil\theta\log_2 x\rceil$ bulk blocks. The error $O(2^{-k})$ of
Theorem~\ref{thm:onestep} prices a different statement --- \emph{predicting} the
next exit valuation from a window --- which the hypothesis does not use.
```

### 7.4 `aeh.md` §13.2 — drop-in replacing L18–30

````markdown
## 13.2. The hypothesis

Fix a depth `k ≥ 1` and a **cap** `D ≥ 1`: two integers, chosen together and quantified over. For a visit `n` of an `F`-orbit with state `(ω_n, d_n)`, write `A_n = 3^(d_n)·ω_n − 1`, `s_n = v_2(A_n)`, `C_n = A_n + 2^(s_n)`, `σ_n = v_2(C_n)`, `a_(+,n) = v_3(C_n)`. The **capped depth-`k` window** at that visit is

```text
W_{k,D}(n) = ( ω_n mod 2^(k+2),  min(d_n, D),  min(s_n, D),  min(σ_n, D),  min(a_(+,n), D) ).
```

Its alphabet is finite — at most `2^(k+1)·D^3·(D+1)` letters — and the cap is what makes it so: it caps the three stratum labels as well as the depth, `σ` and `a_+` being unbounded. `W_{k,D}` is defined at every visit of every orbit, from the state and its own step, with no reference to the past.

`W_{k,D}` is **not** the depth-`k` window of stage4.md `11.8.7.6`. That object carries residues to the state-dependent depth `σ + k + 2` together with the *exact* labels `(s, σ, a_+)`, so its alphabet is countably infinite; it decides the next step's `s` and `3`-gain in an error-free trichotomy with undecided rate `~2^-(k+1)` (`11.8.7.6.1`). `W_{k,D}` decides nothing — it is a statistic, and nothing on this page asks more of it. The implication runs one way: `11.8.7.6`'s window determines `W_{k,D}` whenever `D` exceeds its labels.

Let `π_{k,D}` denote the **stationary law** of `W_{k,D}`: the law under the two-sided Bernoulli measure `B̂ = ⊗_(i ∈ Z) (geom(1/2) × geom(1/2))` on the door-letter alphabet, pushed forward by the reconstruction of `13.6.3`(iii). The space is two-sided because the absorption `a_(+,n) = v_3(y_n + 1)` is a function of the `3`-adic *past* and has no realization on the one-sided `2`-adic side at all (`13.6.3`(iii); the past-limit `y_3` of itinerary.md `14.15.3.3`); with an infinite past the reconstruction is exact almost surely, so `π_{k,D}` carries no exceptional-set caveat and the `2·(0.93)^W` estimate of `13.6.3`(iv) survives only where it belongs, in the finite-past bound of `13.6.4`. The word **product** names exactly two clauses of `π_{k,D}`, both proved at `13.6.3`(v) and neither more:

```text
omega-residue Haar-uniform among the valid (= odd) residues mod 2^(k+2),
              INDEPENDENT of the depth (indeed of the whole past);
depth         d = m + a,  m geometric(1/2)  (P(m = j) = 2^-j),  a the absorption,
              m INDEPENDENT of a.
```

It is *not* a product across the window's coordinates — `s` is an exact function of the full state `(ω,d)`, hence not independent of the `ω`-residue — and it is *not* a product across time: the process `(W_{k,D}(n))_n` is stationary under `B̂` but has deterministic transitions (from class `(1 mod 8, d odd)` the next depth is exactly `1`), so the `L`-block law `π^(L)_{k,D}` is **not** `π_{k,D}^(⊗L)`. This law is *derived*, not posited, and its depth marginal is computed in closed form at `13.6.5`, which is where the values live. The stationary law of the exact window chain is a different object: a `~1%`-accurate model of this marginal, internal to this record, whose exact discrepancy from it is recorded at `13.6.5`.

**Hypothesis 13.2.1 (AEH, ensemble form).** Fix a horizon rate `θ > 0` and a cut sequence `X_N → ∞` with `log X_N = o(log N)`. For each `N`, draw `x` uniformly from the odd integers of `[N, 2N)`, set `(ω_0, d_0) = R(x)` and `(ω_{n+1}, d_{n+1}) = F(ω_n, d_n)`, and let the **letter** at block `n` be `ℓ_n = (m_(+,n), s_(n+1))` (`13.6.3`(i); reverse.md `14.14.6`). Call block `n` a **bulk** block if `x_exit(n) > X_N`. For a finite letter word `w = (w_1, …, w_L)`, let `f_N(w, x)` be the unweighted frequency of `w` among the blocks `(ℓ_n, …, ℓ_(n+L−1))` with `n` among the first `T = ⌈θ log₂ N⌉` and every index bulk, each such block counted once, with no per-orbit reweighting (`13.5`). Then for **every finite word `w`** and every `ε > 0`, the density of starts `x ∈ [N, 2N)` with `|f_N(w, x) − B[w]| > ε` tends to `0` as `N → ∞`, where `B[w] = Π_i 2^-(m_i + r_i)`, for every admissible `θ` and `(X_N)`.

**Hypothesis 13.2.2 (the window form; equivalent).** Same sampling and same bulk blocks. For every `k`, `D` and `L`, let `ν^(L)_{k,D,N}(x)` be the unweighted empirical distribution of the `L`-blocks of consecutive capped windows `W_{k,D}` over those blocks. Then for every `ε > 0` the density of starts with `‖ν^(L)_{k,D,N}(x) − π^(L)_{k,D}‖_TV > ε` tends to `0`, where `‖·‖_TV` is total variation on the finite window alphabet, `‖μ − π‖_TV = ½ Σ_w |μ(w) − π(w)|`. `13.2.1 ⟺ 13.2.2` is Theorem `13.6.4`. The case `L = 1` — the empirical law of single window states against `π_{k,D}` — is the marginal form that `13.3.1` and `13.3.2` consume; it is strictly weaker than either hypothesis, by (q1).

**The segment boundary.** An integer orbit segment has no infinite past at its first block, and `W_{k,D}` does not need one: it is read off the state and its own step. What the past supplies is the *identification of the law*. The transient is real and exactly located — for a uniform odd start `x`, `a = v_3(x+1)` has `P(a = j) = 2·3^-(j+1)`, i.e. `(2/3, 2/9, 2/27, …)` against the bulk `(2/3, 19/63, 2/63, …)`, because a uniform integer is `≡ 0 mod 3` a third of the time and a door never is (`13.6.5`) — and it relaxes geometrically (`13.6.3`(iv)). It therefore occupies `O(1)` blocks of a horizon `T = ⌈θ log₂ N⌉ → ∞` and contributes `O(1/T)` to every frequency above. No burn-in enters the statement; the burn-in of `10` in `experiments/aeh_symbolic.py` is a finite-size device.
````

The remaining §13.2 paragraphs (L32 "Why the ensemble…", L34 "Base case…", L36 "Supporting exact
facts…") are unchanged except for three token substitutions: `π_k → π_{k,D}` throughout, and at L36 the
clause "A symbolic form of the hypothesis is recorded at itinerary.md `14.15.2`: AEH is precisely the
statement that…" now reads without hedge, because `13.2.1` *is* that statement. Add to L34, after
"Hypothesis 13.2.1 is therefore a theorem for every `θ < 1/4`":

```markdown
The bound is on the joint law of the whole length-`n` word, so it delivers every finite-`L` pattern frequency at once, not merely the single-letter marginal: the base case proves `13.2.1` in full, at every block length, in its provable range.
```

### 7.5 `aeh.md` Theorem `13.6.4` — the definition sentence and (q1)

Replace, inside the theorem statement at L113, the clause defining bulk-equidistribution:

```markdown
say its window-state process is **bulk-equidistributed** if for every `k`, `D` and `L`, the `L`-blocks of consecutive capped depth-`k` windows `W_{k,D}` (`13.2`) have bulk frequencies given by `π^(L)_{k,D}`, the `L`-block law of the stationary process under `B̂`. This is *not* `π_{k,D}^(⊗L)`: `13.6.3`(v) is a single-visit law and does not determine block frequencies, and the process has deterministic transitions (`13.2`).
```

Replace (q1) at L125 with:

```markdown
* **(q1) Single visits versus blocks.** The `L = 1` marginal form (`13.2.2` at `L = 1`) is strictly weaker than the hypothesis, and the gap is exact rather than technical. Bulk-genericity implies it (with the depth marginal read per `13.6.5`), and that direction is a theorem; the converse **is obstructed, precisely**: the absorption sequence is `2`-adically invisible — `a_(+,n+1)` is not a function of any depth-`k` window at visit `n`, at any `k` — so single-visit equidistribution controls single letters (via the trichotomy `11.8.7.6.1`, undecided rate `~2^-(k+1) → 0`) but not letter pairs. The graded correspondence is exact: `L`-letter statistics are visit-`(L+1)`-block statistics, the `a`-sequence being what each extra block position adds. This is why `13.2.1` is stated at every `L`, and why the calibration record — which has always measured consecutive pairs (`13.4`; `aeh_calibration.py` L368, `aeh_symbolic.py` L597) — is testing the hypothesis rather than a marginal of it. Consequences that consume only the marginal say so: `13.3.1`, `13.3.2`.
```

`13.6.4`'s displayed equivalence, its proof, and (q2) stand unchanged.

### 7.6 `aeh.md` L2 — status front matter

```markdown
status: hypothesis FORMALIZED in ensemble form (13.2.1) as bulk Bernoulli-genericity of the door letter words, with the equivalent capped-window form at 13.2.2 and the dictionary proved at 13.6.4; calibrated — bulk uniformity confirmed UNQUALIFIED at every tested depth and cell, at block lengths L <= 2; the 13.5 anomaly RESOLVED as a protocol artifact (with an exact routing lemma); depth marginal exact (13.6.5); proof effort remains parked per stopping rules
```

The "Current state" blockquote at L8 needs the same two substitutions and one added clause: `π_k →
π_{k,D}`; "follow the exact product law `π_k`" → "follow `π_{k,D}`, whose two product clauses are
`13.6.3`(v)"; and after "the single-visit-versus-block distinction recorded (13.6.4)" add "— the
hypothesis is the block form, the single-visit marginal (13.2.2 at `L = 1`) being strictly weaker".

### 7.7 `itinerary.md` L73

```markdown
One pointer sentence, no more: the cylinder's natural measure — `2^-S` in the Haar-odd normalization of aeh.md `13.6.2`(4), `2^-(S+1)` as a density in all of `Z` — is exactly what aeh.md's stationary law `π_{k,D}` (`13.2`) quantifies; AEH is *precisely* the statement that the stratum words of the bulk segments of uniformly sampled starting values (aeh.md `13.2.1`) equidistribute against that measure at every finite word length — an equivalence with the window form named and proved at aeh.md `13.6` (the genericity form of AEH), with the cylinder measure identified there as a Bernoulli product measure. (One fact, one page: aeh.md's content is not restated here, and no statistic is run.)
```

*(The normalization clause is a separate small correction: L73 currently equates `2^{−(S+1)}` with what
`π_k` quantifies, but `13.6.2`(4) gives the Haar-odd cylinder mass as `2^{−S}`. `2^{−(S+1)}` is the
class's density in `Z`. One clause fixes it; it is not part of this round's blockers.)*

### 7.8 `bridge.md` L69 and `HANDOFF.md` L20

Substantively unchanged under Option 1. `bridge.md` L69's `π_k → π_{k,D}` and "(aeh.md 13.2.1)"
pointer both remain correct.

---

## 8. Drop-in text — Option 2 (rejected here; sufficient to switch)

Everything in §3 applies unchanged: `W_{k,D}`, `D` free, `π_{k,D}`, TV, `B̂`, the boundary paragraph,
and §7.4's `13.2` preamble down to (but not including) Hypothesis `13.2.1`. What differs:

### 8.1 `aeh.md` Hypothesis `13.2.1` (single-visit, repaired)

```markdown
**Hypothesis 13.2.1 (AEH, ensemble form).** Fix a depth `k`, a cap `D`, a horizon rate `θ > 0`, and a cut sequence `X_N → ∞` with `log X_N = o(log N)`. For each `N`, draw `x` uniformly from the odd integers of `[N, 2N)`, set `(ω_0, d_0) = R(x)` and `(ω_{n+1}, d_{n+1}) = F(ω_n, d_n)`, and let `ν_{k,D,N}(x)` be the unweighted empirical distribution of the capped windows `W_{k,D}` over the **bulk visits** among the first `T = ⌈θ log₂ N⌉` — those with `x_exit > X_N` — each qualifying visit counted once, with no per-orbit reweighting (`13.5`). Then for every `ε > 0`, the density of starts `x ∈ [N, 2N)` with `‖ν_{k,D,N}(x) − π_{k,D}‖_TV > ε` tends to `0` as `N → ∞`, for every admissible `k, D, θ` and `(X_N)`, where `‖·‖_TV` is total variation on the finite window alphabet.
```

### 8.2 `aeh.md` appended anchor `13.2.2`

```markdown
**Hypothesis 13.2.2 (AEH-P, the process form).** Same sampling and same bulk visits. For every `k`, `D` and `L`, the unweighted empirical distribution of the `L`-blocks of consecutive capped windows converges to `π^(L)_{k,D}` in total variation, off a vanishing density of starts. Equivalently (Theorem `13.6.4`), the letter word of those bulk segments is bulk-generic for the Bernoulli law `B`: every finite letter word has its `B`-frequency. **AEH-P is strictly stronger than AEH `13.2.1`**, which is its `L = 1` case; the converse is obstructed for the exact reason recorded at `13.6.4`(q1). Every consequence of `13.3` uses `13.2.1` alone. The genericity form of `13.6`, the calibration record's consecutive-pair cells (`13.4`), and bridge.md `16.4.3`'s "missing statistical half" are all statements about **AEH-P**.
```

### 8.3 `paper/collatz-reduced-v3.tex`

`hyp:aeh` keeps the L243–257 shape with three substitutions: `\pi_k \to \pi_{k,D}`,
`\lVert\cdot\rVert \to \lVert\cdot\rVert_{\mathrm{TV}}` with the definition given in the preceding
paragraph, and "the depth-$k$ windows" → "the capped windows $W_{k,D}$". The `\pi_k` paragraph is §7.1
verbatim. Then add, immediately after the hypothesis:

```latex
Hypothesis~\ref{hyp:aeh} constrains single blocks. The corresponding statement
about \emph{consecutive} blocks --- that for every $L$ the $L$-blocks of
consecutive capped windows have the frequencies of the stationary process ---
is strictly stronger, and is what the symbolic form of \texttt{aeh.md} \S13.6 is
an equivalence with (\texttt{aeh.md} Hypothesis 13.2.2, Theorem 13.6.4). The
single-block form does not imply it: the absorption sequence is $2$-adically
invisible, so single-visit equidistribution controls single letters but not
letter pairs. Section~\ref{sec:aeh}'s consequences use the single-block form
only; the calibration campaign's consecutive-pair cells test the stronger one.
```

### 8.4 The nine sites, under Option 2

Each must name AEH-P. Minimal edits: `aeh.md` L2 "symbolic form … PROVED as an equivalence" →
"…equivalent to the *process* form 13.2.2, strictly stronger than 13.2.1"; L8, L36, L71, L143, L145
each replace "AEH" with "AEH's process form (13.2.2)" in the genericity sentence; `itinerary.md` L73
"AEH is thereby precisely the statement" → "AEH's process form (aeh.md 13.2.2) is precisely the
statement"; `bridge.md` L69 "its symbolic name is the genericity form" → "the genericity form names its
process strengthening (aeh.md 13.2.2)"; `HANDOFF.md` L20 likewise.

---

## 9. The consequence trace

Verdicts are for the recommended Option 1 unless a second verdict is given for Option 2.

| # | Consequence | Verdict | Note |
|---|---|---|---|
| 1 | `13.3.1` ledger, error `O(2^-k)` | **Survives restated; the error term is retired** | With `s` a coordinate of `W_{k,D}`, `P(s=j) = 2^{-j}` is a marginal of `π_{k,D}` — exact at every `j < D`, with one tail cell above. The `O(2^{-k})` priced *prediction* from residues, which `13.2.1` no longer performs. What keeps an error term is `11.8.7.6.1`'s trichotomy, whose statement is unaffected. The `k → ∞` diagonal becomes a `(k,D) → ∞` diagonal. Same under Option 2. |
| 2 | `13.3.2`, the `1/3` rate | **Survives restated, with a cap error** | `P(s even) = Σ_{j even} 2^{-j} = 1/3` is a marginal, exact up to the single cell `{s ≥ D}` of mass `2^{-(D-1)}` whose parity split the cap hides. Exact along `D → ∞`. Previously written as exact with no cap error; that was an artifact of `D_k` being invisible. Same under Option 2. |
| 3 | `13.3.2`, the drift non-consequence | **Survives verbatim, reinforced** | The cap makes the point structural: all mass beyond `D` is one cell and carries no information about the mean of the unbounded `m_+`. TV convergence on a finite alphabet gives no `limsup` control — one visit in `T` with `σ = T^2` moves the mean by `T` and TV by `1/T`. Round 2's rider question (item 3, L350) is untouched by this round. |
| 4 | `13.3.3` scope discipline | **Survives verbatim** | Nothing here touches density-of-starts, non-iteration, or the staircase tails. |
| 5 | `13.6.3`(v)'s product law and its space | **Fails as written; survives restated on `B̂`** | "Under Haar-odd (equivalently `B`)" is wrong for the absorption clause: `a_{n+1} = v_3(y_n+1)` is not a function on odd `Z_2`. Restated on `B̂` the renewal argument is *cleaner* — the conditional law of the future given the whole past is `B`, so `(m_n, q_n) ⊥` past holds at every index `n ∈ Z`, and `m_n ⊥ a_{n+1}` is exact rather than asymptotic. No value changes. Required under both options. |
| 6 | `13.6.4`'s definition of *bulk-equidistributed* | **Fails as written; survives restated** | "bulk frequencies given by the product law of `13.6.3`(v)" is underdetermined: a single-visit law does not fix `L`-block frequencies. The theorem's own `(⇐)` proof uses the `L`-block law ("an `L`-letter pattern is a function of the `(L+1)`-block of window states, and its bulk frequency is the corresponding block frequency"). Replace by `π^(L)_{k,D}`. Required under both options. |
| 7 | `13.2`'s "the cap does one job, keeping the window alphabet finite" | **Fails as written** | The labels `(s, σ, a_+)` that `13.6.3`(iii) reads into the same object are unbounded. Repaired by capping them: the cap does two jobs. Required under both options. |
| 8 | `13.6.4`'s theorem, displayed equivalence and proof | **Survives verbatim** | The proof is a deterministic dictionary with explicit finite-window error `2L(0.93)^W`; only the definition it opens on moves (item 6). Under Option 1 it becomes an equivalence with AEH; under Option 2 with AEH-P. |
| 9 | `13.6.4` (q1) | **Survives restated; role changes** | Option 1: from qualifier on the identification to the reason the hypothesis is stated at all `L`. Option 2: promoted to the statement separating two named hypotheses. Its mathematics — the `2`-adic invisibility of the absorption sequence, the exact `L`-letter ↔ `(L+1)`-block grading — is untouched under both. |
| 10 | `13.6.5`'s values `2/3`, `19/63`, `2/63`, `P(d=·)` | **Survive verbatim** | §10. One clause repaired: "Under `B`" → "Under `B̂`", since `y_3` is a past-limit. |
| 11 | `13.6.5`'s Tao attribution | **Survives verbatim** | It attributes the law of `Syrac(Z_3)`, which is a stationary law on a two-sided/past-limit object in Tao's own setting. Nothing in the identification `a = v_3(Syrac(Z_3) + 2)` or in the unit rescaling `y_3 = Syrac(Z_3)/2` uses the one-sidedness. |
| 12 | `13.6.5`'s window-chain discrepancy (`17/63` vs `19/63`, `4/63` vs `2/63`) | **Survives verbatim** | It is a comparison of two exactly computed laws; neither moves. |
| 13 | `13.6.6` | **Survives verbatim (Option 1)** / re-pointed (Option 2) | Under Option 1 its "bulk `B`-genericity of the integers' letter words" is exactly `13.2.1`. Its (b) clause about non-generic points now refers to the two-sided shift; harmless. |
| 14 | `13.6.7` | **Survives verbatim (Option 1)** / re-pointed (Option 2) | Its whole purpose — keeping the two equidistributions apart — is unaffected. |
| 15 | The nine "equivalence" sites (§1.1) | **Survive verbatim (Option 1); fail as written (Option 2)** | This is the round's largest single cost difference. |
| 16 | paper L241, the `π_k` paragraph | **Fails as written** | `\pi_k` hides `D`; no norm; no separation from `thm:onestep`'s window; "Let $\pi_k$ denote this product law" names a joint law by one of its two product clauses. §7.1. |
| 17 | paper L243–257, `hyp:aeh` | **Restated in place** | §7.2 (Option 1) or §8.3 (Option 2). Unpublished; no erratum framing. |
| 18 | paper `thm:onestep` (L159–161) | **Survives verbatim; does not move** | Its labelled variable-depth window is correct for what it does and is one of the eight v3 repairs the Version note (L42) records. It stays a separate, countable object, and §5 gains the sentence saying so (§7.1). |
| 19 | paper L301–313, the "what the hypothesis supplies" paragraph | **Survives restated** | Only the ledger clause moves (§7.3). The Inselmann/Tao framing and the "does not iterate" clause are untouched. |
| 20 | `13.4` calibration record | **Survives; one claim narrows** | Every number stands. "UNQUALIFIED at all tested depths" must gain "at block lengths `L ≤ 2`". The `(s,s')=(4,3)` cell is verified as a genuine `L = 2` test (§4.5). |
| 21 | `13.5` standing rule and Lemma `13.5.1` | **Survive verbatim** | `13.5.1` additionally becomes the citable witness that the window process is not temporally independent. |
| 22 | Appendix A commit pin `c2d465a` (paper L339) | **Dies on any `aeh.md` edit** | Phase-2 mechanic. Flagged, not fixed here. |

---

## 10. Does the depth marginal move under a two-sided formulation? — verified, unhedged

**No. Not one value moves.** Neither `P(a=0) = 2/3`, `P(a=1) = 19/63`, `P(a≥2) = 2/63`,
`P(a≥3) ≈ 0.0061`, nor the derived `P(d=1) = 1/3`, `P(d=2) = 20/63`, `P(d=3) ≈ 0.171555`,
`P(d=4) ≈ 0.087916`.

**Why, from the page's own statements.**

1. `13.6.5` (L130) defines the law by: "by synchronization, `y_n mod 3^j` is a function of the last `j`
   letters alone, so `ν_j` is the exact image of `B^{⊗j}` under the offset formula — a finite rational
   computation". `13.6.3`(iii) (L98) says the same: "For every `W ≥ 1`, `y_n mod 3^W` is an explicit
   function of letters `n−W, …, n−1` **alone**", with `Σ m ≥ W` guaranteed by `m_i ≥ 1`.
2. `ν_j` is therefore a pushforward of the law of **exactly `j` consecutive letters**. Under one-sided
   `B` and under two-sided `B̂` those `j` letters have the *same* i.i.d. law. The pushforward is
   identical. There is no other input.
3. `itinerary.md` `14.15.3.3` gives `v_3(B_{n+1} − B_n) = M_n ≥ n`, so `y_3 ≡ y_n (mod 3^{M_n})`. Hence
   at any index with at least `j` letters of past, `P(a = i)` for `i < j` is exactly the two-sided
   value, and the residual is `P(a ≥ j) ≤ 2·(0.93)^j` (`13.6.3`(iv)).
4. The level-one case is a one-letter computation and needs no past at all: `ν_1 = (2/3, 1/3)` on
   `(1,2) mod 3` is "the `r`-parity law", and `P(r even) = Σ_{j even} 2^{-j} = 1/3` by `13.6.1`. So
   `P(a=0) = 2/3` holds even at the first available index.

**Arithmetic check of the derived values, done rather than recalled.** With `d = m + a`, `m ⊥ a`,
`P(m=j) = 2^{-j}`:

* `P(d=1) = P(m=1)P(a=0) = ½·⅔ = 1/3` ✓ (page: `1/3`).
* `P(d=2) = ½·(19/63) + ¼·(2/3) = 19/126 + 21/126 = 40/126 = 20/63` ✓ (page: `20/63`).
* `P(d=3) = ½·P(a=2) + ¼·(19/63) + ⅛·(2/3) = ½·P(a=2) + 0.1587302`. The page's `0.171555` gives
  `P(a=2) = 0.0256496`, and independently `P(a=2) = P(a≥2) − P(a≥3) = 0.031746 − 0.0061 = 0.025646` ✓
  to the precision printed.
* `P(d=4) = ½·P(a=3) + ¼·P(a=2) + ⅛·(19/63) + 1/16·(2/3) = ½·P(a=3) + 0.0857767`. The page's
  `0.087916` gives `P(a=3) = 0.0042786`, consistent with `P(a≥3) ≈ 0.0061` and a tail ratio below `2/3`
  as `13.6.5`'s verification block requires ✓.

**What the two-sided space does change.** It changes *where the law is exact*, not what the law is.
Under one-sided `B` the object `a_{n+1}` does not exist as a random variable at all — only its
truncation to the precision the available past supplies. Under `B̂` it exists exactly, at every index,
and the reconstruction of `13.6.3`(iii) is exact almost surely rather than off an exceptional event.
`13.6.3`(v)'s "Under Haar-odd (equivalently `B`)" and `13.6.5`'s "Under `B`" are therefore both wrong
as written and both repaired by one substitution, with no numerical consequence.

**Therefore:** the Tao attribution at `13.6.5` and the paper's §5 values (L241) rest on nothing that
moves. Neither needs a hedge, a caveat, or a re-check.

---

## 11. Does the record invite the product-law misreading? — yes, and it also refutes it

**Asked plainly by the brief; answered plainly.** Yes. Three sites read as temporal independence:

* `aeh.md` L2 status: "depth-`k` window states … follow the exact product law `π_k`" — a statement
  about a *process* whose predicate names a product.
* `aeh.md` L8: "It asserts that the depth-`k` window states over the bulk visits of those sampled
  orbits follow the exact product law `π_k`" — same.
* `aeh.md` L113 (`13.6.4`): "the `L`-blocks of consecutive depth-`k` window states … have bulk
  frequencies given by the product law of `13.6.3`(v)". A reader who supplies the only reading under
  which that sentence is well-formed will supply `π_k^{⊗L}`.

Nowhere does the record state that the process is *not* temporally independent. `13.2` L22 does gloss
"product" as the within-state clauses, which is correct; but that gloss is three sections away from
`13.6.4` and does not survive the trip.

**The record contains its own refutation, twice.** `13.2` L36: "The class process under `π_k` is an
explicit finite Markov chain with computable entries (e.g., from class `(1 mod 8, d odd)` the next
depth is exactly `1`)" — a *deterministic* transition. And `13.5.1` (L61): "the residue `ω mod 32`
exactly determines the next class". Under temporal independence neither could hold. The correct
statement is: the process is **stationary** under `B̂` and **strongly dependent**; only the two
within-state clauses of `13.6.3`(v) are product clauses.

Under either option, one sentence must go on the page. §7.4 and §7.5 supply it.

---

## 12. Open questions — named, not smoothed over

1. **Whether `D` should be `k`-linked at all.** I recommend a free parameter. If the author wants the
   subscript `D_k` kept for continuity with the existing text, then the page must say what function of
   `k` it is, and I have no principled candidate: no finite cap makes the capped window decide the
   step (the trichotomy needs `ω mod 2^{σ+k+2}` and exact labels), so any choice is conventional.
   `D = k+2` is the tidiest convention, not a derivation.
2. **TV versus cellwise on the letter side.** I recommend cellwise for the countable letter alphabet
   because it is what genericity means and it is the weaker hypothesis. A TV form on the letter
   alphabet is stateable (the tails are geometric) and would be strictly stronger. I did not settle
   whether the strictly stronger form is worth having; nothing on the page needs it.
3. **The `2·(0.93)^j` bound's provenance under `B̂`.** `13.6.3`(iv)'s proof conditions on "the `i`
   letters nearest `y_n`" and prepends. Under `B̂` the prepending is into an existing infinite past
   rather than into a vacuum. I believe the argument is unaffected — it only uses that each prepended
   letter's `3`-adic digit contribution is final and takes two values with probabilities `2/3, 1/3` —
   but I did not re-derive it in the two-sided setting and flag it as a one-paragraph check for the
   apply phase.
4. **Composite verification of the labelled reconstruction.** `experiments/aeh_symbolic.py`
   `check_two_sided_reconstruction` (L270–322) reconstructs `(ω mod 2^{k+2}, min(d, D))` only — the
   `true_state` at L301 has no labels. The label↔letter dictionary is verified separately (L141's
   "seam identities, letter `= (σ−s, s_+)`"), so nothing is unverified in substance; but the composite
   claim "the *labelled* capped window is an exact function of a bounded two-sided letter window" is
   not run as one test. One `assert` extends the existing test to the five-coordinate `W_{k,D}`. This
   is a verification item for the apply phase, not a finding against the claim.
5. **Round 2's item 2 (how far past `θ = 1/4` the base case extends) and item 4 (horizons past the
   descent) are untouched by this round** and remain open exactly as parked. Item 3 (the drift rider)
   is also untouched; the drift is a non-consequence on the current page (`13.3.2`) and this round
   gives no reason to revisit that.
6. **Round 2's item 5 (`D_k`) is discharged here** as far as a design round can discharge it: the
   parameter now has a role, a quantifier, and a visible index on the law. Whether the author wants a
   fixed value printed is item 1 above.
7. **`itinerary.md` L73's `2^{−(S+1)}` normalization** (§7.7) is a small correction outside this
   round's blockers. Recording it so it is not lost.
8. **Appendix A's commit pin `c2d465a`** (paper L339) and `paper/collatz-reduced-v3.pdf` both go stale
   the moment `aeh.md` is edited. Phase-2 mechanic; this repository has already spent a round on it.

---

## 13. Verification table — every number and quotation read, not recalled

| Item | Source |
|---|---|
| status header, "symbolic form NAMED and PROVED as an equivalence" | `aeh.md` L2 |
| "AEH is precisely the assertion that the integers … inherit that genericity at scale" | `aeh.md` L8 |
| `13.2`: "Fix a depth `k` and a **depth cap** `D_k` — any finite cutoff"; "The cap does one job, keeping the window alphabet finite"; "`(ω mod 2^(k+2), min(d, D_k))` together with validity data" | `aeh.md` L20 |
| "Let `π_k` denote the **exact product law**" and its two clauses | `aeh.md` L22–26 |
| Hypothesis `13.2.1` text, `‖ν_{k,N}(x) − π_k‖ > ε`, `T = ⌈θ log₂ N⌉` | `aeh.md` L30 |
| base case `TV(Law(W_n), B^{⊗n}) ≤ P_B(S_n ≥ L)`; "theorem for every `θ < 1/4`"; `E[m+r] = 4`; `1/β = 1.2047…`; `2.29 ×` budget, `23` of `30` blocks | `aeh.md` L34 |
| "the marginal of `s` is exactly the ledger"; `3`-gain `Σ_{j even} 2^{-j} = 1/3`; "from class `(1 mod 8, d odd)` the next depth is exactly `1`"; "AEH is precisely the statement that the stratum words … equidistribute" | `aeh.md` L36 |
| `13.3.1` ledger with error `O(2^-k)`, undecided set `~2^-(k+1)` | `aeh.md` L40 |
| `13.3.2` `1/3` rate, `0.3352` at `1.1σ`; drift non-consequence; `−0.8367 ± 0.0060` / block, `−0.4166 ± 0.0037` / odd step | `aeh.md` L42 |
| `(s, s') = (4,3)` cell `0.1277` vs `0.128` (`-0.1σ`); `P(bits 3–4 \| class (1,2)) = 0.2533`; `(7,1)` cell `0.5017` | `aeh.md` L50 |
| Lemma `13.5.1` deterministic routing, `1 → (1,1)`, `9 → (7,1)`, `17 → (5,1)`, `25 → (3,1)` | `aeh.md` L61 |
| `13.6` opening, "here upgraded to a proved, named equivalence" | `aeh.md` L71 |
| `13.6.1`, `P(m=j) = P(r=j) = 2^{-j}`, `E[m] = 2`, `P(m odd) = 2/3`, `P(r even) = 1/3` | `aeh.md` L75 |
| `13.6.2`(4), cylinder Haar-odd mass `2^{-S}` | `aeh.md` L84 |
| `13.6.3`(iii): "`y_n mod 3^W` is an explicit function of letters `n−W, …, n−1` **alone**"; "with its stratum labels `(s, σ, a_+)` … the reading of `13.2`'s 'validity data'"; the cap clause `D_k ≤ W` | `aeh.md` L98 |
| `13.6.3`(iv): `P_B(a ≥ j) ≤ 2·(0.93)^j`; exact values `1/3, 2/63, ≈0.0061` | `aeh.md` L100 |
| `13.6.3`(v): "Under Haar-odd (equivalently `B`)"; the two product clauses | `aeh.md` L102–109 |
| `13.6.4` statement, "bulk frequencies given by the product law of `13.6.3`(v)" | `aeh.md` L113 |
| `13.6.4` proof, "letter `n = (σ_n − s_n, s_{n+1})`"; `(⇒)` error `2L(0.93)^W` | `aeh.md` L121 |
| (q1) "as literally stated is the `L = 1` case"; "obstructed, precisely"; "`13.4` measures consecutive pairs" | `aeh.md` L125 |
| `13.6.5` values `2/3`, `19/63`, `2/63`, `≈0.0061`; `P(d=·) = 1/3, 20/63, 0.171555, 0.087916`; `ν_1 = (2/3, 1/3)`; "the exact image of `B^{⊗j}`" | `aeh.md` L130–135 |
| Tao attribution, `Syrac(Z/9Z)` list, mass `2/63` at residue `7` | `aeh.md` L137 |
| chain law `17/63`, `4/63`, `19/63`; orbit adjudication `154,389` bulk visits, seed `31005`; `P(ω_+ ≡ 1 mod 3 \| a_+ = 0) = 0.6662 ± 0.0015` | `aeh.md` L139 |
| verification block: `(ω mod 2^5, min(d,6))` from letters, `4,368` visits, `1` exceptional; seam identity letter `= (σ−s, s_+)` | `aeh.md` L141 |
| `13.6.6` "this particular null set inherits genericity at scale"; "bulk `B`-genericity of the integers' letter words" | `aeh.md` L143 |
| `13.6.7` "(1) AEH's genericity form … bulk-generic for the Bernoulli law `B`" | `aeh.md` L145 |
| `thm:deltaM` residues `ω mod 2^{σ+k+2}`, `d mod 2^{σ+k}`, `a_+ mod 2^k` | `paper` L150–152 |
| `thm:onestep` "consists of the residues of Theorem~\ref{thm:deltaM} together with the stratum labels $(s, \sigma, a_+)$" | `paper` L159–160 |
| `\pi_k` paragraph, "Let $\pi_k$ denote this product law"; Tao values `2/3`, `19/63`, `2/63`, `1/3`, `20/63` | `paper` L241 |
| `hyp:aeh` with undefined `\lVert \nu_{k,N}(x) - \pi_k \rVert` | `paper` L243–257 |
| "AEH implies the ledger with error $O(2^{-k})$ via Theorem~\ref{thm:onestep}" | `paper` L301 |
| Version note: `thm:onestep`'s labelled window as a v3 repair; "Hypothesis~\ref{hyp:aeh} is restated in ensemble form" | `paper` L42 |
| Appendix A commit pin `c2d465a` | `paper` L339 |
| `stage4.md` `11.8.7.6` window definition, identical to `thm:onestep` | `stage4.md` L100–106 |
| `11.8.7.6.1` proof: "$d_+ = (σ − s) + a_+$ is exact from the labels"; window determines `C mod 2^{σ+k+2}` | `stage4.md` L114 |
| undecided rate `2^{-(k+1)}`, measured `0.0275` at `k=4`, `0.0019` at `k=8` | `stage4.md` L118 |
| letter `(m,r)` = `(m_+` of edge, `s` of next edge`)` | `reverse.md` L411–414 |
| Theorem `14.15.1.5`, one odd class mod `2^{S+1}` | `itinerary.md` L46–53 |
| `14.15.2` pointer sentence, `2^{-(S+1)}`, "an equivalence named and proved at aeh.md `13.6`" | `itinerary.md` L73 |
| `14.15.3.3` `v_3(B_{n+1} − B_n) = M_n → ∞`, `M_n ≥ n` | `itinerary.md` L97–99 |
| `bridge.md` `16.4.3` "its symbolic name is the genericity form" | `bridge.md` L69 |
| `HANDOFF.md` "now a named, proved equivalence (the genericity form, aeh.md 13.6)" | `HANDOFF.md` L20 |
| `pair43` = `P(s'=3 \| s=4)`, null `0.128` = measured unconditional `P(s'=3)` | `experiments/aeh_calibration.py` L332, L368, L374 |
| s-pair independence screens, class transitions | `experiments/aeh_calibration.py` L28, L36–48, L61, L70, L76–81 |
| letter-pair histogram and independence check | `experiments/aeh_symbolic.py` L570–571, L597–599 |
| reconstruction `true_state = (ω mod 2^{k+2}, min(d,D))`, no labels; defaults `W=8, k=3, D=6` | `experiments/aeh_symbolic.py` L270, L301, L320 |
| flagship protocol: `[2^70, 2^71)`, burn-in `10`, horizon `30`, cut `2^30`, seed `31005` | `experiments/aeh_symbolic.py` L539–546 |
| `‖` occurs in `aeh.md` only at L30; `total variation`/`TV` only at L34 | grep, whole repo |
| "validity data" occurs only at `aeh.md` L20 and L98 | grep, whole repo |
| round 2 unsettled items 2, 4, 5 | `briefs/v3r2-aeh-formulation-findings.md` L349, L351, L352 |
| round 2's uniform-start absorption law `2/3, 2/9, 1/9` and its mechanism | `briefs/v3r2-aeh-formulation-findings.md` L74 (re-derived here: `P(v_3(x+1)=j) = 2·3^{-(j+1)}`) |

Derived, and how: alphabet bound `2^{k+1}·D^3·(D+1)` from `2^{k+1}` odd residues mod `2^{k+2}` and four
capped coordinates; `P(d=·)` convolution checks in §10; `P(r even) = Σ_{j≥2 even} 2^{-j} = (1/4)/(3/4) = 1/3`;
uniform-start absorption `P(v_3(x+1) = j) = (1/3)^j·(2/3) = 2·3^{-(j+1)}`, giving `2/3, 2/9, 2/27` and
`P(a≥2) = 1/9`.
