# Brief: two record defects found at review — the undefined `σ` in Prop 12.6.1, and the `p = 92` bound mismatch — for a delegated session

**Context required before starting (in order):** `README.md`, `AGENTS.md` (especially: math statements edited conservatively, no change logs in tracked files, every fact lives in exactly one page, `sources/` immutable), `cycles.md` §12.6.1 and §12.8 (12.8.1, 12.8.2 with its `n₀(p)` table, 12.8.5).

Both defects were found by the **main session at review**, not by a delegate, and neither has anything to do with the all-`p` staircase result. They are independent, self-contained, and repairable now. A sibling session (`staircase-status-audit`) is auditing the staircase fallout in parallel — **do not touch §12.8.3 or §12.8.6, which are its territory.**

## Defect 1 — `σ` is never defined in Proposition 12.6.1, and the natural reading is wrong

`cycles.md` Proposition 12.6.1 states

> `R_r := Σ_(t=0)^(p-1) 3^(M_t) · 2^(S_t) · (2^(s_t) - 1)`, where, reading indices in rotation order starting at `r`: `M_t = Σ_(j>t) m_j` and `S_t = Σ_(j<t) σ_j`.

**`σ_j` is used and never defined anywhere in the proposition.** The natural reading, `σ_j = m_j + s_j`, is **wrong**. The correct convention — the one the established, committed `experiments/uniform_trim.py` `R_rot` uses, and the one under which everything in §12.8 was computed — is

> **`σ_j = s_j + m_{j+1}`.**

Measured at review on 300 random profiles: the correct convention agrees with `uniform_trim.R_rot` **300/300**; the natural misreading agrees **6/300**, and produces `R_r` wrong by orders of magnitude.

**Why the wiki's own guardrails do not catch it, which is the part that makes this urgent.** The sanity identity the proposition cites — the trivial cycle `m_t = s_t = 1`, giving `R = 4^p − 3^p` — gives `σ = 2` under **both** readings and therefore passes either way. `K = Σs_t + n` is a cyclic sum and is likewise blind to the shift. So a reader implementing from the prose gets a silently wrong object that reproduces the one published canary.

This is live: it is the frame Merle works in (the transport recurrence of Remark 12.6.1.1 is shared-ledger entry L-A1, kernel-verified on his side), and a referee reading §12.6.1 would implement the wrong thing.

### Queue for defect 1

1. **Establish the correct convention yourself**, from `experiments/uniform_trim.py` and from Remark 12.6.1.1's transport recurrence `2^(σ_r) R_(r+1) = 3^(m_r) R_r + (2^(s_r) − 1)·q`, in fresh code. Confirm both the agreement counts above and that the recurrence holds identically under `σ_r = s_r + m_{r+1}` and fails under the misreading. Confirm the trivial-cycle canary cannot distinguish them.
2. **Repair Proposition 12.6.1 in place**: define `σ` explicitly in the proposition, in one clause, in the page's register. Do not restate the mathematics, do not renumber, do not touch the proof. This is a definition that was missing, not a change of content — say so in the commit message, not in the file.
3. **Sweep for the same omission elsewhere.** Does `σ` appear undefined in `spine.md`, `itinerary.md` (Lemma 14.15.9.2 is the mirror-frame statement), `stage*.md`, or the papers' sources? Record every occurrence and whether it is defined at its point of use. Where a *published* source has the same gap, **record it — do not edit `paper/` or `sources/`.**
4. **Add a canary that would have caught it**, to `experiments/uniform_trim.py` or a small new script: a check that distinguishes the two conventions — the trivial cycle cannot, so use a profile with unequal `m` and `s`, and assert against the transport recurrence. Commit its output. The point is that the next implementer fails loudly instead of silently.

## Defect 2 — the `p = 92` search bound is inconsistent between two pages

`README.md` (strategy section) and `cycles.md` 12.8.5 both give the crossover search bound at `p = 92` as **`n ~ 10^18`**. `cycles.md` 12.8.2's own `n₀(p)` table gives **`n₀(92) ~ 4.78·10^21`** — about 4,800× larger. Both are wiki, neither is published; found during the joint-note premise check (`briefs/jointnote-premise-ours-findings.md`), recorded and deliberately not corrected there.

### Queue for defect 2

5. **Recompute `n₀(92)` from Corollary 12.8.2's own displayed equation**, in fresh exact code, and determine which figure is right — or whether the two are answering different questions (e.g. different constants, a different Rhin exponent, `n` versus `K`, or an older version of the bound). **Do not assume the table is right and the prose wrong; check both.**
6. **Repair whichever is wrong, in its own commit**, with the correct value and one clause of scope if the two figures turn out to answer different questions. If the discrepancy has a cause worth recording (a superseded constant, say), record the *current correct statement* only — history is git's job.
7. Confirm the repair changes nothing downstream: 12.8.5's conclusion is that the crossover plan is withdrawn as infeasible, and `10^18` and `4.78·10^21` are both infeasible, so the strategic conclusion should be untouched either way. **Verify that rather than asserting it**, and say so.

## Record

8. `experiments/record_defects_check.py` + committed output (the convention discrimination, the canary, and the `n₀(92)` recomputation).
   `briefs/record-defects-repair-findings.md` — both defects, the evidence, the exact repairs made, and the sweep results for defect 1 item 3.
   `HANDOFF.md` — ONE scoped paragraph; a sibling edits item 1 in parallel, keep to your own lines.

## Rules

- Branch **`record-defects-repair`**. Verify your worktree HEAD contains this brief; if not, rebase onto the `main` SHA in your launch instructions, and state the base SHA.
- **You MAY edit `cycles.md` §12.6.1 and, for defect 2, `README.md` and `cycles.md` 12.8.5 or 12.8.2 — those repairs are the deliverable.** You may **not** touch §12.8.3 or §12.8.6 (the sibling's territory), `paper/`, or `sources/`.
- Separate commits for the two defects, and content separate from structure.
- Nothing is labeled proved without verification code that could have failed; record failures rather than deleting them.
- No pushes; nothing for the ledger, the note or the reply.
- Encoding: Edit/Write tools only, never PowerShell `Get-Content`/`Set-Content`; run `experiments/encoding_scan.py` before your last commit.
- Stop after item 8.
