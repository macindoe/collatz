# Brief: page splits (reverse.md → itinerary.md; anchors.md → anchor-digit-search.md) + the §11.9 renumber

Date: 2026-07-23. Author-approved (2026-07-23): both splits and the renumber. Branch: create `wiki-splits` from `main`.

## Ground rules (non-negotiable)

- Read `AGENTS.md` first. These are **organizational edits only**: content moves verbatim — no rewording, no proof edits, no claim changes — except the minimal seam prose this brief specifies (front matter, stub pointers, resolver lines, repointed citations). Monolith-era and post-monolith section numbers are stable citation anchors: **no section is renumbered** except the single §11.9 → §11.10 move in commit 3.
- One commit per numbered group below, in order. Each split commit carries its own inbound-reference sweep so no commit leaves dangling pointers.
- Front-matter `updated:` on every touched page → 2026-07-23. New pages get full front matter (`status`, `scope`, `updated`, `source`) per the schema.
- After each commit, grep the repo for references to the moved/renumbered material and fix every hit in **evergreen pages** (index, README, TOUR, HANDOFF, spine, program, stage*, cycles, aeh, ladder, bridge, anchors, reverse, open-problems, publication, and the two new pages). Do NOT edit `sources/` (immutable), `briefs/` (frozen record), `archive/`, `paper/`, or `experiments/` docstrings — stale numbers there are historical record; the resolver note in commit 3 covers them.
- Do not push, do not merge; leave the branch for main-session review.

## Commit 1 — anchors.md split

Create `anchor-digit-search.md` and move §17.7, §17.8, §17.9, §17.10 into it **verbatim** (current post-consolidation text, headings and numbering unchanged — the new page owns sections 17.7–17.10).

