# Findings: the round-4 fix pass — the sweep found a fourth site, and (g)'s offset clause is repaired

**Branch.** `v3r4-review-round4`. Base `3c30b61`; three commits added, in the ordered sequence the
brief asked for:

| commit | contents |
|---|---|
| `5e57468` | record: `aeh.md`, `publication.md`, `open-problems.md`, `experiments/aeh_budget_clause.py` |
| `a1f2ac3` | paper: the four claim sites, D6, D7, rebuilt PDF |
| `3882f0e` | Appendix A pin `e634513` → `a1f2ac3`, rebuilt PDF |

No push, no merge, no rebase, no branch switch, no worktree. Every file written with the Write/Edit
tools; no PowerShell redirection touched a tracked file.

---

## 1. The sweep — every instance of the retracted claim, and how each was resolved

The claim being hunted: *that AEH supplies the mean exponent, that it converts a step horizon into
blocks per bit, that the block-unit endpoint is a consequence of or part of the hypothesis, or that
zero cemetery mass gives the budget.*

**Method.** Not a site list. I read `paper/collatz-reduced-v3.tex` end to end and then ran a keyword
sweep over the whole file for every noun the claim can wear — `consequence of`, `part of what`,
`asserts`, `blocks per bit`, `block units`, `block time`, `mean exponent`, `exponent per block`,
`steps per block`, `divides by`, `divisor`, `converted`, `conversion`, `same unit`, `underwrite`,
`cemetery`, `no mass`, `beta`, `4.8188`, `1.2047`, `budget` — and adjudicated every hit. The same
sweep was run over every tracked wiki page (`aeh.md`, `index.md`, `README.md`, `TOUR.md`,
`HANDOFF.md`, `bridge.md`, `stage1.md`–`stage4.md`, `cycles.md`, `itinerary.md`, `open-problems.md`,
`publication.md`, `spine.md`, `program.md`, `reverse.md`, `anchors.md`, `ladder.md`).

**Four instances in the paper. Three were the ones named; the fourth was named by nobody.**

### 1a — tex L59, *Related work and provenance*, PDF page 4 (D1a)

> "…their reading in the reduced blocks of Section 5 is not free: it divides by a mean number of
> steps per block **that is itself part of what Hypothesis 5.1 asserts**."

**Resolved** → "…it divides by a mean number of steps per block **which is a theorem of the cylinder
count inside the digit budget and, past it, neither a theorem nor a consequence of
Hypothesis~\ref{hyp:aeh}**." The following sentence ("What Hypothesis 5.1 asserts is not descent but
the letter statistics themselves") is unchanged and now follows correctly.

### 1b — tex L42, *Version note*, PDF page 2 (D1b)

> "…**their reading in reduced blocks being a consequence of Hypothesis 5.1 rather than an input to
> it**."

**Resolved** → "…their reading in reduced blocks being **available from the cylinder count inside the
digit budget and from nothing in this paper past it**." The anti-circularity function of the clause
survives: something unavailable is even less an input than a consequence would be.

### 1c — tex L432–433, §5 Inselmann paragraph, PDF page 15 (D1c)

> "…**it is therefore a consequence of Hypothesis 5.1 and not available to underwrite it**."

**Resolved** → "…it is therefore **not available to underwrite the hypothesis: inside the digit
budget it is a theorem of the cylinder count (`aeh.md` Lemma 13.2.4(g)), and past it neither a
theorem nor a consequence of the hypothesis (`aeh.md` §13.2.3)**."

### 1d — tex L379–381, §5, PDF page 14 — **FOUND BY THIS PASS; named by neither the external reviewer, the design wave, the apply wave, nor the verify wave**

> "That conversion is available here precisely because the word is exactly `B` here. **A descent from
> `N` to `O(1)` takes `1/β = 1.2047…` blocks per bit, equivalently `4.8188…` units of exponent per
> bit, some `4.8` times as far.**"

This is the retracted claim in its flattest form. The preceding sentence has just restricted the
conversion's availability to *here* — inside the budget, where the word is exactly `B` — and the next
sentence then asserts the block-unit endpoint of a *full descent*, at `τ = 4.8188`, as a plain fact,
with "equivalently" doing the conversion. Sixteen lines later, L397–400 says the endpoints "read as
`1/4` and `1/β` blocks per bit **only after** dividing by the mean exponent per block, which is a
theorem where the cylinder count runs and, past it, is neither a theorem nor a consequence of
Hypothesis 5.1". The two sentences are on the same printed page and contradict each other.

