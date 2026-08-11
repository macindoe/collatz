# Findings: wiki-consolidation-3-handoff — the HANDOFF rewrite (2026-08-12)

Brief: `briefs/wiki-consolidation-3-handoff-brief.md`. Authority: `briefs/wiki-consolidation-3-audit-findings.md` §1, §9 items 4 and 8. Branch `wiki-consolidation-3-handoff`, base `e8a0b65` (current `main`, the briefs commit) — the worktree was cut at `d09895c` and the branch was created at `e8a0b65` before any work, per the brief's rebase instruction; the audit merge `049bda3` is an ancestor.

`HANDOFF.md` rewritten in place from 121 lines / 132 KB to 74 lines / **14.1 KB** (14,391 bytes working copy). `python experiments/encoding_scan.py`: **CLEAN** (451 tracked files, 0 invalid, 0 BOM, 0 double-encoding), run after both file writes and before the commit. `HANDOFF.md` and this file are the only files touched; Read/Edit/Write tools only.

## Where the five no-home facts landed

- (i) The author's five round-12 decisions, as a dated list — item 1, "The author's round-12 decisions (2026-07-30)", all five with their enactment status.
- (ii) The Zenodo-metadata non-decision with the if-Merle-asks answer — item 1, Live conditions, stated in full.
- (iii) Merle's personal-background sentence (lycée electricity teacher, no doctorate, a year in) — item 1, Standing conventions, closing sentence, attributed to his round-10 letter.
- (iv) The L-A9 bracket-resolution rule — item 1, Live conditions: the `[GRADE AT SIGNING…]` bracket must not survive into the merged, signed note, resolves at PR #1's review, and the grade line restates per whatever h1 becomes.
- (v) The spend-limit symmetry anecdote — item 1, round-12 decisions list, inside decision (1) (the cost answer).

## Deviations from the §1 spec

1. **Size: 14.1 KB against the ≈8–12 KB target.** The blocks the spec mandates verbatim (charter, onboarding, register norm, author's role, six fronts bullets, standing conventions, standing decisions, items 2–3, delegation pattern, all five quirks) total ≈9.5 KB on their own; the §1(a) fact set (live conditions, current repo values, 13 ledger lines, v3 facts, the decision list, pointers) does not fit in the remaining ≈2.5 KB. Preservation was chosen over the size figure; nothing on the facts-to-preserve list was dropped, and every non-verbatim block took a tightening pass.
2. **Pointers line extended, not copied.** Old line 93's entries are all retained; added the credit-language homes from audit item 9 (12.6.1.4, 12.8.6.1, 12.8.6.4) and `briefs/jointnote-*` beside `briefs/merle-*`, so the joint-note arc (Window D pre-checks, the PR #2 draft record) keeps a named `briefs/`-family pointer.
3. **The staircase arc pointer** landed in the Cycles fronts bullet (the brief's fronts-bullet-or-item-3 option), naming all seven findings files; item 3 stands unmodified.
4. Two small compressions of preserved wording: the live-conditions block states "his approving review is the round's second key" without old line 89's "for the first time in the PR itself" clause, and the v3 defect names the frozen self-description as "not yet published" rather than quoting the full parenthesis (the full text is in `paper/collatz-reduced-version-history.md`).

## Discrepancies

None material. Every audit §1 claim spot-checked against the file text verified at its quoted place; the stale round-9 HEAD pins (`81431c7`, `97b57d7`) died with their blocks and the current values (`7c05458`, `d48ba9e`, the two PR branches) are the ones carried. All 19 stale labels of §1(c) are gone (grep-verified: no "awaiting review", "in flight", "NOT PUSHED", owed-lists or round narration survives outside the verbatim quirk block's incidental "round-9 delegate session"). The hosting-pin-v2 / canonical-citation-v3 clauses sit adjacent (standing decisions verbatim, then the one-clause coexistence note with the author's open decision), per §9 item 8.
