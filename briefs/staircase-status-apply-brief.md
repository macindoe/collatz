# Brief: apply the staircase status edits — both gates cleared — for a delegated session

**Context required before starting (in order):** `README.md`, `AGENTS.md` (status words, conservative editing, "no change logs in tracked files", `archive/` keeps refuted routes with the evidence that killed them, `sources/` immutable), `cycles.md` §12.8 in full, and the four records this applies: **`briefs/staircase-status-audit-findings.md`** (the inventory and the drafted replacements R1–R13 — your primary source), `briefs/staircase-allp-construction-findings.md` (Theorem B), `briefs/staircase-allp-diophantine-findings.md` (Theorem D, Lemma D), `briefs/staircase-gamma-upper-findings.md` (the `γ` bracket, and the correction to Lemma D's proof).

## Both gates are cleared

**P1 — `γ = O(1)` is proved** (merge `2b9e424`; script re-run at review, byte-identical, 45 checks, 0 failures; the sharp criterion independently re-derived by the main session). The exact statement, and nothing stronger may be written:

> For every `p ≥ 16`, Construction B yields a period-`p` size-passer with **`3.683012 ≤ γ ≤ 5.140212`**, both ends absolute. `3 ≤ p ≤ 15` by explicit exhibition. **`p ∈ {2,4}` lie outside Construction B's reach** — their canonical windows contain no integer.

**P2 — the author's decision: "better specified."** Record the reasoning, because it is what licenses every upgrade below:

- The published v2 sentence describes a **shape** — *"block depths growing geometrically at ratio ≈ log₂3 with unit exit valuations, closed by a single block of unit depth and maximal exit valuation"* — and specifies **no rounding rule**.
- §12.8.6.2's partial-sum rounding recipe entered the wiki at `2c54669`, **after** the paper. The defective approach was never published.
- Construction B matches the printed description **more exactly** than the old recipe did: crash depth **exactly 1** — "a single block of unit depth" — where §12.8.6.2 allowed 1 or 2.
- The published `p = 7` instance **is** a member of the family and passes all seven rotations (verified independently at review). **The family was never mis-specified; the generator was.**

So this is one family throughout, now correctly generated. Say it that way — not "the old family failed."

## What you are doing

**Applying** the audit's proposals. This is the first window in this arc permitted to edit wiki pages, and it edits only what the audit inventoried.

## Queue

1. **Re-verify before you write.** Every number entering prose must be checked at its named place in the four findings files. The audit itself found that two drafted replacements it was told to start from were stale; do not assume its own R1–R13 are error-free either. Where you correct one, say so in the commit message.

2. **Apply in the audit's recommended order**, one commit per group, content separate from structure:
   - §12.8.6 rewritten (the audit's full replacement, all four section numbers keeping their roles);
   - 12.8.3 and the §12.8 preamble;
   - `cycles.md` front matter and Current-state;
   - the pointer pages (`index.md`, `TOUR.md`, `open-problems.md`, `README.md` — README line 17's paragraph, **not** line 34, which the sibling already repaired);
   - `publication.md`.

3. **Status words, exactly.** "Proved" may be written only with the scope above attached — the `p ≥ 16` unconditional range, the exhibited finite tail, `p ∈ {2,4}` outside, and the `γ` bracket. Do not write `O(1)` bare where the bracket is meant, and do not let "for every period" quietly absorb the two excluded ones. Where a hypothesis is consumed (Theorem B's `γ ≥ Γ(p,n)` and (H0)), the page must say the theorem has hypotheses.

4. **Lemma D's proof must be stated at the sharp criterion.** The sufficient-span argument — *"14θ ≥ 1, so 15 points cover the circle"* — reaches a true conclusion by a reason that is not the governing one, and both the audit and the main session used it. The governing condition is `maxgap{jθ mod 1 : j ≤ J} ≤ arc length`, an **iff**: `J = 13` (66 consecutive integers) for the two-sided arc, `J = 12` (61) for the one-sided form, `J = 11` failing both. If any page states the covering argument, state it this way. "71" is valid but neither minimal nor derived — do not print it as if it were.

5. **Supersede, do not delete.** §12.8.6.2's recipe and §12.8.6.3's correction algorithm stay in the page, clearly marked as the superseded route, with the reason they failed — the missing additive offset `1/(L−1)` per block, hence a `Θ(p)` shortfall, hence no `O(1)` or `O(log p)` move bound to be proved. `AGENTS.md` keeps refuted routes with the evidence that killed them, and these are mathematical statements, not a change log. The audit flagged this tension and its resolution is: keep the objects, in place, marked; write no history narration around them.

6. **The correspondent's citation.** Merle cites `12.8.6.1` as "the Diophantine coverage bound". After the rewrite that number resolves to a different statement, so the superseded-formulation paragraph the audit drafted **must not be dropped** — it is what keeps his citation resolvable.

7. **What must not move, and verify by reading rather than assuming:** 12.8.5's strategic conclusion, the parked cycle front, all three README stopping rules, 12.8.1, 12.8.2, 12.8.4, and §12.6.1 (repaired by a sibling this session). This result is sharper evidence that counting cannot do better and **no evidence at all about exclusion**. A status sweep this size is exactly where a stopping rule gets loosened by accident.

8. **Do not touch `paper/` or `sources/`.** The published-record decision stays with the author. **Do** carry forward the audit's drafted erratum text — correcting only the v2 note's identification of the remaining gap, silent on the hedge — into your findings, updated for P2 and for P1's exact constants, marked clearly as **drafted, not applied**.

9. **Verify the result.** Re-run `experiments/encoding_scan.py`. Confirm no section number was renumbered, no cross-reference elsewhere in the wiki now points at a statement that changed meaning (grep for `12.8.3`, `12.8.6`, and each sub-number across the tree), and that every claim you upgraded has a findings file behind it.

10. **Record**: `briefs/staircase-status-apply-findings.md` — what was applied where, every deviation from the audit's drafts with its reason, the cross-reference sweep, the drafted erratum, and anything you left undone. Plus ONE scoped `HANDOFF.md` paragraph consolidating this arc's state.

## Rules

- Branch **`staircase-status-apply`**. Verify your worktree HEAD contains this brief; if not, rebase onto the `main` SHA in your launch instructions, and state the base SHA.
- Per-item commits. Do **not** merge — the main session reviews and merges.
- Math statements are edited conservatively: do not improve a proof while doing status work, do not renumber, and keep every fact in exactly one page with the others pointing at it.
- No pushes. Nothing for the ledger, the shared repo, or the reply — the reply is the next window and explicitly not yours.
- Encoding: Edit/Write tools only, never PowerShell `Get-Content`/`Set-Content`; run the scan before your last commit.
- Stop after item 10.
