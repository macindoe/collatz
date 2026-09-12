# Findings: the top-door lineage as an object of its own (2026-09-13)

Delegated session, branch `top-door-lineage`. Supports `briefs/top-door-lineage-brief.md`.

## Base SHA and branch

The worktree's HEAD at spawn (`a7543ce`) predated the brief: `briefs/top-door-lineage-brief.md` did not exist in the worktree, and `git log --oneline -1` showed a commit dated 2026-09-10 (the tears-problem merge), not 2026-09-13. Per the brief's own rule, checked `git merge-base a7543ce 4ccfc09`: `a7543ce` is an ancestor of the local `main`'s HEAD `4ccfc09` (a clean fast-forward, no divergent commits on the worktree branch), so `git merge --ff-only main` was used rather than a rebase. Branch `top-door-lineage` was then created from `4ccfc09`.

**Base SHA: `4ccfc09`** (`briefs: delegation brief for HANDOFF item 6 -- the top-door lineage as an object ...`).

## Mathematics (Queue item 1, written before any computation)

### Definitions (author's terminology, 2026-09-10)

For a state `(Ω,D)`, reverse.md 14.1.1 gives representatives `y_a = 2^(D-a) 3^a Ω - 1`, `0 ≤ a ≤ D-1`. The `a=0` representative `y₀ = 2^D Ω - 1` (reverse.md 14.8.1) is the **top door**; the representatives with `a ≥ 1` are the **side doors**. A **top-door lineage** is a backward path through top doors only — at every backward step, the branch used is the current state's own top door.

### Item 1: aliveness and parity; the forward/backward bridge

**Claim (Theorem 14.5.1 at `a=0`).** The top door of `(Ω,D)` is alive iff `2^D Ω ≢ 1 (mod 3)`, i.e. iff `y₀ = 2^D Ω - 1 ≡ 1 (mod 3)`.

This is Theorem 14.5.1 read verbatim at `a=0`: "the sole mortal door is `a=0`: it is dead iff `2^D Ω ≡ 1 (mod 3)`." Nothing to re-derive; a direct instantiation.

**Claim.** If `y₀` is alive, every admissible branch `s` is odd.

Reverse.md 14.1.1's parity constraint: a branch `s` is admissible for a door `y` iff `s` is odd when `y ≡ 1 (mod 3)` and even when `y ≡ 2 (mod 3)`. An alive top door has `y₀ ≡ 1 (mod 3)` (above), so every admissible `s` is odd — a direct instantiation, not a new fact.

**Claim (forward direction, the bridge).** A step's exit is the `a`-th door of the successor state exactly when the step's 3-gain is `a`. In particular, a step whose exit is the successor's *top* door has 3-gain `0`.

This is reverse.md 14.14.1.1's dictionary (`a_+ = a`, the door-recovery formula `y+1 = 2^m 3^a Ω` read against the forward step's own `C = 2^s(y+1)`). It is the fact that makes "backward path through top doors" and "forward orbit with no 3-gain at any step" the same object, stated in the Provenance as a claim and re-derived here from 14.14.1.1, not asserted.

**Claim (spine.md 9.3, `s` odd `⟺` `a_+ = 0`).** Lemma 9.3.1: `3 | x_exit+1` iff `s` even. Contrapositive: `3-gain = 0` iff `s` odd.