**Resolved** → "A descent from `N` to `O(1)` takes `4.8188…` units of exponent per bit, some `4.8`
times as far — **which is `1/β = 1.2047…` blocks per bit once one divides by that same mean**."
This is exactly the shape `aeh.md` L67 uses ("which is `1/β = 1.2047…` blocks per bit once one
divides by `E[m + r] = 4`"): the conversion is named as an operation, and its status is settled
eighteen lines later at L397–400 rather than presupposed here. The exponent figure `4.8188`, which is
Inselmann's theorem in the unit it is proved in, is what now carries the sentence.

### 1e — `aeh.md` `13.3.2` (D2) — the surviving instance in the record

> "…but the endpoint `1/β` in block units **is this page's own hypothesis, not his theorem**."

**Resolved** → "…but the endpoint `1/β` in block units is **neither his theorem nor a consequence of
this page's hypothesis: inside the digit budget it is `13.2.4`(g), and past it nothing on this page
supplies it (`13.2.3`)**." The attribution function — refusing the endpoint to Inselmann — is kept.
**Nothing else in `13.3.2` was touched**; the word-diff of that paragraph is exactly this one clause,
and the deferred §7.9 rescoping of its *first reason* is untouched.

### Adjudicated and left standing (not instances)

| site | why it is not the claim |
|---|---|
| tex L42 "Section 5 states no descent or contraction consequence of Hypothesis 5.1" | a negative; correct. |
| tex L456 "a consequence of Hypothesis 5.1 rather than the per-start statement itself" | about the calibration's *pooled* runs measuring the across-orbit average of per-start frequencies, which genuinely is a consequence of the hypothesis. Correct. |
| tex L322–325 "…which is what `π_{k,D}`'s giving `†` no mass **requires**" | consistency stated as a *necessary* condition on the target law, the direction `aeh.md` `13.2.3` states. It does not say zero cemetery mass *gives* the budget; the following sentences say the opposite explicitly. |
| tex L336–341 "…with the divisor in either block reading the mean of the target law: a theorem about orbits below the budget, and not a consequence of the hypothesis above it" | this round's own corrected sentence. |
| tex L374–378 "…it reads as `1/4` blocks per bit only through the mean exponent per block … That conversion is available here precisely because the word is exactly `B` here" | in-budget, correct, and it is the sentence 1d was contradicting. |
| tex L425–429 "…`4.8188…` times the classical range …, the two measured in the same units", backed by Thm 1.6 | the `T`-time ↔ Syracuse-time change is the one Inselmann *proves* (Thm 1.6 through his Thm 3.8 eq. (3.20)); the next sentence says so. Only the further Syracuse → block change is unsupported, and that is 1c. |
| `aeh.md` L67, L84, L86–94, `13.2.4`(g) closing line | all this round's corrected text; re-read against the repair, all consistent. |
| `publication.md` L29 | already fully corrected in an earlier round; states the endpoint identification `1/β` is *not* unconditional. |
| `index.md` L26/L46, `README.md` L40, `stage1.md` L579/L620, `TOUR.md`, `bridge.md`, `HANDOFF.md`, `itinerary.md` L73 | all cite the *in-budget* conclusion, which `13.2.4`(g) strengthens rather than moves. No mismatch. |

**No fifth instance found**, in the paper or in any tracked wiki page.

---

## 2. Disposition of D2–D10

| # | disposition |
|---|---|
| **D1** | four sites, §1 above. Fixed. |
| **D2** | fixed, §1e. Subtractive; needs nothing deferred; `13.3.2` otherwise byte-identical. |
| **D3** | fixed, §3 below. The repair closes. `13.2.4.1` needed no edit — see §3.4. |
| **D4** | closed: fresh script `experiments/aeh_budget_clause.py`, and `13.2.4`'s Verified line rewritten as **one current line** covering (a)–(e) and (g), per `AGENTS.md`. §4 below. |
| **D5** | fixed. "positive precisely for `τ > 4θ`" → "positive on that range … `I(θ, τ)` is the tail term's rate precisely on `4θ < τ` and nowhere else: below `4θ` the tail term does not vanish at all, while the expression itself is positive on both sides of the threshold and is undefined at `τ ≤ 2θ`." Both of verify's objections are named, and the undefined region is named too. |
| **D6** | fixed **in the paper only**, as briefed. tex L328–329 → "(`aeh.md` Lemma 13.2.4(g), whose two error terms are, **on that range**, precisely the two clauses of admissibility)". `aeh.md`'s (g) self-corrects in its next clause and was left. |
| **D7** | fixed, and the theorem number **was** unambiguous in `briefs/v3r3-inselmann-horizon-findings.md`, so no restatement was needed. See §5. |
| **D8** | fixed. `publication.md` L41 → "their reading as `1/β` blocks per bit is **not available at all past the digit budget**". |
| **D9** | fixed. `aeh.md` L8 (*Current state*) → "…and the hypothesis is exactly what lies past that digit budget, **where what it supplies is frequencies and not the exponent mean (`13.2.3`)**." Purely subtractive; claims nothing deferred. |
| **D10** | fixed, lightly. `open-problems.md` `11.11`'s opening now points instead of restating: "aeh.md `13.2.3` records what the hypothesis says about its own exponent budget, and `13.2.4`(g) what the cylinder count proves inside it; neither is restated here. On the reading those two fix, the Cesàro statement `T_N^(−1)Σ(m_n + r_n) → 4` is a theorem inside the digit budget and does not follow past it." The Cesàro statement is kept because both open questions are about it. The two questions themselves are untouched. |

Front-matter `updated:` bumped to `2026-08-03` on the three edited pages, per `AGENTS.md`'s
status-change workflow. No `status:` field changed; no anchor renumbered; no numbered theorem's claim
strengthened, weakened or renumbered; no change log, dated journal or "was X, now Y" prose added to
any tracked page.

---

## 3. D3 — the offset clause, with the reasoning

### 3.1 What was wrong

Printed in (g)'s first bullet:

> (The budget clause counts `Σ(m_i + s_i)` and (a)–(b) count `Σ(m_i + r_i)`; by `13.2.3` the two
> differ by `s_n − s_0`, and `max_(n ≤ T_N) s_n ≤ 2 log₂ T_N` off a `B`-event of mass `≤ 2/T_N`,
> which the same bound transfers and **which `δ_N` absorbs**.)

Two separate faults, and verify named the first:

1. `2/T_N = Θ(1/log N)` and `δ_N(τ) = e^(−Θ(b))`, so `δ_N` cannot absorb it. As printed, (g) gave
   "the budget does not bind" only off a set of density `O(1/log N)`.
2. **The `max` is bounding the wrong sign.** With `S^bud_n = S^let_n + s_0 − s_n`, the term `−s_n` is
   *favourable*: a large late letter makes the budget count smaller, not larger. Only the near end
   matters, and only through one index.

### 3.2 The one index

`S^bud_n = Σ_(i<n)(m_i + s_i)` is nondecreasing in `n` (every summand is `≥ 2`), so
`max_(n ≤ T_N) S^bud_n = S^bud_(T_N)` and the whole horizon is controlled by the single event
`{S^bud_(T_N) ≥ Λ_N}`. Verified on real orbits: `0` monotonicity failures across all six measured
cells.

### 3.3 The bound, made convention-proof

I did not take the offset's *exact* form on trust, because the record carries three different letter
indexings and they give three different offsets. I settled it computationally
(`experiments/aeh_budget_clause.py`, and a probe in the scratchpad), on real orbits, `300` starts at
`b = 300`, `n = 40`:

* `stratum(G^i(x)) = (m_i, s_i)` exactly — `0` failures. So the door letter of `x` pairs a block's own
  `m` with that block's own `s`.
* **Reading A**, letter `i = stratum(G^i x)`: `S^let_n = S^bud_n` **exactly**, offset `0`.
* **Reading B**, `13.2.1`/`13.2.4` as printed (`ℓ_n = (m_(+,n), s_(n+1)) = stratum(x_exit(n))`):
  `S^bud_n − S^let_n = (m_0 + s_0) − (m_n + s_n)` — "one letter at each end", which is what `13.2.3`'s
  own first phrase says. This equals `s_0 − s_n` only when `m_0 = m_n`, which happened on `87` of
  `300` starts.
* **Reading C**, letter `i = (m_i, s_(i+1))`: `S^bud_n − S^let_n = s_0 − s_n` exactly — the identity
  `13.2.3` prints — but this pairing mixes two strata and is not a door letter.

Rather than adjudicate the record's index convention (not on this pass's list, and `13.2.3` is not
either), I wrote the repair so that it is **true under all three readings**: the budget count exceeds
the letter count by at most `m_0 + s_0`, the total exponent of the start's own block. Under A the
excess is `0 ≤ m_0 + s_0`; under B it is `≤ m_0 + s_0`; under C it is `s_0 ≤ m_0 + s_0`. Checked
directly at **every** index `n ≤ T_N`, under readings A and B, across all six cells: `0` failures.

