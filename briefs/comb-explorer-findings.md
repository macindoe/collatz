# Findings: the comb explorer (viz/comb_explorer.html)

Delegated session, branch `comb-explorer`. Supports `briefs/comb-explorer-brief.md`.

## Base SHA and branch

The worktree's HEAD at spawn was `a7543ce` (2026-09-13), which predates the brief: `briefs/comb-explorer-brief.md` did not exist there. `git rebase main` fast-forwarded the worktree branch cleanly onto local `main` at `efa92a4` (2026-09-15, the brief's own delegation commit), and `comb-explorer` was cut from there.

**Base SHA: `efa92a4`.**

## What was built

`viz/comb_explorer.html`, one self-contained HTML file in the house style (the shared `:root` palette with the dark-scheme block, system font, `<meta charset="utf-8">`), no external scripts, styles, fonts or images, nothing fetched, usable from `file://`. Every integer is a `BigInt`; states are `[ω, d]` arrays of `BigInt`; no floating point anywhere a displayed integer or a decision depends on it. Integers longer than 24 digits render as `first 8 digits … last 4 digits (N digits)` with a click-to-reveal of the full value, and long values are allowed to wrap (`word-break`) so they never break the layout.

**The arithmetic core** sits in its own `<script>` block between the exact lines `// === COMB CORE BEGIN ===` and `// === COMB CORE END ===`, 150 lines, with no DOM access (the check script refuses the block if it finds any). Functions, all on `BigInt`: `v2`, `v3`, `isValidState`, `exitData(ω,d) → {A, s, y}`, `stateOfOdd(y)`, `F`, `nodeAt(y,s)` (the state at branch `s` on door `y`), `lowestBranch(y)`, `doors(Ω,D) → [{a, y, alive}]`, `parent(ω,d) → {state, type} | null`, `children(Ω,D) → {list: [{state, type, s, door: {a, y}}], dead: [{a, y, dead}], excluded: [...]}` (the cascade child first, then the door children in door order; dead doors apart; the root's self-child under `excluded`), `rawDescent(ω,d,a)` (the points `x_a, 2x_{a+1}, x_{a+1}, …, 2A, A, …, 2y, y`, tagged `odd` / `rise` / `max` / `peak` / `sibpeak` with the sibling's state / `cascade` / `door`), `pathToRoot(ω,d,cap) → {path, capHit, doorEdges, cascadeEdges, lambda, eta}` with `η = 1 + door edges`, `λ = edges` (Proposition 18.3.2(b)) and `η = λ = 0` at the root, the 28 census constants of 18.5 with their total, and `selfTest()`.

**The page**, feature by feature as delivered:

