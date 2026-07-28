# Brief: the all-`p` staircase, gap A — the γ budget and candidate availability at every scale — for a delegated session

**Context required before starting (in order):** `README.md` (binding stopping rules), `AGENTS.md`, `cycles.md` §12.8 in full (12.8.1 the uniform trim, 12.8.2 effective finiteness, 12.8.3 the staircase, 12.8.5 the stopping rule, **12.8.6 and all its sub-items** — this session attacks 12.8.6.1), `briefs/staircase-allp-brief.md` and `briefs/staircase-allp-findings.md` (the previous attempt, which reached floor grade), `briefs/merle-pincer-check-findings.md` item 4 (the `p = 22` hole and the two out-of-chain candidates), `paper/collatz-reduced-v2.tex` Theorem `thm:staircase` and Theorem `thm:uniform` (the published statements and the published hedge).

## Why this exists

`cycles.md` 12.8.3 and the published `thm:staircase` both carry the same hedge: the staircase family is assessed, **not proved**, to pass all size conditions with `γ = O(log p)` at every period. 12.8.6 raised the evidence to a contiguous verified range `p ∈ {2,…,23}` and named **12.8.6.1's Diophantine coverage bound as the sole remaining gap** of that floor-grade result.

That hedge is now load-bearing outside the wiki: the joint note's proposed contribution sentence would present the counting dichotomy to a referee, and `briefs/jointnote-premise-ours-findings.md` records that the sharpness half is **exactly half proved** — a theorem by exhibited witness, plus an all-`p` claim carrying the hedge.

**Main-session pre-check, to be re-derived independently and then used:** the multiplicative gaps in the convergent chain of `log₂3` *are* its partial quotients, so a coverage lemma routed through convergent denominators alone is equivalent to `log₂3` being badly approximable — open for every classical constant and, by Borel–Bernstein plus Merle's Gauss–Kuzmin measurement, almost certainly false. Concretely, `q₁₃ = 190537 → q₁₄ = 10590737` is a **55.6× gap** covering periods **`p = 27…35`** with no convergent denominator at all — immediately past where the record stops. The `p = 22` hole was the first sighting of this, not an anomaly.

**Stopping-rule compliance, and state it in your findings:** this is a negative structural result about the reach of *size/counting* arguments — the same category as 12.8.6, whose own status paragraph records the compliance, and the same as `briefs/staircase-allp-brief.md`. It is **not** a per-period cycle search, it constructs size-passers rather than cycles, and it never touches the divisibility system except to confirm (as 12.8.3 and 12.8.6.4 do) that the constructed configurations fail it. **The cycle front stays PARKED and 12.8.5 is unaffected at any grade.** If you find yourself searching for cycles, stop — that is the stopping rule biting.

## Queue

1. **Determine the γ budget. This is the item that decides everything else, so do it first and do it carefully.**
   - Fix the definition of `γ` from 12.8.1 / 12.6.1 and state it in your own words, with the exact inequality the staircase must satisfy at each rotation.
   - Then answer precisely: **what growth rate of `γ(p)` does the sharpness claim actually need in order to do its job?** Its job, per 12.8.3 and 12.8.5, is to show that no polynomial-in-`p` extension of the small-period constants can survive — the period-3 constant being `0.1157n − 2` with `n ≈ 1.585^p`. Write out the comparison explicitly.
   - **The hypothesis to test:** the published hedge claims `O(log p)`, but the comparison may be defeated by any *subexponential* `γ`, since the constant it must fall below grows like `1.585^p`. If a much weaker bound suffices, say so with the inequality written out, and say exactly which bound is the weakest that still works (`O(p)`? `O(p log p)`? `o(1.585^p)`?). **If the weaker bound suffices, the whole problem changes character**, because effective irrationality measures can feed a `O(p)`-type budget and cannot feed a `O(log p)` one.
   - Record honestly if the answer is that `O(log p)` really is needed — that is a legitimate and useful negative.

