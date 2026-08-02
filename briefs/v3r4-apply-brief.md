# Brief: apply round 4 (v3 round 4, the whole apply phase)

**Branch.** `v3r4-review-round4`, at `6ead133` (design phase committed; `main` is `fa9edf5`). Work directly in `c:\Users\Ace\Documents\Collatz` on that branch. **Do not create a worktree.**

**This is an edit task.** The design is settled and the author has ruled. You land it — record first, then the paper, then the pin. Where you believe a drop-in is wrong, stop and report; do not improvise a third version.

**Round 4 is a subtraction.** The reviewer's framing, and the author's instruction. The paper and the record should say *less* about what AEH supplies when you are done, not more. One item adds — `13.2.4`(g), below — and it is an unconditional theorem the reviewer explicitly asked for.

## Read first

- `briefs/v3r4-clock-findings.md` — the design. Its Option 1 drop-in text is what you are landing. Read its consequence trace in full; it lists every site.
- The **current** text of every section before you edit it. Round 3 rewrote most of §13 and several claims in the round-3 findings files are already stale. Cite files, not findings documents.

## What lands

**1. The blocker, Option 1 — AEH stays purely distributional.**

- `aeh.md` L84, the consistency bullet: the claim that zero cemetery mass "is exactly `E_B[m+r] = 4` in Cesàro form" fails and is restated. A vanishing *frequency* of `†` is not a bound on a *sum* over its complement.
- `aeh.md` L86–90, the two-range table: the row survives as arithmetic; the annotation "the divisor `4` is `13.2.1`'s own content" fails.
- `aeh.md` L8, L67, L116; `paper` L246, L322–329, L385–387, L394; `publication.md` L29, L41 — restated per the findings.
- Throughout: "all of them within budget" becomes "all but `o(T_N)` blocks within budget", and nothing says AEH converts Inselmann's endpoint into blocks per bit.

**2. `13.2.4`(g) — the one addition.** The below-budget result: taking the budget as the cylinder cutoff, the two clauses of admissibility are exactly the two terms of the base case's total-variation bound, so `P(S_{T_N} ≥ Λ_N) → 0` *and* the exponent mean converges to 4, unconditionally, for every `θ < 1/4`. This is simultaneously the reviewer's missing cemetery-budget step and the conversion, restricted to where it is a theorem. **Corollary `13.2.4.1` needs it and needs to quantify over `τ`** — it currently claims the cemetery form for every admissible `(τ, θ)` with `τ < 1` without either.

**3. The three smaller corrections.**

- `aeh.md` L83, the Inselmann ceiling: "No `τ ≥ 4.8188…` is protected", "sharp rather than a gap in technique", and "above the ceiling there is no orbit left to sample" are none of them supported by the source. Restate to what the theorem gives — protection for every `τ < 4.8188…`, and a scope decision above it.
- `13.2.4`(a) prints `P_B(S_(n+1) ≥ J)`; the sharp and correct form is `P_B(S_n ≥ J)`.
- `13.2.3`'s "The gap is `O(1)`" — the two exponent counts differ by one unbounded geometric letter at each end, so it is `O_P(1)` with geometric tails. Negligible against `log N`, but not deterministic.

**4. `13.6.4`'s union bound.** The residual cell `{σ_n ≥ D} ∪ {s_{n+1} ≥ D}` is given "`π_{k,D}`-mass `(D+1)·2^{−(D−1)}`". That double-counts the intersection; under the stated independence the exact mass is `(D+1)·2^{−(D−1)} − D·2^{−2(D−1)}`. The printed figure is a valid union bound and the proof is unaffected, so **change "of mass" to "of mass at most"** — or print the exact expression, your call, but say which you did and why.

## What does NOT land — and where it goes instead

The design delegate derived a **prefix result**: quantifying over every admissible pair and letting `τ ↓ 4θ` pins the exponent mean of the in-budget prefix, yielding a conditional block drift there, with the deficit confined to the budget-exhausting block and the cemetery tail. It also found that this would rescope `13.3.2`'s first reason.

**The author has deferred both.** Its hinge — how tightly `τ` may approach `4θ` — is unsettled, and its supporting clause is unmeasured. Round 4 does not claim it.

So: **leave `13.3.2` exactly as it stands.** As written it is conservative and true; it is merely not the sharpest available statement, and the sharper one is unproved.

Record the deferred material in `open-problems.md`, per `AGENTS.md` ("new open questions → `open-problems.md`, phrased so that closure is checkable"), as **two** checkable items: whether `τ ↓ 4θ` is legitimate and what the prefix result then gives; and that **if** it holds, `13.3.2`'s first reason needs rescoping. Claim neither. Point at `briefs/v3r4-clock-findings.md` for the drafted argument so the work is not lost.

## The paper, and the pin

After the record is committed:

- Apply the paper sites listed above. **Do not prune** — the author has deferred the reviewer's pruning plan to a separate round. Do not cut content to reduce pages.
- **Re-pin Appendix A.** It names `677a76a`, which predates round 3's own corrections at `276b87c` — a reader following the pin to check `13.2.4` or `13.6.4` reaches pre-correction proofs. Commit the record and paper first, then re-pin to the commit containing them, then commit the pin change alone, as `3511a0d` and `643e864` did. Before committing, verify the claim: does that commit contain every `aeh.md` section and script the paper names, in its corrected form?
- Rebuild: three `pdflatex -halt-on-error` passes. Report each pass, box warnings, unresolved references, and the page count. Confirm from the built PDF's extracted text that the changes are present in the artifact.

## Constraints

- **Branch `v3r4-review-round4` only.** You may `git add` and `git commit`. **No push, no merge, no rebase, no branch switching, no worktree.** If a commit is refused, stop and report.
- Write files with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes this repo's `≤`, `—`, `ε`. Confirm they still render after editing.
- No change logs, dated journals, or "was X, now Y" prose in any tracked page.
- Do not renumber any monolith anchor. `13.2.4`(g) appends to an existing lemma; add no others.
- **No numbered theorem's claim may be strengthened, weakened, or renumbered** in the paper.
- Every number and section reference verified against the file, not recalled. Note the design findings corrected the brief's own line numbers once already.
- **Do not fix anything not on this list.** Report it instead.

## Deliverable

The edits committed, plus `briefs/v3r4-apply-findings.md`: the site-by-site table with any deviation and its reason, what you did about the `13.6.4` wording, the two `open-problems.md` entries as landed, the build report, the pin commit and your verification of its claim, and anything you found and did not fix.

Your final message: what landed, the build result and page count, the pin, and anything you stopped on.
