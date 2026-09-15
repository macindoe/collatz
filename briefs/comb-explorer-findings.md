# Findings: the comb explorer (viz/comb_explorer.html)

Delegated session, branch `comb-explorer`. Supports `briefs/comb-explorer-brief.md`.

## Base SHA and branch

The worktree's HEAD at spawn was `a7543ce` (2026-09-13), which predates the brief: `briefs/comb-explorer-brief.md` did not exist there. `git rebase main` fast-forwarded the worktree branch cleanly onto local `main` at `efa92a4` (2026-09-15, the brief's own delegation commit), and `comb-explorer` was cut from there.

**Base SHA: `efa92a4`.**

## What was built

`viz/comb_explorer.html`, one self-contained HTML file in the house style (the shared `:root` palette with the dark-scheme block, system font, `<meta charset="utf-8">`), no external scripts, styles, fonts or images, nothing fetched, usable from `file://`. Every integer is a `BigInt`; states are `[ω, d]` arrays of `BigInt`; no floating point anywhere a displayed integer or a decision depends on it. Integers longer than 24 digits render as `first 8 digits … last 4 digits (N digits)` with a click-to-reveal of the full value, and long values are allowed to wrap (`word-break`) so they never break the layout.

**The arithmetic core** sits in its own `<script>` block between the exact lines `// === COMB CORE BEGIN ===` and `// === COMB CORE END ===`, 150 lines, with no DOM access (the check script refuses the block if it finds any). Functions, all on `BigInt`: `v2`, `v3`, `isValidState`, `exitData(ω,d) → {A, s, y}`, `stateOfOdd(y)`, `F`, `nodeAt(y,s)` (the state at branch `s` on door `y`), `lowestBranch(y)`, `doors(Ω,D) → [{a, y, alive}]`, `parent(ω,d) → {state, type} | null`, `children(Ω,D) → {list: [{state, type, s, door: {a, y}}], dead: [{a, y, dead}], excluded: [...]}` (the cascade child first, then the door children in door order; dead doors apart; the root's self-child under `excluded`), `rawDescent(ω,d,a)` (the points `x_a, 2x_{a+1}, x_{a+1}, …, 2A, A, …, 2y, y`, tagged `odd` / `rise` / `max` / `peak` / `sibpeak` with the sibling's state / `cascade` / `door`), `pathToRoot(ω,d,cap) → {path, capHit, doorEdges, cascadeEdges, lambda, eta}` with `η = 1 + door edges`, `λ = edges` (Proposition 18.3.2(b)) and `η = λ = 0` at the root, the 28 census constants of 18.5 with their total, and `selfTest()`.

**The page**, feature by feature as delivered:

