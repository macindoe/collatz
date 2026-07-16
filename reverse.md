---
status: ACTIVE — predecessor structure and 3-adic mirror machinery exact and fully dualized (14.1–14.10); dead ends classified (14.5); rigorous density bound proved (14.6, c* = 0.3304; canonical five-lemma proof in paper 2); steering laws back-ported (14.12); KL–LP density refinement closed short of the 0.43 bar (14.6.5, 14.13, structural obstruction recorded); the door/exit seam proved and placed (14.14) — a total, constant-offset graded law for the 3-adic anchor along forward orbits, with the core-extraction deficit shown to relocate onto it exactly rather than dissolve; a corollary layer (14.14.7–14.14.8, block-map brief) reads G as T's own variable-return-time block map, strengthens the tightness law, and composes it along fixed itineraries, reconciling the periodic-word fixed point with the classical cycle candidate (cycles.md §12.1) — no change to the seam's or the Bridge's status; the itinerary language is now fully characterized at finite level (14.15) — the classical Collatz coding in door coordinates, a full shift with no finite-level rigidity to find, and a formulation-grade two-sided Z_2×Z_3 coding whose periodic points are the classical cycle candidate and whose general locus is the Bridge's symbolic name — no change to the Bridge's status; the unique-predecessor lemma, the finite bicylinder corollary (no finite two-sided obstruction, ever), and the positive realization height (an equivalent boundedness criterion for 14.15.3(c)'s diagonal locus) are proved (14.15.4, bicylinder-height brief) — no change to the Bridge's status
scope: new section 14 (post-monolith)
updated: 2026-07-16
source: new material; the author's reversal question; builds on 9.8 (spine.md), 11.5 (open-problems.md), §3 anchor machinery
---

