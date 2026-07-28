# Brief: what the all-`p` closure retires — a status audit of the wiki and the published record — PROPOSALS ONLY — for a delegated session

**Context required before starting (in order):** `README.md` (binding stopping rules), `AGENTS.md` (layers, status words, "math statements are edited conservatively", "no change logs in tracked files", `sources/` immutable), `cycles.md` §12.8 in full, and **the two results this audit is about**: `briefs/staircase-allp-construction-findings.md` (Theorem B — Construction B, no correction step, `γ = O(1)`) and `briefs/staircase-allp-diophantine-findings.md` (the γ budget, the availability results, and Theorem D — unconditional coverage for every `p ≥ 16`). Also `briefs/staircase-allp-findings.md` (the superseded floor-grade attempt) and `publication.md`.

## What happened, and why this session exists

Two delegated sessions closed both halves of the all-`p` staircase sharpness question, and the main session verified the load-bearing parts independently at review (Lemma D re-derived from scratch; the Theorem D → Theorem B composition re-checked at `p = 16…28` in an independently written evaluator, 0 failures). Merges `e42d785` and `da5f06d`.

Together they compose into a proof of what `cycles.md` 12.8.3 and the published `thm:staircase` both carry as **assessed, not proved**, and they prove it at `γ = O(1)`, which is **stronger** than the published `O(log p)`. Coverage: every `p ≥ 16` unconditionally, `p ≤ 15` by direct finite check, except `p ∈ {2,4}` which lie outside Construction B's own reach and are covered by direct exhibition.

Our record has not moved a word. It currently says, in several places, things that are now wrong, stale, or understated — and one of those places is a **published** artifact, which changes what "fix it" can mean.

**This session proposes; it does not edit.** No file in the repository is modified except your own findings and one HANDOFF paragraph. Every proposal is a quotation of the current text plus a drafted replacement, for the main session and the author to weigh.

## The standard the proposals must meet

- **Status words are load-bearing.** `proved`, `assessed`, `verified`, `heuristic`, `floor grade` mean specific things here. A proposal that upgrades a word must say exactly which theorem licenses the upgrade and what its hypotheses are.
- **State the scope honestly, including the holes.** `p ∈ {2,4}`, the `p ≤ 15` finite check, `Γ`'s conservativeness, and the fact that verification stops at `p ≈ 32` on big-integer cost are all part of the true statement.
- **Conservative editing.** Do not improve a proof while doing status work; do not renumber; every fact lives in exactly one page and the others point at it.

## Queue

1. **Sweep the whole tracked tree** for every statement the two theorems make wrong, stale, or understated. Do not guess at the list — search. Start from, and go beyond: `cycles.md` (the Current-state paragraph at the top, 12.8 preamble, 12.8.3, 12.8.5, and all of 12.8.6 including 12.8.6.1's status paragraph, 12.8.6.2, 12.8.6.3, 12.8.6.4 and the "Achieved grade" paragraph), `README.md` (the scoreboard and the strategy/stopping-rules section), `index.md`, `open-problems.md`, `program.md`, `spine.md`, `publication.md`, `HANDOFF.md`, `TOUR.md`, and any `briefs/` or `viz/` text that states the claim's status. Produce a **table**: file, location, current text quoted verbatim, verdict (RETIRE / UPDATE / UNAFFECTED / UPGRADE), and why.

2. **For each RETIRE or UPDATE, draft the replacement.** Match the page's register exactly. Two items are already drafted for you in the sibling findings and should be used as the starting point, not re-invented: `briefs/staircase-allp-diophantine-findings.md` §5(b) (the v2 note's replacement text) and §6.7 / §5(c) (12.8.6.1 restated at the new interface, with the convergent-run framing kept as **superseded rather than deleted**, since the published note points at it).

3. **The three specific recalibrations the sibling sessions named.** Carry each into a concrete proposal:
   - 12.8.6's "Achieved grade: floor" paragraph and the sentence *"the sole remaining gap in this floor-grade result is the Diophantine coverage bound of 12.8.6.1"* — wrong twice over now.
   - 12.8.6.4's band `γ/log₂p ∈ [1.828, 3.643]` — should be described as what the recipe produced, not as a property of the family; passers exist at `γ/log₂p ≈ 0.46…0.65`, i.e. `γ` roughly constant.
   - Algorithm 12.8.6.3 — **removed from the argument**, not bounded. Propose whether it stays in the page as the historical route (clearly marked superseded) or goes; recommend one and say why.

4. **The published record, and be precise about what is possible.** `paper/collatz-reduced-v2.tex` corresponds to a **published artifact** (v2, DOI 10.5281/zenodo.21421120); the PDFs and `sources/` are frozen. So determine and state plainly:
   - Exactly which published sentences are now superseded — quote them (`thm:staircase`, its hedge clause, the abstract's dichotomy sentence, and the v2 note).
   - Which are *wrong* versus merely *understated*. A hedge that says "not proved here" is not falsified by a later proof; a note that misidentifies the remaining gap **is** now incorrect.
   - The options, with a recommendation: leave the published record alone and carry the update in the wiki only; publish an erratum; or prepare a v3. Say what each costs and what a referee would expect. **Do not edit `paper/` or `sources/`.**
   - Note for the author's judgment, without deciding it: Construction B is 12.8.3's own shape — geometric climb at ratio ≈ `L`, unit exits, one crash block — with the additive offset `1/(L−1)` it was always missing. Whether the published sentence's "staircase family" is therefore *the same family better specified* or *a different family* is the question that decides whether the published claim can be restated. Lay out the case each way; do not adjudicate.

5. **What does NOT change, stated explicitly.** 12.8.5's strategic conclusion, the cycle front staying PARKED, and the README stopping rules are unaffected at any grade — this is sharper evidence that counting cannot do better, and no evidence at all about exclusion. Confirm that by reading, not by assumption, and record it; a status sweep of this size is exactly where a stopping rule gets loosened by accident.

6. **Ordering and risk.** Recommend the order the edits should be applied in, which are safe mechanical status changes and which are substantive mathematical restatements needing their own review, and what a reviewer should re-check for each. Flag any proposal where you are less than confident.

7. **Record** (branch commits, per item):
   - `briefs/staircase-status-audit-findings.md` — the sweep table; every drafted replacement in full; the published-record analysis with its options and recommendation; the explicit unaffected list; the application order.
   - `HANDOFF.md` — ONE scoped paragraph. A sibling session (`record-defects-repair`) runs in parallel on two unrelated defects; keep to your own lines.

## Rules

- Branch **`staircase-status-audit`**. Verify your worktree HEAD contains this brief; if not, rebase onto the `main` SHA in your launch instructions, and state the base SHA.
- **PROPOSALS ONLY. Do not edit `cycles.md`, `README.md`, `index.md`, `open-problems.md`, `program.md`, `spine.md`, `publication.md`, `TOUR.md`, `paper/` or `sources/`.** The only files you write are your findings and your HANDOFF paragraph.
- Per-item commits. Do not merge; the main session reviews and merges, and the author decides what is applied.
- No pushes; no interaction with Merle's repositories; nothing for the ledger, the note or the reply — what goes to Merle is a later decision and explicitly not yours.
- Encoding: Edit/Write tools only, never PowerShell `Get-Content`/`Set-Content`; run `experiments/encoding_scan.py` before your last commit.
- Stop after item 7.
