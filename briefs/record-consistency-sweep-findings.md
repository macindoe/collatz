# Findings: record-consistency-sweep — the five items left after the staircase arc (2026-07-29)

Brief: `briefs/record-consistency-sweep-brief.md`. Branch `record-consistency-sweep`.
**Base SHA `ece5e0c`** — the worktree was cut from `3eab8f1`, which does not
contain the brief; the branch was rebased onto `ece5e0c` before any work began.

Five per-item commits, structure separate from content. **Not merged, nothing
pushed.** `paper/`, `sources/`, `cycles.md`, `viz/`, and all ledger and
correspondence material are untouched. **No claim, constant, status word or
piece of mathematics was changed anywhere**; no item turned out to require one.

`python experiments/encoding_scan.py`: **CLEAN**. Every edit was made with the
Edit/Write tools; PowerShell touched no tracked file.

| commit | file(s) | item |
|---|---|---|
| `e4d5ca4` | `experiments/` ×3 | 1, the mis-resolving citations |
| `bdb84da` | `TOUR.md` | 2, the floor-grade entry |
| `0603f5d` | `HANDOFF.md` | 3, the duplicate item numbering |
| `0e6902e` | `briefs/staircase-allp-findings.md` | 4, the supersession header |
| `c11e3c7` | `README.md` | 5, line 53 |
| (this commit) | `briefs/`, `HANDOFF.md` | this record; one scoped paragraph |

---

## 1. The `experiments/` citations

Sixteen citations of `12.8.6.2` exist across `experiments/`, not the seven
sites the apply findings list. Each was read in context and sorted three ways.

### 1.1 Repointed (3 sites, all in comments or docstrings)

Each names the object as well as the number, so the citation survives the next
renumbering rather than depending on it.

| site | what it means | now reads |
|---|---|---|
| `merle_pincer_check.py:19` | header, naming the formulas the script implements | the pure-geometric base profile of the superseded recipe, `12.8.6.3`, explicitly *not* Construction B |
| `merle_pincer_check.py:374`, `:473` | docstrings of `construct_12_8_6_2_fresh` and its caller | the same, plus a line saying the **function name is a code identifier, not the citation** |
| `merle_round3_check.py:421`, `:424` | docstring of `base_construct` | the same |
| `staircase_allp_construction.py:250` | docstring of `base_geometric` | the same, and named as **the negative control** — the profile lacking the additive `1/(L-1)` offset |
| `staircase_allp_construction.py:510` | PART 2 banner comment | the same, with a clause redirecting the printed text of that Part |

All six are the genuine article: each function builds the *pure* geometric
profile with partial-sum rounding, which is the superseded route, now
`12.8.6.3`. Verified by reading the code, not by the recorded list.

### 1.2 Left alone: printed output (7 sites)

The brief forbids output changes and prescribes re-running each edited script
against its committed output as the check — which is only possible if printed
strings are out of scope. So every citation inside a `print`/`hdr` argument
was left as it stands, **even where the number now mis-resolves**:

* `p22_passer.py:170`, `:180` — "construction 12.8.6.2 + N correction moves of 12.8.6.3"
* `prime_local_probe.py:939` — "the staircase recipe (12.8.6.2)"
* `staircase_allp_construction.py:496`, `:514`, `:791` — the PART 1b/2 and NC-B banners
* `staircase_allp_diophantine.py:1010` — "Recipe of 12.8.6.2 + 12.8.6.3"

Two of these scripts have committed output files (`staircase_allp_construction_output.txt`,
`staircase_allp_diophantine_note.txt`), so editing them would have required
regenerating committed output for a section number. **Flagged for the main
session:** these seven remain stale in the sense that matters to a reader who
runs the script rather than reads it. Repointing them is a real decision — it
costs a regenerated output file — and it was not this window's to make. The
banner comment now added at `staircase_allp_construction.py:509` tells a reader
of that Part which object its own printed text means.

### 1.3 Left alone: resolves correctly, or is not the construction (6 sites)

