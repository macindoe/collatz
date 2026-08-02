# Findings: verify round 4 — the subtraction is incomplete in the paper, and (g) needs one line

**Branch.** `v3r4-review-round4` at `3c30b61`; `main` at `fa9edf5`. Read-only on every tracked file; this
file is the only one written. Nothing committed, no git write operation, no worktree. The rebuild was done
on a copy in the scratchpad, so the repository working tree is untouched (`git status` shows only this
findings file and the brief).

**Verdict in one line.** The record is correct and the addition is sound, but **the paper still asserts the
retracted claim in three places, one of them verbatim on page 4**, and each contradicts the sentence this
round wrote on page 14. **Merge after four named fixes**, all small and all local.

---

## 1. Defect list, most severe first

### D1 — BLOCKING. The retracted claim survives in the paper at three sites, and contradicts the round's own corrected sentence

Round 4's whole content is that the block-time conversion is **not** supplied by the hypothesis past the
digit budget. The corrected sentence, tex L397–400, page 14:

> …which is a theorem where the cylinder count runs (`aeh.md` Lemma 13.2.4(g)) and, past it, **is neither a
> theorem nor a consequence of Hypothesis 5.1** (`aeh.md` §13.2.3).

Three other sentences in the same file say the opposite. All three are in the current build; I read them in
the rendered PDF, not only in the source.

| # | tex line | PDF page | printed text |
|---|---|---|---|
| D1a | **L59** (`Related work and provenance`) | **4** | "All of these horizons are counted in steps, and their reading in the reduced blocks of Section 5 is not free: it divides by a mean number of steps per block **that is itself part of what Hypothesis 5.1 asserts.**" |
| D1b | **L42** (`Version note`) | **2** | "…with those horizons given in the step units in which they are proved, **their reading in reduced blocks being a consequence of Hypothesis 5.1** rather than an input to it." |
| D1c | **L432–433** (§5, Inselmann paragraph) | **15** | "The further passage to block time needs the frequency with which a Syracuse step ends a block… **it is therefore a consequence of Hypothesis 5.1** and not available to underwrite it." |

**D1a is the same sentence, in the same words, that this round deleted twice.** `aeh.md` L84 read
"**part of what `13.2.1` asserts**"; paper L322 read "is **part of Hypothesis~\ref{hyp:aeh}** where it does
not". Both were removed at `123683d` and `e634513`. The identical formula survives untouched at tex L59, in
the paragraph that positions this work against Terras / Everett / Korec / Inselmann / Tao — precisely where
a novelty reviewer reads it, and precisely the comparison `publication.md` §4 exists to keep honest.
**Neither the design wave's site list (§1, §9) nor the apply wave's §6 names it.** My earlier grep for
`part of Hypothesis` missed it too; the phrase is `part of what Hypothesis~\ref{hyp:aeh} asserts`.

D1b is the same claim in the v3 version note, which also survives from before the round.

D1c is apply §6 item 2, flagged and left. **Adjudicated below at §3; it is a defect, not a false alarm.**

