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
