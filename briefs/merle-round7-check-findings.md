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

---

## Addendum: authenticated-era resolution and unauthenticated verification (2026-07-24)

The record above is kept intact as the record of the public-claim test (2026-07-23). What
follows resolves it. Sequence, for the record: (1) the main session's authenticated API
check (the repo is the author's own) returned `{"private": true, "pushed_at":
"2026-07-23T07:16:36Z", "default_branch": "main"}` — the repo existed, was still private,
and had been pushed to that morning (his seeding work). (2) An interim instruction to this
delegate to read with ambient credentials was denied by the permission system and handed
back without workaround; no authenticated read was ever performed from this session.
(3) The author flipped the repo to public himself, 2026-07-24.

**Flag adjudication (main session, carried into the record):** only the repo owner could
execute the visibility change, and the author owns it — Merle, as a collaborator, could
not have flipped it; his letter's "public per §7" most plausibly recorded the protocol's
intent rather than an executed state. The flag stands as history (not public at check
time, 2026-07-23); the state is resolved by the author's own action, same week. The
in-file evidence below is consistent with this reading: Merle's own commit edited
PROTOCOL.md §7 to read "The repository is public" — the agreed state, written down —
while the visibility bit stayed with the owner.

### The clone, unauthenticated (the flip verified by access itself)

`git -c credential.helper= clone https://github.com/macindoe/one-obstruction-three-faces.git`
succeeded with no credentials, 2026-07-24, into the scratchpad. **HEAD:
`61d2cf30a6c53418913b8b93a345ae2fcacbfb5a`** (`61d2cf3`, "NOTE §4: make
realization-height ref renumber-proof (Ben splitting reverse.md->itinerary.md,
2026-07-23); pin section on co-edit", author Eric MERLE, 2026-07-23 09:16:34 +0200 —
matching the API `pushed_at` 07:16:36Z to the second). History since the round-6-era
base `ff379c4`: two Merle commits — `f496abe` ("Turn Merle key on L-A2; co-edit L-A3;
accept PROTOCOL 7; seed NOTE architecture") and `61d2cf3` above. Repo contents:
`README.md`, `PROTOCOL.md`, `LEDGER.md`, `NOTE.md`.

### The four blocked sub-checks, now run

#### (i) PROTOCOL.md §7 — CONFIRMED, with the in-file/executed distinction noted

§7 ("Publication") provides for the flip, condition explicit: *"This repository starts
private; making it public is proposed as the default once the protocol is agreed —
**accepted (Merle, 2026-07-19; per the correspondence: "yes to the repo, yes to the
protocol"). The repository is public.**"* So: the flip is provided for, conditioned on
protocol agreement, and the acceptance is recorded in-file (via `f496abe`). The sentence
"The repository is public" preceded the executed flip by roughly a day — the letter's
claim (d) tracked this in-file state. Recorded flat; adjudication as above.

#### (ii) LEDGER.md L-A2 — CONFIRMED, both keys, no digit mismatch

The entry carries the seeded draft (Ben, 2026-07-19; keys: his `a67970f` scripts + our
`experiments/prime_local_probe.py` and `experiments/merle_round5_check.py`) plus:
*"**Merle key turned (2026-07-19).** Independent re-verification in his stack's own
conventions (canaries hand-computed before coding): the gcd law exact, the forcing `> 1`,
and divisible-iff-base — **2,400/2,400 checks each**, random bases `p ≤ 5` × repetitions
`j = 2..5`. Artifact: `experiments/test_REQ-MATH-012_repeated_word_law.py` [pinned at his
commit `ec4f229`]. Status: **two keys**."* Against the letter's "2400/2400 exact, canary
green — two keys": no digit differs. One precision the letter compresses: the entry's
count is 2,400/2,400 **each** across the three checked clauses (gcd law, forcing,
divisible-iff-base). Consistent, not a mismatch; recorded for exactness.

#### (iii) LEDGER.md L-A3 — CONFIRMED co-edited; coherent with cycles.md 12.6.1.2/12.6.1.3

The entry carries the seeded draft plus: *"**Co-edited (Merle, 2026-07-19).** Entry text
accepted as seeded — one precision: the Merle-side artifact for the side-asymmetry is the
*adjudicated* version at commit `3b547c4` … Status: **two keys**."* — with the
collatz-lab.org/cycles/ cross-link and the framing clause (spent finite stock ⟹ every
remaining candidate needs the finite-place × archimedean coupling) in the entry text.
Coherence with cycles.md checked item by item: the four anchored cycles
`{+1} ∪ {−1, −5, −17}`, the stock exactly three with Gersonides 1342/43 (Mihailescu not
needed), `−17` the lone nontrivial-divisibility instance, the envelope
`q_+ + q_− = 2^{⌊kL⌋}`, the `log₂(3/2)`-absolute vs 50/50-ratio asymmetry with the
`k = 1` sole tie, the exhaustive `k ≤ 10` census, and the joint keys
(`a67970f` + `merle_round5_check.py`, 211,047 checks, 0 failures) all match Remark
12.6.1.2 in sense and digit. Nothing contradicts 12.6.1.3; the entry does not cite
12.6.1.3's ceiling identification (it post-dates the seeding) — observation, not a flag;
a candidate addition at co-edit time, the author's call.

#### (iv) NOTE.md — skeleton confirmed; the realization-height reference, verbatim

Skeleton shape: an architecture draft (Merle, 2026-07-19; "prose not started"), working
title *"One obstruction, three faces: the Collatz cycle problem between size, digits, and
the local–global seam,"* eight sections — §0 the porch (Gersonides front door), §1 the
problem and two shores, §2 Face I size [L1], §3 Face II digits [L-A1, L-A2], §4 Face III
the seam [L3], §5 quantitative complements [L-A3, L4], §6 what remains, §7 method — plus
appendix candidates (Lean artifact; shared test vectors; the two gateways cross-linked).
Every numbered claim enters via a turned ledger entry, as the header states.

The realization-height reference (§4, "Face III — the seam"), **exact current text**:

> The realization-height theorem (Macindoe wiki, `itinerary.md`; section renumbering in
> progress 2026-07-23 — pin on co-edit): an itinerary is realized by an integer iff its
> 2-adic and 3-adic limits coincide at a positive integer; the classical negative cycles
> reappear as diagonal points of the wrong sign.

(The "pin on co-edit" marker is deliberate, per his letter; commit `61d2cf3` made the
reference renumber-proof pending the pin.)

### Pin determination — REVISED against the verbatim text

**Final: the pin is `itinerary.md` 14.15.5(b), Corollary 14.15.5.4 (the combined
characterization), with 14.15.5(c) for the wrong-sign clause.** His stated theorem —
"realized by an integer iff its 2-adic and 3-adic limits coincide at a positive integer"
— is the first two legs of 14.15.5.4's three-way equivalence (`W` integrally realized ⟺
`y₂(W) = y₃(W)` ∈ the positive odd integers ⟺ `(H_{p,q})` bounded), and "the classical
negative cycles reappear as diagonal points of the wrong sign" is exactly 14.15.5(c)'s
negative-diagonal reconciliation (`y₂ = y₃ = −5`, integer of the wrong sign, hence not
realized). The round-1 provisional call of 14.15.9(c) is **withdrawn** — recorded, not
smoothed: it was made without the reference text, and the text names the characterization,
not the whole-period height law; the caveat recorded above (that the alternative reading
would win once the text was readable) is the branch that obtained, with the one refinement
that the statement's home is 14.15.5.4 (which cites Theorem 14.15.4.5's boundedness leg)
rather than 14.15.4(c) alone.

