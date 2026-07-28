# Brief: the all-`p` staircase, gap B — remove the correction algorithm, prove the size conditions directly — for a delegated session

**Context required before starting (in order):** `README.md` (binding stopping rules), `AGENTS.md`, `cycles.md` §12.8 in full — especially **Proposition 12.6.1** (the size conditions `q ≤ R_r` and the rotation numerators), **12.8.1** (the uniform trim and its max-plus recursion), **12.8.3** (the staircase), **12.8.6.2** (the explicit profile), **12.8.6.3** (the bounded correction algorithm) and **12.8.6.4** (the instance record) — plus `briefs/staircase-allp-findings.md` (the previous attempt; item 5.3 records that no closed-form bound on the correction algorithm's move count is established) and `experiments/staircase_allp.py`, `experiments/p22_passer.py`, `experiments/uniform_trim.py`.

## Why this exists

`cycles.md` 12.8.6 names 12.8.6.1's Diophantine coverage bound as "the sole remaining gap" of the floor-grade result — but 12.8.6.4's own text records a second one: **no closed-form bound on the correction algorithm's move count is established, at `p = 22` or any other period.** A proof of the all-`p` sharpness claim needs both gaps closed. A sibling session (`briefs/staircase-allp-diophantine-brief.md`) has the first. **You have the second, and it is the one that does not depend on any Diophantine input.**

The shape of the problem: 12.8.6.2 builds an explicit profile from a candidate `n`, and it *typically falls short* on one to a few rotations near the crash block, by a handful of bits. 12.8.6.3 then repairs it by a deterministic local search — auditable, logged, but with no proved termination or bound. **A theorem cannot rest on "an algorithm closed it in every case we ran."**

**The target: replace the algorithm with a proof.** Either (i) prove the base construction's shortfall is bounded and that a bounded, explicitly described set of moves always repairs it; or, better, (ii) modify the construction so that it provably satisfies every rotation's size condition with no correction at all, and prove that directly.

**Stopping-rule compliance, and state it in your findings:** this is a negative structural result about the reach of *size/counting* arguments, the same category as 12.8.6, and explicitly not a cycle search. You construct size-passers, never cycles; you touch the divisibility system only to confirm — as 12.8.3 and 12.8.6.4 do — that the constructed configurations fail it. **The cycle front stays PARKED; 12.8.5 is unaffected at any grade.**

## Queue

1. **State the target inequality exactly.** From Proposition 12.6.1, write out `R_r` for a general profile `(m_t, s_t)` and the condition `q ≤ R_r` at every rotation `r`, with `q = 2^K − 3^n`. Then specialize to the staircase shape of 12.8.6.2 — geometric climb at ratio `≈ L` with unit exits, one crash block `m_{p−1} = c ∈ {1,2}`, `s_{p−1} = S − (p−1)`. Identify **which rotations are the binding ones** and why they cluster near the crash block, in your own words rather than by re-reading the algorithm's logs.

2. **Quantify the base construction's shortfall.** 12.8.6.2 rounds *partial sums* rather than individual `m_j`, bounding the prefix error at `1/2`. Derive what that buys at the level of `R_r`: an explicit bound on how far the base profile can fall short at the worst rotation, as a function of `p`, `n`, the candidate's approximation quality `‖nL‖`, and the crash depth `c`. Compare it against the measured shortfalls in the existing record (`experiments/staircase_allp.py`, and the `p = 22` rows, the largest at 13 moves).

3. **Then attempt the theorem, preferring route (ii).**
   - Try to exhibit a *modified explicit profile* — a different rounding rule, a different crash depth, a shifted geometric ratio, an extra degree of freedom in the last climb block — for which all `p` size conditions can be **proved** directly, with `γ` bounded explicitly as a function of `p` and the candidate's quality.
   - **Report `γ` as a formula, not as a constant.** The sibling session is determining what budget the sharpness claim actually needs; state the growth you achieve (`O(log p)`, `O(p)`, `O(p log p)`, …) so the two results compose at review. Do not assume the budget is `O(log p)`.
   - If route (ii) resists, fall back to route (i): prove a bound on the shortfall and exhibit an explicit finite repair schedule with a proved move count.
   - Everything must be **unconditional in the profile variables** — you may take the candidate `n` and its quality as *given inputs* (that is the sibling's gap, not yours) and state precisely which properties of `n` your proof consumes. That interface is the deliverable's most important part: name the exact hypothesis on `n` under which your construction provably passes.

4. **Verify, in fresh independently written code.** `experiments/staircase_allp_construction.py`, exact big-integer arithmetic throughout, importing no verification from `staircase_allp.py` or `uniform_trim.py`.
   - Instantiate your construction across the full existing range and beyond it, checking every rotation's `q ≤ R_r` exactly.
   - **Negative controls, and they are required:** show the proof's hypotheses are load-bearing — perturb the rounding rule, the crash depth, the quality hypothesis, and confirm the size conditions genuinely fail where the theorem says they should not hold. A bound that never bites has not been tested.
   - Confirm every constructed instance fails the divisibility system, as 12.8.3 and 12.8.6.4 record for theirs.

5. **Record** (branch commits, per item):
   - `experiments/staircase_allp_construction.py` + committed output.
   - `briefs/staircase-allp-construction-findings.md` — the target inequality; the shortfall bound with its derivation; the theorem attempted, with its **exact hypothesis on `n`** stated as the interface to the sibling result; the proof in full or the obstruction stated sharply; the verification table and the negative controls; and a verdict on whether 12.8.6.3's algorithm can be **removed from the argument** rather than merely bounded.
   - `HANDOFF.md` — ONE scoped paragraph. A sibling session (`staircase-allp-diophantine`) runs in parallel; keep to your own lines.

## Rules

- Branch **`staircase-allp-construction`**. Verify your worktree HEAD contains this brief; if not, rebase onto the `main` SHA given in your launch instructions, and state the base SHA in the findings.
- Per-item commits. Do **not** merge — the main session reviews (re-runs the script) and merges.
- **Nothing is labeled proved without independently written verification code that could have failed. Failures and dead ends are recorded, not deleted** — a sharply characterized obstruction is a real deliverable here, and it is better than an overstated theorem.
- Do not edit `cycles.md`, `paper/` or `publication.md`; recommend instead. Changing a published hedge is a main-session decision after review. `sources/` is immutable.
- No pushes; no interaction with Merle's repositories; nothing for the ledger, the note or the reply.
- Encoding: Edit/Write tools only, never PowerShell `Get-Content`/`Set-Content`; run `experiments/encoding_scan.py` before your last commit.
- Stop after item 5.
