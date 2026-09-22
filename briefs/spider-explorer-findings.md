# Findings: the spider explorer (viz/spider_explorer.html)

Delegated session, branch `spider-explorer`. Supports `briefs/spider-explorer-brief.md`.

## Base SHA and branch

The worktree's HEAD at spawn was `946e0d8`, one commit behind local `main` and missing `briefs/spider-explorer-brief.md` itself. Per the brief's Rules, rebased onto local `main` before starting: branch `spider-explorer` created from `main` at `a79c97d` (the brief's own delegation commit, dated 2026-09-23), a fast-forward with no divergent commits to carry over.

**Base SHA: `a79c97d`.**

## What was built

`viz/spider_explorer.html`, one self-contained HTML file in the house style (the shared `:root` palette and dark-scheme block from `viz/comb_explorer.html`, system font, `<meta charset="utf-8">`), no external scripts, styles, fonts or images, nothing fetched, usable from `file://`. Every integer is a `BigInt`; states are `[Ω, D]` arrays of `BigInt`. Integers longer than 24 digits render as `first 8 … last 4 (N digits)` with click-to-reveal, matching the comb explorer's convention. Positive comb only — no root selector, no signed machinery — since spiders.md §19 and the brief's own page description never take a negative input.

**The arithmetic core** sits in its own `<script>` block between `// === SPIDER CORE BEGIN ===` and `// === SPIDER CORE END ===`, 269 lines, with no DOM access (the check script refuses the block if it finds any). The comb primitives (`v2`, `v3`, `exactDiv`, `mod3`, `modN`, `isValidState`, `isRoot`, `exitData`, `stateOfOdd`, `F`, `nodeAt`, `lowestBranch`, `doors`, `parent`, `children`) are copied from `viz/comb_explorer.html`, trimmed to the positive-only case (`isRoot(w,d) = (w===1n && d===1n)` in place of the comb explorer's four-component ring machinery, which this page never needs). Above them:

- `nodeClass(state, parentDepth)` — `root | abdomen | leg | orphan link | hair fork` (Definition 19.1.1, Definition 19.2.1), taking the parent's depth as an explicit argument rather than recomputing `parent()` internally, since the hair walk below already has it;
- `owner(state)` — ascends through comb parents while the class stays depth-1, terminating at an abdomen or the root (Theorem 19.2.2);
- `legs(abdomen)` — the abdomen's depth-1 children with the producing rule (`{kind:'cascade'}` or `{kind:'door', a}`) and the leg's own class (Lemma 19.1.6);
- `hair(legState)` — the chain from a leg to where it ends: each node's state, class, residues mod 3/8/9/24, `t = v₃(4Ω−1)` at a fork, and a **structured** `ruleKind`/`ruleNext` (`'link'`, `'fork-continue'` with `ruleNext ∈ {'fork','link'}`, or `'fork-end'`) — no prose in the core — together with the child spiders every fork spawns (`spawned`: its cascade child always, its top-door child too when `t ≥ 2`, Definition 19.3.1);
- `spider(abdomen)` — the whole piece: legs, hairs, size, every spawned child spider (from the abdomen's own `a = 1` and top-door children when they are not legs, and from every hair fork), and the parent spider `owner(parent(abdomen))`; refuses gracefully at the root by returning `rootPiece()` — a dedicated small object (size 1, single child spider `(1,2)`) rather than applying the `D ≥ 2` abdomen formula to `(1,1)`, since the root's own cascade child `(1,2)` is an abdomen (the root is a fork by residue with `t = v₃(3) = 1`, and its own top-door child is itself, the excluded self-loop — a fact the general formula, whose cascade child is always a leg by Lemma 19.1.6, does not cover);
- `selfTest()` with the canaries listed below.

**A deliberate refactor for verifiability.** The first draft put prose sentences (with the lemma citation already baked in) directly into the core's `hair()`/`spider()` return values. This made independent comparison brittle — any wording difference between the JS and a fresh Python re-implementation would read as a disagreement even when the underlying rule was identical. Refactored before the check script was written: the core now returns only structured fields (`ruleKind`, `ruleNext`, `t`), and the UI layer (`nodeRuleText`, `spawnRuleText`, in the second `<script>` block) composes the words and the lemma citation from that data. The check script therefore compares substance, not prose.

**The page**, feature by feature:

1. *Reading aids.* One paragraph at the top: what a spider is, what a click does, the registered vocabulary (abdomen, leg, hair, fork, link, orphan link, spider, spider tree) with lemma/theorem/definition pointers into spiders.md §19; no family-frame vocabulary.
2. *Go to a spider.* One input accepting a state `Ω,D` or a positive odd integer `x` (read as a door, `stateOfOdd(x)`, matching the comb explorer's convention); the page computes `owner()` and opens that spider. The default on load is the spider of `(1,2)`. `x = 1` resolves to `stateOfOdd(1) = (1,1)`, whose owner is the root itself — handled by the same `spider()` call as everything else (no special-cased input branch), landing on the root's own piece display: "Refuse `x = 1` gracefully as the root" from the brief.
3. *The abdomen card.* State, peak, depth, residues mod 3/8/9/24, the leg-count formula `(D−1) + [a=1 leg] + [top-door leg]` with the live 0/1 indicator values and the citation to Lemma 19.1.6, size, hair count, child-spider count.
4. *Hairs, flat.* One leg-head row per leg (the producing rule, cited to Lemma 19.1.6), then one row per hair node (state, class badge, residues, `t` at a fork) with one rule row after it in words, citing Lemma 19.1.2 or 19.1.3. No nested lists anywhere — every row is a direct child of `#content` (briefs/comb-explorer-findings.md's lesson, read before writing any DOM code).
5. *The borders.* One "the borders" section: a row per child spider (its state, the spawning node and the rule in the brief's own four-way wording — `abdomen's a = 1 child`, `abdomen's top-door child`, `hair fork's cascade child`, `hair fork's top-door child, t = …` — and its depth), and one parent-spider row with the comb edge type that connects them (cascade or door, comb.md 18.2.1).
6. *Self-test on load.* The footer prints `self-test: N checks, 0 failures` from `selfTest()`.

## Verification: `experiments/spider_explorer_check.py`

Fresh Python, imports nothing from any existing script. It (1) extracts the core, runs it under node (v20.10.0) via a JSON stdin/stdout harness that recursively converts digit-string arguments (including inside nested state arrays) to `BigInt`; exits 2 without running anything if `node` is missing; (2) implements `owner`, `legs`, `hair`, `spider`, the classes and the continuation rules independently from spiders.md's definitions, producing the same structured (non-prose) `ruleKind`/`ruleNext` fields as the refactored core, converted to the same wire format `JSON.stringify` produces (every integer a decimal string) for direct dict equality — the strongest comparison available, since it checks every field of every hair node and every spawned child, not just a summary count; (3) compares on the canaries (the spider of `(1,2)` with its four child spiders per spiders.md's corrected hand derivation; the root's own piece; `(17,1)` an orphan link owned by `(5,2)`; the leg `(13,1)` of `(5,2)` with children `(17,2)`/`(17,1)`; the leg `(7,1)` with children `(1,4)`/`(1,3)`) and on 1,000 random abdomens (`Ω < 10^6`, `2 ≤ D ≤ 12`, seed `20260923`) for the full spider structure, 500 random depth-1 nodes for `owner`, and 300 random odd `x < 10^12` for the go-to (door recovery then `owner`); (4) runs the page under a stubbed `document` for the go-to of `(1,2)`, of the odd integer `17`, and of the abdomen among the 1,000 random samples whose spider has the longest single hair, measuring the maximum DOM nesting depth under `#content` and the rendered row count (and its per-kind breakdown — abdomen, leg-head, node, rule, border, parent rows) against a Python row-count formula that mirrors the page's `renderSpider()` exactly; (5) prints per-function counts and `TOTAL: checks = N, failures = 0`.

```text
spider_explorer_check.py -- seed 20260923, 2026-09-23
core block: 269 lines between the markers, no DOM access
node v20.10.0; 2108 requests answered
--- the page's selfTest() under node ---
  self-test: 1411 checks, 0 failures
--- canaries (the spider of (1,2); the root's piece; (17,1)/(13,1)/(7,1)) ---
  14 canary checks so far, 0 failures
--- 1,000 random abdomens (Omega < 10^6, 2 <= D <= 12) plus 4 canary abdomens: the full spider ---
  1004 spiders compared, 0 mismatches expected; size range 1..84, mean 32.610
  longest single hair among the 1,000 random abdomens: 30 nodes, in the spider of (351535,7)
--- 500 random depth-1 nodes: owner ---
  1000 checks, 0 failures expected
--- 300 random odd x < 10^12: the go-to (stateOfOdd then owner) ---
  600 checks, 0 failures expected
--- rendering under a stubbed document: go-to (1,2), the odd integer 17, and the longest-hair abdomen (351535,7) ---
  page load under the stub, footer: self-test: 1411 checks, 0 failures
  depth bound stated: 3 (container > row > link-or-span > abbreviated-integer span)
  (1,2)                            owner (1, 2), spider size 4: max nesting depth 2, rendered rows 15
  17                               owner (1, 3), spider size 30: max nesting depth 2, rendered rows 86
  longest-hair abdomen (351535,7)  owner (351535, 7), spider size 57: max nesting depth 2, rendered rows 163

TOTAL: checks = 2643, failures = 0
```

Output committed verbatim at `experiments/spider_explorer_check_output.txt`, written by the script itself (no shell redirection, no BOM).

**Single reproducing command:**

```
python experiments/spider_explorer_check.py
```

No phases, no flags. Runs in a few seconds.

**The self-test line as it prints in a browser: not observed.** This session has no browser and cannot open the page. The line above (`self-test: 1411 checks, 0 failures`) is the core's `selfTest()` exercised under node, both directly (the check script's own node harness, function-by-function) and through the stubbed-`document` rendering harness, which loads both script blocks and reports the same footer text — a smoke test of the load and render paths, not a browser test. **The DOM layer was not browser-tested**: layout, click targets, the click-to-reveal, and the dark scheme are unverified in a real browser and should be looked at once when the main session opens the file.

`experiments/encoding_scan.py`: **RESULT: CLEAN** (run after the wiki edits and again after staging every new file, before the final commit).

## Wiki edits

- `README.md`: the repository map's `viz/` row gains one entry for `spider_explorer.html`, inserted after `comb_explorer.html` (which already names spiders.md §19's node classes), one clause, nothing else.
- `spiders.md`: one sentence at the end of §19.4 naming the explorer; front matter `updated` moved from `2026-09-22` to `2026-09-23`. No number, claim or verification line changed.
- Not edited: `HANDOFF.md`, `comb.md`, `symbols.md`, `index.md`, `AGENTS.md`, `TOUR.md`, and everything else.

## What the brief asked for that was not done, and why

Nothing in the brief was left undone. Two judgment calls worth flagging for review:

1. **The rendering-row layout puts a rule row after every hair node, including the last one**, not only "between" consecutive nodes as the brief's item 2 literally reads. The last rule row states why the hair ends (`fork ends the hair (t = … ≥ 2, Lemma 19.1.3)`), which is itself a fact about that node worth citing; the alternative (a rule row only between two node rows, `n − 1` of them for `n` nodes) would silently drop the termination reason from the flat display. Kept as implemented; easy to change at merge if the literal reading is preferred.
2. **`nodeClass`'s signature** takes `(state, parentDepth)` and returns the same six-way class the comb explorer's `nodeClass` returns (`root | abdomen | leg | orphan link | hair fork`, `hair link` unreachable), reading `parentDepth` only for a depth-1 node. The brief's own wording ("`nodeClass(state, parentDepth) → abdomen | fork | link | root` from `(Ω, D)`, and the finer labels … from the parent's depth") could be read as two separate return alphabets; this implementation treats `fork`/`link` as intermediate concepts folded into the finer labels, never returned bare, matching what the comb explorer already displays and what `symbols.md` §4 registers.

## For the main session at merge

- **Base and seams.** Cut from `a79c97d`. Touches `viz/spider_explorer.html` (new), `experiments/spider_explorer_check.py` and `experiments/spider_explorer_check_output.txt` (new), `README.md` (one `viz/` row entry), `spiders.md` (one sentence at the end of §19.4, front matter `updated`), and this file. Five single-purpose seams, each a small insertion.
- **Re-run the check script fresh**: single command, foreground, a few seconds (`python experiments/spider_explorer_check.py`). It re-extracts the core from the committed page, so a stale copy cannot pass.
- **Browser.** Open the page once: the self-test footer should read `self-test: 1411 checks, 0 failures`; the default view should be the spider of `(1,2)` (size 4, 2 hairs, 4 child spiders); typing `17` and clicking go should land on `(1,3)`'s spider; clicking a child-spider or parent-spider link should move one spider at a time with no layout break.
- **The core-vs-UI split (structured `ruleKind` vs. prose)** is the one architectural choice in this session beyond what the brief specified directly; it is what makes the independent verification a field-by-field structural comparison rather than a string comparison, and is worth preserving in any future revision of this page.
- **Commit stream.** Five commits on `spider-explorer`: the page; the check script with its output; the README row; the spiders.md sentence; this file.
