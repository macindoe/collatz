# Findings: round-7 verify (merle-round7-check)

Delegated session, 2026-07-23. Brief: `briefs/merle-round7-check-brief.md` (base commit `2253901`).
All checks below were run 2026-07-23, ~13:45–13:50 UTC. Register: findings only;
confirmations and flags separated. Nothing here disputes the letter's text — the pasted
digits are author-verbatim; where observation and claim differ, both are recorded.

## Item 1 — the sibling page

Fetched `https://collatz-lab.org/cycles/` (the real URL, not the Gmail wrapper).

### Confirmations

- **The page is live.** Title: *"Collatz cycles: two towers, four harbours"* — matching
  the letter's claimed title. One sentence, flat: a bilingual (French/English) explanatory
  page on why hidden Collatz loops are hard to rule out, presented through the
  two-towers/near-miss picture rather than formulas, credited to Eric Merle (© 2026,
  ORCID `0009-0008-7940-402X`).
- **Back-link to our gateway, verbatim:**

  ```text
  https://macindoe.github.io/collatz/viz/cycle_anchor_gateway.html
  ```

  anchor text "Benjamin Macindoe's interactive gateway" / "gateway interactif de
  Benjamin Macindoe". **Resolution check:** fetched that URL directly; it serves our
  page — title and first heading "Cycle anchor gateway", and the footer's
  round-6-era TODO placeholder ("TODO: link when his sibling gateway exists") is
  visible in the served copy, i.e. GitHub Pages is serving `viz/cycle_anchor_gateway.html`
  from the public repo at the pushed state. The link resolves; not stale, not broken.
  (Path-case note: the URL says `collatz` lowercase; the repo's API `full_name` is
  `macindoe/collatz`, so the case matches exactly.)
- **DOI citations, verbatim as they appear on the page:**
  - `10.5281/zenodo.21421120` — anchored to "Reduced coordinates for the Collatz map" (v2). Digit-exact against publication.md.
  - `10.5281/zenodo.21303918` — anchored as the mirror paper ("papier miroir"). Digit-exact against publication.md.
  - The v1 DOI `10.5281/zenodo.21273548` does **not** appear. The brief's expectation was v1 "and/or" v2; citing v2 only is within expectation and consistent with the round-5 hosting decision (DOI-pinned to v2). Recorded, not flagged.
- Other outbound links, for the record: `../papers/` ("Nos papiers"), CC BY-SA 4.0,
  his ORCID, LinkedIn, and GitHub — the GitHub link points at
  `https://github.com/ericmerle3789/collatz-conditional-cycles` (his public conditional-cycles
  repo), **not** at the shared repo. Observation only; nothing on the page claims otherwise.

### Flags

- None for item 1.

## Item 2 — the shared repo

### Flag (primary): the shared repo is not publicly accessible; every sub-check blocked

Attempted per the brief: unauthenticated read-only clone of
`github.com/macindoe/one-obstruction-three-faces` into the scratchpad.

- `git -c credential.helper= clone https://github.com/macindoe/one-obstruction-three-faces.git`
  → git fell back to a username prompt (GitHub's behavior when the repo is not visible
  unauthenticated); clone failed.
- Unauthenticated GitHub API, `GET /repos/macindoe/one-obstruction-three-faces` → HTTP 404
  (`{"message": "Not Found"}`). Same for the web URL (`HTTP/1.1 404 Not Found`,
  server date `Thu, 23 Jul 2026 13:47:54 GMT`).
- Control that the failure is not on our end: `GET /repos/macindoe/collatz` succeeds
  unauthenticated (`"private": false`, `"pushed_at": "2026-07-23T13:41:35Z"`,
  default branch `main`).
- Alternate-location checks: `GET /users/macindoe/repos` — the shared repo is absent from
  the public list; `GET /users/ericmerle3789/repos` — his public repos are
  `collatz-conditional-cycles`, `one-obstruction-three-faces-lean`, and an unrelated repo;
  `GET /repos/ericmerle3789/one-obstruction-three-faces` → 404.

Per the brief's rule, no authentication was used to work around this; recorded and flagged
instead. Consequence: **the letter's claim (d) — "shared repo now public per its section 7" —
did not verify at check time** (2026-07-23 ~13:48 UTC). Possible innocent explanations (flip
not yet executed, executed after the letter was drafted but reverted, or a rename) are not
adjudicated here; the observation stands as an observation.