1. *The tree.* A flat sequence of rows in depth-first order, each indented by `min(level, 24)` steps (no canvas, no nesting per level; see Revision 1). At load: the root `(1,1)` at level `0`, expanded to show its one child `(1,2)` as a collapsed stub, and one greyed line for door `1`: "its lowest-branch child, at branch 1, is the root itself, the excluded self-loop (18.2.1)". The `+` control expands one level: the cascade child first, then the door children in door order `a = 0, 1, …`, then a dead top door greyed with the 14.5.1 pointer. Nothing is computed before it is shown; collapsing hides the subtree and keeps it. Edge type is a word in a badge (`root` / `cascade` / `door`), with a background tint as a secondary cue only.
2. *The node card.* The state; the peak `A = 2^s · y` read as "branch `s` on door `y`"; `λ` with the census count for that level; `η`; and, for a door child, "through the top door" or "through side door `a = …`" (for a cascade child, "cascade child, same door"). `λ` and `η` on the cards are exact by construction: each node is registered from its parent with `level + 1` and `doorEdges + (edge is door)`, so they are the path-to-root counts; the detail panel recomputes them from `pathToRoot` and the two agree (the check script compares `pathToRoot` on `2,313` states and paths).
3. *The detail panel.* (a) The path to the root as a breadcrumb, each edge badged, with the tally `λ = … edges = … door + … cascade; η = 1 + … = …` and a one-clause pointer to 18.3.2(b); the root reads `λ = η = 0`. (b) The raw descent from a selectable representative (top door by default; every side door offered) down to the door, every point tagged; the lower siblings' peaks marked `peak of (ω′,d′), the sibling at branch j`, each a link; one line citing Proposition 18.4.1. (c) The siblings on the door: branches `s₀, s₀+2, …` to two beyond this node, with state and peak `2^j y`, this node marked, and a note on the shared `η`, the `(j − s₀)/2` level offset (18.3.2(c)) and the `A, 4A, 16A` law (18.2.5); on door `1` a clause that its lowest sibling is the root.
4. *Go to a node.* The input accepts `ω,d` (parentheses and spaces tolerated) or a positive odd integer `x`. For `x` the message states the recovery `x + 1 = 2^m · 3^a · Ω` and which door of which state `x` is (14.6.5.1). The path to the root is computed under a cap of `10,000` steps; if the cap hits the page says so and places nothing; otherwise the tree is expanded along the path from the root, the node is selected and scrolled into view, and the message reports its level and `η`. States in the panel (path nodes, siblings, sibling peaks, `F(ω,d)`) are links that go to that node.
5. *Level context.* Every `λ` on a card or in the panel carries "level `λ` has `N` nodes" from the embedded census, or "is beyond the census" past level `27`. One line under the tree: levels double from about level `17`; the largest peak at level `λ` is `2^{2λ+1}`, on door `1` (Lemma 18.5.1).
6. *Reading aids.* One paragraph at the top: what the comb is, the two edge types, the top and side doors and door mortality, `η` and `λ`, the root's single child, what `+` and a click do, all with section pointers into comb.md §18 and reverse.md 14.5.1. Vocabulary as the registry has it; no columns, tears, or grouping by core anywhere on the page.
7. *Self-test on load.* `selfTest()` runs in the core and the footer prints one line. The canaries: the root's only child `(1,2)` and the excluded self-loop; door `1`'s chain at branches `1, 3, 5, 7, 9` with the cascade parents between them; door `5`'s `(7,1), (1,4), (107,1)` at `s = 2, 4, 6` with peaks `20, 80, 320`; `(7,3)`'s four children with their types, branches and doors and the cascade child's peak `752`; `(1,2)`'s top door `3` dead; the distances of `(1,2)`, `(11,1)`, `(7,1)`, `(107,1)` and the root; the cap reported when hit; the raw descent of `(107,1)` from `213` with `80` and `20` as the peaks of `(1,4)` and `(7,1)`; the census constants summing to `126,917,355`; the path of `(137,517)` — `1,365` nodes, `λ = 1364`, `η = 1056`, largest peak `249` digits (Revision 1); and, for `300` states from a fixed 64-bit linear-congruential sequence (seed `20260915`, no `Math.random`), the degree formula and `parent(child) = node` with the matching type for every child, `F(child) = node` and the door for door children, peak `4A` for the cascade child. The line reads:

```text
self-test: 13241 checks, 0 failures
```

**The self-test line as it prints in a browser: not observed.** This session has no browser and cannot open the page. The line above is the core's `selfTest()` exercised under node through the check script (which prints the same line) and through a second harness with a stubbed `document` that loaded both script blocks and drove the DOM layer (expand, collapse and re-expand, select, go-to by state, by odd integer, by a 39-digit odd integer, an invalid state refused, reset) without runtime errors — a smoke test of the render paths, not a browser test. **The DOM layer was not browser-tested**: layout, the sticky panel, click targets, the dark scheme and the click-to-reveal are unverified in a real browser and should be looked at once when the main session opens the file.

## Verification: `experiments/comb_explorer_check.py`

Fresh Python; imports nothing from any other script in the repository. It reads the page, extracts the text between the two markers (exactly one of each, or it exits `2`), refuses the block if it contains DOM access, appends a stdin/stdout JSON harness (requests `{fn, args}` with arguments as decimal strings converted to `BigInt`; results with every `BigInt` rendered as a decimal string), and runs it once under `node` (`shutil.which`; if `node` is missing the script says so and exits `2` — it never passes vacuously). The Python side is written from the definitions, not from the JavaScript: door recovery from 14.6.5.1; the parent from 18.2.1; the cascade child by 14.10.1's `N(y, s+2) = 4N(y, s) − 3` with `N = 3^D Ω`; the door children as 14.1.1's predecessors at the lowest admissible branch; the raw descent by iterating the raw map from `x_a` to `y`, tagging from position and Lemma 18.1.2(iii); `η` by iterating `F` to `(1,1)` — the definition, not the page's `1 + door edges` — and `λ` by counting parent edges.

Compared, seed `20260915`, 2026-09-15:

- the page's `selfTest()` under node: `13,239` checks, `0` failures;
- the brief's canaries as hard-coded expectations, each checked on both implementations (`35` checks);
- `2,000` random states (`ω < 10^6`, `3 ∤ ω`, `d ≤ 40`) plus the `13` canary states, every function: `exitData`, `F`, `stateOfOdd` on the exit, `doors`, `parent`, `children`, `pathToRoot` with the full path, `η` and `λ` (largest `λ` `194`; every path reached `(1,1)`);
- `300` random odd `x < 10^12`: `stateOfOdd(x)`, the recovered state's door `a = v₃(x+1)` equal to `x`, and the full path to the root with `η` and `λ` (largest `λ` `140`, largest `η` `119`, no cap hit);
- `200` random representatives: the raw descent point by point and tag by tag (`4,658` points; `64` lower-sibling peaks named, each verified to be a lower branch on the same door with that peak).

