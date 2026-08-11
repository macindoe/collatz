# Brief: wiki consolidation pass 3 — the HANDOFF rewrite

**Branch:** `wiki-consolidation-3-handoff`. Verify your worktree contains merge `049bda3` (the audit merge) before writing anything; rebase onto current `main` if not.
**Authority:** `briefs/wiki-consolidation-3-audit-findings.md` §1 — the facts-to-preserve list (a), the drop-map (b), the stale-label corrections (c). Read §1 in full, and §9 items 4 and 8. Where the audit contradicts HANDOFF.md's current text, re-read the file and follow the file; record any material discrepancy.
**Deliverable:** HANDOFF.md rewritten in place to the current-state standard, one commit; plus `briefs/wiki-consolidation-3-handoff-findings.md` (short: deviations from the §1 spec, where each of the five no-home facts landed, the encoding-scan verdict). **HANDOFF.md and your findings file are the only files you touch.**
**Register:** flat, calibrated. **Tools:** Read/Edit/Write only — never PowerShell Get-/Set-Content (HANDOFF.md is exactly the file that was mangled this way once; see its own quirks section). Run `python experiments/encoding_scan.py` before committing.

## The rewrite

Target ≈ 8–12 KB on the 2026-07-22 precedent (the file's charter, line 3, is the warrant). Structure:

1. **Keep in substance or verbatim** (audit §1(a) items 1–4): charter, onboarding order, register norm (verbatim), author's-role paragraph (verbatim), delegation pattern, all five infrastructure quirks in full.
2. **State of the fronts**: all six bullets, re-dated as-of 2026-08-12, content per §1(a) — the papers bullet's v3 headline set preserved exactly.
3. **Item 1 (Merle), rewritten — live conditions FIRST** (§1(a) item 10: the two open PRs and what each review means, the grade-at-signing bracket rule, the L-A9-restates-per-h1 clause, round 13 under the new medium, the Zenodo-metadata non-decision with its if-Merle-asks answer, the ccchallenge flat note), then standing conventions (item 5), repo facts at CURRENT values (item 6 — the stale round-9 HEAD pins do not survive), the ledger state block one line per entry (item 7), the standing-decisions block **verbatim, never paraphrased** (item 8 — keep the hosting-pin-v2 and canonical-citation-v3 clauses adjacent so the difference stays visible, §9 item 8; whether the hosting pin moves to v3 is the author's open decision — say so in one clause), the v3 facts (item 12), the author's five round-12 decisions as a dated list (item 11), and the pointers line (item 9's pointer set).
4. **Items 2 and 3** (KL–LP residual; longer-horizon items): keep as they stand.
5. **Drop everything the drop-map covers** (§1(b)) — the rewrite keeps one pointer sentence per arc naming the `briefs/` family. The **five no-home facts** (§1(b) flagged list) are PRESERVED in the rewrite — do not attempt to verify homes and drop them; preservation is the decided course. All 19 stale labels of §1(c) disappear with their blocks.
6. **Renumber cleanly**: open items become 1 (Merle), 2 (KL–LP), 3 (longer-horizon). The staircase items 4–10 vanish — their consolidated state is cycles.md §12.8.6 and the fronts bullet; add one sentence in the fronts bullet or item 3 pointing at the seven staircase findings files as the arc's record only if it reads naturally.

## Review criteria your commit will be checked against

Every dropped block matched to its drop-map row; the verbatim blocks byte-identical (register norm, author-role, standing decisions, quirks); the five no-home facts present; both PR-open conditions and the bracket rule present; fronts re-dated; no round-by-round narration anywhere; nothing in the rewrite contradicts the pages it points at.

No network operations. Commit message descriptive, ending with:

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
