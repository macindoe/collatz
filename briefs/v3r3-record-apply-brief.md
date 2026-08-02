# Brief: apply round 3 to the record (v3 round 3, Wave 3, first of two)

**Branch.** `v3r3-review-round3`, base `adbde8e` (design phase committed; `dc61306` is `main`). Work directly in `c:\Users\Ace\Documents\Collatz` on that branch. **Do not create a worktree.**

**This is an edit task.** The design is settled. You are not re-deciding anything; you are landing four delegates' drop-in text in the wiki, correctly and in the right order. Where you believe a drop-in is wrong, stop and report — do not improvise a third version.

A parallel-numbered delegate applies the paper (`briefs/v3r3-paper-apply-brief.md`) **after** you, reading the record you leave. The wiki is the authority; the paper cites it. Get the record right and the paper follows.

## Read first, in this order

1. `briefs/v3r3-aeh-object-findings.md` — the object. §3 definitions, §4 Option 1 (**the author's choice**), §7 drop-ins.
2. `briefs/v3r3-inselmann-horizon-findings.md` — §0, §3, §5 drop-ins.
3. `briefs/v3r3-cut-weighting-findings.md` — §4 (the measurement), §5–§7, §8 drop-ins, §9 reconciliation.
4. `briefs/v3r3-basecase-density-findings.md` — §5 drop-ins, §8 (the verification code), and its closing notes on collisions.

## Apply order, and the two known collisions

**Order: A → B → C → D.** Later delegates saw earlier ones and deliberately supersede them in places. Both collisions are flagged in the findings themselves; both are your responsibility to get right:

1. **The defective density sentence.** C's §8.4 rewrites `aeh.md` L32 and reproduces the old density inference verbatim. Applying C's block as-is carries the defect forward. **D's §5.1 is the substitute tail for that block.** The same pattern occurs at the paper's L301–304, where A's §7.3 also reproduces it — that one belongs to the paper delegate, but record it in your handover note.
2. **The anchor collision.** C claimed `13.2.3`; D yielded and renumbered itself to `13.2.4`/`13.2.5`. Apply C's `13.2.3` and D's `13.2.4`/`13.2.5`. **Renumber nothing else** — monolith anchors are stable citation targets (`AGENTS.md`).

## What lands where

**`aeh.md`** — the bulk of the work. §13.2 and the hypothesis; the new anchors; §13.4's reconciliation sentence; L48's cut-coordinate note; §13.6.3(v)'s probability space; §13.6.4's definition sentence and (q1); the status front matter (L2) and the Current-state paragraph (L8).

**`itinerary.md` L73**, **`bridge.md` L69**, **`HANDOFF.md` L20** — the genericity/equivalence pointers. Under Option 1 these become true where they stand; apply A's §7.7/§7.8 text and change no more than it says.

**`publication.md`** — four things: B's §5.7/§5.8 replacements for the Inselmann material; B's Tao-motive correction at L45; and the two round-2 leftovers below.

## The round-2 leftovers the author added to scope

- **G4.** `publication.md` L39 records a superseded plan ("wiki-only now… no v3 yet") and the `status:` line says "both papers published". **The correct state, confirmed by the author this round: v3 is drafted and unpublished, with a reserved DOI (`10.5281/zenodo.21730505`).** Record that state. This is a status field, not a diary — no "was X, now Y".
- **G5.** Retired names: `anchor-digit-search.md` L37 and L78 call AEH "the bulk hypothesis"; `bridge.md` L48 says AEH is needed "for typical orbits" where the record now says "typical starting values". Neither sentence is false; both use retired vocabulary. Align them, minimally.

## Three corrections of fact, not of phrasing

These are the round's substance. Handle them exactly.

1. **The bulk cut binds.** `aeh.md` L48 says "in these runs neither binds, so no number below depends on the choice." C measured the flagship run and it is false: the core cut removes 2.64 % of visits and binds on 15.5 % of orbits; the door cut 1.67 % / 8.9 %; the two disagree on 1,538 visits. This is independently confirmable from the record's own number — each orbit contributes exactly 30 visits when nothing is dropped, and `154,389` is not a multiple of 30. Apply C's §8.6.

2. **The same false claim is in the code.** `experiments/aeh_symbolic.py` L541–544's docstring asserts the cut "never binds". Correct the **docstring only**. Do not change what the code does — the recorded numbers were produced by the current behaviour, and changing it would orphan them.

3. **The density inference is false, not merely unproved.** D has a counterexample (`aeh.md` L32's claim fails for `Bad_N = [N, N(1+1/log N))`). The repair is the dyadic-shell formulation, D's Prop. `13.2.5`.

## The numbers you must not quietly restate

C's measurement means the recorded calibration numbers were produced under a cut that biases the ledger's own statistic. **Which recorded numbers this touches is an open question** — C checked plausibility, not the numbers (`briefs/v3r3-cut-weighting-findings.md` §12), and re-running the campaign is out of scope for this round.

So: **do not re-derive, adjust, or silently re-word any measured value in `13.4` or `13.6.5`.** Where the surrounding prose asserts something the measurement no longer supports, apply the delegates' text, which was written knowing this. Then produce, as part of your handover, **an explicit list of every number now standing under a protocol whose bias is known but unquantified.** That list goes to the main session for the author's decision; it does not go into a tracked page as a caveat you invented.

## The verification record

D's lemma is proved and numerically checked with fresh code. Per `AGENTS.md` ("Before marking anything proved"), the owning page carries a single current verification line: what was checked, the range, the date.

- Promote D's scratch code, inlined at `briefs/v3r3-basecase-density-findings.md` §8, to `experiments/`. Name it to match the repo's conventions and have its header state which page and result it supports (`AGENTS.md`, Layers 3).
- Add the verification line to `aeh.md` in the form the page's other verification lines use. Do not append a second one — overwrite if a line for the same result exists.

## Constraints

- **Branch `v3r3-review-round3` only.** You may `git add` and `git commit` on it. **No push, no merge, no rebase, no branch switching, no worktree.** If a commit is refused, stop and report; do not route around it.
- Commit in coherent units with messages in the repository's register (see `git log`). **No change logs, dated journals, or "was X, now Y" prose in any tracked page** — history is git's job (`AGENTS.md`).
- Write files with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes this repo's `≤`, `—`, `ε` and silently corrupts these pages. After editing, confirm those characters still render correctly.
- Do not renumber any monolith anchor beyond the two new ones named above.
- Every fact lives in exactly one page (`AGENTS.md`). If two pages would state the same thing, one states it and the other points.
- Do not touch `paper/` — that is the next delegate's scope, including the `.tex`, the `.pdf` and the version note.
- Do not attempt to prove AEH, and do not extend any claim past what the four findings files support.

## Deliverable

The edits, committed on the branch, plus `briefs/v3r3-record-apply-findings.md` containing:

1. a site-by-site table: file, line, which delegate's text was applied, and any deviation with its reason;
2. the collision resolutions, stated explicitly;
3. **the list of measured values now standing under a known-biased protocol** (see above);
4. anything a drop-in asserted that you could not verify against the files;
5. what you changed that no delegate specified, and why — this list should be short, and every entry is a flag for review.

Your final message to the main session should be a compact summary: what landed, the two collisions, the biased-number list, and anything you stopped on.