With the rendering test of Revision 1 (four go-to cases under the stubbed document, `38` checks): **TOTAL: checks = 15329, failures = 0.** Output committed verbatim at `experiments/comb_explorer_check_output.txt`, written by the script itself (no shell redirection, no BOM; the node version line is the only machine-dependent one).

**Single reproducing command:**

```
python experiments/comb_explorer_check.py
```

No phases, no flags. Runs in a few seconds.

`experiments/encoding_scan.py`: **RESULT: CLEAN** (run after the wiki edits and again before the final commit).

## One defect found and fixed before commit

The first run of the self-test under node failed the degree canary at all `300` LCG states: the check compared `cs.list.length` (a JavaScript Number) with a `BigInt` sum under `===`, which is always false. Wrapped in `BigInt(...)`; no arithmetic was wrong. Recorded because it is the kind of mixed-type slip the "BigInt everywhere" rule exists to catch.

## Wiki edits

- `README.md`: the repository map's `viz/` row extended by one entry for `comb_explorer.html`, after `stratum_field_explorer.html`, in the row's style. Nothing else.
- `comb.md`: one sentence at the end of 18.6 naming the explorer and its check script. Front matter `updated` already read `2026-09-15` and is unchanged.
- `TOUR.md`: untouched. Its Visualizations sentence says the README's repository map lists each file, which stays true with the new row; no clause was needed.
- Not edited: `HANDOFF.md`, `reverse.md`, `symbols.md`, `index.md`, `ladder.md`, `stage*.md`, `open-problems.md`, `publication.md`, `paper/`, `sources/`.

## For the main session at merge

- **Base and seams.** Cut from `efa92a4`. Touches `viz/comb_explorer.html` (new), `experiments/comb_explorer_check.py` and `experiments/comb_explorer_check_output.txt` (new), `README.md` (the one `viz/` row entry), `comb.md` (one sentence at the end of 18.6), and this file. The README row and the comb.md sentence are the two seams; both are single insertions.
- **The census constants are duplicated on the page.** The 28 counts of comb.md 18.5 are embedded in the core as `CENSUS` (with the total `126,917,355` as a self-test canary). If the census is ever re-run to more levels, the page's array is a second copy to update; comb.md stays the authority.
- **Browser.** Open the page once: the self-test footer should read `self-test: 13241 checks, 0 failures`; expand `(1,2)`, click `(7,1)`, and use the go-to with `213` — the message should place `(107,1)` at level `4` with `η = 2` and the descent should mark `80` and `20`; then go to `137,517` — the message should begin "read as the state (137, 517)", place it at level `1,364` with `η = 1056`, and the tree should show the `1,364` ancestors each with a stub.
- **Commit stream.** Five commits on `comb-explorer` (the page; the check script with its output; the README row; the comb.md sentence; this file), merged at `f5c31d3`; then Revision 1 on `comb-explorer-fix` (the page; the check script with its output; this file).

## Revision 1 (briefs/comb-explorer-fix-brief.md)

