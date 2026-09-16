---
status: FORMULATION — a construction (the backward tree of reduced states re-indexed by peak level), its elementary structural properties proved with fresh code, and a census; no front moves
scope: new section 18 (post-monolith)
updated: 2026-09-15
source: the author's session of 2026-09-15; briefs/peak-comb-brief.md
---

> **Current state.** The backward tree of reduced states (reverse.md 14.4), with the even integer `A = 3^d ω − 1` — the structural-step numerator — counted as the coordinate of its node (the **peak**), and each door's infinite fan over the exit valuation `s` replaced by a chain: a node at branch `s ≥ 3` hangs from the node at branch `s − 2` on the same door (a **cascade edge**, reverse.md 14.10.1's step read downward), and the node at the lowest admissible branch hangs from the door's own state (a **door edge**, one `F`-step). Proved: peaks and states are in bijection; the parent rule is well defined and its graph on the states whose `F`-orbit reaches `(1,1)` is a tree rooted at `(1,1)` with exactly the node set of 14.4; every node has finite degree — one cascade child plus one door child per live door — so every level is finite with no size cutoff, and no node is a leaf; the root has exactly one child; the two distances (reduced `η` = `F`-steps, peak `λ` = level) obey `η = 1 +` door edges and `λ − η + 1 =` cascade edges `≥ 1`, the `+1` being the root's own self-loop; the comb re-indexes 14.1.1's completeness against the raw map exactly; the largest peak at level `λ` is `2^{2λ+1}`, on door `1`. A census to level `27` (`126,917,355` nodes, doubling per level) and one exploratory table, reported flat. The comb moves no front: the conjecture is the statement that it spans every state (Theorem 9.8.3), unchanged.

# 18. The peak comb

The tree of reverse.md §14.4 is indexed by core size, and each of its doors carries an infinite family of predecessors, one per admissible `s` (14.1.1). This section indexes the same tree by distance from `(1,1)`, with a different choice of what a step is. The author's observation (2026-09-15): an orbit entering a door at a high branch falls, on its way down, through the peaks of every lower branch on that door — the peaks are on the raw trajectory, the lower branches' odd points are not — so the natural neighbour of a branch-`s` node is the branch-`(s−2)` node below it, not the door's state. Making that the parent turns each door's fan into a chain, and the tree into what the author called a comb. Nothing here is new dynamics: the object is 14.1.1's predecessor structure with one parent chosen per node.

## 18.1. The peak

**Definition 18.1.1 (the peak).** For a valid state `(ω,d)` the **peak** is the even integer `A(ω,d) = 3^d ω − 1` — spine.md §4.5's structural-step numerator, here counted as the coordinate of the node. With `s = v₂(A)` and `y = A/2^s` the exit (a door of `F(ω,d)`, reverse.md 14.14.1), the peak sits at **branch `s` on the door `y`**: `A = 2^s y`.

**Lemma 18.1.2 (peaks and states).** (i) The peak determines the state: `d = v₃(A+1)`, `ω = (A+1)/3^d`. (ii) A positive even integer `A` is a peak iff `3 | A + 1`, i.e. iff `A ≡ 2 (mod 6)`; so peaks and valid states are in bijection. (iii) Fix an odd `y`. Among the even numbers `2^j y`, `j ≥ 1`, the peaks are exactly those with `2^j y ≡ 2 (mod 3)`: none if `3 | y`; the odd `j` if `y ≡ 1 (mod 3)`; the even `j` if `y ≡ 2 (mod 3)`. Peak and non-peak alternate along the cascade, and the peaks on door `y` are `2^s y` for exactly the admissible branches `s` of 14.1.1, `2^s y` being the peak of the predecessor at branch `s`.

**Proof.** (i) `A + 1 = 3^d ω` with `3 ∤ ω`, so `v₃(A+1) = d` and the cofactor is `ω`. (ii) A peak has `A + 1 = 3^d ω` an odd multiple of `3`. Conversely, if `A ≥ 2` is even and `3 | A + 1`, then `A + 1` is odd, `d := v₃(A+1) ≥ 1`, `ω := (A+1)/3^d` is odd and prime to `3`, and `A = 3^d ω − 1` is the peak of the valid state `(ω,d)`; `A ≥ 2` is automatic from `d, ω ≥ 1`. (iii) `3 | 2^j y + 1` iff `2^j y ≡ 2 (mod 3)` iff `(−1)^j y ≡ −1 (mod 3)`, which is the stated parity rule and is 14.1.1's admissibility condition verbatim. When it holds, `2^j y + 1 = 3^d ω` defines the predecessor at branch `j` on door `y`, whose exit is `y` and whose exit valuation is `v₂(3^d ω − 1) = v₂(2^j y) = j`. ∎

**Remark 18.1.3 (the raw maximum is `2A`).** From any representative `x_a = 2^{d−a} 3^a ω − 1` the block's raw trajectory is `x_a, 2x_{a+1}, x_{a+1}, …, x_{d−1}, 2A, A, A/2, …, 2y, y` (spine.md §6.3, Proposition 9.1.1: `3x_b + 1 = 2x_{b+1}` and `3x_{d−1} + 1 = 2A`). Its maximum is `2A`, one halving above the peak, and `2A` is never a peak: `2A + 1 = 2·3^d ω − 1 ≡ −1 (mod 3)`. The record's laws are written on `A`, so the peak is `A`; `2A` is a fact about the raw map's bookkeeping only.

**Worked instance.** Door `5` (`≡ 2 mod 3`, even branches) carries `(7,1)`, `(1,4)`, `(107,1)` at `s = 2, 4, 6`, with peaks `20`, `80`, `320` (`4·5 + 1 = 21 = 3·7`; `16·5 + 1 = 81 = 3^4`; `64·5 + 1 = 321 = 3·107`). The entry of `(107,1)` is `213`, and its raw orbit `213, 640, 320, 160, 80, 40, 20, 10, 5` passes the peaks `80` and `20` of the two lower branches and none of the odd points `15, 23, 35, 53` of `(1,4)` or `13` of `(7,1)`.

**Verified** — `experiments/peak_comb.py`, fresh code (imports nothing from any other script; exact integers at every decision; seed `20260915`; 2026-09-15), section (a): the bijection on `2,002` random states (`ω < 10^6`, `d ≤ 40`) and `3,000` random even integers below `10^12` (a peak iff `≡ 2 mod 3`), the alternation and the branch-`j` identification on `2,000` random odd `y` (`3 | y` included) at `j = 1, …, 40`, `80,000` pairs; the worked instance as a canary; `0` failures.