2. **Characterize what candidate scales are unconditionally available.** For each period `p`, the construction needs an `n` in a bounded multiplicative window around `1.585^p`, with `K = ⌈nL⌉`, of the correct sign, and with approximation quality good enough for the budget of item 1.
   - Convergent denominators `q_m`: available only where the chain has them, with the gaps quantified above.
   - **Semiconvergents** `q_{m−1} + k·q_m`, `k = 1…a_{m+1}`: spaced *additively* by `q_m`, so their consecutive ratios tend to 1 and they blanket any large-partial-quotient gap. Derive their approximation quality exactly — `‖(q_{m−1} + k q_m)L‖` in terms of `θ_{m−1}`, `θ_m` and `k`, with the sign — and the worst case over `k`.
   - **Multiples** `t·q_m`: `|K − nL| = t·θ_m` exactly (the tightening Merle stated in round 11 and we confirmed).
   - **The product to aim at:** a statement of the form *"for every `p ≥ p₀`, the window `[c₁·1.585^p, c₂·1.585^p]` contains an `n` of the correct sign with `n·‖nL‖ ≤ B(p)`"*, with `c₁, c₂, B` explicit and the argument **unconditional** — no assumption on the partial quotients of `log₂3`. Then compare `B(p)` against item 1's budget.
   - If unconditionality fails, say exactly what it fails on, and whether an effective irrationality measure (Rhin 1987, exponent 13.3 — see `briefs/merle-la7-mu-check-findings.md` for the adjudicated citation) repairs it and at what cost in the exponent.

3. **The empirical test, and it is decisive.** Run the existing recipe (12.8.6.2 + 12.8.6.3, `experiments/staircase_allp.py`, unmodified where possible) over **`p = 24…36`**, the stretch that includes the nine-period convergent desert `p = 27…35`, using semiconvergent and multiple candidates.
   - If passers exist throughout, the availability gap is an artifact of how the candidate chain was built, not a fact about `log₂3` — which is the outcome that makes a proof reachable.
   - If some period genuinely resists, **that is the more valuable finding**: record which, why, and what the binding constraint is (availability, quality, or the correction budget).
   - Record the achieved `γ` and `γ/log₂p` at every period, extending 12.8.6.4's table. **Exact big-integer verification of every rotation's `q ≤ R_r`**, and the divisibility check on every constructed instance (expected: all fail, as at 12.8.3 and 12.8.6.4).
   - Fresh verification code, `experiments/staircase_allp_diophantine.py`, written independently; you may re-use the *recipe* but not import its verification.

4. **Attempt the lemma.** With items 1–3 in hand, try to prove the coverage statement of item 2 outright, at the budget of item 1. Standard tools are fair game — three-distance, Ostrowski representation, the classical `θ_{m−1} = a_{m+1}θ_m + θ_{m+1}` recursion, and effective measures where unconditionality demands them.
   - **If it closes, it closes 12.8.6.1** — state the theorem, the proof, and independently written verification code with negative controls, per `AGENTS.md`. Nothing is labeled proved without code that could have failed.
   - **If it half-closes, say so precisely.** "Proved for all `p` outside an explicit finite/computable exceptional set" is a real result and is exactly the shape this problem is likely to yield. So is "proved conditional on an effective measure with exponent ≤ X".
   - **If it does not close, record the obstruction sharply enough that the next session does not repeat the attempt.** A well-characterized wall is the deliverable in that case.

5. **Record** (branch commits, per item):
   - `experiments/staircase_allp_diophantine.py` + committed output.
   - `briefs/staircase-allp-diophantine-findings.md` — the γ budget with the comparison written out; the availability characterization with exact quality formulas; the `p = 24…36` table; the lemma's status (proved / partially proved / obstruction), with the proof or the wall stated in full; and an explicit verdict on **whether the published `thm:staircase` hedge can be lifted, and if so in what wording**. Do not edit `cycles.md` or the paper — recommend, and the main session reviews.
   - `HANDOFF.md` — ONE scoped paragraph, under a new numbered item if item 1 is the wrong home. A sibling session (`staircase-allp-construction`) runs in parallel on the other gap; keep to your own lines.

## Rules

- Branch **`staircase-allp-diophantine`**. Verify your worktree HEAD contains this brief; if not, rebase onto the `main` SHA given in your launch instructions, and state the base SHA in the findings.
- Per-item commits. Do **not** merge — the main session reviews (re-runs the script) and merges.
- **Nothing is labeled proved without independently written verification code. Failures are recorded, not deleted.** `sources/` is immutable.
- No pushes; no interaction with Merle's repositories; nothing for the ledger, the note or the reply.
- Do not edit `cycles.md`, `paper/` or `publication.md`. A status-word change to a published hedge is a main-session decision after review.
- Encoding: Edit/Write tools only, never PowerShell `Get-Content`/`Set-Content`; run `experiments/encoding_scan.py` before your last commit.
- Stop after item 5.