**Why all three are wrong, and not merely infelicitous.** The passage from Inselmann's step horizon to block
time is the division by the mean exponent per block. Round 4 established (and `aeh.md` L84, L94 now print)
that past the budget the hypothesis gives the vanishing *frequency* of `†` and nothing more, and that a
vanishing frequency is not a bound on a sum over its complement. The apply wave's defence of D1c — that the
sentence names a *frequency* (`P(s ≥ 2) = 1/2`, the density of the parity pattern `10`), which is a genuine
one-letter marginal of `B` — does not hold: AEH asserts frequencies **in block time**, and the quantity the
passage needs is the frequency of block-ending steps **in Syracuse-step time**. Converting a block-time
frequency into a step-time frequency is division by the empirical mean of `m`, i.e. the same first moment
the round retracted. `13.3.2` says so itself ("calling that `1/β` divides by `E[m] = 2` `Syr`-steps per
block"). So the statistic the sentence names is *not* asserted by the hypothesis at the time scale the
sentence needs it, and D1c is the retracted claim in the "consequence" direction.

**Fix (all three, purely subtractive — none needs the deferred result).**

* L59: replace "that is itself part of what Hypothesis~\ref{hyp:aeh} asserts" with
  "which is a theorem of the cylinder count inside the digit budget and, past it, neither a theorem nor a
  consequence of Hypothesis~\ref{hyp:aeh}".
* L42: replace "their reading in reduced blocks being a consequence of Hypothesis~\ref{hyp:aeh} rather than
  an input to it" with "their reading in reduced blocks being available from the cylinder count inside the
  digit budget and from nothing in this paper past it".
* L432–433: replace "it is therefore a consequence of Hypothesis~\ref{hyp:aeh} and not available to
  underwrite it" with "it is therefore not available to underwrite the hypothesis: inside the digit budget
  it is a theorem of the cylinder count (\texttt{aeh.md} Lemma 13.2.4(g)), and past it neither a theorem nor
  a consequence of the hypothesis (\texttt{aeh.md} \S13.2.3)".

Note that the anti-circularity conclusion each sentence exists to carry — that Inselmann's endpoint in block
units cannot corroborate AEH — **survives all three fixes and is strengthened by them**: an unsupported
conversion is even less available to underwrite the hypothesis than a consequence of it would be.

---

### D2 — HIGH. `aeh.md` `13.3.2`: "the endpoint `1/β` in block units is this page's own hypothesis, not his theorem"

**Adjudicated independently; I do not inherit the apply wave's verdict.** The sentence has an attribution
function — the contrast "not his theorem" refuses the endpoint to Inselmann — and that function is correct.
But the noun it uses to name the alternative source is **"this page's own hypothesis"**, i.e. Hypothesis
`13.2.1`, and round 4 established that `13.2.1` does not carry the block-unit endpoint. The sentence
therefore asserts of `13.2.1` exactly what the round removed from `13.2.3`.

It now contradicts two sentences on its own page, both written this round:

* L67: "its block-per-bit reading needs that average as a statement about orbits: a theorem inside the digit
  budget (`13.2.4`(g)), and **past it neither a consequence of the letter statistics asserted here** nor
  independent corroboration of them."
* L94: "below the budget that conversion is `13.2.4`(g), and **past it the record carries no orbit statement
  supplying it**."

Fifty-seven lines apart, the page says both "the record carries no orbit statement supplying it" and "it is
this page's own hypothesis".

**On the freeze.** The author deferred §7.8 (`13.2.6`) and §7.9 (the rescoping of `13.3.2`'s *first reason*).
This sentence is neither: it sits at the end of the Inselmann paragraph, and the repair is purely
subtractive and needs nothing deferred. The apply wave froze the whole of `13.3.2` and so did not reach it.
I judge the freeze over-broad on this one clause.

**Fix.** Replace "but the endpoint `1/β` in block units is this page's own hypothesis, not his theorem" with
"but the endpoint `1/β` in block units is neither his theorem nor a consequence of this page's hypothesis:
inside the digit budget it is `13.2.4`(g), and past it nothing on this page supplies it (`13.2.3`)."

---

### D3 — MEDIUM. `13.2.4`(g)'s offset parenthetical: `δ_N` does not absorb what it is said to absorb

Printed in (g):

> (The budget clause counts `Σ(m_i + s_i)` and (a)–(b) count `Σ(m_i + r_i)`; by `13.2.3` the two differ by
> `s_n − s_0`, and `max_(n ≤ T_N) s_n ≤ 2 log₂ T_N` off a `B`-event of mass `≤ 2/T_N`, which the same bound
> transfers and **which `δ_N` absorbs**.)

The `B`-mass bound `≤ 2/T_N` is right — I checked the union bound exactly, below. But `2/T_N = Θ(1/log N)`
and `δ_N(τ) = e^(−Θ(b))`, so `δ_N` cannot absorb it, and the gap grows without bound:

| `b` | `T_N` | `δ_N(τ)` | `2/T_N` | ratio |
|---|---|---|---|---|
| 400 | 80 | 1.731e−02 | 2.500e−02 | 1.444 |
| 1,600 | 320 | 1.211e−05 | 6.250e−03 | 5.161e+02 |
| 8,000 | 1,600 | 1.893e−21 | 1.250e−03 | 6.604e+17 |
| 128,000 | 25,600 | 3.558e−312 | 7.813e−05 | 2.196e+307 |

(θ = 0.20, τ = 0.90; `δ_N(τ)` = window term + tail term as (g) defines it.)

The consequence: as printed, (g)'s first bullet gives "the budget does not bind" only off a set of density
`O(1/log N)`, not `e^(−Θ(b))`, and **Corollary `13.2.4.1` inherits the error** — its "by `13.2.4`(g) the
budget binds on a set of density `e^(−Θ(b))`" is not justified by the printed argument.

**The conclusion is true and the repair is one line, using a different bound.** `S^bud_n = Σ_(i<n)(m_i+s_i)`
is nondecreasing, so only `n = T_N` matters, and `S^bud_(T_N) = S^let_(T_N) + s_0 − s_(T_N) ≤ S^let_(T_N) +
s_0 − 1`. Hence for any small `ρ > 0` with `(1−ρ)τ > 4θ`,

```text
P(S^bud_(T_N) >= Lam_N)  <=  P(S^let_(T_N) >= (1-rho) Lam_N)  +  P(s_0 > rho Lam_N),
```

the first term `e^(−I(θ,(1−ρ)τ)b + o(b))` by (a)–(b) at budget `(1−ρ)τ`, the second `≤ 2^(−ρΛ_N+1) =
e^(−Θ(b))`. So `e^(−Θ(b))` survives, and the `max_(n ≤ T_N)` bound — which is both unnecessary (one index
suffices) and too weak (it costs `1/log N`) — should be replaced by this. I measured the boundary letter's
law to confirm the second term behaves: over 4,000 uniform odd starts at `b = 1200`, `P(s_0 = 1..8) =
0.5032, 0.2392, 0.1328, 0.0663, 0.0320, 0.0107, 0.0070, 0.0050` against `2^(−j)`, mean `1.99475`, maximum
`13`.

I also confirmed the printed `≤ 2/T_N` is correct as stated: the exact union bound
`(T_N+1)·P(s > ⌊2log₂T_N⌋)` is `1.9775e−02 / 4.8981e−03 / 7.6342e−04 / 1.9076e−04` at
`b = 400 / 1600 / 8000 / 32000`, against `2/T_N = 2.5e−02 / 6.25e−03 / 1.25e−03 / 3.125e−04`.

---

### D4 — MEDIUM (compliance). `13.2.4`'s **Verified** line does not cover (g)

`AGENTS.md`, *Before marking anything "proved"*: run an independent numerical check — a fresh
implementation, not the one quoted in the text — and record what was checked, the range and the date in the
page, as one current line. `aeh.md`'s front matter says "unconditional base case **PROVED** at 13.2.4", and
(g) is new proved content inside that lemma.

The Verified line (L112, dated 2026-08-02) covers: the exhaustive cylinder count at `J = 18, 20, 22`; class
invariance mod `2^(S_n+1)`; the general window at seven `N`; the tail identity `P_B(S_n ≥ J) =
P(Bin(J−1,1/2) < 2n)` at five `(n,J)`; pattern-frequency concentration; the boundary transient; and (c).

It covers **none of (g)'s new computational content**: the rate `I(θ,τ) = τ(log 2 − H(2θ/τ))`, its reduction
to `I(θ)` at `τ = 1`, the budget-non-binding density, or the exponent-mean concentration. The design wave's
consequence trace explicitly predicted the Verified block would survive verbatim because "(g) adds no new
computational claim beyond the tail identity already verified there" — that is not right; the rate formula
and the mean convergence are both new.

**What would close it.** A line recording: (i) `I(θ,τ)` reproduces the printed `I(θ)` at `τ = 1`; (ii)
`I(θ,τ)` is the measured exponential decay rate of the tail term; (iii) on real odd starts, at consistent
`(τ,θ)` with `τ < 1`, the budget does not bind and `T_N^(−1)Σ(m_n+r_n) → 4`, with a negative control at
`τ < 4θ`. **I ran exactly that check** — §2.4 below has the numbers, ready to be quoted. I did not edit the
page.

---

### D5 — LOW (but printed as a mathematical fact). "positive precisely for `τ > 4θ`" is false of the expression

(g) prints: "at the exact rate `I(θ, τ) = τ(log 2 − H(2θ/τ))` … — **positive precisely for `τ > 4θ`**, `0` at
`τ = 4θ`, and equal to (b)'s `I(θ) = log 2 − H(2θ)` at `τ = 1`."

`log 2 − H(p) > 0` for every `p ≠ 1/2`, so the expression is positive on **both** sides of `τ = 4θ`. Values I
computed: `I(0.20, 0.75) = +0.001667903`, `I(0.24, 0.95) = +0.000052633`, `I(0.20, 0.50) = +0.09637238` — all
at `τ < 4θ`. And for `τ ≤ 2θ` the expression is not defined at all (`2θ/τ ≥ 1`).

What *is* true is that the **tail term vanishes** precisely when `τ > 4θ`; below that threshold the true rate
is `0`, not `I(θ,τ)`. Measured: at `(θ,τ) = (0.20, 0.50)` the tail is `1.0000000000` at `b = 500, 2000, 8000,
32000`; at `(0.24, 0.80)`, `0.9999706 → 1.0000000`; at `(0.10, 0.30)`, `0.9999822 → 1.0000000`.

**Fix.** "…at the exact rate `I(θ,τ) = τ(log 2 − H(2θ/τ))` on the range `4θ < τ`, where it is positive, `0` at
`τ = 4θ`, and equal to (b)'s `I(θ)` at `τ = 1`; past that threshold the tail term does not vanish at all."

---

### D6 — LOW. "the two clauses of admissibility are exactly the two terms of (a)" over-claims, and the paper repeats it unqualified

`13.2.3` defines *admissible* = *protected* ∧ *consistent*, and *protected* runs to `τ < 4.8188…`
unconditionally (bullet 2). For an admissible pair with `1 ≤ τ < 4.8188…` the window term does **not**
vanish, so the two clauses of admissibility are not the two terms of (a). The identification holds only on
(g)'s own range `4θ < τ < 1`, where it is a coincidence of thresholds rather than of mechanisms: `τ < 1` is
also what the *altitude bound* needs, but the window term of (a) is the price of a general `[N,2N)` over a
dyadic one, which is a different fact with the same threshold.

`aeh.md` (g) states the correct content immediately after the headline ("`τ < 1` is what makes the window
term … vanish, and `4θ < τ` is what makes the tail term vanish"), so the page self-corrects. **The paper does
not**: tex L328–329, page 13, prints only "(`aeh.md` Lemma 13.2.4(g), whose two error terms are precisely the
two clauses of admissibility)". Add "on that range" or "which on that range are precisely…".

---

### D7 — LOW. `paper` L321 cites the wrong Inselmann theorem for protection, in the sentence that says "nothing converted"

> every `$\tau < (1-\log_2\sqrt3)^{-1} = 4.8188\ldots$` is protected at natural density one by Inselmann
> `\cite[Thm.~1.10]{inselmann}` --- **the same unit, nothing converted.**

`τ` is a division count (`T_1`-time). `13.3.2` records that Thm 1.10 is the **Syracuse** envelope
(`2.4094…` `Syr`-steps per bit) and Thm 1.1 is the `T_1` one; `aeh.md` L82 correctly cites "Thm `1.1`/`1.10`".
So the sentence claims the unit is unconverted while citing the theorem stated in the converted unit — which
is the exact genre of slip this round exists to remove. `\cite[Thms.~1.1 and~1.10]{inselmann}` fixes it.
(Design §7.18 flagged it optional; apply §6 item 3 left it. I rate it above cosmetic for that reason.)

---

### D8–D10 — NITS, listed for completeness

* **D8.** `publication.md` L41: "The horizons are unconditional in step time; **their reading as `1/β` blocks
  per bit is not**." Read literally this implicates that the block reading *is* conditional-on-AEH; after
  round 4 it is neither. It points at L29, which is now correct, so the reader is not misled for long.
  "…is not available at all past the digit budget" would close it.
* **D9.** `aeh.md` L8 (`Current state`) is not wrong, but it does not carry the round's correction. The apply
  wave's reason for leaving it (the §7.12 drop-in consisted solely of the deferred prefix clause) is right
  about that drop-in; a purely subtractive clause — "…and past that budget what it supplies is frequencies
  and not the exponent mean (13.2.3)" — needs nothing deferred. A page's Current-state paragraph is where its
  current answer lives.
* **D10.** `open-problems.md` `11.11`'s opening restates `13.2.4`(g)'s content rather than pointing at it
  (`AGENTS.md`: "Every fact lives in exactly one page. Other pages point to it; they do not restate it"). It
  does cite (g), and the restatement is needed to pose the questions, so this is a convention nit only.

---

## 2. `13.2.4`(g), derived independently, and the numerical check

### 2.1 The derivation

Setup as in `13.2.4`: `x` uniform on the odd integers of `[N,2N)`, `b = ⌊log₂N⌋`, `T_N = ⌈θb⌉`,
`ℓ_n = (m_n, r_n)`, `S_n = Σ_(i<n)(m_i+r_i)`. Fix `4θ < τ < 1`, `Λ_N = ⌈τb⌉`, and take `J = Λ_N` in (a)–(b).

**The substitution is exact.** (b)'s standing hypothesis is `J = ⌈(1−η)b⌉` with `0 < η < 1 − 4θ`. Putting
`J = Λ_N` forces `η = 1 − τ`, and `0 < 1−τ < 1−4θ` **is** `4θ < τ < 1`, character for character. ✓ And
`J = Λ_N → ∞ ≥ 2`. ✓

**Window term.** `N ∈ [2^b, 2^(b+1))` and `Λ_N ≤ τb + 1`, so `2^(Λ_N+2)/N ≤ 8·2^(−(1−τ)b)`, i.e.
`O(N^(−(1−τ)))`, vanishing iff `τ < 1`. At `τ = 1` it is `Θ(1)` and at `τ > 1` it diverges: I computed
`2^(Λ_N+2)/2^b = 2^(−198), 2^(−18), 2^2, 2^(102)` at `(b,τ) = (2000, 0.90), (2000, 0.99), (2000, 1.0),
(2000, 1.05)`. ✓ **Printed claim correct.**

**Tail term and the rate.** `P_B(S_(T_N) ≥ Λ_N) = P(Bin(Λ_N−1, 1/2) < 2T_N)` by (b). With `M = Λ_N−1 ≈ τb`
trials and threshold `2T_N ≈ (2θ/τ)M`, Cramér's rate per trial for the lower tail of `Bin(M,1/2)` at level
`pM` is `D(p‖1/2) = log 2 − H(p)`, so per bit of start the rate is `τ(log 2 − H(2θ/τ))`. ✓ **The formula is
correct**, on `p = 2θ/τ < 1/2`, i.e. exactly on `τ > 4θ` — and *only* there, which is D5.

At `τ = 1` it reduces to `log 2 − H(2θ)`, (b)'s `I(θ)`, identically. ✓

**Transfer.** `|P(A) − Q(A)| ≤ TV(P,Q)` for every event, so with `δ_N(τ)` = window + tail:
`P(S_(T_N) ≥ Λ_N) ≤ P_B(S_(T_N) ≥ Λ_N) + δ_N(τ) ≤ 2δ_N(τ)`. ✓ **The constant 2 is right.**
`S_n` is nondecreasing, so this single event controls the whole horizon. ✓

**The budget clause versus the letter count.** `13.2.1` budgets `Σ(m_i+s_i)`; (a)–(b) count `Σ(m_i+r_i)`; with
`r_i = s_(i+1)` the two differ by exactly `s_n − s_0` — I verified this identity on every simulated orbit as
an assertion in the code, 1,220 orbits, zero failures. **This is where (g) is wrong (D3), and repairable.**

**Second bullet.** Under `B^(⊗T_N)`, `S_(T_N)` is a sum of `2T_N` iid geometric(1/2) on `{1,2,…}`, i.e. the
waiting time for the `2T_N`-th head, of mean `4T_N`. `E_B[m] = E_B[r] = 2`, so `E_B[m+r] = 4`. ✓ Geometric
summands have exponential moments, so Cramér gives `P_B(|S_(T_N)/T_N − 4| > ε) ≤ 2e^(−c(ε)T_N)`, and adding
the TV gives exactly the printed `δ_N(τ) + 2e^(−c(ε)T_N)`. ✓ **Correct.**

**Range.** `4θ < τ < 1` is solvable iff `θ < 1/4`. ✓ And (f)'s `I(1/4) = 0` closes the range. ✓

**Corollary `13.2.4.1`.** With (g)'s repair it follows: off the exceptional set the tallied word is the
letter word, so (d) is `13.2.1`'s conclusion and (e) is `13.2.2`'s, at every admissible `τ < 1`; the added
quantification over `τ` and the identification step it was previously missing are both now present. ✓ Its
"density `e^(−Θ(b))`" is correct **only after D3 is repaired**; the printed (g) argument gives `O(1/log N)`.

**Verdict on (g).** *The theorem is true, the two substantive claims are correct, the substitution
`η = 1 − τ` is exact, and the rate is right on its range.* Three defects, none fatal: the offset absorption
(D3, one line to repair), the positivity clause (D5, wording), and the admissibility headline (D6, wording).

### 2.2 Exact tail identity, fresh code

`P_B(S_n ≥ J)` computed by exact rational convolution of `2n` geometric(1/2) laws (no Binomial anywhere in
that routine) against `P(Bin(J−1,1/2) < 2n)`, at ten `(n,J)` pairs chosen not to overlap the page's five:

```
(1,3) 3/4   (2,6) 13/16   (3,8) 15/16   (4,11) 121/128   (5,13) 4017/4096
(6,17) 63019/65536   (7,21) 247029/262144   (2,30) 2045/268435456
(8,40) 428618123/4294967296   (10,33) 3832555763/4294967296
```

**All ten equal, exactly.** (My first implementation dropped the tail mass at the truncation key and failed
all ten; the bug was in the check, not in the page — recorded so the number above is not mistaken for a
first-try pass.)

### 2.3 The rate, measured

`I(θ) = log 2 − H(2θ)` at `θ = 0.20 / 0.24 / 0.25`: `0.020135513551 / 0.000800213470 / 0.0`, matching
`aeh.md` L65's printed `0.0201 / 0.00080 / 0`. `I(θ,1) = I(θ)` to double-precision equality at
`θ = 0.05, 0.10, 0.15, 0.20, 0.22, 0.24, 0.245, 0.25`.

`−ln P(Bin(⌈τb⌉−1,1/2) < 2⌈θb⌉)/b` against `I(θ,τ)`, log-sum-exp on exact log-binomials:

| `(θ,τ)` | `I(θ,τ)` | b=500 | b=2,000 | b=8,000 | b=32,000 | b=128,000 |
|---|---|---|---|---|---|---|
| (0.20, 0.90) | 0.00556704 | 0.00939967 | 0.00682536 | 0.00596452 | 0.00568782 | 0.00560264 |
| (0.20, 0.99) | 0.01834593 | 0.02322322 | 0.01989386 | 0.01881831 | 0.01848561 | 0.01838626 |
| (0.24, 0.99) | 0.00045462 | 0.00277343 | 0.00121123 | 0.00070699 | 0.00053700 | 0.00048044 |
| (0.20, 0.81) | 0.00006173 | 0.00182364 | 0.00058627 | 0.00022896 | 0.00011731 | 0.00008013 |

Monotone convergence to `I(θ,τ)` from above in every row, including the row with `τ` a hair above `4θ`.

### 2.4 Real orbits — the check that would close D4

Fresh block decomposition built from the record's own definitions (`stage1.md`'s size ledger: `x = 2^m u − 1`
has exit `(3^m u − 1)/2^s`; `13.2.3`'s `m + s` divisions per block), big-integer arithmetic, importing
nothing from `experiments/`. Uniform odd starts in `[2^b, 2^(b+1))`.

| `b` | `θ` | `τ` | `T_N` | `Λ_N` | budget bound | exponent mean `T_N^(−1)Σ(m+r)` (s.d.) | `E[m]`, `E[r]` |
|---|---|---|---|---|---|---|---|
| 400 | 0.20 | 0.90 | 80 | 360 | 8 / 400 | 4.00887 (0.22273) | 1.9999, 2.0090 |
| 800 | 0.20 | 0.90 | 160 | 720 | **0 / 300** | 4.00317 (0.15038) | 1.9965, 2.0067 |
| 1,600 | 0.20 | 0.90 | 320 | 1,440 | **0 / 200** | 3.99248 (0.11232) | 1.9982, 1.9943 |
| 3,200 | 0.20 | 0.90 | 640 | 2,880 | **0 / 120** | 3.99111 (0.08547) | 1.9955, 1.9956 |
| 1,600 | 0.24 | 0.99 | 384 | 1,584 | 30 / 200 | 4.01137 (0.09851) | 2.0069, 2.0045 |
| 1,600 | 0.10 | 0.50 | 160 | 800 | **0 / 200** | 4.00519 (0.15782) | 1.9974, 2.0078 |

The two rows where the budget binds are the two where `δ_N(τ)` is still large: `δ_N = 1.73e−02` at
`b = 400` (observed 0.020, bound `2δ_N = 0.035`) and `δ_N = 1.14e−01` at `(1600, 0.24, 0.99)` (observed
0.150, bound `2δ_N = 0.228`). **The printed bound is respected in every row.**

Negative controls at inconsistent pairs (`τ < 4θ`), which (g) predicts must bind:

| `b` | `θ` | `τ` | `4θ` | budget bound |
|---|---|---|---|---|
| 1,600 | 0.24 | 0.90 | 0.96 | 199 / 200 |
| 1,600 | 0.20 | 0.70 | 0.80 | 200 / 200 |

Seeds 91001–91008, 77001. Scripts in the scratchpad (`g_check.py`, `g_check2.py`); not committed, per the
read-only constraint.

---

## 3. The two flagged sentences and the three unedited sites

| site | verdict |
|---|---|
| `aeh.md` `13.3.2` "…is this page's own hypothesis, not his theorem" | **Defect — D2.** The attribution reading is real but the sentence names `13.2.1` as the source of a claim `13.2.1` does not carry, and contradicts L67 and L94. Fix is subtractive and needs nothing deferred. |
| `paper` L432–433 "…consequence of Hypothesis~\ref{hyp:aeh} and not available to underwrite it" | **Defect — D1c.** *Not* consistent with L397–400: page 14 says the block-time reading is neither a theorem nor a consequence of the hypothesis; page 15 says it is a consequence. The apply wave's defence (the statistic is a one-letter marginal) fails because AEH gives block-time frequencies and the sentence needs a step-time one, which is again the mean. |
| `aeh.md` L8 (Current state) | **Reasoning verified; reads correctly.** "There is no drift or contraction consequence: equidistribution at each fixed `k` does not deliver one, and the corresponding trajectory statement is unconditionally known anyway (13.3.2)" is a pure negative, carries nothing retracted, and is exactly what frozen `13.3.2` still says. Editing it with the §7.12 drop-in would indeed have claimed the deferred result. See D9 for the separate gap the apply reasoning does not cover. |
| `paper` L246 | **Reasoning verified; reads correctly.** "…window equidistribution at each fixed `(k,D)` does not control the means of the unbounded `m_+` and `s`, so no drift or contraction statement about orbits follows from it (`aeh.md` §13.3.2)" is a negative, and it names the round-4 mechanism (the uncontrolled means) more precisely than the drop-in would have. Nothing retracted survives. |
| `publication.md` L41 | **Reasoning verified; reads correctly.** "**Claim no descent or drift consequence for AEH** (aeh.md `13.3.2` carries none)" is true with the prefix result absent, and nothing in the repository now claims one. One soft implicature at D8. |

---

## 4. Was the deferral honoured? — Yes

* **`13.3.2` is byte-identical to `fa9edf5`.** Old `aeh.md` L118 and new L124 both hash
  `bb60789b566fcd2b8c2604788cd00400`. Every diff hunk in `aeh.md` is at 67, 69, 83–84, 86, 89–91, 93, 97,
  102–104, 116, 201 (old numbering); L118 is in none of them. (This is also why D2 was not reached.)
* **No anchor renumbered, none added.** The set of `1[23].x` anchors in `aeh.md` is identical before and
  after: `12.6.1.4 12.6.1.5 12.8.4 13.1 13.2 13.2.1 13.2.2 13.2.3 13.2.4 13.2.4.1 13.2.5 13.3 13.3.1 13.3.2
  13.3.3 13.4 13.5 13.5.1 13.6 13.6.1 13.6.2 13.6.3 13.6.4 13.6.5 13.6.6 13.6.7`. `13.2.4`(g) appends to an
  existing lemma.
* **`13.2.6` appears nowhere** in any tracked page or in the paper — no dangling pointer to the deferred
  proposition.
* **Nothing claims the prefix result or a conditional drift.** Swept `aeh.md`, the paper, `publication.md`,
  `open-problems.md`, `index.md`, `stage1.md`, `README.md`, `bridge.md`, `HANDOFF.md`, `TOUR.md`,
  `itinerary.md`, `program.md`, `spine.md`, `stage4.md` for `prefix`, `in-budget`, `n*`, `drift consequence`,
  `descent consequence`, `contraction consequence`. Every hit is a negative statement or the open questions.
* **`open-problems.md` `11.11` states two checkable questions and claims neither.** The section says so
  explicitly ("neither is claimed by any page, and `13.3.2` stands as written until the first closes");
  question 1 gives closure criteria in both directions and names the hinge (the `τ ↓ 4θ` quantifier);
  question 2 is explicitly conditional on question 1 and records that `13.3.2`'s second reason and its
  conclusion are not in question either way. Both point at `briefs/v3r4-clock-findings.md` §2 and §7.8 for
  the drafted argument. The front-matter `scope:` field records `11.11` as post-monolith, and `11.9` is
  correctly left vacant.

---

## 5. The pin

**`e634513` verified independently**, by extracting every `\texttt{...md}` and `\texttt{experiments/...}`
citation from the `.tex` and checking each against `git show e634513:`, not against the working tree.

**Named and present at `e634513`:** `aeh.md` §13.1, §13.2.3, Lemma 13.2.4, Lemma 13.2.4(g), Corollary
13.2.4.1, Proposition 13.2.5, §13.3.2, §13.4, §13.5, Lemma 13.6.3 with items (iii) and (v), Theorem 13.6.4,
§13.6.5; `itinerary.md` §14.15.1.5; `stage3.md` §11.8.6.3; `cycles.md` §§12.2.3, **12.5.2**, **12.5.3**,
12.6.1, **12.6.2**, **12.7.4**, **12.7.5**, 12.8.6; and all six scripts
`experiments/{period1,period2,period3}_cycles.py`, `one_step_propagation.py`, `anchor_increment.py`,
`absorption_law.py`. All ten files present, all anchors found.

**The five bolded `cycles.md` sections are ones the apply wave's verification did not list** (its §4 names
only 12.2.3, 12.6.1, 12.8.6). They are all present, so the pin's claim holds; but the check behind it was
incomplete, and I record that so the next pin move does not repeat the omission.

**Negative checks at `e634513` (`aeh.md`):** `P_B(S_(n+1)` — absent; `in Cesàro form` — absent;
`own content` — absent; `No τ ≥ 4.8188… is protected` — absent; `all of them within budget` — absent;
`13.2.6` — absent. **Positive:** `P_B(S_n ≥ J)` present (5 hits); `13.6.4`'s cell reads
`of π_{k,D}-mass at most`; `13.2.3` reads `compatibility with the target law`; (g)'s rate string present.

**The pin is well formed.** `e634513` is an ancestor of `HEAD`; the only files differing between `e634513`
and `HEAD` are `paper/collatz-reduced-v3.{tex,pdf}` (the pin commit itself) and the two round-4 apply
briefs — so every wiki page and script the paper names is *identical* at the pin and at branch tip. The
justification for moving is also verified: `git merge-base --is-ancestor 677a76a 276b87c` succeeds, so the
old pin did predate round 3's own residual corrections. The two historical pins `72ec88e` and `9d9d1ec`
(published version-note text, both pointing at `cycles.md` §12.8.6) are untouched, correctly.

---

## 6. Build and rendered layout

Clean build in the scratchpad from a copy of the branch `.tex`, no `.aux` carried over.

| pass | exit code | pages | bytes |
|---|---|---|---|
| 1 | 0 | 17 | 434,853 |
| 2 | 0 | 17 | 434,853 |
| 3 | 0 | 17 | 434,853 |

* **Overfull boxes: zero.** **Underfull: one** — `\hbox (badness 1067)` at tex L484–485, the `lagarias`
  bibitem inside `\thebibliography`. Independently confirmed pre-existing: rebuilding `fa9edf5`'s `.tex`
  reproduces `badness 1067` at L470–471 (the same bibitem; the 14-line shift is this round's insertions
  above it) and also gives 17 pages.
* **Unresolved references: none.** The log contains no `LaTeX Warning` of any kind — no undefined reference,
  no undefined citation, no rerun request. The only warning line in the whole log is the underfull hbox.
* **Content-identical to the committed PDF.** Same page count (17), same byte size (434,853), and
  `pdftotext -layout` output byte-identical. The files differ only in the MD5 (`045e6e9a…` rebuilt vs
  `d82949…` committed), which is the embedded `CreationDate`/`ModDate` — the committed PDF is the artifact
  the branch's `.tex` produces.
* **Repository untouched:** I built on a copy, so `paper/*.aux`, `*.log`, `*.pdf` in the repo are unmodified
  and there is nothing to avoid committing.

**Rendered layout, looked at (not extracted).** Pages 13, 14, 15, 16 at 130 dpi, plus page 4 for D1a.

| page | content | layout |
|---|---|---|
| 13 | the restated `Consistency is compatibility with the target law` paragraph, `13.2.4(g)` citation, `a vanishing frequency of † is not a bound on a sum over its complement`, the `→ 4 does not follow` clause | clean; the long paragraph justifies evenly, the inline display `T_N^{-1}\sum_{n<T_N}(m_n+r_n) \to 4` sits on one line, `4.8188…` and `1/β = 1.2047…` break correctly at line end |
| 14 | the `Hence 4θ<τ<1 …` continuation, the base-case display, the restated L397–400 endpoint sentence | clean; the TV display is well set; `\S13.2.3` and the `13.2.4(g)` pointer both fall inside the line |
| 15 | the Inselmann paragraph carrying D1c | clean; no bad break |
| 16 | Appendix A with the new pin | clean; `e634513` sits in `\texttt` on one line |
| 4 | Related work, carrying D1a | clean typographically — the defect is the sentence, not the setting |

No broken display, no bad break, no orphan or widow introduced by this round.

---

## 7. Housekeeping

* **UTF-8.** `aeh.md`, `open-problems.md`, `publication.md`, `index.md`, `stage1.md`, `itinerary.md`,
  `HANDOFF.md`, `AGENTS.md`, `README.md`, `paper/collatz-reduced-v3.tex` all decode as valid UTF-8, no BOM,
  no `Ã`/`Â`/`â€` sequence, no `U+FFFD`. `aeh.md` glyph counts old → new: `≤` 52→61, `—` 170→179, `ε` 29→34,
  `θ` 42→58, `τ` 23→47, `†` 6→9, `β` 15→16, `≥` 66→67, `→` 26→29, `Λ` 9→13, `Σ` 25→30. Every delta is
  non-negative; nothing was lost to re-encoding. (CRLF line endings are present in every page including ones
  this round did not touch, so they are the checkout's convention and not a round-4 artifact.)
* **No theorem statement moved.** The set of `\begin{theorem|proposition|lemma|corollary|hypothesis|
  heuristic|definition|remark}` environments and every `\label{}` is identical at `fa9edf5` and at `HEAD`,
  and all three `.tex` diff hunks (L319–341, L396–408, L458) fall outside every theorem environment.
  `hyp:aeh` (L248–276) is untouched symbol for symbol.
* **No change logs or dated journals added.** Nothing in the `aeh.md`, `open-problems.md` or
  `publication.md` diffs is "was X, now Y" prose, a session journal, or a dated verification record beyond
  the single current `Verified` line the schema requires.
* **Cross-page status pass.** `index.md` L26 ("formalized; calibration clean; symbolic form named and
  proved") and L46 (the base case at `θ < 1/4`, exceptional set at shell scale, "the hypothesis is exactly
  what lies past that budget"), `README.md` L40 ("no drift or contraction consequence follows"),
  `TOUR.md` L15/26, `bridge.md` L69, `HANDOFF.md` L20, `stage1.md` L579 and L620 (the ledger "formal inside
  the digit budget", citing `13.2.4`(d)–(e) and `13.2.4.1`), `open-problems.md` L86 and `itinerary.md` L73
  were all checked against `aeh.md`'s front matter and against the corrected `13.2.3`. **No mismatch.**
  Every one of these cites the in-budget conclusion, which (g) strengthens rather than moves.
* **The apply wave's other three unfixed items.**
  * `paper` L321 Inselmann cite — **not harmless**, see D7.
  * `aeh.md` L58 "for every `J ≥ 1`" against `13.2.4`(a)'s `J ≥ 2` — **harmless, confirmed.** At `J = 1`,
    `P_B(S_n ≥ 1) = 1` for `n ≥ 1`, so the bound reads `TV ≤ 2^3/N + 1`: true and vacuous, never false.
  * `13.6.3`(i)(a)'s "(irrelevant to every Cesàro limit below)" against the new `13.2.3` sentence —
    **harmless, confirmed.** (i)(a)'s "below" scopes to §13.6's frequency limits, where a one-index shift
    moves a frequency by `O(1/T_N)`; `13.2.3` localises the one place a *sum* over an unbounded letter is at
    stake, which is at the budget boundary in §13.2 and not "below" 13.6.3.
* **`13.6.4`'s "at most" — arithmetic independently confirmed.** With `s` geometric(1/2) on `{1,2,…}` and
  `σ_n = s_n + m_n` a sum of two independent such, `P(σ_n ≥ D) = D·2^(−(D−1))` (checked at `D = 2`: 1, and
  `D = 3`: 3/4) and `P(s_(n+1) ≥ D) = 2^(−(D−1))`; the sum is the printed `(D+1)·2^(−(D−1))` and the
  double-counted intersection is `D·2^(−2(D−1))`. "at most" is correct, the downstream clause
  `L(D+1)·2^(−(D−1))` is valid unchanged, and no downstream number moves.

---

## 8. Merge recommendation

**Merge after fixes — do not merge as-is.**

Everything that landed is an improvement and nothing that landed is false, except inside (g) at D3/D5/D6,
which are repairable in place. The record half of the round is done properly: `13.2.3` is honest, `13.2.4`(a)
is sharp, `13.2.4`(g) is a real unconditional gain, the deferral is respected exactly, `13.3.2` is untouched
to the byte, `11.11` claims nothing, the pin is right, the build is clean, and the pages render correctly.

But the round's stated purpose was for the paper to **say less about what AEH supplies**, and the paper still
says it three times, including verbatim on page 4 in the paragraph a novelty reviewer reads first, and
including in the version note that describes what v3 does. As it stands, the paper contradicts itself about
the round's own headline point on pages 2, 4 and 15 versus pages 13 and 14. Merging that publishes an
internal inconsistency created by a round whose purpose was to remove it.

**Required before merge:** D1 (three tex sentences), D2 (one `aeh.md` clause), D3 (one line inside (g), plus
`13.2.4.1` reading correctly after it), D4 (extend the `Verified` line — the check is run and its numbers are
at §2.2–2.4).

**Recommended in the same pass, since the file is open anyway:** D5, D6, D7.

**Author's call, no strong view:** D8, D9, D10.

All required fixes are subtractive or citational; none needs the deferred prefix result, none reopens
`13.3.2`'s first reason, and none touches a theorem statement. A rebuild and a re-run of the (g) check is all
the re-verification they need.

---

## 9. What I could not check

Named plainly, as required.

1. **The counterexample of `13.2.3`'s consistency bullet was not re-simulated.** I checked its arithmetic —
   a letter of size `cT_N` at an in-budget index moves the mean by `c`, the following `o(T_N)` cemetery
   blocks keep `†`'s frequency vanishing, and one block in `T_N` moves any fixed pattern frequency by
   `O(1/T_N)` — and I confirmed the budget clause has the slack `(τ−4θ)b` the construction needs. I did not
   rerun the design wave's synthetic-word simulation.
2. **The `L = 1` Fatou bound and the `τ ↓ 4θ` diagonal** (the deferred prefix argument, now
   `open-problems.md` `11.11`) — out of scope this round and not adjudicated. I take no position on whether
   question 1 closes affirmatively.
3. **Inselmann's paper was not read.** Every claim about Thm 1.1, 1.4, 1.6, 1.10 and Thm 3.8 — including
   D7's premise that Thm 1.10 is the Syracuse envelope and Thm 1.1 the `T_1` one — is taken from
   `briefs/v3r3-inselmann-horizon-findings.md` and from `13.3.2`'s own text, not from the source.
4. **The law of the boundary letter `s_0` under the *orbit* measure** was measured empirically (4,000 starts
   at `b = 1200`, geometric to three decimals) but not derived. D3's proposed repair needs a tail bound on
   `s_0`, and I did not prove one; the measurement supports it.
5. **`c(ε)` in (g)'s second bullet is not made explicit** on the page and I did not compute it. The Chernoff
   rate for a sum of geometrics exists and is positive; I verified the convergence empirically (§2.4) rather
   than bounding the constant.
6. **The Chernoff-rate convergence in §2.3 is asymptotic, not a proof.** The measured `−ln tail/b` approaches
   `I(θ,τ)` from above at every `b` tested; I did not verify the second-order term or bound the finite-`b`
   discrepancy.
7. **`archive/`, `sources/`, `viz/` and `experiments/` docstrings were not swept** for surviving instances of
   the retracted claim. My sweep covered the tracked wiki pages, `README.md`, `TOUR.md`, `HANDOFF.md`,
   `AGENTS.md` and the paper. (`briefs/` was read but is a record, not a claim surface.)
8. **The calibration numbers were not re-measured.** The flagship run's `τ ≈ 2.29`, `4.0017` exponent per
   block, `22` of `30` blocks past the budget, and `13.4`/`13.5`'s statistics are quoted from the page.
9. **No LaTeX visual diff against the pre-round PDF.** I compared page count, byte size and `pdftotext
   -layout` output for the rebuilt-versus-committed pair, and I rendered and read five pages of the new
   build; I did not render the `fa9edf5` build and compare images page by page.
10. **The `.claude/worktrees/` tree contains dozens of stale agent worktrees** carrying old copies of the
    wiki. I excluded them from every sweep. They are not tracked content, but if any is ever merged from,
    it will carry pre-round text.
