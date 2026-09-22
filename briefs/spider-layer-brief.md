# Brief: the spider layer — the comb partitioned into abdomens with their hairs (new page `spiders.md`, section 19): the classification of nodes by depth and residue, the hair chains, the partition theorem, the spider tree with its census, and where determinism lives one layer up — for a delegated session

**Context required before starting (in order):** `README.md` (strategy and **binding stopping rules** — no cycle search of any kind; equidistribution proof effort waits for an idea; measurements may feed the ledger), `AGENTS.md`, `HANDOFF.md` (register norm; delegation pattern; the PowerShell quirk), `comb.md` §18 in full as merged — especially 18.2.3 (children and degree), 18.5 (the census, the depth ledger on levels), 18.7.2 (the mean degree 2), 18.7.3 (the digit-transfer law), 18.9.1 (the level-1 branching laws: a door child through any door `a ≥ 2` has depth exactly `1`; through `a = 1` depth `1 + v₃(2^{D+1}Ω − 1)`; the top door by its residue; the cascade child by 14.10.1), 18.9.2–18.9.5 (signatures, the residue budget, the negative on anything finer than residues), `reverse.md` 14.10.1 (the cascade step: child depth `1` when `D ≥ 2`, `1 + v₃(4Ω − 1)` when `D = 1`), 14.5.1 (mortality), 14.2.4 and 14.6.5.2 (the depth ledger and its exact per-window form), `viz/comb_explorer.html` and `experiments/comb_explorer_check.py` (the explorer; its isolated arithmetic core between the markers; the check harness), `symbols.md`, `TOUR.md`, `index.md`, `briefs/comb-signatures-brief.md` and its findings (the form; the standards a Sonnet delegate met after one revision round — read the findings' Revision 1 section for the kinds of statistical error that were sent back).

## Provenance

The author's direction of 2026-09-22: build the next deterministic abstraction up from reduced states, one layer at a time, with the stated north star that the layers may be raised until the whole map is one object. This brief builds the first such layer. It was worked out with the author and pre-checked in the main session with throwaway code (not filed; write the script of record from scratch). **Every claim below is a claim to be re-derived and re-verified here, not a fact.** A claim is never confirmed or dissolved by naming its type; corrections carry a re-derivation. Grade: **formulation** (a construction, its elementary properties proved, a census) plus measurements; no front moves; nothing proposed; no cycle searched; no family-frame vocabulary (no columns, tears, or grouping by core). The positive comb only; one sentence may note that every rule below is sign-blind (18.8).

## Item A — the classification of nodes (Lemma 19.1.1)

For a comb node `(Ω, D)`:

- **abdomen**: `D ≥ 2`;
- **fork**: `D = 1`, `Ω ≡ 1 (mod 3)`;
- **link**: `D = 1`, `Ω ≡ 2 (mod 3)`;
- the **root** `(1,1)` is a fork by residue but is treated as its own piece (its only child is the abdomen `(1,2)`).

**Claims to prove, from 18.9.1 and 14.10.1.**

1. A **link** has exactly one child: its cascade child `(4Ω − 1, 1)`, of depth `1`, which is always a **fork** (`4Ω − 1 ≡ 1 (mod 3)` when `Ω ≡ 2`); its top door `2Ω − 1` is dead. **Pre-checked** on all `66,666` depth-1 states with `Ω < 2·10^5` and on the comb to level `18`: `0` failures.
2. A **fork** has exactly two children: its cascade child of depth `t + 1 ≥ 2` (an abdomen) and its top-door child (the top door `2Ω − 1 ≡ 1 (mod 3)` is alive, `s₀ = 1`) with core `(4Ω − 1)/3^t` and depth `t`, where `t = v₃(4Ω − 1) ≥ 1`. The top-door child has depth `1` iff `t = 1` iff `Ω ≢ 7 (mod 9)`; when it has depth `1` it is a link or a fork in equal measure (**pre-checked** on the comb to level `18`: `27,515` links against `27,623` forks — derive whether this is exact by residue, e.g. by `Ω mod 27`, or only statistical).
3. Consequently **a depth-1 node has at most one depth-1 child** (**pre-checked**: `137,920` depth-1 nodes with one, `27,522` with none, `0` with two, on the comb to level `18`). The depth-1 material above any node is therefore a union of simple chains, never a bush.
4. **Which depth-1 nodes have a depth-1 parent** (equivalently, which are *not* direct children of an abdomen). For a link: the parent is an abdomen unless `s(Ω,1) = 1` and `Ω ≡ 1 (mod 8)`, i.e. the **orphan links** are exactly `Ω ≡ 17 (mod 24)` (**pre-checked**: all `66,666` depth-1 states, `0` mismatches; `1/8` of depth-1 states). For a fork the main session's derivation gives: parent of depth `1` iff `Ω ≡ 1 or 3 (mod 8)` (`s ≥ 3` gives a cascade parent of depth `1 + v₃((Ω+1)/4) = 1` since `Ω + 1 ≡ 2 (mod 3)`; `s = 2` gives a door parent of depth `≥ 2`; `s = 1` gives a door parent of depth `v₂((3Ω+1)/2)`, which is `1` iff `Ω ≡ 1 (mod 8)`). **Derive this fully and verify it; it was not pre-checked numerically.** State the complete residue table of "parent is an abdomen" for depth-1 nodes by `(Ω mod 3, Ω mod 8)`.
5. An **abdomen** `(Ω, D)` has depth-1 children — its **legs** — numbering `D − 1 + [3 ∤ 2^{D+1}Ω − 1] + [top door alive and its child of depth 1]`: the cascade child (core `4·3^{D−1}Ω − 1`), the children through doors `a = 2, …, D−1` (cores `2^{D−a+2} 3^{a−1} Ω − 1`), the `a = 1` child when its depth is `1` (core `2^{D+1}Ω − 1`), and the top-door child when its depth is `1`. Prove the leg cores and the count; note that legs are links or forks by their own residue.

## Item B — hairs, spiders and the partition (Definition 19.2.1, Theorem 19.2.2)

**Definition.** A **hair** is a maximal chain of depth-1 nodes `h₁ → h₂ → … → h_L` (each the unique depth-1 child of the previous) whose first node `h₁` is a leg — a depth-1 child of an abdomen — or the child of the root. The **spider** of an abdomen is the abdomen together with all hairs whose first node is one of its legs. The root's piece is `{(1,1)}` alone.

**Theorem (partition).** Every comb node belongs to exactly one spider or to the root's piece: a node's *owner* is the first abdomen (or the root) met by descending through depth-1 parents. Proof from Item A.3 (chains, no bushes) and the tree property (18.2.2). **Pre-checked** on the comb to level `18`: `247,932` nodes, `82,491` pieces (one per abdomen plus the root), mean piece size `3.006`, largest `40`.

**Hair lengths.** **Pre-checked** distribution over the `96,620` hairs of the comb to level `18`: lengths `1: 53,145; 2: 28,290; 3: 8,818; 4: 4,031; 5: 1,442; 6: 544; 7: 222; 8: 77; 9: 30; 10: 13; 11: 6; 13: 1; 15: 1`. This is not geometric; it alternates by the class of the current node: a link continues with probability `1` (to a fork), a fork continues iff `t = 1`. **Derive the exact law:** the continuation rule per class, the class of each continuation, and the predicted length distribution given the class of the leg and the ledger for `t` (`P(t = j) = 2·3^{−j}` under the depth ledger; check whether the classes along a hair are determined by residues of the leg — the leg's core modulo `3^k` for a `k` growing with the length, per 18.9.2's budget — and what the exact per-window count of hair lengths is on a fixed door, in the spirit of 14.6.5.2). Report predicted against measured.

**Spider size.** The fraction of abdomens among nodes is `1 − P(D = 1) = 1/3` under the depth ledger, so the mean spider size is `3` given the ledger; the census's `3.006` is the calibration. State it with the ledger labeled as a measured law (18.7.2's own posture).

