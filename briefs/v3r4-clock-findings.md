# Findings: what the hypothesis supplies about the budget (v3 round 4, blocking finding)

**Round.** Fourth external review, at `main` `fa9edf5`. Design task, read-only; the one file written is this one.
**Scope.** The blocking finding (the `E_B[m+r] = 4` conversion) plus the two smaller corrections in the same
sections. No pruning, no `13.6.4` union-bound wording, no Appendix A pin.

---

## 0. Verdict, in one paragraph

The reviewer is right that literal `13.2.1` does not give `T_N^{-1}Σ_{n<T_N}(m_n + r_n) → 4`, and the
counterexample is correct as stated: I reproduced it and it survives every fixed pattern frequency and the
vanishing cemetery. But the correction is **not a retraction**, for two reasons the record can state
exactly. First, *below* the budget the conversion is a theorem with an explicit rate — the base case's
total-variation bound transfers the event `{|T_N^{-1}Σ(m_n+r_n) − 4| > ε}` like any other, and the two
clauses of admissibility (`τ < 1`, `4θ < τ`) turn out to be exactly the two terms of `13.2.4`(a). Second,
*above* the budget the hypothesis is not silent either: the cemetery clause, quantified over the admissible
family as `13.2.1` already quantifies it, pins the exponent mean of the **in-budget prefix** at `4`, and the
deficit is confined to the block that exhausts the budget plus the `o(T_N)` blocks past it — which is
precisely where the reviewer's counterexample lives. The correction is therefore a statement about *where
the conversion lives*: unconditional below the budget, prefix-only above it, and never over the full horizon.
I recommend **Option 1** — keep AEH's asserted content distributional and correct the three sites to exactly
what follows — with one consequence the author must accept: the budget clause is not itself a distributional
clause, so `13.3.2`'s first reason has to be scoped to a fixed `(τ, θ)`, and `13.3.2`'s **second** reason
(Inselmann) becomes the one that carries the weight. That is a gain in honesty, not a loss: admissibility
caps `τ` at `4.8188…`, which *is* Inselmann's horizon, so every drift consequence AEH can reach lies inside
a range where a two-sided, uniform, unconditional envelope already holds.

**Round 3's framing was a defensible choice made on incomplete analysis, not an error of reasoning, and
this round overturns it on better information.** Detail at §4. Round 3 knew and wrote down that the
conversion is unavailable unconditionally past `τ < 1` (`v3r3-cut-weighting-findings.md` §11) and chose to
put it inside the hypothesis rather than prove it. What it did not check — and what makes the naming
insufficient — is whether the hypothesis *contains* it. It does not, in the form claimed.

---

## 1. The three sites, verified against the file (and a line-number correction)

The brief's line numbers are off by two on the two bullets. Verified against `aeh.md` at `fa9edf5`:

| brief says | actual line | text |
|---|---|---|
| L86, consistency bullet | **L84** | "…so the hypothesis says the first `T_N` blocks fit inside the budget, which is exactly `E_B[m + r] = 4` in Cesàro form." |
| L88–90, two-range table | **L86** (lead-in) + **L88–91** (fence) | "Reading the two ranges in blocks per bit is therefore a use of the hypothesis, not an input to it" + the two rows |
| L84, Inselmann ceiling | **L83** | "No `τ ≥ 4.8188…` is protected, and this is sharp rather than a gap in technique… Above the ceiling there is no orbit left to sample." |
| paper L315–329 | **L315–329** ✓ | the `protected`/`consistent`/`admissible` paragraph |

Four further sites carry the same claim and are in scope by consequence, not by the brief's list:

* `aeh.md` **L67** — "That window is `1/β` blocks per bit exactly on words whose blocks average
  `E[m + r] = 4` of exponent, so its block-per-bit reading is a consequence of the letter statistics
  asserted here". Correctly hedged as to *what* is asserted; needs one clause naming *which* clause of the
  hypothesis asserts it.
* `aeh.md` **L116** (`13.3.1`) — "along their first `⌈θ log₂ N⌉` blocks, all of them within budget."
* `paper` **L386–387** — "which is a theorem where the cylinder count runs and is
  Hypothesis~\ref{hyp:aeh} where it does not."
* `paper` **L394** — "all of them within the budget."
* `publication.md` **L29** — "a two-letter statistic that Thm 1.6 does not give and that `13.2.1` itself
  asserts"; and **L41** — "Claim no descent or drift consequence for AEH (aeh.md `13.3.2` carries none)."

The paper's **L362–367** paragraph is already correct and load-bearing — "That conversion is available here
precisely because the word is exactly `B` here" is the exact truth of §3 below — and survives verbatim.

### 1.1 The counterexample, reproduced

Synthetic words, letters iid geometric(1/2), `θ = 0.5`, one letter of size `cT` inserted at index
`T − √T` with `c = 3`, budget count `S_n = Σ_{i<n}(m_i + s_i)`, `s_i = r_{i−1}` (seed 40401):

| `T` | cemetery fraction | prefix mean `S_{n*−1}/T` | full mean `S_T/T` |
|---|---|---|---|
| 100 | 0.0900 | 3.780 | 7.350 |
| 400 | 0.0475 | 3.775 | 6.950 |
| 1600 | 0.0244 | 3.847 | 6.949 |
| 6400 | 0.0123 | 3.943 | 6.988 |

Identical at every `τ/θ ∈ {4.5, 4.05, 4.005}`. The cemetery vanishes, every fixed pattern frequency is
unmoved (one letter in `T`, plus `√T` cemetery symbols), the full mean sits at `4 + c = 7`, and the prefix
mean converges to `4`. Two controls, same code (seed 40402): a clean `B`-word gives cemetery `≈ 0` and both
means `→ 4` at every ratio; a word whose excess is *spread* (mean `5`) is **rejected** by the budget clause —
cemetery fraction `0.100 / 0.190 / 0.200` at ratios `4.5 / 4.05 / 4.005`, converging to `1 − (τ/θ)/5`, and
the prefix mean pinned at `τ/θ` exactly (`4.494 / 4.050 / 3.999`). That last row is the whole finding in one
line: **the budget clause forbids excess exponent that is spread out, and permits it only in the terminal
`o(T_N)` blocks.**

---

## 2. What `13.2.1` actually supplies about the budget — the exact residue

Write `Λ_N = ⌈τb⌉`, `T_N = ⌈θb⌉`, `S_n = Σ_{i<n}(m_i + s_i)` (the budget count), and
`n* = min{n ≤ T_N : S_n ≥ Λ_N}` (`= T_N` if none), so the tallied blocks are `0, …, n*−1`.

**(a) `n*/T_N → 1`.** `†` is one symbol and `B[†] = 0`, so its frequency among the `T_N` tallied symbols
tends to `0`; `S_n` is nondecreasing, so the cemetery is a suffix. **Correct reading of L84: "all but
`o(T_N)` of the first `T_N` blocks fit inside the budget", not "the first `T_N` blocks fit".**

**(b) A Fatou lower bound, from the `L = 1` marginal alone.** Each letter value's frequency among the
tallied symbols tends to its `B`-mass, so `liminf T_N^{-1}Σ_{n<n*} m_n ≥ E[m] = 2` and likewise for `r`;
dropping one index moves each *frequency* by at most `1/T_N`, so the same holds for `n < n*−1`. Hence
`liminf T_N^{-1}Σ_{n<n*−1}(m_n + s_n) ≥ 4`.

**(c) An upper bound, from the budget clause.** Block `n*−1` is tallied, so `S_{n*−1} < Λ_N`, i.e.
`T_N^{-1}Σ_{n<n*−1}(m_n + s_n) < Λ_N/T_N → τ/θ`. Consistency `4θ < τ` is exactly the statement that this
upper bound exceeds the Fatou lower bound, so at a **fixed** admissible pair the two do not meet.

