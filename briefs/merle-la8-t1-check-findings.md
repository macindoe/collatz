# Findings: L-A8 / T1 verify (merle-la8-t1-check)

Delegated session, 2026-07-26. Brief: `briefs/merle-la8-t1-check-brief.md`.
Branch `merle-la8-t1-check`, base commit `2374bfe` (the brief commit; the
worktree HEAD `b860fe8` predated the brief and was fast-forwarded to `2374bfe`
before branching, so the base contains the brief as the rules require).
Register: findings only; discrepancies recorded flat with correct values
computed, never disputed in prose; no key is turned; no reply paragraphs.
Verification code: `experiments/merle_la8_t1_check.py` (fresh code, pure
Python stdlib, imports nothing from any Merle repository and nothing from
prior Merle-check scripts; fixed-point big-integer logarithms built in-house
from the atanh series at TWO working precisions, 130 and 210 digits — both
above the brief's 80 — with stability asserted between them, so no float and
no external library touches any pass/fail decision; exact integer arithmetic
at every decision that can be integer; canaries — the four real cycles —
printed first). Output committed as `experiments/merle_la8_t1_check_output.txt`.
**62 recorded checks, 0 failures. Handbacks: two labeling/figure pins (below),
both with correct values computed; no mathematical error found in any link.**
Stopping-rule compliance: this verifies a correspondent's finite discharge —
a 22-item integer check — and opens no orbit or period search; the synthetic
sweeps are element multisets, not orbits; the cycles front stays PARKED.

## Item 1 — the repos, read-only

Fresh unauthenticated clones into the scratchpad (2026-07-26), no writes:

- Shared repo `github.com/macindoe/one-obstruction-three-faces`: **HEAD
  `826970e723d52f0eb5f562ebc0113ed81aa083af` (`826970e`) — exactly the brief's
  expected pin.** The L-A8 entry entered in six commits, all Eric MERLE,
  2026-07-25 (17:24:51 through 18:45:28 +0200): `be8869f` (seed, ceiling
  half), `0905b00` (grid half launched, seam_bound), `9428663` (March 1,
  Legendre window closed at script level), `a37743f` (March 1-bis, analytic
  bridge), `5773bd0` (Legendre step + the `da2c8db` retraction recorded),
  `826970e` (finite discharge).
- Lean repo `ericmerle3789/one-obstruction-three-faces-lean`: **HEAD
  `5c9b66392a157ce63c34f765e18e05723d870ddf` (`5c9b663`) — the expected pin.**
  Read for operational definitions ONLY (`experiments/OUT_REQ-MATH-052..056`
  and the committed scripts `test_REQ-MATH-052..054`); nothing was run, and
  the Lean statement-match is the sibling session `merle-lean-r10-audit`, not
  claimed here.

### The six L-A8 blocks, verbatim (LEDGER.md at `826970e`, lines 265–327)