## 18.2. The comb

**Definition 18.2.1 (the comb).** Nodes: the valid reduced states. Every node `v = (ω,d) ≠ (1,1)` has exactly one **comb parent**, read off its peak `A = 2^s y`:

- `s ≥ 3`: the **cascade parent**, the state at branch `s − 2` on the same door, `((2^{s−2} y + 1)/3^v, v)` with `v = v₃(2^{s−2} y + 1)`; the edge is a **cascade edge**;
- `s ≤ 2`: the **door parent** `state(y) = F(ω,d)`; the edge is a **door edge**.

The root `(1,1)` (`A = 2`, `s = 1`, `y = 1`) has no parent: its door parent would be `state(1) = (1,1)` itself — the `s = 1` self-loop of door `1` — and that loop is excluded. **Siblings** are the nodes on one door; the **lowest sibling** is the one at branch `s₀ ∈ {1,2}`, `s₀ = 1` iff `y ≡ 1 (mod 3)`.

**Proposition 18.2.2 (the comb is the backward tree).** (a) The rule is well defined: the cascade parent is a valid state with exit `y` and exit valuation `s − 2`, and the door parent is `F(ω,d)`. (b) From a node at branch `s` on door `y`, `⌊(s−1)/2⌋` cascade edges lead to the lowest sibling; if that node is the root then `y = 1` and `F(v) = (1,1)`; otherwise its parent edge is the door edge to `F(v)`. (c) The parent chain from `v` reaches the root iff the `F`-orbit of `v` reaches `(1,1)`. Consequently the parent map, restricted to the states whose `F`-orbit reaches `(1,1)`, is a tree rooted at `(1,1)` whose node set is exactly the backward tree of 14.4; the Collatz conjecture is the statement that the comb spans every valid state (Theorem 9.8.3).

**Proof.** (a) `4 ≡ 1 (mod 3)` gives `2^{s−2} y ≡ 2^s y ≡ 2 (mod 3)`, so `3 | 2^{s−2} y + 1`, `v ≥ 1`, and the cofactor is odd and prime to `3`; the parent's numerator is `2^{s−2} y`, so its exit valuation is `s − 2 ≥ 1` and its exit is `y`. The door parent is `F(ω,d) = R(x_exit) = state(y)` (spine.md §3.7; Proposition 14.14.1.1). (b) Each cascade edge keeps the door and lowers the branch by `2` (by (a)); after `⌊(s−1)/2⌋` edges the branch is `s − 2⌊(s−1)/2⌋ ∈ {1,2}`, odd iff `s` is odd iff `y ≡ 1 (mod 3)` (Lemma 18.1.2(iii)). All siblings share the exit `y`, so at the lowest sibling `w` the rule gives the door edge to `state(y) = F(w) = F(v)` — unless `w = (1,1)`, which forces `y = 1` (the root's exit) and then `F(v) = state(1) = (1,1)`. (c) By (b) the chain from `v` reaches `F(v)` in `⌊(s−1)/2⌋ + 1` edges, or stops at the root with `F(v) = (1,1)`; by induction it visits `F(v), F²(v), …` in that order until it stops, and it stops only at the root. If `F^t(v) = (1,1)` the chain reaches it. Conversely the chain's nodes are the `F^i(v)` and their cascade ancestors on the doors of the `F^{i+1}(v)`; the root is the lowest sibling of door `1`, so reaching it means some `F^i(v)` is on door `1` — then `F^{i+1}(v) = (1,1)` — or is the root itself. A chain that ends at the root cannot revisit a node (each node has one parent, and the root has none), so the restriction is a tree; its node set `{v : F-orbit of v reaches (1,1)}` is 14.4's tree by that section's own definition. ∎

**Proposition 18.2.3 (children; the degree formula; the root's single child).** Read upward, a node `(Ω,D)` with peak `A = 2^s y` has:

- one **cascade child**, the state at branch `s + 2` on its own door `y` — reverse.md 14.10.1's `N(y, s+2) = 4·N(y,s) − 3` — with peak `4A`;
- one **door child** per live door `y_a` of `(Ω,D)` (`a = 0, …, D−1`, `3 ∤ y_a`): the state at the lowest admissible branch on `y_a`, `s = 1` if `y_a ≡ 1 (mod 3)`, `s = 2` if `y_a ≡ 2 (mod 3)` — the 14.1.1 predecessor of `(Ω,D)` at that branch. Every other 14.1.1 predecessor of `(Ω,D)` is on the cascade chain above one of these.

So the degree is `1 + D` or `1 + (D − 1)`: the top door `y_0 = 2^D Ω − 1` is dead iff `2^D Ω ≡ 1 (mod 3)`, side doors are never dead (Theorem 14.5.1). Every node has finite degree, every level is finite, and no size cutoff is needed to enumerate a level. The one exception to the door-child count is the root, whose only door child would be itself: **the root has exactly one child, `(1,2)`**, and door `1`'s chain is `(1,1), (1,2), (11,1), (43,1), (19,3), …` at branches `1, 3, 5, 7, 9, …`.

**Proof.** A node's parent edge is a cascade edge iff its `s ≥ 3`, so the cascade children of `(Ω,D)` are the nodes at branch `s + 2` on door `y` — exactly one, branch `s + 2` being admissible when `s` is (Lemma 18.1.2(iii)), with peak `2^{s+2} y = 4A`. A node with `s ≤ 2` has door parent `state(y)`, its door `y` is a live door of that state (`y` is its exit, so `3 ∤ y`, and `y` is a representative of `state(y)` by door recovery, 14.6.5.1), and its branch is the lowest admissible one; conversely each live door `y_a` of `(Ω,D)` carries exactly one node at its lowest branch and its door parent is `state(y_a) = (Ω,D)`. The remaining predecessors of 14.1.1 are the higher branches on the same doors, reached from the lowest-branch node by cascade edges (Proposition 18.2.2(b) read upward). The door count is Theorem 14.5.1. A door child coincides with its parent only if `F(v) = v`; for the root, `y_0 = 1` at branch `1` gives `(1,1)`, the excluded loop, and the root's only child is its cascade child at branch `3` on door `1`, `2^3 + 1 = 9 = 3^2`, i.e. `(1,2)`. Any other comb node has an `F`-orbit reaching `(1,1) ≠ v`, so is not `F`-fixed. ∎

**Remark 18.2.4 (no leaves).** Every node has a cascade child, so the comb has no leaves. A Garden of Eden (14.5.2: `D = 1`, `Ω ≡ 2 (mod 3)`, no `F`-preimage) has exactly one child — its cascade child, which is its own sibling under `F`. Door mortality costs a node one door child, never its continuation.

**Lemma 18.2.5 (the `4A` law).** Along a cascade chain the peaks are `A, 4A, 16A, …` exactly: the node at branch `s + 2` on door `y` has peak `2^{s+2} y = 4·2^s y`. This is 14.10.1's identity with the `−3` moved across: `N(y,s+2) − 1 = 4(N(y,s) − 1)`. ∎

**Verified** — `experiments/peak_comb.py`, section (b), 2026-09-15: on the box `ω < 10^5` (`3 ∤ ω`), `1 ≤ d ≤ 30` (`999,990` states) the parent is valid, of the stated type, at branch `s − 2` on the same door or equal to `F`, and the node is regenerated exactly once by its parent's child rule; the local chain lemma (b) at every state; the self-child exclusion fired at no state of the box other than the root. Reachability: every state with `ω < 2·10^4`, `d ≤ 30` (`200,010` states) has an `F`-orbit reaching `(1,1)` (largest `η = 148`); on `3,000` random states of the full box the whole parent chain and the whole `F`-orbit were computed separately and compared (largest level `161`). Degree formula: `2,000` random states (`Ω < 10^4`, `D ≤ 12`), children distinct, each child's parent the node, door children equal to the 14.1.1 predecessors at `s ≤ 2`, and all `361,890` predecessors at `s ≤ 60` placed on cascade chains above a door child; a brute-force forward scan of all `(ω ≤ 3000, d ≤ 12)` against the comb's prediction at eight targets including `(1,1)`; the root's single child and door `1`'s chain as canaries. Section (c): the `4A` law and the `2A` raw maximum from every representative of `3,000` random states (`20,759` block trajectories; the even peaks a trajectory passes are exactly the lower siblings' peaks). `0` failures.