1. *The tree.* An indented nested list (no canvas). At load: the root `(1,1)` at level `0`, expanded to show its one child `(1,2)` as a collapsed stub, and one greyed line for door `1`: "its lowest-branch child, at branch 1, is the root itself, the excluded self-loop (18.2.1)". The `+` control expands one level: the cascade child first, then the door children in door order `a = 0, 1, …`, then a dead top door greyed with the 14.5.1 pointer. Nothing is computed before it is shown; collapsing hides the subtree and keeps it. Edge type is a word in a badge (`root` / `cascade` / `door`), with a background tint as a secondary cue only.
2. *The node card.* The state; the peak `A = 2^s · y` read as "branch `s` on door `y`"; `λ` with the census count for that level; `η`; and, for a door child, "through the top door" or "through side door `a = …`" (for a cascade child, "cascade child, same door"). `λ` and `η` on the cards are exact by construction: each node is registered from its parent with `level + 1` and `doorEdges + (edge is door)`, so they are the path-to-root counts; the detail panel recomputes them from `pathToRoot` and the two agree (the check script compares `pathToRoot` on `2,313` states and paths).
3. *The detail panel.* (a) The path to the root as a breadcrumb, each edge badged, with the tally `λ = … edges = … door + … cascade; η = 1 + … = …` and a one-clause pointer to 18.3.2(b); the root reads `λ = η = 0`. (b) The raw descent from a selectable representative (top door by default; every side door offered) down to the door, every point tagged; the lower siblings' peaks marked `peak of (ω′,d′), the sibling at branch j`, each a link; one line citing Proposition 18.4.1. (c) The siblings on the door: branches `s₀, s₀+2, …` to two beyond this node, with state and peak `2^j y`, this node marked, and a note on the shared `η`, the `(j − s₀)/2` level offset (18.3.2(c)) and the `A, 4A, 16A` law (18.2.5); on door `1` a clause that its lowest sibling is the root.
4. *Go to a node.* The input accepts `ω,d` (parentheses and spaces tolerated) or a positive odd integer `x`. For `x` the message states the recovery `x + 1 = 2^m · 3^a · Ω` and which door of which state `x` is (14.6.5.1). The path to the root is computed under a cap of `10,000` steps; if the cap hits the page says so and places nothing; otherwise the tree is expanded along the path from the root, the node is selected and scrolled into view, and the message reports its level and `η`. States in the panel (path nodes, siblings, sibling peaks, `F(ω,d)`) are links that go to that node.
5. *Level context.* Every `λ` on a card or in the panel carries "level `λ` has `N` nodes" from the embedded census, or "is beyond the census" past level `27`. One line under the tree: levels double from about level `17`; the largest peak at level `λ` is `2^{2λ+1}`, on door `1` (Lemma 18.5.1).
6. *Reading aids.* One paragraph at the top: what the comb is, the two edge types, the top and side doors and door mortality, `η` and `λ`, the root's single child, what `+` and a click do, all with section pointers into comb.md §18 and reverse.md 14.5.1. Vocabulary as the registry has it; no columns, tears, or grouping by core anywhere on the page.
7. *Self-test on load.* `selfTest()` runs in the core and the footer prints one line. The canaries: the root's only child `(1,2)` and the excluded self-loop; door `1`'s chain at branches `1, 3, 5, 7, 9` with the cascade parents between them; door `5`'s `(7,1), (1,4), (107,1)` at `s = 2, 4, 6` with peaks `20, 80, 320`; `(7,3)`'s four children with their types, branches and doors and the cascade child's peak `752`; `(1,2)`'s top door `3` dead; the distances of `(1,2)`, `(11,1)`, `(7,1)`, `(107,1)` and the root; the cap reported when hit; the raw descent of `(107,1)` from `213` with `80` and `20` as the peaks of `(1,4)` and `(7,1)`; the census constants summing to `126,917,355`; and, for `300` states from a fixed 64-bit linear-congruential sequence (seed `20260915`, no `Math.random`), the degree formula and `parent(child) = node` with the matching type for every child, `F(child) = node` and the door for door children, peak `4A` for the cascade child. The line reads:

```text
self-test: 13239 checks, 0 failures
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

**TOTAL: checks = 15291, failures = 0.** Output committed verbatim at `experiments/comb_explorer_check_output.txt`, written by the script itself (no shell redirection, no BOM; the node version line is the only machine-dependent one).

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
- **Browser.** Open the page once: the self-test footer should read `self-test: 13239 checks, 0 failures`; expand `(1,2)`, click `(7,1)`, and use the go-to with `213` — the message should place `(107,1)` at level `4` with `η = 2` and the descent should mark `80` and `20`.
- **Commit stream.** Five commits on `comb-explorer`: the page; the check script with its output; the README row; the comb.md sentence; this file.

## Files changed

- `viz/comb_explorer.html` (new)
- `experiments/comb_explorer_check.py` (new), `experiments/comb_explorer_check_output.txt` (new)
- `README.md` (one entry in the `viz/` row)
- `comb.md` (one sentence at the end of 18.6)
- `briefs/comb-explorer-findings.md` (this file)