**Correction to the brief's "off resonance" hedge.** The Provenance states this equivalence "off resonance." Re-derivation from stage3.md's trichotomy (11.8.6.2.1, `h(s) = v_3(2^s-1)`, `h(s) = 0` if `s` odd, `1+v_3(s)` if `s` even; `a_+ = h(s)` if `h(s) < d`, `a_+ = d` if `h(s) > d`, `a_+ = d + v_3(ω+β) ≥ d` if `h(s) = d`, the resonant case) shows the hedge is unnecessary: since every valid state has `d ≥ 1`, and `h(s) = 0` exactly when `s` is odd, the resonance condition `h(s) = d` is *impossible* whenever `s` is odd (it would require `d = 0`). So for `s` odd, `h(s) = 0 < d` always holds, unconditionally, and `a_+ = h(s) = 0` with no exception. Conversely, for `s` even, `h(s) ≥ 1`, and all three trichotomy cases give `a_+ ≥ 1` (`h(s) ≥ 1`, or `d ≥ 1`, or `d + v_3(ω+β) ≥ d ≥ 1`), so `a_+ ≠ 0` always. **The biconditional `s` odd `⟺` `a_+ = 0` holds unconditionally, at every state, not merely off a resonant sub-case.** The resonant case is real — it changes the *value* `a_+` takes when `s` is even (from the generic `h(s)` to the larger `d + v_3(ω+β)`) — but it never produces an exception to the biconditional itself, since resonance cannot even arise when `s` is odd. This is the "boundary case" the brief's Queue item 1 asked to check; the correction is a strengthening (unconditional in place of "off resonance"), not a refutation, and it is re-derived here from stage3.md rather than asserted. Explicit resonant instances were constructed and checked (item (a)(ii) below) to confirm `a_+ ≥ 1` (never `0`) exactly at the boundary `h(s) = d`.

**Consequence.** A top-door orbit — forward, no 3-gain at any step — has `d_t = m_t` at every state: no `3^a` factor is ever absorbed.

### Item 3: standing in the record (pointers only, re-checked, not restated)

- reverse.md 14.5.1/14.8.3: the sole mortal door is `a=0`, dead on exactly two of the four `(Ω mod 3, D mod 2)` classes, "density 1/2" under uniform counting of those classes. So a top-door lineage dies backward at rate `1/2` per step. Confirmed the exact criterion (not merely the rate) in item (a)(iii) below: measured alive rate `0.5005` on `30,000` trials, `0` criterion mismatches.
- reverse.md 14.6/14.6.5: the rigorous density bound (`c* ≈ 0.3304`, lifted to `0.33515`) is built on the door tree rooted at `y=1`'s *own* branching rule, which reverse.md 14.6's Definition explicitly builds via `y ↦ (2^(s+1)y-1)/3` — Lemma 14.6.2's triple law credits the `m=1` (never-dead) representative, and 14.6.5's multi-door lift credits the side doors `a=1,…,D-2` as the *extra*, disjoint resource. The top door (`a=0`) is the one that can die (14.5.1); the proved density accrues on the doors that cannot. So "the proved density lives on the side doors, not the top" is the correct reading of 14.6/14.6.5's own construction, not a new derivation.
- cycles.md 12.6.1.5: the odd-step stratum's margin `c_strat ≈ 0.2667875` (interior maximum at `α* ≈ 0.3747344`) against the general `c_gen ≈ 0.0793186`. "Odd-step stratum" there means every `s_t` odd in the counting sense of that remark's two families — exactly the top-door / odd-stratum condition named here under a different name, confirmed by inspection of 12.6.1.5's definition ("odd-step stratum — all `s_t` odd").

## Item 4: the odd-stratum cycle equation

**Derivation.** Proposition 12.6.1: `ω_r · 3^(a_(r-1)) · q = R_r` for every rotation `r`, where `R_r = Σ_t 3^(M_t) 2^(S_t) (2^(s_t)-1)`, `M_t = Σ_(j>t) m_j`, `S_t = Σ_(j<t) σ_j`. Neither `M_t` nor `S_t` nor the `(2^(s_t)-1)` factor references any `a_t` — the *definition* of `R_r` is purely in `(m_t,s_t)`. The only place `a` enters Proposition 12.6.1's statement is the left-hand factor `3^(a_(r-1))`. On the odd stratum (every `s_t` odd), item 1's law gives `a_t = 0` for every `t` unconditionally, so `3^(a_(r-1)) = 1` at every rotation, and the equation reads

```text
ω_r · q = R_r      for every rotation r,
```

