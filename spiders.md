---
status: FORMULATION — the first abstraction layer above reduced states: the classification of comb nodes by depth and residue (abdomens, forks, links), the hair chains, the partition of the comb into spiders, the hair-length law, the spider tree with its census, and the coordinates of a spider; no front moves
scope: new section 19
updated: 2026-09-26
source: the author's direction of 2026-09-22 (build the next deterministic abstraction up from reduced states, one layer at a time) and question of 2026-09-26; briefs/spider-layer-brief.md, briefs/spider-coordinates-brief.md
---

> **Current state.** Every comb node (comb.md §18) is classified by its depth `D` and, at depth `1`, its residue `Ω mod 3`: an **abdomen** (`D ≥ 2`), a **fork** (`D = 1`, `Ω ≡ 1 mod 3`), or a **link** (`D = 1`, `Ω ≡ 2 mod 3`); the root `(1,1)` is a fork by residue but is its own piece (19.1). A link has exactly one child, always a fork of depth `1`; a fork has exactly two children, a cascade abdomen and a top-door child whose depth is `1` iff `Ω ≢ 7 mod 9`, in which case its own class is exact by `Ω mod 9` — so a depth-`1` node has at most one depth-`1` child, and the depth-`1` material above an abdomen is a set of simple chains, the **hairs** (19.1, 19.2). Which depth-`1` nodes are *not* legs (direct children of an abdomen) is settled completely: the residue table by `(Ω mod 3, Ω mod 8)`, (Lemma 19.1.5). The comb partitions exactly into **spiders** (an abdomen plus its hairs) and the root's own piece; over the comb to level `18`, `247,932` nodes fall into `82,491` pieces, mean size `3.006`, largest `40` (19.2). The hair-length law is a two-state Markov chain forced by Items A.1–A.2; matched to the *true* (level-boundary-corrected) length distribution to within `2%` at every one of the first eight lengths — the level-`18` census window itself truncates `71.5%` of hairs, an artifact identified and corrected, not a property of the law (19.2). The spider tree (spiders as nodes) is proved a tree with a census by level, a sufficient digit budget for a whole spider's shape, and a negative answer, with a reason, to whether the child-spider count is a bounded-residue function of the abdomen's core (19.3). The layer is a residue-based coarse-graining of the comb by depth and by `Ω mod 24` and `mod 9`, sitting inside 18.9's own horizon; nothing here moves any front (19.4). A spider has exact coordinates in one direction: its legs are the doors `b = 1, …, D−1` of `(Ω, D+1)`, with its door `0` or the top leg `y_0(Ω, D+1)/3` by `t = v₃(2^{D+1}Ω − 1) ∈ {0, 1}`, and every member is a closed formula in the abdomen `(Ω, D)` and a position `(b, w)` — the leg's door index and the hair word — with a lens identity that reads `Ω`, `D` and `b` back off the member by valuations, as `(ω, d)` is read off `x + 1`. In the other direction, reading the position off a member is walking the hair descent, which is the member's own Collatz orbit in two-halving steps and sibling moves; a search for a walk-free identifier closed negative in the forms tested — the position is a `2`-adic residue whose modulus grows as `2^{2j+3}·3` with the position `j`, and the owner's depth is decided by no bounded residue at all (19.5).

# 19. The spider layer

Every rule in this section is sign-blind, exactly as in 18.8: no algebraic step below reads the sign of `Ω`. Only the positive comb is worked out; the record does not repeat the construction on the three negative components.

## 19.1. The classification of nodes

**Definition 19.1.1 (the classification).** For a comb node `(Ω, D)`:

- an **abdomen** if `D ≥ 2`;
- a **fork** if `D = 1` and `Ω ≡ 1 (mod 3)`;
- a **link** if `D = 1` and `Ω ≡ 2 (mod 3)`.

The root `(1,1)` is a fork by this residue rule, but is treated as its own piece throughout (19.2): its only child is the abdomen `(1,2)` (comb.md 18.2.3).

