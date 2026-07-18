# Brief: the cycle-side gateway visualizer (for a delegated session)

**Context required before starting (in order):** `AGENTS.md` (register norm; verified-numbers discipline), `briefs/merle-round5-check-findings.md` (entire — the single source of truth for every number displayed), `viz/block_family_decomposer.html` and `viz/stratum_word_ticker.html` (the two existing gateways — match their conventions: self-contained single-file HTML, no external requests, explainer voice, header/footer style), `cycles.md` 12.5–12.6.1.1 (the frame the viz teaches), `HANDOFF.md` item 1 (why this exists: the collaboration's gateway layer; Eric Merle builds a sibling on his side and the two will cross-link).

**Before writing any chart code, load the `dataviz` skill** and follow it for palette construction, mark specs, and light/dark behavior.

## Purpose

The third gateway viz, aimed at the cycle side: the on-ramp a lay-but-willing reader takes *before* the papers or the joint note. It tells the round-5 story — loops are real, each anchored to a near-miss of the two towers; the free stock (`|q| = 1`) is exactly three and spent since 1343-level arithmetic; the one lottery win is −17; the side-asymmetry is Benford — using the colour-matching system below. File: `viz/cycle_anchor_gateway.html`. One file, self-contained, no CDN, no fonts fetched, works from `file://`.

## The colour-matching system (the design's one idea — carry it strictly)

- **House colours:** one colour per known cycle (+1, −1, −5, −17), constructed per the dataviz skill's categorical formula. The SAME colour marks that cycle's orbit loop, its anchor near-miss on the tower ladder, and its rows/points in the k-map strip. Hovering a house anywhere highlights its objects everywhere.
- **Sector hues:** a north (positive) and south (negative) hue pair; the Benford walk's points inherit these. House colours for −1, −5, −17 should read as belonging to the south family, +1 to the north family (shade variation within the family).
- **The `q` accent:** ONE reserved accent colour for `q` wherever it appears — the gap bar on the ladder, the divisor in the cycle equation `x_r · q = R_r`, the modulus in the transport recurrence. Same object, three costumes; the accent teaches the identification.

## Panels, in narrative order

1. **The two towers and the near-miss ladder.** Powers of 2 and 3 on a log axis (BigInt values, exact); for each k a gap bar between the flanking powers of 2, split `q₊ | q₋` — the envelope identity `q₊ + q₋ = 2^⌊kL⌋` visible as the bar exactly filling the gap. The three `|q| = 1` locks (2-3, 4-3, 9-8) glow in their house colours; k = 7 shows −139 as the lottery win; k = 1 is flagged as the unique exact tie (`q₊ = q₋ = 1`).
2. **The four houses as orbits.** The actual loops drawn — 1; −1; −5 ⇄ −7; the seven-element −17 loop (−17, −25, −37, −55, −41, −61, −91) — house-coloured, each labelled with its `(k, m, q)` anchor. Caption carries the moral: loops are real, so any parity/speed argument that forbids loops proves too much.
3. **One condition, not p.** Pick a word (presets: the −17 word `(1,1,1,2,1,1,4)`, a random k = 5 word); spin its rotations; show `q | R_r` holding or failing at ALL rotations simultaneously — rotation-invariance (the transport recurrence, Remark 12.6.1.1 / ledger L-A1) as the visible gear. Exact BigInt arithmetic for the divisibility verdicts.
4. **The repeated-word sweep.** Choose a base word and a repetition count j; display `gcd(q_P, R_0) = |q_P|/q_red(B)`, forced > 1 for j ≥ 2 (ledger L-A2): the repeated word falls back onto its base's house colour (default demo: the k = 5 all-2s word collapsing onto +1's colour, `q_P = 781`, gcd = 781). Exact BigInt.
5. **The Benford walk.** `{k·log₂3}` on [0,1) with the `log₂(3/2)` threshold line; points sector-coloured by which side wins the absolute near-miss; a running-fraction readout converging to 58.5%; a toggle to the ratio question (threshold ½, split 50/50) captioned "both answers are right — to different questions; divisibility lives on q as an integer, so the additive one is the cycle-relevant one." Win/lose decisions by exact BigInt comparison (`2·3^k` vs `3·2^⌊kL⌋`); float only for plot positions. Range k ≤ 2000 is plenty; k = 1 marked as the tie.
6. **The spent stock.** The closing panel: three tickets, dealt by k = 2 (one north, two south), never another — badge the result "Gersonides, 1343" (De numeris harmonicis; the viz does not mention Mihailescu) — then the wall: every later candidate needs `q | R₀` nontrivially; −17 the single known win (139, prime, word primitive); the k ≤ 10 strip: 250,952 profiles checked, 37 divisible, all 37 the known houses. End-line, flat: what remains is exactly the open question, and it needs the two-towers geometry and the divisibility arithmetic coupled — no finite place alone will do it.

**Shared interaction:** a k-slider (1..~60 for the ladder) shared where meaningful; house-hover cross-highlighting across all panels (the colour-matching payoff). Keep it vanilla JS, no frameworks.

## Rules

- Every displayed number that states a result (the anchor table, 139, 781, 250,952, 37, 384, 58.5%, log₂(3/2) = 0.5849625007, the k = 1 tie, 211,047/0) is transcribed from `briefs/merle-round5-check-findings.md` — no new claims, no re-derivation in prose. In-page BigInt computation is for interactive panels' live verdicts only and must agree with the findings where they overlap (spot-check in the report).
- Register flat, including captions: heuristics labeled, nothing sold. The word "proof" appears only where the findings use it.
- Explainer text at the level of the two sibling viz — a willing lay reader, no prerequisites; symbols introduced before use.
- Light and dark themes both styled (dataviz skill rules); page never scrolls horizontally.
- A cross-link slot for Eric Merle's sibling gateway (placeholder text + href="#" clearly marked TODO until his exists).
- Credit line in the footer: the spent-stock framing due to Eric Merle (round-5 correspondence); verification joint; link the two DOIs like the sibling viz do (10.5281/zenodo.21421120, 10.5281/zenodo.21303918).
- Branch **`cycle-gateway-viz`**, commits as you go (at minimum: skeleton, panels, polish), do NOT merge — the main session reviews (including opening the file and exercising every panel) before merging.
- Only `viz/cycle_anchor_gateway.html` (plus this brief's findings notes if needed in your report) — touch nothing else. No scope expansion.

## Definition of done

The file opens from disk with no network access, both themes clean, all six panels present with the colour system carried strictly, house-hover cross-highlighting working, every stated number matching the findings file, the L-A1/L-A2 panels' live arithmetic exact (BigInt), the cross-link slot present, and a report listing: panel-by-panel what was built, the spot-check table (live verdicts vs findings numbers), and any deviations with reasons.
