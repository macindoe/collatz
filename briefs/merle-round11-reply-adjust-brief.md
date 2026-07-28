# Brief: adjust the round-11 reply — the all-`p` closure, and three things our own record got wrong — for a delegated session

**Context required before starting (in order):** `README.md`, `AGENTS.md`, `HANDOFF.md` item 1, **`briefs/merle-round11-reply-draft.md`** (the draft you are adjusting — read it end to end first), and the records of what changed since it was written: `briefs/staircase-allp-construction-findings.md`, `briefs/staircase-allp-diophantine-findings.md`, `briefs/staircase-gamma-upper-findings.md`, `briefs/staircase-status-audit-findings.md`, `briefs/staircase-status-apply-findings.md`, `briefs/record-defects-repair-findings.md`. Then read `cycles.md` §12.8.6 **as it now stands** — the reply must describe the page he will actually open.

## What this session does

The round-11 reply is drafted, reviewed and on file. It is **business paragraphs only**, with four bracketed placeholders that are the author's and must stay untouched and empty: the personal opening; anything answering his personal paragraphs; the joint note's contribution sentence together with the answer to his three proposals; the personal closing.

Since it was drafted, our side closed the all-`p` staircase question and repaired two defects in our own record. **You are adding that material and adjusting whatever it makes stale — nothing else.** Every existing paragraph that is still accurate stays exactly as it is.

## The new material, with its scope attached

**The all-`p` sharpness claim is proved**, and proved at a constant, which is stronger than the `O(log p)` our own paper hedged. Two theorems compose:

- **Construction B** (`cycles.md` 12.8.6.2): given a candidate `n` satisfying `(H0)` and `γ(n) ≥ Γ(p,n)`, an explicit profile satisfies **all `p`** size conditions `q ≤ R_r`, crash depth exactly 1, **with no correction step at all**. The old recipe's shortfall was `Θ(p)` — it was wrong by a fixed additive offset of `1/(L−1) = 1.70951` per block, the standing depth whose interest at rate `log₂(3/2)` pays each block's unit of exit valuation.
- **Availability** (12.8.6.1): such an `n` exists in every scale window, **unconditionally** — no hypothesis on the partial quotients of `log₂3`, no irrationality measure, no continued-fraction chain. The governing fact is one exact number, `θ = 8 − 5·log₂3 = 0.0751874964…`, and a two-sided arc slightly longer than it.

**The scope, which travels with every sentence:** `3.683012 ≤ γ ≤ 5.140212`; unconditional for `p ≥ 16`; `3 ≤ p ≤ 15` by explicit finite check; **`p ∈ {2,4}` outside Construction B's reach** — their canonical windows hold no integer. Two theorems with hypotheses, not one unconditional statement. Say all of it; the register here is that a result with stated holes is worth more than a clean sentence.

**Do not overstate the origin either.** This arc opened because the joint-note premise check found the sharpness half exactly half proved — which happened because *his* letter asked for a contribution sentence. That is worth one clause, not a paragraph.

## The three items that are ours to hand back, plainly

1. **`σ` was undefined in Proposition 12.6.1, and the natural reading is wrong.** This is the frame he works in — Remark 12.6.1.1's transport recurrence is shared-ledger entry L-A1, kernel-verified on his side — so tell him directly and without hedging that our page had a defect that could have misled him. The correct convention is `σ_j = s_j + m_{j+1}`, now defined in place. What makes it worth a paragraph rather than a line: **every structural guardrail is blind to it.** The trivial-cycle canary gives `σ = 2` under both readings and reproduces `4^p − 3^p` either way; `K` is a cyclic sum; and the transport recurrence itself is satisfied exactly under *both* conventions — 1685/1685, with a proof, because every `σ` telescopes and both readings are cyclic rearrangements of the same multiset. Only an externally pinned check sees it. Offer the canary we added. If his own artifacts implement the proposition, this is worth his checking; put that as an offer, not a warning about his work.
2. **The `p = 92` search bound was wrong in our prose by a factor of 4,778** — `n₀(92) = 4.78·10^21`, not the `~10^18` README and 12.8.5 carried; the prose had quoted the bare exponential rate `1.585^92 = 2.53·10^18` and dropped the corollary's ~1890 factor. The table was right throughout. Nothing downstream moves: both figures are infeasible by 1,400+ orders of magnitude.
3. **His pincer, stated accurately and generously.** The `p = 22` episode is now understood as a property of the *candidate list* — the continued-fraction chain has a genuine hole there — rather than of `log₂3`. His Diophantine pincer hypothesis named that cause and both closing candidates, and 12.8.6.4 credits it; that record stands unchanged. The new route does not need it, and **that is not a demotion of the observation** — it is the same diagnosis, now general. Write it so that it reads as what it is.

## What to adjust in the existing draft

4. **The joint-note section.** The premise check found two places where the fit was looser than his sentence implied. **One of them is now closed**: the sharpness half is proved. The other stands — what we published is *effective finiteness* at every period, not "counting closes every period". Update that paragraph to say exactly which one moved and which did not. **Do not write the contribution sentence, do not propose wordings for it, and do not propose an outline** — those exclusions are unchanged and absolute.
5. **The published record.** Our own `thm:staircase` hedge stands as printed — "not proved *here*" is a statement about the paper and a later proof elsewhere does not falsify it. But the v2 note's identification of the remaining gap is now incorrect on both halves, and an erratum correcting only that sentence is drafted, not issued. Tell him, in a clause: he may cite the paper in the joint note, and should know which sentence is superseded.
6. **The where-everything-lives map** gains the new sections and findings files, with their check counts. The wiki-`main` pin stays marked **CHECK AT SEND TIME** and the co-edit's shared-repo SHA stays `[PENDING]` — the co-edit is a parallel session's work and is not claimed here.
7. **Nothing is offered for the ledger.** This is our result, one key, and whether it becomes a ledger entry is the author's decision and a later co-edit. The reply may report and offer it; it may not seed anything.

## Verification

Every number, section reference and constant must be checked at its named place before it enters the draft, exactly as the first drafting session did — and that instruction has already earned its keep twice this round, catching `1.43823` and two false inequalities. `cycles.md` §12.8.6 is freshly rewritten; quote it as it now reads, not as the findings describe it.

## Record

- The adjusted `briefs/merle-round11-reply-draft.md`, edited in place, with its header's verification note updated to cover the new material and to list what changed in this pass.
- `briefs/merle-round11-reply-adjust-findings.md` — what you added, what you adjusted, what you left alone and why, and any number you could not verify at its named place.
- `HANDOFF.md` — ONE scoped paragraph.

## Rules

- Branch **`merle-round11-reply-adjust`**. Verify your worktree HEAD contains this brief; if not, rebase onto the `main` SHA in your launch instructions, and state the base SHA.
- Per-item commits. Do **not** merge — the main session reviews and merges. **Nothing is sent; sending is the author's.**
- The four placeholders stay untouched and empty. No contribution sentence, no note outline, no genre proposal.
- Register: flat, calibrated, no excitement inflation. This is a good result and the draft should read as though good results are ordinary. Where our record was wrong, say it once, plainly, and move on.
- Do not edit `cycles.md`, `paper/`, `sources/` or any wiki page; this is a correspondence window.
- No pushes; no interaction with his repositories.
- Encoding: Edit/Write tools only, never PowerShell `Get-Content`/`Set-Content`; run `experiments/encoding_scan.py` before your last commit.
