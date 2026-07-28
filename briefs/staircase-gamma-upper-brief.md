# Brief: gate P1 — prove the `γ` upper bound, so `γ = O(1)` stops being an assertion — for a delegated session

**Context required before starting (in order):** `README.md`, `AGENTS.md`, `cycles.md` §12.8, and the three records this closes over: `briefs/staircase-allp-construction-findings.md` (Theorem B and `Γ(p,n)`), `briefs/staircase-allp-diophantine-findings.md` (§6.3 Lemma D, §6.4 Theorem D), and `briefs/staircase-status-audit-findings.md` (the flag this brief exists to discharge — its "less confident" item 1).

## The gap, stated precisely

Both staircase sessions assert **`γ = O(1)`** for the constructed family. Neither proves it, and the status audit caught this.

What is proved: Theorem D delivers, in every scale window, an `n` with `δ := ⌈nL⌉ − nL` **small** — hence `γ(n) = −log₂(1 − 2^{−δ})` **large** — which is exactly what Theorem B's hypothesis `γ(n) ≥ Γ(p,n)` requires. That is a **lower** bound on `γ`, and it is one-sided.

What is *not* proved: any **upper** bound on the `γ` of the witness actually produced. And a size-passer with large `γ` is a **worse** witness, not a better one — sharpness wants `γ` small. The exposure is real and visible in our own end-to-end table: at `p = 26` the first `n` the pigeonhole supplies has `δ ≈ 10⁻⁵` and `γ = 17.06`.

So the claim that the family achieves `γ = O(1)` — the claim that makes this result *stronger* than the published `O(log p)` — currently rests on a table, not a theorem.

## The route the audit proposed, and what remains to check

Replace the one-sided target with a **two-sided arc**: require `δ ∈ [δ_lo, δ_hi]`.

- `δ_hi = 0.116939` is forced from above by `sup_p Γ(p, 1.05·L^p) = 3.683012` — it is the largest `δ` still meeting Theorem B's hypothesis.
- Any `δ_lo > 0` bounds `γ` above by `−log₂(1 − 2^{−δ_lo})`.
- The pigeonhole of Lemma D needs the arc **longer than `θ = 8 − 5L = 0.0751874964…`**.

The audit's instance, which the main session re-derived independently: `[0.04, 0.116939]` has length `0.076939 > θ` with margin `0.00175`, giving **`3.6830 ≤ γ ≤ 5.1926` uniformly in `p`**; brute force to `n = 3·10⁶` gives a worst run of 16 against the proved bound of 71.

**That is a sketch verified numerically, not a proof, and the margin is thin.** What this session must settle:

1. **Do it in exact arithmetic.** The margin is `1.75·10⁻³` and `δ_hi` is itself a rounded decimal. Redo the whole chain in exact or certified-interval arithmetic: `sup_p Γ`, the induced `δ_hi`, `θ`, the arc length, and the resulting `γ` bounds. A proof whose margin depends on a truncated decimal is not a proof. If the exact `sup Γ` forces `δ_hi` slightly below `0.116939`, say so and carry the exact value.
2. **The `(H0)` interaction at the smallest `p`, which the audit explicitly did not check.** Theorem B needs (H0) as well as `γ ≥ Γ`. Verify (H0) holds for the `n` the two-sided pigeonhole supplies, at every `p ≥ p₀`, and establish `p₀` honestly.
3. **State `p₀` and the finite tail.** Theorem D covers `p ≥ 16` because the window holds ≥ 71 integers there. Under the two-sided condition, re-derive the window-size requirement — it may move. Then `p < p₀` by explicit finite check, recording which periods are covered by exhibition and that `p ∈ {2,4}` lie outside Construction B's reach.
4. **Optimize, and report the honest constant.** `δ_lo` may be taken just above `δ_hi − θ`, which is the best possible under this method; that gives the smallest achievable upper bound on `γ`. Report the optimum. Also check whether using `Γ(p,n)` exactly rather than its supremum widens the arc at large `p` and improves the constant — and whether the improvement is worth the extra clause.
5. **Consider whether a better `γ` is reachable at all**, briefly and without opening a new front: the true minimum `γ` over passers at each `p` is a different question from the minimum this *method* certifies. Record what the existing tables show and stop; do not launch a search.

## The verification the claim has to carry

`experiments/staircase_gamma_upper.py`, fresh code, exact big-integer / exact-rational arithmetic:

- The pigeonhole in exact arithmetic across the certified `p` range.
- **End-to-end**: for a spread of `p ≥ p₀`, take the `n` the two-sided argument guarantees, confirm `Γ(p,n) ≤ γ(n) ≤ C` and (H0), run Construction B, and verify **all `p` rotations' `q ≤ R_r` in your own evaluator** — note the σ convention is `σ_j = s_j + m_{j+1}`, now defined in Prop 12.6.1 and canaried in `experiments/record_defects_check.py`. Confirm every instance **fails** `q | R_r`.
- **Negative controls, required:** an arc shorter than `θ` must exhibit an empty maximal gap (the pigeonhole genuinely fails); an `n` with `δ` below `δ_lo` must give `γ` above the bound; an `n` with `δ` above `δ_hi` must fail Theorem B's hypothesis. A bound that never bites has not been tested.

## Record

`briefs/staircase-gamma-upper-findings.md` — the theorem with its exact constants, the proof, `p₀` and the finite tail, the (H0) verification, the optimized constant, the verification table and the negative controls; and a plain verdict: **is `γ = O(1)` now proved, and with what constant and what scope?** Plus `experiments/staircase_gamma_upper.py` + committed output, and ONE scoped `HANDOFF.md` paragraph.

## Rules

- Branch **`staircase-gamma-upper`**. Verify your worktree HEAD contains this brief; if not, rebase onto the `main` SHA in your launch instructions and state the base SHA.
- Per-item commits. Do not merge; the main session reviews (re-runs the script) and merges.
- **Do not edit `cycles.md`, `README.md`, `publication.md`, `paper/` or `sources/`.** The status edits are gated on this result and are a later, separate window. `sources/` is immutable.
- Nothing is labeled proved without verification code that could have failed. If the two-sided route does **not** close — if the exact arithmetic eats the margin, or (H0) fails at small `p` — say so plainly and state what the honest claim is instead (`γ = O(1)` for `p ≥ p₀` only, or a weaker constant, or a bound with an exceptional set). A correct weaker statement is the deliverable in that case.
- Stopping rules: this is the same negative structural result about size arguments; size-passers only, never cycles; the cycle front stays PARKED and 12.8.5 is unaffected.
- No pushes; nothing for the ledger, the note or the reply.
- Encoding: Edit/Write tools only, never PowerShell `Get-Content`/`Set-Content`; run `experiments/encoding_scan.py` before your last commit.