### 3.4 The repair as it now reads, and why it closes

> `Σ_(i<n)(m_i + s_i)` is nondecreasing in `n`, so only `n = T_N` is at stake, and there the budget
> count exceeds the letter count by at most the total exponent `m_0 + s_0` of the start's own block.
> Fix `ρ ∈ (0, 1)` with `(1 − ρ)τ > 4θ`, which `τ > 4θ` permits; then
> `{Σ_(i<T_N)(m_i + s_i) ≥ Λ_N}` is contained in `{S_(T_N) ≥ (1 − ρ)Λ_N} ∪ {m_0 + s_0 > ρΛ_N}`, of
> mass at most `2δ_N((1 − ρ)τ) + δ_N(τ) + ρΛ_N·2^(1 − ρΛ_N)` — the first by (a)–(b) at budget rate
> `(1 − ρ)τ`, which is again in `(4θ, 1)`; the other two by transferring the one-letter law
> `P_B(m + r ≥ t) = t·2^(1−t)` through (a) at `n = 1`. Every term is `e^(−Θ(b))`.

Reasoning, step by step:

* **The inclusion.** If `S^bud_(T_N) ≥ Λ_N` and `S^let_(T_N) < (1−ρ)Λ_N`, then
  `m_0 + s_0 ≥ S^bud_(T_N) − S^let_(T_N) > ρΛ_N`. So the event is covered by the two named.
