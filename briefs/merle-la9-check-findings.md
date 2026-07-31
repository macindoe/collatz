# L-A9 check (δ8 impossibility) + round-12 offers-discharge — findings

**Session:** delegated verification, branch `merle-la9-check`, base `9d9d1ec`
(the worktree was cut at the stale `3eab8f1` and fast-forwarded to `9d9d1ec`
before starting, per the brief's setup step). Date: 2026-08-01 (the session
was interrupted by a spend limit mid-run on 2026-07-30 and resumed; all
mid-flight conclusions were re-derived by the committed script, not trusted
from memory). Verifier: `experiments/merle_la9_check.py` + committed output —
**50 checks, 0 failures**, fresh code importing nothing from either Merle
repository and nothing from any earlier check of ours; canaries printed
first, pinned to externally recorded numbers; logs at two working precisions
with agreement asserted; every decision that can be an exact integer
comparison is one.

## 1. The repositories, read-only, and the record

Fresh clones in the session scratchpad, no writes, no interaction beyond
`git clone`.

- Shared repo `macindoe/one-obstruction-three-faces`: **HEAD `7c05458`**,
  exactly as the brief expected (`78f80f0` seeds L-A9 and discharges the
  round-11 offers; `7c05458` is the one-hash fix on top, correcting offer
  e's hash from `4f4bb2e` to `7f20348` — the correction is right, see §5).
- His Lean repo `ericmerle3789/one-obstruction-three-faces-lean`: **HEAD
  `d48ba9e`** (`7f20348` the round-11 repairs, `4f4bb2e` the REQ-067
  precision fix, `d48ba9e` opens `rounds/`). No drift in
  `T1Structure.lean` after `7f20348`.

### 1.1 The L-A9 entry, verbatim (LEDGER.md at `7c05458`)

> ## L-A9 — The δ8 impossibility: no uniform Product-Bound refinement closes the window (Merle, correspondence 2026-07-29)
>
> **DRAFT — one key (Merle: scripts, exact arithmetic, canaries). Macindoe key invited.**
>
> Seeded because `NOTE.md`'s own header rule requires it: every numbered claim enters via this ledger first, and Face I's Merle half — the δ8 impossibility, cited in `NOTE.md` §2 and §6 and in the shared README — had no entry at all. Macindoe raised the omission in round 11 by applying that rule, and deliberately created no entry for it; this is that entry.
>
> **The claim.** The Product-Bound chain cannot be closed by any improvement in effective Diophantine constants. It is not that the required exponent is hard to reach: it is **below the absolute floor of rational approximation**.
>
> > To close the current window (Barina `2⁷¹`; Hercher `1.375·10¹¹`) through the Product-Bound chain, the required effective irrationality measure has exponent **`c* ≈ 0.9617`** (`0.9622` with the exact Barina bound `2075·2⁶⁰`). By Dirichlet, every irrational `ξ` admits infinitely many `|ξ − p/q| < 1/q²`, so **no irrational has an effective exponent below 2**. Hence `c* < 2` closes the route for every constant, not merely for `log₂3`.
>
> The deficits, for scale rather than for the argument: at the diophantine dream `c = 2` — conjectured for `log₂3`, true for almost every real — `k_max = 1.9205·10⁷` against Hercher's `1.375·10¹¹`, a missing factor **7159.5** on `k`; closing at `c = 2` would instead require `X₀ = 2^109.4` against Barina's `2^71`, a missing **2^38.4** of computation. At Salikhov's real `c = 5.125`, `k_max = 3693`, short by a factor of about 37 million.
>
> **The scissors, and why brute force runs the wrong way.** The lower jaw grows as `k_max(X₀) = (3X₀)^{1/(c+1)} ≤ X₀^{1/3}` even at `c = 2`. The upper jaw — Crandall on the real convergents of `log₂3` — grows as `k_min(X₀) ~ X₀^α` with **α measured at 0.482–0.511** over `X₀ ∈ [2⁷¹, 2⁴⁰⁰]`. Since `1/2 > 1/3`, **the open window `(k_max, k_min)` widens as verification advances**: ratio 1817 at `2⁷¹`, `9·10¹⁹` at `2⁴⁰⁰`. Each GPU-year spent on verification enlarges the no-man's-land this chain would have to cross. Sanity check recorded with it: raw Crandall at `2⁷¹` gives `3.49·10¹⁰`, a factor 3.9 below the refined Hercher threshold — same order, as it should be.
>
> **Artifacts**, both already public in this project's Lean repository and both re-run on 2026-07-29 with canaries passing: [`experiments/test_REQ-MATH-001_scissors_cstar.py`](https://github.com/ericmerle3789/one-obstruction-three-faces-lean/blob/main/experiments/test_REQ-MATH-001_scissors_cstar.py) (the exponent and the two deficits) and [`experiments/test_REQ-MATH-004_scissors_race.py`](https://github.com/ericmerle3789/one-obstruction-three-faces-lean/blob/main/experiments/test_REQ-MATH-004_scissors_race.py) (the race between the jaws).
>
> **Honest scope, and it is the reason this enters at one key rather than two.** This is exact arithmetic in Python with written-ahead canaries; **nothing here is formalized, and nothing here is a theorem about cycles.** It is a statement about one proof route — that the Product-Bound chain, refined uniformly, cannot reach the window — and it excludes no cycle whatsoever. `α = 0.482–0.511` is a **measured** exponent over a finite range of `X₀`, not a proved one; the argument needs only `α > 1/3`, which the measurement supports comfortably, but the gap between measured and proved is real and is not papered over here. The Dirichlet half, by contrast, is unconditional and is the load-bearing half: `c* < 2` is fatal to the route on its own, independently of the race.
>
> **What it does for the note.** It is the analytic face of the one wall — paired with the staircase sharpness as the constructive face [L1, and Macindoe's round-11 proof of the all-`p` half]. Both say the same thing from opposite sides: refinement of the existing instruments does not reach, and the sharpness says the instruments cannot be made to reach. Neither excludes anything.
>
> Open for co-editing, and the wording of the grade line above is the part I would most like a second opinion on.

### 1.2 The offers-discharge block, verbatim (same commit)

> **Merle — round-11 offers discharged (2026-07-29).** Recorded here rather than in prose so the offers above do not read as open.
>
> - *(offer e — the two `q₂₁`.)* Discharged at [`7f20348`](https://github.com/ericmerle3789/one-obstruction-three-faces-lean) — line 188's subscripts corrected to `q₂₂`/`q₂₃`, line 186's `δ` given its REQ-054 factor 2, and the header's withdrawn `4.955e10` named as withdrawn rather than replaced in silence. Subscripts pinned in-file to the `q₀ = q₁ = 1` convention. Comments only; the file was recompiled after the edit under the hardened four-check protocol — 0 errors, 0 stack overflow or abort, 0 `sorryAx`, fifteen theorems in the axiom log, kernel-3 throughout.
> - *(offer f — Cor. 29's `X₀ ≥ 3·2⁶⁹`.)* Still not landed in Lean, and its home is here rather than there. Recorded in this ledger now: **Hercher's Corollary 29 requires `X₀ ≥ 3·2⁶⁹ = 1536·2⁶⁰`**, against his Theorem 23's `704·2⁶⁰` and this note's own instantiation at `2048·2⁶⁰ = 2⁷¹`. `704 < 1536 < 2048`: the asymmetry runs in Hercher's favour on hypothesis and on conclusion alike.
> - *(offer g — the deleted `(d-bis)` table.)* Discharged, and the diagnosis was exactly right. The committed `test_REQ-MATH-052` is byte-identical between `41fa4f8` — the commit whose OUT file carried the table — and HEAD, same blob, one commit in its whole history: it never produced that section, at any commit. A generator is now committed, `experiments/test_REQ-MATH-052bis_ostrowski_grille.py`, reproducing the ten rows, the four figures this ledger cites, and the eps-small column with median 15601, under four canaries written before the run. **One column it does not recover and says so in its own header:** the control sample `[2,1,1,1,2,1,2,1,1,306]`, median 1, is not reconstructible from the output and its generator was never committed. The control is therefore re-specified at a fixed seed and declared as re-specified, with a 200-draw control added — median 2, maximum 53, and **0 of 200 reaching 306** — which is a stronger instrument than the original ten but is not the original ten. The sentence in the seed block above should be read accordingly: the eps-small side is recovered, the control side is re-derived.
> - *(and one not offered, found while discharging the others.)* `test_REQ-MATH-067`, the source of the `0.00103` quoted in correspondence, computed the continued fraction of `log₂3` at `mp.dps = 400` and took 2000 partial quotients. At that precision the expansion **diverges from the true one at index 385**; 1615 of the 2000 terms were rounding noise. The correct value is **`0.00078`**. Macindoe's own three figures — largest bin deviation `0.008425`, his `χ²/N` over the complete partition `0.001214`, and `χ²/dof < 0.567` at every binning from 3 to 40 bins — reproduce exactly on the correct sequence and none on ours, where the maximum `χ²/dof` is `1.0504` and would have contradicted his bound. Fixed at `dps = 3000` with a canary that recomputes the whole sequence at double precision and refuses to proceed if one term moves. The substantive conclusion is unchanged and now rests on a correct sequence.

### 1.3 Operational definitions, from his two scripts (read, not run as verification)

`test_REQ-MATH-001_scissors_cstar.py` (dps 60):

- **The Product-Bound chain as he computes it:** `m ≤ (k^{c+1} + k)/3`
  ("papier Merle §5.2"), `m` the cycle minimum element, `k` the odd-element
  count (the script compares `k` against Hercher's `K`, which counts odd
  members — same axis, per the la8 adjudication).
- **`k_max(X₀, c)`** = the largest integer `k` with `(k^{c+1}+k)/3 < X₀`
  (bisection): the largest length the chain excludes at verification `X₀`.
- **Closing the window** = `k_max ≥ K_H = 1.375·10¹¹`, i.e.
  `(K_H^{c+1} + K_H)/3 = X₀`, solved as `c* = ln(3X₀ − K_H)/ln(K_H) − 1`.
- **Two `X₀` in-script:** `X0_paper = 2⁷¹` ("canaris calibres papier") and
  `X0_barina = 2075·2⁶⁰ = 2^71.019` ("la verification Barina exacte
  (§6.1)") — both c* variants printed.
- **Written-ahead canaries:** `k_max(c=6) = 1322`, `k_max(c=5.125) = 3693`
  (documented values from his paper §5.2).

`test_REQ-MATH-004_scissors_race.py` (dps 800, 160 partial quotients; the
in-file comment records that its own v1 at 90 quotients/dps 120 produced an
`α → 0` artifact above `2^300` — his own regime lesson, already applied):

- **`k_min(X₀)`** = `max_j (3/2)·min(q_j, 2X₀/(q_j + q_{j+1}))` over the
  convergent denominators of `log₂3` ("mecanisme Crandall + convergents,
  formule documentee papier Merle §6.1") — the Crandall jaw.
- **α** = the local slope `Δln k_min / Δln X₀` between consecutive grid
  points `2^71, 2^100, 2^150, 2^200, 2^300, 2^400`.
- Sanity: at `2⁷¹`, raw `k_min` vs Hercher's refined `1.375·10¹¹`.

Neither script was run as verification; every number was re-derived in
`merle_la9_check.py` from scratch (his `k_min` code was additionally
replicated once in the scratchpad to confirm that the entry's `9·10¹⁹` is
what his own procedure prints — it is, see §4).

### 1.4 Side item: the §12 NOTE.md claim — verified from the log, flat

Claim (round-12 letter §12): five commits touched `NOTE.md`, three his on
23–24 July, two ours on the 24th, net +2/−2 lines since the 19 July
skeleton, our §4 text verbatim at HEAD. From `git log --follow --numstat`
in the fresh clone:

- Commits since the skeleton `f496abe`: **five** — `61d2cf3` (Merle,
  2026-07-23), `430c00c` (macindoe, 07-24), `d2407b9` (macindoe, 07-24),
  `b8842bb` (Merle, 07-24), `6b9f2b1` (Merle, 07-24). Three his, two ours,
  dates as claimed. **MATCH.**
- `git diff f496abe..HEAD -- NOTE.md --numstat` = **+2/−2**. **MATCH.**
- Our §4 sentence (the realization-height pin with "positive odd integer")
  survives **verbatim** at HEAD inside his rewritten §4. **MATCH.**
- One flat calibration: the skeleton commit `f496abe` is dated 2026-07-18
  23:48:48 **+0200**; "the 19 July skeleton" is correct in the author's
  (Macindoe's) timezone, where that instant is 19 July morning. Not a
  discrepancy; recorded so nobody re-litigates the date.

## 2. The Barina adjudication (the literature lookup the brief granted)

**Question:** the entry says "the exact Barina bound `2075·2⁶⁰`" where our
la8 record and `cycles.md` 12.6.3 instantiate `2048·2⁶⁰ = 2⁷¹`. Which is
Barina's actual verified bound?

**Barina's citable, paper-stated threshold is `2⁷¹ = 2048·2⁶⁰`.**
Citation: D. Barina, *Improved verification limit for the convergence of
the Collatz conjecture*, The Journal of Supercomputing **81** (2025) — the
paper's result is verification of all `n < 2^71`; his project page
(`pcbarina.fit.vutbr.cz`) carries the matching log line "2025-01-15 the
convergence of all numbers below 2^71 is verified", and no later milestone.
This is exactly the pin `cycles.md` 12.6.3 carries and exactly what the
la8/T1 chain instantiates.

**`2075·2⁶⁰` appears nowhere in Barina's published record** — not in the
2025 paper, not in the project page's static text or log. What the project
page does carry is a progress counter denominated in `2⁶⁰` blocks (the
page's opening statement renders as "N × 2⁶⁰" with the N filled in by
script). `2075·2⁶⁰ = 2^71.019` is therefore consistent in form and
magnitude with a **snapshot of the live counter** taken after the 2^71
milestone — and his script sources it not from Barina but from his own
paper corpus ("`X0 = 2075 * 2^60 (Barina 2025, §6.1 table)`"). Whether the
counter ever displayed 2075 could not be verified this session (the value
is script-rendered and unarchived); recorded as unverifiable, not disputed.

**Verdict on the entry's parenthetical:** the *arithmetic* is right — both
`c*` values are correct under their own `X₀` (verified: 0.9617 at `2⁷¹`,
0.9622 at `2075·2⁶⁰`) — but the *label* "the exact Barina bound" is wrong
in the direction that matters for a ledger: `2075·2⁶⁰` is an unarchived,
moving, uncitable counter snapshot at best, and the citable, stable,
paper-stated bound is `2⁷¹`. Our la8 instantiation at `2048·2⁶⁰` is the
right one and needs no change. Co-edit offer drafted in §6 (h3).

## 3. The clean-room derivation of `c*`, written out

Derived before computing, importing nothing of his. Let `(x_i)` be a
positive cycle of the odd map `x → (3x+1)/2^{v_i}` with `k` odd elements,
`K = Σv_i`, `m = min x_i`, `L = log₂3`.

1. **Product identity.** Multiplying `3x_i + 1 = 2^{v_i}·x_{i+1}` around
   the cycle, the `x` products cancel: `∏(3x_i+1) = 2^K·∏x_i`, so
   `2^K/3^k = ∏(1 + 1/(3x_i))`.
2. **Bound by the minimum.** `∏(1 + 1/(3x_i)) ≤ (1 + 1/(3m))^k ≤
   e^{k/(3m)}`. Taking `ln`: `(K − kL)·ln2 ≤ k/(3m)`.
3. **Positivity.** For a genuine positive cycle `K − kL > 0` (the la8
   `ceiling_lower` fact), and `ε := K − kL = ‖kL‖` since `K` is the
   integer nearest above `kL`. So **`m ≤ k/(3·ln2·ε)`** — the sharp
   Product-Bound chain, with no room to improve the exponent (step 2 is
   tight to `O(1/m)`).
4. **Diophantine input.** An effective irrationality measure in the
   standard convention `|L − p/q| > κ/q^μ` gives `ε = k·|L − K/k| >
   κ/k^{μ−1}` (a reduced denominator only helps). Hence
   **`m < k^μ/(3κ·ln2)`** and `k_max(X₀) = (3κ·ln2·X₀)^{1/μ}`.
5. **Closing the current window** (`k_max ≥ K_H`) therefore requires
   `μ ≤ μ* = ln(3κ·ln2·X₀)/ln(K_H)`. Computed (script, two precisions):
   **`μ* = 1.9617`** at `κ = 1/ln2`, **`1.9474`** at `κ = 1`,
   **`1.9161`** at the Hurwitz constant `κ = 1/√5`.
6. **The floor.** Dirichlet: every irrational has infinitely many
   `|ξ − p/q| < 1/q²`, so no effective bound with `μ < 2` exists for any
   `ξ` and any `κ`; and at `μ = 2` exactly, Hurwitz caps the constant at
   `κ ≤ 1/√5` (attained only by badly approximable numbers, which `log₂3`
   is conjecturally not). Since `μ* < 2` in every constant convention,
   **the route is shut for every constant — confirmed.** Even granting the
   unattainable best case (`μ = 2`, `κ = 1/√5`), the current window stays
   open by a factor **2.93** on `k` (`k_max = 4.69·10¹⁰` vs `1.375·10¹¹`),
   i.e. `2^3.11` of missing verification.

**Where his numbers sit in this.** His chain `m ≤ (k^{c+1}+k)/3` is
*exactly* the sharp chain of step 3 — verified numerically to the `+k`
term — under the input `K·ln2 − k·ln3 > k^{−c}`: his **`c` is the
linear-form exponent, one below the measure** (`μ = c + 1`, constant
`κ = 1/ln2`). His `c* = 0.9617` is therefore correct arithmetic (we
reproduce 0.961722 and 0.962232 exactly, and `c* + 1 = μ*` at his κ to
four digits), and the chain itself wastes nothing. What the convention
does affect is the two *comparisons* the entry builds on it (§4).

## 4. The Dirichlet half — the attack he asked for, and the verdict

### 4.1 The logical direction — CONFIRMED

As the entry uses it, the argument is: closing needs exponent `c*`; no
irrational admits an effective exponent that good; hence no improvement in
effective constants — for `log₂3` or any other number — closes the route.
Modus tollens, valid, and genuinely unconditional given (i) the chain
reduction (§3, sharp, verified) and (ii) Dirichlet's theorem. The
current-window impossibility statement is **theorem-grade**: it needs no
measurement, no `α`, no computation beyond arithmetic. This half deserves
the second key — *after* one repair, below.

### 4.2 The defect: the floor and the exponent live in different conventions

The grade line pairs **`c* ≈ 0.9617`** (computed in the linear-form
convention, where Dirichlet's floor is `c ≥ 1`) with **"no irrational has
an effective exponent below 2"** (the measure convention, where the same
floor is `μ ≥ 2`). Each sentence is right in its own convention; put in
one sentence they overstate the margin by exactly the one power of `k`
that separates the conventions:

| convention | required to close | Dirichlet floor | margin |
|---|---|---|---|
| linear form (`ε > κ/k^c`, his `c`) | `c* = 0.9617` | `c ≥ 1` | **0.038** |
| measure (`\|L − p/q\| > κ/q^μ`) | `μ* = 1.92–1.96` | `μ ≥ 2` | **0.04–0.08** |
| the entry's pairing | `0.9617` | `2` | reads as ~1.04 |

The same mix produces the entry's "for scale" figures. "At the diophantine
dream `c = 2` — conjectured for `log₂3`, true for almost every real" is a
description of the **measure** exponent `μ = 2`; instantiated in his
chain's `c`-slot it becomes `μ = 3`, and the deficits computed there
(7159.5 on `k`, `2^38.4` of computation, and "Salikhov's `c = 5.125`" →
`k^{6.125}`) are all one power of `k` more favourable to the impossibility
than the dream they name. At the true dream the deficits are:

- `μ = 2, κ = 1`: `k_max = 7.01·10¹⁰`, missing factor **1.96** on `k`;
  closing needs `X₀ = 2^72.95` — **missing `2^1.95`**, i.e. two doublings
  of verification, not `2^38.4`.
- `μ = 2, κ = 1/√5` (the best any irrational admits): missing **2.93** on
  `k`, `X₀ = 2^74.11`, missing `2^3.11`.

(Both directions stated plainly: the convention mix is *conservative* for
the impossibility conclusion — the route is shut in every convention — but
the entry's stated margin, and its picture of the dream, are not what the
numbers say. The razor is real: the route dies by 2–8% in the exponent,
or a factor 2–3 on `k` at the unattainable floor, not by the distance
from 0.96 to 2. Note also `2^38.4` is not even the `μ = 3` *dream* — no
conjecture puts `μ(log₂3)` at 3; the sentence names a regime nothing
lives in.)

Two smaller notes on the same half:

- "Salikhov's real `c = 5.125`": `5.125` is Salikhov 2007's measure of
  **`ln 3`**, not of `log₂3` — the transplant our la7-mu check adjudicated
  (`briefs/merle-la7-mu-check-findings.md` §2.3; for `log₂3` the citable
  effective input is Rhin 1987's linear-form exponent 13.3, i.e.
  `μ_eff = 14.3`). Doubly displaced here (wrong number, and measure-vs-
  linear-form slot); immaterial to the conclusion, since every published
  effective exponent is far above `μ*` anyway.
- The Dirichlet floor sentence itself ("no irrational has an effective
  exponent below 2") is exactly right in the measure convention, and the
  strengthening "for every constant, not merely `log₂3`" survives even at
  `μ = 2` via Hurwitz — the entry does not use Hurwitz and does not need
  it for `μ < 2`, but the `μ = 2` boundary case does need it, and with it
  the current-window impossibility is complete over *all* `(κ, μ)`.

### 4.3 Is the reduction "closing ⟺ exponent `c*`" exact?

Yes, with two model boundaries, both of which the entry itself already
respects: (i) it quantifies over **uniform** refinements only — inputs of
the form `ε > κ/k^{−c}` at the single point `k` — which is what "refined
uniformly" says; routes that consume the actual convergent structure
(Crandall, Hercher) are outside it, which is exactly why the scissors
half exists. (ii) The `+k` term and the `e^{k/(3m)}` step cost nothing at
these scales (verified: relative effect `< 10^{−4}` on every reported
figure). No hidden slack; the reduction is exact.

### 4.4 The scissors half, attacked in a second regime chosen against it

All figures replicate on his grid (raw Crandall `3.49·10¹⁰`, factor 3.94,
ratios 1816.94 and `9.10·10¹⁹`, α-slopes 0.489/0.482/0.511/0.508/0.505).
Then the controls:

- **Extension `2^400 → 2^2000`** (50-bit steps): local α in
  **[0.449, 0.553]**; full chord over `[2^71, 2^2000]` = **0.5001**. The
  claim `α > 1/3` survives the extended regime comfortably.
- **Width-dependence** (sliding windows at every 1-bit start): at 1-bit
  width the local slope hits 0 and 1 (plateaus and catch-ups — "α" is a
  property of the sampling grid); at **30-bit width the minimum is 0.3229
  — below 1/3** (3 of 1900 windows, the deserts around the large partial
  quotients; his narrowest grid gap is 29 bits, so his 0.482 owes
  something to window placement); at 100-bit width min 0.4434; at 200-bit
  width min 0.4681, and `α > 1/3` holds at every placement up to
  `2^2000`. So the measured claim is safe **at the widths his grid
  actually uses and above**, and the honest scope is "chord slopes at
  width ≥ ~100 bits", not a bare exponent.
- **`α > 1/3` is the right threshold only in his convention.** Against
  the true Dirichlet floor the forever-form of the claim ("the window
  widens as verification advances, for every constant") needs
  **`α > 1/2`** — and the measurement *straddles* 1/2: his own band
  0.482–0.511 contains it, our 400-bit minimum is 0.4867, and the full
  chord is 0.5001. The measurement cannot decide the race at the floor.
  What it does decide: the window widens for every effective exponent
  `μ > 1/0.4867 ≈ 2.05` — hence for every published effective input
  (best today: `μ_eff = 14.3`), and for anything remotely reachable.
- **Negative control, golden ratio** (the most chain-favourable
  irrational in existence): at `μ = 2, κ = 1/√5` the ratio
  `k_min/k_max` sits in the fixed band **[1.08, 1.35]** across
  `2^100..2^400` — a photo finish decided by constants, no widening —
  while the entry's `c = 2` race grows by 17 orders over the same span.
  "Widens forever" is a property of `μ > 2`, not of the route.
- **Negative control, Liouville-flavoured constant**: min rung slope
  0.0000 — the instrument does report `α < 1/3` when the quotients
  explode, so `log₂3`'s `α > 1/3` is informative, not built in.
- **Calibration, not a defect:** proving `α > 1/3` asymptotically is a
  `q_{j+1} = O(q_j²)`-type statement — essentially `μ(log₂3) ≤ 3` — far
  beyond any published bound (`14.3`). The entry's "measured, not
  proved" is right; the calibration adds that it is not *provable* with
  current technology either, which strengthens the case for leaving the
  scissors half at the measured grade permanently rather than "pending".

### 4.5 Verdict on the two halves

- **Dirichlet half:** conclusion CONFIRMED, unconditional, theorem-grade
  — *as restated in a single convention* (offer h1). As written, the
  grade line's margin comparison (`0.9617` vs `2`) does not survive the
  attack he asked for.
- **Scissors half:** every number replicates; the honest scope is
  narrower than the entry's in one direction (α is width-dependent and
  the 1/3 threshold is convention-bound) and wider in another (the claim
  extends to `2^2000` and the full chord is 0.5001). Measured-not-proved
  is the right permanent grade.

## 5. The offers-discharge block, item by item

### 5.1 Offer e (`7f20348`) — VERIFIED at line level, comments only

Read directly at `7f20348` in the fresh Lean clone
(`git show 7f20348:OneObstruction/T1Structure.lean`), and the whole diff
`c991430 → 7f20348` inspected:

- **Header:** now reads "Legendre window 3.5035491e10 (exact; integral
  form 3.503177115e10 — the earlier 4.955e10 was **withdrawn** at
  REQ-MATH-054)". The withdrawn figure is named as withdrawn. ✓
- **The `δ` line:** `‖n·log₂3‖ ≤ 2n/(3X·ln2)` — the REQ-054 factor 2 is
  present. ✓
- **The subscripts:** "`n ≥ q₂₂ = 6.547·10¹⁰` … one convergent step below
  Hercher's underlying `q₂₃ = 1.375·10¹¹`", with the convention pinned
  in-file ("Indexing pinned to `q₀ = q₁ = 1` both counted (OUT-054/056):
  `q₂₁ = 6586818670`, `q₂₂ = 65470613321`, `q₂₃ = 137528045312`") and the
  correction dated and attributed. ✓
- **The already-correct `q₂₁`** in the discharge docstring (old line 433,
  now 438) is untouched and now consistent with the repaired lines. ✓
- **Comments only:** the `7f20348` diff to `T1Structure.lean` touches
  docstring/header text exclusively; every theorem statement, proof and
  discharge numeral is character-identical. ✓ No drift in the file at any
  later commit up to HEAD `d48ba9e`. ✓
- **Trust boundary, stated:** the "recompiled under the hardened
  four-check protocol" claim is **read-not-built** — no Lean toolchain our
  side — and it left no committed artifact of its own: the axiom log
  `T1Structure_axioms.txt` is unchanged at `7f20348` (consistent with a
  comments-only edit, but the recompile claim rests on his commit message
  and letter, not on anything checkable here). The log itself carries the
  fifteen entries with `discharge_all → [propext]` and `convPairs_length`
  axiom-free, unchanged from the round-11 audit's record. ✓
- The shared-repo hash correction `7c05458` ("fixed at 7f20348, not
  4f4bb2e") is **right**: `4f4bb2e` touches only the REQ-067 files. ✓

### 5.2 Offer f — the ledger wording vs our records: NO DRIFT

The discharge sentence ("Hercher's Corollary 29 requires `X₀ ≥ 3·2⁶⁹ =
1536·2⁶⁰`, against his Theorem 23's `704·2⁶⁰` and this note's own
instantiation at `2048·2⁶⁰ = 2⁷¹`; `704 < 1536 < 2048`: the asymmetry runs
in Hercher's favour on hypothesis and on conclusion alike") was checked
word against word with `briefs/merle-la8-t1-check-findings.md` (the
Hercher adjudication: Cor. 29 verbatim, the `1536·2⁶⁰ = 3·2⁶⁹` identity,
Barina meeting it) and `briefs/jointnote-premise-external-findings.md`
(the three-row `704/1536/2048` table; the Thm-23-at-`704·2⁶⁰` attribution
via Hercher's Definition 4). Every number, every attribution and the
direction of the asymmetry match both records. The la8 record quotes
"Corollary 24, Table 1" at `X₀ = 704·2⁶⁰` and the external-premise
findings attribute `704·2⁶⁰` to Theorem 23 via Definition 4 — both true of
the same `X₀`, no conflict. The exact-vs-integral window distinction
(`3.5035`/`3.5032`, la8 item (d)) is not implicated by this sentence.
**Flag: none.**

### 5.3 Offer g (052bis at `7f20348`) — reproduction AND reimplementation

**Reproduction (his artifact, run as-is from the clone):** output
**byte-identical** to the committed `OUT_REQ-MATH-052bis.txt`; all four
written-ahead canaries PASS; the ten rows, the four ledger figures
(`14936 = [(665,22),(306,1)]`, `15601`, `31202`, `46803`), the eps-small
column `[306, 15601, 15601, 306, 15601, 15601, 306, 79335, 306, 15601]`
with median 15601; the control re-specification is declared in the file's
own header (original `[2,1,1,1,2,1,2,1,1,306]` not reconstructible,
generator never committed, three candidate definitions failed); the
200-draw control prints median 2, max 53, 0/200 reaching 306 — exactly as
the ledger discharge states. The ledger's reading instruction ("the
eps-small side is recovered, the control side is re-derived") is accurate.

**Reimplementation (ours, the verification):** `merle_la9_check.py` part 5
recomputes everything from scratch — the eps-small `n` from an exact
fixed-point test at two scales, the greedy expansion over independently
derived convergent denominators — and confirms the four ledger rows, the
column, the median, and that every eps-small `n < 200000` has smallest
denominator ≥ 306.

**One calibration finding, offered kindly (h5): the `0/200` is
seed-typical but not seed-robust.** The seed-free census over *all*
`n < 200000`: **897 of 199,999 (0.4485%)** have smallest denominator
≥ 306, so `P(0 in 200 draws) = 0.407` — his seed-1 draw of 0/200 was a
fair coin-flip outcome, and our own 200 draws at a different seed hit
1/200. Nothing qualitative moves (population median 2 against the
eps-small 15601 is unambiguous), but the census line is strictly stronger
than any control draw and costs nothing; drafted as a wording offer.

### 5.4 REQ-067 (`4f4bb2e`) — the volunteered defect: VERIFIED in full

Independent computation (fresh code; his 067 script read for conventions
only): the true CF prefix built by exact-integer Euclid on fixed-point
`ln3/ln2` at two precisions (3319 stable terms); the fragile
floor/reciprocal float loop reimplemented at `dps = 400`.

- **Divergence index 385** (0-based, `a₀` counted), i.e. **1615 of 2000
  terms are noise** — exactly his claim. ✓
- **`0.00078`** on the correct sequence under his P3 definition (eight
  head classes summed, `k ≥ 9` computed and not added): 0.000775. ✓ And
  **`0.00103`** reproduces on the wrong sequence (0.001034) from our own
  reimplementation of the fragile loop — the defect and the fix both
  replicate. ✓
- **The six-number table**, under the confirmed convention (classes
  `{1},…,{B−1},{≥B}`, `dof = B−1` — our `merle_r11_hygiene_check.py`
  `gk_stats` convention, as the main session confirmed): correct sequence
  `0.008425 / 0.001214 / 0.5666`; wrong sequence
  `0.004496 / 0.001249 / 1.0504`. All six to the digit. ✓
- **His convention-sensitivity numbers too:** at `dof = B` the maxima
  become `0.5524 / 1.0204`, and at `dof = B−2` the correct sequence
  reaches `1.0793` — reproduced, confirming his point that the row is
  reproducible under exactly one convention. ✓
- **The stronger form of our own bound HOLDS:** our committed run tried
  13 binnings and printed `< 0.567`; his exhaustive maximum over all 38
  binnings `B ∈ [3, 40]` is **0.56657 < 0.567**. His exhaustive form is
  the stronger statement and it is true. ✓
- The `4f4bb2e` fix itself read in the clone: `dps = 3000`, the C0 canary
  (recompute at doubled precision, refuse if one term moves) present and
  written before the statistics; the printed label now names the
  truncation, the unsummed class and its 0.152 mass. ✓

## 6. The grade-line adjudication, and the drafted offers

### 6.1 What the check established

The entry's arithmetic is flawless — every figure replicates to the digit,
including the two he flagged as approximate. The impossibility conclusion
is **confirmed and strengthened** (it survives the sharp chain, every
constant convention, the Hurwitz boundary case, and the φ-transplant
control). What does not survive is the grade line's *margin*: `0.9617`
belongs to the linear-form convention, the floor `2` to the measure
convention, and in any single convention the route is shut by 0.04–0.08 in
the exponent — a razor, not a chasm. The scissors half replicates
entirely, is honestly labelled measured, and gains from the second regime
(chord 0.5001 to `2^2000`) while losing its width-independence (30-bit
windows dip below 1/3) and its 1/3 threshold (which is convention-bound;
the floor race needs 1/2, undecided by measurement).

### 6.2 The three options weighed

- **(a) Entry as-is, our key turned scoped.** Rejected: the sentence he
  asked us to attack hardest is the one that fails — turning a key on the
  entry while its headline margin mixes conventions would be exactly the
  regime-blind agreement his §4(d) column exists to prevent.
- **(b) Split grade inside one entry.** Right shape, and the natural
  reading of his own scope paragraph: the Dirichlet half (current-window
  impossibility) is two-keyable as unconditional *once restated in a
  single convention*; the scissors half stays at measured grade
  permanently (see §4.4 — proved-`α` is `μ(log₂3) ≤ 3`-hard, so "pending
  proof" would be dishonest).
- **(c) Defect found → turn-with-offer.** This is (b) with the standing
  pattern's mechanics, and it is the recommendation.

### 6.3 Recommendation (no key turned here)

**Turn-with-offer, split grade.** The Macindoe key can turn on the
Dirichlet half — the claim, the chain reduction, and the floor argument,
which this session verified clean-room — conditional on offer h1 below
(the single-convention restatement). The scissors half is confirmed as
measured and should carry the width scope (h4). The key turn itself is the
main session's and the push is gated on the author, per the brief.

### 6.4 Drafted co-edit offers (wording only; his prose untouched)

- *(h1 — the grade-line repair, the load-bearing one.)* Restate the
  headline in one convention, both flavours available: "To close the
  current window the chain needs a linear-form bound `K·ln2 − k·ln3 >
  k^{−c}` with `c* ≈ 0.9617` — equivalently an irrationality measure
  `μ* = c* + 1 ≈ 1.96` (`1.92` even at the Hurwitz constant). Dirichlet's
  floor is `c ≥ 1` (`μ ≥ 2`): the route is shut for every constant, by a
  margin of a few hundredths in the exponent. At the floor itself
  (`μ = 2`, `κ = 1/√5`, attainable by no number with unbounded partial
  quotients) the window would still stay open today by a factor 2.9 on
  `k`." This keeps his conclusion word for word and replaces only the
  0.9617-vs-2 pairing.
- *(h2 — the dream deficits relabelled.)* Either name the regime the
  7159.5 / `2^38.4` / 37-million figures live in (chain exponent
  `c = 2`, i.e. measure `μ = 3` — which nothing conjectures for `log₂3`)
  or add the true-dream row: at `μ = 2`, `κ = 1`, the deficit is a factor
  1.96 on `k` and `2^1.95` of computation (`2^72.95` closes), `2.93` and
  `2^3.11` at the Hurwitz constant. The second option is the honest
  razor and, we would argue, the *stronger* sentence: the route dies by
  Dirichlet's strict inequality alone, not by a wide numeric gap.
- *(h3 — the Barina label.)* "`0.9622` with the exact Barina bound
  `2075·2⁶⁰`" → "`0.9622` at the project counter's `2075·2⁶⁰` (unarchived
  snapshot; the paper-stated, citable bound is `2⁷¹` — D. Barina,
  J. Supercomputing 81 (2025))". Both `c*` values are right under their
  own `X₀`; only the provenance label moves.
- *(h4 — the α scope.)* Pin the measured range to its grid: "chord
  slopes over the grid `2^71..2^400`; extended chord 0.5001 to `2^2000`;
  at window widths below ~100 bits local slopes leave the band (min
  0.32 at 30 bits) — the claim is about widths ≥ 100 bits". And tie the
  forever-clause to its true threshold: "the window widens for every
  effective exponent `μ > ~2.05`; at the Dirichlet floor itself the race
  is a photo finish the measurement cannot decide (`α` straddles 1/2)".
  This also corrects "the argument needs only `α > 1/3`", which is true
  only against the `μ ≥ 3` jaw of the entry's convention.
- *(h5 — the 052bis census line.)* Offer the seed-free replacement for
  the control sentence: "among all 199,999 `n < 200000`, 897 (0.45%)
  have smallest Ostrowski denominator ≥ 306; all ten eps-small `n` do
  (median 15601 against a population median of 2)". One line, strictly
  stronger than any drawn control, and it retires the seed question.

### 6.5 What could not be established, with reasons

- Whether Barina's live counter ever displayed `2075·2⁶⁰` — the value is
  script-rendered on his page and unarchived; recorded as unverifiable,
  not disputed (§2).
- His `7f20348` recompile of `T1Structure.lean` — read-not-built, no Lean
  toolchain our side, and the edit left the axiom log unchanged so there
  is no committed artifact to check (§5.1; trust boundary stated).
- His own 2026-07-29 re-run of the two scissors scripts — not witnessed;
  immaterial, since every figure was re-derived here in fresh code and
  his `k_min` procedure was additionally replicated once in the
  scratchpad to confirm the entry's `9·10¹⁹` is what it prints.

## 7. Flags, collected (all flat, none disputed in prose)

1. The grade line's `0.9617`-vs-`2` pairing mixes the linear-form and
   measure conventions; margin in any single convention is 0.04–0.08
   (§4.2; offer h1). The conclusion itself is confirmed.
2. "At the diophantine dream `c = 2` — conjectured for `log₂3`, true for
   almost every real": the clause describes `μ = 2`; the figures beside
   it are computed at `μ = 3` (§4.2; offer h2).
3. "Salikhov's real `c = 5.125`": Salikhov's exponent is a measure of
   `ln 3`, transplanted here into the linear-form slot — doubly displaced,
   immaterial to the conclusion (§4.2; la7-mu §2.3 is the standing
   record).
4. "The exact Barina bound `2075·2⁶⁰`": mislabelled provenance; citable
   bound is `2⁷¹` (§2; offer h3).
5. `α = 0.482–0.511` is grid-dependent (30-bit windows dip to 0.32;
   50-bit extension spans 0.449–0.553); "needs only `α > 1/3`" is
   convention-bound, the floor race needs `α > 1/2`, undecided (§4.4;
   offer h4).
6. The 052bis `0/200` control summary is seed-typical, not seed-robust
   (census: 0.4485%, `P(0/200) = 0.407`; our seed drew 1/200) (§5.3;
   offer h5).
7. The `7f20348` recompile claim has no committed artifact (log unchanged
   — consistent with comments-only, stated as trust boundary) (§5.1).
8. Flat, for completeness: the raw-Crandall `3.49·10¹⁰` and the la8 exact
   Legendre window `3.5035·10¹⁰` are numerically close and unrelated
   objects (a jaw at `2⁷¹` vs a Legendre validity bound); worth one
   clause somewhere if both ever appear in one paragraph, recorded here
   so nobody conflates them.

