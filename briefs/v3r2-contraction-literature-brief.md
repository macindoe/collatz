# Brief: does AEH's contraction consequence sit below the unconditional literature? (v3 round 2, gate on L247)

**Round.** Second external review of the unpublished `paper/collatz-reduced-v3.tex`. This brief exists because the AEH reformulation (`briefs/v3r2-aeh-formulation-findings.md`) restated the paper's contraction consequence into a form that may already be known unconditionally. Nothing about the paper's AEH section can be finalized until this is settled.

**This is a literature check, not an edit task.** Produce an answer; change nothing.

## The question

The paper (L247) currently claims:

> AEH implies the ledger with error $O(2^{-k})$ via Theorem~\ref{thm:onestep}, the exact $\tfrac13$ rate, and almost-everywhere contraction

The reformulation establishes that "almost-everywhere contraction" is not a per-orbit almost-everywhere statement and never was. Restated, the consequence is approximately:

> for every `ε, θ, k` there is a set `E` of natural density `0` such that every starting value `x ∉ E` has its first `⌈θ log₂ x⌉` bulk window-state frequencies within `ε` of `π_k` — and, subject to a uniform-integrability rider that is *not* derived, almost every starting value in natural density descends below `x^η` within `O(log x)` blocks.

`briefs/v3r2-aeh-formulation-findings.md` §9 item 1 flags: this is "the same genre as the unconditional density theorems (Terras 1976; Korec's `x^{0.7924}`; Tao's logarithmic-density result reaching almost-bounded values)", and declines to adjudicate it.

**Settle it.** Is the *conditional* conclusion weaker than, comparable to, or incomparable with what is already proved *unconditionally*?

## Read the repository first — do not re-do work already done

- `publication.md`: the novelty sweep, especially the "2024–26 landscape" section and the claim-by-claim verdicts. It already surveys the classical foundations and pins several citations. Establish what the project has already adjudicated before searching outward.
- `briefs/v3r2-aeh-formulation-findings.md` §3, §3.1, §4, §7, §9 — the exact restated statement you are comparing. Do not compare against a paraphrase; use the statement as written there.
- `paper/collatz-reduced-v3.tex` L237–259 (Section 5 entire), L59 (Related work), and the bibliography at L265–278.
- `aeh.md` §13.3.1–13.3.3.
- `sources/` — check whether any relevant paper is already held locally before fetching.

## The external work

Use web search and fetch. Establish, with precise statements and sources:

1. **Terras (1976)** — already cited as `\bibitem{terras}`. What density statement does it actually prove (stopping time / a.e. descent below the start), and in which density?
2. **Korec** — the `x^{0.7924}` result. Exact statement, year, venue, and which density.
3. **Tao (2019/2020)**, *Almost all orbits of the Collatz map attain almost bounded values*. Exact statement, the density used (logarithmic), and what "almost bounded" means.
4. Anything else in that line that supersedes or sharpens these — check whether Tao's result has been strengthened since.

Natural versus logarithmic density is **not a detail here.** A statement in natural density and one in logarithmic density are not directly comparable in either direction; establish exactly which each result uses and what that implies for the comparison.

## What to deliver a verdict on

1. **Is the restated AEH consequence already known unconditionally?** Answer for the contraction half specifically. If it is subsumed, say so plainly — that is a useful finding, not a failure.
2. **Is the ledger half (frequency of `s` values, the `1/3` 3-gain rate) also subsumed?** Terras-type results concern descent, not per-step frequency laws; check whether the frequency statement is separately known.
3. **Should the paper cite Korec and/or Tao, and where?** Related work (L59), the AEH section, or both. Draft the `\bibitem` entries and the sentence(s) that would cite them, in the paper's existing register.
4. **Natural or logarithmic density for the restated statement?** The reformulation uses natural density because that is what the dyadic sampler realises and what makes its base-case argument exact; §5.7 there notes log-density is an acceptable variant and a one-line change. Recommend one.
5. **Does anything here change how the AEH section should be framed?** If the conditional consequence is weaker than the unconditional state of the art, the honest framing is that AEH's value lies in the *exactness of π_k and the per-step laws*, not in the descent consequence. Say so if that is where the evidence points.

## Deliverable

Write **only** `briefs/v3r2-contraction-literature-findings.md`, containing: the precise statement of each external result with its source and density; the comparison verdict for each of the five questions above; draft `\bibitem` entries and citing sentences if citations are warranted; and an explicit list of anything you could not establish from accessible sources.

Distinguish throughout between what you verified from a primary source, what you took from a secondary description (abstract, survey, encyclopedia entry), and what you could not confirm. Do not state a theorem's exact form from memory — if you cannot get the statement from a source, say so.

## Constraints

- **Read-only on every tracked file.** The one file you may write is your findings file.
- No `git` write operations of any kind — no commit, branch, checkout, stash, or push.
- Write with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes this repo's `≤`, `—`, `ε`.
- Do not edit the bibliography, the `.tex`, or any wiki page. Phase 2 applies.
