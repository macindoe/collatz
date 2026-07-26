# Brief: the stratum field explorer — `anchor_field_explorer` on `(m, r)` (for a delegated session)

**Context required before starting (in order):** `AGENTS.md` (register norm; verified-numbers discipline), `viz/anchor_field_explorer.html` (**the template — read it whole; this is a sibling, not a new genre**), `itinerary.md` 14.15.1 (Definition 14.15.1.1, Lemma 14.15.1.3, Theorem 14.15.1.5) and 14.15.2 (the full-shift consequence), `aeh.md` §13.6 (Lemma 13.6.1, the letter law) and §13.1–13.5 skim for the bulk/bottom distinction, `stage4.md` 11.8.7.7 (the digit budget), `viz/stratum_word_ticker.html` intro paragraphs only (**to avoid overlap** — that page teaches what a letter *is* at bit level; this page must not re-teach it).

**Before writing any chart code, load the `dataviz` skill** and follow it for palette construction, mark specs, and light/dark behavior.

## Purpose

The author asked for `anchor_field_explorer` "on the coordinates of `(m, r)` instead of `(ω, d)`". File: **`viz/stratum_field_explorer.html`**. One file, self-contained, no CDN, no fonts fetched, works from `file://`. **Tight companion register** — match `anchor_field_explorer.html` exactly in size and shape (~8–14 KB; one canvas, one mode dropdown, one intro paragraph, hover tooltip, click-to-trace panel). This is **not** a gateway page; do not write a teaching essay.

## The one thing that must not be got wrong

`(ω, d)` is a **state space**: each cell *is* a state, `F` maps cell → cell, an orbit is a path on the grid. `(m, r)` is an **alphabet**: each cell is a residue class mod `2^(m+r+1)` containing infinitely many doors `y` (Lemma 14.15.1.3(i)), and **there is no map on the plane** — the successor letter depends on which `y` you are at, not on the cell.

Consequences that are binding on the design:

- The intro paragraph must say this in one sentence, plainly. A reader must not come away thinking the `(m,r)` plane carries dynamics.
- Modes 2, 3 and 4 below are all properties of **one chosen representative** of the class — the smallest positive **live** (`3 ∤ y`) door on that stratum. Every tooltip and caption for those modes must name the representative explicitly (show the actual `y`), never present the value as a property of the letter itself.
- Click-to-trace is therefore **not** "the cell's orbit". It is: click a cell → take its smallest live witness `y` → walk `y`'s forward letter word `(stratum(G^i(y)))_i` as a polyline across the plane. Label the panel accordingly.

## The four modes (one `<select>`, exactly as the template's `mode` dropdown)

### Mode 1 — `letter law` (default): empirical ÷ exact, bulk vs bottom

Colour = observed letter frequency ÷ the exact Bernoulli mass `2^−(m+r)` (aeh.md Lemma 13.6.1), on a **diverging** ramp centred at 1.0. A second control (radio pair or a second `<select>`) switches the sample:

- **bulk** — fixed-horizon, unweighted, above a cut, per aeh.md's standing sampling rule: `N = 4000` random odd starts below `2^160`, at most `H = 25` letters each, stop early if `y ≤ 2^48`. Pre-checked in the main session: **≈100,000 letters, worst ratio deviation 0.076 over all `m, r ≤ 4`** — i.e. the field reads flat.
- **bottom** — every odd start `3 ≤ y < 20001`, run to `1` (step cap 500). Pre-checked: **162,979 letters**, and the field is visibly wild — `(1,1) → 0.842`, `(1,3) → 2.029`, `(3,3) → 0.383`, `(3,4) → 3.813`.

The contrast between the two samples is the point of the mode, and it is exactly aeh.md §13's bulk/bottom distinction. Caption it flatly in one clause; do not editorialize and do not claim anything about AEH's status.

**Required guard:** cells whose *expected* count under `2^−(m+r)` falls below ~20 are statistically meaningless at these sample sizes. Render them in a neutral "insufficient sample" treatment (hatch or muted grey), not as a coloured ratio, and say so in the legend. Getting this wrong would paint sampling noise as structure — the exact failure mode aeh.md §13.5 records.

**Determinism:** the bulk sample must use a small seeded PRNG written into the file (e.g. mulberry32/xorshift with a fixed seed) — **not `Math.random()`** — so the picture is reproducible and the numbers are checkable. State the seed in the page.

### Mode 2 — `witness price`

Colour = bit-length of the smallest live door realizing the letter, on a sequential ramp. This is the digit budget (stage4.md 11.8.7.7) as a picture: the letter costs `m+r+1` bits and the witness sits at roughly the class modulus. Main-session pre-checked values (`y`, smallest live):

```
r=4 |   53    35    23   527  1375  3647
r=3 |    5    67   215   143    95  1087
r=2 |   13    19    55    79   223   319
r=1 |    1    11     7    47    31   191
      m=1     2     3     4     5     6
```

Show the numeral in-cell where it fits.

### Mode 3 — `successor structure`

