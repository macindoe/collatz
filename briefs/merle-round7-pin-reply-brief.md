# Brief: NOTE.md pin preparation + round-7 reply draft (for a delegated session)

**Context required before starting (in order):** `HANDOFF.md` item 1 (post-addendum state), `briefs/merle-round7-check-findings.md` (both the round-1 record and the addendum — the NOTE.md verbatim reference, the revised pin determination, the two co-edit notes), `itinerary.md` 14.15.5 (the pin target: Theorem 14.15.5.3, Corollary 14.15.5.4, the (c) instance) and 14.15.6.7 (the signed characterization), `briefs/merle-round5-reply-brief.md` (register model for replies).

## Provenance

Round-7 state after the check + addendum: sibling page verified and cross-linked (our footer live at `2f24b56`, pushed); shared repo public (author flip, 2026-07-24) at HEAD `61d2cf3`; §7, L-A2, L-A3 all verified; NOTE.md's realization-height reference on file verbatim, awaiting its pin ("pin section on co-edit" — his own commit message invites the co-edit). Pin target confirmed against itinerary.md: **14.15.5(b), Corollary 14.15.5.4**, with 14.15.5(c) for the wrong-sign clause. Two co-edit notes on file: his paraphrase drops "odd" ("positive integer" where the theorem says "positive odd integers" — load-bearing); 14.15.6(d)/Theorem 14.15.6.7 is the natural cross-reference if he wants the negative cycles as first-class signed diagonal points rather than wrong-sign exceptions.

## Queue

1. **Pin commits, prepared in the scratchpad clone of the shared repo — LOCAL ONLY, never pushed** (the push waits on the author's explicit go-ahead; report both diffs verbatim in your final report):
   - **Commit A (the pin, minimal):** in `NOTE.md` §4, replace the parenthetical "(section renumbering in progress 2026-07-23 — pin on co-edit)" with the pinned reference — sense: `itinerary.md` §14.15.5(b), Corollary 14.15.5.4 (the combined characterization); wrong-sign clause at §14.15.5(c). Nothing else changes. Commit message names the co-edit invitation ("pin section on co-edit", `61d2cf3`) and the target.
   - **Commit B (the "odd" precision, separable):** his paraphrase's "coincide at a positive integer" → "coincide at a positive odd integer", matching Theorem 14.15.5.3 / Corollary 14.15.5.4 exactly. One word; commit message states why it is load-bearing (the even case is vacuous under the odd coordinates; the theorem's hypothesis is the positive odd integers). Kept separate so the author can approve A alone or A+B.
   - Do NOT fold in the 14.15.6(d) cross-reference or any L-A3 edit — those are offered in the reply, Merle's call.

2. **Reply draft** (one commit on branch `merle-round7-reply` in OUR repo): `briefs/merle-round7-reply-draft.md`. Register per the round-5 reply model: flat, warm without inflation, his metaphors may be answered in kind but briefly. Sense to carry, in whatever order reads naturally:
   - The page: received, read, cross-link filled — our footer now links "Two towers, four harbours" and states operate ↔ narrate as present fact; the gateway serves it live.
   - The visibility wrinkle, told plainly and without accusation: at first check the repo wasn't public (his letter said it was); only the owner could execute the flip, so Ben flipped it on reading the letter — §7 now reads true. One sentence, closural.
   - Verification: his LEDGER edits verified at `61d2cf3` — L-A2 both keys confirmed (his 2,400/2,400-each entry matches his letter), L-A3 co-edits coherent against cycles.md; the two-key discipline held on both sides.
   - The pin: done at 14.15.5.4 (the combined characterization), with the one-word precision offered/applied per commit B — "positive odd integer" — named as a precision to his paraphrase, not a correction to his mathematics. Draft this passage so it reads correctly whether or not commit B ships (e.g., name the precision either way).
   - Offered, his call: the 14.15.6(d) signed reading (his "wrong sign" points become first-class under Theorem 14.15.6.7); and an L-A3 candidate addition — the spent stock's ceiling identification (cycles.md 12.6.1.3, post-dates his seeding).
   - Note the wiki reorganization is settled (the renumber that had him waiting is what the pin now stands on).
   - No new mathematical claims; anything cited must exist at the named section. Sending stays with the author.

## Rules

- Shared-repo work stays in the scratchpad clone, committed locally, **no push under any circumstances this session** — report diffs and hashes; hand the push decision back.
- Our-repo work: branch `merle-round7-reply`, one commit, do NOT merge — the main session reviews and merges.
- No HANDOFF edit (the pending-item ticks happen at merge).
- Flat register throughout; no scope expansion; stop after item 2.
