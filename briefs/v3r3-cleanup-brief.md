# Brief: the round-3 residuals (v3 round 3, Wave 6, closing)

**Branch.** `v3r3-review-round3`, at `eca22d4`. Work directly in `c:\Users\Ace\Documents\Collatz` on that branch. **Do not create a worktree.**

Four residuals, self-reported by the fix delegate at `briefs/v3r3-fix-findings.md` and confirmed by the main session. **Fix exactly these four and nothing else.** The round has run six waves; an unscoped edit at this point enters the record unreviewed. If you find something new, report it in your findings — do not touch it.

## The four

**1. A wrong printed number.** `aeh.md` L219 prints the chain-law rejection as "`≈ 14` pooled standard errors". The fix delegate measured `15.1` under the protocol the clause states (the printed cut) and `14.5` cut-free. **Re-measure it yourself** with the existing script — do not adopt either figure from a findings file — and print the one consistent with the protocol the clause states, which is the printed cut, since commit `28647e1` deliberately kept the other four figures in that clause true of the run that produced them. If your measurement disagrees with both, print yours and say so.

**2. A retired symbol.** `anchor-digit-search.md` L139 still writes the law as `π_k`. The round renamed it to `π_{k,D}` and made the cap visible in the notation; this is the one surviving instance in a tracked page. Change the symbol only — the sentence's claim is about the invariant measure and is unaffected.

**3. A status sentence left behind.** `stage1.md` L579's "First, it is a heuristic" now sits behind the `11.8.4.5` ledger snapshot the proved-claim workflow required the fix wave to update. Reconcile it: the ledger is now a marginal of `π_{k,D}`, exact below the cap, with an unconditional base case proved for `θ < 1/4` (`aeh.md` `13.2.4`). Say what is true, minimally — this is a status claim, not a rewrite of the surrounding argument, and the rest of the paragraph's reasoning must survive intact.

**4. Two index nits**, recorded at `briefs/v3r3-tailbound-findings.md` §1(4) and U5. Read them there and apply what they say.

## Constraints

- **Branch `v3r3-review-round3` only.** You may `git add` and `git commit`. **No push, no merge, no rebase, no branch switching, no worktree.**
- **Do not touch `paper/`.** The Appendix A pin at `2e79417` names `677a76a`, and the paper is final for this round. If one of the four appears to require a paper edit, stop and report — it would mean the round needs another pin commit.
- Write files with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes this repo's `≤`, `—`, `ε`. Confirm they still render after editing.
- No change logs, dated journals, or "was X, now Y" prose in any tracked page.
- Do not renumber any anchor.
- Read the current text before editing it. Much of §13 was rewritten this round, and several claims in this round's findings files are already stale.

## Deliverable

The edits committed, plus `briefs/v3r3-cleanup-findings.md`: what you measured for item 1 and what you printed, the disposition of items 2–4, and anything you found and did not fix.

Your final message: the four dispositions in one line each, and anything you stopped on.