**(d) Over the family they do meet, on the prefix.** `13.2.1` is quantified "for every admissible
`(τ, θ)`". For fixed `θ < 1/β` and every large `k`, `τ_k = θ(4 + 1/k)` is admissible (consistent by
construction, protected since `τ_k < 4.8188…`). Applying (c) at `τ_k` gives `≤ 4 + 1/k`; a diagonal in `k` —
the same step `13.3.1` already takes in `(k, D)` — gives `T_N^{-1}Σ_{n<n*−1}(m_n + s_n) → 4`. Then, since
each of `T_N^{-1}Σ m_n` and `T_N^{-1}Σ s_n` has `liminf ≥ 2` and their sum converges to `4`, **both converge
to `2`**, and by the altitude accounting of `13.2.3` the prefix descends at `2 log₂3 − 4 = −β` per block.

**(e) And they do not meet on the full horizon.** Nothing above touches block `n*−1` itself — the budget
clause is *predictable*, so the block that carries `S` across `Λ_N` is tallied at full weight and its own
letter is unbounded — nor the `T_N − n*` blocks past it. The counterexample of §1.1 lives exactly there. So
`T_N^{-1}Σ_{n<T_N}(m_n + r_n) → 4` **does not follow**, and with a letter of size `T_N²` it fails by an
unbounded amount.

**Consequence for `13.3.2`.** Its first reason — "convergence of window-state frequencies at each fixed `k`
gives `liminf` bounds but no `limsup` on `m_+`" — is **correct at a fixed pair and incomplete over the
family**. The missing `limsup` is supplied, on the prefix, not by the equidistribution clause but by the
budget clause. `13.3.2`'s second reason is unaffected and becomes the load-bearing one: admissibility caps
`τ` at `4.8188… = (1 − log₂√3)^{-1}`, which is Inselmann's own horizon, so the prefix of (d) is *by
construction* inside the range where Thm 1.1/1.10 gives a two-sided envelope, uniform in the time,
unconditional, at natural density 1. A conditional statement strictly inside an unconditional one is worth
nothing, exactly as `13.3.2` says. **Whichever option the author takes, this scoping of `13.3.2` is
required**, because it is a fact about `13.2.1` as round 3 wrote it, not about either option.

---

## 3. The asymmetry question: is the conversion a theorem below the budget? — **Yes, with a rate**

The brief's conjecture holds, and more cleanly than expected: the two clauses of admissibility are exactly
the two terms of `13.2.4`(a).

Take `4θ < τ < 1`, `J = Λ_N = ⌈τb⌉` in `13.2.4`(a)–(b). Then `η = 1 − τ`, and (b)'s standing hypothesis
`0 < η < 1 − 4θ` is *precisely* `4θ < τ`. The bound reads

```text
TV( Law(l_0,...,l_{T_N-1}),  B^(x T_N) )  <=  2^(Lam_N + 2)/N  +  P_B(S_{T_N} >= Lam_N)
                                              ^ vanishes iff tau < 1   ^ vanishes iff tau > 4theta
```

* **First term.** `2^(Λ_N+2)/N = O(N^{−(1−τ)})`, vanishing exactly for `τ < 1`. This is the *protected*
  clause, in its unconditional range.
* **Second term.** `P_B(S_n ≥ J) = P(Bin(J−1, 1/2) < 2n)` exactly (verified in exact rational arithmetic at
  six `(n,J)`, §11), with large-deviation rate

  ```text
  I(theta, tau) = tau * ( log 2 - H(2 theta / tau) )   nats per bit of start,   H = binary entropy in nats,
  ```

  positive exactly when `2θ/τ < 1/2`, i.e. **exactly when `4θ < τ`**, zero at `τ = 4θ`, and equal to the
  record's printed `I(θ) = log 2 − H(2θ)` at `τ = 1` (checked: `0.020136` at `θ = 0.20` and `0.00080021` at
  `θ = 0.24`, matching `aeh.md` L65's `0.0201` and `0.00080`). This is the *consistent* clause.

A total-variation bound transfers **every** event of the joint word law. So, off a set of starts of density
`≤ 2δ_N(τ) = e^{−Θ(b)}`:

1. **`P(S_{T_N} ≥ Λ_N) → 0`** — the budget is not binding, `†` never appears, and `13.2.1`'s tallied word
   *is* the untruncated letter word. This is the reviewer's missing estimate, and it is already inside
   `13.2.4`(b): the substitution is `η = 1 − τ`, nothing more.
2. **`T_N^{-1}Σ_{n<T_N}(m_n + r_n) → 4` in density**, with the exceptional density
   `≤ δ_N(τ) + 2e^{−c(ε)T_N}` — under `B^{⊗T_N}` the sum is the waiting time for the `2T_N`-th head, mean
   `4T_N`, geometric summands, hence Chernoff; and the deviation is an event of the joint law.

So: **the conversion `E_B[m+r] = 4` is a theorem about orbits for every `θ < 1/4`, and by `13.2.4`(f)'s own
identity `I(1/4) = 0` it is available from nothing in that lemma past it.** The shape is delegate B's
exactly (`v3r3-inselmann-horizon-findings.md` §2.5–2.6): the needed statistic is unconditionally available
precisely up to the digit budget and precisely nowhere past. This round adds that the statistic in question
is not only the pair-frequency but the *first moment*, and that its unavailability past the budget is not
merely "not proved" but **not implied by AEH either**, except in the prefix form of §2(d).

The `13.2.3` offset matters here and only here: `S_n` and `Σ(m_i + r_i)` differ by `s_n − s_0`, two unbounded
geometric letters. Inside the budget `max_{n ≤ T_N} s_n ≤ 2 log₂ T_N` off a set of `B`-mass `≤ 2/T_N`, which
the same TV bound transfers, so the offset is `O(log log N)` against `Λ_N = Θ(log N)` and is absorbed. At the
tallied set's boundary above the budget it is *not* absorbed — that single letter is the whole of §2(e).

---

## 4. Verdict on round 3's "named as AEH's own content" framing

**A defensible choice made without the check that would have refuted it, overturned here on better
information — not an error of reasoning.** Stated plainly, with the distinction the brief asks for.

What round 3 got right, and it is not small:

