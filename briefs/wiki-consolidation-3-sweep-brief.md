# Brief: wiki consolidation pass 3 — the sweep branch

**Branch:** `wiki-consolidation-3-sweep`. Verify your worktree contains merge `049bda3` (the audit merge) before writing anything; rebase onto current `main` if not.
**Authority:** `briefs/wiki-consolidation-3-audit-findings.md` (§2, §3, §4, §7, §8) — read it in full first. Its proposed fixes are proposals: verify each against the current file before applying (locate by quoted text, not line number; where the audit contradicts the file, the file wins — record the discrepancy in your findings and stop on anything material).
**Deliverable:** the edits below in six commits (content separate from structure), plus `briefs/wiki-consolidation-3-sweep-findings.md` recording, per edit: applied as proposed / applied with deviation (stated) / declined (why), with before/after quoted for every judgment-grade edit. Refresh `updated:` front matter (2026-08-12) only on pages whose content changed.
**Register:** flat, calibrated. **Tools:** Read/Edit/Write only — never PowerShell Get-/Set-Content. Run `python experiments/encoding_scan.py` before each commit; record the final verdict.

## The commits (audit §8, with the reviewer's decisions resolved)

- **Commit A (mechanical):** index.md status-paragraph v2→v3 sentence (§2 item 1) + publication.md table row (§2 item 6) + aeh row base-case phrase (§2 item 11 — approved); publication.md status-surface clauses (§2 item 5, and item 7's **measure half only** — the Lagarias-sweep half stays open per §9 item 5); ladder.md mis-homed pointer (§4 item 1).
- **Commit B (judgment):** program.md stale trim clause (§2 item 3); stage1.md checkpoint tail restated at the current answer (§2 item 4 — before/after quoted in the findings AND the commit message; no formula touched); TOUR.md v3 rows (§2 items 8–9 — per §9 item 6, the v2-era facts are preserved as historical, not deleted).
- **Commit C (convention trims):** `status:` fields of aeh.md, publication.md, and anchor-digit-search.md (§3 items 1–3, all three approved; the audit's proposed forms are the starting point); reverse.md theorem-header provenance stamp and itinerary.md remark-title stamp (§3 items 5–6 — the mathematical clauses stay, only date/branch/brief provenance goes; before/after quoted).
- **Commit D (its own commit, correspondence-adjacent):** the cycles.md 12.6.1.4(a) ledger-status sentence (§2 item 2 / §3 item 4). Replace only that one sentence; every other character of the remark — in particular the Merle credit prose immediately before it — must be byte-identical. Quote the whole remark before/after in your findings.
- **Commit E (approved candidates):** README.md statistics-door clause pointing at aeh.md 13.2.4 (§2 item 10 — approved at review; the author's push gate is the final veto and the findings should say so); anchor-digit-search.md §17.8/§17.9 **retitle only** — "(executed; kept as the search's specification)" — not the collapse option (§3 item 7).
- **Commit F (structure; briefs/ supersession headers):** the four headers of audit §7, items 1–4 (item 4 approved for symmetry), each exactly one line under the title, wording per the audit. Nothing else in any briefs/ file is touched.

## Guard rails

- No mathematical statement edited anywhere. No edit touches cycles.md 12.8.5, the PARKED wording, README's stopping rules (lines 32–38), or any displayed formula.
- HANDOFF.md and `experiments/` are out of scope (parallel branches own them). Do not touch them.
- No network operations.
- Commit messages descriptive, ending with:

  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