**Lemma 19.1.2 (a link's one child).** A link `(Ω, 1)` has exactly one child: its cascade child `(4Ω − 1, 1)`, of depth `1`, which is always a fork; its top door is dead.

**Proof.** The top door of `(Ω,1)` is `y₀ = 2Ω − 1`; it is dead iff `2Ω ≡ 1 (mod 3)` (comb.md 18.2.3/reverse.md 14.5.1), and `2Ω ≡ 2·2 ≡ 1 (mod 3)` since `Ω ≡ 2`. With `D = 1` there is no side door (`a` ranges over `∅`), so the cascade child is the only child. By comb.md 18.9.1's cascade-child law at `D = 1`, its depth is `1 + v₃(4Ω − 1)`; and `4Ω − 1 ≡ Ω − 1 ≡ 2 − 1 ≡ 1 (mod 3)` (using `4 ≡ 1 mod 3`), so `v₃(4Ω − 1) = 0` and the depth is exactly `1`. Its core `4Ω − 1` is itself `≡ 1 (mod 3)`, a fork. ∎

**Lemma 19.1.3 (a fork's two children, and the exact class split at `t = 1`).** A fork `(Ω, 1)` has exactly two children: a cascade child of depth `t + 1 ≥ 2` (an abdomen) and a top-door child of depth `t`, where `t = v₃(4Ω − 1) ≥ 1`; both children share the same core, `(4Ω − 1)/3ᵗ`. The top-door child has depth `1` iff `t = 1` iff `Ω ≢ 7 (mod 9)`, and then its class is exact: a **fork** iff `Ω ≡ 1 (mod 9)`, a **link** iff `Ω ≡ 4 (mod 9)`.

**Proof.** The top door is `y₀ = 2Ω − 1 ≡ 2 − 1 ≡ 1 (mod 3)` (`Ω ≡ 1`), hence alive (`2·1 ≢ 1 mod 3`... concretely `2Ω ≡ 2 ≢ 1 mod 3`) and at the lowest branch `s₀ = 1` (`y₀ ≡ 1 mod 3`). By comb.md 18.9.1 at `D = 1`: the cascade child has depth `1 + v₃(4Ω − 1) = t + 1`, and the top-door child's numerator is `2y₀ + 1 = 4Ω − 1`, the same integer, so its depth is `v₃(4Ω − 1) = t` and its core is `(4Ω − 1)/3ᵗ` — the same core as the cascade child's, reached by one fewer factor of `3` removed. Since `Ω ≡ 1 (mod 3)`, `4Ω − 1 ≡ 0 (mod 3)`, so `t ≥ 1` always; writing `Ω mod 9 ∈ {1, 4, 7}`: `4·1 − 1 = 3` (`v₃ = 1`), `4·4 − 1 = 15` (`v₃ = 1`), `4·7 − 1 = 27` (`v₃ = 3 ≥ 2`) — so `t = 1` iff `Ω ≡ 1` or `4 (mod 9)`, i.e. iff `Ω ≢ 7 (mod 9)`. When `t = 1` the core is `(4Ω − 1)/3`: at `Ω ≡ 1 (mod 9)` this is `1` (mod 3, from `3/3 = 1`, and in general `(4Ω−1)/3 mod 3` is fixed by `Ω mod 9`, exact); at `Ω ≡ 4 (mod 9)` it is `5/3 = ` … concretely for `Ω = 4`: `(16−1)/3 = 5 ≡ 2 (mod 3)`, a link; for `Ω = 1`: `(4−1)/3 = 1 ≡ 1 (mod 3)`, a fork. Since the map `Ω ↦ (4Ω−1)/3 mod 3` is an affine function of `Ω mod 9` on each of the two admissible residues, it is constant on each: `Ω ≡ 1 (mod 9)` always gives a fork, `Ω ≡ 4 (mod 9)` always gives a link. ∎

**Corollary 19.1.4 (at most one depth-`1` child).** A depth-`1` node has at most one depth-`1` child: a link has exactly one (forced, Lemma 19.1.2); a fork has one iff `t = 1`, else none (Lemma 19.1.3). Consequently the depth-`1` material lying above an abdomen is a union of simple chains — the hairs of 19.2 — never a bush.

**Lemma 19.1.5 (the complete parent-is-abdomen table).** For a depth-`1` node `(Ω, 1)`, whether its comb parent is an abdomen is a function of `(Ω mod 3, Ω mod 8)`, given by:

```text
                Omega mod 8 = 1   3          5      7
fork (Ω=1 mod3):    orphan      orphan     abdomen  abdomen
link (Ω=2 mod3):    orphan      abdomen    abdomen  abdomen
```

Equivalently, by CRT to modulus `24`: the **non-legs** (a depth-`1` node whose parent is *not* an abdomen) are exactly `Ω ≡ 1, 17, 19 (mod 24)` — `Ω ≡ 17 (mod 24)` for links (the **orphan links**, pre-checked in the brief) and `Ω ≡ 1` or `19 (mod 24)` for forks, called **hair forks** (19.2 explains the naming); every other residue mod `24` is a leg (a depth-`1` child of an abdomen).

**Proof.** Write the node's peak `A = 3Ω − 1 = 2ˢy`. The 2-adic case split on `Ω` is standard: `s = 1` iff `3Ω ≡ 3 (mod 4)` iff `Ω ≡ 1 (mod 4)`; for `Ω ≡ 3 (mod 4)`, writing `Ω = 4k+3`, `3Ω − 1 = 4(3k+2)`, and `3k+2` is odd iff `k` is odd iff `Ω ≡ 7 (mod 8)` (giving `s = 2`) and even iff `Ω ≡ 3 (mod 8)` (giving `s ≥ 3`).

*Case `s = 1` (`Ω ≡ 1 mod 4`, i.e. `Ω mod 8 ∈ {1,5}`).* The parent is the door parent `state(y)`, `y = (3Ω−1)/2`, so `y + 1 = (3Ω+1)/2`. Since `3Ω + 1 ≡ 1 (mod 3)` unconditionally (`3Ω ≡ 0`), and dividing by the unit `2` preserves nonvanishing mod `3`, `(3Ω+1)/2 ≢ 0 (mod 3)` always — the parent's depth carries **no** factor of `3`, so `D' = v₂((3Ω+1)/2)` exactly. Concretely `D' = 1` iff `(3Ω+1)/2 ≡ 2 (mod 4)` iff `3Ω + 1 ≡ 4 (mod 8)` iff `Ω ≡ 1 (mod 8)` (using `3⁻¹ ≡ 3 mod 8`); else `D' ≥ 2`. This computation used only `Ω mod 8`, independent of `Ω mod 3` — both fork and link give the same split.

*Case `s = 2` (`Ω ≡ 7 mod 8`).* The parent is `state(y)`, `y = (3Ω−1)/4`, odd (since `Ω ≡ 7 mod 8` forces `(3Ω−1)/4` odd), so `y + 1` is even (`m ≥ 1`); and `y + 1 = (3Ω+3)/4 = 3(Ω+1)/4`, carrying a forced factor of `3` (`a ≥ 1`) independent of `Ω mod 3`. Hence `D' = m + a ≥ 2` always: **abdomen**, regardless of class.

*Case `s ≥ 3` (`Ω ≡ 3 mod 8`).* The parent is the cascade parent, at branch `s − 2` on the same door; by the inverse of the `4A − 3` identity (comb.md 18.2.5/reverse.md 14.10.1), its numerator is `(N + 3)/4` where `N = 3Ω` (the branch-`s` numerator), i.e. `3(Ω+1)/4`. So `D' = 1 + v₃((Ω+1)/4) = 1 + v₃(Ω + 1)` (`4` a unit mod `3`). For a fork (`Ω ≡ 1 mod 3`): `Ω + 1 ≡ 2 (mod 3)`, `v₃(Ω+1) = 0`, `D' = 1` — a non-leg (**orphan**). For a link (`Ω ≡ 2 mod 3`): `Ω + 1 ≡ 0 (mod 3)`, `v₃(Ω+1) ≥ 1`, `D' ≥ 2` — **abdomen**.

Collecting the three cases into the table, and taking CRT with `Ω mod 3` to modulus `24`, gives the stated residues; each of the `8` valid classes mod `24` (`Ω` odd, `3 ∤ Ω`) was checked non-empty. ∎

**Lemma 19.1.6 (the abdomen leg count).** An abdomen `(Ω, D)` has

```text
legs = (D − 1) + [3 ∤ 2^{D+1}Ω − 1] + [top door alive and its child of depth 1]
```

legs: the cascade child (core `4·3^{D−1}Ω − 1`, always a **link**), the children through doors `a = 2, …, D−1` (cores `2^{D−a+2}3^{a−1}Ω − 1`, always **links**), the door-`a = 1` child when its depth is `1` (core `2^{D+1}Ω − 1`, always a **fork** when it is a leg), and the top-door child when its depth is `1` (class not forced).

**Proof.** The cascade child of an abdomen has depth `1` always (comb.md 18.9.1 at `D ≥ 2`), so it is a leg unconditionally; its core `4·3^{D−1}Ω − 1 ≡ −1 ≡ 2 (mod 3)` since `D − 1 ≥ 1` forces the leading term `≡ 0 (mod 3)` — always a link. For `a ≥ 2`, comb.md 18.9.1's proof gives the child's numerator bracket `2^{D−a+2}3^{a−1}Ω − 1`, and `a − 1 ≥ 1` again forces the leading term `≡ 0 (mod 3)`, so the bracket `≡ −1 ≡ 2 (mod 3)` — depth `1` and a link, always, for every `a ≥ 2` (there are `D − 2` such doors, giving the `D − 1` count together with the cascade leg). For `a = 1`, the bracket `2^{D+1}Ω − 1` carries no forced factor of `3`: it is a leg iff `2^{D+1}Ω ≢ 1 (mod 3)`, i.e. (since `2^{D+1}Ω` is a unit mod `3`, hence `≡ 1` or `2`) iff `2^{D+1}Ω ≡ 2 (mod 3)` — and then the bracket itself is `≡ 2 − 1 ≡ 1 (mod 3)`, a fork, forced by the same triviality that decides leg-hood. The top door's numerator always carries at least one forced factor of `3` (it is chosen at the admissible branch `s₀`), so no such triviality applies to its quotient; the class is not forced and both occur (the fork's own top-door child of Lemma 19.1.3 is the `D = 1` instance of exactly this indeterminacy). ∎

Lemma 19.5.1 reads the same count as `D − 1 + [t ≤ 1]`, `t = v₃(2^{D+1}Ω − 1)`: the legs are the doors `b = 1, …, D−1` of `(Ω, D+1)`, together with its door `0` when `t = 0` or `y_0(Ω, D+1)/3` when `t = 1`.

**Verified** — `experiments/spider_layer.py`, Part A, fresh code (imports nothing from any other script), seed `20260922`, 2026-09-22: canaries `(17,1)` with parent `(13,1)` and child `(67,1)`, `(13,1)` with children `(17,2)` and `(17,1)`, `(7,1)` with children `(1,4)` and `(1,3)`, `(1,2)` abdomen; Lemma 19.1.2 on `1,973` random links (`0` failures); Lemma 19.1.3 on `1,997` random forks, including the exact `Ω mod 9` class split (`0` failures at either residue); Corollary 19.1.4 on the same samples; Lemma 19.1.5's table on `2,973` random depth-`1` states spanning every one of the `8` cells of `(Ω mod 3, Ω mod 8)`, and the CRT residues `{1,17,19} mod 24` confirmed against the table (`0` failures); Lemma 19.1.6 on `3,000` random abdomens (`D` from `2` to `14`), with the forced-class claims checked at every leg (`0` failures). `57,290` checks, `0` failures.

## 19.2. Hairs, spiders and the partition

**Definition 19.2.1 (hair, spider).** A **hair** is a maximal chain of depth-`1` nodes `h₁ → h₂ → … → h_L` (each the unique depth-`1` child of the previous, Corollary 19.1.4), whose first node `h₁` is a **leg** — a depth-`1` child of an abdomen. (The alternative clause of "or the child of the root" is vacuous on the positive comb: the root's only child is the abdomen `(1,2)`, never depth-`1`.) The **spider** of an abdomen is the abdomen together with every hair whose first node is one of its legs. The **root's piece** is `{(1,1)}` alone.

A hair node past `h₁` is called an **orphan link** if it is a link (Lemma 19.1.5's "forced class" facts show a link is *never* preceded by a link — its only child is always a fork, Lemma 19.1.2 — so every non-leg link is exactly the class Lemma 19.1.5 calls the orphan; this is the naming used by the explorer's class badge, comb_explorer.html), and a **hair fork** if it is a fork. The symmetric class "a link preceded by a link" is therefore provably empty; `experiments/spider_layer.py` and `experiments/comb_explorer_check.py` both confirm `0` occurrences.

**Theorem 19.2.2 (the partition).** Every comb node belongs to exactly one spider or to the root's piece: a node's **owner** is the first abdomen (or the root) met by ascending through comb parents while the class stays depth-`1`.

**Proof.** By Corollary 19.1.4, ascending from any depth-`1` node through comb parents while the class remains depth-`1` is a simple chain (no branching), and it is finite: level strictly decreases along a comb parent edge (comb.md 18.2.1), so the ascent terminates, and it terminates only at a node whose parent is *not* depth-`1` — an abdomen, or the root (whose only child `(1,2)` is itself an abdomen, so the root is never reached by ascending from a depth-`1` descendant; it owns only itself). Every node is therefore assigned exactly one owner: an abdomen (itself, if it is one), the root (itself alone), or the abdomen found by ascending. This partitions the node set into the root's singleton piece and, for each abdomen, the piece `{owner⁻¹(abdomen)}` — the abdomen plus every hair whose first node's owner it is, i.e. every hair whose first node is one of its legs. ∎

**Census** — `experiments/spider_layer.py`, Part B, over the comb to level `18` (cumulative, `247,932` nodes, built fresh from `(1,1)`): `82,491` pieces, mean size `3.006`, largest `40` — matching comb.md's own pre-check exactly. Class tally: `82,490` abdomens (plus the root), `96,620` legs, `55,117` hair forks, `13,704` orphan links, `0` hair links.

**The hair-length law.** The continuation rule, per class, follows directly from Lemmas 19.1.2–19.1.3: a link **always** continues, to a fork (probability `1`, not a measured rate); a fork continues iff `t = 1`, which the depth ledger `P(t = j) = 2·3^{−j}` (comb.md 18.9.1, a measured law wherever it is used, per reverse.md 14.2.4's own posture) gives probability `2/3`, and when it continues the next class is a fork with probability `1/2` and a link with probability `1/2` — exact by residue (`Ω ≡ 1` vs `4 mod 9`, Lemma 19.1.3), not merely the near-even split the raw census happens to show. This is a two-state Markov chain (states link `L`, fork `F`): `L → F` always; `F → F`, `F → L`, `F →` end each with probability `1/3` (from `2/3 · 1/2` twice, plus `1/3` for `t ≥ 2`).

Writing `f(n | L)`, `f(n | F)` for the probability that the hair from a node of the given class has exactly `n` more nodes (itself included):

```text
f(1|F) = 1/3,           f(1|L) = 0,
f(n|F) = (1/3)f(n−1|F) + (1/3)f(n−1|L)   (n ≥ 2),
f(n|L) = f(n−1|F)                          (n ≥ 2).
```

Given the measured leg-type mix (fork legs `27,542`, `28.51%`; link legs `69,078`, `71.49%`, over the level-`18` census), the predicted length distribution is `P(n) = p_F·f(n|F) + p_L·f(n|L)`.

**The level-`18` census window is not the law.** Measured directly within the window, the length distribution (`53,145` at length `1`, `28,290` at `2`, `8,818` at `3`, …) disagrees badly with the prediction — e.g. `55.0%` of hairs measured length `1` against a predicted `9.5%`. The discrepancy is a boundary artifact, not a failure of the law: a hair node discovered exactly at level `18` has no census-recorded child, so a chain that reaches the boundary is cut off there whether or not it truly continues — and by Lemma 19.1.2 a link **always** continues, so every link leg sitting exactly at level `18` (`34,743` of the `69,078` link legs) is wrongly recorded as a length-`1` hair. Recomputing every hair's length by ground-truth arithmetic alone (`comb_children`, unbounded, independent of the census) rather than by the census neighbour list shows `69,099` of the `96,620` hairs (`71.5%`) are affected. The **true** distribution matches the predicted one closely at every tested length:

```text
 len   predicted   measured (true)   ratio
   1    0.09502     0.09514          1.0012
   2    0.26999     0.27006          1.0003
   3    0.12167     0.12083          0.9931
   4    0.13055     0.12914          0.9891
   5    0.08407     0.08410          1.0003
   6    0.07154     0.07128          0.9963
   7    0.05187     0.05253          1.0126
   8    0.04114     0.04190          1.0184
```

The true maximum hair length observed in this census is `55` (against `15` within the truncated window). The census-window figures are shown so that the truncation is visible; the boundary-corrected figures are the ones that test the law.

**Spider size.** The fraction of abdomens among nodes is `1 − P(D = 1) = 1/3` under the depth ledger, so the mean spider size is `3` given the ledger, a measured law (comb.md 18.7.2's own posture); the census's `3.006` is the calibration.

**Verified** — `experiments/spider_layer.py`, Part B: the partition theorem checked exactly on the full level-`18` census (every node in exactly one piece, `0` failures); the root's piece `= {(1,1)}`; every non-root piece owned by an abdomen with every other member depth-`1`; the continuation rule re-verified at the census level by ground-truth arithmetic, not the (truncated) census neighbour list (`82,782` link occurrences across every hair, all `82,782` continuing, `0` failures); the boundary-truncation count (`69,099/96,620`) and the true hair-length distribution computed and compared to the predicted law as above. `247,945` checks, `0` failures.

## 19.3. The spider tree

**Definition 19.3.1 (the spider tree).** The nodes of the **spider tree** are the spiders and the root's piece; the parent of a spider is the owner (Theorem 19.2.2) of its abdomen's own comb parent. A spider's children are spawned by: the abdomen's own deeper children (its door-`a = 1` child when it is *not* a leg, i.e. `3 | 2^{D+1}Ω − 1`; its top-door child when its depth is `≥ 2`), and by each fork in its hairs — the fork's cascade child, always an abdomen (Lemma 19.1.3), and the fork's top-door child when `t ≥ 2` (then it is itself an abdomen, depth `t`, not a continuation of the hair). Links spawn nothing.

**Proposition 19.3.2.** The spider tree is a tree rooted at the root's piece, and its edges are exactly the comb's own edges from a node of one spider to an abdomen outside it.

**Proof.** By construction, a spider's children are exactly the abdomens reached by a single comb edge from some node of the spider (every such edge either stays within the spider — a link's forced continuation, or a fork's `t = 1` continuation, both landing on a depth-`1` node with the same owner by Theorem 19.2.2 — or lands on an abdomen, which starts a new spider owned by itself); this is checked directly against comb.md's own children rule in the verification below. The spider-parent map strictly decreases comb level (every comb edge does, comb.md 18.2.1), so no cycle is possible and every spider's parent-chain is finite; since the root's piece is the unique piece with no parent (the root's own comb parent does not exist, and no other piece's abdomen has the root as its comb parent, since the root's only child `(1,2)` is not the root), every chain terminates there. ∎

**Census** (over the level-`18` positive comb, `82,491` pieces): per spider level (comb edges of the spider tree to the root's piece),

```text
 slvl  spiders   mean size  mean legs  mean child-spiders
   0        1      1.000      0.000       1.000
   1        1      4.000      2.000       4.000
   2        4     16.750      3.000      12.500
   3       50     10.060      2.140       8.000
   4      400      8.580      2.232       5.895
   5     2358      6.232      1.982       3.601
   6     8490      4.593      1.698       2.135
   7    18128      3.494      1.425       1.241
   8    22496      2.730      1.118       0.762
```

overall (all `82,491` pieces): mean size `3.006`, mean legs (= hairs) per spider `1.171`, mean child spiders `1.000` (every non-root piece has exactly one spider-tree parent edge, so the mean child count over the whole finite tree is `(82,491 − 1)/82,491 ≈ 1`, an identity of a finite rooted tree, not a law). Levels past about `7`–`8` show a visible level-`18` census-boundary effect (the mean child-spider count declining toward `0` as the level rises, since spiders near the boundary have systematically fewer of their true children recorded) — the same kind of finite-window artifact identified for hair lengths above, reported flat and not corrected further here (the correction used for hair lengths does not extend cheaply to whole subtrees).

**The residue-modulus measurement.** Following comb.md 18.9.2.2–18.9.3's own method — a sufficient digit budget composed edge by edge, with cap `J = 2` (the abdomen/depth-`1` boundary, the only depth distinction a spider's shape needs) — a **sufficient** modulus `3^M` fixing a whole spider's shape (every hair's length and class sequence, and the fact that every deeper edge reaches an abdomen, not that abdomen's own core) was computed for `2,500` sampled spiders: mean `4.97`, max `26`; the mean does not show a strong trend against spider size over the sampled range (sizes `1`–`12`), since most sampled spiders are short and the budget is dominated by the base cap plus one or two hair steps. On the `120` sampled spiders with sufficient budget `≤ 8`, the **exact** modulus (found by full-coset search, as in 18.9.3) equals the sufficient one in every case — `0` slack, on the tested range.

**The child-spider question, answered.** Is the number of child spiders of a spider an exact function of `(D, Ω mod 3^k)` for a `k` independent of the spider's size? **No**, over the census to level `18`: grouping spiders by the coarse class `(D, Ω mod 9)` and restricting to classes with `≥ 5` members, every one of `45` such classes (all of them) contains spiders with more than one distinct child-spider count — e.g. the class `(D = 2, Ω mod 9 = 1)` contains spiders with `0`, `2`, and `4` child spiders. The child-spider count correlates with spider size (Pearson `r = 0.82` over all `82,490` non-root pieces), and the reason is structural, not a naming: the count is `Σ (1 + [t ≥ 2])` over every fork in the spider's hairs (each fork always contributes its cascade child; it contributes a second, its top-door child, exactly when it ends the hair), so it grows with the number of forks in the spider — which grows with the spider's hair lengths, and hair lengths are unbounded (19.2). A larger `k` shrinks the class but never bounds the count uniformly, for the same reason 18.9.2's digit budget for a signature grows with the depth asked of it: a hair of length `L` needs on the order of `L` further ternary digits to resolve (each fork step costs one digit, each link step costs none, in exactly comb.md 18.9.2.2's cost accounting), so no finite `k` suffices for every spider.

**Verified** — `experiments/spider_layer.py`, Part C: the canary spider of `(1,2)` — legs `(11,1)` (a link) and `(7,1)` (a fork); hair `(11,1) → (43,1)` (`t = v₃(4·43−1) = 2`, ending it) and hair `(7,1)` alone (`t = v₃(4·7−1) = 3`, ending immediately) — spider `{(1,2), (11,1), (43,1), (7,1)}`, size `4`, matching the brief's pre-check; **four** child spiders, `(19,3)` and `(19,2)` from `(43,1)`'s cascade and top-door children, `(1,4)` and `(1,3)` from `(7,1)`'s (a fork that ends its hair spawns two new spiders at once, from its cascade *and* top-door children, not one — the point a first hand derivation missed and the code caught); the spider tree's edges checked against a direct scan of every comb edge out of every piece, on all `82,491` pieces (`0` failures); acyclicity and root-reachability of every spider-parent chain, on all `82,491` pieces; the census table; the sufficient-budget measurement on `2,500` sampled spiders and the exact-modulus search on `120` of them; the child-spider-count evidence (the `45`-class survey and the correlation). `830,703` checks (cumulative from Parts A–C), `0` failures. Whole script: `1,135,938` checks, `0` failures, wall clock `4.8` s; single reproducing command `python experiments/spider_layer.py`.

## 19.4. Standing

What the layer is: a residue-based coarse-graining of the comb by depth (`D ≥ 2` vs `= 1`) and, within depth `1`, by `Ω mod 3` (fork vs link), `Ω mod 8` (whether the parent is an abdomen), and `Ω mod 9` (a fork's continuation class) — sitting entirely inside 18.9's own horizon: a spider's shape is a signature in that section's sense, and the digit budget that fixes it (19.3) is 18.9.2's own cost composition applied along a hair. What it is not: no front moves, nothing about which states the comb reaches is touched, and no cycle is searched. The author's north star — that the layers built this way may eventually be raised until the whole map is one object — is recorded here as the stated direction of the work, not as a claim: nothing beyond the construction, the partition, the hair-length law and the spider tree's census is asserted in this section. Grade: **formulation plus measurements**. A single spider can be walked node by node, with the rule cited at every step, in `viz/spider_explorer.html`. Coordinates for a spider's members — each member as a closed formula in its abdomen and a position, and a search for an identifier that needs no walk — are 19.5.

## 19.5. The coordinates of a spider

The author's question of 2026-09-26: is there a common identifier for the members of a spider, in the way `ω` and `d` identify and fully describe a reduced state? A reduced state does two things for an odd integer `x`. It is read off `x` by two valuations, with no iteration (`x + 1 = 2^m 3^a ω`, `d = m + a`); and it lists all `d` odd integers it stands for by one closed formula (`y_a = 2^{d−a}3^aω − 1`, `0 ≤ a < d`; spine.md §3.2–3.7, reverse.md 14.6.5.1). The question splits the same way for a spider: (i) from the abdomen `(Ω, D)`, is every member a closed formula in `(Ω, D)` and a position? (ii) from a member, can `(Ω, D)` be read off without the walk to the abdomen? 19.5.1–19.5.3 answer (i) yes, exactly; 19.5.2 and 19.5.5 answer (ii) no in the forms searched, with the reason. Everything is framed by doors, branches and digits; nothing here is new dynamics.

Throughout, for an abdomen `(Ω, D)`, `y_b(Ω, D+1) = 2^{D+1−b}3^bΩ − 1` (`0 ≤ b ≤ D`) are the doors of the state one depth up on the same core, and `t = v₃(2^{D+1}Ω − 1) = v₃(y_0(Ω, D+1))` — at `D = 1` this is Lemma 19.1.3's `t = v₃(4Ω − 1)`.

### 19.5.1. The legs are the doors of `(Ω, D+1)`

**Lemma 19.5.1 (legs and doors).** Let `(Ω, D)` be a comb node, `D ≥ 1`.

- (a) Its **lower children** — the door-`a` children for `a = 1, …, D−1` and the cascade child — have numerators `3·y_b(Ω, D+1)` for `b = 0, …, D−1`, each value once: the door-`a` child has numerator `4y_a(Ω,D) + 1 = 3·y_{a−1}(Ω, D+1)`, and the cascade child `4A + 1 = 4·3^DΩ − 3 = 3·y_{D−1}(Ω, D+1)`. The lower child through `b` has depth `1 + v₃(y_b(Ω, D+1))` and core `y_b(Ω, D+1)/3^{v₃(y_b(Ω,D+1))}`. At `D = 1` the only lower child is the cascade child, numerator `3·y_0(Ω, 2) = 3(4Ω − 1)`.
- (b) The top door `y_0(Ω, D)` is alive iff `t ≥ 1`; when alive it is `≡ 1 (mod 3)`, its branch is `s₀ = 1`, and its child's numerator is `2y_0(Ω, D) + 1 = y_0(Ω, D+1)`. So the lower child through `b = 0` and the top-door child share the core `y_0(Ω, D+1)/3^t`, at depths `t + 1` and `t` — Lemma 19.1.3's shared core, now at every `D ≥ 1` (at `D = 1` the lower child through `b = 0` is the cascade child).
- (c) For an abdomen (`D ≥ 2`) the legs are exactly: `(y_b(Ω, D+1), 1)` for `b = 1, …, D−1`, each a link; `(y_0(Ω, D+1), 1)` when `t = 0`, a fork; `(y_0(Ω, D+1)/3, 1)` when `t = 1`, of either class. The leg count is `D − 1 + [t ≤ 1]`, Lemma 19.1.6's count in one bracket. A leg of the first two kinds — a **lower leg**, with **leg index** `b` — has core `x_0 = y_b(Ω, D+1)`, so `x_0 + 1 = 2^{D+1−b}3^bΩ`: read as an odd integer, the lower leg's core is the door `b` of `(Ω, D+1)`, and `state(x_0) = (Ω, D+1)`. The third kind — the **top leg** (leg index `0`, marked top) — has `3x_0 + 1 = 2^{D+1}Ω`.

**Proof.** (a) For `a ≥ 1`, `y_a(Ω,D) + 1 = 2^{D−a}3^aΩ ≡ 0 (mod 3)`, so `y_a ≡ 2 (mod 3)` and the door child sits at branch `2` (Lemma 18.1.2(iii)), with numerator `4y_a + 1 = 2^{D−a+2}3^aΩ − 3 = 3(2^{D+1−(a−1)}3^{a−1}Ω − 1) = 3·y_{a−1}(Ω, D+1)`. The cascade child sits at branch `s + 2` on the node's own door (Proposition 18.2.3), with numerator `2^{s+2}y + 1 = 4A + 1 = 4·3^DΩ − 3 = 3(2^2·3^{D−1}Ω − 1) = 3·y_{D−1}(Ω, D+1)`. A child's depth is the `v₃` of its numerator and its core the cofactor (reverse.md 14.1.1). (b) `y_0 = 2^DΩ − 1 ≡ 2 (mod 3)` would need `3 | 2^DΩ`; so `y_0` is dead (`≡ 0`) or `≡ 1 (mod 3)`, and it is alive iff `2^DΩ ≡ 2 (mod 3)` iff `2^{D+1}Ω ≡ 1 (mod 3)` iff `t ≥ 1`. At `y_0 ≡ 1` the lowest admissible branch is `1` (18.1.2(iii)), numerator `2y_0 + 1 = 2^{D+1}Ω − 1 = y_0(Ω, D+1)`: depth `t`, core `y_0(Ω, D+1)/3^t`; by (a) the lower child through `b = 0` has numerator `3·y_0(Ω, D+1)`, depth `t + 1` and the same core. (c) For `b ≥ 1`, `y_b(Ω, D+1) + 1 ≡ 0 (mod 3)`, so `v₃(y_b(Ω, D+1)) = 0`: depth `1`, core `≡ 2 (mod 3)`, a link. For `b = 0` the lower child has depth `t + 1`, a leg iff `t = 0`, and then `2^{D+1}Ω ≡ 2 (mod 3)` makes the core `≡ 1`, a fork; the top-door child has depth `t`, a leg iff `t = 1`, core `y_0(Ω, D+1)/3`, whose class nothing forces. So exactly one of the two is a leg when `t ≤ 1` and neither when `t ≥ 2`; 19.1.6's two brackets are `[t = 0]` and `[t = 1]`. The state of `x_0 = y_b(Ω, D+1)` is door recovery (14.6.5.1) on `x_0 + 1 = 2^{D+1−b}3^bΩ`, `D + 1 − b ≥ 2`; the top leg has `3x_0 + 1 = y_0(Ω, D+1) + 1`. ∎

So the legs of `(Ω, D)`, apart from a top leg, are representatives of `(Ω, D+1)` — the same core one depth up: the doors `b ≥ 1` always, the door `b = 0` iff `t = 0`; at `t = 1` its place is taken by `y_0(Ω, D+1)/3`, and at `t ≥ 2` by nothing.

**Worked instances.** `(1,2)`: `t = v₃(7) = 0`, legs `(11,1) = (y_1(1,3), 1)` and `(7,1) = (y_0(1,3), 1)` — 19.3's canary spider. `(5,2)`: `t = v₃(39) = 1`, legs `(59,1) = (y_1(5,3), 1)` and `(13,1) = (y_0(5,3)/3, 1)`; the door-`1` child `(13,2)` and the top-door child `(13,1)` share the core `13`.

**Verified** — `experiments/spider_coordinates.py`, Parts 0 and A, fresh code (imports nothing from any other script), seed `20260926`, 2026-09-26: the canaries above; (a)–(c) on `3,000` random abdomens (`Ω < 10^6`, `2 ≤ D ≤ 14`; `t = 0 / 1 / ≥ 2` at `1,487 / 1,031 / 482`) and on every one of the `82,490` abdomens of the level-`18` census, the children computed by the comb's children rule and each sent back through the parent rule, the leg set and count against 19.1.6's formula; (a) at `D = 1` on `2,000` random depth-`1` nodes. `1,046,447` checks, `0` failures.

### 19.5.2. The hair descent map

**Lemma 19.5.2 (the descent).** Let `(x, 1) ≠ (1,1)` be a depth-`1` node. Its comb parent has depth `1` iff `x ≡ 1, 17` or `19 (mod 24)`, and then it is `(desc(x), 1)` with

```text
desc(x) = (3x + 1)/4   if x ≡ 1 (mod 8)    (door parent at s = 1; x ≡ 1 or 17 mod 24)
desc(x) = (x + 1)/4    if x ≡ 3 (mod 8)    (cascade parent at s ≥ 3; x ≡ 19 mod 24)
```

(every other residue gives an abdomen parent, Lemma 19.1.5). Hence a depth-`1` node's **hair position** `j` — the number of `desc`-steps to its leg — and its owner (Theorem 19.2.2) are found by iterating `desc` while `x mod 24 ∈ {1, 17, 19}`: the last node `x_0` is a leg, and the owner is its comb parent. The iteration terminates (`desc(x) < x` for `x > 1`) and never reaches the root: `desc(x) = 1` only at `x = 1`, the root's excluded self-loop (`(x+1)/4 = 1` would need `x = 3`, not a core).

In **raw coordinates** — a depth-`1` node's single representative `n = 2x − 1`, its top door; the depth-`1` odd integers are exactly those with `n ≡ 1 (mod 4)` and `3 ∤ (n+1)/2` — the same map reads

```text
n ↦ (3n + 1)/4   if n ≡ 1 (mod 16)   one step of the odd-to-odd map T, with exactly two halvings
n ↦ (n − 1)/4    if n ≡ 5 (mod 16)   the inverse of the sibling relation n′ ↦ 4n′ + 1, with T(n) = T((n − 1)/4)
```

and the descent continues iff `n mod 48 ∈ {1, 33, 37}`.

**Proof.** Write `A = 3x − 1 = 2^s y`; the case split is Lemma 19.1.5's. `s = 1` iff `x ≡ 1 (mod 4)`: the parent is `state(y)`, `y = (3x−1)/2`, and `y + 1 = (3x+1)/2` is prime to `3`, so the parent's depth is `v₂((3x+1)/2)`, equal to `1` iff `x ≡ 1 (mod 8)`, and then its core is `(y+1)/2 = (3x+1)/4`. `s = 2` iff `x ≡ 7 (mod 8)`: the parent has depth `≥ 2`. `s ≥ 3` iff `x ≡ 3 (mod 8)`: the cascade parent's numerator is `(N + 3)/4` with `N = A + 1 = 3x` (14.10.1 read downward), i.e. `3(x+1)/4`, of depth `1 + v₃(x+1)`, equal to `1` iff `x ≡ 1 (mod 3)`, and then its core is `(x+1)/4`. Collecting: depth `1` iff `x ≡ 1 (mod 8)` (either class: `x ≡ 1, 17 mod 24`) or `x ≡ 3 (mod 8)` with `x ≡ 1 (mod 3)` (`x ≡ 19 mod 24`). Raw form: `x ≡ 1 (mod 8)` iff `n ≡ 1 (mod 16)` and `x ≡ 3 (mod 8)` iff `n ≡ 5 (mod 16)`; `2·(3x+1)/4 − 1 = (3n+1)/4`, with `3n + 1 ≡ 4 (mod 16)`, so exactly two halvings; `2·(x+1)/4 − 1 = (n−1)/4`, and `3n + 1 = 4(3·(n−1)/4 + 1)`. The residues mod `48` are `2·{1, 17, 19} − 1`. An odd `n` has a depth-`1` state iff `v₂(n+1) = 1` and `3 ∤ n + 1`. ∎

**What the descent is.** Read on the integers, the descent of a hair is the Collatz map itself, restricted: where `n ≡ 1 (mod 16)` it is one odd-to-odd step with two halvings; where `n ≡ 5 (mod 16)` it is not a step of the orbit at all but the move to the smaller sibling with the same image; it stops at the leg. Its length, the hair position, is unbounded, since hair lengths are (19.2). This is the core of the answer to (ii): recovering the owner from a member is walking a segment of the member's own Collatz orbit, of unbounded length.

**Verified** — Part B, 2026-09-26: `desc` against the comb parent, the mod-`24` continuation test, the raw form, the mod-`48` set, the two-halving and sibling identities, and the owner by `desc`-iteration against the owner by comb-parent ascent, on `15,000` random depth-`1` nodes (`x < 10^9`, all eight cells mod `24`) and on every one of the `165,441` depth-`1` nodes of the level-`18` census (hair positions `0` to `14`). `1,199,762` checks, `0` failures.

### 19.5.3. The member formula and the lens identity

**Definition 19.5.3 (hair word, position).** Along a hair from its leg `x_0`, each step up is a **link step** `x ↦ 4x − 1`, taken iff `x ≡ 2 (mod 3)` (the cascade child, Lemma 19.1.2), or a **fork step** `x ↦ (4x − 1)/3`, taken iff `x ≡ 1` or `4 (mod 9)` (the top-door child at `v₃(4x − 1) = 1`, Lemma 19.1.3); the hair ends at a fork with `x ≡ 7 (mod 9)`. The **hair word** of the member `x_k` is `w = ε₁ε₂…ε_k ∈ {0,1}^k` (`ε = 0` a link step, `1` a fork step); `k = |w|` is its length and hair position, `f = f(w) = ε₁ + … + ε_k` its number of fork steps, `f_j` the count after `j` steps. A member's **position** is `(b, w)`: its leg's index from Lemma 19.5.1(c), marked when the leg is the top leg, and its hair word. (The fork count `f(w)` is unrelated to 19.2's `f(n | ·)`.)

**Proposition 19.5.3.** Let `x` be the member at position `(b, w)` of the spider of `(Ω, D)`, with leg `x_0`.

- (a) **Member formula.** `3^f x + c_w = 4^k x_0`, where `c_w = Σ_{i=1}^{k} 4^{k−i} 3^{f_{i−1}}`, equivalently `c_∅ = 0`, `c_{wε} = 4c_w + 3^{f(w)}`. With Lemma 19.5.1(c):

```text
lower leg b:   x = (2^{2k+D+1−b} 3^b Ω − 4^k − c_w) / 3^f
top leg:       x = (2^{2k+D+1} Ω − 4^k − 3c_w) / 3^{f+1}
```

- (b) **Lens identity.** Write `lens_{b,w}(x) = 3^f x + c_w + 4^k` at a lower leg and `3^{f+1} x + 3c_w + 4^k` at the top leg (the **lens** of the position). Then

```text
lower leg b:   lens_{b,w}(x) = 4^k (x_0 + 1)  = 2^{2k+D+1−b} 3^b Ω
top leg:       lens_{b,w}(x) = 4^k (3x_0 + 1) = 2^{2k+D+1} Ω
```

so `Ω` is the `2,3`-free part of `lens_{b,w}(x)`, `b` is its `3`-adic valuation (`0` in the top form), and `D = v₂ + v₃ − 2k − 1` — as `ω` is the `2,3`-free part of `x + 1` and `d = m + a` the sum of its valuations. Equivalently: `lens_{b,w}(x) − 1` is the door `b` (the door `0` for the top leg) of the state `(Ω, D + 1 + 2k)`.

- (c) **Admissible words.** Whether `w` is the start of the hair at leg `b` of `(Ω, D)` is a function of `x_0 mod 3^{f(w)+1}`; with `x_0` written in `Ω`, a function of `D` and `Ω mod 3^e`, where

```text
e = max(0, f(w) + 1 − b)   (lower leg b),        e = f(w) + 2   (top leg),
```

and whether the hair ends exactly after `w` needs one ternary digit more (the end test `x_k ≡ 7 mod 9`).

**Proof.** (a) Induction on `k`: at `k = 0`, `x = x_0`. If `3^f x + c_w = 4^k x_0` and the next step is `x′ = (4x − 1)/3^ε`, then `3^{f+ε}x′ = 3^f(4x − 1) = 4(4^k x_0 − c_w) − 3^f = 4^{k+1}x_0 − (4c_w + 3^f)`. Unwinding the recursion gives the sum; substituting `x_0 + 1 = 2^{D+1−b}3^bΩ` or `3x_0 + 1 = 2^{D+1}Ω` gives the closed forms. (b) Add `4^k` to (a) (after multiplying by `3` in the top case). `Ω` is odd and prime to `3`, so the valuations are as stated; the door statement is door recovery (14.6.5.1) on `lens_{b,w}(x) − 1`. (c) `x_j = (4^j x_0 − c_{ε₁…ε_j})/3^{f_j}` exactly, with `4^j` a unit mod every power of `3`, so `x_j mod 3^m` is a function of `x_0 mod 3^{m + f_j}` (18.9.2.2's digit fact (c)). A link step at `x_j` reads `x_j mod 3`, needing `x_0 mod 3^{f_j + 1}`; a fork step reads `x_j mod 9`, needing `x_0 mod 3^{f_j + 2} = 3^{f_{j+1} + 1}`; the largest over the word is `3^{f(w)+1}`, and the end test reads `3^{f(w)+2}`. A lower leg has `x_0 ≡ −1 (mod 3^b)`, and `x_0 mod 3^m` is a function of `(D, Ω mod 3^{m−b})` for `m > b` (`2^{D+1−b}` a unit); a top leg has `x_0 = (2^{D+1}Ω − 1)/3`, so `x_0 mod 3^m` is a function of `(D, Ω mod 3^{m+1})`. ∎

The exponent is 19.3's cost accounting read from a leg: one ternary digit of `Ω` per fork step, none per link step, less the `b` digits a lower leg's `−1` already fixes. **Measured exact:** over `Ω mod 3^7`, `D = 2, …, 6`, every leg type and every word prefix with `e ≤ 6`, the least modulus is `3^e` in all `1,426` cases where the prefix is not forced; in the other `39` the prefix holds at every `Ω` of that leg type — in `35` because `e = 0` already (the prefixes `0`, `01`, `010` at `b ≥ 2` and `0` at `b = 1`), and in the other `4` (`b = 2`, `w = 0101`, `e = 1`, at `D = 3, …, 6`) because the single digit value the last step excludes is `2^{D−1}Ω ≡ 0 (mod 3)`, which `3 ∤ Ω` rules out.

**Corollary 19.5.3.1 (the deep legs).** A lower leg with `b ≥ 3` carries exactly the hair `0 1 0` (four nodes: link, fork, link, and a fork ending it). A leg with `b = 2` begins `0 1 0 1` (at least five nodes), its fifth node a link iff `2^{D−1}Ω ≡ 2 (mod 3)`. A leg with `b = 1` is a link whose next node is a fork ending the hair iff `2^DΩ ≡ 1 (mod 3)`.

**Proof.** A lower leg is `x_0 = 3^b u − 1`, `u = 2^{D+1−b}Ω` prime to `3`. For `b ≥ 3`: `x_1 = 4x_0 − 1 ≡ −5 ≡ 4 (mod 9)`, so a fork step follows; `4x_1 − 1 ≡ −21 (mod 27)` gives `x_2 ≡ −7 ≡ 2 (mod 9)`, a link; `x_3 = 4x_2 − 1 ≡ −29 ≡ 7 (mod 9)`, the end. For `b = 2`: `x_1 = 36u − 5 ≡ 4 (mod 9)`, `x_2 = 48u − 7 ≡ 2 (mod 3)`, `x_3 = 192u − 29 ≡ 3u + 7 (mod 9)`, which is `1` or `4` and never `7`: a fork step follows, and `x_4 = (4x_3 − 1)/3` is a fork at `u ≡ 1` and a link at `u ≡ 2 (mod 3)`. For `b = 1`: `x_1 = 12u − 5 ≡ 3u − 5 (mod 9)`, which is `7` (the end) at `u ≡ 1` and `1` (a fork step follows) at `u ≡ 2`. ∎

So the first steps of a hair at a leg with `b ≥ 1` are fixed by the leg's own digits, not drawn from 19.2's two-state chain, which describes the mixture over all legs. True hair lengths by leg type over the census abdomens (shares of lengths `1, 2, 3, 4` nodes): `b = 0`, `41,286` legs, `0.332, 0.114, 0.146, 0.086` (the chain from a fork: `0.333, 0.111, 0.148, 0.086`); `b = 1`, `82,490` legs, `0, 0.501, 0.167, 0.056` (the chain from a link: `0, 0.333, 0.111, 0.148`); `b = 2`, `27,432` legs, none below `5`; `b ≥ 3`, `13,721` legs, all `4`; top legs, `27,353`, `0.170, 0.220, 0.129, 0.115`; all `192,282` legs together `0.0954, 0.2705, 0.1214, 0.1299`, within `1%` of 19.2's predicted `0.0950, 0.2700, 0.1217, 0.1306`. The mixture's agreement is measured, as in 19.2; why the leg types average to the chain is not examined here.

**Worked instance.** On the hair from the top leg `13` of `(5,2)`, the member `17` has word `w = 1` (`k = f = 1`, `c_w = 1`): `lens(17) = 9·17 + 3 + 4 = 160 = 2^5·5`, so `Ω = 5`, `D = 5 − 2 − 1 = 2`, and `159 = y_0(5, 5)`. The `b = 3` leg of `(1,4)` is `y_3(1,5) = 107`, with hair `107 → 427 → 569 → 2275`, word `010`, ending at `2275 ≡ 7 (mod 9)`.

**What the analogy gives and what it does not.** (i) is answered: a spider member is addressed by `(Ω, D; b, w)` as a state's representative is addressed by `(ω, d; a)`, it is a closed formula in those four, and the lens identity reads `Ω`, `D` and `b` back off the member by valuations once the position is known. (ii) is not: a representative's `a` and `m` are the two valuations of `x + 1`, read in one step, while a member's `(b, w)` is the descent of 19.5.2 — a segment of the member's own Collatz orbit down to its leg — whose length is the hair position, unbounded; the lens needs `k`, `f` and `c_w`, which are that segment's record. This is 18.9's residue horizon in one more form: the coordinates are exact, and reading them off costs a walk whose length no bounded residue fixes (19.5.5).

**Verified** — Parts C and D, 2026-09-26: every leg of every one of the `82,490` census abdomens (inside or past the level-`18` boundary, `192,282` hairs) and of `2,000` random abdomens (`Ω < 10^6`, `2 ≤ D ≤ 14`, `15,761` hairs), each walked to the true end of its hair by ground-truth arithmetic (longest `55` nodes) — at every one of the `978,238` depth-`1` members: the step rule against the comb's children, the recursion against the sum, the member formula as an exact division, both lens identities with their three valuations and the door reading of `lens − 1`, and the descent returning to the leg in `k` steps; Corollary 19.5.3.1 at every lower leg with `b ≥ 1`; (c) by `163,678` random lifts `Ω′ ≡ Ω (mod 3^e)` at fixed `D` (the prefix, and at full length the whole hair with its end, preserved at every lift), and the least-modulus measurement above by full-coset enumeration.

### 19.5.4. The raw dictionary of a spider

**Remark 19.5.4.** In odd integers (18.4.1 with 19.5.1–19.5.3):

- the abdomen `(Ω, D)` is a **rising run** `y_0(Ω,D) → y_1(Ω,D) → … → y_{D−1}(Ω,D)`, each step `n ↦ (3n+1)/2` with one halving, followed by the exit `y` after `s + 1` halvings (`3y_{D−1} + 1 = 2A`). The run is maximal: `y_0` has no one-halving odd predecessor, since `2y_0 − 1 ≡ 2^{D+1}Ω ≢ 0 (mod 3)`. An abdomen's run has `D − 1 ≥ 1` one-halving steps; a depth-`1` node's run is its one integer `n ≡ 1 (mod 4)`, with none;
- the lower leg `b` is the odd integer `2y_b(Ω, D+1) − 1 = 4y_b(Ω, D) + 1` — the sibling of the run's own element `y_b(Ω, D)`, with the same `T`-image; the top leg (at `t = 1`) is `(4y_0(Ω, D) − 1)/3`, the odd preimage of the run's first element with exactly two halvings;
- a hair rises from its leg by `n ↦ 4n + 1` when `3 | n` (a link step: a multiple of `3` has no odd preimage, and `4n + 1 ≡ 1 (mod 3)` is its sibling) and by `n ↦ (4n − 1)/3` when `n ≡ 1 (mod 3)` (a fork step: the odd preimage with exactly two halvings); it ends at `n ≡ 4 (mod 9)`, where that preimage has depth `≥ 2` and is a representative of an abdomen. A hair's integers are never `≡ 2 (mod 3)`;
- descending, 19.5.2's raw map read on `n mod 8` instead of `n mod 16` — `(3n + 1)/4` at `n ≡ 1 (mod 8)`, `(n − 1)/4` at `n ≡ 5 (mod 8)` — carries a member down its hair and, from the leg, one step further, onto the run element `y_b(Ω, D)` (by a two-halving step from a top leg, by the sibling move from a lower leg), whose state and door index are `(Ω, D)` and `b`.

So, in the classical Collatz graph, a spider is **a maximal run of one-halving steps together with the two-halving predecessor chains that feed it, taken modulo the `4n + 1` sibling relation**: from the run, alternately take the two-halving preimage (when `n ≡ 1 mod 3`) and the sibling (when `3 | n`), until the preimage leaves depth `1`.

**Literature.** No name for this object was found in what the record holds. Checked: `TOUR.md`'s dictionary rows and the works they cite, the two published papers and their bibliographies, and the drafts under `sources/`. The relation `T(4n + 1) = T(n)` appears in the record only as the cascade step (reverse.md 14.10.1, `N(y, s+2) = 4N(y, s) − 3`) and in 18.4.1; predecessor trees of the `3x + 1` problem are cited to Wirsching 1998 in paper 2's related work, but the record does not hold Wirsching's text, so whether it names this object is not checked here. No web search was made.

**Verified** — Part D (run with Part C), 2026-09-26: at every abdomen walked, the run's steps, halving counts, exit and maximality; at every leg, its raw value, the sibling or two-halving identity, and the raw descent landing on `y_b(Ω, D)` with state `(Ω, D)` and door index `b`; at every one of the `978,238` members, depth `1` and never `≡ 2 (mod 3)`; each of the `770,195` raw moves with its residue condition, its sibling or two-halving identity and its inversion by the raw descent; the end at `n ≡ 4 (mod 9)` at every hair's last node.

### 19.5.5. The search for a walk-free identifier

The question, sharpened so that a search can close it: **is there a function of a member, computable without the walk, that is constant on every spider and separates spiders?** Two searches over the level-`18` census (`247,932` nodes, built fresh). The window matters here: the `41,061` abdomens at level `18` have no leg inside it and are left out; the other `41,429` give spiders of size `≥ 2`, of which `5,129` are **complete** (every hair ends inside the window). A spider cut by the window has fewer members and is more easily constant, so counts are given for both.

**E.1, affine lenses and comb quantities.** For `g_{α,β}(x)` = the `2,3`-free part of `αx + β` on the member's core, `α ∈ {1, 2, 3, 4, 6, 8, 9, 12, 16, 27}`, `β ∈ [−27, 27]` (`550` pairs, `311` after dividing out common powers of `2` and `3`; `αx + β` vanishes only at core `1` with `β = −α`, recorded with a sentinel rather than skipped, since skipping would drop the pair `(1, −1)` below), constancy was counted on the spiders (all members, abdomen included), on the `43,475` window hairs of `≥ 2` nodes, on the `41,312` link pairs (a link and its child) and on the `27,509` fork pairs (a fork and its fork-step child), against a baseline of the same members shuffled into groups of the same sizes:

```text
                           spiders       hairs    link pairs       fork pairs
g_(3,−1) = exit y          0             22,934   41,312 / 41,312  0
g_(1,−1)                   0              6,409   1                27,509 / 27,509
every other pair           ≤ 1           ≤ 2      ≤ 4              ≤ 2
shuffled baseline (max)    ≤ 1           ≤ 1      ≤ 3              —
```

Two invariants, derived before being read off the table. A link step has `3x′ − 1 = 4(3x − 1)`, so `g_{3,−1}(x)` — the exit `y`, since `3x − 1 = A = 2^s y` with `3 ∤ y` — is constant along it: a link and its child are siblings on one door, which is the control, `100%` by construction. A fork step has `x′ − 1 = (4/3)(x − 1)`, so `g_{1,−1}(x)` is constant along it — the all-fork case of the lens identity (`c_w = 4^k − 3^k` when `f = k`, so `3^k(x − 1) = 4^k(x_0 − 1)`). No affine pair is invariant under both steps: that needs `β = −α/3` and `β = −α` at once. The hair counts are exactly these: the `22,934` window hairs whose steps are all link steps and the `6,408` whose steps are all fork steps, plus one small-core coincidence (`5, 19, 25`: `g_{1,−1} = 1` throughout). Every other count is at the baseline's level; the single spider is `(1,2)`'s, where `Ω = 1` and every value in sight is `1`. Nothing separates spiders, because nothing is constant on them.

Comb quantities: the peak `A` and the top door `y_0` are injective on nodes (Lemma 18.1.2; door recovery) and constant on no spider; the peak's odd part is the exit `y` by definition. The exit `y` and `F(v)` are constant on `3,460` window spiders — every one an abdomen with only its cascade leg and that leg's link-step child inside the window, a cascade chain on the abdomen's own door cut at level `18` — and on `0` complete spiders; `F²(v)` is constant on `3,463` window spiders, of which `2` are complete — `(1,2)` and `(3641,2)`, whose members all reach `(1,1)` within two `F`-steps. The shuffled baseline is `0` for each.

**E.1 (ii), a lens returning the owner's core.** Which pairs give `g_{α,β}(x) = Ω` at a depth-`1` member? Exactly the lenses of Proposition 19.5.3(b) whose coefficients fall in the searched range, i.e. `k ≤ 2`, each at `100%` of its position class: `(1,1)` at every lower leg (`82,786`), `(3,1)` at every top leg (`13,834`), `(1,5)` at `b ≥ 1, w = 0` (`30,874`), `(3,5)` at `b = 0, w = 1` (`6,904`), `(3,7)` and `(9,7)` at the top leg's `w = 0, 1` (`3,461`, `2,236`), `(3,21) ~ (1,7)` at `b ≥ 1, w = 01` (`10,266`), `(3,23)` and `(9,23)` at `b = 0, w = 10, 11` (`1,735`, `1,131`) — and elsewhere only `769` coincidences among `1,097,430` hits, at most `12` for any pair outside its class. The search recovers the lens identity for short words and nothing else. No pair returns `Ω` at every depth-`1` member of more than one complete spider (`(1,2)`'s again); the window's `13,853` for `(1,1)` are cut spiders whose window members are only legs.

**E.2, residue determinacy.**

**Proposition 19.5.5 (the position is a `2`-adic cylinder).** For each `j ≥ 0`, whether a depth-`1` core `x` has hair position exactly `j` is a function of `x mod 2^{2j+3}·3`.

**Proof.** A `desc`-step at `x` reads `x mod 8` and `x mod 3` (the test `x mod 24 ∈ {1, 17, 19}` and the case). `desc(x) mod 2^m` is a function of `x mod 2^{m+2}` (both branches divide exactly by `4`). And `(3x + 1)/4 ≡ 1 (mod 3)` for every `x`, while `(x + 1)/4 ≡ x + 1 (mod 3)`, so `desc^i(x) mod 3` is a function of `x mod 3` alone. The first `j + 1` tests therefore read `x mod 2^{2j+3}` and `x mod 3`. ∎

**Measured exact:** by full-coset search over every odd residue prime to `3` mod `2^{2j+3}·3`, with candidates `2^a·3^c`, the least modulus is `2^{2j+3}·3` at every `j = 0, …, 7` (`24, 96, 384, …, 393,216`); confirmed on every depth-`1` node of the census and on `300` random large lifts per `j`, and the least modulus consistent with the census alone coincides at every `j`. So the position is decided by a bounded residue at each fixed `j`, but the modulus grows by `2^2` per step and no single modulus decides it. The derivation corrects the expectation that fork steps would cost ternary digits here: the descent reads two binary digits per step, as any fixed-parity segment of `T` does (Terras's cylinders; TOUR.md's digit-budget row), and one ternary digit in all; the ternary budget of 19.3 and 19.5.3(c) belongs to the ascent from a leg, not to the descent from a member.

**Proposition 19.5.5.1 (the owner is not a bounded residue).** For no `j ≥ 0` and no modulus `2^a 3^c` is the owner's depth `D`, or its `Ω mod 3`, a function of `x mod 2^a 3^c` on the members at hair position `j`.

**Proof.** Take an abdomen `(Ω₁, D₁)` with `D₁ ≥ max(a, 2)` whose `b = 1` leg `x_0 = 3·2^{D₁}Ω₁ − 1` has a hair reaching position `j`, with word `w`, `f = f(w)`. Such an `Ω₁` exists at every `D₁` and `j`: for `j ≥ 2` choose `Ω₁ ≡ 2^{−D₁−1} (mod 3^{j−1})`, which makes `x_1 = 4x_0 − 1 ≡ 1 (mod 3^j)`, and fork steps multiply `x − 1` by `4/3`, so `j − 1` of them follow; at `j ≤ 1` any `Ω₁` serves (the leg is a link, whose child always exists, Lemma 19.1.2). Let `D₂ = D₁ + 1` and choose `Ω₂` odd with `Ω₂ ≡ 2^{−1}Ω₁ (mod 3^{c+f+1})`. The `b = 1` leg of `(Ω₂, D₂)` is `x_0′ = 3·2^{D₂}Ω₂ − 1`, and `x_0′ − x_0 = 3·2^{D₁}(2Ω₂ − Ω₁)` is divisible by `2^a·3^{c+f+2}`; by 19.5.3(c) the word `w` is admissible at `x_0′` too, and by (a) the two members at position `(1, w)` differ by `4^k(x_0′ − x_0)/3^f`, divisible by `2^a 3^c`. Their owners have depths `D₁ ≠ D₂` and cores `Ω₂ ≡ 2Ω₁ ≢ Ω₁ (mod 3)`. (Every rule used is local — 19.5.1–19.5.3 and the parent rule — so nothing here depends on whether the two abdomens lie in the comb.) ∎

The reason in one line: a member sees its owner's depth only through the factor `2^{D+1−b}` in its leg (19.5.1(c)), which every fixed `2`-adic modulus loses once `D` is large, and `Ω mod 3` shifts with it. **Verified** by construction: `336` such pairs (`j = 0, …, 6`, `a = 3, 6, …, 24`, `c = 1, …, 6`), each member's position and owner checked by descent and by comb-parent ascent.

**The answer.** In the forms searched, no walk-free identifier exists. No affine lens with the searched coefficients is constant on spiders: two are constant along one kind of step each (the exit along link steps, `g_{1,−1}` along fork steps) and none along both, and the rest is coincidence at small cores; the comb quantities on file are constant only on window-cut cascade chains and next to the root; the hair position is a bounded residue at each fixed `j`, with modulus `2^{2j+3}·3`, so no single modulus decides it; and the owner's depth and `Ω mod 3` are decided by no bounded residue at any position. The reason is the one 19.5.2 states: the owner is read at the end of the member's own Collatz orbit segment, whose length is unbounded and whose record `(k, f, c_w)` is what the lens needs. What was checked for a closed form of such a segment: `TOUR.md`'s dictionary rows and the sources they cite — the segment is a fixed-parity segment of `T`, whose cylinder is a residue class mod a power of `2` growing with its length (Terras 1976), and nothing on file gives the segment's end without walking it. The answer to the author's question is therefore 19.5.3's coordinates `(Ω, D; b, w)`, with the lens identity as the positive content, and this closure as its calibration. The searches are bounded — affine lenses with `α ≤ 27`, `|β| ≤ 27`, the comb quantities listed, residues `2^a 3^c` — and no impossibility beyond Proposition 19.5.5.1 is claimed.

**Verified** — Part E, 2026-09-26: the census built fresh (`247,932` nodes); E.1's tables above, with the exact invariants asserted as checks (`g_{3,−1}` and the exit on every link pair, `g_{1,−1}` on every fork pair, every exit-constant spider identified as a window-cut cascade chain, every `k ≤ 2` lens returning `Ω` at every member of its class); E.2's full-coset search for `j = 0, …, 7` with its census and lift confirmations; the `336` constructions of Proposition 19.5.5.1. Whole script: `15,380,113` checks, `0` failures, wall clock about `35` s; single reproducing command `python experiments/spider_coordinates.py`, which writes `experiments/spider_coordinates_output.txt` itself.

### 19.5.6. Standing

Proved, each with an independent check by fresh code: the legs of an abdomen are the doors `b = 1, …, D−1` of `(Ω, D+1)`, with its door `0` at `t = 0` or the top leg at `t = 1` (19.5.1); the hair descent map and its raw form, the Collatz map in two-halving steps interleaved with sibling moves (19.5.2); the member formula, the lens identity, and the residue condition on admissible words, with the deep-leg corollary (19.5.3); the raw dictionary (19.5.4); the position's sufficient modulus and the owner's non-determinacy by any bounded residue (19.5.5). Measured: the exact least moduli (words over `Ω mod 3^7`; positions `j ≤ 7`), the per-leg-type hair lengths, and E.1's tables. The answer to the author's question is the coordinates `(Ω, D; b, w)` in the direction abdomen to member and a walk of unbounded length in the other. Nothing is proposed, no front moves, no cycle is searched; the positive comb only (every rule is sign-blind, 18.8, and not exercised here). Grade: **formulation plus measurements**.
