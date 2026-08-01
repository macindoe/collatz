# Brief: the AEH sample space and limiting procedure (v3 round 2, blocking finding)

**Round.** Second external review of the unpublished `paper/collatz-reduced-v3.tex`, reviewed at `e4dac49` (= current `main`). Two of the first round's three blockers are repaired. This one is not, and it is the round's only true blocker.

**This is a design task, not an edit task.** Produce text; change nothing.

## The finding

The reviewer, on Hypothesis~\ref{hyp:aeh} (`paper/collatz-reduced-v3.tex` L241–247):

> The revised hypothesis takes orbit length → ∞ first and X → ∞ second. But for any convergent orbit: above a fixed cutoff X, there are only finitely many qualifying visits; once X exceeds that orbit's maximum, there are no qualifying visits. Thus the empirical distribution either freezes as a finite sample or becomes undefined. It cannot converge to π_k. If Collatz is true, the literal hypothesis fails for every starting state.
>
> The explanatory paragraph actually notices the problem — "a given orbit need not supply a growing set of qualifying visits" — but then claims the cut makes the hypothesis nondegenerate. It does the opposite under the stated iterated limit.
>
> The clean repair is an ensemble formulation matching the calibration protocol: uniformly sampled large starting values, a specified fixed/growing horizon, per-visit weighting, and an explicit order of limits. Retaining a single-orbit formulation would require conditioning on infinitely many bulk visits, which would no longer support the claimed contraction consequence.

This is correct, and it was half-seen already: `briefs/v3-external-review-corrections-findings.md` item 3 (L306) recorded the same degeneracy and left it. Last round then *added* the explicit limit order, converting a vague statement into a demonstrably empty one. Do not treat the previous round's wording as a constraint.

## Scope: this is not confined to the paper

`aeh.md` Theorem 13.6.4 (L101) defines its bulk frequency "in the limit orbit length → ∞ then X → ∞ (exactly `13.2.1`'s regime)". The same defect. Any repair must land in three places at once — the paper's Hypothesis, `aeh.md` 13.2.1, and 13.6.4's bulk-frequency definition — or the record becomes self-contradictory again.

## Read before deciding

- `aeh.md` §13 entire. Especially: 13.1 (two regimes), 13.2 + Hypothesis 13.2.1, 13.3.1–13.3.3 (the conditional consequences), 13.4 (calibration protocol), 13.5 (the standing rule: fixed-horizon, unweighted, per-visit sampling from uniform starts — ratio estimators forbidden), 13.6.3(v) (the product law under `B`), 13.6.4 + its (q1)/(q2) qualifications, 13.6.5, 13.6.6 (the nondegeneracy paragraph the reviewer is contradicting), 13.6.7.
- `paper/collatz-reduced-v3.tex` L237–256 (all of Section 5), plus L247 specifically.
- `experiments/aeh_calibration.py` and `experiments/aeh_anomaly.py` — what the campaign actually sampled.

Note the strongest single piece of evidence for the reviewer's recommendation: §13.5's standing rule already *is* an ensemble protocol. Every number in the calibration record was measured under uniform large starts at fixed horizon with per-visit pooling. The hypothesis as stated has never been the thing we measured.

## The task

Settle the formulation. Default to the ensemble form; deviate only with an argument. Whatever you choose must specify, explicitly and unambiguously:

1. the sample space (what is drawn, from where);
2. the horizon (fixed? growing with the sampling scale? at what rate?);
3. the weighting (per-visit, per-orbit — §13.5 forbids one of these for a reason);
4. the bulk cut's role, and whether it survives at all under an ensemble form;
5. the order of every limit, with each one non-degenerate at the point it is taken.

**Then trace the consequence chain. This is the part that matters most.** For each, state whether it survives verbatim, survives restated, or fails:

- 13.3.1 (ledger with error `O(2^-k)`);
- 13.3.2 (3-gain rate exactly 1/3, and the drift);
- 13.3.3 (the scope discipline: "even in full, AEH yields almost-everywhere statements only", staircase tails not excluded);
- the paper's L247: "AEH implies the ledger with error `O(2^{-k})` … and almost-everywhere contraction". The reviewer explicitly warns the contraction consequence is at risk. An ensemble statement about sampled starts is not *prima facie* a per-orbit almost-everywhere statement — say plainly what it is and is not;
- 13.6.4's equivalence theorem, which is proved **orbit by orbit** with no measure on starting values. If 13.2.1 becomes an ensemble statement, what is 13.6.4 now an equivalence *between*? It may need to be restated as a per-orbit property that the ensemble form quantifies over. Work this out; do not wave at it;
- 13.6.6's claim that "the bulk cut is precisely what makes the integer question nondegenerate" — the reviewer says it does the opposite. Adjudicate.

If the honest answer is that the ensemble form also fails to support contraction as claimed, say so. A round that discovers the consequence must be weakened is a successful round. Do not manufacture a repair that preserves the conclusion by vagueness — vagueness is what got us here.

## Deliverable

Write **only** `briefs/v3r2-aeh-formulation-findings.md`, containing:

1. the recommended formulation, with reasoning, and the rejected alternatives with why;
2. **exact drop-in LaTeX** for the paper's `hypothesis` environment and its following explanatory paragraph — ready to paste, matching the surrounding prose register;
3. **exact drop-in Markdown** for `aeh.md` Hypothesis 13.2.1 and for 13.6.4's bulk-frequency definition sentence;
4. any consequential rewording L247 and §13.3 require, as drop-in text;
5. a plain list of everything that breaks or weakens, stated without hedging;
6. anything you could not settle, named as an open question rather than smoothed over.

## Constraints

- **Read-only on every tracked file.** The one file you may write is your findings file. No edits to `aeh.md`, the `.tex`, or any other page — those are Phase 2, by a different delegate.
- No `git` write operations of any kind: no commit, no branch, no checkout, no push. You are working directly in `c:\Users\Ace\Documents\Collatz` on `main`.
- Write files with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes this repo's `≤`, `—`, `ε` and silently corrupts the wiki pages.
- Do not renumber any monolith anchor (`13.2.1`, `13.6.4`, …). They are stable citation targets (`AGENTS.md`).
- No change logs, no dated journals, no "was X, now Y" prose in anything destined for a tracked page (`AGENTS.md`). Your findings file is a working document and is exempt.
- Numbers, section numbers and quoted values must be verified against the files, not recalled.
