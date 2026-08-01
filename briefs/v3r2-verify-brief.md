# Brief: verify round 2 and close the stale pointers (v3 round 2, Phase 3)

Branch `v3r2-review-round2`, three commits on top of `e4dac49`:
`81e41e1` (briefs/findings), `c2d465a` (content), `3511a0d` (Appendix A pin + PDF).
Not yet merged to `main`. **Nothing is pushed and nothing may be pushed.**

You have two jobs: **verify** what the round did, and **apply** a short list of pointer-page repairs the content round could not reach. You may run read-only `git` commands (`log`, `show`, `diff`, `status`) but **no** `git` write operation — no add, commit, branch, checkout, stash, merge, or push. The main session owns version control.

## Part 1 — apply the stale pointers

`briefs/v3r2-record-apply-brief.md`'s delegate flagged these as out of its scope. All name AEH by its **retired** "bulk form", or lean on the bulk cut in the way `aeh.md` `13.6.6` now disowns. Bring each into line with the ensemble form of `aeh.md` `13.2.1`:

- `anchors.md` L59 — "bulk-form hypothesis (13.2.1)"
- `index.md` L26 — "precise bulk formulation (13.2)"
- `reverse.md` L62 — "AEH: orbit equidistribution"
- `TOUR.md` L26 — "the bulk hypothesis conditions on a size cut and cannot see individual tails by construction". Still true, but the *reason* has changed: individual tails are unreachable because the statement is about sampled starting values at a finite horizon, not because of the cut.
- `itinerary.md` L73 and `aeh.md` L36 — a matched pair, both saying AEH is equidistribution of "actual orbits' stratum words". Under the ensemble form the objects are the bulk segments of sampled starts. **Edit both together or neither** — they are deliberately synchronized.

**`reverse.md` §14.5.3 is out of bounds.** Its "measured stationary depth distribution" is the *reverse tree's* depth law, a different object that earlier sweeps have wrongly "corrected". Touch only L62.

Keep every edit minimal — these are pointer sentences, not statements of the hypothesis. Update `updated:` front matter on any page you edit that has it.

## Part 2 — verify

Report findings; do not repair anything outside Part 1 without saying so.

**A. The Appendix A pin resolves.** The paper's Appendix A claims "every wiki section and script named in this paper is cited at commit `c2d465a`". Check it literally: extract every `\texttt{...}` wiki section number and every script filename named anywhere in `paper/collatz-reduced-v3.tex`, and confirm each exists at `c2d465a` (`git show c2d465a:<file>`). This exact claim has been wrong before — it is why commit `643e864` exists.

**B. Paper and record agree.** Compare, statement by statement:
- what AEH is (sample space, horizon, limit) — paper Hypothesis 5.1 against `aeh.md` `13.2.1`;
- what it buys — paper's reframed consequences paragraph against `aeh.md` §13.3. **Neither may claim a drift or contraction consequence.**
- `π_k`'s depth component — must be the exact convolution law in both, stated in one place with the other pointing;
- `13.6.5`'s attribution to Tao — present in both, values unchanged (`2/3`, `19/63`, `2/63`, `1/3`, `20/63`);
- the staircase scope — the paper's correction against `cycles.md` §12.8.6's period ranges.

**C. AGENTS.md compliance on every page touched this round.** No change logs, no dated journals, no "was X, now Y" prose. `status:` a short state phrase, not a diary. Every fact in exactly one place — in particular, check that the retired window-chain depth law is no longer presented as `π_k`'s definition anywhere, and that `13.6.4`'s `(q2)` no longer asks the reader to retroactively reinterpret `13.2`.

**D. No anchor renumbered.** `13.2.1`, `13.6.4`, `13.6.5`, `14.15.1.5`, `12.8.6` and every other monolith number must resolve to the same object as at `e4dac49`.

**E. Encoding.** Grep every `.md` for `Ã`, `â€`, `Â`. Confirm the `≤ — ε π ω ⊥` characters in edited passages read correctly.

**F. The five review findings.** Confirm each is addressed, and say how: (1) Hypothesis 5.1's sample space; (2) `π_k`'s joint labelled law including `a_+`, and the convolution attaching to `d = m + a`; (3) `aeh.md` no longer defining `π_k` by the refuted stationary law; (4) staircase status versus the version note's no-strengthening claim; (5) the digit budget's removed proved-identity claim.

**G. Anything the round broke.** Cross-page claims that no longer hold, dangling references, pointers to sections that changed meaning.

## Deliverable

Write `briefs/v3r2-round-findings.md`: what the round changed, the verification result for each of A–G, what you repaired in Part 1, and every open item — including ones already known (the abstract's singular/plural "main new theorem"; the v2 note's "hedge sentence" now naming a `\paragraph`; the 15-page length against the reviewer's 12-page request). State plainly anything you could not verify.

## Constraints

- **No `git` write operations.** Read-only git is fine.
- Write with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection.
- Do not rebuild the PDF; it is already built from the pinned tex and committed. If you find a `.tex` defect, **report it, do not fix it** — a tex edit would desynchronize the committed PDF and the pin.
- Do not renumber anything. Change no numerical value.
