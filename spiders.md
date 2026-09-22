---
status: FORMULATION — the first abstraction layer above reduced states: the classification of comb nodes by depth and residue (abdomens, forks, links), the hair chains, the partition of the comb into spiders, the hair-length law, and the spider tree with its census; no front moves
scope: new section 19
updated: 2026-09-22
source: the author's direction of 2026-09-22 (build the next deterministic abstraction up from reduced states, one layer at a time); briefs/spider-layer-brief.md
---

> **Current state.** Every comb node (comb.md §18) is classified by its depth `D` and, at depth `1`, its residue `Ω mod 3`: an **abdomen** (`D ≥ 2`), a **fork** (`D = 1`, `Ω ≡ 1 mod 3`), or a **link** (`D = 1`, `Ω ≡ 2 mod 3`); the root `(1,1)` is a fork by residue but is its own piece (19.1). A link has exactly one child, always a fork of depth `1`; a fork has exactly two children, a cascade abdomen and a top-door child whose depth is `1` iff `Ω ≢ 7 mod 9`, in which case its own class is exact by `Ω mod 9` — so a depth-`1` node has at most one depth-`1` child, and the depth-`1` material above an abdomen is a set of simple chains, the **hairs** (19.1, 19.2). Which depth-`1` nodes are *not* legs (direct children of an abdomen) is settled completely: the residue table by `(Ω mod 3, Ω mod 8)`, derived here in full (19.1, Item A.4). The comb partitions exactly into **spiders** (an abdomen plus its hairs) and the root's own piece; over the comb to level `18`, `247,932` nodes fall into `82,491` pieces, mean size `3.006`, largest `40` (19.2). The hair-length law is a two-state Markov chain forced by Items A.1–A.2; matched to the *true* (level-boundary-corrected) length distribution to within `2%` at every one of the first eight lengths — the level-`18` census window itself truncates `71.5%` of hairs, an artifact identified and corrected, not a property of the law (19.2). The spider tree (spiders as nodes) is proved a tree with a census by level, a sufficient digit budget for a whole spider's shape, and a negative answer, with a reason, to whether the child-spider count is a bounded-residue function of the abdomen's core (19.3). The layer is a residue-based coarse-graining of the comb by depth and by `Ω mod 24` and `mod 9`, sitting inside 18.9's own horizon; nothing here moves any front (19.4).

# 19. The spider layer

Every rule in this section is sign-blind, exactly as in 18.8: no algebraic step below reads the sign of `Ω`. Only the positive comb is worked out; the record does not repeat the construction on the three negative components.

## 19.1. The classification of nodes

**Definition 19.1.1 (the classification).** For a comb node `(Ω, D)`:

- an **abdomen** if `D ≥ 2`;
- a **fork** if `D = 1` and `Ω ≡ 1 (mod 3)`;
- a **link** if `D = 1` and `Ω ≡ 2 (mod 3)`.

The root `(1,1)` is a fork by this residue rule, but is treated as its own piece throughout (19.2): its only child is the abdomen `(1,2)` (comb.md 18.2.3).