From each cell's smallest live witness, colour by the **next** letter's `m` (categorical palette; offer `r` as well if it costs nothing). The picture is structureless, and that is the content: the itinerary language is the full shift, no forbidden word and no forbidden transition, so no finite-state admissibility graph exists to find (itinerary.md 14.15.2). One caption clause pointing at 14.15.2. **Do not** imply the plane has a transition map — this is the successor of a chosen representative and the tooltip must say so.

### Mode 4 — `q, by order of magnitude`

Colour = `log2(q)` of the smallest live witness, where `q = (y+1)/2^m` — the odd payload the block carries into the tripling. Main-session pre-checked `q` values:

```
r=4 |   27     9     3    33    43    57    19    17
r=3 |    3    17    27     9     3    17    27     9
r=2 |    7     5     7     5     7     5     7     5
r=1 |    1     3     1     3     1     3     1     3
      m=1     2     3     4     5     6     7     8
```

Over `m, r ≤ 12` the range is `q ∈ [1, 15019]` (`log2` up to 13.9), all `q` odd, witnesses up to 26 bits — so a log ramp is the right choice and the author's instinct here is correct.

**The visible banding has an explanation, and you must check it before stating it.** Lemma 14.15.1.3(i) pins `q ≡ 3^(−m)(1 + 2^r) (mod 2^(r+1))`, so the smallest such `q` is constant along `r` up to the period of `3^(−1)` mod `2^(r+1)` in `m` — which would predict period 2 at `r=1,2` and period 4 at `r=3`, matching the rows above. Verify this independently with your own code; if it holds, one clause in the caption pointing at 14.15.1.3(i); **if it does not hold exactly, show the field with no explanation and record the mismatch in your report.** Do not assert the mechanism on the strength of four rows.

## Grid and interaction

- Extent `1 ≤ m, r ≤ 12` (masses below that are `< 2^−24`; nothing is lost). Unlike the template's 88×44 micro-cells, use large cells (~34–44 px) so numerals fit. `m` on x, `r` on y, `r` increasing upward — mirroring the template's `d`-up convention.
- **Hover tooltip** (all modes): the letter `(m,r)`; its exact Bernoulli mass `2^−(m+r)`; its class — one residue class mod `2^(m+r+1)`, give the residue; the smallest live witness `y` with its `q`; and the mode-specific value. BigInt where needed.
- **Click** → trace the witness's forward letter word as a polyline with dots, exactly as the template draws orbits (first dot larger/accented), plus a monospace word panel below listing the letters in order. Cap at ~40 letters like the template. Letters landing outside the 12×12 view break the polyline, same as the template's `c===null` handling.
- Reuse the template's structure wherever you can — canvas sizing with `devicePixelRatio`, the `cellAt` hit test, the tooltip element, the legend row, the orbit panel, the `clear` button, the CSS custom-property theme block. Vanilla JS, no frameworks.

## Rules

- **Performance:** modes 1's two samples are ~100k and ~163k BigInt `G`-steps. Compute **lazily** (only when the mode is first selected), cache the result, and show a brief "computing…" state. Measure actual wall time and report it. If either sample exceeds ~2 s on a normal machine, reduce it (halve `N`, or raise the bottom-mode start bound less far) and report the sizes you shipped and the deviation they give — do **not** silently ship the numbers quoted above if you changed the sample.
- Every number the page *states as a result* must be either computed live in the page or transcribed from this brief. Re-derive the tables above with your own code before shipping and report any disagreement as a finding rather than quietly matching the brief.
- Register flat. No claim about AEH's status, the Bridge, or the conjecture. `2^−(m+r)` is a proved exact law (aeh.md 13.6.1); the empirical panels are empirical and must be worded as such.
- Light and dark themes both styled (dataviz skill rules); page never scrolls horizontally; the canvas keeps its aspect ratio on narrow screens.
- Footer/companion line: check `publication.md` for which paper actually covers the door/stratum material and cite that DOI in the template's style. If neither paper covers §14.15, cite the wiki sections only — **do not** copy the template's DOI line unexamined.
- Branch **`stratum-field-explorer`**, commits as you go (at minimum: skeleton + grid, the four modes, polish). Do **not** merge — the main session reviews (opening the file, exercising every mode, re-running the samples) before merging.
- Files: `viz/stratum_field_explorer.html`, plus **one separate commit** adding the page to the `viz/` row of `README.md`'s repository map (one clause, matching the existing entries' voice). Nothing else — no wiki-page edits, no `TOUR.md`, no new `experiments/` script.

## Definition of done

The file opens from disk with no network access; both themes clean; all four modes present in one dropdown with the bulk/bottom sub-control on mode 1; the insufficient-sample guard visibly working; hover and click-to-trace working with the representative named honestly in every mode that uses one; the intro's alphabet-not-a-state-space sentence present; the README row added in its own commit; and a report giving: mode-by-mode what was built, your independently recomputed versions of the three tables above (witness, `q`, and the four bulk/bottom ratios) against the brief's values, the sample sizes and wall times actually shipped, the verdict on the mode-4 banding explanation, and any deviations with reasons.