> ## L-A8 — T1, the no-hair theorem for cycles: the ceiling half at the kernel (Merle, correspondence 2026-07-25)
>
> **DRAFT — one key (Merle: Lean kernel + scripts); Macindoe key invited.**
>
> T1 is the structure theorem the joint note's §6 names as the program's next step: *every surviving positive cycle is forced into a rigid shape* — no freedom, like a black hole's no-hair theorem. Its **ceiling half is now a kernel theorem**, stated in pure integers with no logarithm:
>
> > `ceiling_upper` : a positive cycle with `p+1` odd elements, all `≥ X`, with `2(p+1) < 3X`, has `3^(p+1) < 2^K < 2·3^(p+1)` — i.e. `K = ⌈(p+1)·log₂3⌉` is forced.
>
> Chain: the **cycle product identity** `∏(3xᵢ+1) = 2^K·∏xᵢ` (telescoping over the rotation, `Fintype.prod_equiv`); the **survivor bound** `2^K(3X)^{p+1} ≤ 3^{p+1}(3X+1)^{p+1}` (per-factor `(3x+1)(3X) ≤ 3x(3X+1) ⟺ X ≤ x`); and the elementary strict two-bound `(m+1)^n < 2m^n` for `2n < m` (induction, no analysis). [`OneObstruction/T1Structure.lean`](…/41fa4f8/OneObstruction/T1Structure.lean), **kernel-3, 0 sorry, no user axioms, no `native_decide`**, committed axiom log; canaries instantiate the theorems on the trivial cycle.
>
> Machine chain first (REQ-MATH-052, committed): the product identity holds **exactly on all four real cycles, both shores** (`−17`: `∏(3x+1) = −403123745024000 = 2^11·∏x`); the Legendre window is `4.955·10^10` (below Hercher's `1.375·10^11`, so the surviving range is governed by the Ostrowski regime, not Legendre — stated honestly); and the **grid half** is script-verified: the Ostrowski expansion of every `ε`-small `n` uses **only large convergent denominators** (median lowest denominator 15601, against 1 for controls; e.g. `14936 = 22·665 + 306`, the coefficient 22 being the partial quotient 23 − 1). The grid half — `n` forced onto the convergent sub-grid — is measured and stated, **not yet proved**; it is the remaining half of T1.
>
> **Honest scope:** the ceiling half needs only `x_min > 2(p+1)/3` — far weaker than verification bounds — and pins `K` for every surviving scale. It does not by itself exclude anything; it removes one degree of freedom (K) of the two (K, shape), which is exactly what a no-hair theorem does. Open for co-editing.
>
> **Merle — the grid half, launched to proof (2026-07-25, stack `81054ea`).** The quantitative core of the second half is now also a kernel theorem:
>
> > `seam_bound` : under the same cycle hypotheses with `2p < 3X`: `2^K·3X < 3^(p+1)·(3X + 2(p+1))` — reading: `q·3X < 2(p+1)·3^(p+1)`, the seam gap squeezed inversely to the minimum element.
>
> Chain: `survivor_bound` + `succ_pow_le_pow_add` (difference of powers in multiplied form, no natural subtraction) + the strict two-bound. **Five T1 theorems, all kernel-3, 0 `sorry`, no `native_decide`**, committed axiom log; both compiles first-try. Consequences computed exactly (REQ-MATH-053): best approximation verified **exhaustively** to `q₁₀ = 190537` (for every `j`, `min_{n<q_{j+1}} ‖nL‖ = θ_j`, attained at `q_j`); for `X ≥ 2⁷¹` the first admissible scale is **`n ≥ q₂₁ = 6.547·10¹⁰`** — one convergent step below Hercher's dedicated `q₂₂ = 1.375·10¹¹`, which is *itself a convergent denominator*, exactly as this frame predicts. What remains for the grid half: formalizing the best-approximation step (standard number theory, nontrivial in Lean) — the Ostrowski confinement is measured (`ε`-small `n` use only large denominators) and stated, not yet kernel-proved.
>
> **Merle — March 1: T1 closed in the Legendre window (2026-07-25, stack `89d9efc`).** The grid half now has a fully verified consequence, and one more kernel theorem.
>
> **Verified exactly (REQ-MATH-054):** from `seam_bound`, a positive cycle with `x_min ≥ 2⁷¹` forces `‖n·log₂3‖ < n·δ` with `δ = 2/(3·2⁷¹·ln 2) = 4.0734·10⁻²²`. Legendre's criterion applies whenever `n ≤ √(1/2δ) = 3.5035·10¹⁰`, and then `K/n` must be a **convergent** of `log₂3` — so `n` is one of the 22 convergent denominators below that window. **All 22 fail the constraint** (the tightest, `q₂₁ = 6.587·10⁹`, by a factor 5.4). Hence: **no positive cycle with `x_min ≥ 2⁷¹` and length `n ≤ 3.5035·10¹⁰`.** For comparison, Hercher's dedicated paper bound is `1.375·10¹¹` — 3.9× further, but on paper; this chain is designed to be machine-checked end to end.
>
> **Kernel added:** `seam_gap_at_barina` — the integer half, stated subtraction-free (`2^K·3X < 3^(p+1)·3X + 3^(p+1)·2(p+1)` at `X = 2⁷¹`), with a canary showing it is not vacuous about the trivial cycle. **Six T1 theorems, all kernel-3, 0 `sorry`, no `native_decide`**, both files compiled first try, committed axiom log.
>
> **Honest scope and the remaining link.** The analytic half — the real bridge `q ≥ 3ⁿ·ε·ln 2`, Legendre, and the 22-point check — is exactly verified but **not formalized**. Its entry point is identified and clean: `LegendreApprox.abs_sub_ge_of_not_convergent` (Legendre contrapositive wrapping Mathlib's criterion, **0 sorry, 0 axioms, 0 native_decide**) in the Merle Junction repository. A correction recorded rather than smoothed: the previous entry's `δ` dropped a factor 2, which moved the window from `4.955·10¹⁰` to `3.5035·10¹⁰`; the earlier figure is withdrawn.
>
> **Merle — March 1-bis: the analytic bridge is now kernel too (2026-07-25, stack `dac39a3`).** The step from the integer seam gap to Legendre's input needed no continued fractions after all — only `Real.log_le_sub_one_of_pos` from Mathlib:
>
> > `ratio_bound_at_barina` : `1 < 2^K/3^(p+1) < 1 + 2(p+1)/(3·2⁷¹)` (cast of the integer gap)
> > `log_gap_at_barina` : `0 < K·log 2 − (p+1)·log 3 < 2(p+1)/(3·2⁷¹)`
>
> Dividing the second by `(p+1)·log 2` is exactly `|log₂3 − K/(p+1)| < δ`, `δ = 2/(3·2⁷¹·ln 2)` — the input of Legendre's criterion. **Eight T1 theorems, every one kernel-3, 0 `sorry`, no `native_decide`, no user axioms**, committed axiom log; every compile first-try but one trivial cast.
>
> **What is now left for a fully machine-checked closure of the Legendre window** is exactly two named steps: invoke Legendre's criterion (entry point `LegendreApprox.abs_sub_ge_of_not_convergent`, clean, already in the Merle Junction repository, wrapping Mathlib) and discharge the 22-point convergent check (REQ-MATH-054: all 22 fail, tightest by a factor 5.4). The mathematics is verified; what remains is formalization, not discovery.
>
> **Merle — the Legendre step proved, and a retraction recorded (2026-07-25, stack `4856058`).**
>
> *First, the retraction.* An earlier commit (`da2c8db`) claimed this step was kernel-3. **That claim was false.** `lake env lean` printed no `error:` line but had aborted with a stack overflow, and at workable recursion depths the proof carried `sorryAx`; I read "0 errors" without checking the compiler had finished. It is withdrawn in the artifact with a `RETRACTED` note stating what was claimed and why it failed. The verification protocol is now hardened: every check tests for `error:` **and** stack overflow/abort **and** `sorryAx` **and** presence in the theorem's own `#print axioms` probe.
>
> *Then, the proof.* The obstruction was elaboration blow-up on the literal `2⁷¹`, not mathematics. Abstracting the threshold fixes it:
>
> > `quotient_is_convergent_gen` : a positive cycle above threshold `X`, of length `n = p+1` with `4000·n² ≤ 2079·X`, has `K/n` a **convergent** of `log₂3`.
>
> `X` is a variable, so no numeral reaches a tactic; the final nonlinear step is supplied explicitly rather than left to `nlinarith`. The chain is now complete and general: `cycle_prod_identity → survivor_bound → seam_bound → log_gap_gen → quotient_is_convergent_gen`, plus `ceiling_upper`. **Eleven theorems, all kernel-3, 0 `sorry`, no `native_decide`, no user axioms**, each verified by its own probe; `LegendreApprox` (from the Merle Junction repository) compiles unchanged.
>
> Instantiating `X := 2⁷¹` gives the Barina window `n ≤ 3.5032·10¹⁰`. What remains for the full closure is only the finite discharge: the 22 convergent denominators inside that window, all of which fail the seam constraint (REQ-MATH-054/055, tightest by a factor 5.4).
>
> **Merle — T1's finite discharge proved; the window closes (2026-07-25, stack `5c9b663`).**
>
> > `discharge_all` : every convergent denominator of `log₂3` in the Barina window satisfies `2000·q·(q+q′) ≤ 2079·2⁷¹`, hence fails the seam criterion.
>
> Kernel `decide`, axioms **`[propext]` only**; `convPairs_length = 22` uses **no axioms at all**. The trick that made it cheap: instead of computing `θ_j` to twenty-odd digits, use the classical convergent bound `θ_j > 1/(q_j + q_{j+1})`, which turns the whole check into one **integer** inequality per convergent — no logarithm anywhere. Verified first (REQ-MATH-056): all 22 pass, tightest margin **5.17×** at `q = 6586818670` (the exact test gives 5.44×, so the integer form is conservative by design), with a non-vacuity canary showing the criterion **fails** at the next convergent — which is precisely why the window ends where it does.
>
> **T1's status, stated exactly.** Kernel-proved: the ceiling (`K` pinned), the whole seam chain, the logarithmic gap, the Legendre step (`n` must be a convergent denominator), and the finite discharge (each listed denominator fails). **Thirteen theorems, 0 `sorry`, no `native_decide`, no user axioms**, all four verification checks clean. The remaining glue is two standard continued-fraction facts, named rather than hidden: that `convPairs` is exactly the list of convergent denominators in the window, and the classical bound `θ_j > 1/(q_j+q_{j+1})` that links the integer criterion to the seam constraint. Both are textbook; neither is in Mathlib in directly usable form.
>
> **The statement this closes on:** *no positive cycle with `x_min ≥ 2⁷¹` and length `n ≤ 3.5032·10¹⁰`* — verified exactly throughout, and formalized except for the two named continued-fraction facts.

### Operational definitions and artifact observations (read, never run), flat

- REQ-052/053/054 have committed scripts + outputs; **REQ-055 and REQ-056
  have committed outputs only** (`OUT_REQ-MATH-055.txt`, `OUT_REQ-MATH-056.txt`;
  no `test_REQ-MATH-055/056*.py` anywhere in the repo at `5c9b663`).
- `OUT_REQ-MATH-052.txt` and `OUT_REQ-MATH-053.txt` each contain a Python
  traceback mid-file followed by continued output — concatenations of a
  crashed run and a patched re-run; the numbers quoted in the entry come from
  the post-patch portions. Recorded flat.
- `OUT_REQ-MATH-053.txt` contains **two tables with indexings differing by
  one**: its first P3 table has `j=19: q_j = 397573379` (standard indexing,
  matching the committed script), while its "P3 etendu" table — not produced
  by the committed script — has `j=18: 397573379`, i.e. every label shifted
  down by one. This is the origin of the `q₂₁` collision (see Discrepancy 2).
  The same OUT's own line "Hercher publie : n > 1.375e11 = **q_23** exactement
  (True)" uses the standard index — internally split within one file.
- Stack `81054ea`/block 2 says best approximation was verified "exhaustively
  to `q₁₀ = 190537`". The committed REQ-053 script sweeps `n < 31867` (its
  `qs[10]`), and 190537 is `qs[13]` — the figure matches neither the sweep
  bound nor its own convention. Immaterial (my check goes further; below),
  recorded flat.
- Discharge criterion (OUT-056): `2000·q_j·(q_j+q_{j+1}) ≤ 2079·2^71`, with
  canary `1/(q_j+q_{j+1}) < θ_j < 1/q_{j+1}` verified `j = 1..14` his side;
  window stated there as the integral `n ≤ 35031771147`. OUT-055 records the
  rational bound `ln 2 > 693/1000`, the integral-vs-exact window loss
  (0.011%), and a rounder Lean threshold `34,900,000,000` proposed for
  formalization (superseded by the abstracted-threshold route per the blocks).

## Item 2 — the clean-room chain (every derivation in this session's words)

### (a) Cycle product identity — CONFIRMED EXACT

*Derivation (three lines).* For consecutive odd elements of a cycle of the odd
map, each step is exactly `3x_i + 1 = 2^{v_i} x_{i+1}` with `v_i = v_2(3x_i+1)`.
Multiplying the `n = p+1` step identities around the cycle:
`∏_i (3x_i+1) = 2^{Σv_i} ∏_i x_{i+1}`, and the right product is `∏_i x_i`
cyclically shifted, hence equal. So `∏(3x_i+1) = 2^K ∏ x_i` with `K = Σ v_i`. ∎

*Verified:* exact on all four real cycles, both shores, plus the per-step
identity on every step. The `−17` instance reproduces the entry's figures
digit-exact: `∏(3x+1) = −403123745024000 = 2^11 · (−196837766125)`, `K = 11`.
(This is the odd-element form of cycles.md 12.1.1's `2^K = 3^n ∏(1+ε_t)`.)

### (b) Survivor bound + ceiling — CONFIRMED (equivalence proved; sweep exact)

*Per-factor equivalence (one line).* `(3x+1)(3X) ≤ 3x(3X+1) ⟺ 9xX + 3X ≤
9xX + 3x ⟺ X ≤ x`. ∎  (Verified exhaustively `x, X < 60` and on 2000 random
pairs to `10^30`, exact.)

*Survivor.* With `X = x_min` and `R := ∏(3x_i+1)/∏x_i` (exact rational; for a
cycle `R = 2^K` by (a)): each factor `(3x_i+1)/x_i = 3 + 1/x_i ≤ 3(3X+1)/(3X)`
by the equivalence, and `> 3` always. Multiplying the `n` factors:
`3^n < R ≤ 3^n (3X+1)^n/(3X)^n`, i.e. `2^K (3X)^n ≤ 3^n (3X+1)^n`. ∎

*Ceiling.* The strict two-bound `(m+1)^n < 2m^n` for `2n < m` (elementary
induction) at `m = 3X` gives `R < 2·3^n` when `2n < 3X`. So a cycle has
`3^n < 2^K < 2·3^n`, i.e. `n·log₂3 < K < n·log₂3 + 1`, forcing
`K = ⌈n·log₂3⌉ = bitlength(3^n)` — no logarithm needed in the statement. ∎

*Verified:* two-bound on an integer grid; `3^n < R < 2·3^n` on 400 random
synthetic **multisets** (elements only — no orbits, satisfying the hypotheses
`x_i ≥ X` odd, `2n < 3X`) with exact rationals; the sandwich
`2^{K₀−1} < 3^n < 2^{K₀}`, `K₀ = bitlength(3^n)`, strict for all `n ≤ 2000`
(3^n is never a 2-power); trivial-cycle canary (`2 < 3`, `3 < 4 < 6`, `K = 2`).

### (c) Seam bound + log gap — CONFIRMED; the withdrawn figure adjudicated

*Seam (derivation).* From (b), `q_R := R − 3^n ≤ 3^n[(3X+1)^n − (3X)^n]/(3X)^n`.
The difference of powers: `(3X+1)^n − (3X)^n ≤ n(3X+1)^{n−1}` (each of the `n`
telescoping terms is `≤ (3X+1)^{n−1}`), and `(3X+1)^{n−1} < 2(3X)^{n−1}` by the
two-bound (needs `2(n−1) < 3X`, implied by `2n < 3X`). Hence
`q_R (3X)^n < 2n·3^n (3X)^{n−1}`, i.e. **`q·3X < 2n·3^n`** for a cycle
(`q = 2^K − 3^n`, `n = p+1`). ∎  (Verified as exact rationals on 400 multisets.)

*Log gap (derivation).* `q > 0` gives `2^K/3^n = 1 + q/3^n`, so
`0 < K·ln2 − n·ln3 = ln(1 + q/3^n) ≤ q/3^n < 2n/(3X)` (using `ln x ≤ x − 1`,
his `Real.log_le_sub_one_of_pos`). Dividing by `n·ln2`:
`0 < K/n − log₂3 < 2/(3X·ln2) =: δ`. Since the gap is one-signed,
`|log₂3 − K/n| < δ` and `‖n·log₂3‖ ≤ |n·log₂3 − K| < n·δ`. ∎

*Verified:* `δ = 2/(3·2^71·ln2) = 4.07336·10⁻²²` (in-house fixed point, two
precisions agreeing) — the entry's `4.0734·10⁻²²` is this value rounded.
**The withdrawn `4.955·10^10` window is exactly the missing-factor-2
artifact:** with `δ_wrong = 1/(3X·ln2)` (REQ-053's constant) the window
`√(1/(2δ_wrong))` computes to `49547666543 = 4.9548e10` (his rounded 4.955e10),
which is the corrected window times `√2` exactly. Confirmed.

### (d) The window, exactly — BOTH FIGURES RIGHT, EACH FOR ITS OWN DEFINITION (Discrepancy 1 pinned)

Legendre's criterion applies when `δ ≤ 1/(2n²)`, i.e. `n ≤ √(1/(2δ))`.

- **Exact form:** `√(1/(2δ)) = √(3·2^71·ln2/4)`; floor = **`35035491004`**
  (two precisions agree) = `3.50355·10^10` → rounds to **`3.5035·10^10`**.
- **Integral form:** `n ≤ √(1/(2δ)) ⟺ 4n² ≤ 3·ln2·X`; the rational
  under-approximation `2079/4000 < 3·ln2/4` (equivalently `693/1000 < ln2`,
  verified by integer fixed-point comparison at both precisions) gives the
  sufficient integer condition `4000n² ≤ 2079·2^71`, whose largest solution is
  **`n = 35031771147`** (exact isqrt; tightness verified both sides) =
  `3.50318·10^10` → rounds to **`3.5032·10^10`**.
- Direction: the integral window is strictly inside the exact one (loss
  0.011%) — **conservative, the right direction** (everything the integral
  window claims, the exact window also claims).

**Pin, flat:** `3.5035·10^10` is correct for the exact definition
`√(1/(2δ))` — that is the definition in stacks `9428663`/`89d9efc` and
REQ-MATH-054 (and the withdrawn `4.955e10` was this same definition with the
factor-2 slip). `3.5032·10^10` is correct for the integral definition
`4000n² ≤ 2079·X` at `X = 2^71` — introduced when the Legendre step was
formalized with the abstracted threshold (stack `4856058`, block `5773bd0`),
and it is the right figure for the **final closure statement**, since the
kernel discharge runs over the integral window. So yes: the definition
shifted mid-entry (exact → integral), both figures are right under their own
definitions, nothing is wrong beyond the entry using the two four-digit
roundings without saying the definition moved. Offer-shaped fix: one clause
in the final block ("`3.5035·10^10` = the exact Legendre bound; the kernel
uses the integral under-approximation `4000n² ≤ 2079·2^71`, i.e.
`n ≤ 35031771147 ≈ 3.5032·10^10`").

### (e) Convergents — CONFIRMED (22 in-window); labeling resolved (Discrepancy 2 pinned); census cross-check exact

Continued fraction of `log₂3` computed from scratch (in-house fixed-point
`ln3/ln2`, exact Euclid on the scaled integers; partial quotients identical at
130 and 210 digits through all needed terms):
`[1; 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1, 1, 55, 1, 4, 3, 1, 1, 15, 1, 9, 2, 5, 7, 1, 1, ...]`.

- **Standard indexing** (the convention pinned here and used throughout:
  `p_0/q_0 = 1/1` from `a_0 = 1`, `p_1/q_1 = 2/1`, `p_2/q_2 = 3/2`, ...; note
  `q_0 = q_1 = 1` are two distinct convergents sharing a denominator value):
  `q = 1, 1, 2, 5, 12, 41, 53, 306, 665, 15601, 31867, 79335, 111202, 190537,
  10590737, 10781274, 53715833, 171928773, 225644606, 397573379, 6189245291,
  6586818670, 65470613321, 137528045312, 753110839881, ...`
- **Census cross-check:** the project's known scales 5, 12, 41, 53, 306, 665,
  15601, 190537 all appear — exact.
- Convergent sides verified by **exact integer power comparisons**
  (`p_j/q_j > L ⟺ 2^{p_j} > 3^{q_j}`) for `j ≤ 13`: alternation exact.
- **Best approximation verified exhaustively to `n < 190537`** (extending his
  committed `n < 31867` sweep): for every `j` with `q_{j+1} ≤ 190537`,
  `min_{1≤n<q_{j+1}} ‖nL‖` is attained at `n = q_j` and equals `θ_j`. Exact
  fixed-point, no failures.
- **The window count:** exactly **22** convergents have `q_j ≤ 35031771147` —
  they are `j = 0..21`, and the set is identical under the exact window
  `35035491004`. Matches `convPairs_length = 22`. (Note, flat: 22 counts
  convergents, not distinct denominator values — `q_0 = q_1 = 1` both appear;
  both trivially pass the criterion, so nothing turns on it.)

**Discrepancy 2, pinned flat (the `q₂₁` collision).** Under the standard
indexing above:

- `6586818670` **is `q₂₁`** → stack `89d9efc`'s "the tightest, `q₂₁ =
  6.587·10⁹`" is **correctly labeled** (and OUT-054/056 use this indexing).
- `65470613321` **is `q₂₂`**, not `q₂₁` → stack `0905b00`'s "first admissible
  scale `n ≥ q₂₁ = 6.547·10¹⁰`" is **off by one** (substance correct — see
  (f): the first admissible scale under the exact seam test IS `65470613321`).
- `137528045312` **is `q₂₃`**, not `q₂₂` → the same stack's "Hercher's
  dedicated `q₂₂ = 1.375·10¹¹`" is **off by one** (substance correct — see
  the Hercher adjudication).

The convention behind the shifted labels is dropping the 0-th convergent
(indexing from `2/1` as `q_1`... equivalently 0-basing the list after the
first `1`). The origin is visible in his own artifacts: OUT-053's committed
first table is standard-indexed, its uncommitted "P3 etendu" table is
shifted-by-one, and the ledger blocks inherited the shifted labels; OUT-053's
own Hercher line says `q_23` (standard). Fix is one convention sentence plus
two subscripts in block `0905b00`'s text (or a ledger-side correction note,
since stacks are history): `q₂₂ = 6.547·10¹⁰`, `q₂₃ = 1.375·10¹¹`, and the
entry's indexing declared to be the one with `q₂₁ = 6586818670`.

### The Hercher adjudication (single-constant web access, used once)

**Citation.** C. Hercher, *There are no Collatz m-cycles with m ≤ 91*,
Journal of Integer Sequences **26** (2023), Article 23.3.5; arXiv:2201.00406
(v3, 4 Apr 2023). Read directly this session (pages 1–5, 11–20 of the arXiv
v3 PDF) under the brief's single-constant grant. Exact statements:

- **Corollary 29:** "If `X₀ ≥ 1536·2^60 = 3·2^69` then every nontrivial cycle
  contains at least `K > 1.375·10^11` odd numbers."
- **Remark 28:** to reach that threshold by previous methods one needs
  `δ < (K+L)/K < δ + 1.1032·10⁻²²` (his `δ` is `log₂6`; his `K, L` = odd and
  even counts), i.e. `X₀ ≥ 3781·2^60`; his Theorem 27 lowers this to
  `2836·2^60`, and the computer-assisted Corollary 29 to `1536·2^60`.
- **Corollary 24, Table 1** (at the paper's `X₀ = 704·2^60`): final row "For
  all `m ∈ ℕ`: `K > 7.20·10^10`"; adjacent row `m ≤ 1.34·10^10`:
  `K > 1.37·10^11`.

**Adjudication of the flourish** ("Hercher's bound `1.375·10^11` is itself a
convergent denominator"):

1. **Integer equality against the printed figure: NO.** Hercher prints only
   the display value `1.375·10^11 = 137500000000`, which is **not** equal to
   `q₂₃ = 137528045312`; the paper nowhere prints the exact integer. The
   printed figure is a rounded-down display (true threshold / printed =
   1.000204), so his `K > 1.375·10^11` is the safe weakening.
2. **Identity of the underlying threshold: YES, verified two ways in this
   session's own arithmetic.** Hercher's threshold mechanism (his Lemma 22)
   is exactly smallest-denominator-in-an-interval — continued-fraction
   machinery on `(K+L)/K` just above `log₂6`, whose denominators are the same
   `q_j` as `log₂3`'s. (i) His Table-1 bound "for all `m`: `K > 7.20·10^10`"
   is the semiconvergent denominator `q₂₁ + q₂₂ = 72057431991 = 7.2057·10^10`
   — reproduced exactly. (ii) His Remark-28 interval width `1.1032·10⁻²²` is
   the distance from `log₂6` to that semiconvergent,
   `(θ₂₁ − θ₂₂)/(q₂₁+q₂₂)` — this session computes `1.1033·10⁻²²`
   (agreement to 4 significant digits; the 5th differs from his print,
   immaterial and recorded flat). Crossing that width forces the denominator
   to the **next** rung, which is exactly `q₂₃ = 137528045312`. So the
   "next threshold" his abstract names IS the convergent denominator `q₂₃`,
   and Merle's flourish is **right in substance** — with the label `q₂₃`
   (standard indexing), not `q₂₂`, and with "exactly" meaning the underlying
   threshold, not the printed decimal.
3. **Scope of Hercher's bound, for the comparison's honesty (item (g)):**
   Corollary 29 is **conditional on verification reaching `X₀ ≥ 3·2^69`** —
   a condition met by Barina's current limit `2^71` (cycles.md 12.6.3 pin:
   J. Supercomputing, 2025), so the `1.375·10^11` bound stands today; at the
   paper's own `X₀ = 704·2^60` the unconditional bound was `K > 7.20·10^10`.
   Hercher's `K` counts **odd members** — the same length convention as T1's
   `n = p+1`. So the comparison IS apples-to-apples on both axes, with one
   asymmetry in Hercher's favor: his hypothesis is weaker (`3·2^69 < 2^71`
   of verified range needed) and his conclusion covers all `n ≤ 1.375·10^11`
   against T1's `n ≤ 3.5032·10^10` — the honest form of "3.9× further, but
   on paper" (ratio verified: `q₂₃/35031771147 = 3.9258`; his 3.92 against
   the exact window: 3.9254). T1's differential value is machine-checkability
   and the shape rigidity (K pinned per scale), not range — which is what the
   entry's honest-scope paragraphs already say.

### (f) The finite discharge — CONFIRMED EXACT (all four numbers reproduce)

*Classical bound (two lines).* `θ_j = |q_j α − p_j| = 1/(α_{j+1} q_j + q_{j−1})`
where `α_{j+1}` is the CF tail (standard identity), and
`α_{j+1} < a_{j+1} + 1` gives `α_{j+1} q_j + q_{j−1} < (a_{j+1}+1) q_j + q_{j−1}
= q_{j+1} + q_j`, hence **`θ_j > 1/(q_j + q_{j+1})`**. ∎ (Verified numerically
with both sides of the sandwich `1/(q_j+q_{j+1}) < θ_j < 1/q_{j+1}` for
`j ≤ 27`.)

*The full implication, directions explicit.* Suppose a positive cycle has
`x_min ≥ 2^71` and length `n ≤ 35031771147`. By (c), `0 < K/n − L < δ`. Write
`K/n` in lowest terms as `a/b` (`b ≤ n`); then `|L − a/b| < δ ≤ 1/(2n²) ≤
1/(2b²)`, so by **Legendre's criterion** (if a reduced `a/b` satisfies
`|α − a/b| < 1/(2b²)` it is a convergent — proof via best approximation: take
`j` with `q_j ≤ b < q_{j+1}`; then `|q_j α − p_j| ≤ |bα − a| < 1/(2b)`, and if
`a/b ≠ p_j/q_j`, `1/(bq_j) ≤ |a/b − p_j/q_j| < 1/(2b²) + 1/(2bq_j)` forces
`b < q_j`, a contradiction) `a/b = p_j/q_j` for some `j`, and `n = m·q_j`,
`K = m·p_j` for an integer `m ≥ 1`. Then `|n·L − K| = m·θ_j` **exactly**, and
the cycle's gap demands `m·θ_j < n·δ = m·q_j·δ`, i.e. `θ_j < q_j·δ` — the
`m` cancels, so **every multiple of `q_j` in the window reduces to the same
per-convergent test** (this closes a small looseness in the entry's phrase
"`n` is one of the 22 convergent denominators": a priori `n` is a multiple of
one; the discharge kills all multiples at once). Now the integer criterion:
`2000·q_j(q_j+q_{j+1}) ≤ 2079·2^71` implies (using `693/1000 < ln2`)
`2q_j(q_j+q_{j+1}) ≤ 3·ln2·2^71`, i.e. `q_j·δ ≤ 1/(q_j+q_{j+1}) < θ_j` —
contradicting the cycle's demand. **Direction: criterion holds at `q_j` ⟹ no
positive cycle with `x_min ≥ 2^71` at any length `n = m·q_j` in the window.**
With Legendre covering every in-window `n`, the closure follows. ∎

*Verified, all exact:*

- **All 22 criteria pass** (`j = 0..21`), pure integer arithmetic.
- **Tightest margin `5.1713×` at `q₂₁ = 6586818670`** — the entry's `5.17×`;
  LHS `= 949258476701148143940000`, RHS `= 2079·2^71 =
  4908899958942996199636992` (both reproduce OUT-056 digit-exact).
- **Exact test at `q₂₁`: `θ₂₁/(q₂₁δ) = 5.4433×`** — the entry's `5.44×`; and
  `θ_j ≥ q_jδ` holds at all 22, so the integer form is conservative exactly
  as claimed (5.17 < 5.44 the right way).
- **Non-vacuity canary: the first convergent past the window, `q₂₂ =
  65470613321`, FAILS the criterion** (`2000·q₂₂(q₂₂+q₂₃) =
  26580893368085642900386000 > 2079·2^71`), and under the exact seam test
  `q₂₂` is admissible (`θ₂₂ < q₂₂δ`) while no `j ≤ 21` is — i.e. the first
  scale the seam chain cannot exclude is `n = q₂₂ = 6.547·10^10`, exactly
  stack `0905b00`'s substance (with the label corrected per Discrepancy 2).
- Multiples: `|m·q_j·L − m·p_j| = m·θ_j` verified at three `(j, m)` instances.

### (g) Scope statement — CONFIRMED AS STATED, with the comparison notes above

The closure "**no positive cycle with `x_min ≥ 2^71` and length
`n ≤ 3.5032·10^10`**" follows from (a)–(f) exactly as stated, with: length
`n` = number of odd elements (`= p+1`, same convention as Hercher's `K`);
`x_min ≥ 2^71` = the Barina verification input (cycles.md 12.6.3; for a real
nontrivial positive cycle this hypothesis is automatic, since any element
below the verified range would converge); the window figure being the
integral form per (d). The Hercher comparison is apples-to-apples per the
adjudication above; the one scope asymmetry worth keeping honest in co-edit
language: Hercher's `1.375·10^11` needs only `X₀ ≥ 3·2^69` of verification —
strictly less than the `2^71` this chain instantiates — so "3.9× further" is
if anything understated on hypotheses, and T1's claim to fame is the
kernel-checkable chain plus the structural (no-hair) reading, not range.

### (h) Non-vacuity — CONFIRMED: each real cycle exits scope exactly where the hypotheses say

| cycle | n | K | q = 2^K−3^n | positive shore (q>0)? | x_min ≥ 2^71? | excluded from T1's scope by |
|---|---|---|---|---|---|---|
| +1 | 1 | 2 | +1 | yes | no | **only** `x_min < 2^71` |
| −1 | 1 | 1 | −1 | no | no | negative shore (`q < 0`) |
| −5 | 2 | 3 | −1 | no | no | negative shore (`q < 0`) |
| −17 | 7 | 11 | −139 | no | no | negative shore (`q < 0`) |

The pleasing consistency check: the trivial cycle's scale `n = 1` **is** on
the convergent grid (`q_0 = q_1 = 1`), and the discharge criterion at `q = 1`
*passes* — meaning the chain proves no length-1 positive cycle exists **above**
`2^71`; the real trivial cycle lives below, passing through exactly the
`x_min` crack and no other. The three negative cycles have `2^K < 3^n`
(verified exact), so the positive-shore hypothesis (`q > 0`) excludes them
before any size question arises. No link is contradicted by any real cycle.

## Adjudication summary (one line per claimed link)

| Link (entry claim) | Status |
|---|---|
| 1. Product identity, exact on 4 cycles; `−17` figures | **CONFIRMED EXACT** (derivation three lines; digit-exact) |
| 2. Survivor bound; per-factor `⟺ X ≤ x` | **CONFIRMED** (one-line equivalence proved; exact sweeps) |
| 3. Ceiling `3^n < 2^K < 2·3^n` at `2(p+1) < 3X`; `K = ⌈nL⌉` | **CONFIRMED** (two-bound proved on grid; sandwich exact to n = 2000) |
| 4. Seam `q·3X < 2(p+1)·3^{p+1}` | **CONFIRMED** (derived; exact rational sweep) |
| 5. Log gap; `δ = 4.0734e-22`; factor-2 correction | **CONFIRMED** (`4.07336e-22`; withdrawn `4.955e10` = exactly `√2` × corrected window) |
| 6. Legendre window; 3.5035 vs 3.5032 | **BOTH RIGHT, DEFINITIONS PINNED** (exact `35035491004` vs integral `35031771147`; integral conservative; the definition shifted at stack `4856058`) |
| 7. 22 convergents in window; `q₂₁` tightest | **CONFIRMED EXACT** (count 22 = `j = 0..21` standard; labels: `89d9efc` correct, `0905b00` off by one on both `q₂₁` and "Hercher's `q₂₂`") |
| 8. Discharge: 5.17× / 5.44× / canary at next convergent | **CONFIRMED EXACT** (5.1713 / 5.4433; `q₂₂` fails criterion and is the first admissible seam scale; multiples covered by the same test — the entry's "n is a convergent denominator" tightened to "a multiple of one", closed by the same 22 checks) |
| 9. Closure statement | **CONFIRMED AS STATED** (integral window figure; conventions checked) |
| 10. Hercher flourish | **RIGHT IN SUBSTANCE, TWO QUALIFICATIONS** (threshold = `q₂₃` = 137528045312 exactly, verified via his Remark-28 width and Table-1 semiconvergent `7.2057e10 = q₂₁+q₂₂`; but the paper prints only the rounded `1.375e11`, and the bound is conditional on `X₀ ≥ 3·2^69` — met by Barina `2^71`) |

**The kernel claims (thirteen theorems, axiom hygiene, `convPairs`,
retraction record) are NOT adjudicated here** — that is the sibling session
`merle-lean-r10-audit`. This session confirms the mathematics those theorems
state, in fresh code, from scratch.

## Flags, collected (recorded, not disputed)

1. **Window figure (Discrepancy 1):** both 3.5035e10 and 3.5032e10 correct,
   each under its own definition; the definition shifted mid-entry
   (exact → integral) without a naming clause. Offer: one sentence in the
   final block distinguishing them (values on file: `35035491004` /
   `35031771147`).
2. **`q₂₁` labeling (Discrepancy 2):** stack `0905b00`'s `q₂₁ = 6.547e10` and
   "Hercher's `q₂₂` = 1.375e11" are off by one under the indexing that makes
   its own sibling stack (`89d9efc`, `q₂₁ = 6.587e9`) and his OUT-054/056
   correct; true labels `q₂₂ = 65470613321`, `q₂₃ = 137528045312`. Substance
   right in both stacks. Offer: pin the convention (`q₀ = q₁ = 1` both
   counted; `q₂₁ = 6586818670`) and correct the two subscripts.
3. **Hercher wording:** "Hercher's dedicated `q₂₂ = 1.375·10^11`, itself a
   convergent denominator" should read: Hercher's next-threshold bound is
   `K > 1.375·10^11` (Cor. 29, conditional on `X₀ ≥ 3·2^69`, met by Barina
   `2^71`), the underlying threshold being exactly `q₂₃ = 137528045312`,
   which the paper prints only in rounded form. The frame-prediction point
   (the thresholds live on the convergent/semiconvergent grid) is genuinely
   supported — his 7.20e10 all-`m` row is `q₂₁+q₂₂` exactly.
4. **Artifact hygiene, flat:** REQ-055/056 outputs committed without scripts;
   OUT-052/053 contain tracebacks of crashed first runs; OUT-053 carries two
   mutually shifted index conventions (the source of Discrepancy 2); block 2's
   "best approximation exhaustively to `q₁₀ = 190537`" matches neither the
   committed sweep bound (`n < 31867`) nor its own indexing (190537 = `q₁₃`) —
   our side re-verified the property exhaustively to `n < 190537`, so the
   fact stands regardless.
5. **Count vocabulary, minor:** "22 convergent denominators" counts
   convergents `j = 0..21` including both `q₀ = q₁ = 1`; as distinct scales
   there are 21. Nothing turns on it (both pass trivially); one clause fixes.

## Key recommendation (recommendation only; no key is turned here)

**Turn-with-scope** — the mathematics of every link is confirmable in the
clean room and was confirmed here (62 exact checks, 0 failures; every
headline number reproduced digit-exact: `4.0734e-22`, both windows, 22, 5.17×,
5.44×, the canary, 3.9×):

- **Turns on:** the product identity, survivor/ceiling, seam, log gap, the
  Legendre-window closure and the 22-point discharge **as verified
  mathematics**, including the corrected-δ history (his own factor-2
  correction confirmed exactly) and the non-vacuity structure.
- **Deferred to the sibling audit (`merle-lean-r10-audit`), explicitly outside
  this key:** all kernel claims (thirteen theorems, `[propext]`-only
  discharge, `convPairs_length`, the `da2c8db` retraction record).
- **Offers to carry (acceptance his call):** (a) the window clause pinning
  exact vs integral definitions (flag 1); (b) the indexing convention + the
  two subscript corrections in the `0905b00` block's text (flag 2); (c) the
  Hercher sentence restated per flag 3 (with the Cor. 29 citation and the
  `X₀ ≥ 3·2^69` condition named — it strengthens the frame-prediction point
  rather than weakening it); (d) the two named glue facts are indeed textbook
  and our clean-room derivations of both (the multiples-reduction and
  `θ_j > 1/(q_j+q_{j+1})`) are in these findings, offered as the ledger's
  statement of what "glue" means precisely — including the small tightening
  that in-window `n` is a priori a *multiple* of a convergent denominator,
  closed by the same 22 checks; (e, minor) flags 4–5 as wording/hygiene notes.