Two co-edit-time notes for the pin delegate, observations only: his paraphrase says
"positive integer" where 14.15.5.4 says "positive **odd** integers"; and the signed sequel
14.15.6 (negative cycles as *ordinary* periodic diagonal points of the signed
characterization, 14.15.6(d)) is the natural cross-reference if he wants the wrong-sign
clause upgraded. The pin push itself waits on the author's explicit go-ahead.

### Updated summary

| Letter claim | Final status |
|---|---|
| (a) sibling page live, back-link, DOIs | **Confirmed** (round-1, unchanged) |
| (b) L-A2 clean-room, 2400/2400, two keys | **Confirmed** against the entry; no digit mismatch ("each"-count precision noted) |
| (c) L-A3 co-edited | **Confirmed**; coherent with 12.6.1.2/12.6.1.3 |
| (d) protocol accepted; repo public per §7 | §7 acceptance **confirmed** in-file (`f496abe`); the flip was not executed at check time — historical flag stands, resolved by the author's own flip 2026-07-24 |
| (e) NOTE.md seeded, reference unpinned | **Confirmed**; verbatim text above; pin = 14.15.5(b) Corollary 14.15.5.4 (round-1 call revised) |

Shared-repo hashes relied on: `61d2cf3` (HEAD, full hash above), `f496abe`, `ff379c4`
(base of his edits, matching the round-6 record); artifact pins cited inside entries:
`ec4f229`, `3b547c4`, `a67970f`, `804a8a7`, `7d3d44a`.
