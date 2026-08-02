# Brief: the round-3 fix wave (v3 round 3, Wave 5b, final production step)

**Branch.** `v3r3-review-round3`, at `df9e5e6`. Work directly in `c:\Users\Ace\Documents\Collatz` on that branch. **Do not create a worktree.**

**This is an edit task and the last one in the round.** After you, the main session reviews the full diff and the author decides the merge. Everything below is already adjudicated — you are landing it, not re-deciding it.

## Inputs

- `briefs/v3r3-verify-findings.md` — the defect list D1–D12 and the biased-number audit. This is your primary work order.
- `briefs/v3r3-tailbound-findings.md` — the derivation, its drop-in text, and **its Appendix A, which contains a verification script you must land**.

Read the **current** text of every section before editing it. This round rewrote most of §13.2 and §13.6, and several claims circulating in this round's earlier findings files are already stale. Cite files, not findings documents.

## Order of work

Land in this order, committing in coherent units:

**1. The record fixes.**

- **D5 + the tail bound.** Land `briefs/v3r3-tailbound-findings.md`'s two **required** drop-ins: `aeh.md` L178 (`13.6.3`(iv), full paragraph) and L30 (§13.2's relocation clause, which is wrong that the bound is consumed only by `13.6.4` — `13.2.4`(e) consumes it too). Then land its two **optional** drop-ins at L101 (`13.2.4`(e)) and L199 (`13.6.4`(⇒)), which replace `2L(0.93)^W` with the sharper `(L/3)(5/6)^(W−1)`. **The optional pair must land together or not at all.** If either fails to apply cleanly against the current text, land only the required two and report. Separately, complete the `13.6.4`(⇐) parenthetical per verify's D5: it is true and was necessary, but still needs the cap-to-infinity step against the tail cell, which the (⇒) direction spells out and (⇐) does not.
- **Land the verification script.** `13.6.3`'s verification line names `experiments/aeh_tailbound.py`, which does not exist — the tail-bound delegate was barred from writing it. Its full source is in Appendix A of that findings file. Create it, **run it**, and confirm its output matches the verification line before committing. Header must state which page and result it supports (`AGENTS.md`). Until this lands, `13.6.3` is out of compliance.
- **D2.** `README.md` L40 is stale on all three headline corrections: "the exact product law", "Bulk uniformity stands unqualified at all tested depths", "a density-zero set of starting values".
- **D3.** `bridge.md` §16.4.3 still says "uniformity stands unqualified" with no ceiling.
- **D4.** The front matter says the base case is **PROVED**, which triggers `AGENTS.md`'s status-change workflow. Steps 2–4 were skipped: `stage1.md` 11.8.4.5 still lists the ledger as heuristic; `open-problems.md` L84 still poses it as open (add a calibration note pointing to the closure, per the workflow — do not delete the entry); `index.md` L46 does not mention the base case.
- **D7.** `13.2`'s "23 of its 30 tallied blocks" measures 22.0 under the page's own accounting. Verify the arithmetic yourself, then correct it.
- **D8.** The complement slip: the statistic is the density of the pattern where a block *ends* (odd then even), not where it continues. Two sites — `aeh.md` §13.3.2 and `publication.md` item 4. Both values are one-half and both are pair statistics, so no argument changes; only the naming is wrong.

**2. The two biased-protocol numbers.** Verify's audit shrank the list to two entries: `13.6.5`'s visit count, and `P(d=2) = 0.3192`, whose cut-free value it computed as `0.3185`. The chain rejection, the `L¹ ≤ 0.006` and the `a₊ = 0` cell were all bounded and survive cut-free. **Re-run the adjudication cut-free** with the existing script and, if the values confirm, update those two and state the protocol. **This is the only measured value the round changes — if anything is ambiguous, change nothing and report.** Do not adopt another delegate's computed number without reproducing it.

**3. The paper fixes**, after the record is committed.

- **D1**, the one that would otherwise ship. `\cite[Remark 1.13, footnote 4]{tao}` names a footnote that is version-dependent: in the printed *Forum Math. Pi* version (= arXiv v5) footnote 4 of Remark 1.13 is the Wirsching/Thomas pointer, and the "ancient iteration" text is footnote 4 only from v6–v7. Pin the version so the locator is true of the reference the paper prints. Verify flagged that it could not check Cambridge's text directly, so state in your findings what your fix assumes.
- **D10.** The paper prints `z = 41` and "1,600–2,600 orbits per cell" without the qualifier the record now carries.
- **D9.** The paper-apply findings claimed the version note carries no "was X, now Y" prose; it does, in four places. A version note is the right genre for that, so **the text is fine and the self-assessment was wrong** — correct the record of it in your findings, change no prose on that account.
- Rebuild: three `pdflatex -halt-on-error` passes. Report each pass, all box warnings, unresolved references, and the page count. **No length mandate — the author has ruled: correctness first, do not cut content.** Commit the rebuilt PDF with the source.

**4. The Appendix A pin, as a separate final commit.** The pin currently names `b278e5a`, whose `paper/` still prints the old pin. Earlier rounds solved this with a follow-up commit (`643e864` then `3511a0d`). So: commit everything above first, note that commit's SHA, then update the pin to it and commit that change alone. Before committing, **verify the claim**: does that commit contain every `aeh.md` section and every script the paper names?

## Constraints

- **Branch `v3r3-review-round3` only.** You may `git add` and `git commit`. **No push, no merge, no rebase, no branch switching, no worktree.** If a commit is refused, stop and report.
- Write files with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes this repo's `≤`, `—`, `ε`. Confirm they still render after editing.
- No change logs, dated journals, or "was X, now Y" prose in any tracked page. The paper's version note is the one place that genre belongs.
- Do not renumber any monolith anchor. The round has added five (`13.2.2`–`13.2.5`, `13.2.4.1`); add none.
- Every number verified against the file or recomputed, not recalled.
- **Do not fix anything not on this list.** If you find something new, report it; the round has had five waves and unscoped edits are how a defect enters unreviewed.

## Deliverable

The edits committed, plus `briefs/v3r3-fix-findings.md`:

1. item-by-item disposition of D1–D10 and the tail-bound drop-ins: what landed, what did not, why;
2. whether the optional constant pair landed;
3. the cut-free re-run: what you ran, what you got, what you changed;
4. the build report;
5. the pin commit, and your verification that its claim is true;
6. anything you found and did not fix.

Your final message: what landed, what did not, the build result, and anything you stopped on.