## 18.3. The two distances

**Definition 18.3.1.** For a comb node `v`, the **reduced distance** `η(v)` is the number of `F`-steps from `v` to `(1,1)`, and the **peak distance** `λ(v)` is the number of comb edges from `v` to the root — its **level**. (The brief's provisional `r` and `ℓ` were not adopted: both glyphs carry registry rows, symbols.md §3–4 and §6.)

**Proposition 18.3.2.** For every node `v ≠ (1,1)`:

- (a) the path from `v` to the root ends with the cascade edge `(1,2) → (1,1)`, whatever `v` is;
- (b) `η(v) = 1 + (number of door edges on the path)`, and the number of cascade edges is `λ(v) − η(v) + 1 ≥ 1`;
- (c) all siblings on one door share `η` — each is one `F`-step from the door's state — and are separated by `λ`: the node at branch `s` sits `(s − s₀)/2` levels above the lowest sibling;
- (d) `λ(v) ≥ η(v)`, with equality iff the path carries exactly one cascade edge, the terminal one — i.e. iff `s(F^i(v)) ≤ 2` for every `F^i(v)` before `(1,2)` and the orbit enters `(1,1)` from `(1,2)`.

**Proof.** (a) is Proposition 18.2.3: the root's only child is `(1,2)`, by a cascade edge. (b) By Proposition 18.2.2(b)–(c) the path visits `F(v), F²(v), …, F^t(v) = (1,1)`, `t = η(v)`, in order; it enters each `F^{i+1}(v) ≠ (1,1)` by a door edge and enters `(1,1)` by the cascade chain of door `1` (a). So the door edges number `t − 1`, and the remaining `λ − (t − 1)` edges are cascade edges, at least the terminal one. (c) Siblings share the exit, hence `F`; the branch-`s` node reaches the lowest sibling by `(s − s₀)/2` cascade edges (18.2.2(b)). (d) From (b): `λ − η = (cascade edges) − 1 ≥ 0`, with equality iff there is exactly one cascade edge; the cascade edges on the path are the runs `⌊(s(F^i(v)) − 1)/2⌋` of the orbit's states, plus the terminal run on door `1`, which is one edge exactly when the orbit's last state before `(1,1)` is `(1,2)`. ∎

The `+1` in (b) is the root's self-loop: the door edge that would stand for the last `F`-step would run from the branch-`1` node of door `1` — the root — to itself, and the comb enters the root by door `1`'s cascade chain instead. Read without that boundary, "`η` = door edges" is off by one at every node: `(1,2)` has `η = 1` and no door edge; `(11,1)` has `η = 1` and two cascade edges.

**Verified** — `experiments/peak_comb.py`, sections (b) and (d), 2026-09-15: on the `3,000` full chains of 18.2's verification and on `17,245` census nodes (every node while a level has at most `2,000`, a deterministic hash sample of about `2,000` per level above), `η` computed by iterating `F` and `λ` by the parent rule: `η = 1 +` door edges, cascade edges `= λ − η + 1 ≥ 1`, the terminal edge `(1,2) → (1,1)`, and `λ ≥ η` with equality iff one cascade edge, at every node; "`η` = door edges" held at none of them. `0` failures.

## 18.4. Completeness against the raw map

The comb accounts for every way into a state under the raw map `Col`; this is Proposition 14.1.1's completeness (doors × admissible `s`) re-indexed, and the following records the dictionary. An integer `z` has at most one odd `Col`-predecessor, `w = (z − 1)/3`, present iff `z ≡ 4 (mod 6)`; its even predecessor `2z` is always present and is the next point up its own cascade.

**Proposition 18.4.1 (odd predecessors along a block).** Let `x_a` be a representative of `(ω,d)` with peak `A = 2^s y`, and take the block's raw trajectory `x_a, 2x_{a+1}, x_{a+1}, …, x_{d−1}, 2A, A, …, 2y, y` (Remark 18.1.3). The odd predecessors of its points are:

- the odd points `x_b`: none;
- `2x_b` (`a < b ≤ d − 1`) and `2A`: the previous odd point of the block, `x_{b−1}` and `x_{d−1}` — the block's side doors in turn (14.8.4);
- a cascade point `2^j y`, `1 ≤ j ≤ s`, when it is a peak (`2^j y ≡ 2 mod 3`): none;
- a cascade point `2^j y` that is not a peak, `j ≥ 2`: the last odd point `2·3^{d'−1} ω' − 1` of the sibling `(ω',d')` at branch `j − 1` on door `y` — the cascade point is that sibling's `2A'`;
- `2y` when `y ≡ 2 (mod 3)`, i.e. `y = y_{a'}` is a side door of `state(y)`, `a' ≥ 1`: the previous door `y_{a'−1}` of `state(y)`; when `y ≡ 1 (mod 3)`, `2y` is the peak of the branch-`1` node and has none.

So along a block the odd ways in are: the block's own rising run (its side doors), the lower siblings on its door (through their peaks, which the trajectory passes), and — at the last even point — the next state's own rising run. Nothing else, and every 14.1.1 edge appears exactly once.

**Proof.** Odd `z` is never `≡ 4 (mod 6)`. `2x_b = 3x_{b−1} + 1` and `2A = 3x_{d−1} + 1` (Proposition 9.1.1, spine.md §6.3). For `z = 2^j y`: `z ≡ 4 (mod 6)` iff `2^j y ≡ 1 (mod 3)` iff `2^{j−1} y ≡ 2 (mod 3)`, which by Lemma 18.1.2(iii) says `j − 1` is an admissible branch (for `j ≥ 2`) or `j = 1` with `y ≡ 2`. Then `w + 1 = (2^j y + 2)/3 = 2(2^{j−1} y + 1)/3`. For `j ≥ 2`, `2^{j−1} y + 1 = 3^{d'} ω'` is the sibling at branch `j − 1`, so `w = 2·3^{d'−1} ω' − 1`, its representative `a = d' − 1`. For `j = 1`, `y + 1 = 2^m 3^{a'} Ω` with `a' ≥ 1`, so `w + 1 = 2^{m+1} 3^{a'−1} Ω`, i.e. `w = y_{a'−1}` of `state(y) = (Ω, m + a')`. ∎

**Verified** — `experiments/peak_comb.py`, section (e), 2026-09-15: for every odd `x < 2·10^5`, the block trajectory computed by iterating `Col` equals the bookkeeping list, and at each of its `699,994` points the odd predecessor computed from `z ≡ 4 (mod 6)` equals the comb's prediction; `0` failures.

## 18.5. The census

**Lemma 18.5.1 (the largest peak at a level).** The largest peak among the nodes at level `λ` is `2^{2λ+1}`, attained by door `1`'s chain node at branch `2λ + 1` and by no other node.

**Proof.** A cascade child has peak `4A`; a door child at the lowest branch `s₀ ≤ 2` on a door `y_a` has peak `2^{s₀} y_a ≤ 4 y_{D−1} < 4·(2A/3) < 4A`, since the largest door `y_{D−1} = 2·3^{D−1} Ω − 1` satisfies `3 y_{D−1} + 1 = 2A`. So the maximum at level `λ + 1` is four times the maximum at level `λ`, attained only by the cascade child of the previous maximum; from the root's `A = 2` this is `2·4^λ`, on door `1`. ∎

**The level table.** `experiments/peak_comb.py`, section (f): the comb enumerated from `(1,1)` level by level (a level-by-level pass to level `20` and a depth-first pass to level `27`; the two agree row for row), with no size cutoff — every level is finite by Proposition 18.2.3. Per level: node count, the number of nodes entered by a cascade edge and by a door edge, the distribution of `d`, and the largest peak (`2^{2λ+1}`, Lemma 18.5.1).

```text
level     nodes  cascade-in   door-in  depth distribution (d:count)                                 largest peak
    0         1           0         0  1:1                                                        2
    1         1           1         0  2:1                                                        8
    2         2           1         1  1:2                                                        32
    3         3           2         1  1:1 3:1 4:1                                                128
    4        10           3         7  1:7 2:2 3:1                                                512
    5        17          10         7  1:14 2:3                                                   2048
    6        30          17        13  1:18 2:10 3:2                                              8192
    7        61          30        31  1:37 2:16 3:7 4:1                                          32768
    8       124          61        63  1:87 2:26 3:6 4:4 5:1                                      131072
    9       239         124       115  1:159 2:58 3:17 4:2 5:1 7:1 8:1                            524288
   10       478         239       239  1:311 2:111 3:39 4:13 5:4                                  2097152
   11       961         478       483  1:628 2:204 3:81 4:30 5:10 6:5 7:3                         8388608
   12      1978         961      1017  1:1358 2:435 3:129 4:38 5:13 6:5                           33554432
   13      3823        1978      1845  1:2527 2:854 3:303 4:97 5:27 6:8 7:4 8:1 9:1 >9:1          134217728
   14      7748        3823      3925  1:5103 2:1745 3:584 4:206 5:74 6:22 7:9 8:5                536870912
   15     15597        7748      7849  1:10533 2:3425 3:1111 4:356 5:112 6:33 7:18 8:9            2147483648
   16     30844       15597     15247  1:20518 2:6878 3:2290 4:774 5:257 6:86 7:27 8:8 9:4 >9:2   8589934592
   17     61947       30844     31103  1:41131 2:13852 3:4631 4:1550 5:523 6:175 7:59 8:18 9:6 >9:2 34359738368
   18    124068       61947     62121  1:83007 2:27438 3:9077 4:3025 5:1028 6:338 7:96 8:38 9:14 >9:7 137438953472
   19    247507      124068    123439  1:164761 2:54928 3:18497 4:6259 5:2051 6:686 7:231 8:67 9:20 >9:7 549755813888
   20    495986      247507    248479  1:330699 2:110194 3:36624 4:12363 5:4103 6:1345 7:451 8:153 9:37 >9:17 2199023255552
   21    991393      495986    495407  1:661294 2:219939 3:73436 4:24585 5:8130 6:2656 7:919 8:296 9:90 >9:48 8796093022208
   22   1982520      991393    991127  1:1321407 2:440768 3:146701 4:48935 5:16292 6:5580 7:1905 8:631 9:206 >9:95 35184372088832
   23   3966341     1982520   1983821  1:2644323 2:881392 3:293996 4:97753 5:32580 6:10893 7:3606 8:1194 9:385 >9:219 140737488355328
   24   7931430     3966341   3965089  1:5288102 2:1761956 3:587086 4:195928 5:65509 6:21893 7:7284 8:2430 9:819 >9:423 562949953421312
   25  15864465     7931430   7933035  1:10574822 2:3525352 3:1176339 4:391906 5:130532 6:43604 7:14601 8:4863 9:1615 >9:831 2251799813685248
   26  31732224    15864465  15867759  1:21157717 2:7050153 3:2349809 4:783445 5:260578 6:86878 7:28987 8:9730 9:3262 >9:1665 9007199254740992
   27  63457557    31732224  31725333  1:42303397 2:14099510 3:4701082 4:1568814 5:523400 6:174259 7:57909 8:19383 9:6465 >9:3338 36028797018963968
```

`126,917,355` nodes over levels `0..27`. Growth is a doubling per level — the ratio of consecutive counts is within `1%` of `2` from level `17` on and `2.000` to three decimals from level `22` — because every node has one cascade child and, on average, close to one live door (`0.9998` door children per node into level `27`). The cascade-in column at level `λ` is exactly the node count at level `λ − 1`. The depth distribution of a level matches the backward depth ledger `P(d = j) = 2·3^{−j}` (14.3) to three decimals at `j ≤ 5` from level `20` on (level `27`: `0.6667, 0.2222, 0.0741, 0.0247, 0.0082`). **Wall clock** for the depth-first pass on the author's machine: `215.6 s` (`257 s` for the whole script); the single reproducing command is `python experiments/peak_comb.py`. One more level would double both.

**Comparison with 14.4's core-size counts.** The tree of 14.4 is enumerated by expanding states in increasing core with a cutoff `ω ≤ X` — it counts the states reachable backward from `(1,1)` *through states with `ω ≤ X`*, not every tree state with `ω ≤ X` (a state with a small core whose `F`-image has a large core is never reached by that expansion). Re-enumerated here from 14.1.1 with fresh code, every door's scan over `s` run to the same branch cap as 14.4's script: `834` states at `2^10` and `6,280` at `2^13`, equal to 14.4's counts (the script also runs the scan with an early stop — the first branch past `s₀ + 6` whose predecessor's core exceeds `X` — and shows what such a stop drops: `(59,5)` at `2^10`, `19` states at `2^13`, each a genuine 14.1.1 predecessor at a branch past the stop, so the cap and not the stop is the correct convention). Every one of the `834` and `6,280` states has a finite peak distance (largest `λ = 35` and `43`, means `15.4` and `19.6`), and every one with `λ ≤ 27` is a census node at exactly that level (`766` and `4,997` states). The census's own nodes with `ω ≤ 2^10` number `2,088` (`1,322` of them outside 14.4's box tree, each with an `F`-iterate of core `> 2^10` — e.g. `(713,5) → (43315,1)`), and `12,211` with `ω ≤ 2^13` (`7,214` outside). The counts agree exactly on the object 14.4 enumerates; the naive comparison does not, because 14.4's box is connected through the box and the comb's levels are not.

**The forced opening run (ladder.md 15.6.2) in comb language.** The mechanism of Proposition 15.6.2 is orbit-level and reads on the comb as: a depth-`1` node with core `κ ≡ 1 (mod 2^j)` exactly, `j ≥ 3`, has a door edge at `s = 1` — through the parent's top door, `m₊ = 1`, no `3`-gain — to a depth-`1` node with core `≡ 1 (mod 2^{j−2})` exactly, and so on while `j ≥ 3`: a forced chain of `⌊(j−1)/2⌋` door edges toward the root, all at `s = 1`, ending at a depth-`1` core with `j ∈ {1,2}`, after which the next edge is not forced. Not re-proved here; the mechanism is 15.6.2's own. **Verified** on the comb, section (g): every depth-`1` census node with core `≡ 1 (mod 8)` (`14,099,479` nodes over levels `0..27`) has the stated chain, with the exact valuation `j − 2` at each step; `0` failures.

**One exploratory table, reported flat** (section (h)). Along the path from a node to the root the edge types come in runs; each maximal cascade run is a node's own run above its lowest sibling, of length `k = ⌊(s−1)/2⌋`, and each maximal door run is a run of consecutive `F`-steps with `s ≤ 2`. Tabulated over the census (each run once, at its top node) and, beside it, over the uniform box `ω < 10^5`, `d ≤ 30`, against the exit-valuation ledger `P(s = j) = 2^{−j}` (14.3), which predicts `P(k) = (3/4)·4^{−k}` for a state's own run, a geometric door run `P(n) = (1/4)(3/4)^{n−1}`, and door edges at `s = 1` versus `s = 2` in the ratio `2 : 1`:

```text
own cascade run k (each maximal cascade run once; 126,917,354 census nodes, 999,990 box states)
   k    census fraction   ledger (3/4)4^-k   box fraction
   0        0.49999           0.75000          0.75001
   1        0.25002           0.18750          0.18749
   2        0.12500           0.04688          0.04687
   3        0.06249           0.01172          0.01172
   4        0.03125           0.00293          0.00293
   5        0.01562           0.00073          0.00073
door run n (each maximal door run once; 63,457,556 census door children; box states with s <= 2, forward)
   n    census fraction   ledger (1/4)(3/4)^(n-1)   box fraction
   1        0.50001           0.25000                0.24997
   2        0.24999           0.18750                0.18752
   3        0.12492           0.14062                0.14076
   4        0.06251           0.10547                0.10533
   5        0.03131           0.07910                0.07875
   6        0.01562           0.05933                0.05988
door edges at s=1 : s=2 -- census 0.5000 : 0.5000; ledger 0.6667 : 0.3333; box 0.6667 : 0.3333
mean door run -- census 2.000, ledger 4.000, box 3.992; mean own cascade run -- census 1.0000, ledger 0.3333, box 0.3333
```

The box population matches the ledger at every printed entry. The census population does not, and the deviation is structural, not new: every node has exactly one cascade child, so about half of every level sits above its lowest sibling (`P(k) ≈ 2^{−(k+1)}` in place of `(3/4)4^{−k}`), a door run is cut in half for the same reason, and the comb counts each door once whereas the ledger weights doors by forward visits — the same door multiplicity `D` that 14.5.3's renewal carries as its `E_D` factor. A calibration line; nothing is proposed.

## 18.6. Standing

What the comb is: the classical Collatz inverse tree — Lagarias 1985's Collatz graph, equivalently the Syracuse preimage tree — with each block's odd rising run contracted to its reduced state and the halvings of a cascade taken in pairs, so that the two preimages of the graph, `2z` and `(z−1)/3`, become the cascade edge and the door edge (TOUR.md's dictionary row). It is a re-indexing of 14.1.1: the same predecessor set, one parent chosen per node, the infinite fan over `s` replaced by a chain, every level finite. Its two distances separate what a step of `F` counts (`η`) from what the raw orbit's descent through the peaks counts (`λ`), and the `+1` between them is the root's self-loop.

What it is not: no front moves. Nothing in this section constrains which states the comb reaches; the node set is the backward tree of 14.4 by definition, and the conjecture is the statement that the comb spans every valid state (Theorem 9.8.3, unchanged). The census is a count, the exploratory table a calibration line, and the family frame (grouping states by core, ladder.md §15's column relations) is not used here except for the one orbit-level law of 15.6.2. Grade: **formulation**.

The comb can be walked node by node in `viz/comb_explorer.html`, which expands the tree one node at a time from `(1,1)` and shows, for any node, its peak, branch and door, `η` and `λ`, its path to the root, its raw descent through the lower siblings' peaks, and the siblings on its door, every integer exact (its arithmetic core is checked against an independent implementation by `experiments/comb_explorer_check.py`).

## 18.7. The comb as the word: the dictionary, the mean degree, the two determinacies, and the digit-transfer law

The author's question (2026-09-16): how to look for inter-state determinism along `λ` and `η`, and whether the doors need an enumeration of their own, like the letter system of itinerary.md 14.15.1. No new alphabet is needed: the comb's edges are the letter system in door coordinates, and `η` and `λ` are statistics of the itinerary word (18.7.1). What the comb adds is one tree on which the forward, 2-adic determinacy (along door edges) and the backward, 3-adic one (along cascade chains) sit together, one identity for its level growth (18.7.2), and one exact count at the seam between the two determinacies (18.7.3). Nothing here is new dynamics, and the family frame is not used.

### 18.7.1. The path is the word

**Lemma 18.7.1.** Let `v ≠ (1,1)` be a comb node with `F`-orbit `v = v₀, v₁, …, v_η = (1,1)`, `η = η(v)`, and for `i < η` let `s_i = s(v_i)` be the exit valuation, `y^{(i)}` the exit (a door of `v_{i+1}`) and `a_i = v₃(y^{(i)} + 1)` its door index in `v_{i+1}` (`a_i = a₊` of the step, 14.14.1.1). Then:

- (a) the comb path from `v` to the root is, for `i = 0, …, η − 2`, `⌊(s_i − 1)/2⌋` cascade edges on door `y^{(i)}` followed by the door edge into `v_{i+1}` through its door `a_i`; and for `i = η − 1`, `(s_{η−1} − 1)/2 ≥ 1` cascade edges on door `1` ending at the root, with no door edge. Hence

```text
η(v) = number of F-steps,        λ(v) = Σ_{i<η} ⌊(s_i − 1)/2⌋ + (η − 1),
```

Proposition 18.3.2(b) with the cascade count written out;

- (b) in itinerary terms, let `W = ((m_0,r_0), …, (m_{η−1},r_{η−1}))` be the itinerary word of the exit `y^{(0)}` (Definition 14.14.8.1: `y^{(i+1)} = G(y^{(i)})`). Then `m_i = D_{i+1} − a_i` and `r_i = s_{i+1}` (14.14.6; `s_η = s(1,1) = 1`), the last letter is door `1`'s `(1,1)`, and

```text
η(v) = |W|,        λ(v) = ⌊(s_0 − 1)/2⌋ + Σ_{i<η} ⌊(r_i − 1)/2⌋ + (η − 1),
```

where `s_0` is the `r`-component of the letter of any door of `v` (all doors of one state share `r = s` of that state, 14.14.4). Letter `i ≤ η − 2` is the door edge into `v_{i+1}` through door `a_i = D_{i+1} − m_i` followed by `v_{i+1}`'s own cascade run of `⌊(r_i − 1)/2⌋` edges; the last letter contributes nothing — its door edge would be the root's excluded self-loop and its run is empty; the run of `v` itself precedes the word.

**Proof.** (a) From `v_i`, at branch `s_i` on door `y^{(i)}`, Proposition 18.2.2(b) gives `⌊(s_i − 1)/2⌋` cascade edges to the lowest sibling on that door; if it is not the root, its parent edge is the door edge to `state(y^{(i)}) = F(v_i) = v_{i+1}`, entering through the door `y^{(i)} = y_{a_i}(v_{i+1})` (door recovery). The lowest sibling is the root iff `y^{(i)} = 1` (the root is the branch-`1` node of door `1`, and a node on a door `y ≠ 1` is not on door `1`), iff `v_{i+1} = state(1) = (1,1)` (the only door of `(1,1)` is `1`), iff `i + 1 = η`. At `i = η − 1` the door is `1 ≡ 1 (mod 3)`, so `s_{η−1}` is odd, and `v_{η−1} ≠ (1,1)` sits at branch `≥ 3`. (b) `G(y)` is the exit of `state(y)` (14.14.3.2's proof), so the `G`-iterates of `y^{(0)}` are the orbit's exits; `m_i = v₂(y^{(i)} + 1) = D_{i+1} − a_i` by door recovery; `r_i = v₂(3^{D_{i+1}} Ω_{i+1} − 1) = s(v_{i+1})`; door `1` has `m = 1`, `r = v₂(3 − 1) = 1`. Substituting `r_i = s_{i+1}` in (a) gives the second formula. ∎

**Worked instance.** `(107,1)`: `A = 320 = 2^6·5`, `s_0 = 6`, exit `5`, `5 + 1 = 2·3`, so `a_0 = 1` — the side door of `state(5) = (1,2)`, whose doors are `3` (dead) and `5`; then `(1,2)` has `A = 8 = 2^3`, `s_1 = 3`, exit `1`. The path is two cascade edges `(107,1) → (1,4) → (7,1)` (branches `6, 4, 2` on door `5`), the door edge `(7,1) → (1,2)`, and the cascade edge `(1,2) → (1,1)`: `η = 2`, `λ = 2 + 1 + 1 = 4`. The word of the exit `5` is `((1,3), (1,1))` — door `5` has `m = 1`, `q = 3`, `r = v₂(9 − 1) = 3 = s_1` — and `λ = ⌊5/2⌋ + ⌊2/2⌋ + ⌊0/2⌋ + 1 = 4`.

**Grade.** A dictionary lemma; nothing is computed. Its content is that `λ` and `η` are word statistics — `η` the length of the word, `λ` a function of its `r`-components — so determinism "along `λ` and `η`" is determinism of the letter word: at every finite length the cylinder theorem (14.15.1.5), beyond it the Bridge. The doors need no enumeration of their own: the door index `a_i` is the letter's `m_i` read against the depth of the state entered.

**Verified** — `experiments/comb_dictionary.py`, fresh code (imports nothing from any other script; exact integers at every decision; seed `20260916`; 2026-09-16), section (a): on `3,000` random states (`ω < 10^6`, `d ≤ 40`; largest `η = 159`, `λ = 206`) the comb path by the parent rule equals the edge sequence predicted from the `F`-orbit's `(s_i, a_i)` edge for edge, each door edge enters `F(v_i)` through its door `a_i`, the last step ends in door `1`'s cascade run with no door edge, `η = 1 +` door edges, `λ` by the path and by both formulas, the `G`-iterates of the exit are the orbit's exits, `r_i = s_{i+1}` and `m_i = D_{i+1} − a_i` at every letter, the last letter is `(1,1)`, and every door of `v` has `r = s_0`; the `(107,1)` instance and door `1`'s chain as canaries; `0` failures.

### 18.7.2. The mean degree is 2

**Proposition 18.7.2.** (a) For every level `λ ≥ 1` the number of nodes at level `λ + 1` is the sum of the degrees at level `λ`, so, with Proposition 18.2.3's `deg = 1 + D − [top door dead]`,

```text
n_{λ+1} / n_λ = 1 + (mean D at level λ) − (dead-top-door fraction at level λ),
```

exactly. (b) If the depths at a level follow the backward depth ledger `P(D = j) = 2·3^{−j}` and the top door is dead on half the nodes, then the mean depth is `Σ_j 2j·3^{−j} = 3/2`, the mean number of door children is `1`, and the mean degree — the level ratio — is `2`.

**Proof.** (a) Every child of a level-`λ` node is at level `λ + 1`, and every level-`(λ+1)` node is the child of exactly one level-`λ` node; the root's degree is `1` and every other node's is `1 + D − [dead]`. (b) `Σ_{j≥1} j x^j = x/(1 − x)²` at `x = 1/3` is `3/4`, twice which is `3/2`; `3/2 − 1/2 = 1`. ∎

The two inputs of (b) are measured laws on the comb's levels, not theorems about them: the depth ledger is 14.2.4's measured law over the branches of a door (exact only per window of `3^k` consecutive branches on one door, 14.6.5.2 — a comb level is not such a window), and the `1/2` is 14.5.1's density over residue classes. So (b) says that given those inputs the level growth is exactly `2`; the census's ratio `2.000` from level `22` and its `0.9998` door children per node into level `27` (18.5) are the statement that the inputs hold on the levels. Measured per level on a fresh enumeration to level `20` (the full table is in the committed output):

```text
level    nodes  mean D  dead-top  door children  mean degree  next/this   P(D=1..4)
   16    30844  1.5027    0.4943         1.0084       2.0084     2.0084   0.6652 0.2230 0.0742 0.0251
   17    61947  1.5049    0.5021         1.0028       2.0028     2.0028   0.6640 0.2236 0.0748 0.0250
   18   124068  1.4956    0.5007         0.9949       1.9949     1.9949   0.6690 0.2212 0.0732 0.0244
   19   247507  1.5027    0.4987         1.0039       2.0039     2.0039   0.6657 0.2219 0.0747 0.0253
   20   495986  1.4998    0.5010         0.9988       1.9988        -     0.6668 0.2222 0.0738 0.0249
ledger 2/3^j                                                              0.6667 0.2222 0.0741 0.0247
```

**Verified** — section (b): a fresh level-by-level enumeration to level `20` (`991,425` nodes, `8.3 s`), counts equal to 18.5's table row for row; at every level `Σ deg = n_{λ+1}` and `Σ deg = n_λ + Σ D − #dead` as integer identities, every child valid, distinct and regenerating its parent under the parent rule, the degree formula at every node; `0` failures.

### 18.7.3. The two determinacies, and the digit-transfer law across a door edge

**The two determinacies, placed.** Along door edges toward the root, the next `k` letters of a node's word are fixed by its door modulo `2^N` — the cylinder theorem 14.15.1.5, which is the digit budget of stage4.md 11.8.7.7: finite prefixes are cheap, unbounded ones are the Bridge. Along a cascade chain on a fixed door everything is exact: the sibling at branch `s + 2` from the sibling at `s` by 14.10.1, and the depth sequence `d = 1 + v₃(s − M₃(y))` (14.2.4) with the exact ternary ledger 14.6.5.2. So on the comb, 2-adic determinacy runs along door edges and 3-adic determinacy along cascade chains, and the one seam between them is the door edge seen from the 3-adic side. The following counts it.

**Theorem 18.7.3 (digit transfer across a door edge).** Let a door edge have parent door `y` (odd, `3 ∤ y`), branch `s₀ ∈ {1,2}` (`s₀ = 1` iff `y ≡ 1 (mod 3)`) and child `(ω, d)`, `2^{s₀} y + 1 = 3^d ω`, whose doors are `y'_a = 2^{d−a} 3^a ω − 1`, `0 ≤ a ≤ d − 1`. Write `ỹ ↦ (ω̃, d̃)` for a second door edge.

1. `s₀` is a function of `y mod 3`, and `d` of `y mod 3^{d+1}`: `d ≥ k` iff `y ≡ −2^{−s₀} (mod 3^k)`. `d` is not a function of `y mod 3^d`: of the three lifts `y + 2t·3^d`, `t mod 3`, exactly one has `d̃ ≥ d + 1`.
2. For two door edges with the same `s₀` and the same `d`, and any `0 ≤ a < d`,

```text
v₃(y − ỹ) ≥ d        and        v₃(y'_a − ỹ'_a) = v₃(y − ỹ) − (d − a).
```

3. (Top door.) For `j ≥ 1`, `y'_0 mod 3^j` is a function of `(y mod 3^{j+d}, s₀)` — agreement mod `3^{j+d}` already forces `d̃ = d` — and not of `y mod 3^{j+d−1}`: two edges of the same `d` whose doors agree to exactly `j + d − 1` digits have top doors differing mod `3^j`, with `v₃(y'_0 − ỹ'_0) = j − 1`. So `j` output digits consume `j + d` input digits, and the map from the `(j+d)`-th digit of `y` to the `j`-th of `y'_0`, lower digits fixed, is a bijection of `Z/3`. The same-`d` hypothesis of the sharpness clause is needed only at `j = 1`, where agreement mod `3^d` does not fix `d` (clause 1).
4. (Side doors.) `v₃(y'_a + 1) = a` exactly, so `y'_a ≡ −1 (mod 3^a)` and `≢ −1 (mod 3^{a+1})`: the low `a` digits are fixed by the door index alone — ladder.md 15.7.6's gained digits, read on the mirror side. For `j > a`, `y'_a mod 3^j` is a function of `(y mod 3^{j−a+d}, s₀)` and not of `y mod 3^{j−a+d−1}` (same `d`; the hypothesis needed only at `j − a = 1`). For `j ≤ a` the residue is `−1`, a function of no digit of `y`.

**Proof.** (1) `v₃(2^{s₀}y + 1) ≥ k` iff `2^{s₀}y ≡ −1 (mod 3^k)`, a condition on `y mod 3^k`; `d` itself is "`≥ d` and not `≥ d + 1`", which needs `d + 1` digits; and `2^{s₀}(y + 2t·3^d) + 1 = 3^d(ω + 2^{s₀+1}t)`, which is `≡ 0 (mod 3^{d+1})` for exactly one `t mod 3`. (2) `2^{s₀}y + 1` and `2^{s₀}ỹ + 1` are both `≡ 0 (mod 3^d)`, so their difference `2^{s₀}(y − ỹ)` is, and `v₃(y − ỹ) ≥ d`; then `ω − ω̃ = 2^{s₀}(y − ỹ)/3^d` has `v₃ = v₃(y − ỹ) − d` (`2^{s₀}` a unit) and `y'_a − ỹ'_a = 2^{d−a}3^a(ω − ω̃)` has `v₃ = v₃(y − ỹ) − d + a`. (3), (4) are (2) at `a = 0` and `a ≥ 1`, with `v₃(y'_a + 1) = v₃(2^{d−a}3^a ω) = a`: agreement mod `3^{j−a+d}` with `j > a` gives `v₃(y − ỹ) ≥ d + 1`, hence `d̃ = d` by (1), hence `v₃(y'_a − ỹ'_a) ≥ j`; agreement to exactly `j − a + d − 1` digits with `d̃ = d` gives exactly `j − 1`. ∎

**What the theorem is.** The child door `y'_a` has stratum `(m, r) = (d − a, s₀)` — `m = v₂(y'_a + 1) = d − a`, and `r` is the exit valuation of its state, the child — and `G(y'_a) = y`, the child's exit. So clause 2 is Theorem 14.14.4.1, `v₃(G(y') − G(z')) = v₃(y' − z') + m` on a fixed stratum, read backward along the door edge with `m = d − a`; nothing new is computed. Its content in comb coordinates: **across a door edge into door `a` of the child, the 3-adic precision budget moves by exactly `−(d − a)` digits** — `d` lost to the exact division by `3^d`, `a` regained from the forced `−1` — and `d − a = m(y'_a)` is the 2-adic entry depth of the door entered, the letter's `m` (14.14.6's `m₊`); no door edge is free, since `a ≤ d − 1`. Along a cascade edge the door is unchanged and no digit of it is consumed: clause 2 holds with any admissible branch `s` in place of `s₀` (same proof, `d = d(y,s)`), so a cascade run only changes which `d` the next door edge is charged. Under the depth ledger (a measured law, 18.7.2) the mean loss at the top door is `E[d] = 3/2` digits per door edge. This is 14.13's per-generation precision loss counted per comb edge, and the count reconciles the record's two figures: at 14.6's designated door (`a = 0` when `d = 1`, `a = d − 1` when `d ≥ 2` — the collapse identity 14.6.1) the loss is exactly one digit at every edge, which is 14.6.5's "one digit of precision loss per generation"; at the top door it is `d`, which is 14.13's "exactly `d` digits". The theorem does not make `M₃` propagate: `M₃(y'_a) mod 3^k` is a function of `y'_a mod 3^{k+1}` (14.7.1) and hence of `y mod 3^{k+1+d−a}`, a function of finitely many digits of the parent door only because the child door itself is one; 14.6.5's affine obstruction stands, with its price written down.

**Boundary cases.** `y = 1`: `s₀ = 1`, `d = 1`, `ω = 1`, the child is the root and `y'_0 = 1` — the excluded self-loop; no door edge of the comb has parent door `1`. `j = 0`: the clauses are vacuous, and `j + d = d` digits do not fix `d` (doors `5` and `11` agree mod `3` with `d = 1` and `d = 2`). The dead top door: `y'_0 ≡ 0 (mod 3)` iff `2^d ω ≡ 1 (mod 3)` (14.5.1); clause 2 does not see liveness — `y'_0` is an integer either way — and at `j = 1` it says that whether the child's top door is dead is a function of `y mod 3^{d+1}` and `s₀`; a dead `y'_0` carries no door edge, so `d − 0` is then the cost of a door that is not taken.

**Verified** — section (c): the top-door law on `5,000` random `(y, s₀, j ≤ 6)` (`y` of up to `60` bits): agreement mod `3^{j+d}` gave `d̃ = d` and equal `y'_0 mod 3^j` in all `5,000`, with clause 2 exact; agreement to exactly `j + d − 1` digits with `d̃ = d` gave unequal `y'_0 mod 3^j` and `v₃(y'_0 − ỹ'_0) = j − 1` in all `4,584` such draws (`416` draws, all at `j = 1`, changed `d` and were filtered, as clause 1 predicts); `2,464` child top doors dead, each by 14.5.1's criterion; at every edge a lift agreeing mod `3^d` with a larger `d`; the designated door's loss exactly one digit. The side-door law on `3,000` random edges with `d ≥ 2` (largest `d = 10`), every `a < d`, `j = a + 1, …, a + 5`: `v₃(y'_a + 1) = a`, the stratum `(d − a, s₀)` and `G(y'_a) = y`, agreement at `j − a + d` digits and disagreement at one fewer (`34,198` sharp pairs), clause 2 at every pair, and `y'_a ≡ −1 (mod 3^j)` for `j ≤ a` against an unrelated edge; clause 2 with `d(y,s)` at `2,000` edges at branches `s ≤ 30`; the two hand-checked edges (parent doors `5` and `13`) and the boundary cases as canaries. Whole script: `8,034,120` checks, `0` failures; single reproducing command `python experiments/comb_dictionary.py`, `10 s`.

**Standing of 18.7.** Grade: formulation, plus one law (18.7.3) that is 14.14.4.1 in comb coordinates. Nothing is proposed; no front moves. What the section settles is the author's question: determinism along `η` and `λ` is determinism of the itinerary word, the doors need no alphabet of their own, and the one place the comb's two determinacies meet has an exact price — `d − a` ternary digits per door edge, none per cascade edge.
