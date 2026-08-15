# Brief: symbols.md — the wiki-wide symbol registry (for a delegated session)

**Context required before starting (in order):** `README.md`, `AGENTS.md` (one-fact-one-page and current-answer norms — the registry is pointers, never a second home for a fact), `index.md`, `spine.md` §3–§4 (the note's own Dictionary of Symbols, which this page subsumes by reference and must not edit), then the frame home sites as you sweep them per the queue.

## Provenance and principle

A containment audit (2026-08-15, this session) found the wiki's notation has outgrown its only lookup surface. `spine.md` §4 is the original note's dictionary and stops at the spine's four layers; everything since — the stage digit cost, the cycles numerator frame, the door/itinerary coding, the signed layer, the anchors — has no lookup page. The cost is now measured, not hypothetical: `σ` carries four meanings across the wiki, `q` at least three, `m`/`r`/`n`/`K`/`M`/`S`/`R`/`a` differ by frame, and the numeral `0.585` names two different quantities. No single file currently mixes two meanings of one glyph — the collisions are harmless only by that luck, and the author has been bitten in practice (reading `q | R_0` with the wrong `q`).

**The page's charter: lookup and collision visibility, nothing else.** One new top-level page, `symbols.md`. One row per symbol **per frame**. A row is: glyph | one-line meaning | defining pointer | elsewhere (cross-links to the same glyph's other rows). Meanings are one line, no restated theorems, no new claims; every fact stays on its owning page and the registry points at it. Pointers cite **file + section/definition number** (e.g. `cycles.md` Proposition `12.6.1`), never line numbers.

## Structure of the page

1. Three-line preamble: what the page is, and the standing norm it enforces — *a session introducing notation checks this page first; a new symbol gets a row with its defining pointer; a reused glyph gets its collision cross-linked in the same commit.*
2. Per-frame sections, one per queue item below.
3. A closing **Collision index**: every glyph with two or more rows, listed once with all its meanings side by side, plus the numerical-constant collisions.

## Queue: the frames, in sweep order

For each frame: read the named home sections, extract the recurring symbols, write the rows, verify every pointer resolves (open the cited section and confirm the glyph is actually defined there — no pointer goes in unverified).

1. **Spine / block frame** (`spine.md` §3–§5): `T`, `x`, `(u,m)`, `E`, `a`, `ω`, `d`, `(ω,d)`, `R`, `F`, `A`, `s`, `x_exit`, the `₊` family. Rows point to spine.md §3/§4; do not duplicate §4's prose — one-line meanings only.
2. **Stage / digit frame** (`stage3.md`, `stage4.md`, `reverse.md`, `anchors.md`, `ladder.md` as they define, not merely use): the digit cost `σ = v₂(C) = s + m₊`, `C`, `N(c)` and the target family `c`, the anchor/ladder targets (`1 − 2^s`, `3^{−k}`), the drift constant `log₂3 − 1 ≈ 0.585`. Sweep for others that recur across files.
3. **Cycles numerator frame** (`cycles.md` §12.5–§12.6, esp. Proposition `12.6.1` and Remarks `12.6.1.1`–`12.6.1.4`): profile `(m_t, s_t)`, `n = Σ m_t`, `K = Σ s_t + n`, `q = 2^K − 3^n`, the rotation numerators `R_r`, the tail sums `M_t`, `S_t`, `σ_j = s_j + m_{j+1}`, `ω_t`, `G_k` (the repetition factor of `12.6.1.4`). Include the **odd-step frame renaming** of `12.6.1.2`/`12.6.1.3` — `(k, m, q)` with `K ↔ m`, `n ↔ k` — as its own sub-block with an explicit warning row: same equation, renamed letters.
4. **Door / itinerary frame** (`itinerary.md` §14.14–§14.15, definitions at `14.15.1.1`, `14.14.8.4`, `14.15.3`, `14.15.4.3`, `14.15.9.1`–`14.15.9.2`): door `y`, `stratum(y) = (m,r)`, `G`, letters/words `W`, the masses `M_n`, `S_n`, `M_P`, `S_P`, `M(W)`, `S(W)`, the adelic limits `y₂`, `y₃`, the composed fixed point `y^*` with `α`, `β`, the reduced form `y^* = a/q` (this `q` and this `a` are NOT frame 3's — this is the flagship collision, cross-link it hard), the realization sets and heights `R_{p,q}`, `H_{p,q}` with window `(p,q)` (a third `q`), `Q_n`, `ρ_n`, `j_n`, `t_n`, `k₀`.
5. **Signed layer** (`itinerary.md` §14.15.6–§14.15.9): the sector sign `σ ∈ {+1,−1}`, `R^σ`, `H^σ`, `H^±`, `k^±`, `V_±`, `Spec_σ`, `c_σ`, `κ`.
6. **AEH / measure frame** (`aeh.md` §13): the shift map `σ`, `X_sing`, and whatever else recurs (sweep; standard-deviation and exponent usages of Greek letters are prose, not registry rows — include only symbols with a definition site).
7. **Collision index.** At minimum the seeded set — `σ` (×4), `q` (×3+), `m`, `r`, `n`, `K`, `M`, `S`, `R`, `a`, `k` — plus every additional multi-row glyph the sweep surfaces, plus the constants entry: `0.585` as `log₂3 − 1` (drift, `stage1.md`/`reverse.md`/`cycles.md` §12.5) vs `log₂(3/2)` (side-asymmetry density, `cycles.md` `12.6.1.2`). Verify each seeded collision during the sweep; if one is wrong, record that in the findings file rather than forcing it into the page.

## Scope

Main wiki pages only: `spine.md`, `reverse.md`, `stage1.md`–`stage4.md`, `stage1-synthesis.md`, `aeh.md`, `anchors.md`, `ladder.md`, `bridge.md`, `cycles.md`, `itinerary.md`, `open-problems.md`, `program.md`, `anchor-digit-search.md`. Out of scope: `briefs/`, `sources/`, `archive/`, `paper/`, and external-notation pins (e.g. Simons–de Weger's `H`/`K`/`L` quoted inside `cycles.md` `12.5` stay where they are — the registry covers the wiki's own recurring notation only).

## Rules (non-negotiable)

- Lookup only: no theorem restated, no claim made, no fact re-homed. A row's meaning is one line.
- Every pointer verified against the cited section before it goes in; no line-number citations.
- Two files touched total: `symbols.md` (new) and `index.md` (one new row in the pages table; nothing else on that page).
- `spine.md` untouched.
- Edit files ONLY with the Edit/Write tools — never PowerShell `Get-Content|Set-Content` (PS 5.1 double-encodes the repo's UTF-8: `≤`, `—`, `ε`, `σ`).
- Register norm: flat. Size guidance: a scannable lookup page, roughly 10–20 KB; if fidelity and size conflict, fidelity wins.
- Work on branch **`symbols-registry`**, commit the page and the index row separately, do NOT merge — the main session reviews (including verifying a sample of pointers) before merging.
- Off-brief findings (a collision that is really an inconsistency, a definition site that has drifted, a pointer that cannot be made to resolve) to `briefs/symbols-registry-findings.md` — record, don't fix.

## Definition of done

`symbols.md` exists with all seven queue sections, every row's pointer verified, the collision index complete over the seeded set plus sweep discoveries; `index.md` has its one-row addition; the findings file records the sweep (files covered, verification method, anything ambiguous); clean commits on `symbols-registry`.