* **First term.** `(1−ρ)τ < τ < 1` and `(1−ρ)τ > 4θ` by the choice of `ρ`, which is possible exactly
  because `τ > 4θ` — so (b)'s standing hypothesis `0 < η < 1 − 4θ` holds at `η = 1 − (1−ρ)τ`, and the
  total-variation transfer of (a) gives `≤ 2δ_N((1−ρ)τ)`, at rate `I(θ, (1−ρ)τ) > 0`.
* **Second and third.** `m_0 + s_0` is one letter's total exponent. Under `B` its law is exactly
  `P_B(m + r ≥ t) = t·2^(1−t)` (independently derived and confirmed exact in rational arithmetic at
  every `t ≤ 14`). (a) at `n = 1` and `J = Λ_N` transfers it at a total-variation cost `≤ δ_N(τ)`,
  since `S_n` is nondecreasing in `n`.
* **The rate.** Every term is exponentially small in `b`, so the exceptional density is `e^(−Θ(b))`,
  which is all (g) and `13.2.4.1` claim. The composite rate is smaller than `I(θ, τ)` — it is a
  minimum over `I(θ, (1−ρ)τ)` and `ρτ log 2`, and `ρ` trades them off — so I did **not** print a rate
  for it; `δ_N(τ)`'s own rate `I(θ, τ)` is stated where it belongs, on the tail term.

**Does it close? Yes.** No step needs anything deferred, no step needs the `13.3.2` rescoping, and
the conclusion is exactly the printed one. The one honest cost is the unnamed composite rate.

**Corollary `13.2.4.1` was not edited, and that is the correct disposition.** Its
"by `13.2.4`(g) the budget binds on a set of density `e^(−Θ(b))`" was unjustified *because* (g) was
broken; with (g) repaired it is exactly what (g) now delivers, word for word. Editing it would have
been a change with nothing behind it. I re-read the whole corollary against the repaired (g): the
quantification over admissible `τ < 1`, the identification of the tallied word with (d)'s and the
tallied window blocks with (e)'s, and the closing "both hold unconditionally in that range" all read
correctly.

---

## 4. The verification script and its numbers