* It identified that the conversion was *being used* and was not a theorem, and said so
  (`v3r3-cut-weighting-findings.md` §6.1's table: "**part of the hypothesis** for `τ ≥ 1`. … it is the only
  clause that is not a theorem").
* It searched for an unconditional proof past `θ = 1/4` and reported, correctly and with a structural
  reason, that there is none (§11: "the missing object is a Cesàro upper bound on the exponent per block,
  i.e. `E[m + r] ≤ 4`, which is B's §2.5 circle: available unconditionally only from Terras's cylinder
  count, whose range is `τ < 1`").
* It made `τ` primitive, which is right for an independent reason this round confirms: `τ` is the unit the
  base case's two error terms are both stated in, and §3 shows admissibility's two clauses are exactly those
  two terms.
* Its closing sentence names the design intention exactly: "that is why the design puts the conversion
  inside the hypothesis rather than trying to prove it."

What it did not do, and what makes the naming insufficient:

* It checked that the conversion is **not a theorem** and never checked whether it is a **consequence of
  the hypothesis**. "Part of what `13.2.1` asserts" is a claim about the hypothesis's content, and no
  section of `v3r3-cut-weighting-findings.md` derives it. The step that was skipped is one line: `B[w] = 0`
  for words containing `†` gives vanishing *frequency* of `†`, and a vanishing frequency of an event is not
  a bound on a sum over the complement of that event.
* The gap was already on the page in the right shape. `13.3.2` had, since round 2, refused a drift
  consequence on the ground that equidistribution gives `liminf` but no `limsup` on an unbounded letter.
  L84's Cesàro claim is a `limsup` on the same unbounded letter, asserted from the same equidistribution.
  Round 3 rewrote the neighbourhood of both sentences in one pass and did not collide them.

So the naming was *honest* — it made the dependence visible, which is what it was for — and *insufficient*,
because visibility is not derivability. Round 3's own §11 is the document that should have caught it: having
established that `E[m+r] ≤ 4` is not available unconditionally, the next question is what makes it available
conditionally, and the answer (§2 above) is "the budget clause, on a prefix" and not "the frequency clause,
on the horizon". The distinction was reachable with the material in hand.

One thing round 3 did that this round does **not** overturn: the cemetery design itself. It is what makes
the tally denominator deterministic above the budget, it is predictable, and §2 shows it does real work —
it forbids spread-out excess exponent (§1.1's control row). What changes is only the reading of that work.

---

## 5. The two options, costed

### 5.1 Option 1 — keep AEH's asserted content distributional; correct the sites to exactly what follows

**Exact statement.** `13.2.1` and `13.2.2` unchanged, symbol for symbol. `13.2.3`'s *consistency* clause
`θ·E_B[m+r] < τ` is retained and re-read as **compatibility with the target law** — the condition under
which `B` itself predicts no out-of-budget block, hence the condition under which `π_{k,D}`'s giving `†` no
mass is not already contradicted by the model. What the hypothesis then delivers about the budget is §2:
`o(T_N)` cemetery, `4 ≤ liminf ≤ limsup ≤ τ/θ` on the in-budget prefix, and `→ 4` on that prefix over the
admissible family. What it does not deliver is the full-horizon mean.

| item | under Option 1 |
|---|---|
| `13.2.3` admissibility | unchanged as a definition; *consistent* re-read as model-compatibility. Both clauses gain a sharper identity: they are the two terms of `13.2.4`(a) (§3) |
| the two-range table | both rows survive as arithmetic on the definition (`θ < 1/4` ⟺ an admissible `τ < 1` exists; `θ < 1/β` ⟺ an admissible `τ < 4.8188…` exists). The annotation changes: the divisor is the target law's mean, a theorem about orbits below the budget and a prefix consequence above it |
| paper §5 | L322–329 restated; L386–387 gains a range qualifier; L394 "all of them" → "all but `o(T_N)`, and all of them when `τ < 1`". L362–367 unchanged |
| newly claimed | `13.2.4`(g): the budget clause and the exponent mean, unconditionally, for `θ < 1/4`. `13.2.6`: the prefix form, conditionally, above it |
| no longer claimed | that AEH says the first `T_N` blocks fit inside the budget; that it says "exactly `E_B[m+r] = 4` in Cesàro form"; that the divisor `4` is `13.2.1`'s own content without qualification |
| `13.3.2` consistent? | **only after its first reason is scoped to a fixed pair.** The budget clause does supply a prefix `limsup`. Reason 2 then carries the weight, and carries it easily: the prefix is inside Inselmann's window by construction |
| calibration | untouched. The campaign measures frequencies; the flagship's `4.0017` exponent per block at `τ ≈ 2.29` becomes a measurement *of* the prefix statement rather than of an asserted clause |
| `13.6` (the name) | untouched. AEH remains "the integers inherit Bernoulli genericity at scale" — a frequency statement, which is what `13.6.2`/`13.6.4`/`13.6.6` are about |
| novelty ledger | improves. `13.2.4`(g) is a small unconditional gain inside the budget; nothing conditional is added that Inselmann already owns |

**Cost.** The record loses a clean sentence and gains three careful ones. `13.3.2` needs surgery. And the
record must state a conditional consequence (the prefix drift) that it currently says it carries none of —
uncomfortable in a round whose purpose is subtraction, but the alternative is to leave a false
understatement in `13.3.2` for a fifth reviewer to find.

### 5.2 Option 2 — add an explicit non-binding-budget clause

**Exact statement.** Append to `13.2.1` (and by the dictionary to `13.2.2`): *"and, at every admissible
`(τ, θ)`, the density of starts with `S_{T_N} ≥ Λ_N` tends to `0`."* This is the better of the two shapes —
strictly weaker than a bare moment clause, and it is *exactly* what `13.2.4`(g) proves below the budget, so
the hypothesis would be the literal extension of its own base case. (A bare moment clause
`T_N^{-1}Σ(m_n + r_n) → 4` is the alternative shape; it is implied by this one via §2(b)+(d) and has no
compensating advantage.)

| item | under Option 2 |
|---|---|
| `13.2.3` admissibility | *consistent* becomes a genuine sub-claim of the hypothesis rather than a compatibility condition. Both L84 and paper L324 become true **as written** |
| the two-range table | the annotation "the divisor `4` is `13.2.1`'s own content" becomes literally correct |
| the cemetery | becomes decoration: off a vanishing density `†` never appears. It still has to stay, to keep the tally well-defined on the exceptional set, but it stops doing work |
| paper §5 | L322–329 needs only the added clause; L394's "all of them within the budget" survives verbatim |
| newly claimed | `T_N^{-1}Σ_{n<T_N}(m_n + r_n) → 4` over the full horizon, hence `Σm/T_N → 2`, `Σs/T_N → 2`, hence a **full-horizon block drift of `−β`** — a conditional descent statement |
| `13.3.2` consistent? | **no, not as written.** "No drift or contraction consequence is carried" must be withdrawn outright and replaced by "a drift consequence follows and is worth nothing". Reason 1 is deleted, not scoped |
| `13.6` (the name) | **damaged.** Genericity is a frequency notion. `13.6.2`'s Bernoulli identification, `13.6.4`'s equivalence and `13.6.6`'s "this null set inherits genericity" are all statements about pattern frequencies; a tail-probability clause is a different genre and would have to be carried through `13.6.4`'s statement as a separate hypothesis on both sides. AEH would no longer be exactly the assertion that the integers are generic points |
| calibration | the clause is partly calibrated already (the flagship's `4.0017` per block at `τ ≈ 2.29`), which is the honest point in its favour; but no run measures `P(S_{T_N} ≥ Λ_N)` at `τ` near `4θ`, which is where the clause bites |
| novelty ledger | **worsens.** The clause's entire new consequence is a conditional descent/drift statement whose range of validity — capped by admissibility at `4.8188…` — is *exactly* the range Inselmann covers unconditionally, two-sidedly and uniformly in the time. `publication.md` already records "Claim no descent or drift consequence for AEH"; this would be a strengthening of the hypothesis purchased entirely to buy back something the record has already conceded |

**Cost, in one sentence.** Option 2's marginal content over Option 1 is the terminal `o(T_N)` blocks plus one
letter, and what that margin buys is a drift theorem that already exists unconditionally.

---

## 6. Recommendation (for the author to accept or overturn — not settled here)

**Option 1**, in the sharpened form of §7: correct the three sites, add `13.2.4`(g) and `13.2.6`, and scope
`13.3.2`'s first reason.

**One-line reason.** Option 2 strengthens the hypothesis out of its own genre — genericity — to buy a
conditional drift statement whose entire range is inside an unconditional theorem, while Option 1 costs only
sentences and gains an unconditional result (`13.2.4`(g)) the record did not have.

**The strongest argument the other way, stated fairly.** Option 2 makes the record's existing sentences true
as written, keeps the cemetery honest as a device rather than a claim, and posits only what the base case
already proves — a hypothesis that is the literal extension of its own theorem is a cleaner object than one
that is the extension of part of it. If the author weighs "the hypothesis extends its base case exactly"
above "the hypothesis is a genericity statement", Option 2 is the right call and §8 is sufficient to switch.

**What is not optional under either.** §2's finding that the budget clause is not a distributional clause,
and the resulting scoping of `13.3.2`'s first reason. That is a fact about `13.2.1` as it stands.

---

## 7. Drop-in text — Option 1 (recommended)

Verbatim replacements. Surrounding sentences and anchors are preserved; nothing is renumbered; two anchors
are appended (`13.2.4`(g) and `13.2.6`).

### 7.1 `aeh.md` L83 — the Inselmann ceiling bullet

Replace the whole bullet with:

````markdown
* At `τ = (1 − log₂√3)^(-1) = 4.8188…` the cited theorems' range ends, and the hypothesis is not quantified at or above it. What the source supports, exactly: Thm `1.1`'s envelope is quantified only for `k ≤ (1 − log₂√3)^(-1) log₂ m` and gives nothing in either direction past that; inside the range its *upper* side puts the altitude at budget `τ` at `(1 − τ/4.8188…)log₂ N ± ε log₂ N`, and Cor `1.4` states the endpoint case directly — `T_1^(⌊log₂ m/(1 − log₂√3)⌋)(m) ≤ m^ε` at natural density `1`, for every fixed `ε > 0`. So at the ceiling the orbit is already at `N^(o(1))`, the order of the cuts the definition admits, and protection there is not available. Past the ceiling the reason for stopping is that the descent has happened and `13.1`'s bottom regime is no longer excluded from the tally; `13.6.6` records that the unrestricted statement is false on a convergent orbit. This is a scope decision resting on a proved descent, not a proof that no `τ` above the ceiling is protected — a convergent orbit past the descent still supplies blocks; what it no longer supplies is bulk ones.
````

### 7.2 `aeh.md` L84 — the consistency bullet

Replace the whole bullet with:

````markdown
* Consistency is **compatibility with the target law**, not a claim about orbits: under `B` a block spends `E_B[m + r] = 4` of exponent, so `4θ < τ` says exactly that `B` itself predicts no out-of-budget block — the condition under which `π_{k,D}`'s giving `†` no mass is not already contradicted by the model. For `τ < 1` it is more, and unconditionally: `13.2.4`(g) proves that no block of the horizon leaves the budget and that the empirical exponent mean converges to `4`. For `τ ≥ 1` the hypothesis delivers neither, and what it does deliver is `13.2.6` — `†` has vanishing frequency, so all but `o(T_N)` of the first `T_N` blocks are in budget; the exponent mean of the in-budget prefix is bounded below by `E_B[m + r] = 4` (Fatou on the letter marginals) and above by `τ/θ` (the budget itself), and taking `τ ↓ 4θ` through admissible pairs pins it at `4`. What is not delivered is any control of the block at which the budget is exhausted — the clause is predictable, so that block is tallied at full weight and its own letter is unbounded — or of the `o(T_N)` blocks past it. Hence `T_N^(−1)Σ_(n<T_N)(m_n + r_n) → 4` does **not** follow, and can fail by any amount.
````

### 7.3 `aeh.md` L86 and L88–91 — the lead-in and the two-range table

Replace the lead-in sentence, the fenced block and the sentence following it with:

````markdown
Both ranges read in blocks per bit through the same divisor, `E_B[m + r] = 4`, and the two readings do not have the same status:

```text
4θ < τ < 1          <=>  θ < 1/4        every clause a theorem, the divisor included (13.2.4(g))
4θ < τ < 4.8188...  <=>  θ < 1/beta     the admissible range; the divisor is the target law's mean,
                                        and only 13.2.6's prefix form says an orbit realizes it
```

with `1/β = 1.2047…`, `β = 2(2 − log₂3) = 0.8301…`, and `4/β = (1 − log₂√3)^(-1)` an identity. Each equivalence is arithmetic on the definition of consistency — `θ < 1/4` says an admissible `τ < 1` exists, `θ < 1/β` says an admissible `τ < 4.8188…` does — and neither is by itself a statement about any orbit. `β`'s leading factor `2` is `E[m] = 2` Syracuse steps per block, so "`1/β` blocks per bit" carries a conversion of the same kind inside its own definition; below the budget that conversion is `13.2.4`(g), and past it it is `13.2.6`'s prefix statement and nothing stronger.
````

### 7.4 `aeh.md` L69 — `13.2.3`'s gap sentence

Replace the final sentence of the paragraph ("The gap is `O(1)` in a budget of `Θ(log N)`, the same one-index
offset `13.6.3`(i)(a) records, and nothing below distinguishes them.") with:

````markdown
The gap is exactly `s_n − s_0`, a difference of two geometric letters: `O_P(1)` with geometric tails, not a deterministic `O(1)`, since letters are unbounded. It is negligible where it is used — `max_(n ≤ T_N) s_n ≤ 2 log₂ T_N` off a set of `B`-mass `≤ 2/T_N`, hence `O(log log N)` against a budget of `Θ(log N)` — and it is the same one-index offset `13.6.3`(i)(a) records. Nothing below distinguishes the two counts except at the boundary of the tallied set, where the offset is the single letter that carries `S` across the budget (`13.2.6`).
````

### 7.5 `aeh.md` L97 — `13.2.4`(a)'s index

Replace `P_B(S_(n+1) ≥ J)` with `P_B(S_n ≥ J)`, so the bullet's first sentence reads:

````markdown
* **(a) Word law.** For every `n ≥ 0` and every `J ≥ 2`, `TV(Law(ℓ_0, …, ℓ_(n−1)), B^(⊗n)) ≤ 2^(J+2)/N + P_B(S_n ≥ J)`. For `N = 2^b` and `J = b` the first term is `0`.
````

The proof below it is already stated for the sharp form and needs no change: the good event is
`S(W) + 1 ≤ J` on a word of `n` letters, so the excluded event is `{S_n ≥ J}`, whose `B`-mass (b) computes
exactly. The printed `S_(n+1)` gives a valid but non-sharp bound and is the only site in the record carrying
it — the base-case display at L61–62 and the paper's L343 both print `S_n`.

### 7.6 `aeh.md` — new item `13.2.4`(g), appended after (f)

````markdown
* **(g) The budget clause, and the exponent mean.** Let `4θ < τ < 1` and put `Λ_N = ⌈τb⌉`. Take `J = Λ_N` in (a)–(b), i.e. `η = 1 − τ`; then (b)'s hypothesis `0 < η < 1 − 4θ` is *exactly* the consistency clause `4θ < τ`, and the two clauses of admissibility are exactly the two terms of (a): `τ < 1` is what makes the window term `2^(Λ_N+2)/N = O(N^(−(1−τ)))` vanish, and `4θ < τ` is what makes the tail term vanish, at the exact rate `I(θ, τ) = τ(log 2 − H(2θ/τ))` nats per bit of start (`H` the binary entropy in nats) — positive precisely for `τ > 4θ`, `0` at `τ = 4θ`, and equal to (b)'s `I(θ) = log 2 − H(2θ)` at `τ = 1`. Write `δ_N(τ)` for the sum of the two terms, `e^(−Θ(b))`. Because a total-variation bound transfers **every** event of the joint word law:
  * **The budget does not bind.** `P(S_{T_N} ≥ Λ_N) ≤ 2δ_N(τ) → 0`. Off that set no block of the horizon is tallied `†`, so `13.2.1`'s tallied word is the letter word of (d) and `13.2.2`'s tallied blocks are those of (e). (The budget clause counts `Σ(m_i + s_i)` and (a)–(b) count `Σ(m_i + r_i)`; by `13.2.3` the two differ by `s_n − s_0`, and `max_(n ≤ T_N) s_n ≤ 2 log₂ T_N` off a `B`-event of mass `≤ 2/T_N`, which the same bound transfers and which `δ_N` absorbs.)
  * **The exponent mean converges to `E_B[m + r] = 4`.** For every `ε > 0` the density of starts with `|T_N^(−1)Σ_(n<T_N)(m_n + r_n) − 4| > ε` is at most `δ_N(τ) + 2e^(−c(ε)T_N) → 0`: under `B^(⊗T_N)` the sum is the waiting time for the `2T_N`-th head, of mean `4T_N` with geometric summands, so Chernoff applies, and the deviation is an event of the joint law.

  This is the conversion `E_B[m + r] = 4` as a theorem about orbits, and its range is the cylinder count's own: every `θ < 1/4`, and by (f)'s identity `I(1/4) = 0` nothing in this lemma past it.
````

### 7.7 `aeh.md` L104 — Corollary `13.2.4.1`

Replace the corollary with:

````markdown
**Corollary 13.2.4.1.** For every admissible `(τ, θ)` with `τ < 1` — equivalently, by `13.2.3`, every `θ < 1/4`, since `4θ < τ < 1` is solvable exactly then — and every cut sequence `(X_N)` as above: by `13.2.4`(g) the budget binds on a set of density `e^(−Θ(b))`, so off that set `13.2.1`'s tallied word is the letter word of `13.2.4`(d) and `13.2.2`'s tallied window blocks are those of `13.2.4`(e). Hence `13.2.4`(d) is the conclusion of Hypothesis `13.2.1` and `13.2.4`(e) is the conclusion of Hypothesis `13.2.2`, at every admissible `τ < 1` and not at one only; both hold unconditionally in that range, at every finite block length, and so does the consistency clause they are quantified by.
````

### 7.8 `aeh.md` — new anchor `13.2.6`, appended to §13.2 (after the "Scope, stated once" paragraph, L110)

````markdown
**Proposition 13.2.6 (what the budget clause supplies past the base case, and what it does not).** Fix `θ` with `4θ < (1 − log₂√3)^(-1)` and suppose `13.2.1` holds at every admissible `(τ, θ)`, as it is quantified. Put `n* = min{n ≤ T_N : S_n ≥ Λ_N}` (`= T_N` if there is none), so the tallied blocks are `0, …, n*−1`. Then, off a vanishing density of starts:

1. **The cemetery is a vanishing suffix.** `†` is one symbol and `B[†] = 0`, so its frequency among the `T_N` tallied symbols tends to `0`; `S_n` is nondecreasing, so `T_N − n* = o(T_N)` and `n*/T_N → 1`.
2. **The in-budget prefix is trapped between `4` and `τ/θ`.** Block `n*−1` is tallied, so `T_N^(−1)Σ_(n<n*−1)(m_n + s_n) = T_N^(−1)S_(n*−1) < Λ_N/T_N → τ/θ`; and `liminf T_N^(−1)Σ_(n<n*−1)(m_n + s_n) ≥ E[m] + E[r] = 4` by Fatou on the letter marginals, each letter value's frequency among the tallied symbols tending to its `B`-mass and one dropped index moving every frequency by `1/T_N`. Only the `L = 1` marginal form (`13.2.2` at `L = 1`) is used. Consistency `4θ < τ` is exactly the statement that the two bounds do not meet at a fixed pair.
3. **Over the admissible family they meet, and the prefix carries the mean.** `τ_k = θ(4 + 1/k)` is admissible for every large `k`, so 2 reads `≤ 4 + 1/k`; the diagonal in `k` — the step `13.3.1` takes in `(k, D)` — gives `T_N^(−1)Σ_(n<n*−1)(m_n + s_n) → 4`. Since `T_N^(−1)Σ m_n` and `T_N^(−1)Σ s_n` each have `liminf ≥ 2` and sum to `4` in the limit, both converge to `2`; by the altitude accounting of `13.2.3` the first `n*−1` blocks then descend at `2 log₂3 − 4 = −β` per block, the per-step approximation error being `O(1/x_exit)` and summable inside the budget by the altitude bound.
4. **The deficit, exactly located.** Nothing above reaches block `n*−1` itself — the budget clause is *predictable*, so the block carrying `S` across `Λ_N` is tallied at full weight and its letter is unbounded — or the `T_N − n*` blocks past it. A single letter of size `cT_N` at index `T_N − √T_N`, with the following `√T_N` blocks in the cemetery, leaves every fixed pattern frequency at its `B`-value and the cemetery frequency at `O(T_N^(−1/2))`, while moving `T_N^(−1)Σ_(n<T_N)(m_n + r_n)` from `4` to `4 + c`; at size `T_N²` it moves it without bound. **So `T_N^(−1)Σ_(n<T_N)(m_n + r_n) → 4` does not follow from `13.2.1` at any admissible `(τ, θ)` with `τ ≥ 1`, and can fail by any amount.** The missing input is uniform integrability of the letter sizes over the terminal `o(T_N)` blocks — the same input `13.3.2` names, in the same shape.

**Scope.** 3 is a conditional drift consequence and is priced at zero by `13.3.2`'s second reason, not its first: admissibility caps `τ` at the descent horizon `4.8188…` itself, so the prefix of 3 lies by construction inside the range where Inselmann's envelope is unconditional, two-sided and uniform in the time. Below the budget the whole proposition is superseded by `13.2.4`(g), which gives the full horizon and not a prefix.
````

### 7.9 `aeh.md` L118 — `13.3.2`'s first reason

Replace the sentence beginning "First, it does not follow:" up to "…equidistribution does not supply." with:

````markdown
First, it does not follow from equidistribution: the per-block increment is `m_+·(log₂3 − 1) − s`, and `m_+`, `s` are unbounded; convergence of window-state frequencies at each fixed `k` gives `liminf` bounds on their empirical means (Fatou) but no `limsup` on `m_+`, and the drift needs the latter, i.e. a uniform-integrability input equidistribution does not supply. What supplies a partial substitute is the *budget* clause rather than the frequency clause, and it reaches exactly as far as `13.2.6`: over the admissible family the in-budget prefix does carry `E_B[m + r] = 4` and hence `−β` per block, while the block that exhausts the budget and the `o(T_N)` blocks past it are uncontrolled, so nothing follows about the first `T_N` blocks as a whole and no uniform-integrability input has been found. Second — and this is why the first reason is not the load-bearing one, since `13.2.6` shows a prefix form does follow — it would be worth nothing if it did:
````

and continue with the existing text from "the corresponding trajectory statement is an unconditional
theorem at natural density `1`." One clause is added at the end of the Inselmann sentence, after
"…`13.2.1`'s admissible ceiling `θ = 1/β` (`13.2.3`)":

````markdown
— so `13.2.6`'s prefix lies inside that window by construction, admissibility capping `τ` at the same `4.8188…`
````

### 7.10 `aeh.md` L67 — one clause

Replace "so its block-per-bit reading is a consequence of the letter statistics asserted here, not
independent corroboration of them" with:

````markdown
so its block-per-bit reading is a consequence of what is asserted here — of the budget clause, in the prefix form of `13.2.6`, and unconditionally only inside the digit budget (`13.2.4`(g)) — and not independent corroboration of it
````

### 7.11 `aeh.md` L116 — `13.3.1`'s budget clause

Replace "along their first `⌈θ log₂ N⌉` blocks, all of them within budget" with:

````markdown
along their first `⌈θ log₂ N⌉` blocks, all but `o(⌈θ log₂ N⌉)` of them within budget — all of them when `τ < 1`, by `13.2.4`(g)
````

### 7.12 `aeh.md` L8 — the Current-state blockquote, one clause

Replace "There is no drift or contraction consequence: equidistribution at each fixed `k` does not deliver
one, and the corresponding trajectory statement is unconditionally known anyway (13.3.2)." with:

````markdown
There is no drift or contraction consequence worth carrying: equidistribution at each fixed `k` delivers none, the budget clause delivers one only along the in-budget prefix (13.2.6), and the corresponding trajectory statement is unconditionally known across the whole admissible range anyway (13.3.2).
````

### 7.13 `paper/collatz-reduced-v3.tex` L322–329

Replace those eight lines (from "Consistency is a theorem where" through "hypothesis itself supplies.")
with:

````latex
Consistency is compatibility with the target law rather than a claim about
orbits: under $B$ a block spends $\mathbb{E}_B[m+r] = 4$ of exponent, so
$4\theta < \tau$ says exactly that $B$ itself predicts no out-of-budget block,
which is what $\pi_{k,D}$'s giving $\dagger$ no mass requires. Where the cylinder
count runs it is more, and unconditionally: for $\tau < 1$ no block of the horizon
leaves the budget and the empirical exponent mean converges to $4$
(\texttt{aeh.md} Lemma 13.2.4(g), whose two error terms are precisely the two
clauses of admissibility). Past that range the hypothesis supplies less. That
$\dagger$ has vanishing frequency says all but $o(T_N)$ of the first $T_N$ blocks
are in budget, and pins the exponent mean of the in-budget prefix at
$\mathbb{E}_B[m+r] = 4$ once $\tau$ is taken down to $4\theta$ through admissible
pairs; but the block at which the budget is exhausted is tallied at full weight
and its letter is unbounded, and the $o(T_N)$ blocks past it are uncontrolled, so
$T_N^{-1}\sum_{n<T_N}(m_n+r_n) \to 4$ does not follow and can fail by any amount
(\texttt{aeh.md} Proposition 13.2.6). Hence $4\theta < \tau < 1$ is
$\theta < 1/4$ and $4\theta < \tau < 4.8188\ldots$ is
$\theta < 1/\beta = 1.2047\ldots$, where $\beta = 2(2-\LL) = 0.8301\ldots$ is the
classical per-block contraction rate and $4/\beta = (1-\log_2\sqrt3)^{-1}$ is an
identity --- each of these being arithmetic on the definition of consistency,
with the divisor in either block reading the mean of the target law: a theorem
about orbits below the budget, and a statement about a prefix above it.
````

### 7.14 `paper/collatz-reduced-v3.tex` L385–387

Replace "the endpoints read as $1/4$ and $1/\beta$ blocks per bit / only after dividing by the mean exponent
per block, which is a theorem where the / cylinder count runs and is Hypothesis~\ref{hyp:aeh} where it does
not." with:

````latex
the endpoints read as $1/4$ and $1/\beta$ blocks per bit
only after dividing by the mean exponent per block, which is a theorem where the
cylinder count runs (\texttt{aeh.md} Lemma 13.2.4(g)) and, past it, is supplied
by Hypothesis~\ref{hyp:aeh} along the in-budget prefix only and not over the full
horizon (\texttt{aeh.md} Proposition 13.2.6).
````

### 7.15 `paper/collatz-reduced-v3.tex` L393–394

Replace "carry those frequencies along their first / $T_N$ blocks, all of them within the budget." with:

````latex
carry those frequencies along their first
$T_N$ blocks, all but $o(T_N)$ of them within the budget --- and all of them when
$\tau < 1$.
````

### 7.16 `paper/collatz-reduced-v3.tex` L246 — one clause in the \S5 preamble

Replace "so no drift or contraction statement about orbits follows from it (\texttt{aeh.md} \S13.3.2)" with:

````latex
so no drift or contraction statement about orbits follows from equidistribution alone; the budget clause reaches only the in-budget prefix, and what it reaches there is unconditional anyway (\texttt{aeh.md} \S13.3.2, Prop.~13.2.6)
````

### 7.17 `publication.md` L29 and L41

L29, replace "a two-letter statistic that Thm 1.6 does not give and that `13.2.1` itself asserts" with:

````markdown
a two-letter statistic that Thm 1.6 does not give, that `13.2.1` supplies only along its in-budget prefix (aeh.md `13.2.6`), and that is unconditional only inside the digit budget (aeh.md `13.2.4`(g))
````

L41, replace "**Claim no descent or drift consequence for AEH** (aeh.md `13.3.2` carries none)." with:

````markdown
**Claim no descent or drift consequence for AEH.** The only one available is `13.2.6`'s in-budget prefix form, which admissibility places inside Inselmann's own window by construction and which is strictly weaker than his theorem in every respect (aeh.md `13.3.2`).
````

### 7.18 Optional precision, flagged not required

`paper` L321 cites `\cite[Thm.~1.10]{inselmann}` for protection, but protection is stated in the budget
count `S_n`, which is `T_1`-time; Thm 1.1 is the `T_1`-envelope and Thm 1.10 the Syracuse one. `aeh.md` L82
already cites both. `\cite[Thms.~1.1 and~1.10]{inselmann}` would match. Also `aeh.md` L58 says "for every
`J ≥ 1`" where `13.2.4`(a) and the paper say `J ≥ 2`; at `J = 1` the bound is vacuous rather than false, so
nothing is wrong. Neither is required by this round.

---

## 8. Drop-in text — Option 2 (rejected), at switching resolution

Sufficient to switch without another round.

**(i) `aeh.md` `13.2.1`, final sentence.** After "…for every **admissible** `(τ, θ)` in the sense of
`13.2.3`", append: *"Asserted with it, at every admissible `(τ, θ)`: the density of starts with
`S_{T_N} ≥ Λ_N` tends to `0` — the budget does not bind within the horizon."* Mirror in `13.2.2` ("same
budget, same tallied blocks, same non-binding clause") and in the paper's `hypothesis` environment after
L275.

**(ii) `aeh.md` L84.** The bullet becomes: *"Consistency is a theorem for `τ < 1` — `13.2.4`(g) — and is
**part of what `13.2.1` asserts** for `τ ≥ 1`, by the non-binding clause: the first `T_N` blocks fit inside
the budget, so `T_N^(−1)Σ_(n<T_N)(m_n + r_n) ≤ τ/θ`, and with the Fatou bound `≥ E_B[m + r] = 4` and `τ ↓ 4θ`
through admissible pairs this is exactly `E_B[m + r] = 4` in Cesàro form."* The current bullet's conclusion
survives; only its derivation is printed.

**(iii) The two-range table.** Row 2's annotation survives as written ("the divisor `4` is `13.2.1`'s own
content"), with `13.2.4`(g) cited on row 1.

**(iv) `13.3.2`.** "No drift or contraction consequence is carried, for two independent reasons" must be
replaced outright: *"A drift consequence does now follow — the non-binding clause plus Fatou gives
`T_N^(−1)Σ m_n → 2` and `T_N^(−1)Σ s_n → 2`, hence `−β` per block over the whole horizon — and it is worth
nothing: the corresponding trajectory statement is an unconditional theorem at natural density `1` over
exactly the admissible range, admissibility capping `τ` at Inselmann's own `4.8188…`."* Then the existing
Inselmann paragraph, unchanged.

**(v) `13.6.4`.** The equivalence is between two frequency statements and does not carry the new clause.
Add to the "Corollary and recorded qualifiers" block a third qualifier: *"(q3) The non-binding-budget clause
of `13.2.1`/`13.2.2` is a statement about a tail probability, not about bulk frequencies, and the
equivalence above neither uses nor delivers it; it is a letter-word event, so it transfers unchanged between
the two forms, but it is carried as a separate hypothesis on both sides."*

**(vi) `13.6.6`.** The sentence "AEH is the assertion that this particular null set inherits genericity at
scale" must gain "…together with a non-binding-budget clause that is not itself a genericity statement".

**(vii) `paper`.** L322–324 survives verbatim; L325–329 survives verbatim; L394 survives verbatim; the
hypothesis environment gains the clause; L246's drift clause is replaced as in (iv). `13.2.4`(g) and the
`13.2.3` and `13.2.4`(a) corrections of §7.4–7.7 are **unchanged under either option** — they are
independent of the choice.

**(viii) `publication.md`.** L41's "Claim no descent or drift consequence for AEH" is withdrawn and replaced
by "the AEH descent consequence is conditional, full-horizon, and strictly weaker than Inselmann's
unconditional theorem over the same range; claim it only with that comparison attached."

---

## 9. Consequence trace

| # | Item | Verdict | Note |
|---|---|---|---|
| 1 | `13.2.1`, `13.2.2` as statements | **Survive verbatim** | Not touched by Option 1. Option 2 appends one clause to each |
| 2 | `13.2.3`'s clock paragraph | **Survives; final sentence restated** | `O(1)` → `O_P(1)`, with the exact gap `s_n − s_0` and where it matters (§7.4) |
| 3 | `13.2.3`'s `protected` definition | **Survives verbatim** | Unchanged by anything here |
| 4 | `13.2.3`'s `consistent` definition | **Survives verbatim as a definition; its reading changes** | From "part of what the hypothesis asserts" to "compatibility with the target law, plus `13.2.4`(g) below the budget and `13.2.6` above it" |
| 5 | `13.2.3` bullet 1 (`τ < 1` protected) | **Survives verbatim** | The altitude bound is universal |
| 6 | `13.2.3` bullet 2 (`τ < 4.8188…` protected) | **Survives verbatim** | Correctly hedged already |
| 7 | `13.2.3` bullet 3 (the ceiling) | **Fails as written; survives restated** | §7.1. "No `τ ≥ 4.8188…` is protected" and "no orbit left to sample" are not in the source |
| 8 | `13.2.3` bullet 4 (consistency) | **Fails as written; survives restated** | §7.2. The blocking finding |
| 9 | The two-range table, row 1 | **Survives; annotation strengthens** | The divisor is now a theorem too, by `13.2.4`(g) |
| 10 | The two-range table, row 2 | **Survives as arithmetic; annotation fails** | §7.3 |
| 11 | `13.2.4`(a) | **Index error; corrected** | `S_(n+1)` → `S_n`; the proof and (b) already state the sharp form |
| 12 | `13.2.4`(b)–(f) | **Survive verbatim** | (b) already contains the budget step with `η = 1 − τ` |
| 13 | `13.2.4`(g) | **New** | §7.6. Unconditional; the budget clause and the exponent mean, `θ < 1/4` |
| 14 | Corollary `13.2.4.1` | **Fails as a deduction; survives restated** | Needed (g) to identify the tallied word with the letter word, and to quantify over `τ` |
| 15 | `13.2.4`'s **Verified** block | **Survives verbatim** | Nothing measured is affected. (g) adds no new computational claim beyond the tail identity already verified there |
| 16 | `13.2.5` | **Survives verbatim** | The shell argument never inspects the property |
| 17 | `13.2.6` | **New** | §7.8. Conditional; the prefix form and the exact deficit |
| 18 | `13.3.1` (ledger) | **Survives; one clause** | "all of them within budget" → "all but `o(T_N)`; all of them when `τ < 1`" |
| 19 | `13.3.2`, the `1/3` rate | **Survives verbatim** | Unaffected |
| 20 | `13.3.2`, reason 1 (no `limsup`) | **Fails as scoped; survives restated** | Correct at a fixed pair, incomplete over the family. §7.9. **Required under either option** |
| 21 | `13.3.2`, reason 2 (worth nothing) | **Survives verbatim, and becomes load-bearing** | Admissibility's ceiling *is* Inselmann's horizon, so every reachable drift consequence is inside it |
| 22 | `13.3.2`'s Inselmann paragraph | **Survives; one clause added** | The range-containment clause, §7.9 |
| 23 | `13.3.3` (scope) | **Survives verbatim** | Density statements, no iteration, staircase tails not excluded — none of it touched |
| 24 | `13.4`, `13.5` | **Survive verbatim** | The flagship's `4.0017` per block is re-read as a measurement of `13.2.6`'s prefix statement, not of an asserted clause |
| 25 | `13.6.1`–`13.6.3` | **Survive verbatim** | `13.6.3`(i)(a)'s one-index offset is now cited by `13.2.3`'s corrected sentence |
| 26 | `13.6.4` and (q1), (q2) | **Survive verbatim under Option 1** | Frequency statements only. Under Option 2 they need (q3), §8(v) |
| 27 | `13.6.5` | **Survives verbatim** | Untouched |
| 28 | `13.6.6` (the name) | **Survives verbatim under Option 1** | Genericity is preserved. Under Option 2 it must be qualified, §8(vi) |
| 29 | `13.6.7` | **Survives verbatim** | Untouched |
| 30 | `aeh.md` L8 blockquote | **Survives; one clause** | §7.12 |
| 31 | `aeh.md` L2 status header | **Survives verbatim** | "unconditional base case PROVED at 13.2.4 (every `θ < 1/4`, at every block length)" is unaffected and is strengthened by (g) |
| 32 | `aeh.md` L67 | **Survives; one clause** | §7.10 |
| 33 | `paper` L246 | **Survives; one clause** | §7.16 |
| 34 | `paper` L248–290 (`hyp:aeh` and the window form) | **Survive verbatim** | Not touched by Option 1 |
| 35 | `paper` L292–321 | **Survive verbatim** | The ensemble paragraph, the horizon paragraph and the `protected` definition are all correct |
| 36 | `paper` L322–329 | **Fails; restated** | §7.13 |
| 37 | `paper` L331–360 (base case) | **Survives verbatim** | Already prints `P_B(S_n \ge J)` |
| 38 | `paper` L362–367 | **Survives verbatim, and is the model sentence** | "That conversion is available here precisely because the word is exactly `B` here" is exactly §3's finding |
| 39 | `paper` L385–387 | **Survives restated** | §7.14 |
| 40 | `paper` L389–394 | **Survives; one clause** | §7.15 |
| 41 | `paper` L404–419 (Inselmann) | **Survives verbatim** | Already says the block-time passage "is therefore a consequence of Hypothesis 5.1 and not available to underwrite it" — correct under Option 1 once `13.2.6` fixes what "consequence" means |
| 42 | `paper` L433–439 (Calibration) | **Survives verbatim** | Untouched |
| 43 | `publication.md` L29, L41 | **Survive restated** | §7.17 |
| 44 | `publication.md` L44, L45 | **Survive verbatim** | The unfound-residue list and the density note are unaffected |
| 45 | `index.md` L46, `open-problems.md` L86, `stage1.md` L579, L620 | **Survive verbatim** | All four cite `13.2.4`(d)–(e)/`13.2.4.1`'s conclusion inside the budget, which (g) strengthens rather than moves |
| 46 | `experiments/*` | **Untouched** | Nothing here needs a run. §10 item 4 names the one measurement that would be new |
| 47 | Appendix A commit pin (`paper` L447) | **Moves on any `aeh.md` edit** | Settled apply-wave mechanic; not this brief's |

---

## 10. Open questions

1. **Whether `13.2.6` should be a numbered anchor at all.** I recommend it, because §2(d) is a derivation
   that has to be checkable and because without it `13.3.2`'s first reason cannot be scoped honestly. But it
   is new material entering the record in a round whose purpose is subtraction, and the author may prefer to
   compress it into the L84 bullet and drop the anchor. §7.2's bullet is written so that it still reads
   correctly with the pointer changed to a parenthetical derivation.
2. **How tightly `τ` may approach `4θ`.** All of §2(d) rests on `13.2.1` being asserted at every admissible
   pair, including `τ = θ(4 + 1/k)` for large `k`. That is how round 3 wrote the quantifier and how
   `13.2.4`(g) proves it below the budget, so it is not gratuitous — but it is the hinge, and a reviewer who
   wanted `τ` bounded away from `4θ` would remove `13.2.6`(3) and leave only `13.2.6`(1)–(2). I did not find
   a reason inside the record to prefer a fixed slack, and I flag the choice rather than assume it.
3. **The endpoint `τ = 4.8188…` exactly.** §7.1 says protection there "is not available"; whether it is
   *refutable* needs a diagonal in Inselmann's `ε` together with his envelope's own per-block bound
   (`v3r3-inselmann-horizon-findings.md` §2.4: `m_i ≤ 2εL + 1` inside the range) to move Cor. 1.4's `T_1`-time
   statement onto a door. I believe it goes through and I did not write it out; nothing on the page needs it,
   and §7.1 is drafted so that it does not depend on it. Round 3 parked the same endpoint (its §12 item 2).
4. **`13.2.6`(3) is untested.** The calibration campaign measures frequencies; the prefix statement is a
   statement about `S_{n*−1}/T_N` at `τ` near `4θ`, which no run reports. The flagship's `4.0017` exponent
   per block at `τ ≈ 2.29` is the closest thing and is a full-horizon pooled mean, not a prefix quenched one.
   Measuring the distribution across orbits of `S_{n*−1}/T_N` at two or three `τ/θ` ratios would be one run
   and would test exactly the clause the correction now leans on. Not done here; it is an
   `experiments/` item, and it is adjacent to round 3's own open question 5 (the untested quenched form).
5. **Whether any other page reads the conversion.** I swept `aeh.md`, the paper, `publication.md`,
   `index.md`, `open-problems.md`, `stage1.md`, `itinerary.md`, `reverse.md`, `stage4.md`, `bridge.md`,
   `README.md` for `E[m+r]`/`E_B[m+r]`, "within budget", `4.8188` and `1/β`, and the sites in §1 and §9 are
   all of them. I did not sweep `archive/`, `experiments/` docstrings, or `sources/`.
6. **`13.2.6`(3)'s altitude step.** I state the per-block descent `−β` with the rider that the
   `log₂((3y+1)/2) − log₂(3y/2)` error is `O(1/y)` per step and summable inside the budget by the altitude
   bound. That is correct but I did not write the summation out; if the author wants the drift consequence
   stated without a rider, the clean form is the exponent statement (`Σ(m+s)/T_N → 4`, `Σm/T_N → 2`) with the
   altitude reading left as a remark.
7. **The reviewer's "particularly at reduced-block exits".** I read this as pointing at the gap between
   Inselmann's `T_1`-iterates and the record's doors. For the *positive* direction the gap is closed —
   `13.6.3`(i)(a) plus `v3r3-inselmann-horizon-findings.md` §2.7 rider 3: the doors are genuine Syracuse
   iterates. For the *negative* direction (refuting protection above the ceiling) it is open, and it is one
   of the reasons §7.1 declines to claim the refutation. If the reviewer meant something else by the phrase,
   I did not identify it.

---

## 11. Verification record — every number and quotation read or computed, not recalled

| Item | Source |
|---|---|
| `aeh.md` L83, L84, L86, L88–91, L67, L69, L95–104, L108, L110, L116, L118 quoted verbatim | `aeh.md` at `fa9edf5`, read in full |
| `paper` L246, L248–290, L292–329, L331–360, L362–387, L389–419, L433–439, L447 | `paper/collatz-reduced-v3.tex`, read L1–40 and L230–479 |
| `publication.md` L29, L41, L44 | `publication.md`, read in full |
| Round 3's §7 ("with the division named as AEH's own content"), §6.1 table, §11 ("that is why the design puts the conversion inside the hypothesis rather than trying to prove it"), §12 items 1–3 | `briefs/v3r3-cut-weighting-findings.md` L344–530, L720–844 |
| Inselmann Thm 1.1, 1.3, Cor. 1.4, Thm 1.6, 1.9, 1.10, Thm 3.8 eq. (3.20), Prop. 2.4, and the "read cover to cover through §3: no pattern of length ≥ 2 is counted" finding | `briefs/v3r3-inselmann-horizon-findings.md` §1.1–1.8, §2.1–2.7, §3 |
| "the letter statistic needed … is unconditionally available precisely on the range `θ < 1/4`, and precisely nowhere else" | same, §2.5 |
| `m_i ≤ 2εL + 1` inside the envelope; the doors are Syracuse iterates | same, §2.4, §2.7 rider 3 |
| What `13.2.4` proves; `I(1/4) = 0` and the Chernoff tilt `e^λ = 2(1−2θ)`; TV transfers every event of the joint law | `briefs/v3r3-basecase-density-findings.md` §3.5, §4, §9 items 3–4 |
| `log₂3 = 1.584962500721156`; `β = 0.8300749985576878`; `1/β = 1.204710419826604`; `(1 − log₂√3)^{-1} = 4/β = 4.818841679306416`; `4.8188…/4 = 1.204710419826604` | computed this session, double precision |
| `I(θ) = log 2 − H(2θ)` = `0.020135513…` at `θ = 0.20`, `0.000800213…` at `θ = 0.24`, `0` at `θ = 1/4` — matching `aeh.md` L65's printed `0.0201`, `0.00080`, `0` | computed this session |
| `I(θ,τ) = τ(log 2 − H(2θ/τ))` reduces to `I(θ)` at `τ = 1` at three `θ`, to 6 decimals; positive iff `τ > 4θ`; sample values `0.005567` at `(0.20, 0.9)`, `0.000455` at `(0.24, 0.99)`, `0.000062` at `(0.20, 0.81)` | computed this session |
| `P_B(S_n ≥ J) = P(Bin(J−1, 1/2) < 2n)` exact in rational arithmetic at `(n,J) = (2,5), (3,7), (2,9), (3,14), (4,20), (5,25)` — all equal, confirming `13.2.4`(b) and that `S_n` (sum of `2n` geometrics) is the sharp index in (a) | computed this session |
| The counterexample: cemetery fraction, prefix mean, full mean at `T = 100…6400`, `c = 3`, at four `τ/θ`; the clean control; the spread-excess control rejecting the budget clause at `1 − (τ/θ)/5` | simulated this session, seeds 40401/40402 |
| `13.2.6` and `13.3.4` free as anchors; `13.2.4` has items (a)–(f) only | grepped across `*.md`, `paper/*.tex` |
| Downstream citers of `13.2.4`/`13.2.4.1`: `index.md` L46, `open-problems.md` L86, `stage1.md` L579 and L620 | grepped |
| Paper macros in scope for the drop-ins (`\LL`, `\w`, `\wnext`, `\dnext`, `\Z`, `\vt`, `\vth`) and labels (`hyp:aeh`, `prop:budget`, `thm:onestep`, `lem:absorption`) | `paper/collatz-reduced-v3.tex` L17–23, L38–246 |
| Flagship run numbers (`τ ≈ 2.29`, `160` exponent against `70` bits, `4.0017` per block, `22` of `30` blocks past the budget) | `aeh.md` L67 |