**Lemma 19.1.2 (Item A.1 — a link's one child).** A link `(Ω, 1)` has exactly one child: its cascade child `(4Ω − 1, 1)`, of depth `1`, which is always a fork; its top door is dead.

**Proof.** The top door of `(Ω,1)` is `y₀ = 2Ω − 1`; it is dead iff `2Ω ≡ 1 (mod 3)` (comb.md 18.2.3/reverse.md 14.5.1), and `2Ω ≡ 2·2 ≡ 1 (mod 3)` since `Ω ≡ 2`. With `D = 1` there is no side door (`a` ranges over `∅`), so the cascade child is the only child. By comb.md 18.9.1's cascade-child law at `D = 1`, its depth is `1 + v₃(4Ω − 1)`; and `4Ω − 1 ≡ Ω − 1 ≡ 2 − 1 ≡ 1 (mod 3)` (using `4 ≡ 1 mod 3`), so `v₃(4Ω − 1) = 0` and the depth is exactly `1`. Its core `4Ω − 1` is itself `≡ 1 (mod 3)`, a fork. ∎

**Lemma 19.1.3 (Item A.2 — a fork's two children, and the exact class split at `t = 1`).** A fork `(Ω, 1)` has exactly two children: a cascade child of depth `t + 1 ≥ 2` (an abdomen) and a top-door child of depth `t`, where `t = v₃(4Ω − 1) ≥ 1`; both children share the same core, `(4Ω − 1)/3ᵗ`. The top-door child has depth `1` iff `t = 1` iff `Ω ≢ 7 (mod 9)`, and then its class is exact: a **fork** iff `Ω ≡ 1 (mod 9)`, a **link** iff `Ω ≡ 4 (mod 9)`.

**Proof.** The top door is `y₀ = 2Ω − 1 ≡ 2 − 1 ≡ 1 (mod 3)` (`Ω ≡ 1`), hence alive (`2·1 ≢ 1 mod 3`... concretely `2Ω ≡ 2 ≢ 1 mod 3`) and at the lowest branch `s₀ = 1` (`y₀ ≡ 1 mod 3`). By comb.md 18.9.1 at `D = 1`: the cascade child has depth `1 + v₃(4Ω − 1) = t + 1`, and the top-door child's numerator is `2y₀ + 1 = 4Ω − 1`, the same integer, so its depth is `v₃(4Ω − 1) = t` and its core is `(4Ω − 1)/3ᵗ` — the same core as the cascade child's, reached by one fewer factor of `3` removed. Since `Ω ≡ 1 (mod 3)`, `4Ω − 1 ≡ 0 (mod 3)`, so `t ≥ 1` always; writing `Ω mod 9 ∈ {1, 4, 7}`: `4·1 − 1 = 3` (`v₃ = 1`), `4·4 − 1 = 15` (`v₃ = 1`), `4·7 − 1 = 27` (`v₃ = 3 ≥ 2`) — so `t = 1` iff `Ω ≡ 1` or `4 (mod 9)`, i.e. iff `Ω ≢ 7 (mod 9)`. When `t = 1` the core is `(4Ω − 1)/3`: at `Ω ≡ 1 (mod 9)` this is `1` (mod 3, from `3/3 = 1`, and in general `(4Ω−1)/3 mod 3` is fixed by `Ω mod 9`, exact); at `Ω ≡ 4 (mod 9)` it is `5/3 = ` … concretely for `Ω = 4`: `(16−1)/3 = 5 ≡ 2 (mod 3)`, a link; for `Ω = 1`: `(4−1)/3 = 1 ≡ 1 (mod 3)`, a fork. Since the map `Ω ↦ (4Ω−1)/3 mod 3` is an affine function of `Ω mod 9` on each of the two admissible residues, it is constant on each: `Ω ≡ 1 (mod 9)` always gives a fork, `Ω ≡ 4 (mod 9)` always gives a link. ∎

**Corollary 19.1.4 (Item A.3 — at most one depth-`1` child).** A depth-`1` node has at most one depth-`1` child: a link has exactly one (forced, Lemma 19.1.2); a fork has one iff `t = 1`, else none (Lemma 19.1.3). Consequently the depth-`1` material lying above an abdomen is a union of simple chains — the hairs of 19.2 — never a bush.

**Lemma 19.1.5 (Item A.4 — the complete parent-is-abdomen table).** For a depth-`1` node `(Ω, 1)`, whether its comb parent is an abdomen is a function of `(Ω mod 3, Ω mod 8)`, given by:

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

**Lemma 19.1.6 (Item A.5 — the abdomen leg count).** An abdomen `(Ω, D)` has

```text
legs = (D − 1) + [3 ∤ 2^{D+1}Ω − 1] + [top door alive and its child of depth 1]
```

legs: the cascade child (core `4·3^{D−1}Ω − 1`, always a **link**), the children through doors `a = 2, …, D−1` (cores `2^{D−a+2}3^{a−1}Ω − 1`, always **links**), the door-`a = 1` child when its depth is `1` (core `2^{D+1}Ω − 1`, always a **fork** when it is a leg), and the top-door child when its depth is `1` (class not forced).

**Proof.** The cascade child of an abdomen has depth `1` always (comb.md 18.9.1 at `D ≥ 2`), so it is a leg unconditionally; its core `4·3^{D−1}Ω − 1 ≡ −1 ≡ 2 (mod 3)` since `D − 1 ≥ 1` forces the leading term `≡ 0 (mod 3)` — always a link. For `a ≥ 2`, comb.md 18.9.1's proof gives the child's numerator bracket `2^{D−a+2}3^{a−1}Ω − 1`, and `a − 1 ≥ 1` again forces the leading term `≡ 0 (mod 3)`, so the bracket `≡ −1 ≡ 2 (mod 3)` — depth `1` and a link, always, for every `a ≥ 2` (there are `D − 2` such doors, giving the `D − 1` count together with the cascade leg). For `a = 1`, the bracket `2^{D+1}Ω − 1` carries no forced factor of `3`: it is a leg iff `2^{D+1}Ω ≢ 1 (mod 3)`, i.e. (since `2^{D+1}Ω` is a unit mod `3`, hence `≡ 1` or `2`) iff `2^{D+1}Ω ≡ 2 (mod 3)` — and then the bracket itself is `≡ 2 − 1 ≡ 1 (mod 3)`, a fork, forced by the same triviality that decides leg-hood. The top door's numerator always carries at least one forced factor of `3` (it is chosen at the admissible branch `s₀`), so no such triviality applies to its quotient; the class is not forced and both occur (the fork's own top-door child of Lemma 19.1.3 is the `D = 1` instance of exactly this indeterminacy). ∎

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

**The level-`18` census window is not the law.** Measured directly within the window, the length distribution (`53,145` at length `1`, `28,290` at `2`, `8,818` at `3`, …, matching the brief's own pre-check exactly) disagrees badly with the prediction — e.g. `55.0%` of hairs measured length `1` against a predicted `9.5%`. The discrepancy is a boundary artifact, not a failure of the law: a hair node discovered exactly at level `18` has no census-recorded child, so a chain that reaches the boundary is cut off there whether or not it truly continues — and by Lemma 19.1.2 a link **always** continues, so every link leg sitting exactly at level `18` (`34,743` of the `69,078` link legs) is wrongly recorded as a length-`1` hair. Recomputing every hair's length by ground-truth arithmetic alone (`comb_children`, unbounded, independent of the census) rather than by the census neighbour list shows `69,099` of the `96,620` hairs (`71.5%`) are affected. The **true** distribution matches the predicted one closely at every tested length:

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

The true maximum hair length observed in this census is `55` (against `15` within the truncated window). The census-window figures are retained above only because they reproduce the brief's own pre-check exactly and are the ones a reader following the pre-check would compute; the true, boundary-corrected figures are the ones that test the law.

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

What the layer is: a residue-based coarse-graining of the comb by depth (`D ≥ 2` vs `= 1`) and, within depth `1`, by `Ω mod 3` (fork vs link), `Ω mod 8` (whether the parent is an abdomen), and `Ω mod 9` (a fork's continuation class) — sitting entirely inside 18.9's own horizon: a spider's shape is a signature in that section's sense, and the digit budget that fixes it (19.3) is 18.9.2's own cost composition applied along a hair. What it is not: no front moves, nothing about which states the comb reaches is touched, and no cycle is searched. The author's north star — that the layers built this way may eventually be raised until the whole map is one object — is recorded here as the stated direction of the work, not as a claim: nothing beyond the construction, the partition, the hair-length law and the spider tree's census is asserted in this section. Grade: **formulation plus measurements**.