- New page front matter: `status:` = executed search, clean at every endpoint (statistical batteries, non-automaticity screen, operation lenses, PractRand) — derive the exact phrase from the moved §17.7/§17.10 content; `scope:` = sections 17.7–17.10 (the single-sequence digit-structure search program), split from anchors.md 2026-07-23; `source:` = anchors.md (the hub retains §17.1–17.6). Give it a short Current-state paragraph (a few sentences, assembled from the moved content's own conclusions — no new claims).
- `anchors.md` keeps §17.1–17.6 and gains, where §17.7 stood, a short stub: one line per program axis (17.7 executed search — clean; 17.8–17.9 the planned axes; 17.10 standing) pointing at `anchor-digit-search.md`. Trim anchors.md's front-matter `status:` to the hub's own state (REFERENCE, pointers only) with the search outcome as one clause + pointer; update `scope:`.
- Inbound sweep for "17.7"–"17.10" and "anchors.md §17.7"-style references in evergreen pages. Known citers to check (grep to confirm and catch more): `index.md` (anchors row + Current-status paragraph), `README.md` (viz table's companion-views clause), `HANDOFF.md` (State of the fronts, AEH line), `bridge.md` (16.4.3 single-sequence endpoints bullet), `aeh.md` (if any), `TOUR.md`. Repoint to `anchor-digit-search.md`; the section numbers themselves do not change. Add the new page's row to `index.md`'s Pages table and the resolver: `§17.1–17.6 → anchors.md · §17.7–17.10 → anchor-digit-search.md`.

## Commit 2 — reverse.md split

Create `itinerary.md` and move **all of §14.15** (the `## 14.15.` heading through the end of the file, i.e. 14.15.1–14.15.9 including the 14.15.7/14.15.8 stubs) into it verbatim; numbering unchanged — the new page owns §14.15.

- New page front matter: `status:` = itinerary language closed at finite level (full shift); two-sided coding and signed three-way diagonal characterization complete; whole-period height laws closed (14.15.9) with the q-dichotomy; open front = periodic cycle exclusion (q = 1 beyond the known instances); the Bridge unchanged. `scope:` = section 14.15 (post-monolith), split from reverse.md 2026-07-23. `source:` = reverse.md (built on the door/exit seam, 14.14). Current-state paragraph: extract the 14.15-specific half of reverse.md's current Current-state callout (the full-shift/coding/heights sentences), verbatim where possible.
- `reverse.md` keeps §14.1–14.14 and gains, where §14.15 stood, a short stub under a `## 14.15.` heading: the itinerary language now lives at `itinerary.md` — one sentence naming what it contains (cylinder theorem, two-sided coding, signed diagonal characterization, whole-period height laws) and one line noting the accounting owner 14.14.6 stays here. Rewrite reverse.md's front-matter `status:`/Current-state to cover §14.1–14.14 with one pointer sentence to itinerary.md for the 14.15 arc; update `scope:`.
- **Dependency note to preserve:** itinerary.md builds on 14.14's `G`/stratum coordinates and cites 14.14.x, 14.2, 14.6 etc. — those citations stay as-is but gain "(reverse.md)" qualifiers ONLY where the moved text's existing style leaves the target page ambiguous; where the text already says a bare `14.14.x`, add the page name at first use per subsection, minimally. Conversely reverse.md's remaining text cites 14.15.x in a few places (e.g. 14.14.8's composed-fixed-point remark, the 14.14.6 accounting) — qualify those with "(itinerary.md)" at first use.
- Inbound sweep for `14.15` references in evergreen pages. Known citers (grep to confirm and catch more): `index.md` (reverse row — split its long description: the 14.15 clauses move to a new itinerary.md row; resolver: `§14.1–14.14 → reverse.md · §14.15 → itinerary.md`; Current-status paragraph), `bridge.md` (16.1 itinerary-language paragraph, 16.4.5's door/exit-seam bullet and equivalent-names block), `cycles.md` (12.6.1.1 "Lemma 14.15.9.2 (reverse.md)" → itinerary.md; 12.6.1.2 census cross-frame), `open-problems.md` (11.6 calibration note → 14.15.2; the §11.9→11.10 section's pointer, see commit 3), `HANDOFF.md` (fronts dashboard; Merle pointers "reverse.md 14.15.9(a)" → itinerary.md), `stage4.md` (11.8.7.3.1 mirror pointer if any), `aeh.md` (13.2 symbolic-form pointer → 14.15.2), `ladder.md` (15.4 cites 14.10 — stays reverse.md), `anchors.md`/`anchor-digit-search.md` (17.3 pointers to 14.14/14.15.9 — 14.14 stays, 14.15.9 repoints), `README.md` (viz table's stratum_word_ticker clause if it cites 14.15), `TOUR.md`, `publication.md` (14.15.x verdict lines).

## Commit 3 — §11.9 → §11.10 renumber (open-problems.md)

The post-monolith "Per-letter (period-cutting) window height laws" section in `open-problems.md` currently numbered 11.9 collides with the monolith's §11.9 (program.md, Closing Perspective — immovable). Author-approved renumber to §11.10.

- First verify §11.10 is unused repo-wide (grep `11.10`; word-boundary aware — beware matches inside other numbers). If somehow taken, STOP this commit and report.
- Rename the heading to `## 11.10. Per-letter (period-cutting) window height laws`; update open-problems.md front-matter `scope:` line accordingly.
- Update every editable inbound citation of the post-monolith 11.9: `itinerary.md` (the 14.15.9 scope note's two mentions, formerly reverse.md), `index.md` (Pages-table row for open-problems + resolver — the resolver's post-monolith 11.9 entry becomes: `§11.10 (post-monolith; recorded as 11.9 in pre-2026-07-23 briefs) → open-problems.md`, and the monolith line reverts to plain `§11.8.8, §11.9 → program.md`), plus any other evergreen-page hits the grep finds.
- `briefs/periodic-shelf-brief.md` and other briefs citing "open-problems.md 11.9" are frozen record — do NOT edit; the resolver note above is the bridge for those readers.

## Commit 4 — final integrity sweep

- Grep for dangling references: every `14.15` hit in an evergreen page must say itinerary.md (or be inside itinerary.md); every `17.7|17.8|17.9|17.10` hit must say anchor-digit-search.md (or be inside it); no evergreen page cites a post-monolith `11.9` any more.
- Verify byte-accounting: report old/new sizes of reverse.md, itinerary.md, anchors.md, anchor-digit-search.md, and confirm moved content is verbatim (e.g. diff the extracted section text against the pre-split file where practical).
- Confirm index.md's Pages table, resolver, and Current-status paragraph are mutually consistent and match every touched page's front matter.

## Final report

Return: per-commit summary; the four page sizes before/after; the grep evidence for §11.10 being free; the list of frozen files still citing old locations (briefs/sources — expected, unedited); anything skipped with reason.
