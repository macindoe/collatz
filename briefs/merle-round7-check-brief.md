# Brief: round-7 verify + record (for a delegated session)

**Context required before starting (in order):** `HANDOFF.md` item 1 (through the round-6 shipped state), `briefs/merle-round6-record-brief.md` (provenance + item 1 — the pending items this round closes), `viz/cycle_anchor_gateway.html` footer (the slot his link will fill — read only, do not edit in this session).

## Provenance

Eric Merle's seventh reply (pasted verbatim by the author, 2026-07-23). His letter claims: (a) the sibling gateway page is live at `collatz-lab.org/cycles/` ("Two towers, four harbours"), linking back to our gateway, citing the reduced-coordinates preprint and mirror with DOIs; (b) L-A2 re-derived clean-room on his side, 2400/2400 exact, canary green — two keys in the ledger; (c) L-A3 (spent stock / four real loops / Benford adjudication) co-edited on the shared side; (d) protocol accepted as it stood, shared repo now public per its section 7; (e) `NOTE.md` seeded on the shared side — skeleton only, with one deliberate marker: the realization-height theorem's reference points at `itinerary.md` with a "pin the section" note, left unpinned because 14.15 was mid-split on our side.

Transcription note for the record: the letter's URL carries a Gmail redirect wrapper (`google.com/url?q=https://collatz-lab.org/cycles/...`) — a copy artifact, not content; the site is `https://collatz-lab.org/cycles/`.

State at launch: our `main` was pushed to `origin` (d53d0ec..86ee304, 2026-07-23) before this brief was cut, so the split structure (itinerary.md, anchor-digit-search.md) and the four merged knowledge briefs are public.

## Queue

1. **Verify the sibling page** (no commit; feeds item 3). Fetch `https://collatz-lab.org/cycles/`. Record: (i) the back-link to our gateway — the exact URL he uses and whether it resolves to `viz/cycle_anchor_gateway.html` in our public repo (record the URL verbatim either way; a broken or stale link is a flag, not a failure); (ii) the DOI citations — expected `10.5281/zenodo.21273548` and/or `10.5281/zenodo.21421120` (paper 1 v1/v2) and `10.5281/zenodo.21303918` (mirror paper), per publication.md; record exactly which appear and whether any digit differs; (iii) one sentence on what the page is (register: flat description, no praise transcription).

2. **Verify the shared repo** (no commit; feeds item 3). Clone `github.com/macindoe/one-obstruction-three-faces` read-only into the scratchpad (it should now be public — if the clone fails unauthenticated, record that and flag; do not authenticate around it). Verify against his claims: (i) `PROTOCOL.md` section 7 — does it in fact provide for the public flip he cites; (ii) `LEDGER.md` L-A2 — both keys present (his clean-room re-derivation; his letter says 2400/2400 exact — compare against what the entry records; the pasted digits are author-verbatim, so a mismatch is a finding, recorded and flagged, never "corrected"); (iii) L-A3 — the co-edits, entry coherent with cycles.md 12.6.1.2/12.6.1.3; (iv) `NOTE.md` — the skeleton, and the realization-height reference with its "pin the section" marker: record the exact current text of that reference, and identify (do not edit) the section it should pin to — check itinerary.md yourself and name the section the theorem actually matches, with one sentence of justification; HANDOFF's standing pointer is 14.15.9(a) but verify, don't assume. Record every commit hash you rely on.

3. **Record** (two commits on the branch):
   - `briefs/merle-round7-check-findings.md` — the verification record: items 1 and 2, findings only, flags separated from confirmations, hashes and URLs verbatim.
   - `HANDOFF.md` item 1 update — round-7 received (pasted verbatim; closural register). Both round-6 pending items landed: his LEDGER.md edits (verified this round, per findings) and the sibling-page link (live, verified). New state: owed our side — (a) fill the footer cross-link slot in `viz/cycle_anchor_gateway.html` and push (separate delegate); (b) pin the NOTE.md realization-height reference in the shared repo (separate delegate; push only on the author's explicit go-ahead); (c) reply (drafted after a–b settle; sending stays with the author). Keep the Repos-and-ledger facts paragraph current (repo now public; L-A2 both keys with his clean-room re-derivation; NOTE.md seeded).

## Rules

- Branch **`merle-round7-check`**, commits as itemized in item 3, do NOT merge — the main session reviews and merges.
- Read-only everywhere outside this repo: no pushes to the shared repo, no edits to `viz/`, no web actions beyond fetching the named page. If any push or external write seems needed, stop and hand back.
- Discrepancies (digits, hashes, claims) are recorded and flagged, never disputed in prose and never silently reconciled.
- No reply paragraphs; no scope expansion; stop after item 3.