Blocked sub-checks, each **unverified this round** (claims neither confirmed nor
contradicted; the pasted digits stay author-verbatim on file):

- (i) `PROTOCOL.md` §7 — whether it provides for the public flip: **could not be read.**
- (ii) `LEDGER.md` L-A2 — both keys present; his stated `2400/2400` exact, canary green:
  **could not be compared against the entry.**
- (iii) `LEDGER.md` L-A3 — co-edits, coherence with cycles.md 12.6.1.2/12.6.1.3:
  **could not be read.**
- (iv) `NOTE.md` — skeleton and the realization-height reference's exact current text:
  **could not be read.** No verbatim text is quoted here because none was obtainable;
  nothing in this file should be mistaken for the reference's wording.
- **Shared-repo commit hashes relied on: none** — none were obtainable. Hashes on file from
  prior rounds (his Lean repo `3b547c4`; his LEDGER edit base `ff379c4`) are cited from the
  round-6 record, not re-verified here.

### The pin target (item 2(iv), second half — determined from our side; no edit made)

The letter says NOTE.md's realization-height theorem reference points at `itinerary.md`
with a "pin the section" note. Determined from itinerary.md's actual content:

**The pin should be `itinerary.md` 14.15.9(c) — Theorem 14.15.9.6 with Corollary
14.15.9.7.** Justification, one sentence: 14.15.9(c) is where the exact realization-height
law is stated and proved — the closed forms `H⁺_{np,np} = ρ_n + [t_n = 0]·Q_n`,
`H⁻_{np,np} = (1 + [t_n = 2])·Q_n − ρ_n`, with the capped-at-`|y^*|` versus
escaping-at-CRT-rate dichotomy governed by `q = 1` (the subsection's own headline reads
"the per-sector realization height at whole-period windows obeys an exact law") — whereas
HANDOFF's standing pointer 14.15.9(a) contains only the supporting arithmetic (fixed-point
Lemma 14.15.9.1, rotation Lemma 14.15.9.2, adelic anchor Theorem 14.15.9.3), none of it a
realization-height theorem.

So the standing pointer 14.15.9(a) was checked and does **not** survive as the pin target;
(a) remains the right pointer for the transport-recurrence connection (L-A1; the
"(Integer form.)" remark after Lemma 14.15.9.2 ties it to cycles.md 12.6.1.1), which is
presumably how it entered HANDOFF — but the theorem *named* by the letter matches (c).

**Caveat, flagged:** this determination is made without NOTE.md's actual reference text
(blocked above). If his reference turns out to mean the boundedness-equivalence — "integrally
realized ⟺ realization height bounded" — rather than the periodic-word height law, the pin
would instead be `itinerary.md` 14.15.4(c) (Theorem 14.15.4.5, the equivalence theorem),
with the signed/combined form at 14.15.5.4 / 14.15.6(c). Re-confirm against the verbatim
reference text at pin time, when the repo is readable; the pin push itself waits on the
author's explicit go-ahead regardless.

## Hashes and state relied on (our side)

- Branch base: `2253901` (the round-7 brief commit; descendant of `86ee304`).
- Public repo state verified serving: `origin` = `github.com/macindoe/collatz`,
  `main` pushed through `86ee304` (per the brief's launch state; API `pushed_at`
  `2026-07-23T13:41:35Z`), and the footer TODO placeholder visible in the served gateway
  page confirms the deploy is at the round-6-merged state.

## Summary

| Letter claim | Status |
|---|---|
| (a) sibling page live, back-link, DOIs | **Confirmed** (back-link resolves; DOIs digit-exact, v2 + mirror; v1 absent, within expectation) |
| (b) L-A2 both keys, 2400/2400, canary green | **Unverified — blocked** (repo inaccessible) |
| (c) L-A3 co-edited | **Unverified — blocked** (repo inaccessible) |
| (d) protocol accepted; repo now public per §7 | **Flagged** — repo not publicly accessible at check time; §7 text unread |
| (e) NOTE.md seeded, realization-height reference unpinned | **Unverified — blocked**; pin target determined our-side: 14.15.9(c), with the 14.15.4(c) caveat above |