> **Current state.** The reduced map run backward. The predecessor structure of `F` is completely characterized (14.1, verified exactly against brute force), and it is governed by a **3-adic anchor** `M₃(y)` — an affine logarithm base 2 — through the exact law `d = 1 + v₃(s − M₃(y))` (14.2): the precise mirror of the forward 2-adic law, with the roles of 2 and 3, and of `s` and `d`, exchanged (duality table, 14.3). The backward branching ledger is `P(d = j) = 2·3^(−j)`, verified. The backward tree from `(1,1)` is enumerable exactly in increasing `ω`; its empirical growth exponent is ≈ 0.97–0.98 and rising with the cutoff, consistent with density one (14.4). Honest scope: backward reachability of all states *is* the conjecture (9.8), so this front proves no shortcut — its target is the density program: an exact renewal equation for the tree from the exact branching law, aimed at the Krasikov–Lagarias-type exponents. The first naive renewal equation was wrong (representative multiplicity) and is recorded as the open item. **The queue of dual per-step theorems (14.7–14.10) is now closed**: digit-determinacy, the anchor-increment law, the one-step decision procedure, and the depth ladder all have exact 3-adic mirrors, each verified independently — and each also carries a genuine, non-forced asymmetry against its forward counterpart, precisely identified rather than papered over (no cross-prime step in 14.7's division; a hard mortality-freeze in 14.8 with no forward analogue; a trichotomy collapsing to a dichotomy in 14.9; a forced step-size-2 in 14.10's ladder). **The door/exit seam (14.14, 2026-07-14)** re-expresses the forward Bridge increment and the reduced map itself around one coordinate, the live door `y` shared by both directions: the exit map `G` (14.14.3) semiconjugates to `F` in door coordinates (an extension of `F` via the many-to-one `state` map, not a strict conjugacy), is total and lives entirely on live doors (no mortality), and on fixed `2`-adic strata is an honest `3`-adic contraction (14.14.4) that supports a total graded `ΔM₃` law with a *constant* modulus offset (14.14.5) — sharper in form than either the forward law (11.8.7.3.1) or the top-door mirror (14.8.2), both of which need a growing modulus. The reconciliation (14.14.6) shows this is not new leverage on the Bridge: the seam's stratum labels are exactly stage3.md/stage4.md's own `(s, m_+)` digit-cost pair, so the gain is bought at the core-extraction deficit's own price, relocated rather than escaped. **A corollary layer (14.14.7–14.14.8, 2026-07-15, per `briefs/block-map-brief.md`)** interprets `G` as `T`'s own variable-return-time block map (14.14.7: `T^{v_2(y+1)}(y) = G(y)`, tied cleanly to spine.md's block/cascade decomposition), strengthens `14.14.5`'s tightness paragraph into an exact per-stratum metric law (14.14.5.4), and composes the affine and graded laws along a fixed sequence of strata (14.14.8): the composed map synchronizes at every fixed `3`-adic precision, and its periodic-word fixed point is identified — explicitly, not as a new lever — with the classical rational cycle candidate already implicit in cycles.md §12.1. The Bridge's own status is unchanged. **The itinerary language (14.15, 2026-07-16, per `briefs/itinerary-coding-brief.md`)** proves the finite-itinerary cylinder theorem — every finite word over the door alphabet `{(m,r):m,r≥1}` is realized by exactly one odd residue class mod `2^(S+1)` (14.15.1) — identifies this as the classical Collatz coding (Terras, Everett, Lagarias) read in door coordinates, not new mathematics about `T`, and draws the calibration that the itinerary language is a **full shift**: no finite-state admissibility rigidity exists to find (14.15.2). It then formulates, at formulation grade, a two-sided coding: right-infinite words determine a `2`-adic coordinate (the classical future-coding, injectivity proved), left-infinite words determine a `3`-adic coordinate by a convergence argument on `14.14.8`'s own composed law, and a bi-infinite word's *diagonal compatibility locus* — the definition and its trivial direction only — is identified as the Bridge in symbolic form, its periodic points as the already-known classical cycle candidate (14.15.3). No change to the Bridge's status. **A fourth block (14.15.4, 2026-07-16, per `briefs/bicylinder-height-brief.md`)** proves the unique-predecessor lemma (the letter-prescribed predecessor of a live door, on a fixed stratum, is unique and automatically positive — the door-coordinate form of the backward branching law, `14.2.4`), the finite bicylinder corollary (every finite two-sided itinerary window, past and future both prescribed, is realized by an actual positive live integer segment — no finite two-sided obstruction, ever), and the positive realization height `H_{p,q}(W)`, whose boundedness is proved exactly equivalent to `14.15.3`(c)'s integral realizability — a working boundedness criterion for the diagonal locus, naming its archimedean content, with no estimate on `H` attempted. No change to the Bridge's status.

# 14. The Reverse Dynamics: a 3-adic Mirror

The forward map `F` is deterministic; run backward it is a tree. This section characterizes that tree exactly and finds that the entire anchor apparatus of the forward theory dualizes: forward arithmetic is 2-adic, backward arithmetic is 3-adic, and the conjecture is the statement that the two trees are one.

## 14.1. Predecessor structure

**Proposition 14.1.1 (complete characterization of `F⁻¹`).** Let `(Ω, D)` be a valid state with representatives `y_a = 2^(D−a) 3^a Ω − 1`, `0 ≤ a ≤ D−1`. The predecessors of `(Ω, D)` under `F` are exactly the states obtained as follows: for each representative `y = y_a` with `3 ∤ y`, and for each `s ≥ 1` with `s` odd if `y ≡ 1 (mod 3)` and `s` even if `y ≡ 2 (mod 3)`, set `N = 2^s y + 1`; then `3 | N` automatically, and the predecessor is

```text
(ω, d) = ( N / 3^(v₃(N)),  v₃(N) ).
```

Every such `(ω, d)` is a valid state with `F(ω, d) = (Ω, D)`, exit value `y`, and exit valuation `s`; distinct `(a, s)` give distinct predecessors; and there are no others. Representatives with `3 | y` (possible only at `a = 0`) contribute nothing: they are **leaf doors**, the reduced form of the classical fact that multiples of 3 have no odd preimages.

**Proof.** `F(ω,d) = (Ω,D)` iff `x_exit(ω,d) = (3^d ω − 1)/2^s` equals some representative `y`, i.e. `3^d ω = 2^s y + 1` with `s = v₂(3^d ω − 1)` consistent. Given `y` and `s`, the factorization `N = 3^d ω` with `3 ∤ ω` forces `d = v₃(N)`, `ω = N/3^d`, and `3 | N` iff `2^s y ≡ 2 (mod 3)`, which is the stated parity condition; the valuation consistency is automatic since `2^s y = N − 1` gives `v₂(3^d ω − 1) = s` exactly (`y` odd). ∎

**Verification.** For seven targets, the rule's output matches a brute-force forward scan over all `(ω ≤ 3000, d ≤ 12)` exactly — no missing, no spurious. Code: `experiments/reverse_tree.py`.

Each valid door thus carries an infinite branch family, one predecessor per `s` of the correct parity: the backward tree has countably infinite branching with exactly computable structure.

## 14.2. The mirror isometry and the 3-adic anchor

**Lemma 14.2.1 (mirror isometry).** For even `t ≥ 2`, `v₃(2^t − 1) = 1 + v₃(t)` (lifting-the-exponent). This mirrors the forward isometry `v₂(9^t − 1) = 3 + v₂(t)`.

The unit group mod `3^k` is cyclic of order `2·3^(k−1)`, generated by `2`; the exponent group in the inverse limit is `Z/2 × Z₃`.

**Definition 14.2.2 (backward anchor).** For odd `y` with `3 ∤ y`, let `M₃(y) ∈ Z/2 × Z₃` be the solution of `2^(M₃(y)) = −1/y`. Its parity component is fixed by `y mod 3` (this is the parity condition of 14.1.1), and its `Z₃` component is the anchor proper.

**Proposition 14.2.3 (algebra of `M₃`).** `M₃(1)` is the distinguished exponent class representing the discrete logarithm of `−1` to base `2` — an element of the exponent group `E₃ = lim Z/(2·3^(k−1)) ≅ Z/2 × Z₃`, not of `Z₃` itself: concretely `2^(3^(k−1)) ≡ −1 (mod 3^k)`, so its truncation mod `2·3^(k−1)` is `3^(k−1)` (verified for `k = 8`). *(Language corrected 2026-07-12 per paper-2 referee: the earlier "3-adic −1" conflated an exponent-group element with a 3-adic integer.)* And `M₃` is an affine logarithm: `M₃(y₁y₂) = M₃(y₁) + M₃(y₂) − M₃(1)` (zero failures in 300 random pairs), so `M₃(y) = M₃(1) − log₂ y` in the 3-adic discrete logarithm.

**Theorem 14.2.4 (backward valuation law).** For a door `y` and any `s` of the correct parity,

```text
d = v₃(2^s y + 1) = 1 + v₃(s − M₃(y)).
```

**Proof.** `2^s y + 1 = y·2^(M₃(y))·(2^(s − M₃(y)) − 1)` since `2^(−M₃(y))·y^(−1) = −1`; the prefactor is a 3-adic unit; the parity condition makes `s − M₃(y)` even in the `Z/2` component, and Lemma 14.2.1 applies to the bracket. ∎

**Verification.** `4,265` random `(y, s)` checks at anchor depth `3^8`, zero failures. The **backward ledger** follows: over branches, `P(d = j) = 2·3^(−j)` — measured `0.6664, 0.2230, 0.0736, 0.0245, 0.0082` against `2/3, 2/9, 2/27, 2/81, 2/243`.

## 14.3. The duality

| forward (§3 of the paper) | backward (this section) |
|---|---|
| arithmetic prime: 2 | arithmetic prime: 3 |
| exit valuation `s = v₂(3^d ω − 1)` | entry depth `d = v₃(2^s y + 1)` |
| anchor `N(ω) = −log ω / log 9 ∈ Z₂` | anchor `M₃(y) = M₃(1) − log₂ y ∈ Z/2 × Z₃` |
| law `s = 2 + v₂(d − M(ω))` | law `d = 1 + v₃(s − M₃(y))` |
| isometry `v₂(9^t − 1) = 3 + v₂(t)` | isometry `v₃(2^t − 1) = 1 + v₃(t)` |
| ledger `P(s = j) = 2^(−j)` | ledger `P(d = j) = 2·3^(−j)` |
| residue classes mod 8 gate the law | residue class mod 3 gates the parity |
| deterministic forward orbit | infinitely-branching backward tree |
| AEH: orbit equidistribution (§13) | density of the tree in ℕ (14.4) |

The conjecture, in this language: the deterministic 2-adic forward flow and the 3-adic backward tree rooted at `(1,1)` describe the same object — every state lies on both.

## 14.4. The backward tree and the density program

Because branching is exact, the tree from `(1,1)` can be enumerated *completely* up to any `ω`-cutoff by expanding states in increasing `ω` (predecessor sizes grow like `2^s y / 3^d`, so the frontier is finite). Counts:

```text
ω ≤ 2^10 :    833 states   (exponent ≈ 0.970)
ω ≤ 2^13 :  6,261           (≈ 0.970)
ω ≤ 2^16 : 51,259           (≈ 0.978)
ω ≤ 2^19 : 408,302          (≈ 0.981)
```

The exponent rises with the cutoff, consistent with the tree having full density (exponent 1) — which is what the conjecture predicts and what no counting can prove. The rigorous frontier here is the Krasikov–Lagarias-type lower bounds (`≥ x^0.84`-flavor), which were derived *without* an exact local branching law. The front's concrete target: derive the exact renewal/functional equation for the tree from Theorem 14.2.4 plus the door structure of 14.1.1, and test whether it sharpens those exponents. **Recorded failure:** the first attempt at that equation (single-type branching, geometric depth) was wrong — it ignored the representative multiplicity (each state has `D` doors) and door-leaf structure; the correct equation is a multi-type renewal over `(door class, depth)` and is the open item.

## 14.5. Dead ends: door mortality, Gardens of Eden, and the renewal equation

*(Added 2026-07-11, from the author's question: under what conditions does backward generation cease?)*

**Theorem 14.5.1 (door mortality).** For a state `(Ω, D)`, the doors `y_a` with `a ≥ 1` are never dead (`y_a ≡ 2 (mod 3)` identically). The sole mortal door is `a = 0`: it is dead iff `2^D Ω ≡ 1 (mod 3)`, which holds on exactly two of the four admissible residue–parity classes of `(Ω mod 3, D mod 2)` (density 1/2 under uniform counting of these classes — there is no uniform measure on the infinite state space, so "half of all states" is shorthand only). **Verified exactly on 20,000 random states, all doors.**

**Theorem 14.5.2 (Gardens of Eden).** A state has no `F`-preimage at all iff `D = 1` and `Ω ≡ 2 (mod 3)` — equivalently, iff its unique representative is an odd multiple of `3`. Every state with `D ≥ 2` is reachable (door `a = 1` is always alive). **Verified against the forward image on 600 states.** This is the reduced form of the classical fact that multiples of `3` have no odd preimages: classically one third of odd numbers are unreachable *values*; in reduced coordinates, unreachability concentrates entirely on depth-`1` states of core `≡ 2 (mod 3)`, while deeper states merely lose one door.

**14.5.3 (the renewal equation, mortality included — resolving the 14.4 open item at the heuristic level).** The multi-type branching analysis of the tree, with the door structure of `14.1.1`, the depth law `2·3^(−d)`, the measured stationary depth distribution, and Theorem `14.5.1`'s mortality (a factor `1/2` on door `0`), gives the renewal mass

```text
mass(c) = E_D [ Σ_(a<D) (½ if a=0 else 1) · 2^(−c(D−a)) 3^(−ca) ] · Σ_s 2^(−cs) · E[3^(cd)].
```

Computed over `c ∈ (0,1)`: the mass **never falls to 1** — its minimum is `≈ 1.52` at `c ≈ 0.7`. The backward tree is supercritical at every sub-density exponent: the analysis predicts growth exponent `1` (full density), consistent with the exact enumeration (`0.970 → 0.981`, rising) and with the conjecture's prediction. Two honest notes: an earlier single-type version of this equation was wrong and is recorded above (14.4); and the present computation is a heuristic with one measured input (the stationary depth law) — the rigorous target is now sharp: **extract a KL-style lower bound (`x^c` reachable states, explicit `c`) from a truncated, fully-rigorous core of this supercritical system.** The `50%` margin at the bottleneck suggests meaningful room.

**Remark (what mortality costs).** Dead ends do not throttle the tree. Their entire price is half a door per state — visible in the mass formula as the lone `½` — against `D`-fold door multiplicity and infinite `s`-branching. The classical intuition that "a third of numbers being leaves" might starve the tree is quantitatively false in reduced coordinates.

## 14.6. A rigorous density bound from the door tree

*(Added 2026-07-11. The front's open theorem target, executed at base level. Reference point: Krasikov–Lagarias 2002 [arXiv:math/0205002] prove `π₁(x) > x^0.84` via linear programs over difference inequalities mod `3^11`; earlier milestones Crandall 1978 (first `x^β`), Krasikov 1989 (`0.43`), Wirsching (`0.48`). The result below is numerically far weaker than all but Crandall; its content is the derivation — fully self-contained in the reduced formalism — and the collapse identity that makes it single-type.)*

**Definition (the door tree `𝒟`).** Root: `y = 1` (the door of `(1,1)`). Children of a node `y` (odd, `3 ∤ y`): for each `s` in the parity class of `y` (`s` odd iff `y ≡ 1 mod 3`), the value

```text
y' = (2^(s+1) y − 1) / 3        (always an integer for allowed s),
```

kept when `3 ∤ y'` and `y' > 1`.

**Lemma 14.6.1 (collapse identity).** Every kept `y'` is the designated door of a genuine `F`-predecessor of `y`'s state: if `d = v₃(2^s y + 1) = 1` the child state is `(ω', 1)` with door `2ω' − 1 = y'`; if `d ≥ 2` it is `(ω', d)` with door `2·3^(d−1)ω' − 1 = y'` — *the same formula in both cases*, independent of `d`. (Algebra: both equal `2(2^s y + 1)/3 − 1`. Verified on `13,408` cases, both types, zero failures.)

**Lemma 14.6.2 (triple law).** For any `3` consecutive allowed `s`, the values `2^s y + 1` are `≡ {0, 3, 6} (mod 9)`, one each. (The three values differ by `3·2^s y ≡ 6 (mod 9)` steps, are distinct mod `9`, and all `≡ 0 (mod 3)`.) Consequently the three candidate `y'` are `≡ {0, 1, 2} (mod 3)`, one each: per triple, exactly **two** children are kept (one from a depth-`1` predecessor, one from depth `≥ 2`), and one door dies.

**Lemma 14.6.3 (validity and distinctness).** Every node of `𝒟` is the door of a state backward-reachable from `(1,1)`; hence (Theorem 9.8.3) every node's `T`-orbit reaches `1`. Distinct nodes are distinct integers: a door determines its state (`(ω,1) = ((y+1)/2, 1)` if `y ≡ 1 mod 3`; else `ω, d` recovered from `v₃((y+1)/2)`), states in the backward tree are distinct, and the two door types are separated mod `3`. (Spot-verified: `800` sampled nodes, all reach `1`.)

**Theorem 14.6.4 (density bound).** Let `π̃(X) = #{odd y ≤ X : the T-orbit of y reaches 1}`. Then for all `X ≥ 1`,

```text
π̃(X) ≥ 2^(−3.6) · X^(0.3),
```

and the same argument yields exponent `c` for any `c` with `(2^(−3.415c) + 2^(−5.415c))/(1 − 2^(−6c)) > 1`; the critical value is `c* ≈ 0.3304`.

**Proof.** Each kept child multiplies its parent by exactly `2^(s+1)/3 · (1 − 1/(2^(s+1)y)) < 2^(s + 1 − log₂3)`, so the log-size increment of the branch at `s` is `δ(s) < s − 0.585`. By Lemma 14.6.2, each consecutive triple of allowed `s` (spanning `6` integers) contributes two kept children; placing them adversarially at the two largest slots of each window gives, for the tiling starting at the worst offset `s₀ = 2`, the mass lower bound

```text
mass(c) ≥ Σ_{j≥0} [ 2^(−c(6j+3.415)) + 2^(−c(6j+5.415)) ].
```

At `c = 0.3` the first two windows alone give `1.0502 > 1`, and every child in those windows satisfies `y' < y·2^(11.415)` (corrected 2026-07-12; the earlier `2^(10.5)` was slack in the wrong direction). Renewal induction with `A = 2^(−12c)` and threshold `2^12`; the strict-scale step is guaranteed by child growth `z ≥ (19/15)y`, and the root is handled by its own mass lemma (children `5, 85, 341`; mass `1.0546 > 1` — the `s = 1` self-loop excluded by definition). Node counts convert to distinct odd integers reaching `1` via the unique-parent/distinctness lemma. **The canonical, fully refereed five-lemma proof is paper 2 (`paper/collatz-mirror-v1.tex`, §8); this section is the working summary, constants aligned.** ∎

**Remark (position and the refinement path).** The bound sits between Crandall (1978) and Krasikov's original `0.43` — deliberately: the core uses *one* door per state, *two* children per triple, and adversarial anchor phases. The empirical core already grows at exponent `≈ 0.45`, and the full tree at `≈ 0.98` (14.4). Each discarded resource maps onto a stage of the Krasikov–Lagarias program (their residue systems mod `3^k` = our door residues; their LP = optimizing over our branch inventory), with one structural difference: their difference inequalities *bound* the local branching, while the anchor law `14.2.4` gives it *exactly*. Whether exactness buys anything beyond `0.84` is an open question, addressed by the refinement program in 14.6.5/14.13: multi-door taken alone gives a genuine but small lift (`c* → 0.33515`, 14.6.5); the `3^k`-residue and exact-anchor-phase routes hit a structural obstruction — the collapse map is affine, not multiplicative, so neither a residue nor the anchor propagates to the child without unavoidable precision loss (14.13) — so the question stands open, now with a precise account of what blocks the obvious attack.

## 14.6.5. Multi-door renewal, rigorously (KL–LP refinement, stage 1)

*(Added 2026-07-11, branch `kl-lp`, per `briefs/kl-lp-brief.md`. First stage of the density-refinement program named in the 14.6 remark: reinstate the door multiplicity the single-door core of 14.6 discards.)*

**Lemma 14.6.5.1 (doors are generic nodes).** Lemma 14.6.1 (collapse identity) and Lemma 14.6.2 (triple law) hold for *any* live door `y` of *any* state backward-reachable from `(1,1)` — not only the designated (top or unique) door that the single-door tree of 14.6 follows. Consequently every live door, whatever its position `a` in its own state, generates its own copy of the same branching structure (Lemma 14.6.3's "mass, non-root" applies verbatim to it), and every door value is itself the door of *some* state: `a = v₃(y+1)`, `D − a = v₂(y+1)`, `Ω = (y+1)/(2^(D−a)3^a)` recovers it uniquely. **Verified:** on the exact tree to `ω ≤ 2^14` (12,668 states, 21,169 live doors), the recovery formula is exact with zero collisions and zero recovery failures; on 200 sampled states of depth `≥ 3`, all 342 sampled *middle* doors (`0 < a < D−1`, i.e. doors the single-door tree never visits) have `T`-orbits reaching `1`. This is what licenses crediting a state's extra doors (`a = 1, …, D−2`, all alive by Theorem 14.5.1) as *additional, disjoint* subtrees rather than as a heuristic add-on.

**Lemma 14.6.5.2 (exact ternary ledger).** For any live door `y` and any window of `3^k` consecutive admissible `s`, the count with `d' = j+1` (equivalently `v₃(s − M₃(y)) = j`) is *exactly* `2·3^(k−1−j)` for `j = 0, …, k−1`, and exactly one `s` in the window has `d' ≥ k+1`. This is a deterministic count (zero variance across `y`), not the measured/heuristic ledger of 14.2.4's remark — it follows from the ultrametric identity `v₃(a+b) = min(v₃(a),v₃(b))` when the valuations differ, applied to the admissible sub-progressions of `s` (step `2·3^j` within a fixed residue mod `3^j`). **Verified:** 251 random `y` × `k ∈ {2,3,4}` = 753 windows, exact-count check at every level `j` plus the single deep-tail count, zero failures.

**Theorem 14.6.5.3 (multi-door lift).** Crediting, at every node whose predecessor state has depth `d' ≥ 3`, the guaranteed-alive door `a = 1` (and more generally `a = 1, …, d'−2`) as an extra disjoint subtree — each such extra door of size `y'' ≈ z/1.5^(d'−1−a)` relative to its state's designated door `z` — raises the rigorous critical exponent from `c* ≈ 0.3304` (Theorem 14.6.4) to

```text
c* ≈ 0.33515.
```

Concretely, `π̃(X) ≥ A·X^0.33` for an explicit constant `A`, via the same renewal induction as 14.6.4 (Lemma renewal), using a window of the first 27 admissible `s` (three nested levels of the ternary structure of Lemma 14.6.5.2) to reach worst-case mass `1.0232 > 1` at `c = 0.33`; every credited node (designated or bonus) exceeds its parent by a comfortable margin (worst case `log₂(y''/y) ≥ 16.8`), so the induction's strict-decrease step holds without modification.

**Proof.** The worst-case mass computation extends Lemma mass (paper §8 / 14.6's Lemma 14.6.mass) via the rearrangement principle already used there ("any true placement dominates it termwise"), applied recursively through the exact nesting of Lemma 14.6.5.2: at each level, the branch that continues to greater depth is provably worth at least as much as either terminating branch (it inherits, self-similarly, the same lower bound one level down, plus the accruing bonus), so the worst case places it at the largest offset of its triple; the closed-form recursion is evaluated in `experiments/density_lp.py`, function `total_mass`, which reproduces the *known* `c* = 0.3304` exactly when the bonus is switched off (sanity check) and finds `c* = 0.33515` with it on. ∎

**Honest assessment.** The lift is real and rigorous but small: multi-door credit, taken alone and worst-case, is a weak resource — deep (bonus-bearing) events are geometrically rare (`3^(−j)`) and the guaranteed-alive doors they unlock are the *smallest* fraction of the extra multiplicity (mortality of `a = 0` was already priced into 14.6.4's baseline via the triple law; the new resource is only `a = 1, …, D−2`). This falls well short of Krasikov's `0.43`, so per the brief's queue the program proceeds to stage 2 (residues mod `3^k`, as an LP) rather than stopping here. A structural obstruction surfaced along the way and is recorded for stage 3: the child's own anchor `M₃(y')` is **not** a simple function of the parent's `M₃(y)` and `s` — the collapse map `y ↦ (2^(s+1)y−1)/3` is affine, not multiplicative, so `M₃`'s affine-log identity (14.2.3) does not propagate through it. This is why a *stationary*, fixed-precision residue-class transition (mod `3^k`, exact across generations) is not available for free; any residue-class LP must either accept one digit of precision loss per generation (KL's own posture) or treat each new node as "fresh" as this stage does.

Code: `experiments/density_lp.py` (checks A, B, C).

## 14.7. Digit-determinacy: the 3-adic mirror

Paper Theorem 3.5 (`thm:deltaM`) is proved by chaining three digit-determinacy facts (a)–(c) about `N(u)`, `C`, `ω_next`. Their mirrors, in the notation of 14.1–14.2 (door `y`, branch `s`, `N = 2^s y + 1`, predecessor `(ω,d)`, `d = v₃(N)`, `ω = N/3^d`):

**Proposition 14.7.1 (mirror digit-determinacy facts).**

```text
(a')  M₃(y) mod 3^k        is determined by  y mod 3^(k+1),
(b')  N     mod 3^q        is determined by  y mod 3^q  and  s mod 3^(q−1)  (parity of s fixed by y mod 3),
(c')  ω = N/3^d mod 3^r    is determined by  N mod 3^(d+r)  and  d  (exact division).
```

**Proof.** (a') `2` is a primitive root mod `3^(k+1)` (order `2·3^k`), so `2^t mod 3^(k+1)` determines `t mod 2·3^k`, i.e. both `t`'s parity and its `Z₃`-truncation mod `3^k`; `y mod 3^(k+1)` determines `−1/y mod 3^(k+1)`, hence `t = M₃(y) mod 3^k`. (b') restricted to the fixed-parity coset of exponents, `2`'s effective order mod `3^q` is `3^(q−1)`, so `2^s mod 3^q` is determined by `s mod 3^(q−1)`; `y` enters `N` linearly. (c') dividing `N` by `3^d` to get a residue mod `3^r` is exact division *within the same prime* — no analogue of a generator-order fact is needed. ∎

**Theorem 14.7.2 (mirror of Thm 3.5).** For every window depth `W` and target `r`: given `y mod 3^(W+1)` and `s mod 3^W`, if `ε := (s − M₃(y)) mod 3^W` is nonzero, then `d = 1 + v₃(ε)` is exact; and if `W ≥ d + r`, the *same* truncations of `y, s` (via (a')–(c'), chained exactly as Thm 3.5 chains (a)–(c)) determine `ω mod 3^r`.

**Finding — the missing cross-prime step (this *is* the honest mirror, not a gap).** Forward's fact (c) needs the order of `3` mod `2^r` because `ω_next` is obtained by dividing a *2-adically analyzed* quantity `C` by a `3`-power — a genuine cross-prime removal. Backward's (c') needs no such fact: `N = 2^s y + 1` is odd by construction (`y` odd, `2^s y` even), so there is never a `2`-power to strip; the only removal, `3^d`, is same-prime relative to the `3`-adic residue being computed. The backward digit flow has one fewer cross-prime step than the forward one — a real structural asymmetry, not a forced analogy.

**Verification.** Facts (a'), (b'), (c'): 3,000 random checks each, zero failures. Theorem 14.7.2, window-only (generous `W = d+r+2`): `r ∈ {1,3,6}`, ≈2,670 checks each, zero failures. Code: `experiments/mirror_dual.py`.

## 14.8. The top-door anchor increment law, and the frozen case identified

Paper Theorem 3.5 also gives `ΔM = M(ω_next) − M(ω)`, the 2-adic anchor increment across a forward step — a *total* function of the state. Its backward mirror tracks the 3-adic anchor of *doors*, not cores, across a backward step.

**Definition 14.8.1.** For a state `(κ,K)`, write `y₀(κ,K) = 2^K κ − 1` for its `a=0` representative (the mortal door of 14.5.1). Given `(Ω,D)`, door `y = y₀(Ω,D)` (alive), branch `s`, predecessor `(ω,d)` (14.1.1): write `y' = y₀(ω,d) = 2^d ω − 1` for the predecessor's own top door.

**Theorem 14.8.2 (graded increment law, mirror of Thm 3.5's `ΔM`).** Whenever `y'` is alive, `ΔM₃ := M₃(y') − M₃(y) mod 3^k` is determined by, and explicitly computable from, `y mod 3^(d+k+1)` and `s mod 3^(d+k)` — chaining 14.7.1 with one further fact, `2^d mod 3^(k+1)` determined by `d mod 2·3^k` (order of `2` mod `3^(k+1)`), where `d` is already exact from the same window.

**Theorem 14.8.3 (the freeze, identified).** `ΔM` is total — Theorem 3.5 never fails, because `ω_next` always exists. `ΔM₃` is *partial*: it is undefined exactly when `y'` is dead, i.e. (Theorem 14.5.1) `2^d ω ≡ 1 (mod 3)`. **This is the mirror the brief asked to identify:** the forward low-order law has no failure mode; the backward one has a hard, discrete, exactly-characterized failure mode — door mortality — occurring on exactly half of all top-door lineages. Forward orbits under `F` never die; backward top-door lineages sometimes do, and the increment law inherits that asymmetry exactly, rather than the "frozen digit" phenomenon of the ladder (15.3) or the trichotomy (14.9) that were the brief's other candidates — both of those turn out to be soft (more window resolves them); mortality is hard (no window helps; the branch is simply absent).

**Verification.** 6,000 random `(Ω,D,s)` trials: 965 alive / 988 dead, freeze rate `0.5059` (vs. Theorem 14.5.1's exact `1/2`, consistent); window-only recovery of `ΔM₃ mod 3^5` on all 965 alive cases, zero failures. Code: `experiments/mirror_dual.py`.

## 14.9. The one-step dichotomy (not a trichotomy)

**Theorem 14.9.1 (mirror of Thm 3.6, `thm:onestep`).** From a depth-`K` window (`y mod 3^(K+1)`, `s mod 3^K`) alone: either `ε := (s − M₃(y)) mod 3^K` is nonzero, in which case the predecessor's depth `d = 1 + v₃(ε)` is exact with no error; or `ε = 0`, in which case the window honestly reports `d ≥ K+1` — never wrong. The undecided rate is `≈ 3^(−K)`.

**Finding — trichotomy collapses to dichotomy.** Forward's valuation law genuinely splits: six of eight residue classes fix `s ∈ {1,2}` as a class constant at *zero* window cost, and only the two lifting classes need the window — three runtime outcomes (non-lifting-decided / lifting-decided / lifting-undecided). Theorem 14.2.4 is unconditional: `d = 1 + v₃(s − M₃(y))` holds for *every* alive door and valid `s`, with no shortcut class (consistent with the ledger `P(d=j) = 2·3^(−j)` being a genuine geometric law, not "most classes get a fixed answer"). The mirror trichotomy genuinely degenerates to a dichotomy — decided/undecided, no free third branch — because `(Z/3^q)^*` is cyclic (generated by `2`, no split), unlike `(Z/2^q)^*` which has the extra `Z/2` factor that gives forward's six non-lifting classes their zero-cost constants.

**Verification.** `K ∈ {2,4,6,8}`, ≈13,200 trials each: zero decision errors at every `K`; undecided rate close to `3^(−K)` (`0.108` vs `0.111` at `K=2`; `0.00083` vs `0.00137` at `K=6`; `0.00008` vs `0.00015` at `K=8`); zero deep-bound violations (every "undecided" case has true `d > K`). Code: `experiments/mirror_dual.py`.

## 14.10. The dual ladder: predecessors at adjacent branches, fixed door

Ladder.md §15 relates `(ω,d)` and `(ω,d+1)` — same core, adjacent depth. The mirror fixes a door `y` and relates predecessors at adjacent branches `s` and `s+2` (the forced step: `s` is confined to one parity by 14.1.1, so `s+1` is not a valid branch).

**Theorem 14.10.1 (ladder dichotomy).** Write `N(y,s) = 2^s y + 1 = 3^d ω`. Then

```text
N(y, s+2) = 4·N(y,s) − 3,
```

and this forces:

```text
d(y,s) = 1   ⟹   ω(y,s+2) = T₃(ω(y,s)),   d(y,s+2) = 1 + v₃(4ω(y,s) − 1),   where T₃(ω) := (4ω−1)/3^(v₃(4ω−1)),
d(y,s) ≥ 2   ⟹   ω(y,s+2) = 4·3^(d−1)·ω(y,s) − 1   exactly,   and   d(y,s+2) = 1   exactly.
```

**Proof.** `N(y,s+2) = 2^(s+2)y + 1 = 4(2^s y) + 1 = 4(N(y,s) − 1) + 1 = 4N(y,s) − 3`. Write `N = 3^d ω`; `v₃(4N) = d` (`4` a `3`-adic unit), `v₃(3) = 1`. If `d ≠ 1`: no valuation collision, so `v₃(N') = min(d,1) = 1` by the ultrametric inequality, forcing `N'/3` coprime to `3`; and `N'/3 = 4N/3 − 1 = 4·3^(d−1)ω − 1` exactly, giving the `d ≥ 2` branch (this also covers `d=0`, impossible for a valid state). If `d = 1`: `N = 3ω`, so `N' = 3(4ω − 1)`, a genuine collision — `v₃(N') = 1 + v₃(4ω−1)` and `ω(y,s+2) = (4ω−1)/3^(v₃(4ω−1))`, the `T₃` branch. ∎

**Finding — the gate, and the forced step.** The pivot `d=1` vs `d≥2` is exactly Theorem 14.2.4's own first digit: `d=1` iff `v₃(s − M₃(y)) = 0`. As the brief anticipated, the dual ladder's tear-line is gated by the 3-adic anchor, exactly mirroring the forward ladder's tear-line being gated by `s(ω,d)=1` via the 2-adic anchor `M(ω)`. The coefficient `4` (not forward's `3`) is not a broken mirror: it is `2^2`, forced by the step size `2` (not `1`) that the parity condition of 14.1.1 imposes on `s` — the ladder's "unit step" is a lattice-of-index-2 step here, a direct and expected consequence of already-proved structure, not a new asymmetry.

**Verification.** 30,000 random `(y,s)` trials (19,992 valid after the `3∤y` filter): 13,445 in the `d=1`/`T₃` branch, 6,547 in the `d≥2`/affine branch, zero failures in both. Code:

## 14.11. Scope and standing

Backward reachability of every valid state from `(1,1)` is *identical* to the Collatz conjecture (Theorem 9.8.3) — this front offers no discount on the hard part, and per the digit-budget principle its unbounded-depth content is the same as the forward front's (3-adic digits now, rather than 2-adic). What it adds: the exact dual machinery (every forward theorem should be checked for a mirror — dual windows, dual trichotomy, dual increment law are unexplored), and the density program, which is the one place where the classical literature's rigorous partial results (KL exponents) might be sharpened by an exact local law. Stopping rule, inherited: work here must produce either mirror theorems or the multi-type renewal equation; exponent-grinding without the equation is not progress.

*(14.7–14.10 close the "dual windows, dual trichotomy, dual increment law" item above: every forward per-step theorem of paper §3 (`sec:anchor`) now has a proved, verified 3-adic mirror.)*


## 14.12. Steering laws (back-ported from paper 2, §7)

Fix a live door `y` and sweep the admissible `s`. Proofs in `paper/collatz-mirror-v1.tex` §7; verification: `experiments/steering.py`.

**Theorem 14.12.1.** (i) *Depth: total control* — branches with `d = d*` have exact density `2·3^(−d*)` (the ledger). (ii) *2-adic residues: frozen* — for admissible `s ≥ k`, the predecessor satisfies `ω ≡ 3^(−d) (mod 2^k)`; direct 2-adic steering is impossible beyond the finitely many small-`s` branches. (iii) *Forward-anchor placement* — for admissible `s ≥ 3`, `M(ω) ≡ d (mod 2^(s−2))`, with the valuation `v₂(M(ω) − d) = s − 2` sharp. (Verified: 1,321 + 2,025 checks, zero failures, sharpness attained.)

**Corollary 14.12.2 (placement).** For every `k` and target residue `ρ mod 2^k` there are infinitely many admissible `s` whose predecessor has `M(ω) ≡ ρ (mod 2^k)`: choose `d* ≡ ρ (mod 2^k)`, then use (i) to find infinitely many `s ≥ k+2` with `d = d*`, and apply (iii).

**Remark 14.12.3 (synthesis: one identity, two readings).** Unwound, (iii) is *the forward valuation law itself* — `ω3^d = 1 + 2^s y` is the exit equation, so `v₂(M(ω) − d) = s − 2` is exactly `s = 2 + v₂(d − M(ω))` (stage1/paper 1) encountered from the other end of the step. Forward, the state is given and the law reveals `s`; backward, `(y, s)` is chosen and the law places `d` — and with it the predecessor's anchor residue. The bridge problem (stage4.md, 11.8.5.6) is thus bracketed on a third side: the anchor walk that is unsolved forward is, by this reading, *placeable* in reverse.

## 14.13. The KL–LP refinement, stages 2–3: an obstruction, precisely recorded

*(Added 2026-07-11, branch `kl-lp`, per `briefs/kl-lp-brief.md`. Continues 14.6.5's stage 1. Per the brief's stop criterion, this section records a precise obstruction rather than a further theorem: the residue-mod-`3^k` LP and the exact-anchor-phase refinement were both attempted; neither could be brought to a verified, sound result within this session, and the reason is structural, not a matter of more grinding.)*

**The target.** Stage 2 asks for a genuine linear program over door residues mod `3^k` (variables = per-residue branch masses, constraints = the exact local branching relations, solved with a real solver), in the spirit of Krasikov–Lagarias's mod-`3^11` system. Stage 3 asks whether folding in the *exact* anchor law `14.2.4` (as equality constraints, where it pins a phase) beats a Krasikov–Lagarias-style inequality treatment.

**What was tried, and what broke.**

1. *Naive stationary residue tracking.* First construction: states = `y mod 3^k`; transition for admissible `s` computed directly from a `k`-digit representative, claiming the child's *full* `k`-digit residue is representative-independent whenever `d = v₃(N) < k`. This is **false** and was caught by an explicit counter-check (3,120 transitions tested against varied higher digits of `y`, 2,279 failures) — the correct statement (re-derived and verified with zero failures over 4,160 checks) is that a parent known mod `3^k` pins the child only mod `3^(k−d)`: dividing by `3^d` costs exactly `d` digits of precision, and since admissible `s` forces `d ≥ 1` always, **no step is free** — a strictly stationary, same-`k`-forever residue system does not exist. This is the concrete, verified form of the affine-map obstruction flagged in 14.6.5's honest assessment.

2. *Drop-on-overflow.* Second construction: states = `(j, r)` — "known to `j` digits, currently `r mod 3^j`" — with `j` strictly decreasing each step (by `d`) and any transition that would exhaust precision simply dropped (zero credit, a valid but conservative simplification). Because `j` strictly decreases with every edge, the resulting transition graph is a **finite DAG with no cycles** — its spectral radius is identically `0` for every `c`. This construction can never certify supercriticality at *any* exponent; it is mathematically correct but useless (confirmed directly: bisection collapses to the search floor for every `k` tried, 1–6).

3. *Generic fallback credited at weight 1.* Third construction: same `(j,r)` states, but instead of dropping an exhausted-precision transition, credit it at weight `1` (as if the child trivially satisfies `f(child,X) ≥ (X/child)^c`) and solve the resulting acyclic system bottom-up. This produces attractive-looking numbers (`k=2`: `c*≈0.41`; `k=3`: `c*≈0.50`; `k=6`: `c*≈0.57`, still climbing) — **but the construction is unsound**: crediting weight `1` unconditionally is only valid once the *accumulated size* from the true root has already crossed the renewal threshold (Lemma renewal's actual base case, paper §8), not merely once residue precision runs out. Precision exhaustion and size-threshold crossing are different events — a child can run out of tracked digits while still being small relative to `X` — and the construction conflates them. No fix was found and verified in-session; **these numbers are not claimed**, only recorded so the trap is not walked into twice (precedent: 14.4's discarded single-type renewal equation).

**Diagnosis.** All three failures trace to one fact, first surfaced in 14.6.5: the collapse map `y ↦ (2^(s+1)y − 1)/3` is *affine*, not multiplicative, so neither the anchor `M₃(y)` nor a truncated residue `y mod 3^k` propagates to the child without irreducible loss (exactly `d` digits per step, `d ≥ 1` always). Krasikov–Lagarias do not face this: their difference-inequality system tracks the map's residue behavior directly, without an analogue of our door/collapse structure, and — per 14.6.5 — their inequalities *bound* branching where our anchor law would give it *exactly*, but exactness only helps if it can be carried forward, and here it provably cannot be carried forward for free. (This precision loss is the reverse face of the forward digit budget, stage4.md 11.8.7.7; both are consolidated as the **core-extraction deficit** in §16, `bridge.md` — one phenomenon under `2↔3`.)

**Answering the 14.6 remark's open question.** *Whether exactness buys anything beyond `0.84`* is not resolved in the affirmative by this program: the one avenue that would have delivered it (a stationary exact-residue LP exploiting `14.2.4`) is obstructed by the precision loss above. The multi-door resource (14.6.5) is exact and does compose, and it buys a real but small lift. Whether a *correctly* size-threshold-coupled version of construction 3 recovers real gains from residues remains open — it is a well-defined technical question (couple the DAG in `(j,r)` to the outer renewal induction's own accumulated-offset variable, rather than crediting exhaustion for free) but was not resolved here.

**Status.** Primary success bar (`c > 0.43`, Krasikov 1989) **not reached** as a verified theorem. Stage 1 (14.6.5) stands as the session's one verified gain: `c* : 0.3304 → 0.33515`. Stages 2–3 close with the obstruction above, precisely stated, per the brief's equally-valid stop condition. No code from attempt 3 is presented as a result; the diagnostic scripts are not committed (dead ends recorded here in prose, per house norms, rather than as unrunnable/misleading code).

## 14.14. The door/exit seam

*(Added 2026-07-14, branch `door-seam`, per `briefs/door-seam-brief.md`. Prompted by an external suggestion, pre-checked against the live pages before delegation: both the forward anchor increment (stage2.md 11.8.5.6) and the reverse predecessor recovery (14.6.5.1) pass through a single intermediate integer, the exit — equivalently, live door — `y` of a reduced edge. This section makes that coordinate change precise: it re-expresses the forward Bridge increment `ΔM` around `y` (14.14.2), and asks whether the forward reduced map itself, written in door coordinates (14.14.3), carries a total graded law for the 3-adic anchor that the core-extraction step of `16.2` provably cannot (14.14.5). It does — with a genuinely constant offset — and 14.14.6 accounts for where the core-extraction deficit's unbounded-depth content sits once the seam is used. The exit map is a coordinate change on already-proved dynamics, not a new dynamical system; the register below is flat throughout, per the brief's register norm.)*

### 14.14.1. Global edge parameterization

Every reduced edge `(ω,d) → (Ω,D)` (14.1.1) factors through one intermediate integer, its exit `y`, and one further parameter, its exit valuation `s = v_2(3^d ω - 1)`:

```text
3^d ω = 1 + 2^s y                          (exit equation)
y + 1 = 2^m 3^a Ω,   m = v_2(y+1),  a = v_3(y+1),  D = m + a     (door recovery, 14.6.5.1)
```

The first line is `14.1.1`'s defining relation for `x_exit`, restated as an equation in `y`; the second is `14.6.5.1`'s recovery formula, restated with `m := D - a` named. Together they parameterize the edge by `(y, s)` exactly as `14.1`–`14.2` already do — nothing here is a new fact.

**Proposition 14.14.1.1 (dictionary with stage4's `C`).** Let `C = 3^d ω - 1 + 2^s` be stage4.md 11.8.7.2's derived quantity, `σ = v_2(C)`, `a_+ = v_3(C)`. Then

```text
C = 2^s (y + 1),      σ = s + m,      a_+ = a,
```

and the forward core `ω_+ = C / (2^σ 3^{a_+})` equals the recovered `Ω` above — i.e. `ω_+ = Ω`, the same integer both routes name.

**Proof.** From the exit equation, `3^d ω - 1 = 2^s y`, so `C = 2^s y + 2^s = 2^s(y+1)`. Since `2^s` is a `3`-adic unit and coprime to the odd factor structure of `y+1`, `v_2(C) = s + v_2(y+1) = s + m` and `v_3(C) = v_3(y+1) = a`. Substituting the door-recovery line, `C / 2^σ = 2^s(y+1)/2^{s+m} = (y+1)/2^m = 3^a Ω`, so `ω_+ = C/(2^σ 3^{a_+}) = 3^a Ω / 3^a = Ω`. ∎

This is bookkeeping over `14.1.1`/`14.6.5.1` — it is stated once, cleanly, because every later result in this section is phrased in the `(y,s)` coordinates it fixes.

**Verified** — `experiments/door_seam.py`, fresh code, function `test_item1`. `6,000` random reduced steps (`ω < 10^6`, `1 ≤ d < 45`): the exit equation, the door-recovery identity, and all three dictionary equalities (`C`, `σ`, `a_+`) hold exactly in every case, `0` failures (2026-07-14).

### 14.14.2. The door-centred Bridge identity

**Definition 14.14.2.1.** For odd `n`, `J(n) := M(n / 3^{v_3(n)})`. This is well-defined for *every* odd `n`, not only `n` coprime to `3`: `M(ω) = N(ω^2)` (stage2.md 11.8.5.6.1) is defined for any odd `ω`, since `ω^2 ≡ 1 (mod 8)` regardless of `ω`'s relation to `3`.

**Lemma 14.14.2.2 (`M` is completely multiplicative, and `M(3) = -1`).** `M(ω_1 ω_2) = M(ω_1) + M(ω_2)` for all odd `ω_1, ω_2`, and `M(3) = -1`.

**Proof.** `M(ω_1ω_2) = N((ω_1ω_2)^2) = N(ω_1^2 ω_2^2) = N(ω_1^2) + N(ω_2^2) = M(ω_1) + M(ω_2)`, using that `N` is a homomorphism on `1 + 8Z_2` (Theorem 11.8.3.7.1) and `ω_1^2, ω_2^2 ∈ 1+8Z_2`. For `M(3)`: `M(3) = N(9)`, and `N(9)` solves `9^n ≡ 9^{-1} (mod 2^k)` for every `k`, i.e. `n = -1` in `Z_2`. ∎

**Corollary 14.14.2.3 (closed form for `J`).** `J(n) = M(n) + v_3(n)`.

**Proof.** Write `n = 3^{v_3(n)} · n'` with `n' = n/3^{v_3(n)}` coprime to `3`. By 14.14.2.2, `M(n) = v_3(n)·M(3) + M(n') = M(n') - v_3(n)`, so `M(n') = M(n) + v_3(n)`, and `M(n') = J(n)` by definition. ∎

**Theorem 14.14.2.4 (door-centred Bridge identity).** For a reduced edge `(ω,d) → (Ω,D)` with exit `y` and exit valuation `s` (14.14.1),

```text
ΔM = J((y+1) / 2^{v_2(y+1)}) − J(1 + 2^s y).
```

**Proof.** By the door-recovery line of 14.14.1, `(y+1)/2^m = 3^a Ω` with `m = v_2(y+1)`, `a = v_3(y+1)`; this integer is already coprime to `3` (its `3`-part is exactly the displayed `3^a`), so `J((y+1)/2^m) = M(Ω)` directly from Definition 14.14.2.1. By the exit equation, `1 + 2^s y = 3^d ω` with `ω` coprime to `3`, so likewise `J(1+2^sy) = M(ω)`. Subtracting, the right side is `M(Ω) - M(ω) = M(ω_+) - M(ω) = ΔM` (14.14.1.1: `ω_+ = Ω`). ∎

**Content and standing.** This relocates the increment `ΔM` — previously stated only as `N((ω_+/ω)^2)`, a function of the *whole next core* — to the mismatch of one fixed operation (`J`, "strip `3`s, then apply `M`") evaluated at the two integers flanking a single door `y`: `1+2^sy` on the incoming side, `(y+1)/2^m` on the outgoing side. This is a reformulation, derived in three lines from `11.8.3.7.1`, `11.8.5.6`, and `14.6.5.1` — not new information about `ΔM`'s unbounded-depth behavior, and it is not presented as such (register warning per the brief, honored here).

**Verified** — `experiments/door_seam.py`, functions `test_item2` and `test_M3_facts`. Bridge identity: `6,000` random reduced steps, `ΔM mod 2^8` computed both directly and via `J(n_1) - J(n_2)`, `0` failures. Supporting facts: `M(3) ≡ -1 (mod 2^12)`, and complete multiplicativity of `M` over `1,000` random odd pairs, `0` failures (2026-07-14).

### 14.14.3. The exit map

**Definition 14.14.3.1 (the exit map `G`).** For a live door `y` (odd, `3 ∤ y`), let `m = v_2(y+1)`, `q = (y+1)/2^m`, and set

```text
G(y) = (3^m q − 1) / 2^{v_2(3^m q − 1)}.
```

Write `state(y)` for the state recovered from `y` by `14.6.5.1` (Ω `= (y+1)/(2^m 3^{v_3(y+1)})`, `D = m + v_3(y+1)`).

**Theorem 14.14.3.2 (three properties of `G`).** For every live door `y`:

1. **Semiconjugacy: `G` semiconjugates to `F` via `state`.** `state(G(y)) = F(state(y))`. Since `state` is many-to-one and constant on `G`'s fibers (property 2 below), this is a *semiconjugacy*, not a strict conjugacy: `G` is an extension of `F` — the doors of a state form a fiber that `G` collapses, one step later, into the fiber of the next state, and `F` is exactly the map `G` induces on the quotient by "same state." That one-step fiber collapse is part of the structure, not a defect. In particular `G` is not a new dynamical system: it is the reduced map `F`, read in door coordinates.
2. **Fiber-constancy.** If `y, y'` are two of the `D` doors of the same state (`state(y) = state(y') = (Ω, D)`), then `G(y) = G(y')`.
3. **Totality and live image.** `G(y)` is always defined, and `3 ∤ G(y)` — `G` maps live doors to live doors.

**Proof.** Write `(Ω, D) = state(y)`, so `y + 1 = 2^m 3^a Ω` with `a = v_3(y+1)`, `D = m+a` (14.6.5.1), hence `q = (y+1)/2^m = 3^a Ω` and `3^m q = 3^{m+a} Ω = 3^D Ω` — **independent of `a`**, which is (2): every door of `(Ω,D)` shares one `q`-image `3^m q = 3^D Ω`, so `G` is constant on the fiber. Now `3^D Ω - 1` is exactly the numerator `A` of the forward step from `(Ω, D)` (stage4.md 11.8.7.2, with `s' := v_2(A)`), so `G(y) = A / 2^{s'}` is the exit value of the forward step `(Ω,D) → F(Ω,D)` — this is (1), since the exit value of a step is by construction a live door of the state it leads to (`14.1.1`, `14.6.5.1`'s recovery formula applies to it), giving `state(G(y)) = F(Ω,D)`. For (3): `D ≥ 1` for every valid state, so `3^D Ω ≡ 0 (mod 3)`, hence `A = 3^DΩ - 1 ≡ 2 (mod 3)`. Since `2^{s'} G(y) = A ≡ 2 (mod 3)` and `2^{s'}` is a unit mod `3`, `G(y) ≡ 2 · (2^{s'})^{-1} ≢ 0 (mod 3)`. `G(y)` is a finite integer for every live door because `A = 3^DΩ - 1 > 0` is a nonzero even number, so `v_2(A)` is finite — totality. ∎

**Content.** `G = E ∘ R` in the brief's notation: `R` is the reduced map `F` and `E` extracts the exit door of the resulting state; Theorem 14.14.3.2(1) makes precise that this composite, read on the door coordinate alone, needs no reference to `(Ω,D)` at all — a fact used throughout `14.14.4`–`14.14.6`. Property (3) sharpens `14.8.3`'s door-mortality freeze (a *partial* backward increment law) by contrast: the top-door lineage of `14.8` dies on exactly half of all cases, but the forward exit map `G` is total and its image is always live — there is no freeze in this direction, because `D ≥ 1` alone forces it, with no further condition on `Ω`.

**Verified** — `experiments/door_seam.py`, function `test_item3`. `5,561` random live doors of random valid states (`Ω < 10^5`, `1 ≤ D < 30`): totality, live image, `state(G(y)) = F(state(y))`, all `0` failures; fiber-constancy (a second, independently sampled door of the same state, `D ≥ 2`), `5,212` pairs, `0` failures (2026-07-14).

### 14.14.4. The fixed-stratum affine/contraction law

For a live door `y`, write `m = v_2(y+1)` and `r = v_2(3^m q - 1)` (`q = (y+1)/2^m`) — so `r` is exactly the exit valuation `s'` of `14.14.3`'s proof, and `(m, r)` is the **stratum** of `y`.

**Theorem 14.14.4.1 (affine law on a fixed stratum).** On the set of `y` with given `v_2(y+1) = m`, `G` extends to a map affine over `Z_3`:

```text
G(y) = 3^m 2^{-(m+r)} · y + (3^m − 2^m) · 2^{-(m+r)}      (as an identity in Z_3, on the stratum with exit valuation r),
```

with multiplier `3^m 2^{-(m+r)}` of exact `3`-adic valuation `m`, computable from the fixed data `(m,r)` alone. Consequently, for `y, z` on the same `(m,r)`-stratum,

```text
v_3(G(y) − G(z)) = v_3(y − z) + m.
```

**Proof.** `G(y) = (3^m(y+1)/2^m - 1)/2^r = (3^m(y+1) - 2^m)/2^{m+r}` directly from Definition 14.14.3.1, which is affine in `y` with the stated coefficients; `2^{m+r}` is a unit in `Z_3` (coprime to `3`), so both coefficients are honest elements of `Z_3`, and `3^m 2^{-(m+r)}` has `v_3 = m` exactly (`2^{-(m+r)}` is a unit). For `y, z` on the same stratum, subtracting gives `G(y) - G(z) = 3^m 2^{-(m+r)}(y-z)`, so `v_3(G(y)-G(z)) = m + v_3(y-z)`, using that `v_3(u·x) = v_3(x)` for any `3`-adic unit `u`. ∎

**Content.** `G` restricted to a stratum is not merely bounded or Lipschitz in the `3`-adic metric — it is an honest affine contraction of exact ratio `3^{-m}`, gaining exactly `m` digits of `3`-adic agreement per application. This is the precise opposite of the core-extraction deficit's forward accounting (`16.2`: knowing `ω` to `2^{σ+r}` pins `ω_+` to only `2^r`, a *loss* of `σ` digits): here the exit map *gains* `m` digits, because its only arithmetic operations on `y` are multiplication by `3^m` (adds digits) and division by a power of `2` (a `3`-adic unit operation, costing nothing `3`-adically). No contradiction with `16.2`, since `G` never extracts a coprime core — that is exactly what `14.14.3`(3) already established (`G`'s image needs no stripping). The gain is not quoted as progress on its own; `14.14.6` prices what it costs.

**Verified** — `experiments/door_seam.py`, function `test_item4`. `4,000` random pairs `(y,z)` matched to a common `(m,r)`-stratum by rejection sampling (`35,870` draws), `y, z < 10^7`: `v_3(G(y)-G(z)) = v_3(y-z) + m` exactly in every case, `0` failures (2026-07-14).

### 14.14.5. A total graded law for the 3-adic anchor along forward orbits

**Definition 14.14.5.1.** `ΔM_3(y) := M_3(G(y)) − M_3(y)`, for a live door `y`. This is total on live doors (14.14.3(3) makes `G(y)` always a live door, so `M_3(G(y))` is always defined) — unlike `14.8`'s top-door increment, which is undefined exactly when the top door of the predecessor is dead (`14.8.3`, rate `1/2`).

**Lemma 14.14.5.2 (affine-log form).** `ΔM_3(y) = −log_2(G(y)/y)`, meaning: `2^{ΔM_3(y)} = y/G(y)` in the exponent group `E_3` of `14.2.2`.

**Proof.** By Definition 14.2.2, `2^{M_3(y)} = −1/y` and `2^{M_3(G(y))} = −1/G(y)`; dividing, `2^{M_3(G(y)) − M_3(y)} = y/G(y)`. ∎

**Theorem 14.14.5.3 (graded `ΔM_3` law, constant offset).** Fix `k ≥ 1`. On every stratum `(m,r)`, the truncation `ΔM_3(y) mod 3^k` is determined by, and explicitly computable from, `y mod 3^{k+1}` together with the stratum labels `(m,r)` — an offset `f(m,r) ≡ 1`, independent of both `m` and `r`.

**Proof.** By fact `(a')` (`14.7.1`), `M_3(y) mod 3^k` is determined by `y mod 3^{k+1}`, with no reference to any stratum. Apply the same fact to `G(y)`: `M_3(G(y)) mod 3^k` is determined by `G(y) mod 3^{k+1}`. By `14.14.4.1`, on the `(m,r)`-stratum `G(y) ≡ 3^m U y + c_0 (mod 3^{k+1})` for the stratum constants `U = 2^{-(m+r)}`, `c_0 = (3^m − 2^m)U` (both computable from `(m,r)` alone, reduced mod `3^{k+1}`); since `3^m U y mod 3^{k+1}` depends on `y` only through `y mod 3^{max(k+1−m,\,0)}`, and `k+1−m ≤ k+1`, `G(y) mod 3^{k+1}` is determined by `y mod 3^{k+1}` and `(m,r)` — with room to spare when `m > 0`. Combining, `ΔM_3 mod 3^k = (M_3(G(y)) mod 3^k) − (M_3(y) mod 3^k) mod 3^k` is determined by `y mod 3^{k+1}` and `(m,r)`. ∎

**Tightness.** The bound `y mod 3^{k+1}` cannot be relaxed to `y mod 3^k`: the `M_3(y)` term alone already needs the full `3^{k+1}` (fact `(a')` is tight — `2` is a primitive root mod `3^{k+1}`, order exactly `2·3^k`, so the discrete log is not determined by one fewer digit), and this requirement passes through to `ΔM_3` unweakened, since the `G(y)` term needs *fewer* digits, never more.

**Content — the decision point, resolved.** `ΔM_3`, restricted to the door coordinate, obeys the graded law the brief asked for, in the mold of `14.8.2` and `11.8.7.3.1` — but with one structural difference worth recording plainly, not as a claimed advance: both of those laws need a modulus that *grows* with the stratum (`3^{d+k+1}` in `14.8.2`, `2^{σ+k+2}` in `11.8.7.3.1`), because both track a step that extracts a coprime core and so *loses* digits proportional to the extracted valuation. Here the offset is the constant `1` at every stratum, because `G` never extracts a core (`14.14.3`(3)) and is an honest affine map on the door coordinate (`14.14.4.1`) — applying `G` costs no extra `y`-precision beyond what computing `M_3(y)` itself already spends. This is a direct corollary of `14.14.4`'s contraction property, not an independent discovery, and `14.14.6` is where its cost is priced rather than left as a free gain.

**Verified** — `experiments/door_seam.py`, functions `test_item5_offset` and `test_item5_deep_strata`. Graded law at offset `f=1`, `K ∈ {2,4,6,8}`: `250` base points and `1,250` lifted pairs per `K` (each pair shares `y mod 3^{K+1}` and the `(m,r)`-stratum with its base point, differs by a large multiple of `3^{K+1}·2^{m+r+10}`), `0` failures at every `K`. Deep-stratum stress test, `m ∈ {1,5,10,15,20}` forced by construction, `K=4`: `120` base points each, `0` failures — the constant offset holds even at large `m`. Tightness: the same test at offset `f=0` (`y` known only mod `3^K`), `K=5`: `1,250` pairs, `873` failures, confirming `f=1` is not slack (2026-07-14).

**Theorem 14.14.5.4 (the total two-case metric law).** *(Added 2026-07-15, branch `block-map`, per `briefs/block-map-brief.md`, item 3 — a strengthening of the tightness paragraph above, which stands and is not being repaired.)* For live doors `y, z` on the same `(m,r)`-stratum (`14.14.4`), `y ≠ z`:

```text
(i)  v_3(z−y) = 0   ⟺   ΔM_3(z) − ΔM_3(y) is odd (the parity component in E_3);
(ii) v_3(z−y) ≥ 1   ⟹   the difference is even, and
     v_3(ΔM_3(z) − ΔM_3(y)) = v_3(z−y) − 1   exactly.
```

**Proof.** Put `H(u) = u/G(u)`, so `2^{ΔM_3(u)} = H(u)` for every live door `u` (Lemma `14.14.5.2`). By the affine law `14.14.4.1` on the shared stratum, `G(u) = (3^m(u+1) − 2^m)/2^{m+r}`, so `H(u) = u·2^{m+r} / (3^m u + 3^m − 2^m)`. Hence

```text
H(z)/H(y) − 1 = [z(3^m y+3^m-2^m) − y(3^m z+3^m-2^m)] / [y(3^m z+3^m-2^m)]
              = (3^m − 2^m)(z−y) / [y·(3^m z + 3^m − 2^m)],
```

the `3^m yz` cross-terms cancelling. Rearranging `14.14.4.1` for `z`, `3^m z + 3^m − 2^m = 2^{m+r} G(z)`, so the denominator is `y·2^{m+r}·G(z)`, a `3`-adic unit: `3 ∤ y` (`y` a live door), `3 ∤ G(z)` (`14.14.3.2(3)`), and `2^{m+r}` a unit trivially. Also `v_3(3^m−2^m) = 0` since `m ≥ 1` (`3^m ≡ 0`, `2^m ≢ 0 (mod 3)`). So

```text
v_3(H(z)/H(y) − 1) = v_3(z−y).                                        (*)
```

Write `Δ := ΔM_3(z) − ΔM_3(y) ∈ E_3`, so `H(z)/H(y) = 2^Δ`. Since `H(z)/H(y)` is a `3`-adic unit it is `≡ 1` or `2 (mod 3)`, and `2^Δ ≡ (−1)^Δ (mod 3)` depends only on `Δ`'s parity component: `≡ 1` iff `Δ` even, `≡ 2` iff `Δ` odd. If `v_3(z−y) = 0`, `(*)` gives `H(z)/H(y) ≢ 1`, i.e. `≡ 2`, i.e. `Δ` odd — case (i), and conversely. If `v_3(z−y) ≥ 1`, `(*)` gives `H(z)/H(y) ≡ 1 (mod 3)`, so `Δ` is even; Lemma `14.2.1` — already proved on this page, cited rather than re-derived, exactly the fact the brief asks for (`v_3(2^t−1) = 1+v_3(t)` for even `t`) — applied to an integer representative of `Δ` gives `v_3(2^Δ−1) = 1+v_3(Δ)`, i.e. `v_3(H(z)/H(y)−1) = 1+v_3(Δ)`. Combined with `(*)`, `v_3(z−y) = 1+v_3(Δ)`, i.e. `v_3(Δ) = v_3(z−y)−1` — case (ii). ∎

**Content.** This strengthens the tightness paragraph above from an existence statement (the offset cannot be relaxed below `f=1`) into an exact per-stratum metric law: taking `v_3(z−y)=k` in case (ii) re-derives tightness quantitatively — the offset `1` is not merely un-slack at the sampled points but a local law at every same-stratum pair, with `k=0` exactly the boundary case (i) where one fewer `3`-adic digit genuinely loses the answer.

**Remark (the one-case form).** The two-case statement is the `(parity, v_3)`-coordinate expression of a single unconditional law, not two separate facts. Substituting `H(z)/H(y) = 2^Δ` (`Δ := ΔM_3(z) − ΔM_3(y)`, Lemma `14.14.5.2`) into line `(*)` of the proof above gives, for every `y ≠ z` on a shared stratum,

```text
v_3(2^Δ − 1) = v_3(z − y),
```

with no case split — immediate from `(*)` and `14.14.5.2`, not re-derived. Cases (i)–(ii) are this one identity read off in the coordinates `(parity, v_3) ∈ Z/2 × Z_3` of the exponent group `E_3` (`14.2.2`): a `Z_3`-only reading of the `k=0` level would ask for `v_3(Δ) = −1`, which is meaningless (`v_3` takes values in `{0,1,2,…} ∪ {∞}`, never `−1`), so the parity component of `Δ` is what carries that boundary level instead — case (i)'s "`Δ` odd" is the coordinate that expresses the level a `Z_3`-valuation alone cannot. No mathematical content changes; the single law was already present, in line `(*)`, before the case split. **Verified** — the unified form is exactly what `test_metric_law_algebra` in `experiments/block_map.py` already checked, via `(*)` itself (2026-07-15).

**Verified** — `experiments/block_map.py`, fresh code, functions `test_metric_law_algebra` and `test_metric_law_cases`. Algebraic step `(*)` (exact `Fraction` arithmetic, no anchor computation, no precision truncation): `3,000` same-stratum pairs (`y, z < 10^7`, `27,621` draws by rejection sampling), `0` failures. Full two-case law via a fresh `2·3^K`-modulus anchor computation (`K=10`, tracking both the parity and `Z_3` components of `E_3`): `2,500` same-stratum pairs (`22,272` draws), split `1,250` at `v_3(z−y)=0` (case (i), parity check) and `1,250` at `v_3(z−y) ≥ 1` (case (ii), exact valuation check), `0` failures in either case (seed `15005`–`15006`, 2026-07-15).

### 14.14.6. Reconciliation with the core-extraction deficit

The stratum labels `(m,r)` driving `14.14.4`–`14.14.5` are `2`-adic data about `y`, even though the law they grade is stated `3`-adically. This is the question the brief poses as the mandatory closing step: does the door/exit seam **evade** the core-extraction deficit (`16.2`), or **relocate** it?

**It relocates it, term for term — not evades it.** Two identifications, both already on file rather than newly needed:

- `m = v_2(y+1)` is not merely *analogous* to stage3.md's entry-depth exponent — it is the *same quantity by definition*: stage3.md 11.8.6.3 defines `m_+ = v_2(x_exit + 1)` for the forward step whose exit value is `x_exit`, and `x_exit = y` is exactly `14.1.1`'s exit equation. So the door's `m`-label *is* `m_+`, the `2`-adic half of that same step's digit cost `σ = s + m_+` (stage3.md, stage4.md 11.8.7.2).
- `r`, from the proof of `14.14.3.2`(1), is `v_2(3^DΩ - 1)` — the exit valuation `s` of the *next* forward step, the one from `state(y)` to `state(G(y))`, taken deterministically (forward `s` is not a free branch choice, `14.1`).

So the stratum pair `(m,r)` attached to a door `y` is exactly `(m_+` of the edge whose exit is `y`, `s` of the edge `y`'s state emits`)` — the two labels stage4.md's own digit-cost decomposition `σ = s + m_+` already tracks, read off the two edges meeting at the door. Composing `14.14.5` along a chain of states `(Ω_0,D_0) → ⋯ → (Ω_N,D_N)` via doors `y_0, y_1 = G(y_0), …, y_N = G(y_{N-1})` needs the stratum pair `(m_i, r_i)` at every step `i`; by the identifications above, `r_i` is the `s` of edge `i → i+1` and `m_{i+1}` is the `m_+` of that *same* edge. So each forward edge contributes exactly one `(s, m_+)` pair to the chain's stratum data — split across two consecutive door-steps, but counted once — and summing over `N` edges reproduces `Σ_i (s_i + m_+^{(i)}) = Σ_i σ_i`, stage4.md 11.8.7.7's own accumulated digit cost, exactly, with no double-counting and no term dropped (up to the two boundary labels `m_0, r_N`, which do not grow with `N`).

**The accounting.** `14.14.4`'s "gain" — `G` sharpening `3`-adic agreement by `m` digits per step, in contrast to `16.2`'s forward loss of `σ` `2`-adic digits per step — is real, and it is bought at *exactly* `16.2`'s own price, not a lower one: identifying which stratum a door sits in (the prerequisite for applying `14.14.4`/`14.14.5` at all) costs precisely the `2`-adic digits `11.8.7.7` already prices as consumed and unregenerated. The seam does not touch that supply; it relabels it. What changes is where the *bookkeeping* looks free: the `3`-adic side of the ledger, which used to look like irrecoverable loss in the naive predecessor picture (`14.13`'s affine-collapse obstruction — a parent known mod `3^k` pins the child only mod `3^{k-d}`), is in door coordinates a bounded, even contracting, computation at every single step. But the unbounded-depth content of the Bridge has not shrunk: it now sits entirely and visibly in the `2`-adic stratum-label sequence `(m_i, r_i)_i`, which *is* the forward `(s, m_+)` sequence, term for term. Composing the graded law along an infinite orbit still requires unboundedly much of that sequence, for the same reason `11.8.7.7` already gives: nothing regenerates it.

**Standing.** This is the honest form of "seam versus deficit": the door/exit coordinate change makes the `3`-adic residue tracking *free* — a genuine simplification, and the reason `14.14.5`'s offset is constant where `14.8.2`'s and `11.8.7.3.1`'s are not — but it does so by making visible, rather than by discharging, the `2`-adic cost that `16.2` and `11.8.7.7` already identified as the Bridge's one hard fact. The core-extraction deficit is not evaded by this section; it is relocated onto a single, already-known, already-priced axis, and the diagnostic reach of `16.2` is extended by having a second, independently-derived route (through the forward direction's *own* deterministic exit sequence, rather than through backward branching) land on the identical accounting.

**Closing status.** What this section changed about the Bridge: a working formulation. `ΔM` now has a coordinate (the door `y`) on which it is a mismatch of one fixed operation (`14.14.2`) rather than an opaque function of the next core; the reduced map itself has a door-coordinate presentation (`G`, `14.14.3`) that is total, mortality-free, and — restricted to a `2`-adic stratum — an exact `3`-adic contraction (`14.14.4`) supporting the strongest-graded increment law in the program to date, constant offset rather than growing (`14.14.5`). What it did not change: the Bridge is exactly as open as it was. `14.14.6`'s accounting shows the `3`-adic gain is paid for, in full and exactly, by `2`-adic stratum data identical to the forward digit budget (`11.8.7.7`) already on file — no bounded amount of that data exists along an infinite orbit, for the same reason `11.8.7.7` gives, and the seam supplies no new argument against it. Both halves of the program's stated escape routes — equidistribution (`aeh.md` §13) for typical orbits, rigidity (`11.8.3.11`) for cycles — stand exactly where `bridge.md` §16 left them. Per the brief's stop criterion: this closes items 1–6 at the floor-plus-primary bar (all six proved, item 5 resolved affirmatively rather than obstructed), and per §16.4.6/16.5's own register, no further front is opened from here — no density-exponent computation, no numerical iteration of `G` hunting statistics, no equidistribution proof attempt. If composing `14.14.5`'s law along orbits suggests further structure, that composition is a separate decision for the main session, not continued here.

### 14.14.7. The block-map identity

*(Added 2026-07-15, branch `block-map`, per `briefs/block-map-brief.md`. An interpretation of `G`, not a new fact about it: the exit map is the accelerated Collatz map itself, run for a return time read directly off the door.)*

**Setup.** Let `T(x) = (3x+1)/2^(v_2(3x+1))` be the accelerated odd Collatz map (spine.md §9.8). For a live door `y`, write `m = v_2(y+1)`, `q = (y+1)/2^m` (odd, by definition of `m`), and `r = v_2(3^m q - 1)`, matching `14.14.4`'s stratum labels.

**Theorem 14.14.7.1 (block-map identity).** For `0 ≤ j < m`,

```text
T^j(y) = 3^j 2^(m-j) q − 1,
```

and `T^m(y) = G(y)`. Consequently `G` is the **variable-return-time block map** of `T`: applying `T` to a live door `y` for exactly `m = v_2(y+1)` iterations reaches `G(y)`. The return time `m` is read off the door itself, not defined as a first-hitting time — no minimality claim is made or needed (at the trivial door `y = 1`, the value `G(1) = 1` is already present at step `0`).

The valuation word of the passage — the successive values `v_2(3 T^j(y) + 1)` for `j = 0, ..., m−1` — is

```text
(1, ..., 1  [m−1 times],  r+1),
```

whose sum is `m + r`, matching the power of `2` in the affine law `14.14.4.1`'s denominator `2^(m+r)` — a consistency check between this section and `14.14.4`, not an independent fact.

**Proof.** Write `x_j := 3^j 2^(m-j) q − 1` for `0 ≤ j ≤ m`, so `x_0 = 2^m q − 1 = y` and `x_m = 3^m q − 1`. Directly,

```text
3x_j + 1 = 3^(j+1) 2^(m-j) q − 2 = 2(3^(j+1) 2^(m-j-1) q − 1) = 2 x_(j+1),
```

an identity for every `0 ≤ j ≤ m−1`. For `j ≤ m−2`, the exponent `m-j-1 ≥ 1`, so `2^(m-j-1) q` is even and `x_(j+1) = 3^(j+1) 2^(m-j-1) q − 1` is odd; hence `v_2(3x_j+1) = v_2(2x_(j+1)) = 1`, so `T(x_j) = x_(j+1)` exactly — a single halving. Chaining `j = 0, ..., m−2` gives `T^j(y) = x_j` for `0 ≤ j ≤ m−1`. At `j = m−1`: `x_(m-1) = 2·3^(m-1) q − 1`, and `3x_(m-1)+1 = 2x_m = 2(3^m q − 1)`; since `q` is odd, `3^m q` is odd and `x_m` is even, so writing `r := v_2(x_m) = v_2(3^m q − 1)` (matching `14.14.3`'s own `r`), `v_2(3x_(m-1)+1) = 1+r`, and `T(x_(m-1)) = 2x_m/2^(1+r) = x_m/2^r`, which is exactly `G(y)` by Definition `14.14.3.1`. This gives both `T^m(y) = G(y)` and the valuation word: `1` at each of `j = 0, ..., m−2` (`m−1` entries) and `r+1` at `j = m−1`, sum `(m-1) + (r+1) = m+r`. ∎

**Cross-checks.**

- *Totality and live image, re-derived.* `T` is total on every positive odd integer (`3x+1` is a positive even number for odd `x`, so `v_2(3x+1)` is finite), and it never outputs a multiple of `3`: mod `3`, `3x+1 ≡ 1` and `2^(v_2(3x+1)) ≡ ±1`, so `T(x) ≡ ±1 ≢ 0 (mod 3)` for *every* odd `x`, whether or not `3 | x`. Since `G(y) = T^m(y)` is, by this theorem, the output of an application of `T`, both totality and `3 ∤ G(y)` (`14.14.3.2(3)`) follow again — from a fact about `T` alone, rather than the state-based argument used in `14.14.3`'s own proof.
- *Worked instance.* `y = 7`: `m = v_2(8) = 3`, `q = 1`. `T(7) = 11`, `T(11) = 17`, `T(17) = 13`; valuations `(1,1,2)`, sum `4 = m+r` with `r = 1`; and `G(7) = 13`.

**Remark (relation to the block/cascade decomposition, spine.md §9.1) — clean, not forced.** Write `(Ω,D) = state(y)` (`14.14.1`), so `y+1 = 2^m 3^a Ω` with `a = v_3(y+1)`, `D = m+a` — i.e. `y` is exactly the representative `x_a` of `(Ω,D)`'s own block, in the indexing of Proposition `9.1.1` (`x_a = 2^(D-a) 3^a Ω − 1`; `m = D-a` matches `9.1.1`'s decreasing `m`-index there). Theorem `14.14.7.1`, applied with `q = 3^a Ω`, says exactly that continuing the block from position `a` for its `D-a` remaining steps reaches the block's exit. The special case `a=0` (`y = x_0 = 2^D Ω − 1`) is Proposition `9.1.1` itself, recovered clause for clause: its "forced halving cascade [of] length `s`" is this section's final valuation `r+1`, with `r=s`. So `m` is not merely analogous to a block length; for a general door it is the *remaining* length of the classical block-cascade from wherever `y` sits within it, and `9.1.1`'s fiber-independence of the exit (every representative shares the same exit law) is exactly `G`'s fiber-constancy (`14.14.3.2(2)`), now carrying an explicit iteration count. Both descriptions name the same object; nothing here is an analogy under strain.

**Verified** — `experiments/block_map.py`, fresh code, functions `test_block_map_iterates`, `test_T_general_facts`, `test_worked_instance`, `test_block_remark`; imports nothing from `experiments/door_seam.py` or elsewhere in the repository (AGENTS.md house norm). Block-map identity and valuation word: `6,000` random live doors (`y < 10^6`), `0` failures in the `T^j(y)` formula, `T^m(y)=G(y)`, and the word/sum check. `T`'s own totality and non-`3`-divisibility, tested on `8,000` random odd `x < 10^7` (not filtered to live doors, and not filtered away from multiples of `3`): `0` failures. Worked instance `7 → 11 → 17 → 13` reproduced exactly (`m=3`, `r=1`, word `(1,1,2)`). Block/cascade remark: `3,704` valid random states (`Ω < 10^5`, `1 ≤ D < 25`, random block position `a`), `0` failures in `m=D-a`, `G(y)` matching the state's own `x_exit`, and direct `m`-fold `T`-iteration matching `x_exit` (seed `15001`–`15003`, 2026-07-15).

### 14.14.8. Composition along fixed itineraries

*(Added 2026-07-15, branch `block-map`, per `briefs/block-map-brief.md`, item 4 — the main session's reserved decision from `14.14`'s closing status: composing `14.14.4`'s affine law and `14.14.5`'s graded law along a run of steps that all follow one fixed sequence of strata.)*

**Definition 14.14.8.1 (itinerary).** A door `y` **follows** the itinerary `(m_0,r_0), ..., (m_(n-1),r_(n-1))` if, writing `y_0 := y` and `y_(i+1) := G(y_i)`, the door `y_i` lies on stratum `(m_i,r_i)` for every `i = 0, ..., n-1`.

**Theorem 14.14.8.2 (composed affine law).** On the doors following a fixed itinerary of length `n`, `G^n` is affine over `Z_3`:

```text
G^n(y) = A_n y + B_n,      A_n = Π_(i=0)^(n-1) 3^(m_i) 2^(-(m_i+r_i)),
```

with `B_n` the standard affine-composition constant (`B_0 = 0`; `B_(i+1) = 3^(m_i)2^(-(m_i+r_i)) B_i + (3^(m_i)-2^(m_i))2^(-(m_i+r_i))`), and `v_3(A_n) = Σ_i m_i`. Consequently, for `y, z` both following the itinerary,

```text
v_3(G^n(y) − G^n(z)) = v_3(y−z) + Σ_i m_i.
```

**Proof.** Write `α_i = 3^(m_i)2^(-(m_i+r_i))`, `β_i = (3^(m_i)-2^(m_i))2^(-(m_i+r_i))`, so `14.14.4.1` says `G(u) = α_i u + β_i` for any `u` on stratum `(m_i,r_i)`. Since `y_i` lies on stratum `(m_i,r_i)` for every `i < n` by hypothesis, `y_(i+1) = α_i y_i + β_i` for every step, and the standard induction for composing affine maps (`A_0=1, B_0=0`; `A_(i+1)=α_i A_i`, `B_(i+1)=α_i B_i+β_i`) gives `y_n = A_n y_0 + B_n` by direct substitution. `v_3(A_n) = Σ v_3(α_i) = Σ m_i` since each `2^(-(m_i+r_i))` is a `3`-adic unit. For the difference law: if `z` also follows the itinerary, `y_(i+1)-z_(i+1) = α_i(y_i-z_i)` at every step (the `β_i` term is itinerary-determined, identical for `y` and `z`, and cancels), so by induction `y_n-z_n = A_n(y_0-z_0)`, giving `v_3(G^n(y)-G^n(z)) = v_3(A_n)+v_3(y-z) = v_3(y-z)+Σm_i`. ∎

**Corollary 14.14.8.3 (synchronization).** Fix `k ≥ 0`. Once `Σ_(i<n) m_i ≥ k+1`, the door `y_n mod 3^(k+1)` is the same for every `y` following the itinerary, independent of `y_0` — it equals `B_n mod 3^(k+1)`, computable from the itinerary alone. Consequently `M_3(y_n) mod 3^k` (fact `(a')`, `14.7.1`) and every subsequent increment `ΔM_3 mod 3^k` (`14.14.5.3`) are determined by the stratum word alone. Stated flatly: along any orbit, the `3`-adic anchor's residues at every fixed precision are eventually a function of the `2`-adic stratum word alone.

**Proof.** `y_n = A_n y_0 + B_n`; since `v_3(A_n) = Σm_i ≥ k+1`, `A_n y_0 ≡ 0 (mod 3^(k+1))` for every `y_0` — the congruence holds identically, not merely for doors following this itinerary — so `y_n ≡ B_n (mod 3^(k+1))`. `M_3(y_n) mod 3^k` is a function of `y_n mod 3^(k+1)` by fact `(a')`, hence of the itinerary alone; `ΔM_3(y_n) mod 3^k` likewise, by `14.14.5.3` applied on the (one further) stratum `(m_n,r_n)`. ∎

**Corollary 14.14.8.4 (periodic-word fixed point — with mandatory reconciliation).** For a periodic itinerary of period `n` (`m_i ≥ 1` for every valid door, so `v_3(A_n) = Σm_i ≥ n ≥ 1`), `1-A_n` is a `3`-adic unit, and the affine relation `y = A_n y + B_n` has the unique solution

```text
y* = B_n / (1 − A_n)  ∈  Z_3.
```

If a genuine period-`n` cycle of `G` (an integer live door with `G^n(y_0)=y_0`) carries this stratum word, its door is exactly `y_0 = y*`.

**Sanity instance.** The trivial fixed point `(1,1)`: single door `y=1`, `m=v_2(2)=1`, `q=1`, `G(1) = (3-1)/2 = 1`, `r=v_2(2)=1`, word `(m,r)=(1,1)`. `A = 3·2^{-2} = 3/4`, `B = (3-2)·2^{-2} = 1/4`, `y* = (1/4)/(1-3/4) = (1/4)/(1/4) = 1`. ✓

**Reconciliation with the classical cycle candidate (cycles.md §12.1) — not a new lever.** By Theorem `14.14.3.2(1)` (semiconjugacy), a period-`n` cycle of `G` corresponds, door for door, to a period-`n` cycle of `F` — by `9.8.4`, either the trivial fixed point or a nontrivial `T`-cycle. `14.14.6` already identifies a *single* door's stratum labels with stage3.md/stage4.md's own `(s, m_+)` step data; extended along a full period, `v_3(A_n) = Σ_i m_i` reproduces exactly cycles.md `12.1.1`'s own invariant `n := Σ_t m_t` (same symbol, same quantity, read off the door sequence rather than the state sequence). So `y*` is the door-coordinate incarnation of the same mechanism cycles.md §12.1 uses throughout: periodicity forces an exact affine relation with a unique rational solution — a *candidate*, not a cycle, until checked for integrality and liveness. This is exactly the device `12.2.1` already carries out for period `1` (its own fixed-point equation, in state coordinates) and `12.1.1`'s product equation `2^K = 3^n Π_t(1+ε_t)` carries out in general. Read in door coordinates, this reproduces the classical candidate; it does not sharpen it, and it supplies no divisibility information the classical equation lacks. Per README's stopping rule, the cycle front is parked and reopens only with a divisibility-aware idea beyond this classical candidate — this reconciliation is explicitly not that idea, and no cycle-exclusion attempt is launched from it here.

**Accounting sentence (extending 14.14.6) — to accompany 14.14.8.3 and 14.14.8.4 wherever they are quoted.** The `3`-adic side of the ledger is not merely cheap per step (`14.14.4`–`14.14.5`) but asymptotically *free* along a fixed itinerary: beyond the first `k+1` accumulated `m`-digits, every residue at precision `3^k` is a function of the stratum word alone (`14.14.8.3`) — a sharpening of, not a change to, the relocation verdict of `14.14.6`: the word itself is exactly the forward `(s,m_+)` digit data already priced by stage4.md `11.8.7.7`, and nothing here reduces how much of that word an infinite orbit requires.

**Closing status.** This layer changes nothing about the Bridge. It is a corollary layer on the already-closed seam (`14.14.1`–`14.14.6`): the block-map identity gives `G` its own meaning as `T`'s variable-return-time block map (`14.14.7`); the semiconjugacy has its accurate name (`14.14.3`'s retitled property); `14.14.5`'s tightness has an exact quantitative form (`14.14.5.4`); and the seam's per-step laws now have their composed form along orbits (`14.14.8.2`–`14.14.8.4`) — including the reminder, made explicit rather than left implicit, that the composed fixed point is the classical cycle candidate under a new name, not a new candidate. Both halves of the program's stated escape routes stand exactly where `bridge.md` §16 left them; per the brief's stop criterion, no cycle-exclusion attempt, no stratum-word statistics, no density computation, and no equidistribution proof attempt follow from any of this.

**Verified** — `experiments/block_map.py`, fresh code, functions `test_composed_affine`, `test_composed_difference`, `test_synchronization`, `test_periodic_fixed_point_algebra`, `test_trivial_fixed_point_sanity`. Composed affine law: `1,500` random doors, itinerary length `n=4`, `G^n(y)` compared against `A_n y + B_n` (exact `Fraction` arithmetic) and `v_3(A_n)` against `Σm_i`, `0` failures. Difference law: `800` pairs sharing a length-`3` itinerary (`584,763` draws by rejection sampling), `0` failures. Synchronization: `600` pairs sharing a length-`3` itinerary (`431,680` draws), all with `Σm_i ≥ k+1 = 3` (guaranteed at `n=3`, `k=2`, since `m_i ≥ 1` always), `y_n mod 3^(k+1)` matching both across the pair and against the formula `B_n mod 3^(k+1)`, `0` failures. Periodic-word fixed-point algebra (`A_n y^*+B_n = y^*`, exact `Fraction` identity, for `500` random itineraries of length `1`–`4`, not necessarily from real periodic orbits): `0` failures. Trivial fixed point sanity instance (`y=1`, word `(1,1)`, `A=3/4`, `B=1/4`, `y*=1`): reproduced exactly (seeds `15007`–`15010`, 2026-07-15).

## 14.15. The itinerary language: the cylinder theorem and the two-sided coding

*(Added 2026-07-16, branch `itinerary-coding`, per `briefs/itinerary-coding-brief.md`. The seam `14.14` is closed and its numbering is untouched; this is a new top-level subsection. Prompted by an external suggestion (ChatGPT, 2026-07-16), reviewed against the live pages before delegation. Per the brief's framing mandate: the cylinder theorem below is **not new mathematics about `T`** — it is the classical Collatz coding fact (parity-vector periodicity, Terras 1976 and Everett 1977; the accelerated form standard, Lagarias's surveys, Wirsching) read in the door/`(m,r)` alphabet fixed by the seam, with its consequences for this program's search space stated once (`14.15.2`) and its two-sided `Z_2 × Z_3` extension formulated at the formulation grade the brief sets, with no new leverage on the Bridge (`14.15.3`). The register below is flat throughout, per the mandate.)*

### 14.15.1. The finite-itinerary cylinder theorem

**Definition 14.15.1.1 (stratum, general).** For odd `y > 0`, `m(y) := v_2(y+1)`, `q(y) := (y+1)/2^{m(y)}`, `r(y) := v_2(3^{m(y)} q(y) - 1)`, `stratum(y) := (m(y), r(y))` — the same quantities `14.14.4` names `(m,r)`, defined here for *every* odd `y`, not only live doors: nothing in the definitions of `m`, `q`, `r` uses `3 ∤ y`.

**Remark (well-defined beyond live doors, already on file).** `14.14.3.1`'s formula for `G` uses exactly `m`, `q`, `r` above and likewise needs no coprimality hypothesis; `14.14.7.1` already proves `G(y) = T^{m(y)}(y)` and that `T` is total and never outputs a multiple of `3`, for *every* odd `x`, live door or not (its own cross-check paragraph makes this explicit). So `stratum` and `G` are total on all positive odd integers, and `G`'s output is always a live door regardless of its input's relation to `3`. This section uses that generality throughout: words below are not restricted to sequences of live doors, only their first letter's realizability as an actual chain is (Corollary `14.15.1.7`).

**Definition 14.15.1.2 (word, follower).** A **word** of length `n` is `W = ((m_0,r_0), …, (m_{n-1},r_{n-1}))` with every `m_i, r_i ≥ 1`. An odd integer `y` **follows** `W` if, writing `y_0 := y`, `y_{i+1} := G(y_i)`, `stratum(y_i) = (m_i,r_i)` for every `i = 0, …, n-1`. Write `S(W) := Σ_i (m_i+r_i)`.

**Lemma 14.15.1.3 (single-stratum cylinder and level shift).** Fix `m, r ≥ 1`.

```text
(i)  stratum(y) = (m,r)  iff  y ≡ 2^m - 1 (mod 2^(m+1))  and, writing q=(y+1)/2^m,
                               q ≡ 3^(-m)(1+2^r) (mod 2^(r+1))
     -- equivalently, iff y is congruent to a single fixed residue mod 2^(m+r+1).
(ii) for y with stratum(y) = (m,r), and any integer t,
     G(y + 2^(m+r+1) t) = G(y) + 2·3^m t                                exactly.
```

**Proof.** (i) `v_2(y+1) = m` iff `y+1 = 2^m·(odd)`, i.e. `y ≡ 2^m-1 (mod 2^{m+1})`; this pins `y+1 mod 2^{m+r+1}`, hence `q=(y+1)/2^m mod 2^{r+1}` exactly. `v_2(3^mq-1)=r` iff the coefficient of `2^r` in `3^mq-1` is odd, i.e. `3^mq ≡ 1+2^r (mod 2^{r+1})`, i.e. `q ≡ 3^{-m}(1+2^r) (mod 2^{r+1})` (`3^m` a unit mod `2^{r+1}`). Both conditions together pin `y` to a single residue mod `2^{m+r+1}`.

(ii) Let `y' = y+2^{m+r+1}t`. Since `m+r+1 > m`, `y' ≡ y (mod 2^{m+1})`, so `m(y')=m`, and `q' := (y'+1)/2^m = q+2^{r+1}t`. Write `3^mq-1 = 2^rc` with `c` odd (`v_2=r` by hypothesis); then `3^mq'-1 = 2^rc + 3^m2^{r+1}t = 2^r(c+2·3^mt)`, and `c+2·3^mt` is odd, so `v_2(3^mq'-1)=r` too (consistent with (i)) and `G(y') = (3^mq'-1)/2^r = c+2·3^mt = G(y)+2·3^mt`. ∎

**Lemma 14.15.1.4 (composed cylinder and level shift).** For a word `W` of length `n`, `S=S(W)`, `M := Σ_i m_i`: the followers of `W` form exactly one residue class `y_W` mod `2^{S+1}`, and for every integer `t`,

```text
G^n(y_W + 2^(S+1) t) = G^n(y_W) + 2·3^M t                                exactly.
```

**Proof.** Induction on `n`. `n=1` is Lemma `14.15.1.3` (`S=m_0+r_0`, `M=m_0`). Suppose the claim holds for the length-`n` prefix `W_n`, with representative `y^{(n)}` and `G^n(y^{(n)}+2^{S_n+1}t) = z + 2·3^{M_n}t` (`z := G^n(y^{(n)})`, odd, since `G` always outputs an odd integer). Append `(m_n,r_n)`: `y` follows `W_{n+1}` iff `y=y^{(n)}+2^{S_n+1}t` (some `t`, by hypothesis) and `stratum(z+2·3^{M_n}t) = (m_n,r_n)`. By Lemma `14.15.1.3`(i), the latter holds iff `z+2·3^{M_n}t ≡ w_{m_n,r_n} (mod 2^{m_n+r_n+1})` for the fixed residue `w_{m_n,r_n}` of stratum `(m_n,r_n)`; since `z` and `w_{m_n,r_n}` are both odd, dividing the (even) difference by `2` and using that `3^{M_n}` is a unit mod every power of `2` gives a unique solution `t ≡ t_0 (mod 2^{m_n+r_n})`. So `t=t_0+2^{m_n+r_n}u`, and `y = y^{(n)}+2^{S_n+1}t_0 + 2^{S_n+1+m_n+r_n}u =: y^{(n+1)} + 2^{S_{n+1}+1}u` (`S_{n+1}=S_n+m_n+r_n`) — the single-class claim for `W_{n+1}`. For the shift identity, `w_1' := z+2·3^{M_n}t_0 = G^n(y^{(n+1)})` lies on stratum `(m_n,r_n)` by construction, and `z+2·3^{M_n}t = w_1' + 2·3^{M_n}(t-t_0) = w_1' + 2^{m_n+r_n+1}·(3^{M_n}u)` (substituting `t=t_0+2^{m_n+r_n}u`), so Lemma `14.15.1.3`(ii) applies at `w_1'` with integer shift-count `t'' = 3^{M_n}u`: `G(w_1'+2^{m_n+r_n+1}t'') = G(w_1')+2·3^{m_n}t'' = G^{n+1}(y^{(n+1)}) + 2·3^{M_n+m_n}u`, giving `G^{n+1}(y) = G^{n+1}(y^{(n+1)}) + 2·3^{M_{n+1}}u` (`M_{n+1}=M_n+m_n`), completing the induction. ∎

**Theorem 14.15.1.5 (the finite-itinerary cylinder theorem).** For every word `W = ((m_0,r_0),…,(m_{n-1},r_{n-1}))`, `S = Σ_i(m_i+r_i)`:

```text
The odd integers following W (y_i on stratum (m_i,r_i) for all i, y_{i+1} = G(y_i))
form exactly one odd residue class mod 2^(S+1).
```

**Proof.** The single-class clause of Lemma `14.15.1.4`, applied to the full word (`n` = word length). ∎

**Corollary 14.15.1.6 (completeness).** Every word over the alphabet `{(m,r) : m,r ≥ 1}` is realized: the residue class of Theorem `14.15.1.5` is nonempty (a residue class mod any modulus has representatives), and in fact contains infinitely many odd integers.

**Corollary 14.15.1.7 (liveness).** For every realized word `W`, the class of Theorem `14.15.1.5` contains infinitely many *live* doors (`3 ∤ y_0`).

**Proof.** The modulus `2^{S+1}` is coprime to `3`; as the class's members increase by `2^{S+1}` each step and `2^{S+1}` is a unit mod `3`, their residues mod `3` cycle through all three values with period `3` in the step index, so at least one in every three consecutive members is coprime to `3`. Only `y_0` needs this check: `y_1,…,y_{n-1}` are automatically live regardless (Remark above, `14.14.7.1`). ∎

**Corollary 14.15.1.8 (single-stratum base case).** A single letter `(m,r)` alone is one class mod `2^{m+r+1}` — Lemma `14.15.1.3`(i) restated as the `n=1` case of Theorem `14.15.1.5`.

**Content — framing (per the brief's mandate).** This is the classical coding fact for the Collatz map, not new mathematics: Terras (1976) and Everett (1977) proved that the first `n` binary parities of an odd start are periodic in the start value with period `2^n`, each of the `2^n` parity vectors realized on exactly one residue class — the raw-bit case of Theorem `14.15.1.5`. The accelerated (block-valued) form is standard (Lagarias's surveys and annotated bibliographies; Wirsching's monograph). What this section adds is only: the same fact, read in the door/`(m,r)` alphabet fixed by the seam (`14.14`), tied to the seam's own strata, with its consequences for this program's search space stated once (`14.15.2`). No claim of new dynamics about `T` is made or intended, per the register norm.

An equivalent proof route pulls the cylinders back through the block-map identity `14.14.7.1` letter by letter: each `(m_i,r_i)` expands to the `T`-valuation word `(1,…,1,r_i+1)` (`m_i` entries, sum `m_i+r_i`), and `3x+1 = 2^ax'` pulls cylinders back uniquely at each raw step since `3` is a unit mod every power of `2`; the two routes agree because the expansion's sum matches `14.14.4.1`'s own denominator `2^{m+r}`. Not re-derived here.

**Verified** — `experiments/itinerary_coding.py`, fresh code (imports nothing from `door_seam.py` or `block_map.py`, per AGENTS.md), functions `test_single_stratum_exhaustive`, `test_two_step_exhaustive`, `test_single_stratum_level_shift`, `test_composed_level_shift`, `test_completeness_and_liveness`. Exhaustive scan, all odd `y < 2^23`, strata capped at `m,r ≤ 7`: `49` distinct strata realized, every one exactly one residue class mod `2^(m+r+1)`, `0` failures. Exhaustive two-step scan, all odd `y < 2^21`, letters capped at `≤ 5`: `625 = 5^4` length-2 words realized — every admissible word under the cap, matching Corollary `14.15.1.6`'s completeness exactly — every one exactly one residue class mod `2^(S+1)`, `0` failures. Single-stratum level-shift lemma, large random shifts (`|t| < 10^6`, `y < 10^7`): `15,000` checks, `0` failures. Composed level-shift (the induction step, checked against direct `n`-fold iteration rather than the affine formula, word lengths `1`–`6`): `6,000` checks, `0` failures. Completeness/liveness on random realized words: `1,500` words, `0` failures in either corollary (seeds `25001`–`25003`, 2026-07-16).

### 14.15.2. Consequences, recorded as calibration

The itinerary language is the **full shift** on the alphabet `{(m,r) : m,r ≥ 1}`: Theorem `14.15.1.5` plus Corollary `14.15.1.6` say every finite word is realized, with no forbidden word and no forbidden transition of any length — the alphabet's only constraint (`m,r ≥ 1`) is already built into `stratum`'s own range. Consequently **no finite-state admissibility graph exists to supply rigidity**: the search region "hidden finite-level order in the stratum word" — a shorter description of which continuations are legal — is closed **by proof**, not by testing. This calibrates the finite-state-chart remark of stage4.md `11.8.7.3.1` ("the reduced dynamics admits an exact countable-state chart... whose only unresolved inputs are the shell labels themselves at unbounded depth") and open-problems.md `11.6`'s finite-state-shadow question directly: the "shell labels at unbounded depth" that remark leaves open are exactly this section's stratum word, and Theorem `14.15.1.5` now says that word is not merely unresolved at unbounded depth but **unconstrained at every finite depth** — the realized words fill the full shift, so the dynamics is not confined to any proper subshift (of finite type or otherwise) that a structure search could uncover.

One pointer sentence, no more: the cylinder's natural measure `2^{-(S+1)}` is exactly what aeh.md's product law `π_k` (`13.2`) quantifies along actual orbits; AEH is thereby *precisely* the statement that actual orbits' stratum words equidistribute against the cylinder measure. (One fact, one page: aeh.md's content is not restated here, and no statistic is run.)

**The accounting sentence** (extends `14.14.6`/`14.14.8`'s own accounting; mandatory wherever items `1`–`3` of this section are quoted). Completeness means the stratum word carries **no structural discount** — the Bridge's remaining content is the word at unbounded length, and the word is free (unconstrained, every finite word realized, no admissibility rigidity to exploit) at every finite level. Nothing here reduces how much of it an infinite orbit requires: the word is exactly the forward `(s,m_+)` digit data `14.14.6` already identifies and stage4.md `11.8.7.7` already prices.

### 14.15.3. The two-sided coding

**(a) The future determines the 2-adic coordinate.**

A right-infinite word is `W = ((m_0,r_0),(m_1,r_1),…)`, every `m_i,r_i ≥ 1`. By Theorem `14.15.1.5` applied to its length-`n` prefixes `W_n`, the followers of `W_n` form a nested sequence of residue classes `y^{(n)} mod 2^{S_n+1}` (nesting is immediate from Lemma `14.15.1.4`'s induction: `y^{(n+1)} ≡ y^{(n)} (mod 2^{S_n+1})`), with `S_n ≥ 2n → ∞`. By the nested-cylinder property of the complete metric space `Z_2`, these classes have a unique common point.

**Definition 14.15.3.1.** `y_2(W) ∈ Z_2` is this unique point: `y_2(W) ≡ y^{(n)} (mod 2^{S_n+1})` for every `n`.

**Theorem 14.15.3.2 (injectivity).** Distinct positive odd integers follow distinct right-infinite words.

**Proof.** If `y ≠ z` both follow the same `W`, then for every `n` both lie in the class `y^{(n)} mod 2^{S_n+1}` (Theorem `14.15.1.5`), so `y ≡ z (mod 2^{S_n+1})` for every `n`; since `S_n → ∞`, this forces `y=z`, contradiction. ∎

**Content.** This is the accelerated form of the classical `2`-adic coding of the Collatz map: the parity-vector periodicity of Terras (1976) and Everett (1977) is the raw-bit case of this same nested-cylinder statement, and the `2`-adic extension of `T` and its explicit conjugacy to a shift-like map (Lagarias 1985; made explicit as the map `Φ` by Bernstein–Lagarias, *The `3x+1` conjugacy map*, Canad. J. Math. 48 (1996), 1154–1169, `Φ ∘ S = T ∘ Φ` for a shift-like `S`) is the identical topology on all of `Z_2`, in the raw parity-bit alphabet rather than the door/`(m,r)` alphabet. Theorem `14.15.3.2` is not a new injectivity fact; it is the standard one, read off Theorem `14.15.1.5` in one line because the seam's coordinates make the cylinders explicit.

**Remark (does `G` extend to `y_2`? — optional, not fully resolved).** For fixed `W`, `G(y_2(W))` can itself be computed as a `2`-adic integer by passing Lemma `14.15.1.3`(ii)/`14.15.1.4`'s shift formula to the limit along the approximants `y^{(n)}`, realizing the shifted word `(m_1,r_1),(m_2,r_2),…` — so `G` behaves well on the specific sub-Cantor-set of points arising this way. But the *formula* defining `G` routes through `m(y)=v_2(y+1)`, undefined at the single point `y=-1 ∈ Z_2` (`v_2(0)=∞`) — a genuine odd `2`-adic integer, though never itself equal to any `y_2(W)` (every `y_2(W)` has `v_2(y_2(W)+1)=m_0<∞` by construction). Whether some extension of `G` patches this point, or whether other such points exist, is not attempted here; this is recorded as the honest obstruction to a literal continuous self-map of `G` on all of odd `Z_2`, per the brief — not forced, not resolved.

**(b) The past determines the 3-adic coordinate.**

A left-infinite word is `(…,(m_{-2},r_{-2}),(m_{-1},r_{-1}))`, every `m_i,r_i ≥ 1`. For `n ≥ 1`, `W_{(-n:0)} := ((m_{-n},r_{-n}),…,(m_{-1},r_{-1}))` (a length-`n` word in forward order); let `A_n,B_n` be its composed-affine constants (`14.14.8.2`), `M_n := Σ_{i=-n}^{-1} m_i = v_3(A_n)`.

**Theorem 14.15.3.3 (the offsets converge).** `(B_n)_{n≥1}` is `3`-adically Cauchy — `v_3(B_{n+1}-B_n) = M_n → ∞` — hence `B_n → y_3 ∈ Z_3`, a limit depending only on the left-infinite word.

**Proof.** Passing from `W_{(-n:0)}` to `W_{(-(n+1):0)}` prepends `(m_{-(n+1)},r_{-(n+1)})`; writing `α,β` for that letter's own affine constants (`14.14.4.1`), substituting `G(y_{-(n+1)}) = αy_{-(n+1)}+β` into `G^n(u) = A_n u+B_n` gives `A_{n+1}=A_nα`, `B_{n+1}=A_nβ+B_n`. So `B_{n+1}-B_n = A_nβ`, and `v_3(B_{n+1}-B_n) = v_3(A_n)+v_3(β) = M_n + 0` (`v_3(A_n)=M_n` by `14.14.8.2`; `v_3(β)=0` exactly as in `14.14.4.1`'s own proof, since `m_{-(n+1)} ≥ 1`). Each `m_i ≥ 1` gives `M_n ≥ n → ∞`, so `(B_n)` is Cauchy in the complete metric space `Z_3` and converges. ∎

**Theorem 14.15.3.4 (the limit is the present door, to every precision).** If a live door `y_0` has an actual integer chain of live-door predecessors `…,y_{-2},y_{-1}` with `y_0 = G^n(y_{-n})` realizing `W_{(-n:0)}` for every `n`, then `y_0 = y_3` exactly in `Z_3`.

**Proof.** By Corollary `14.14.8.3` applied to `W_{(-n:0)}`, once `M_n ≥ k+1`, `y_0 = G^n(y_{-n}) ≡ B_n (mod 3^{k+1})` — independent of `y_{-n}`. By Theorem `14.15.3.3`, `v_3(B_n-y_3) → ∞`. For `n` large enough that both hold at level `k+1`, `y_0 ≡ y_3 (mod 3^{k+1})`; since this holds for every `k`, `y_0 = y_3` in `Z_3`. ∎

**Content.** Theorem `14.15.3.4` is the limit form of the synchronization corollary `14.14.8.3`, read backward: `14.14.8.3` says a fixed-length itinerary eventually forgets its starting door; this says an infinite backward itinerary forgets it completely and pins the present door's every `3`-adic digit, with no residual dependence on chain depth. Theorem `14.15.3.3`'s Cauchy argument is bookkeeping on top of `14.14.8.2`'s composition law, not a new mechanism: the same offset sequence `14.14.8.3` already uses at each finite precision is, as a sequence, self-convergent.

**Verified** — `experiments/itinerary_coding.py`, fresh code, functions `test_word_injectivity` (`8,000` random distinct pairs, `0` failures), `test_offset_cauchy` (pure algebra, exact `Fraction` arithmetic, `1,500` random words, `0` failures), `test_predecessor_sanity` (a fresh reimplementation of the `14.1.1` predecessor construction, including the `a=1` door-mortality fallback of `14.5.1` for the roughly half of steps where the `a=0` representative is dead: `6,730` checks, `0` failures), and `test_past_determines_3adic` (real integer backward chains, depth `100`: `500` chains, `4,000` `(chain, k)` checks of `y_0 mod 3^{k+1}` against the word-only prediction `B_n mod 3^{k+1}` at `k=1..8`, `0` failures) (seeds `25004`–`25007`, 2026-07-16).

**(c) The diagonal compatibility locus.**

**Definition 14.15.3.5.** A bi-infinite word `W = (…,(m_{-1},r_{-1}),(m_0,r_0),(m_1,r_1),…)` yields `(y_2,y_3) ∈ Z_2 × Z_3` via `14.15.3.1` on its right-infinite half and `14.15.3.3` on its left-infinite half. `W` is **integrally realized** iff some live door `y_0` follows the right-infinite half exactly and has an actual integer chain of live-door predecessors realizing the left-infinite half exactly.

**Remark (abundance, not scarcity, of live continuations).** Every live door has such chains in abundance: `14.1.1` gives infinitely many predecessor choices (one per admissible exit valuation `s`) at every backward step, and `14.5.1` guarantees the `a ≥ 1` representative doors of any predecessor state are never dead — so a live continuation exists whenever the chosen predecessor state has depth `≥ 2`, which infinitely many of the infinitely many `s`-choices supply. No word is claimed realizable by this remark — most are not, since `14.15.3.6` below pins any realized word's diagonal point exactly — only that realizability is never blocked for want of a live door to continue through.

**Theorem 14.15.3.6 (trivial direction).** If `W` is integrally realized by `y_0`, then `y_2 = y_3 = y_0` under the diagonal embeddings `Z ↪ Z_2`, `Z ↪ Z_3`.

**Proof.** `y_2=y_0`: `y_0` follows every finite prefix of the right-infinite half, so Theorem `14.15.1.5` places it in every class `y^{(n)} mod 2^{S_n+1}`; as `S_n → ∞`, `y_0=y_2` in `Z_2` (the argument of Theorem `14.15.3.2`, applied to one integer rather than two). `y_3=y_0`: this is exactly Theorem `14.15.3.4`, applied to the actual predecessor chain realizing the left-infinite half. ∎

**Mandatory identifications.**

- **Periodic words.** For a periodic bi-infinite word of period `n`, the forward composed law's fixed point `y^* = B_n/(1-A_n) ∈ Z_3` of Corollary `14.14.8.4` *is* this word's `y_3` (the periodic offsets `B_{kn}` converge geometrically to the same algebraic fixed point as `k → ∞`, the periodic case of Theorem `14.15.3.3`'s limit). If integrally realized by an actual periodic orbit, `14.14.8.4`'s reconciliation already identifies that fixed point with the classical rational cycle candidate of cycles.md `§12.1` — not a lever, and not re-derived here.
- **The general locus.** Characterizing which bi-infinite words are integrally realized — equivalently, which `(y_2,y_3) ∈ Z_2 × Z_3` lie on the diagonal — **is the Bridge in symbolic form** (bridge.md `§16`): closing it for typical words is the equidistribution question (aeh.md `§13`, this section's `14.15.2` pointer), closing it for periodic words beyond the classical candidate is the cycle-rigidity question (`16.4.4`). The formulation above is the deliverable; per the brief, no attempt is made here to characterize the locus beyond this definition, the trivial direction, and the periodic reconciliation.

**(d) Literature check.**

The right-infinite (`2`-adic future) side is classical, per `14.15.3`(a)'s Content paragraph: Terras (1976), Everett (1977), Lagarias (1985), Bernstein–Lagarias (1996). A search for prior treatments of the genuinely *two-sided* object — a `Z_2 × Z_3` (or adelic) coding of Collatz predecessor/successor structure, jointly — turned up no match. Specifically: Wirsching's `3`-adic material (*The Dynamical System Generated by the `3n+1` Function*, Lecture Notes in Math. 1681, Springer, 1998) treats the *starting value* as a `3`-adic variable in order to average stopping-time counting functions over it — a `3`-adic completion of the domain for a statistical purpose, not a coding of the backward itinerary as `Z_3`-valued data; it is not the same object, and is not claimed as prior art here. Monks–Yazinski's autoconjugacy (*The Autoconjugacy of the `3x+1` Function*, Discrete Math. 275 (2004), 219–236) is a `2`-adic involution (the parity-complement map `Ω`), not a `3`-adic construction at all. No solenoid or adelic formulation of Collatz coding meeting ordinary standards of peer review was found; a small number of non-peer-reviewed preprints use adjacent language ("adelic") without a comparable rigorous two-sided coding, and none is cited here. Recorded honestly: the two-sided `(y_2,y_3)` coding of `14.15.3`(c) — even only at the level of its formulation and trivial direction — is not found in this form in the literature searched (2026-07-16).

**Closing status.** What this layer adds: the itinerary language carried by the door/exit seam (`14.14`) is now fully characterized at the finite level — it is the classical Collatz coding, accelerated and read in door coordinates, and it is exactly the full shift on `{(m,r):m,r≥1}` (`14.15.1`–`14.15.2`); it extends to a two-sided `Z_2×Z_3` formulation whose periodic points are the already-known classical cycle candidates and whose general locus is a symbolic name for the Bridge, not a new route into it (`14.15.3`). What this forecloses: any search for finite-level structure in the stratum word — forbidden transitions, hidden admissibility constraints, a shorter description of which words occur — is closed **by proof** (`14.15.2`), not left open for testing. What is unchanged: the Bridge (bridge.md `§16`) is exactly as open as `14.14.6`/`14.14.8`'s closing statuses left it; both escape routes (equidistribution, rigidity) stand where they stood, and this section supplies no new argument toward either. Per the brief's stop line: no statistics of stratum words, no cycle-exclusion attempt, no density-exponent computation, no equidistribution proof attempt, and no ergodic-theoretic expansion beyond the two citations `14.15.3`(d) required follow from anything above.

## 14.15.4. The unique-predecessor lemma, the finite bicylinder corollary, and the positive realization height

*(Added 2026-07-16, branch `bicylinder-height`, per `briefs/bicylinder-height-brief.md`. Packages an external suggestion (ChatGPT, 2026-07-16, post-dating the merged `14.15`), pre-checked and corrected by the author and the main session before delegation: the letter-prescribed predecessor of a positive door is automatically positive — the external suggestion's claimed failure mode ("negative ... deep predecessors") does not occur — and nested-window monotonicity holds only around a *fixed* origin, not a sliding one. `14.15.1`–`14.15.3` are merged and closed and are not edited here; this is a new subsection extending `14.15`'s numbering, per house norm. Register, flat throughout: item (b) closes a small question (no finite two-sided obstruction, ever); item (c) is a *formulation* — the diagonal compatibility locus of `14.15.3`(c) renamed as a boundedness question at the archimedean place — and moves nothing about the Bridge.)*

### (a) The unique-predecessor lemma

**Theorem 14.15.4.1 (unique-predecessor lemma).** Fix a live door `z` and a letter `(m,r)`, `m,r ≥ 1`. There is at most one odd integer `y` with `G(y) = z` and `stratum(y) = (m,r)`, namely

```text
y = 2^m (2^r z + 1) / 3^m − 1,
```

which is an odd integer iff `3^m | 2^r z + 1`, and when it is, `y` is automatically positive and lies on stratum exactly `(m,r)` — both `v_2` conditions are forced by the construction, with no separate check.

**Proof.** *Uniqueness.* Suppose `y` satisfies `G(y)=z` and `stratum(y)=(m,r)`. Write `q := (y+1)/2^m`, an odd integer since `v_2(y+1)=m`. By Definition `14.14.3.1`, `G(y) = (3^m q − 1)/2^{v_2(3^m q − 1)}`, and `v_2(3^m q − 1) = r` by hypothesis, so `G(y)=z` reads `3^m q − 1 = 2^r z`, i.e. `q = (2^r z + 1)/3^m` — one equation, at most one solution `q`, hence at most one `y = 2^m q − 1`.

*Existence and the forced conditions.* Suppose `3^m | 2^r z + 1`; set `q := (2^r z+1)/3^m`, `y := 2^m q − 1`. Since `z` is odd and `r ≥ 1`, `2^r z + 1` is odd, and dividing the odd `3^m` into it preserves oddness: `q` is odd. So `y+1 = 2^m q` with `q` odd, giving `v_2(y+1) = m` exactly — the prescribed `m` is forced, not assumed. And `3^m q − 1 = 2^r z` by construction, `z` odd, so `v_2(3^m q − 1) = v_2(2^r z) = r` exactly — the prescribed `r` is likewise forced. Hence `stratum(y) = (m,r)` exactly and `G(y) = (3^m q − 1)/2^r = z`. Positivity: `q = (2^r z+1)/3^m` is a quotient of two positive numbers that is, by hypothesis, an integer, hence a positive integer (never zero, since `2^r z + 1 ≥ 3`), so `q ≥ 1` and `y = 2^m q − 1 ≥ 2^m − 1 ≥ 1` (`m ≥ 1`). ∎

**Content.** This is injectivity of `G` on a fixed stratum, made explicit and inverted: `14.14.4.1` already exhibits `G`, restricted to a stratum, as affine with nonzero rational slope `3^m/2^{m+r}`; the displayed formula is exactly that affine map inverted, and the nonzero slope is exactly why a solution, when it exists, is unique. The external suggestion packaged into this brief named "negative ... deep predecessors" as a failure mode; the algebra above shows this cannot happen — the two real failure modes are exactly the admissibility congruence `3^m | 2^r z + 1` failing, and (a separate matter, addressed in `14.15.4`(b)–(c)) liveness of a chain's deepest door.

**Reconciliation with the backward branching law (`14.2.4`) — cited, not re-derived; no mismatch found.** Set `N := 2^r z + 1`, `D := v_3(N)`. Substituting into `14.1.1`'s representative-door formula `y_a = 2^{D−a} 3^a Ω − 1` (`Ω = N/3^D`) at index `a = D − m` gives `3^{D−m}Ω = N/3^m = q`, hence `y_a = 2^m q − 1` — exactly the formula above. So the letter-prescribed predecessor of this theorem is `14.1.1`'s own representative door of the predecessor state `(Ω, D)`, at the representative index `a = D − m` that `m` names implicitly and exit valuation `s = r`; and `14.2.4`'s law `D = 1 + v_3(r − M_3(z))` computes, via the anchor, the same depth `D = v_3(2^r z + 1)` this construction needs directly. The two routes agree exactly.

**Verified** — `experiments/realization_height.py`, fresh code (imports nothing from `itinerary_coding.py`, `block_map.py`, or `door_seam.py`), functions `test_predecessor_roundtrip`, `test_exhaustive_uniqueness`, `test_no_negativity`. Round-trip (random live `y < 10^7` → `(m,r)=stratum(y)`, `z=G(y)` → formula must reproduce `y`, positive, odd, correct stratum, correct `G`-image): `6,000` checks, `0` failures. Exhaustive uniqueness (every odd `y < 2^21`, `m,r ≤ 6`, grouped by `(stratum(y), G(y))`): `1,016,064` groups, `0` collisions. No-negativity probe (random `(m,r,z)` with `m ≤ 7`, `z` drawn independently of any real door construction, wherever the admissibility congruence holds): `824` admissible triples out of `8,000` random draws, `0` failures (seed `35001`–`35002`, 2026-07-16).

### (b) The finite bicylinder corollary

**Theorem 14.15.4.2 (finite bicylinder corollary).** Let `V = ((m_{−p},r_{−p}),…,(m_{−1},r_{−1}))` and `U = ((m_0,r_0),…,(m_{q−1},r_{q−1}))` be finite words (past of length `p`, future of length `q`). There is a positive live door `y_0` with an actual chain of live-door predecessors `y_{−1},…,y_{−p}` realizing `V` exactly (`G(y_{−i})=y_{−i+1}`, `stratum(y_{−i})=(m_{−i},r_{−i})` for `i=1,…,p`, deepest door `y_{−p}` live, intermediate doors live automatically) and whose forward orbit realizes `U` exactly (`stratum(G^j(y_0))=(m_j,r_j)` for `j=0,…,q−1`).

**Proof.** Concatenate `V` and `U` into the length-`(p+q)` word `W`. By the finite-itinerary cylinder theorem (`14.15.1.5`), the followers of `W` form one residue class, nonempty and infinite (`14.15.1.6`); by `14.15.1.7`, this class contains infinitely many live doors. Pick one, `y_{−p}`, and set `y_{−p+i} := G^i(y_{−p})` for `i=1,…,p+q`, `y_0 := G^p(y_{−p})`. By the definition of "follows `W`" (`14.15.1.2`), `stratum(y_{−p+i})` is `W`'s `i`-th letter for `i=0,…,p+q−1`: the first `p` letters, realized starting at `y_{−p}`, are `V`; the remaining `q`, realized starting at `y_0`, are `U`. `y_{−p}` is live by choice; every later door in the chain is a `G`-image, hence live automatically (`14.14.3.2`(3) / `14.14.7.1`'s totality-and-live-image fact, which needs no liveness hypothesis on its input). Each step of the resulting chain is, by `14.15.4.1`'s uniqueness, exactly the letter-prescribed predecessor of the next door on the prescribed letter — not a separate construction, the same one. ∎

**Consequence, stated flatly, in `14.15.2`'s register.** Every finite two-sided itinerary window is realized by a positive live integer segment — there is no finite two-sided obstruction. This extends `14.15.2`'s verdict (the word is free at every finite *forward* depth) to finite windows with prescribed past: prescribing a past costs nothing either, at any finite depth.

**Verified** — `experiments/realization_height.py`, function `test_bicylinder`. Random positive live door `y_0 < 10^5`, random `p,q ∈ {0,…,3}`, forward realization `U` computed directly, backward chain `V` built via `14.15.4.1`'s formula with randomly drawn letters (each accepted only when the resulting predecessor is both integral and live): `2,000` trials, all `2,000` successfully built a chain within the search budget, and every check — chain consistency `G(y_{−i})=y_{−i+1}`, liveness of every chain door (not only the deepest), stratum match against the recorded letters, and forward realization of `U` — passed with `0` failures (seed `35003`, 2026-07-16).

### (c) The positive realization height

**Definition 14.15.4.3 (window, positive realization height).** Fix a bi-infinite word `W = (…,(m_{−1},r_{−1}),(m_0,r_0),(m_1,r_1),…)` and a window `(p,q)`, `p,q ≥ 0`, around `W`'s *fixed* origin (position `0`, held fixed throughout — windows are never re-centred). Let

```text
R_{p,q}(W) := { y_0 :  y_0 a positive live door,
                stratum(G^j(y_0)) = (m_j,r_j) for j = 0,…,q−1,
                and the 14.15.4.1 letter-prescribed backward chain
                (predecessor on (m_{−1},r_{−1}), its predecessor on
                (m_{−2},r_{−2}), …) exists to depth p with live
                deepest door }.
```

`H_{p,q}(W) := min R_{p,q}(W)` whenever `R_{p,q}(W) ≠ ∅`.

**Theorem 14.15.4.4 (basic properties).**

1. `R_{p,q}(W) ≠ ∅` for every `p,q ≥ 0`, so `H_{p,q}(W)` is always defined.
2. `R_{p,q+1}(W) ⊆ R_{p,q}(W)` and `R_{p+1,q}(W) ⊆ R_{p,q}(W)`, hence `R_{p',q'}(W) ⊆ R_{p,q}(W)` whenever `p' ≥ p, q' ≥ q` — in particular `R_{p+1,q+1}(W) ⊆ R_{p,q}(W)` (fixed origin).
3. `H_{p,q}(W)` is a positive integer, nondecreasing in `(p,q)` under the product order.

**Proof.** (1) is `14.15.4.2` applied to `W`'s own length-`p` past and length-`q` future around the origin. (2): if `y_0 ∈ R_{p,q+1}(W)`, its forward orbit realizes letters `0,…,q`, in particular the shorter prefix `0,…,q−1`, and its depth-`p` backward condition is untouched — `y_0 ∈ R_{p,q}(W)`. If `y_0 ∈ R_{p+1,q}(W)`, its depth-`(p+1)` chain `y_{−1},…,y_{−(p+1)}` restricts to the depth-`p` prefix `y_{−1},…,y_{−p}`, whose deepest door `y_{−p} = G(y_{−(p+1)})` is live automatically (a `G`-image of the live `y_{−(p+1)}`) — `y_0 ∈ R_{p,q}(W)`; the forward condition is untouched. Chaining the two gives the general case. (3): `R_{p,q}(W)` is a nonempty set of positive integers, so its minimum exists; (2)'s inclusions give (subset's minimum) `≥` (superset's minimum), i.e. `H_{p',q'}(W) ≥ H_{p,q}(W)` whenever `p'≥p, q'≥q`. ∎

**Theorem 14.15.4.5 (equivalence theorem).** `W` is integrally realized (`14.15.3.5`) if and only if `(H_{p,q}(W))_{p,q}` is bounded, if and only if it is eventually constant.

**Proof.** *Bounded ⟺ eventually constant.* Eventually constant trivially implies bounded. Conversely suppose `H_{p,q}(W) ≤ B` for all `p,q`. Along the diagonal, `(H_{n,n}(W))_n` is a nondecreasing sequence of positive integers bounded by `B`, hence eventually constant, say `= y_0` for `n ≥ N`. For `p,q ≥ N`: `H_{p,q}(W) ≥ H_{N,N}(W) = y_0` (monotonicity, `(p,q)≥(N,N)`) and `H_{p,q}(W) ≤ H_{n,n}(W) = y_0` with `n=max(p,q)≥N` (monotonicity, `(n,n)≥(p,q)`), so `H_{p,q}(W)=y_0` for *all* `p,q≥N` — eventually constant as a full net, not merely along the diagonal.

*Integrally realized ⟹ bounded.* Let `y_0^*` realize `W` (`14.15.3.5`): its forward orbit realizes the entire right-infinite half, and it has an actual integer chain of live-door predecessors realizing the entire left-infinite half. For any `p,q`, the depth-`p` prefix of that actual chain is a chain of live-door predecessors realizing the first `p` past letters; by `14.15.4.1`'s uniqueness, any predecessor satisfying `G(y)` equal to the next door and carrying the prescribed stratum equals the unique formula value, so this actual chain coincides, step for step, with the letter-prescribed one. Hence `y_0^* ∈ R_{p,q}(W)` for every `p,q`, giving `H_{p,q}(W) ≤ y_0^*` uniformly.

*Bounded ⟹ integrally realized.* By the first paragraph, `H_{p,q}(W) = y_0` for all `p,q ≥ N`. Fix any `(p,q)`; taking `p',q' ≥ max(p,q,N)`, `(2)` gives `R_{p',q'}(W) ⊆ R_{p,q}(W)`, and `y_0 ∈ R_{p',q'}(W)` (the minimum of a nonempty set is a member of it), so `y_0 ∈ R_{p,q}(W)`. As `(p,q)` was arbitrary, `y_0 ∈ ⋂_{p,q} R_{p,q}(W)`. Letting `q→∞` in the forward condition: `y_0`'s entire forward orbit realizes `W`'s right-infinite half, deterministically. For the backward half: `y_0` has, for every `p`, a letter-prescribed chain to depth `p` with live deepest door; by `14.15.4.1`, the letter-prescribed predecessor at each step is *unique*, so the depth-`(p+1)` chain's nearest `p` entries coincide exactly with the depth-`p` chain — the chains are **compatible under truncation because the prescribed predecessor is unique**, and they union into a single infinite chain `y_{−1},y_{−2},…` (`G(y_{−(i+1)})=y_{−i}` for every `i≥0`) realizing the entire left-infinite half. Liveness: `y_0` is live by definition of `R` (any `R_{p,q}(W)` with `p,q≥0` requires it); each `y_{−i}` (`i≥1`) is live because it is a `G`-image of the next-deeper door of any chain of depth `>i` — automatic regardless of whether that deeper door itself needed an explicit check (`14.14.3.2`(3)). So `y_0`, with this chain, witnesses that `W` is integrally realized. ∎

**Remark (the three-notion separation, stated once).** Three notions of "does a finite window occur," strictly increasing in strength. **Finite symbolic legality** — always: the itinerary language is the full shift (`14.15.2`), every finite word a legal transition sequence, nothing to fail. **Finite positive realization** — always: `14.15.4.2`, every finite two-sided window is realized by an actual positive live integer segment. **Realization at all depths simultaneously** — a single integer realizing the *entire* bi-infinite word — is strictly stronger, and by `14.15.4.5` is exactly equivalent to boundedness of the positive realization height. Its failure mode, when it fails, is `H_{p,q}(W) → ∞`: the minimal witnesses guaranteed to exist at every finite depth by the second notion are forced to escape to infinity as the window grows, so no single integer serves every window at once. This is the precise sense — **archimedean**, at the place the `Z_2 × Z_3` diagonal embedding forgets — in which a word can be finitely compatible everywhere and yet realized by no integer.

**Verified** — `experiments/realization_height.py`, functions `test_trivial_word_height`, `test_monotonicity`, on exactly the two sanity families the brief permits (no growth study of `H` performed or attempted). Trivial all-`(1,1)` word: `y_0=1` (`stratum(1)=(1,1)`, `G(1)=1`, the trivial fixed point) checked to be a member of `R_{n,n}` for `n=0,…,4` directly — since `1` is the least positive odd integer, membership alone proves `H_{n,n}=1` exactly, no search needed — `0` failures at any `n`. Fixed-origin nested-window monotonicity: `20` random words, each the actual itinerary of a real integer (future simulated forward, past built via `14.15.4.1`'s formula with random letters, `m ≤ 2`), `H_{n,n}` computed by exhaustive search up to `2^{17}` at `n=1` and `n=2` on the *same* underlying word and pivot: `20/20` words built, `0` monotonicity violations (and `0` search-bound shortfalls), `17` of `20` strictly grew (seed `35004`, 2026-07-16).

### (d) Accounting and closing status

**Accounting** (extends `14.14.6`/`14.14.8`/`14.15.2`'s own accounting sentence). The positive realization height is another exact name for the Bridge (bridge.md §16): **Bridge ⟷ boundedness versus escape of the positive realization height `(H_{p,q})`.** This is a renaming, not an estimate: nothing above bounds `H`, gives it a recurrence, or bounds its rate of escape when it escapes — the equivalence theorem states what boundedness *means*, not when it holds.

**Periodic words — one reconciling sentence.** For a periodic bi-infinite word, `14.15.3`(c)'s mandatory identification already names the classical rational cycle candidate of cycles.md §12.1 as the word's `y_3`; the trivial word (all letters `(1,1)`) is the case of that identification realized by an actual integer — the trivial fixed point `y=1` — and correspondingly `H_{p,q} ≡ 1` at every window (verified above), the door-coordinate incarnation of the trivial cycle `(1,1)`, not a new fact.

**Closing status.** What this subsection changes: the diagonal compatibility locus of `14.15.3`(c) now has an equivalent boundedness criterion (`14.15.4.5`) naming its archimedean content exactly (the three-notion remark above), and the finite-window question is fully closed — no finite two-sided obstruction exists, ever (`14.15.4.2`). What it does not change: the Bridge is exactly as open as `14.15.3`'s closing status left it. Characterizing which words are integrally realized — beyond the definition, the trivial direction (`14.15.3.6`), and the equivalence theorem's boundedness criterion — remains the Bridge itself, reserved for equidistribution (typical words, aeh.md §13) or rigidity (periodic words, `16.4.4`) exactly as before. Per the brief's stop line: no growth study of `H`, no characterization attempt on the diagonal locus beyond the equivalence theorem, no cycle-exclusion attempt, and no equidistribution proof attempt follow from anything above.