`experiments/aeh_budget_clause.py`, header naming `aeh.md` `13.2.4`(g) and Corollary `13.2.4.1`.
**Fresh code**: it imports nothing from any other file in `experiments/` — the block decomposition,
the door letters, the exact tail law, the rate and `δ_N` are all built in it from the record's own
definitions. **I did not quote a single number from the verify findings**; every figure below is from
this implementation. Seeds `88001`–`88006`, `88011`–`88013`, `88021`, and `70701` for the scratchpad
index probe.

### 4.1 The exact tail identity, at ten new `(n, J)`

`P_B(S_n ≥ J)` by exact rational forward convolution of `2n` geometric(1/2) laws — the routine keeps
only masses at `k ≤ J−1` and returns `1 −` their sum, so nothing is lost at the truncation edge, and
**no binomial coefficient appears on that side of the comparison** — against
`P(Bin(J−1,1/2) < 2n)` computed with `math.comb` in exact rationals. Pairs chosen to overlap neither
the page's five nor the verify pass's ten:

```
(1,4)  1/2                  (2,7)  21/32              (3,10) 191/256
(4,9)  255/256              (5,20) 1/2                (6,13) 4095/4096
(7,30) 23859587/67108864    (9,25) 16587165/16777216
(11,45) 1936010885087/4398046511104                   (12,28) 16776803/16777216
```

**All ten equal, exactly. 0 mismatches.**

### 4.2 The rate

`I(θ,1) = I(θ) = log 2 − H(2θ)` to **exact double-precision equality** (`|diff| = 0.00e+00`) at
`θ = 0.05, 0.10, 0.15, 0.18, 0.20, 0.22, 0.24, 0.245, 0.2499`. The page's printed values reproduce:
`I(0.20) = 0.020135513551`, `I(0.24) = 0.000800213470`, `I(0.25) = 0.000000000000`.

Measured decay `−ln P(Bin(⌈τb⌉−1,1/2) < 2⌈θb⌉)/b`, log-sum-exp on exact log-binomials:

| `(θ,τ)` | `I(θ,τ)` | b=500 | b=2,000 | b=8,000 | b=32,000 | b=128,000 |
|---|---|---|---|---|---|---|
| (0.20, 0.95) | 0.01189181 | 0.01637050 | 0.01333219 | 0.01233667 | 0.01202456 | 0.01193040 |
| (0.22, 0.99) | 0.00612375 | 0.01003233 | 0.00740418 | 0.00652706 | 0.00624600 | 0.00615971 |
| (0.20, 0.85) | 0.00147144 | 0.00437260 | 0.00243853 | 0.00178876 | 0.00157154 | 0.00150182 |
| (0.24, 0.98) | 0.00020410 | 0.00224430 | 0.00084895 | 0.00041775 | 0.00027502 | 0.00022687 |

Monotone convergence to `I(θ,τ)` from above in every row.