with `q, R_r, n = Σm_t, K = Σs_t+n` exactly as in the general Proposition. **What simplifies:** only the `3^a` factor drops. **What does not simplify:** the size conditions `q ≤ R_r` (12.6.1's positivity/domination clause) still vary genuinely by rotation — nothing about the odd stratum makes them uniform, and 12.8.6.4's cited rotation-dependent instances stand unchanged; the transport recurrence's gcd-invariance (12.6.1.1) is unaffected either way, since its own derivation (`2^(σ_r) R_(r+1) = 3^(m_r) R_r + (2^(s_r)-1) q`) never involves `a_t` at all.

**Verification design.** No new cycle is assumed or searched for. Three checks: (i) the transport recurrence re-verified fresh on random general and random odd-stratum profiles (it must hold either way, since it never used `a`); (ii) the simplified equation `ω_r q = R_r` checked with real closing integers on the three known cycles, reconstructed via `d_0 = m_0` (licensed by the odd-stratum consequence `d_t=m_t`) and confirmed to close exactly under forward simulation; (iii) the same reconstruction-and-closure check on all twelve profiles of the bounded census (item 2), which are all odd-stratum profiles by inspection; (iv) an open-path (non-cyclic) confirmation: real random forward orbits, wherever a run of `≥3` consecutive odd-`s` steps occurs, checked directly for `a_+=0` and `D=m_+` at every step of the run — the mechanism chained along genuine (not fabricated) orbit segments.

## Item 2: the bounded census (canary, not extended)

Reproduced at exactly the brief's stated bounds: `p ∈ {1,2,3,4}`, every entry `m_t, s_t ∈ {1,…,6}`, exhaustive (`1,727,604` profiles examined), testing `q | R_0` only (no closure, no period-search, no extension of the bound). Twelve profiles satisfy `q | R_0`:

| p | ms | ss | n | K | q | ω₀ = R₀/q | x₀ = 2^{m₀}ω₀−1 |
|---|---|---|---|---|---|---|---|
| 1 | (1,) | (1,) | 1 | 2 | 1 | 1 | 1 |
| 1 | (2,) | (1,) | 2 | 3 | −1 | −1 | −5 |
| 2 | (1,1) | (1,1) | 2 | 4 | 7 | 1 | 1 |
| 2 | (2,2) | (1,1) | 4 | 6 | −17 | −1 | −5 |
| 2 | (3,4) | (3,1) | 7 | 11 | −139 | −5 | −41 |
| 2 | (4,3) | (1,3) | 7 | 11 | −139 | −1 | −17 |
| 3 | (1,1,1) | (1,1,1) | 3 | 6 | 37 | 1 | 1 |
| 3 | (2,2,2) | (1,1,1) | 6 | 9 | −217 | −1 | −5 |
| 4 | (1,1,1,1) | (1,1,1,1) | 4 | 8 | 175 | 1 | 1 |
| 4 | (2,2,2,2) | (1,1,1,1) | 8 | 12 | −2465 | −1 | −5 |
| 4 | (3,4,3,4) | (3,1,3,1) | 14 | 22 | −588665 | −5 | −41 |
| 4 | (4,3,4,3) | (1,3,1,3) | 14 | 22 | −588665 | −1 | −17 |

All twelve are rotations/repeats (periods 1–4) of exactly the three known words `(1,1)`, `(2,1)`, `((4,1),(3,3))` — checked by construction (every hit's `(ms,ss)` tuple is a rotation of a power of one of the three base words, and the set of hits equals the full set of such rotations/powers within the bound). **No fourth word; no evidence beyond the known instances.**

**Note on `x₀ = -41`.** The block-entry integer `x₀` is *not* rotation-invariant: the two rotations of the `((4,1),(3,3))` word are the same cycle read from its two different states, and their block-entry integers are the two different odd numbers the classical (negative) cycle actually visits at those two points, `-17` and `-41` — both on the same seven-block T-cycle containing `-17`. This is not a fourth cycle; it is confirmation that the census returns *words*, and a word's two rotations carry two different (but equally valid) block-entry witnesses. Recorded because an earlier draft of this script's self-check asserted the wrong invariant (`x₀ ∈ {1,-5,-17}`) and had to be corrected to "hit's word is a rotation/repeat of one of the three base words" — caught by the script itself failing on `-41`, fixed, re-run clean. This is the one thing the pre-check's own bookkeeping (not its mathematical claim) needed correcting.

## Item 5: realized run lengths vs. `(2/3)^n`

**Rate, derived.** Stage1.md's frequency ledger (11.8.4.4): `P(s=1)=1/2`, `P(s=2)=1/4`, `P(s=k)=2^{-k}` — a heuristic past the digit budget, an unconditional theorem inside it (stage1.md, citing aeh.md 13.2.4(d)–(e)). Under this law, `P(s odd) = Σ_{k odd} 2^{-k} = (1/2)/(1-1/4) = 2/3`. Under the further (independence) reading the ledger's own remarks use for block-to-block behavior, a run of consecutive odd-`s` steps is geometric with continuation probability `2/3`, so `P(run length ≥ n) = (2/3)^n`.

**Measurement.** `4,000` independent random large starts (`ω` uniform-odd, `3∤ω`, in `[2^200, 2^260)`, `d=1`), each run forward `120` steps, seed `20260916`; interior (non-boundary-censored) runs of consecutive odd-`s` steps collected: `103,126` runs. Measured `P(s odd) = 0.6662` over all `480,000` steps (theory: `2/3 = 0.6667`).

| n | #runs ≥ n (measured) | P(len≥n) measured | (2/3)^n |
|---|---|---|---|
| 1 | 103126 | 1.0000 | 0.6667 |
| 2 | 68435 | 0.6636 | 0.4444 |
| 3 | 44899 | 0.4354 | 0.2963 |
| 4 | 29493 | 0.2860 | 0.1975 |
| 5 | 19659 | 0.1906 | 0.1317 |
| 6 | 13021 | 0.1263 | 0.0878 |
| 7 | 8568 | 0.0831 | 0.0585 |
| 8 | 5598 | 0.0543 | 0.0390 |
| 9 | 3692 | 0.0358 | 0.0260 |
| 10 | 2458 | 0.0238 | 0.0173 |
| 11 | 1648 | 0.0160 | 0.0116 |
| 12 | 1089 | 0.0106 | 0.0077 |
| 13 | 700 | 0.0068 | 0.0051 |
| 14 | 454 | 0.0044 | 0.0034 |
| 15 | 293 | 0.0028 | 0.0023 |
| 16 | 201 | 0.0019 | 0.0015 |
| 17 | 143 | 0.0014 | 0.0010 |
| 18 | 89 | 0.0009 | 0.0007 |
| 19 | 62 | 0.0006 | 0.0005 |
| 20 | 39 | 0.0004 | 0.0003 |
| 21 | 25 | 0.0002 | 0.0002 |
| 22 | 12 | 0.0001 | 0.0001 |
| 23 | 8 | 0.0001 | 0.0001 |
| 24 | 5 | 0.0000 | 0.0001 |
| 25 | 5 | 0.0000 | 0.0000 |
| 26 | 2 | 0.0000 | 0.0000 |
| 27 | 2 | 0.0000 | 0.0000 |
| 28 | 0 | 0.0000 | 0.0000 |

**Reading, flat.** The measured ratio `P(len≥n)/(2/3)^n` runs from `1.0` (n=1, definitional) up to about `1.5` by `n≈4` and stays in a `1.3`–`2×` band through `n≈15` before the tail (`n≥20`) is too thin (`<40` runs) to read. This is **consistent with** geometric behavior at ratio `2/3` in shape (monotone decay, no plateau, no early cutoff) but the level sits above the naive independence prediction by a roughly constant multiplicative factor in the bulk range — the sample is not large enough, and no correction for the boundary-run censoring beyond the simple interior-run filter was attempted, to say more than "consistent with a geometric law of this rate, not exactly matching the naive i.i.d. count at this sample size." No claim of exact agreement is made; none was expected — the brief calls this calibration, not a theorem, and that is exactly the register used on cycles.md 12.6.1.8's one-sentence summary.

## Item 6: the checkable open question

Filed verbatim at `open-problems.md` 11.13 (below); no mechanism pursued, per the brief's explicit instruction not to force one.

## Item 7: the flat note

`1 + 2^s = 3^k` forces `s` odd: mod `4`, `3^k ≡ 1 (mod 4)` iff `k` even, `≡ 3 (mod 4)` iff `k` odd; `1+2^s ≡ 3 (mod 4)` iff `s=1`, `≡ 1 (mod 4)` iff `s ≥ 2`. So `s=1` forces `k` odd and `s≥2` forces `k` even; combined with the elementary classification (the only solutions are `(s,k)=(1,1),(3,2)`, checked exhaustively for `k<2000`, matching cycles.md 12.6.1.2's Gersonides citation), both solutions have `s` odd. The two guaranteed-neighbour laws of `briefs/ladder-family-graph-brief.md` (`s=1,3`) are therefore top-door.

## Verification record

`experiments/top_door_lineage.py`, fresh code (imports nothing from any existing script: `modq_spectrum.py`, `margin_asymptote.py`, any `mirror_*.py`, any `merle_*.py` — all valuations, the reduced map, the predecessor characterization, and the rotation numerator are reimplemented from the wiki's definitions). Exact Python-integer arithmetic at every pass/fail decision. Canaries first (the trivial fixed point; Prop 12.6.1's fake-trivial-cycle sanity identity at `p ∈ {1,2,3,4,7}`; the three known cycles reconstructed from their odd-stratum profiles and closed by forward simulation). Seed `20260913` (run-length sub-seeds `20260913+1..+3`).

**Single reproducing command:**

```
python experiments/top_door_lineage.py
```

No phases, no flags. Output committed verbatim (modulo the wall-clock `time=` line) at `experiments/top_door_lineage_output.txt`.

**TOTAL: checks=15091, failures=0** (run time ≈7 s).

Breakdown: canaries (trivial fixed point; 5 instances of the fake-trivial-cycle identity; 3 known cycles × ~9 checks each); item (a) — 60,000 forward-direction trials, 26 explicit resonance-boundary instances, 30,000 backward round-trip trials; item (b) — the twelve-profile census plus 2 structural checks; item (c) — 4,000+4,000 transport-recurrence trials, 12 census-closure checks, 2,000 open-path chain trials; item (e) — the `1+2^s=3^k` classification to `k<2000`. Zero failures throughout, including after the one self-check correction recorded above (the `x₀` invariant in item 2), which was caught and fixed before this run.

`experiments/encoding_scan.py`: **RESULT: CLEAN** (re-run after all wiki edits, before the final commit).

## For the main session at merge

- **15.7 pointer to check.** Cycles.md 12.6.1.8's flat note cites `ladder.md 15.7` (the family-graph front's guaranteed-neighbour laws), which does not exist on this branch — it is the deliverable of the parallel `ladder-family-graph` branch. At merge, confirm `ladder.md 15.7` lands with laws at `s=1` and `s=3` (HANDOFF.md item 5's "(i) the merge/skip law," `s` implicit at `1`, and "(ii) the two-row commutation law," `s=3`) so the pointer resolves; if the merged section uses different notation for which law carries which `s`, the clause's parenthetical ("HANDOFF.md item 5; ladder.md 15.7 when merged") may need a one-word adjustment, not a re-derivation — item 7's own mathematics (`1+2^s=3^k ⟹ s` odd) is independent of that page and already verified in this branch.
- **Front-matter seam with the parallel branches.** This branch touches reverse.md's front matter (`updated` only, not the Current-state paragraph, per the brief's instruction) and cycles.md's front matter (`updated` only). `briefs/ladder-afterlife-brief.md` and `briefs/ladder-family-graph-brief.md` (base commit `4ccfc09`, same as this branch) may also touch reverse.md 14.10 (mirror versions, expected and unchecked per HANDOFF item 5) and ladder.md's own front matter; no overlap in *section content* is expected (this branch adds 14.8.4, not 14.10 or 15.x), but the `updated:` date line on reverse.md will collide at merge time across all branches that touch that page — ordinary front-matter resolution, not a content conflict.
- **Section numbering.** 14.8.4 is a new subsection after the existing 14.8.3 (no renumbering of 14.9 onward — 14.8.4 is an addition within 14.8, not an insertion that shifts later numbers). 12.6.1.8 is likewise a new subsection after 12.6.1.7, before Lemma 12.6.2 (unrenumbered). 11.13 is a new top-level open-problems entry after 11.12. None of these required renumbering anything else on their pages.
- **index.md left untouched, deliberately.** The section-number resolver lists page-range ownership only (`§12 (post-monolith) → cycles.md`, `§14.1–14.14 (post-monolith) → reverse.md`, `§11.1–11.7 → open-problems.md` with 11.8/11.10 as the only individually-listed post-11.7 entries); 11.11 and 11.12 were not added as individual resolver lines when they were created, so 11.13 follows that precedent and was not added either. If the main session's convention has since changed, this is a one-line addition, not a content question.
- **Stopping-rule compliance, restated for the reviewer.** No per-period cycle search ran anywhere in this branch. The only enumeration is the item-2 census, reproduced at exactly the brief's stated bounds (`p≤4`, entries `≤6`) and not extended; everything else is either a formula-level identity on profiles (items 4, item (c)(i)-(ii)) or a check along real, already-known objects (the three canaries, the census's own twelve profiles) or genuine random *forward* simulation with no periodicity test (items (a), (c)(iv), (d)). Open-problems.md 11.13 states the "must a cycle be top-door" question without attempting it, per the brief's explicit instruction (Queue item 6, Rules "record obstructions; do not force a mechanism").
- **What was not covered.** No attempt was made to check whether the odd-stratum margin (`0.267`/step) has any bearing on whether 11.13 is *likely* true — cycles.md 12.6.1.5's own calibration note already declines to read `2^{-margin}` as more than a heuristic, and 11.13 does not repeat or extend that reading. No search of any kind, bounded or otherwise, was run past the item-2 census.

## Files changed

- `experiments/top_door_lineage.py` (new)
- `experiments/top_door_lineage_output.txt` (new)
- `reverse.md` (new Remark 14.8.4; front matter `updated`)
- `cycles.md` (new Remark 12.6.1.8; front matter `updated`)
- `open-problems.md` (new entry 11.13; front matter `scope`, `updated`)
- `TOUR.md` (one dictionary row)
- `briefs/top-door-lineage-findings.md` (this file)

No other files touched. `HANDOFF.md`, `ladder.md`, `anchors.md`, `aeh.md`, `README.md`, `publication.md`, `paper/`, `sources/`, `index.md`, `symbols.md` are all untouched, per the brief's rules.

## Review resolution (main session, 2026-09-13)

Item 5's table compares the survival function `P(len ≥ n)` with `(2/3)^n`, and the flat reading above ("a `1.3`–`2×` band") follows from that reference. The reference is one index off: a run counted from its first letter has that letter for free, so under independence `P(len ≥ n) = (2/3)^(n−1)`. Against that column the measured values sit at `0.995, 0.980, 0.965, 0.965, 0.959, 0.946, 0.928, 0.918, 0.915` of the prediction for `n = 2..10` — within `1 %` at `n = 2` and `9 %` at `n = 10`, the shortfall growing slowly as runs are truncated at the orbit's end and the sample thins. cycles.md 12.6.1.8 carries the corrected reading; the script and its committed output are left as run, with the column label as it prints.