## Item C — the spider tree (Definition 19.3.1) and its census

**Definition.** The nodes of the spider tree are the spiders (and the root's piece); the parent of a spider is the owner of its abdomen's comb parent. Its children are spawned by: the abdomen's own deeper children (the `a = 1` child when `3 | 2^{D+1}Ω − 1`, the top-door child when its depth is `≥ 2`), and by each fork in its hairs (the fork's cascade child, always an abdomen; the fork's top-door child when `t ≥ 2`). Links spawn nothing. Prove that this is a tree rooted at the root's piece and that its edges are exactly the comb's edges from a spider's nodes to abdomens outside it.

**Census.** Enumerate the comb to level `18` (a second of work) and build the spider tree over it: per spider, its size, its number of legs and hairs, its abdomen's depth `D`, and its number of child spiders; then the spider tree's own levels (spider level = number of spider edges to the root's piece) with counts per level and the growth ratio, and the distributions of size, legs and child-spider count against what Items A–B predict under the ledger. **Where the determinism lives at this layer:** derive which spider-level quantities are exact functions of the abdomen's `(D, Ω mod 3^k)` for bounded `k` (the leg count and the legs' cores are; the hair lengths and the child-spider count need digits growing with the hair length — say how many, from 18.9.2's budget applied along a hair). Then one measurement in the style of 18.9.3: the exact residue modulus of the abdomen's core that fixes the whole spider (all hairs, all classes), its distribution over spiders, and its growth with spider size. Report flat.

**One exact law to look for, stated as a question, answered either way:** is the number of child spiders of a spider an exact function of `(D, Ω mod 3^k)` for a `k` independent of the spider's size? (The abdomen's contribution is; the hairs' contribution is a sum over its forks of `1 + [t ≥ 2]`, and hair lengths are unbounded, so the expectation is *no*, with the reason stated.)

## Item D — the explorer (small)

Add to `viz/comb_explorer.html` a **class badge** on every node card — `abdomen`, `leg`, `hair link`, `hair fork`, `orphan link`, `root` — computed from `(Ω, D)` and the parent's depth, by a pure function `nodeClass` placed inside the arithmetic core (between the markers; no other core change), and a one-line legend. Extend `experiments/comb_explorer_check.py` with the class rule on `2,000` random nodes against an independent Python implementation and the canaries `(1,2)` abdomen, `(7,1)` leg (fork), `(17,1)` orphan link, `(13,1)` leg (fork), `(67,1)` hair fork; regenerate its output. Nothing else in the page changes.

## Verification: `experiments/spider_layer.py`

Fresh code, imports nothing from any existing script (`peak_comb.py`, `comb_dictionary.py`, `signed_comb.py`, `comb_signatures.py` exist and are not to be imported or copied); exact integers at every pass/fail decision; canaries first (`(17,1)` with parent `(13,1)` and child `(67,1)`; `(13,1)` with children `(17,2)` and `(17,1)`; `(7,1)` with children `(1,4)` and `(1,3)`; the spider of `(1,2)` written out by hand in the findings and matched). Contents: (a) Item A's five claims on random states and on the whole comb to level `18`; (b) the partition on the comb to level `18` with the piece statistics; the hair-length law, predicted and measured; (c) the spider tree and its census; the residue-modulus measurement; the child-spider question. **One documented command reproduces the committed output in full** (`python experiments/spider_layer.py`), in a few minutes of wall clock at most. Foreground; wait; record counts, ranges, seed, date, wall clock.

## Wiki edits — conservative; content and structure in separate commits

- New page **`spiders.md`**, section **19. The spider layer**, front matter in the house style (`status: FORMULATION`; `scope: §19`; `updated`; `source: the author's direction of 2026-09-22; this brief`), a Current-state paragraph, then 19.1 (Item A), 19.2 (Item B), 19.3 (Item C), 19.4 standing (what the layer is: a residue-based coarse-graining of the comb by depth and by `Ω mod 24` and `mod 9`, sitting inside 18.9's horizon; what it is not: no front moves; the author's north star stated in one flat sentence as the direction of work, not as a claim). One verification line per proved claim.
- `comb.md`: one pointer sentence at the end of 18.9.5 (the first coarse-graining of the comb above the residue classes is spiders.md §19; pointer only); front matter `updated`.
- `index.md`: a page-table row for `spiders.md` and a resolver entry for §19, in the existing style.
- `symbols.md`: registry rows for **abdomen, fork, link, orphan link, leg, hair, spider, spider tree**, in the frame the page's structure suggests (§4, after the comb rows), with defining pointers; check the collision index.
- `TOUR.md`: one dictionary row — *spider layer; abdomen; hair* against the literature: no literature name found in the record's sources (say what was checked); the nearest classical object is the partition of the Collatz graph by residue classes mod `2^k 3^l` used in density arguments, which is a partition of integers, not of a tree.
- `README.md`: the `viz/` row's `comb_explorer.html` clause gains "with node classes"; nothing else.
- `briefs/spider-layer-findings.md`: derivations, what the pre-check got wrong (if anything), the verification record, the reading of Item C, and a *For the main session at merge* section.
- **Do not edit** `HANDOFF.md`, `reverse.md`, `ladder.md`, `itinerary.md`, `cycles.md`, `aeh.md`, `stage*.md`, `open-problems.md`, `publication.md`, `paper/`, or anything under `sources/`.
- Run `experiments/encoding_scan.py` before the final commit and record `RESULT: CLEAN`.

## Record

- `experiments/spider_layer.py` + committed output; `experiments/comb_explorer_check.py` + re-generated output.
- `spiders.md` §19; `viz/comb_explorer.html` with the class badge; the `comb.md`, `index.md`, `symbols.md`, `TOUR.md`, `README.md` entries.
- `briefs/spider-layer-findings.md`.

## Rules

- Branch **`spider-layer`** from your worktree HEAD. FIRST verify the worktree contains this brief (`briefs/spider-layer-brief.md`) and that `git log --oneline -1` shows a commit dated 2026-09-22; worktrees are sometimes cut from a stale HEAD — if either check fails, rebase onto local `main` before starting, and state your base SHA in the findings.
- No web access needed; no external resources in the page; no contact with anyone; no pushes; no edits outside this repository.
- File edits via the Edit/Write tools only — never PowerShell `Get-Content`/`Set-Content`.
- Register: flat, calibrated prose. The depth ledger is a measured law wherever it is used as a baseline. Statistical claims carry their baselines computed from the data, with expected cell counts adequate for the statistic used (see the comb-signatures findings' Revision 1 for what was sent back last time). Nothing proposed; no cycle search; no front reopened.
- Run the scripts in the foreground and wait; do not stop until every commit exists on the branch.
- Do NOT merge — the main session reviews (re-runs both scripts; re-derives the fork parent-depth table and the partition theorem independently; runs the core's `nodeClass` under node) and merges. Stop after Record.
