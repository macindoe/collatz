# Brief: stratum_word_ticker — family (siblings) affordance in Read mode

Date: 2026-07-24. Author-approved (2026-07-24, main session): add a per-row "family" view to the Read pane showing the reduced-state siblings that funnel through each row's exit, with the green 0-run framed as the family boundary. Branch: create `ticker-family` from your worktree HEAD (based on `9d519f5` or later; report your base SHA in the findings comment of the commit message).

## Ground rules (non-negotiable)

- Read `AGENTS.md` first. Single file changed: `viz/stratum_word_ticker.html`. No wiki-page edits, no README/index/TOUR edits (the README viz row was checked by the main session and stays valid). Compose pane untouched. Escape demo untouched.
- All arithmetic exact BigInt, matching the file's house style (`'use strict'`, no external resources, CSS variables, dark-mode variables already in place).
- One commit on the branch. Do not push, do not merge; leave for main-session review.
- Sign discipline: the family funnel is `A = 3^d·ω − 1` (**minus** one). This was numerically verified in the main session (families (7,2), (1,4), (5,3): every member's orbit hits `3^d ω − 1`; none hits `3^d ω + 1`). Do not write `+1` anywhere.

## The mathematics (fixed; do not re-derive differently)

For a door `y` with the page's `step(y)` data (`m`, `q`, `A = 3^m q − 1`, `r`, `G = A/2^r`, state `(ω, d)` with `q = 3^a ω`, `d = m + a`):

- The state `(ω, d)` has exactly `d` member doors `y_a = 2^(d−a)·3^a·ω − 1`, `a = 0 … d−1` (reverse.md 14.1.1). The current door is the member with `a = d − m` (equivalently `a = v₃(y+1)`).
- Every member funnels through the single even value `A = 3^d·ω − 1` (= the page's `3^m·q − 1`, same number since `3^m q = 3^d ω`), shares the same exit valuation `r = v₂(A)` and the same next door `G = A/2^r` — hence the entire future word. Members differ only in the first letter's `m` component: member `y_a` carries letter `(d−a, r)`.
- `A` is a faithful single-integer representative of the state: `d = v₃(A+1)`, `ω = (A+1)/3^d` (reverse.md 14.14.1, exit equation `3^d ω = 1 + 2^s y'` read at the seam).
- A member with `3 | y_a` (possible only at `a = 0`, reverse.md 14.1.1) is a dead door: it reads forward like any other but no predecessor reaches it — reuse the page's existing dead-door badge styling.
- The framing the author asked for: the `r` green zeros are the **family breakers** — they are the family's last act. Dividing them out ends the family; the next door `G` opens a new family `(Ω, D)`.

## The feature

1. **Affordance.** In the Read table, make the state cell `(ω, d)` clickable (pointer cursor, dotted underline, `title` tooltip like "click: the d doors of this family and where they merge"). Clicking toggles a full-width expansion row (one `<tr>`, `colspan` spanning the table) directly below that row. Only one expansion needs to be open at a time (toggling another may close the previous — implementer's choice; keep it simple). Expansion state may reset on re-render ("read 14 more letters", new input) — acceptable.
2. **Family panel content** (inside the expansion row; compact, consistent style):
   - Header line: `family (ω, d) — d doors, one funnel`.
   - Member list: for each `a = 0 … d−1`, a chip or line with the member's value (use the page's `fmt`), its letter chip `(d−a, r)` via the existing `chip()` (m blue, r green), the dead badge when `3 | y_a`, and the current door visually marked (reuse the `.sel` outline or equivalent). Order: by `a` ascending (deepest entry `m = d` first) or `m` ascending — pick one and label it.
   - Funnel line: "all `d` doors merge at `A = 3^d·ω − 1` = " followed by `A` rendered with its `r` trailing zeros highlighted (reuse `bitsA(A, r)`), then: dropping the `<r>` green zeros ends the family — the next door `G` opens family `(Ω, D)`. Compute `(Ω, D)` as `step(G).w, step(G).d` (skip this clause when `G === 1n`, the fixed point).
   - A one-line note that `A` alone encodes the state: `d = v₃(A+1)`, `ω = (A+1)/3^d`.
   - **In-page verification (house norm):** on expansion, run `step(y_a)` for every displayed member and check `val === A` and matching `r`; show the green "verified by direct simulation" badge style only if all pass; if any fails, show a warn-styled message (should never happen — surfaced if it does).
   - Cap: if `d > 8`, list the first 6 members + "… (`d` doors total)"; verify the listed ones. (Large `d` is reachable from inputs like `2^40 − 1`.)
   - Trivial case `d = 1`: panel still opens, saying the family has this single door (and, when `3 | y`, that it is the dead one).
3. **Prose.** Add one short paragraph to the Read pane, after the existing long explainer paragraph, in the page's voice: every state `(ω, d)` is a family of exactly `d` doors, all funnelling through the single even value `A = 3^d·ω − 1` — click any row's state to see them; the whole future word from the next door on is family property, only the first letter's `m` is the member's own; and the `r` green zeros are the family boundary — consumed, they end the family, and the next door opens a new one (reverse.md 14.1.1, 14.14.1). Keep it to ~3 sentences; no new claims beyond the mathematics section above.
4. **Optional, only if it stays subtle:** extend `bitsA`'s tooltip with a clause noting the even exit is the family funnel. Do not add columns to the table.

## Verification (required before committing)

- Extract the page's arithmetic (`v2`, `v3`, `pw`, `step`) plus your new family-member computation into a throwaway node script (scratchpad, not committed) and check, for ≥ 200 random doors `y < 10^7` (odd): (a) the member list contains `y` at index `a = d − m`; (b) every member `y_a` is odd, positive, has `v2(y_a+1) = d−a` and `v3((y_a+1)/2^(d−a)) = a`; (c) `step(y_a).val` equals `3^d ω − 1` and `step(y_a).r` equals `r` for all members; (d) `v3(A+1) = d` and `(A+1)/3^d = ω` exactly. 0 failures required; report counts in the commit message.
- Load-check the HTML (at minimum: node-parse the `<script>` body for syntax, and eyeball the rendered DOM string paths for the new panel; if a headless browser is available, open the page and click a state cell for y₀ = 27 — expect family (7,2), members 27 and 41, funnel 62, next family from door 31).
- Spot-check the worked example in the panel by hand: `y = 27` → family `(7, 2)`, members `27` (letter (2,1)) and `41` (letter (1,1)), funnel `A = 62` (one green zero), next door `31`.

## Commit

One commit on `ticker-family`, message summarizing: feature, the funnel identity used (`A = 3^d ω − 1`, faithful via `v₃(A+1)`), verification counts (random-door checks, 0 failures), and your worktree base SHA.