Branch `comb-explorer-fix`, cut from local `main` at **`d5d30bb`** (the fix brief's own commit, on top of the merge `f5c31d3`; the merged page, script, output and findings were byte-identical to the `comb-explorer` branch). Files changed: `viz/comb_explorer.html`, `experiments/comb_explorer_check.py` and its output, this file. Nothing else.

**The defect.** The author typed `137,517` into the go-to box and the page crashed. The arithmetic was not at fault (`pathToRoot(137n, 517n)`: `1,365` nodes, `λ = 1364`, `η = 1056`, largest peak `249` digits, milliseconds). The DOM layer did two things that did not scale with the path: `renderNode` nested one `<ul>` per comb level inside one `innerHTML` string, so the go-to built a DOM `1,365` deep — past what browsers tolerate for nesting and layout — and `gotoState` expanded every ancestor in full, rendering all `4,206` rows a full expansion produces when only the path child of each ancestor was needed.

**The fix, as delivered.**

- *Flat rendering.* `#tree` is a `<div>` holding one row per visible node in depth-first order (the reading order is unchanged); indentation is `margin-left = min(level, 24) × 18px`, so the page never grows wider than the viewport by more than one card, and the level stays printed on every card. The nesting under the container is bounded by a constant: row → span → abbreviation or exponent, depth `3` — abbreviated integers no longer carry an inner `<small>`, so that bound holds with click-to-reveal intact. The walk that emits the rows keeps its own explicit stack (no recursion): the first version of the fix was recursive and overflowed the JavaScript call stack on the render-cap test case below — the same class of failure as the original defect, depth proportional to path length — and was replaced before commit.
- *Path-only expansion on go-to.* Each node carries `shown`: `null` for all children displayed, or the set of child keys displayed. A go-to expands each ancestor to its path child only and renders one stub row `+ k more children (expand)` for the rest, with the dead-door and self-loop notes folded into the stub's count (`+ 2 more children and 1 dead door (expand)`); clicking the stub shows the rest for that ancestor only. Ordinary `+` expansion shows all children as before; an ancestor already fully expanded stays so. The message states the count: "placed at level `1,364` with `η = 1056`; `1,364` ancestors on the path shown, each with the rest of its children behind a stub".
- *The comma reading, explicit and reversible.* `137,517` is read as the state `(137, 517)` and the message begins "read as the state (137, 517) — for the odd integer 137517, type it without the comma", the last phrase a link that performs the odd-integer go-to. When the digits joined are even the message says there is no odd-integer reading. When the comma reading is not a valid state but the digits joined are odd (`9,1`), the message says so and offers the integer `91` the same way.
- *The render guard.* A go-to whose path exceeds `5,000` nodes (the `pathToRoot` cap stays `10,000`) is placed, but only the last `200` ancestors are rendered below the root, with one row "… N ancestors not shown (levels a..b)" in between and the counts in the message. It cannot trigger for typed input of ordinary size; the check script triggers it deliberately with door `1`'s chain node at branch `10003` (a `3,012`-digit `ω`, path `5,002` nodes).
- *Self-test.* Two canaries added inside `selfTest()`: the `(137,517)` path (`1,365` nodes, `λ = 1364`, `η = 1056`) and its largest peak (`249` digits). The footer now reads `self-test: 13241 checks, 0 failures`. **This touches the core block** — `selfTest()` lives between the markers so that the check script can run it under node — but no arithmetic function changed; the `150`-line core is now `155` lines, the difference being those two canary lines and their comment.

**Verification (the rendering test, in `experiments/comb_explorer_check.py`).** The script now also loads both of the page's script blocks under node with a stubbed `document` (plain objects holding `innerHTML` and click listeners), checks the footer line equals `selfTest()`'s under node, and drives the go-to box from a freshly reset tree for four cases, measuring the produced tree HTML with Python's own `html.parser`: the maximum element nesting depth under the container (bound stated: `3`), the rendered rows against the count computed in Python from its own children rule (path nodes, one stub per ancestor with children or notes left unshown, the root's note row, the fold row under the guard), the cards against the visible path nodes, rows strictly below a full expansion, no exception, and the message's opening and counts. Seed `20260915`:

```text
(137,517)    path 1365 nodes (lambda 1364, eta 1056): max nesting depth 3, rendered rows 2729 (cards 1365, stubs 1363, note rows 1), no exception; a full expansion of the ancestors would render 4206 rows
213          path 5 nodes (lambda 4, eta 2): max nesting depth 3, rendered rows 9 (cards 5, stubs 3, note rows 1), no exception; a full expansion of the ancestors would render 13 rows
300-digit x  path 1794 nodes (lambda 1793, eta 1383): max nesting depth 3, rendered rows 3587 (cards 1794, stubs 1792, note rows 1), no exception; a full expansion of the ancestors would render 5437 rows
render cap   path 5002 nodes (lambda 5001, eta 1): max nesting depth 3, rendered rows 404 (cards 202, stubs 200, note rows 2), no exception; a full expansion of the ancestors would render 12504 rows; 4800 ancestors folded
```

plus `9,1` refused with the integer `91` offered. The arithmetic comparisons are unchanged (`15,291` checks); the rendering test adds `38`. **TOTAL: checks = 15329, failures = 0.** Single reproducing command `python experiments/comb_explorer_check.py`, run in the foreground; output committed. `experiments/encoding_scan.py`: **RESULT: CLEAN** before the final commit. No browser was available in this revision either: the numbers above are the stubbed-document harness's, and the page should still be opened once as the *Browser* item above says.

## Files changed

- `viz/comb_explorer.html` (new; revised in Revision 1)
- `experiments/comb_explorer_check.py` (new; extended in Revision 1), `experiments/comb_explorer_check_output.txt` (new; re-generated in Revision 1)
- `README.md` (one entry in the `viz/` row)
- `comb.md` (one sentence at the end of 18.6)
- `briefs/comb-explorer-findings.md` (this file)