* **`experiments/staircase_allp.py` — a recorded site that is not one.** The
  apply findings list it as a `Construction 12.8.6.2` site. It contains no
  `12.8.6.2` at all: lines 1, 6 and 44 cite the **section**, `12.8.6`, and line
  6 names its contents in words ("Diophantine input lemma, explicit staircase
  construction, bounded correction algorithm, verified-instance record"). A
  section citation still resolves. Untouched.
* `staircase_allp_construction.py:7` — "the proposed replacement of Algorithm
  `12.8.6.3` (the bounded correction search)". Still correct: `12.8.6.3` is
  still the correction. Untouched.
* `staircase_allp_construction.py:552`, `merle_pincer_check.py:501`, `:511` —
  "algorithm `12.8.6.3`". Correct as written.
* `merle_pincer_check.py:81`, `:214`, `:664`, `:681` — "lemma `12.8.6.1`"'s
  sign-filtered grid. Resolves in one hop via the superseded-formulation
  paragraph inside `12.8.6.1`, which was kept for exactly this. Untouched.
* Every `12.8.6.4` citation (`make_transport_vectors.py`, `merle_round3_check.py`,
  `p22_passer.py`, `prime_local_probe.py`, `staircase_allp_diophantine.py`,
  `staircase_allp_construction.py`) — the instance record kept its role in the
  rewrite. Untouched.
* `staircase_allp_diophantine.py:6` — "the floor-grade result at cycles.md
  12.8.6". A status word, and the brief forbids changing one. Untouched.

### 1.4 One thing not done, and why

`merle_pincer_check.py`'s function is named `construct_12_8_6_2_fresh`. Renaming
it would not change behaviour, but it is **code**, which the brief excludes.
The docstring now says the name is an identifier and not the citation. Recorded
rather than repaired.

### 1.5 No behaviour or output changed — confirmed, not assumed

Three independent checks:

1. **Parse-tree equality.** For each of the three edited files, `ast.dump` of the
   committed version and of the edited version are **identical once docstrings
   are stripped**. Every statement, expression and non-docstring string literal
   is unchanged — which is a stronger statement than "the diff touches only
   comment lines", since it is checked on the compiled tree rather than by eye.
2. **Docstrings are never read.** None of the three files contains `__doc__` or
   `help(`, so no docstring can reach the output.
3. **Re-runs.** `staircase_allp_construction.py` reproduces its committed
   `staircase_allp_construction_output.txt` **byte-for-byte except for two
   wall-clock timing columns and the total wall-clock line** (`32.0`→`31.6`,
   `95.4`→`93.5`, `407.6 s`→`401.1 s`) — machine speed, not content.
   `merle_round3_check.py` re-runs clean: **29,211 exact checks, 0 failures**.
   `merle_pincer_check.py` is expensive (three correction runs at a 240 s
   deadline each), so instead its edited function and the docstring-bearing
   caller were executed side by side against the committed version's, in the
   same interpreter: `construct_12_8_6_2_fresh` returns identical profiles at
   `(p,n) ∈ {(22,25217), (22,31202), (7,94), (23,47468), (12,140)}`, and
   `item2b_literal_n_rows()` returns an identical string.

---

## 2. `TOUR.md`'s floor-grade entry — **repointed, not retired**

The premise that the entry is unattached holds for the wiki pages and **not for
the tree**. `floor grade` is still carried by:

* `paper/collatz-reduced-v2-review.md` lines 9, 14, 161 — three uses, naming the
  delegated session's outcome. `paper/` is frozen and out of scope, so those
  uses cannot be updated to some other word.
* sixteen files under `briefs/`, including `briefs/staircase-allp-findings.md`,
  which `TOUR.md` line 23 already points a reader at by name.

`README.md` line 5 makes `TOUR.md` the trailhead **for readers arriving from the
papers or from correspondence** — precisely the readers who will meet the word.
Retiring the definition would strand them. So the entry keeps its definition
verbatim and now names its live carrier: no wiki section stands at the grade; it
grades the superseded earlier staircase attempt, which is what the published v2
note reports, and which `cycles.md` 12.8.6 replaced with a proof.

The precedent is one line above it in the same list: the **assessed** entry
already handles a word that stands in print while the wiki has moved past it.
That is the same situation, and it is now handled the same way — which is why
this reads as consistency rather than as a change log.

Nothing else's status vocabulary depended on the entry, so the retire branch's
check was not needed; it is recorded here because it was the question asked.

---

## 3. `HANDOFF.md` numbering

The list ran `1,2,3,4,4,5,5,6,7` — two collisions, from sessions appending in
parallel. Now `1…9`, in the order the items already stood. Two internal
cross-references moved with their targets: "item 5's gate (P1)" → item 6, and
"(item 6)" → item 8.

**No paragraph was reworded, reordered, consolidated or summarised.** The whole
diff is seven numerals, confirmed by `git diff --word-diff`.

Five other `item N` references in the file point at numbered items **inside**
`briefs/` findings files (`merle-la8-t1`, `merle-lean-r10`, `staircase-allp`
item 5.3, and two in the round-11 material). Those are not this list and were
left alone.

---

## 4. `briefs/staircase-allp-findings.md`

One header line, immediately under the title. It names the route, says its
target is *refuted as a target* rather than unachieved — quoting `12.8.6.3`'s own
wording, not grading anything afresh — points at the three findings files that
replaced it, and warns that the sub-numbers cited in the body are pre-rewrite,
so this file's "12.8.6.2" is the pure-geometric profile now numbered 12.8.6.3.

That last clause is worth its words: the body cites `12.8.6.2` the same way the
`experiments/` scripts did, and this is the cheapest place to say so once.

The body is unchanged, including its own 2026-07-17 update section, which covers
only the `p = 22` obstruction and predates the three closing sessions.

---

## 5. `README.md` line 53

Was: "the uniform trim lemma is the open objective". Now: "the uniform trim
resolved, and its sharpness family constructed at every period (12.8.6)".

One clause. It states **no grade** — "constructed at every period" is line 17's
own already-reviewed wording, and the scope (`p ≥ 16` unconditional, finite check
below, `p ∈ {2,4}` by exhibition) stays where it belongs, in the section. Line 17
and line 34 already read correctly and are untouched, as are all three stopping
rules at line 36.

---

## 6. For the reviewer

1. §1.2 is the one place this window left a known defect standing. Seven printed
   citations still say `12.8.6.2` where they mean the superseded profile. The
   fix is not free — two committed output files would need regenerating — so it
   wants its own decision, not a silent repair.
2. §2 reverses the premise the brief was written on. If the intent was to retire
   the entry regardless of `paper/` and `briefs/` usage, this is the item to
   send back.
3. Nothing here is ledger, note, correspondence or shared-repo material.