**Negative control on the rate (D5's substance).** At `τ < 4θ` the tail term does not vanish:

| `(θ,τ)` | `4θ` | b=500 | b=2,000 | b=8,000 | b=32,000 |
|---|---|---|---|---|---|
| (0.20, 0.60) | 0.80 | 0.9999999974 | 1.0000000000 | 1.0000000000 | 1.0000000000 |
| (0.24, 0.85) | 0.96 | 0.9962554540 | 0.9999999547 | 1.0000000000 | 1.0000000000 |
| (0.15, 0.45) | 0.60 | 0.9999997882 | 1.0000000000 | 1.0000000000 | 1.0000000000 |

### 4.3 Real odd starts: the budget clause and the exponent mean

Uniform odd starts in `[2^b, 2^(b+1))`, big-integer block decomposition.

| `b` | `θ` | `τ` | `T_N` | `Λ_N` | budget binds | exponent mean (s.d.) | printed bound `2δ_N(τ)` |
|---|---|---|---|---|---|---|---|
| 400 | 0.20 | 0.90 | 80 | 360 | 8 / 1,000 | 3.99506 (0.21860) | 3.462e−02 |
| 800 | 0.20 | 0.90 | 160 | 720 | 2 / 1,000 | 3.99864 (0.16032) | 2.824e−03 |
| 1,600 | 0.20 | 0.90 | 320 | 1,440 | 0 / 200 | 3.99616 (0.11560) | 2.422e−05 |
| 3,200 | 0.20 | 0.90 | 640 | 2,880 | 0 / 80 | 4.01311 (0.07205) | 2.374e−09 |
| 1,600 | 0.10 | 0.55 | 160 | 881 | 0 / 200 | 4.01197 (0.15595) | 2.946e−16 |
| 1,600 | 0.22 | 0.95 | 352 | 1,520 | 0 / 200 | 4.00521 (0.11580) | 4.042e−03 |

**The printed bound is respected in every row**, and the per-start spread of the exponent mean falls
`0.219 → 0.160 → 0.116 → 0.072` as `b` quadruples along the first four rows, which is the
`T_N^(−1/2)` the Chernoff clause predicts.

**Negative control at `τ < 4θ`**, where (g) predicts the budget must bind:

| `b` | `θ` | `τ` | `4θ` | budget binds |
|---|---|---|---|---|
| 1,600 | 0.24 | 0.90 | 0.96 | 99 / 100 |
| 1,600 | 0.20 | 0.70 | 0.80 | 100 / 100 |
| 800 | 0.25 | 0.95 | 1.00 | 88 / 100 |

### 4.4 The offset clause's own ingredients

* **The clock identity of `13.2.3`**, `x_exit(n−1) = T_1^(S_n)(x)`, run literally — `S^bud_n` steps of
  the one-division map from `x` — at every cell: **0 failures**.
* **Monotonicity** of `Σ_(i<n)(m_i + s_i)`: **0 failures**.
* **The excess over the letter count `≤ m_0 + s_0`** at every index `n ≤ T_N`, under **both** letter
  readings, across all six cells: **0 failures**.
* **`P_B(m + r ≥ t) = t·2^(1−t)`** by exact rational convolution of two geometric(1/2), at every
  `t ≤ 14`: **0 mismatches** (`1, 3/4, 1/2, 5/16, 3/16, 7/64, 1/16, 9/256, 5/256, 11/1024, 3/512,
  13/4096, 7/4096`).
* **The measured law of `m_0 + s_0`** on `3,000` uniform odd starts at `b = 1600`: tail
  `1.00000, 0.73133, 0.49267, 0.31433, 0.18767` at `t = 2…6` against `1, 0.75, 0.5, 0.3125, 0.1875`,
  and `0.06333 / 0.02167 / 0.00567` at `t = 8, 10, 12` against `0.0625 / 0.01953 / 0.00586`; mean
  `3.98467` against `E_B[m + r] = 4`, maximum `16`.
* **The composite bound** of the repaired clause, at the midpoint choice
  `ρ = (1 − 4θ/τ)/2`, holds with room in every cell (`0.008` observed against `2.9e−01` at `b = 400`;
  `0.000` against `1.3e−05` at `(1600, 0.10, 0.55)`).

### 4.5 The Verified line

`13.2.4`'s Verified line was **rewritten, not appended to**: it is one current line naming
`experiments/aeh_basecase.py` (2026-08-02) **and** `experiments/aeh_budget_clause.py` (2026-08-03),
with the freshness clause extended ("neither imports anything from the other, nor from
`aeh_calibration.py`, `aeh_symbolic.py` or `itinerary_coding.py`"), the (a)–(e) record unchanged, and
a new `For (g):` clause carrying §4.1–§4.4 with its seeds. That closes D4.

---

## 5. D7 — the Inselmann citation

`briefs/v3r3-inselmann-horizon-findings.md` quotes the source verbatim and is **unambiguous**, so no
restatement was needed:

* **Thm 1.1** (§1.2 of that file, p. 2 of the source): `(√3/2)^k m^{1−ε} ≤ T^k(m) ≤ (√3/2)^k m^{1+ε}`
  for all `0 ≤ k ≤ log₂ m/(1 − log₂√3)`, natural density 1. "`k` counts **`T`-steps** (the
  one-division map)."
* **Thm 1.10** (§1.5, p. 5): the same envelope with `Syr^k` and `k` counting **Syracuse steps**, out
  to `(log₂(4/3))^{-1} log₂ m`.

The paper's `τ` is a *division* count, i.e. `T_1`-time, and the clause says "the same unit, nothing
converted". The theorem stated in that unit is **Thm 1.1**, whose lower side gives exactly what
protection needs: at `k = τ log₂ N`, `log₂ T^k ≥ (1 − ε − τ(1 − log₂√3)) log₂ N`, which exceeds
`log X_N = o(log N)` for every `τ < 4.8188…`.

**Fixed** → `\cite[Thm.~1.1]{inselmann}`, with "whose two-sided envelope is stated for the
one-division map" added so the reader can see why the unit matches. I did **not** cite
"Thms. 1.1 and 1.10" as verify proposed: attaching "nothing converted" to a pair one of which is
stated in the converted unit is the exact genre of slip this round exists to remove. The paper's other
Inselmann citations were re-read and are each correct in their own unit — Thm 1.10 at L422 for the
Syracuse envelope, Thm 1.6 at L429 for the parity first moment, Cor. 1.4 at L422 for descent — and the
record (`aeh.md` L82, "Thm `1.1`/`1.10`") is a superset of the paper's citation, so no cross-page
mismatch is introduced.

---

## 6. Build

Clean rebuild in `paper/`, `.aux`/`.log`/`.out` deleted first, three
`pdflatex -halt-on-error -interaction=nonstopmode` passes, twice — once after the content commit and
once after the pin commit. Identical both times:

| | |
|---|---|
| passes | 3, all exit code `0` |
| pages | **17** |
| overfull boxes | **0** |
| underfull boxes | **1** — `\hbox (badness 1067)` at L489–490, the `lagarias` bibitem inside `\thebibliography`. Pre-existing; verify independently confirmed the identical badness at `fa9edf5`. |
| unresolved references | **none**; the log contains no `LaTeX Warning` line of any kind, no undefined reference or citation, no rerun request |
| PDF | 434,611 bytes after the content commit, 434,144 after the pin commit; the pin string is the only difference between the two builds |

**Confirmed from the built PDF's text**, not from the source. `pdftotext -layout` on the committed
artifact:

* **Absent**: `part of what Hypothesis`; `being a consequence of Hypothesis 5.1 rather than an input`;
  `it is therefore a consequence of Hypothesis`; `takes 1/β`; `this page's own hypothesis`;
  `Thm. 1.10] — the same unit`.
* **Present**: all four replacements, plus the pin string `commit a1f2ac3`.
* **Every** occurrence of `consequence of Hypothesis` in the artifact was enumerated — there are four,
  and all four are correct statements (the two negatives at pp. 2 and 4, the corrected endpoint
  sentence at p. 14, and the calibration's pooled-runs sentence at p. 17).
* **Every** occurrence of `blocks per bit` was enumerated — there are three, and all three name the
  divisor rather than presupposing it.

---

## 7. The pin

`e634513` → **`a1f2ac3`**, the paper commit, whose parent `5e57468` carries the record half. Moved in
its own commit `3882f0e`, which touches only the pin string and the rebuilt PDF.

**Verified positively at `a1f2ac3`**, by extracting every `\texttt{}` citation from the `.tex` and
resolving each against `git show a1f2ac3:<path>` — never against the working tree.

* **All ten named files present**: `aeh.md`, `cycles.md`, `itinerary.md`, `stage3.md`, and
  `experiments/{period1,period2,period3}_cycles.py`, `one_step_propagation.py`, `anchor_increment.py`,
  `absorption_law.py`.
* **Every named anchor resolves**: `aeh.md` §13.1, §13.2.3, Lemma 13.2.4 with item (g), Corollary
  13.2.4.1, Proposition 13.2.5, §13.3.2, §13.4, §13.5, Lemma 13.6.3 with items (iii) and (v), Theorem
  13.6.4, Proposition 13.6.5; `itinerary.md` §14.15.1.5; `stage3.md` §11.8.6.3.
* **`cycles.md`: all eight sections**, checked by heading text as well as by number — §§12.2.3,
  **12.5.2**, **12.5.3**, 12.6.1, **12.6.2**, **12.7.4**, **12.7.5**, 12.8.6. The five in bold are the
  ones the apply wave's check did not enumerate; verify caught the omission, and this check does not
  repeat it.

**Verified negatively at `a1f2ac3`**: the sentences this round removed are gone — `this page's own
hypothesis`, `positive precisely for τ > 4θ`, `which δ_N absorbs` — and `13.2.6`, the deferred
proposition, appears nowhere, so no pointer dangles. **And positively on this round's own additions**:
`13.3.2`'s restated clause, `P_B(m + r ≥ t) = t·2^(1−t)`, `the total exponent m_0 + s_0 of the start's
own block`, `aeh_budget_clause.py` in the Verified line, `13.2.4`(g)'s corrected rate clause,
`publication.md`'s D8 clause and `open-problems.md`'s pointer form are all present at the pin.

The two historical pins in the published version-note text — `72ec88e` and `9d9d1ec`, both pointing at
`cycles.md` §12.8.6 — are untouched, correctly: they record what a published version said.

---

## 8. Found and not fixed — reported, per the brief

1. **`13.2.3`'s printed offset identity does not match the page's own letter indexing.** `13.2.3` says
   the budget count and the letter count "differ by one letter at each end, since `r_i = s_(i+1)`" and
   then "The gap is exactly `s_n − s_0`". Those two phrases describe different quantities, and under
   the indexing `13.2.1` and `13.2.4` actually define — `ℓ_n = (m_(+,n), s_(n+1)) = stratum(x_exit(n))`
   — the gap is `(m_0 + s_0) − (m_n + s_n)`, not `s_n − s_0`. Measured: the two agree on `87` of `300`
   starts, exactly the ones with `m_0 = m_n`. `s_n − s_0` is right only under a third pairing,
   letter `i = (m_i, s_(i+1))`, which mixes two strata and is not a door letter. **Not fixed** —
   `13.2.3` is on no list, and the repair to (g) was deliberately written to be true under every one
   of the three readings, so it does not inherit the ambiguity. Worth a round of its own: the fix is
   one clause in `13.2.3`, but it should be made by someone free to settle the page's index
   convention, and `13.6.3`(i)(a)'s "fixed one-index offset" clause should be read with it.
2. **`13.2.4`'s own definition of `ℓ_n` is off by one against (a)'s proof.** `13.2.4` sets
   `y_(−1) = x`, `y_n = G^(n+1)(x)`, `ℓ_n = stratum(y_n)` — so `ℓ_0` is the first letter of `G(x)`,
   while (a)'s proof invokes `14.15.1.5` on "the followers of a word `W`", which is the letter word of
   `x` itself, starting at `stratum(x) = ℓ_(−1)`. Harmless to every conclusion — one letter's shift
   costs `O(1/T_N)` in every frequency and nothing in the `e^(−Θ(b))` bounds — but it is the source of
   item 1. **Not fixed**, same reason.
3. **`13.2.3` still carries the `max_(n ≤ T_N) s_n ≤ 2 log₂ T_N` bound off a set of `B`-mass
   `≤ 2/T_N`.** In `13.2.3` this supports a different and correct claim — that the gap is
   `O(log log N)` *in size* against a budget of `Θ(log N)` — and not the claim `δ_N` absorbs it, which
   is what (g) wrongly said and no longer says. Left as correct in its own context, and flagged here
   only because a reader arriving from (g) may expect the two passages to match.
4. **`briefs/v3r3-inselmann-horizon-findings.md` says the block-ending pattern is `11`;
   `aeh.md` `13.3.2` and `publication.md` L29 say `10`.** `10` is right — a block ends at a Syracuse
   step whose exponent is `≥ 2`, i.e. an odd step followed by an even one — so the record's live pages
   are correct and the round-3 brief carries the superseded letter. Briefs are records, not claim
   surfaces, so nothing needs doing; noted so a later round reading that brief does not reintroduce
   `11`.
5. **`c(ε)` in (g)'s second bullet is still not made explicit**, and the composite rate of the
   repaired offset clause is not printed either. Both are positive and neither is needed for any
   stated conclusion. Recorded, not fixed.
6. **Not pruned**, per the brief; **the deferred prefix result is claimed nowhere**, and `13.2.6`
   appears in no tracked page. Re-checked at the pin.
7. **`archive/`, `viz/`, `experiments/` docstrings and `sources/` were swept for the retracted claim
   and are clean of it**, closing the gap verify recorded at its §9.7. The only keyword hits are an
   unrelated `"the pigeonhole's own hypothesis"` assertion label in
   `experiments/staircase_gamma_upper.py`, and an unrelated `"part of what these computations were
   pointing at"` sentence in the `v058`–`v068` drafts, which are `sources/` and immutable by schema
   anyway. `.claude/worktrees/` was excluded, as before.
