---
status: ACTIVE — forward/backward duality complete (14.1–14.12; density bound c* = 0.3304, 14.6); door/exit seam relocates the core-extraction deficit onto the forward digit budget (14.14); itinerary language is a full shift completing the signed two-sided diagonal characterization (14.15, 14.15.6); exact height laws close the integer-fixed-point periodic instances (14.15.7), the non-integral mechanism the rest of the single-letter shelf (14.15.8), and the whole periodic shelf is closed by theorem at whole-period windows (14.15.9) — Bridge status unchanged throughout
scope: new section 14 (post-monolith)
updated: 2026-07-22
source: new material; the author's reversal question; builds on 9.8 (spine.md), 11.5 (open-problems.md), §3 anchor machinery
---

> **Current state.** The reduced map run backward. Proved: the complete predecessor characterization and the backward valuation law `d = 1 + v₃(s − M₃(y))` governed by the 3-adic anchor `M₃` — the exact mirror of the forward 2-adic law, duality table at 14.3 (14.1–14.3); a rigorous density bound `π̃(X) ≥ 2^(−3.6)·X^(0.3)` with critical exponent `c* ≈ 0.3304`, lifted to `0.33515` by multi-door renewal, the stages-2–3 obstruction precisely recorded (14.6, 14.6.5, 14.13); the dual per-step theorem queue closed, each genuine forward/backward asymmetry identified (14.7–14.10); the door/exit seam — the exit map `G` semiconjugate to `F`, an exact per-stratum 3-adic contraction with a constant-offset graded law, the block-map identity `G(y) = T^(v₂(y+1))(y)`, and composition along fixed itineraries — with the reconciliation that the seam relocates, not evades, the core-extraction deficit (14.14). The itinerary language is the classical Collatz coding read in door coordinates and is a full shift — no finite-state admissibility rigidity exists to find (14.15.1–14.15.2); the two-sided coding carries the three-way diagonal characterization — integral realization ⟺ the two adelic limits agree at a single odd integer ⟺ the realization height is bounded — proved signed over the nonzero odd integers, with the known cycles as ordinary periodic diagonal points and `−1` alone outside the coding (14.15.3–14.15.6); and whole-period height laws hold on every periodic word, the dichotomy governed by the fixed-point denominator `q`: at `q = 1` the realized sector is capped at `|y^*|`, at `q > 1` both sectors escape at the CRT-modulus rate (14.15.7–14.15.9). Open: periodic cycle exclusion — ruling out `q = 1` beyond the known instances (`1`, `−5`, `{−17,−41}`) — and the Bridge itself (bridge.md §16), unchanged throughout (14.14.6).

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

**Proposition 14.2.3 (algebra of `M₃`).** `M₃(1)` is the distinguished exponent class representing the discrete logarithm of `−1` to base `2` — an element of the exponent group `E₃ = lim Z/(2·3^(k−1)) ≅ Z/2 × Z₃`, not of `Z₃` itself: concretely `2^(3^(k−1)) ≡ −1 (mod 3^k)`, so its truncation mod `2·3^(k−1)` is `3^(k−1)` (verified for `k = 8`). And `M₃` is an affine logarithm: `M₃(y₁y₂) = M₃(y₁) + M₃(y₂) − M₃(1)` (zero failures in 300 random pairs), so `M₃(y) = M₃(1) − log₂ y` in the 3-adic discrete logarithm.

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

*(The question: under what conditions does backward generation cease?)*

**Theorem 14.5.1 (door mortality).** For a state `(Ω, D)`, the doors `y_a` with `a ≥ 1` are never dead (`y_a ≡ 2 (mod 3)` identically). The sole mortal door is `a = 0`: it is dead iff `2^D Ω ≡ 1 (mod 3)`, which holds on exactly two of the four admissible residue–parity classes of `(Ω mod 3, D mod 2)` (density 1/2 under uniform counting of these classes — there is no uniform measure on the infinite state space, so "half of all states" is shorthand only). **Verified exactly on 20,000 random states, all doors.**

**Theorem 14.5.2 (Gardens of Eden).** A state has no `F`-preimage at all iff `D = 1` and `Ω ≡ 2 (mod 3)` — equivalently, iff its unique representative is an odd multiple of `3`. Every state with `D ≥ 2` is reachable (door `a = 1` is always alive). **Verified against the forward image on 600 states.** This is the reduced form of the classical fact that multiples of `3` have no odd predecessor — classically, one third of odd integers; in reduced coordinates the phenomenon concentrates entirely on depth-`1` states of core `≡ 2 (mod 3)`, while deeper states merely lose one door.

**14.5.3 (the renewal equation, mortality included — resolving the 14.4 open item at the heuristic level).** The multi-type branching analysis of the tree, with the door structure of `14.1.1`, the depth law `2·3^(−d)`, the measured stationary depth distribution, and Theorem `14.5.1`'s mortality (a factor `1/2` on door `0`), gives the renewal mass

```text
mass(c) = E_D [ Σ_(a<D) (½ if a=0 else 1) · 2^(−c(D−a)) 3^(−ca) ] · Σ_s 2^(−cs) · E[3^(cd)].
```

Computed over `c ∈ (0,1)`: the mass **never falls to 1** — its minimum is `≈ 1.52` at `c ≈ 0.7`. The backward tree is supercritical at every sub-density exponent: the analysis predicts growth exponent `1` (full density), consistent with the exact enumeration (`0.970 → 0.981`, rising) and with the conjecture's prediction. Two honest notes: the discarded first attempt at this equation is recorded at 14.4; and the present computation is a heuristic with one measured input (the stationary depth law) — the rigorous target is now sharp: **extract a KL-style lower bound (`x^c` reachable states, explicit `c`) from a truncated, fully-rigorous core of this supercritical system.** The `50%` margin at the bottleneck suggests meaningful room.

**Remark (what mortality costs).** Dead ends do not throttle the tree. Their entire price is half a door per state — visible in the mass formula as the lone `½` — against `D`-fold door multiplicity and infinite `s`-branching. The classical intuition that "a third of numbers being leaves" might starve the tree is quantitatively false in reduced coordinates.

## 14.6. A rigorous density bound from the door tree

*(The front's open theorem target, executed at base level. Reference point: Krasikov–Lagarias 2002 [arXiv:math/0205002] prove `π₁(x) > x^0.84` via linear programs over difference inequalities mod `3^11`; earlier milestones Crandall 1978 (first `x^β`), Krasikov 1989 (`0.43`), Wirsching (`0.48`). The result below is numerically far weaker than all but Crandall; its content is the derivation — fully self-contained in the reduced formalism — and the collapse identity that makes it single-type.)*

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

At `c = 0.3` the first two windows alone give `1.0502 > 1`, and every child in those windows satisfies `y' < y·2^(11.415)`. Renewal induction with `A = 2^(−12c)` and threshold `2^12`; the strict-scale step is guaranteed by child growth `z ≥ (19/15)y`, and the root is handled by its own mass lemma (children `5, 85, 341`; mass `1.0546 > 1` — the `s = 1` self-loop excluded by definition). Node counts convert to distinct odd integers reaching `1` via the unique-parent/distinctness lemma. **The canonical, fully refereed five-lemma proof is paper 2 (`paper/collatz-mirror-v1.tex`, §8); this section is the working summary, constants aligned.** ∎

**Remark (position and the refinement path).** The bound sits between Crandall (1978) and Krasikov's original `0.43` — deliberately: the core uses *one* door per state, *two* children per triple, and adversarial anchor phases. The empirical core already grows at exponent `≈ 0.45`, and the full tree at `≈ 0.98` (14.4). Each discarded resource maps onto a stage of the Krasikov–Lagarias program (their residue systems mod `3^k` = our door residues; their LP = optimizing over our branch inventory), with one structural difference: their difference inequalities *bound* the local branching, while the anchor law `14.2.4` gives it *exactly*. Whether exactness buys anything beyond `0.84` is an open question, addressed by the refinement program in 14.6.5/14.13: multi-door taken alone gives a genuine but small lift (`c* → 0.33515`, 14.6.5); the `3^k`-residue and exact-anchor-phase routes hit a structural obstruction — the collapse map is affine, not multiplicative, so neither a residue nor the anchor propagates to the child without unavoidable precision loss (14.13) — so the question stands open, now with a precise account of what blocks the obvious attack.

## 14.6.5. Multi-door renewal, rigorously (KL–LP refinement, stage 1)

*(First stage of the density-refinement program named in the 14.6 remark: reinstate the door multiplicity the single-door core of 14.6 discards.)*

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

*(Continues 14.6.5's stage 1. This section records a precise obstruction rather than a further theorem: the residue-mod-`3^k` LP and the exact-anchor-phase refinement were both attempted; neither reached a verified, sound result, and the reason is structural, not a matter of more grinding.)*

**The target.** Stage 2 asks for a genuine linear program over door residues mod `3^k` (variables = per-residue branch masses, constraints = the exact local branching relations, solved with a real solver), in the spirit of Krasikov–Lagarias's mod-`3^11` system. Stage 3 asks whether folding in the *exact* anchor law `14.2.4` (as equality constraints, where it pins a phase) beats a Krasikov–Lagarias-style inequality treatment.

**What was tried, and what broke.**

1. *Naive stationary residue tracking.* First construction: states = `y mod 3^k`; transition for admissible `s` computed directly from a `k`-digit representative, claiming the child's *full* `k`-digit residue is representative-independent whenever `d = v₃(N) < k`. This is **false** and was caught by an explicit counter-check (3,120 transitions tested against varied higher digits of `y`, 2,279 failures) — the correct statement (re-derived and verified with zero failures over 4,160 checks) is that a parent known mod `3^k` pins the child only mod `3^(k−d)`: dividing by `3^d` costs exactly `d` digits of precision, and since admissible `s` forces `d ≥ 1` always, **no step is free** — a strictly stationary, same-`k`-forever residue system does not exist. This is the concrete, verified form of the affine-map obstruction flagged in 14.6.5's honest assessment.

2. *Drop-on-overflow.* Second construction: states = `(j, r)` — "known to `j` digits, currently `r mod 3^j`" — with `j` strictly decreasing each step (by `d`) and any transition that would exhaust precision simply dropped (zero credit, a valid but conservative simplification). Because `j` strictly decreases with every edge, the resulting transition graph is a **finite DAG with no cycles** — its spectral radius is identically `0` for every `c`. This construction can never certify supercriticality at *any* exponent; it is mathematically correct but useless (confirmed directly: bisection collapses to the search floor for every `k` tried, 1–6).

3. *Generic fallback credited at weight 1.* Third construction: same `(j,r)` states, but instead of dropping an exhausted-precision transition, credit it at weight `1` (as if the child trivially satisfies `f(child,X) ≥ (X/child)^c`) and solve the resulting acyclic system bottom-up. This produces attractive-looking numbers (`k=2`: `c*≈0.41`; `k=3`: `c*≈0.50`; `k=6`: `c*≈0.57`, still climbing) — **but the construction is unsound**: crediting weight `1` unconditionally is only valid once the *accumulated size* from the true root has already crossed the renewal threshold (Lemma renewal's actual base case, paper §8), not merely once residue precision runs out. Precision exhaustion and size-threshold crossing are different events — a child can run out of tracked digits while still being small relative to `X` — and the construction conflates them. No fix was found and verified in-session; **these numbers are not claimed**, only recorded so the trap is not walked into twice (precedent: 14.4's discarded single-type renewal equation).

**Diagnosis.** All three failures trace to one fact, first surfaced in 14.6.5: the collapse map `y ↦ (2^(s+1)y − 1)/3` is *affine*, not multiplicative, so neither the anchor `M₃(y)` nor a truncated residue `y mod 3^k` propagates to the child without irreducible loss (exactly `d` digits per step, `d ≥ 1` always). Krasikov–Lagarias do not face this: their difference-inequality system tracks the map's residue behavior directly, without an analogue of our door/collapse structure, and — per 14.6.5 — their inequalities *bound* branching where our anchor law would give it *exactly*, but exactness only helps if it can be carried forward, and here it provably cannot be carried forward for free. (This precision loss is the reverse face of the forward digit budget, stage4.md 11.8.7.7; both are consolidated as the **core-extraction deficit** in §16, `bridge.md` — one phenomenon under `2↔3`.)

**Answering the 14.6 remark's open question.** *Whether exactness buys anything beyond `0.84`* is not resolved in the affirmative by this program: the one avenue that would have delivered it (a stationary exact-residue LP exploiting `14.2.4`) is obstructed by the precision loss above. The multi-door resource (14.6.5) is exact and does compose, and it buys a real but small lift. Whether a *correctly* size-threshold-coupled version of construction 3 recovers real gains from residues remains open — it is a well-defined technical question (couple the DAG in `(j,r)` to the outer renewal induction's own accumulated-offset variable, rather than crediting exhaustion for free) but was not resolved here.

**Status.** Primary success bar (`c > 0.43`, Krasikov 1989) **not reached** as a verified theorem. Stage 1 (14.6.5) stands as the session's one verified gain: `c* : 0.3304 → 0.33515`. Stages 2–3 close with the obstruction above, precisely stated, per the brief's equally-valid stop condition. No code from attempt 3 is presented as a result; the diagnostic scripts are not committed (dead ends recorded here in prose, per house norms, rather than as unrunnable/misleading code).

## 14.14. The door/exit seam

*(Both the forward anchor increment (stage2.md 11.8.5.6) and the reverse predecessor recovery (14.6.5.1) pass through a single intermediate integer, the exit — equivalently, live door — `y` of a reduced edge. This section makes that coordinate change precise: it re-expresses the forward Bridge increment `ΔM` around `y` (14.14.2), and asks whether the forward reduced map itself, written in door coordinates (14.14.3), carries a total graded law for the 3-adic anchor that the core-extraction step of `16.2` provably cannot (14.14.5). It does — with a genuinely constant offset — and 14.14.6 accounts for where the core-extraction deficit's unbounded-depth content sits once the seam is used. The exit map is a coordinate change on already-proved dynamics, not a new dynamical system.)*

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

**The accounting.** `14.14.4`'s "gain" — `G` sharpening `3`-adic agreement by `m` digits per step, in contrast to `16.2`'s forward loss of `σ` `2`-adic digits per step — is real, and it is bought at *exactly* `16.2`'s own price, not a lower one: identifying which stratum a door sits in (the prerequisite for applying `14.14.4`/`14.14.5` at all) costs precisely the `2`-adic digits `11.8.7.7` already prices as consumed and unregenerated. The seam does not touch that supply; it relabels it. What changes is where the *bookkeeping* looks free: the `3`-adic side of the ledger, which used to look like irrecoverable loss in the naive predecessor picture (`14.13`'s affine-collapse obstruction — a parent known mod `3^k` pins the child only mod `3^{k-d}`), is in door coordinates a bounded, even contracting, computation at every single step. But the unbounded-depth content of the Bridge has not shrunk: it now sits entirely and visibly in the `2`-adic stratum-label sequence `(m_i, r_i)_i`, which *is* the forward `(s, m_+)` sequence, term for term. Composing the graded law along an infinite orbit still requires unboundedly much of that sequence, for the same reason `11.8.7.7` already gives: nothing regenerates it. This is the page's one accounting sentence, owned here: nothing in `14.14`–`14.15` reduces how much of the stratum word an infinite orbit requires — the word is exactly the forward `(s, m_+)` digit data stage4.md `11.8.7.7` prices, and the Bridge (bridge.md §16) is unchanged by it.

**Standing.** This is the honest form of "seam versus deficit": the door/exit coordinate change makes the `3`-adic residue tracking *free* — a genuine simplification, and the reason `14.14.5`'s offset is constant where `14.8.2`'s and `11.8.7.3.1`'s are not — but it does so by making visible, rather than by discharging, the `2`-adic cost that `16.2` and `11.8.7.7` already identified as the Bridge's one hard fact. The core-extraction deficit is not evaded by this section; it is relocated onto a single, already-known, already-priced axis, and the diagnostic reach of `16.2` is extended by having a second, independently-derived route (through the forward direction's *own* deterministic exit sequence, rather than through backward branching) land on the identical accounting.

**Closing status.** What this section changed about the Bridge: a working formulation. `ΔM` now has a coordinate (the door `y`) on which it is a mismatch of one fixed operation (`14.14.2`) rather than an opaque function of the next core; the reduced map itself has a door-coordinate presentation (`G`, `14.14.3`) that is total, mortality-free, and — restricted to a `2`-adic stratum — an exact `3`-adic contraction (`14.14.4`) supporting the strongest-graded increment law in the program to date, constant offset rather than growing (`14.14.5`). What it did not change: the Bridge is exactly as open as it was. `14.14.6`'s accounting shows the `3`-adic gain is paid for, in full and exactly, by `2`-adic stratum data identical to the forward digit budget (`11.8.7.7`) already on file — no bounded amount of that data exists along an infinite orbit, for the same reason `11.8.7.7` gives, and the seam supplies no new argument against it. Both halves of the program's stated escape routes — equidistribution (`aeh.md` §13) for typical orbits, rigidity (`11.8.3.11`) for cycles — stand exactly where `bridge.md` §16 left them. Per the brief's stop criterion: this closes items 1–6 at the floor-plus-primary bar (all six proved, item 5 resolved affirmatively rather than obstructed), and per §16.4.6/16.5's own register, no further front is opened from here — no density-exponent computation, no numerical iteration of `G` hunting statistics, no equidistribution proof attempt. If composing `14.14.5`'s law along orbits suggests further structure, that composition is a separate decision for the main session, not continued here.

### 14.14.7. The block-map identity

*(An interpretation of `G`, not a new fact about it: the exit map is the accelerated Collatz map itself, run for a return time read directly off the door.)*

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

*(Composes `14.14.4`'s affine law and `14.14.5`'s graded law along a run of steps that all follow one fixed sequence of strata.)*

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

**Accounting.** The `3`-adic side of the ledger is not merely cheap per step (`14.14.4`–`14.14.5`) but asymptotically *free* along a fixed itinerary: beyond the first `k+1` accumulated `m`-digits, every residue at precision `3^k` is a function of the stratum word alone (`14.14.8.3`) — a sharpening of, not a change to, the relocation verdict of `14.14.6`. Bridge status unchanged (`14.14.6`).

**Closing status.** This layer changes nothing about the Bridge. It is a corollary layer on the already-closed seam (`14.14.1`–`14.14.6`): the block-map identity gives `G` its own meaning as `T`'s variable-return-time block map (`14.14.7`); the semiconjugacy has its accurate name (`14.14.3`'s retitled property); `14.14.5`'s tightness has an exact quantitative form (`14.14.5.4`); and the seam's per-step laws now have their composed form along orbits (`14.14.8.2`–`14.14.8.4`) — including the reminder, made explicit rather than left implicit, that the composed fixed point is the classical cycle candidate under a new name, not a new candidate. Both halves of the program's stated escape routes stand exactly where `bridge.md` §16 left them; per the brief's stop criterion, no cycle-exclusion attempt, no stratum-word statistics, no density computation, and no equidistribution proof attempt follow from any of this.

**Verified** — `experiments/block_map.py`, fresh code, functions `test_composed_affine`, `test_composed_difference`, `test_synchronization`, `test_periodic_fixed_point_algebra`, `test_trivial_fixed_point_sanity`. Composed affine law: `1,500` random doors, itinerary length `n=4`, `G^n(y)` compared against `A_n y + B_n` (exact `Fraction` arithmetic) and `v_3(A_n)` against `Σm_i`, `0` failures. Difference law: `800` pairs sharing a length-`3` itinerary (`584,763` draws by rejection sampling), `0` failures. Synchronization: `600` pairs sharing a length-`3` itinerary (`431,680` draws), all with `Σm_i ≥ k+1 = 3` (guaranteed at `n=3`, `k=2`, since `m_i ≥ 1` always), `y_n mod 3^(k+1)` matching both across the pair and against the formula `B_n mod 3^(k+1)`, `0` failures. Periodic-word fixed-point algebra (`A_n y^*+B_n = y^*`, exact `Fraction` identity, for `500` random itineraries of length `1`–`4`, not necessarily from real periodic orbits): `0` failures. Trivial fixed point sanity instance (`y=1`, word `(1,1)`, `A=3/4`, `B=1/4`, `y*=1`): reproduced exactly (seeds `15007`–`15010`, 2026-07-15).

## 14.15. The itinerary language: the cylinder theorem and the two-sided coding

*(The cylinder theorem below is **not new mathematics about `T`** — it is the classical Collatz coding fact (parity-vector periodicity, Terras 1976 and Everett 1977; the accelerated form standard, Lagarias's surveys, Wirsching) read in the door/`(m,r)` alphabet fixed by the seam (`14.14`), with its consequences for this program's search space stated once (`14.15.2`) and its two-sided `Z_2 × Z_3` extension formulated, with no new leverage on the Bridge (`14.15.3`).)*

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

**Accounting.** Completeness means the stratum word carries **no structural discount** — the Bridge's remaining content is the word at unbounded length, and the word is free (unconstrained, every finite word realized, no admissibility rigidity to exploit) at every finite level. Bridge status unchanged (`14.14.6`).

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

*(The letter-prescribed predecessor of a positive door is automatically positive, and nested-window monotonicity holds only around a *fixed* origin, not a sliding one. Item (b) closes a small question (no finite two-sided obstruction, ever); item (c) is a *formulation* — the diagonal compatibility locus of `14.15.3`(c) renamed as a boundedness question at the archimedean place — and moves nothing about the Bridge.)*

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

**Accounting.** The positive realization height is another exact name for the Bridge (bridge.md §16): **Bridge ⟷ boundedness versus escape of the positive realization height `(H_{p,q})`.** This is a renaming, not an estimate: nothing above bounds `H`, gives it a recurrence, or bounds its rate of escape when it escapes — the equivalence theorem states what boundedness *means*, not when it holds. Bridge status unchanged (`14.14.6`).

**Periodic words — one reconciling sentence.** For a periodic bi-infinite word, `14.15.3`(c)'s mandatory identification already names the classical rational cycle candidate of cycles.md §12.1 as the word's `y_3`; the trivial word (all letters `(1,1)`) is the case of that identification realized by an actual integer — the trivial fixed point `y=1` — and correspondingly `H_{p,q} ≡ 1` at every window (verified above), the door-coordinate incarnation of the trivial cycle `(1,1)`, not a new fact.

**Closing status.** What this subsection changes: the diagonal compatibility locus of `14.15.3`(c) now has an equivalent boundedness criterion (`14.15.4.5`) naming its archimedean content exactly (the three-notion remark above), and the finite-window question is fully closed — no finite two-sided obstruction exists, ever (`14.15.4.2`). What it does not change: the Bridge is exactly as open as `14.15.3`'s closing status left it. Characterizing which words are integrally realized — beyond the definition, the trivial direction (`14.15.3.6`), and the equivalence theorem's boundedness criterion — remains the Bridge itself, reserved for equidistribution (typical words, aeh.md §13) or rigidity (periodic words, `16.4.4`) exactly as before. Per the brief's stop line: no growth study of `H`, no characterization attempt on the diagonal locus beyond the equivalence theorem, no cycle-exclusion attempt, and no equidistribution proof attempt follow from anything above.

## 14.15.5. The converse of the trivial diagonal direction: the admissibility-class lemma and the positive-integer diagonal

*(Proves the converse of the trivial direction `14.15.3.6`: `W` is integrally realized iff `y₂(W) = y₃(W)` at a single positive odd integer — completing `14.15.3`(c)'s formulation of the diagonal locus, not narrowing it (the framing paragraph below). Item (b) completes a formulation; the Bridge is unmoved; the `−5` instance in (c) is a reconciliation with classical facts, not a discovery.)*

**Framing (read before the theorems below).** Proving the converse **completes the formulation** of `14.15.3`(c); it does not open the locus. The combined statement — a bi-infinite word is integrally realized iff `y₂(W) = y₃(W) =` a single positive odd integer — is an exact characterization of the diagonal locus **in terms of the word's own two adelic limits**, and deciding whether those limits coincide at a positive integer, for any given family of words, is exactly as hard as it was: it *is* the Bridge (bridge.md §16), under a sharper name. Nothing about which words satisfy it has been learned here, except that the classical negative cycles reappear as negative diagonal points (`(c)` below).

### (a) The admissibility-class lemma

**Setup and the order convention.** Write a finite left word two ways, matching two contexts already on file. `V = ((m_{−1},r_{−1}),…,(m_{−n},r_{−n}))` — shallowest letter first, `m_{−1}` nearest the present door — is the natural indexing for "a window of the past" (matching `14.15.3`(b)'s own bi-infinite word notation). `14.14.8.2`'s composed-affine constants `A_n, B_n`, however, are defined for a word processed **in application order** — the letter applied first (to the innermost, deepest door) listed first — which for a backward chain read forward is `V`'s **reverse**, `((m_{−n},r_{−n}),…,(m_{−1},r_{−1}))`, exactly `14.15.3`(b)'s own `W_{(-n:0)}`. Below, `A_n, B_n` always mean `14.14.8.2` applied to this deepest-first ordering, and `M_n := Σᵢ m_{−i}` (one quantity either way, since it is just a sum).

**Theorem 14.15.5.1 (admissibility-class lemma).** For a finite left word `V = ((m_{−1},r_{−1}),…,(m_{−n},r_{−n}))`, `M_n = Σᵢ m_{−i}`: among positive odd integers, the `z` admitting the letter-prescribed backward chain to depth `n` (each step existing per `14.15.4.1`'s criterion, applied successively) form **exactly one residue class mod `3^{M_n}`, namely `B_n mod 3^{M_n}`**, `A_n, B_n` the composed-affine constants of `V` read deepest-first, as above.

**Remark (liveness is not assumed at intermediate doors — review addition, 2026-07-16).** `14.15.4.1` is stated for a *live* door `z`, but its proof nowhere uses `3 ∤ z`: the existence criterion, the predecessor formula, and the uniqueness argument hold verbatim for every odd `z` — the same generality `14.15.1.1`'s remark records for `stratum` and `G`. The induction below applies the criterion at intermediate chain doors regardless of their liveness (a finite prefix's deepest door may be dead); the chain semantics here does not require liveness, and it enters only at `14.15.5.3`'s infinite union, where every door is a `G`-image and liveness is automatic.

**Proof.** Induction on `n`. *Base* (`n=1`): by `14.15.4.1`, `z` admits a predecessor on letter `(m_{−1},r_{−1})` iff `3^{m_{−1}} | 2^{r_{−1}}z+1`, iff `z ≡ -2^{-r_{−1}} (mod 3^{m_{−1}})` (`2` a unit mod every power of `3`) — one class. `B_1 = β_{(m_{−1},r_{−1})}` (the length-one word's own composed constant), and `β = (3^m-2^m)2^{-(m+r)} = 3^m2^{-(m+r)} - 2^{-r} ≡ -2^{-r} (mod 3^m)` directly (the first term vanishes mod `3^m`, being `3^m` times a `3`-adic unit). So the base class is exactly `B_1 mod 3^{m_{−1}}`.

*Step.* Suppose the depth-`k` class is exactly `{z ≡ B_k (mod 3^{M_k})}` (`B_k` = the deepest-first constant of `((m_{−k},r_{−k}),…,(m_{−1},r_{−1}))`), and on this class the letter-prescribed chain's deepest door is `y_{−k}(z) = (z-B_k)/A_k` (`14.14.8.2`'s own affine relation `z = A_k y_{−k} + B_k`, solved for `y_{−k}`, using `v_3(A_k)=M_k` to divide). Write `A_k = 3^{M_k}U_k`, `U_k` a `3`-adic unit; for `z = B_k + 3^{M_k}w`, `y_{−k}(z) = w/U_k` — linear in `w`, no additive shift. Extending to depth `k+1` needs `y_{−k}(z)` admissible on the new letter `(m_{−(k+1)},r_{−(k+1)})`: by the base-case identity, admissibility reads `y_{−k}(z) ≡ β_{new} (mod 3^{m_{−(k+1)}})`, i.e. (multiplying by the unit `U_k`) `w ≡ β_{new}U_k (mod 3^{m_{−(k+1)}})` — one class for `w`, hence `z = B_k+3^{M_k}w` lands in exactly one class mod `3^{M_k+m_{−(k+1)}} = 3^{M_{k+1}}`, namely `B_k + 3^{M_k}·(β_{new}U_k) = B_k+A_kβ_{new}`. This is exactly `B_{k+1}` under the recursion `B_{k+1}=A_kβ_{new}+B_k` — the **prepend** form `14.15.3.3`'s own proof uses to prepend a new deepest letter (verified below numerically identical, for the same deepest-first word, to `14.14.8.2`'s literal append-form recursion, by associativity of affine composition). ∎

**The order-convention finding, recorded precisely (per the brief).** `14.14.8.2` states its recursion as `B_{i+1}=α_iB_i+β_i`, letters processed **in application order, appending each new letter at the shallow end** of the composition built so far. This theorem's own induction grows admissibility depth by **prepending** a new *deepest* letter — the natural direction, since a longer backward chain is a *deeper* chain, not a *later* one — and the recursion matching this direction is `B_{k+1}=A_kβ_{new}+B_k` (the old constant scales the new letter's own `β`, then adds the old `B_k`), structurally different from `14.14.8.2`'s one-step form (`α_iB_i+β_i`, new letter's `α` scales the old `B_i`). Both compute the *same* `B_n` for the *same* deepest-first word — associativity of affine-map composition, verified below (`2,000/2,000`) — so there is **no numerical mismatch**; but the two recursions are genuinely different bookkeeping routes for the same object, and it is the prepend form, not `14.14.8.2`'s literal statement, that is natural for this theorem's induction direction. This is the reconciliation the brief asks for, not a defect in `14.14.8.2`.

**Corollary 14.15.5.2 (synchronization sharpened).** This strengthens `14.14.8.3` from *"chains that exist agree with `B_n`"* to *"existence itself is the congruence with `B_n`"* — the residue condition is not merely necessary for a realized chain's value, it is equivalent to the chain's existence in the first place.

**Verified** — `experiments/diagonal_converse.py`, fresh code (imports nothing from `realization_height.py`, `itinerary_coding.py`, `block_map.py`, or `door_seam.py`). Base-case identity (`β ≡ -2^{-r} mod 3^m`, exact `Fraction` reduction): `2,000` random `(m,r)`, `0` failures. Recursion reconciliation (`compose_append` vs. the prepend recursion, same deepest-first word, exact `Fraction` equality of both `A_n` and `B_n`): `2,000` random words, length `1`–`6`, `0` mismatches. Admissibility-class lemma, brute force over odd `z`, both directions (soundness: every admissible `z` found lies in the predicted class; completeness: every `z` in the predicted class below the scan bound is admissible): `400` random words (matching the pre-check's own count, fresh code), letters capped `m≤3,r≤4`, length `≤4`, `0` failures either direction. Synchronization-sharpened check (existence vs. congruence, tested both congruent and non-congruent `z` against the same word): `3,000` `(word,z)` checks, `0` failures (seeds `45001`–`45004`, 2026-07-16).

### (b) The converse theorem and the combined characterization

**Theorem 14.15.5.3 (converse of `14.15.3.6`).** If a bi-infinite word `W` has `y₂(W) = y₃(W) = y₀`, a single **positive odd integer**, then `W` is integrally realized by `y₀`.

**Proof.** *Forward half.* `y₂(W)=y₀` places `y₀` in every forward cylinder of `W`'s right-infinite half (`14.15.3.1`, the nested-cylinder construction), so `y₀`'s deterministic forward orbit follows `W`'s future exactly (Theorem `14.15.3.2`'s injectivity argument applied to one integer, as in `14.15.3.6`'s own proof).

*Backward half.* `y₃(W)=y₀` gives, by Theorem `14.15.3.3`'s Cauchy estimate (`v_3(B_{n+1}-B_n)=M_n`, strictly increasing in `n`), `v_3(y₀-B_n) ≥ M_n` for every `n` — i.e. `y₀ ≡ B_n (mod 3^{M_n})` for every `n`. By the admissibility-class lemma (`14.15.5.1`), this means the letter-prescribed backward chain behind `y₀` exists to *every* depth `n`. By `14.15.4.1`'s uniqueness, the depth-`(n+1)` chain's nearest `n` entries coincide exactly with the depth-`n` chain (the mechanism `14.15.4.5`'s own proof already makes explicit, cited not re-derived), so the chains union into one infinite chain `y_{−1},y_{−2},…` realizing `W`'s entire left-infinite half.

*Liveness, derived.* No liveness hypothesis is used anywhere above. `y₀` itself is a `G`-image (`y₀=G(y_{−1})`, from the depth-`1` step, guaranteed to exist by the backward half), and `G`'s image is always live regardless of its input (`14.14.3.2`(3) / `14.14.7.1`), so `3 ∤ y₀` automatically; likewise every `y_{−i}` (`i≥1`) is a `G`-image of the next-deeper chain door, hence live automatically. So `y₀`, with this chain, witnesses that `W` is integrally realized (Definition `14.15.3.5`). ∎

**Corollary 14.15.5.4 (the combined characterization).** For a bi-infinite word `W`:

```text
W integrally realized  ⟺  y₂(W) = y₃(W) ∈ the positive odd integers  ⟺  (H_{p,q}(W))_{p,q} bounded.
```

Three names for one locus: the first equivalence is `14.15.3.6` (⟹, the trivial direction) plus `14.15.5.3` (⟸, this section); the second is `14.15.4.5`'s equivalence theorem, cited not re-derived.

**Verified** — `experiments/diagonal_converse.py`, fresh code, functions `test_converse_mechanism` and `test_forward_half_nesting`. The theorem's constituent mechanisms, on real instances (not an abstract-word brute force, which is infeasible — bi-infinite words are uncountable): random positive live doors `y₀ < 10^5` with real letter-prescribed backward chains to depth `12` (letters drawn honestly by `find_live_predecessor`, not chosen to fit a target) — Cauchy estimate `v_3(y₀-B_n)≥M_n` at every depth `n=1..12` (exact `Fraction`/valuation arithmetic): `300` chains built, `3,600` depth checks, `0` failures. Reconstruction (rebuilding the chain from `y₀` and the recorded letters alone, via `unique_predecessor`, without consulting the already-built chain, then checking it reproduces the chain exactly — the truncation-compatibility/uniqueness mechanism the proof leans on): `300` chains, `0` mismatches. Liveness derived (every chain door, and `G`'s own image of the deepest one, automatically live, no hypothesis assumed): `300` chains (`3,600` chain doors plus `300` `G`-image checks), `0` failures. Forward-half nesting (`y₀`'s residue mod `2^{S_n+1}` matches the word's own cylinder representative, via an independent Hensel-lifting construction rather than brute-force scanning): `2,000` random `(y₀,n)`, `n≤10`, `0` failures (seeds `45005`–`45006`, 2026-07-16).

### (c) The negative-diagonal reconciliation

The single-letter periodic word `W = ((2,1))^∞`. Composed-affine fixed point (`14.14.8.4`, `n=1`): `α=3^2·2^{-3}=9/8`, `β=(9-4)·2^{-3}=5/8`, `y^* = β/(1-α) = (5/8)/(-1/8) = -5` exactly. Extending `stratum`/`G`'s defining formulas (`14.15.1.1`) to negative odd integers — the same algebra (multiplication, exact division by a power of `2`, `2`-adic and `3`-adic valuations), sign-independent throughout, no new theorem needed — gives `stratum(-5)=(2,1)` and `G(-5)=-5`: `-5` is a `G`-fixed point on the word's own letter, matching `y^*` exactly. Identified with the classical accelerated map `T`: `T(-5)=-7`, `T(-7)=-5`, the negative `T`-cycle `{-5,-7}` (`m=2` matches the cycle's block length, `r=1` its own exit valuation), read in door coordinates as this `G`-fixed point at return time `2` (`14.14.7.1`'s block-map identity).

By the combined characterization (`14.15.5.4`), since `y₂(W)=y₃(W)=-5` is a *negative* integer, `W` is **not** integrally realized — no positive live integer realizes this bi-infinite word, though (`14.15.4.2`) every finite two-sided window of it *is* positively realized. So the positive realization height escapes: `H_{n,n}(W) → ∞`.

**Numerical instance (the one prescribed check, not a growth study).** `H_{n,n}(W)`, `n=1..8`, computed exactly (an efficient CRT construction — the forward cylinder's representative mod `2^{S_n+1}` via a direct Hensel-lifting construction, `14.15.1.4`'s own induction reimplemented constructively rather than by scanning, combined with the backward admissible class mod `3^{M_n}` (`14.15.5.1`) by the Chinese remainder theorem, then scanning the resulting arithmetic progression of increasing candidates for the first with a live deepest door — cross-checked against brute-force scanning at `n=1,2,3`, `0` mismatches, confirming the method finds the true minimum, not merely a witness):

```text
n=1: H = 283                     n=5: H = 7,739,670,523
n=2: H = 20,731                  n=6: H = 557,256,278,011
n=3: H = 1,492,987                n=7: H = 40,122,452,017,147
n=4: H = 107,495,419              n=8: H = 2,888,816,545,234,939
```

Strictly increasing at every step checked, `n=1..8`; no shortfall (the search always found a live-deepest-door candidate within the second CRT-progression step). This is the single named instance the brief permits, not a growth study: no rate, no asymptotic, no attempt at a general bound on `H`.

**Reconciliation with the classical picture (one sentence).** The classical negative `3x+1` cycles — `{-1}`, `{-5,-7}`, and the period-`7` (accelerated) cycle `{-17,-25,-37,-55,-41,-61,-91}` — are the standard reason the conjecture is stated over the positive integers (`T` is defined on the positive integers from the outset, spine.md line `67`/`206`; `state(y)` and `door` inherit `y>0` throughout `14.14`–`14.15`); this section's `-5` instance is that same fact, encountered here as a point where the two-sided diagonal coincides at an integer that fails only the sign condition, cleanly separating "coincide at an integer" (weaker, holds here) from "coincide at a *positive* integer" (the actual locus).

**Verified** — `experiments/diagonal_converse.py`, function `test_negative_fixed_point` (exact `y^*=-5`, `stratum(-5)=(2,1)`, `G(-5)=-5`, `T(-5)=-7`, `T(T(-5))=-5`, all matched exactly) and `test_height_escape` (the `H_{n,n}` table above, `n=1..8`, cross-checked against independent brute-force scan at `n=1,2,3` — `0` mismatches, `0` shortfalls) (2026-07-16).

### (d) Accounting and closing status

**Accounting.** The equivalence gives the diagonal locus its third and sharpest name: *the words whose two adelic limits meet at a positive integer.* This is a completion of `14.15.3`(c)'s formulation, not new leverage — deciding `y₂(W)=y₃(W)` for any word family beyond the periodic case remains exactly the Bridge (bridge.md §16), under this name. Bridge status unchanged (`14.14.6`).

**Periodic words.** The characterization plus `14.14.8.4` reproduces the classical rational-cycle-candidate dichotomy exactly: the composed fixed point `y^*` is always rational (`14.14.8.4`); it is a positive integer iff the word is integrally realized (`14.15.5.4`) iff, for a period matching an actual cycle, `y^*` satisfies cycles.md `§12.1`'s own integrality condition, under a new name — not a new exclusion lever, explicitly (`14.14.8.4`'s own reconciliation, cited not repeated).

**Closing status.** What changed: the diagonal locus of `14.15.3`(c) now has a completed characterization — `14.15.5.4`'s three-way equivalence — with the trivial direction (`14.15.3.6`) and its converse (`14.15.5.3`) both proved. The admissibility-class lemma (`14.15.5.1`) is an independently useful sharpening of `14.14.8.3`. The `-5` instance (`c`) reconciles the locus's positivity condition with the classical negative-cycle fact, concretely. What did not change: which words lie on the locus — beyond the definition, both directions of the trivial/converse pair, and the periodic-word reconciliation — remains open, exactly as `14.15.3`(c)/`14.15.4`(d) left it: equidistribution for typical words (aeh.md §13), rigidity for periodic words beyond the classical candidate (`16.4.4`). Per the brief's stop line: no attempt to decide `y₂=y₃` for any word family beyond the periodic instance; no growth study of `H` beyond the single `-5` table above; no cycle-exclusion attempt; no equidistribution proof attempt; no extension to a signed/two-sided-integer realization theory beyond this section's one reconciliation sentence.

## 14.15.6. The signed diagonal: `14.15.1`–`14.15.5` over the nonzero odd integers

*(Origin: `briefs/diagonal-converse-findings.md` — the `14.15.3`–`14.15.5` apparatus is sign-independent, with positivity entering only as a hypothesis location. This layer relocates a hypothesis; it does not move the Bridge (bridge.md §16): the sign restriction that ran through `14.15.3`–`14.15.5` is a sector choice, not a structural asymmetry, apart from one genuine exception recorded precisely in (a) below.)*

### (a) The signed domain, the singular point, and sign preservation

**Definition 14.15.6.1 (signed door space).** The **signed door space** is the set of nonzero odd integers `y ≠ −1`. As before, `y` is **live** iff `3 ∤ y`. `stratum(y) = (m,r)` and `G(y)` are computed by `14.15.1.1`'s formulas verbatim (`m = v_2(y+1)`, `q=(y+1)/2^m`, `r=v_2(3^mq-1)`, `G(y)=(3^mq-1)/2^r`) — algebra that nowhere references the sign of `y`.

**Theorem 14.15.6.2 (totality and sign preservation).** For every `y` in the signed door space:

1. `stratum(y)` and `G(y)` are defined (`m,r` both finite).
2. `3 ∤ G(y)` (`G`'s image is always live).
3. `G(y)` has the **same sign as `y`**, without exception — `G(y) > 0` whenever `y>0`, and `G(y) < 0` whenever `y<0`.
4. **The one genuine sector asymmetry.** `G(y) = −1` is possible only when `y<0` — e.g. `G(−3) = −1` exactly — never when `y>0`. Since `−1` is excluded from the signed door space, this is a **forward mortality** the negative sector alone carries: a live negative door's single `G`-step can leave the domain, undefined at every step thereafter (`m=v_2(0)=∞`), whereas `14.14.3.2`(3)'s totality guarantees a positive door's forward orbit never runs out of room to continue.

**Proof.** (1)–(2) are `14.15.1.1`'s remark and `14.14.3.2`(3)'s argument, cited not re-derived: `y+1 = 2^m3^aΩ` for some (possibly negative) `Ω` and `D=m+a≥1` is exactly the state decomposition `14.6.5.1` supplies for any nonzero `y+1`, and the argument that `A := 3^Dq/3^a\cdot(\ldots)` — concretely `val = 3^mq-1 ≡ -1 ≡ 2 \pmod 3` — is a nonzero even integer uses only `D≥1` and arithmetic mod `3`, neither of which references the sign of `Ω` or `y`; so `m,r` are finite and `3 \nmid G(y)` exactly as in the positive case. (3) is new algebra, the one place positivity entered `14.15.1`–`14.15.5` structurally rather than as a hypothesis label: if `y>0` then `q=(y+1)/2^m>0` is a positive odd integer, so `3^mq ≥ 3` and `val = 3^mq-1 ≥ 2 > 0`, giving `G(y)=val/2^r>0`. If `y<0` (so `y≤-3`, the only other case in the signed domain), then `y+1≤-2<0`, so `q=(y+1)/2^m<0` is a negative odd integer, `q≤-1`, giving `3^mq≤-3^m≤-3` and `val=3^mq-1≤-4<0`, so `G(y)=val/2^r<0`. Both cases are exhaustive and give a strict sign match — (3). (4): by the case split just proved, `G(y)>0` whenever `y>0`, so `G(y)=-1` is impossible for positive `y` — the positive half of (4). For the negative half, `G(y)=-1` means `val=-2^r`, i.e. `3^mq=1-2^r`; at `m=1,r=2`: `q=(1-4)/3=-1`, giving `y=2\cdot(-1)-1=-3` — a valid negative door (`q` odd, matching `m=1` forced exactly as in `14.15.4.1`'s proof pattern) — so a solution exists, and `G(-3)=-1` follows by direct computation from Definition `14.15.6.1`. ∎

**Content.** Sign preservation (3) is unconditional — `-1` is a negative value, not a signless one, so there is no exception to "same sign" as a *sign* statement. The asymmetry is a *domain* fact: the signed door space specifically excludes `-1`, and (4) shows the negative sector's forward map can land exactly there while the positive sector's provably cannot (positivity of `G(y)` for `y>0` rules it out automatically, since `-1` is not positive). This is the precise content behind the pre-check's "one-sided forward mortality," stated against `14.14.3.2`(3): totality is not violated (`G` is still a function wherever it is defined, per (1)–(2)), but the negative sector loses the *guarantee of re-entry* that the positive sector has for free.

**Theorem 14.15.6.3 (signed unique-predecessor lemma).** `14.15.4.1`'s statement, with "positive" replaced throughout by "the same sign as `z`, and never `−1`": fix `z` in the signed door space and a letter `(m,r)`, `m,r≥1`. There is at most one integer `y` with `G(y)=z` and `stratum(y)=(m,r)`, namely `y = 2^m(2^rz+1)/3^m − 1`, an integer iff `3^m \mid 2^rz+1`, and when it is, `y` automatically has the same sign as `z`, is never `−1`, and lies on stratum exactly `(m,r)`.

**Proof.** Uniqueness and the forced stratum are `14.15.4.1`'s proof verbatim — it uses only that `q` is odd and that `3^mq-1=2^rz` pins `v_2` and `v_3` exactly, neither step referencing the sign of `z`. The **only changed step** is the sign conclusion: `q=(2^rz+1)/3^m` is a nonzero integer whenever it exists (`2^rz+1` is odd, hence nonzero, and dividing an odd number by `3^m` preserves nonzero-ness), so `q≥1` or `q≤-1`. If `z>0`: `2^rz+1>0`, so `q>0`, i.e. `q≥1`, giving `y=2^mq-1≥2^m-1≥1>0` — the same conclusion `14.15.4.1` reaches, now derived from `q≥1` rather than assumed. If `z<0`: `2^rz+1 ≤ 1-2^r ≤ -1<0` (`r≥1`), so `q<0`, i.e. `q≤-1`, giving `y=2^mq-1≤-2^m-1≤-3<0` — negative, and strictly `≤-3`, so `y≠-1` is not an added hypothesis but a forced consequence of the same bound. ∎

**Content.** This is exactly `14.15.4.1`'s "quotient of two positive numbers is positive" argument, generalized to "quotient of two same-sign nonzero numbers has that sign" — the one place `14.15.4.1`'s proof used positivity structurally, per the off-brief finding that prompted this brief. It also explains precisely why `−1` cannot be produced by the letter-prescribed predecessor construction at all (unlike `G`, which *can* output `−1` per `14.15.6.2`(4)): the forced bound `|y|≥2^m-1≥1` together with `y≠-1` exactly (`y≤-3` on the negative branch) rules it out algebraically, not by a side condition. Read together with `14.15.6.2`(4), `−1` is reachable as a `G`-image but never as a letter-prescribed predecessor — the precise, one-sided sense in which it sits outside the ordinary backward branching structure that governs every other point of the signed door space.

**Verified** — `experiments/signed_diagonal.py`, fresh code (imports nothing from `diagonal_converse.py`, `realization_height.py`, `itinerary_coding.py`, `block_map.py`, or `door_seam.py`), functions `test_domain_totality_and_sign_preservation`, `test_positive_sector_never_mortal`, `test_negative_forward_mortality`, `test_no_positive_forward_mortality`, `test_signed_unique_predecessor`, `test_predecessor_forced_bound`, `test_round_trip_signed`. Totality and sign preservation: `20,000` random nonzero odd `y≠-1` (`|y|<10^6`, both signs), `0` exceptions, `0` sign mismatches. Positive-sector non-mortality: `10,000` random positive `y`, `G(y)≥1` and `G(y)≠-1` in every case, `0` failures. Negative forward mortality: exhaustive scan of negative odd `y` with `3≤|y|<2000` finds `7` solutions to `G(y)=-1` (`y ∈ {-3,-11,-29,-43,-171,-683,-1821}`), `G(-3)=-1` exact; mirror scan of `200,000` positive odd `y` finds `0` solutions. Signed unique-predecessor lemma: `20,000` random `(z,m,r)` (`z` both signs, `|z|<10^6`, `m<8`, `r<10`), `2,077` admissible, `0` sign mismatches, `0` landed on `-1`, `0` round-trip failures (stratum and `G`-image both reproduced exactly). Forced-bound algebra (the intermediate `q`, checked directly): `20,000` draws, `2,103` admissible, `0` bound violations. Round-trip sanity, both signs: `8,000` random `y≠-1` (`|y|<10^7`), `0` failures (seeds `55001`–`55005`, 2026-07-16).

### (b) The signed admissibility-class lemma and the two-sector bicylinder

**Theorem 14.15.6.4 (signed admissibility-class lemma).** `14.15.5.1`'s statement with "among positive odd integers" relaxed to "among nonzero odd integers `z` in the signed door space (`z≠-1`)": for a finite left word `V=((m_{−1},r_{−1}),…,(m_{−n},r_{−n}))`, `M_n=Σm_{−i}`, the `z` admitting the letter-prescribed backward chain to depth `n` form exactly one residue class mod `3^{M_n}`, namely `B_n mod 3^{M_n}`.

**Proof.** `14.15.5.1`'s own induction, verbatim, with no step altered. The base case cites `14.15.4.1`'s *existence* criterion — `3^{m_{−1}} \mid 2^{r_{−1}}z+1` — a pure divisibility condition on `z` that never referenced positivity in the first place (only `14.15.4.1`'s separate *sign* conclusion did, per `14.15.6.3` above, and that conclusion is not used anywhere in `14.15.5.1`'s congruence-class argument). The inductive step's algebra (`y_{−k}(z)=(z-B_k)/A_k`, the unit `U_k=A_k/3^{M_k}`, the new class `z=B_k+3^{M_k}w`) is likewise pure `3`-adic residue arithmetic, with no sign hypothesis anywhere. So the proof transfers to `z` of either sign without modification — this is the "sign-blind" claim of `briefs/diagonal-converse-findings.md`, now checked rather than conjectured. ∎

**Content.** `14.15.5.1`'s proof used positivity nowhere directly; it only *inherited* a sign conclusion from `14.15.4.1`'s citation, and that conclusion plays no role in deriving the residue class itself. This is the precise sense in which the admissibility-class lemma is "sign-blind": the class computation and the sign of its members are logically independent facts about the same construction.

**Theorem 14.15.6.5 (two-sector bicylinder).** The finite bicylinder corollary (`14.15.4.2`) holds **per sector**: for finite words `V` (past, length `p`) and `U` (future, length `q`), every finite two-sided window `W=V{+}U` is realized by an actual live integer segment of **each** sign — the residue class mod `2^{S+1}` (`S=S(W)`, Theorem `14.15.1.5`) meets each sign in infinitely many live members.

**Proof.** As in `14.15.4.2`, concatenate `V,U` into `W` and apply Theorem `14.15.1.5`: the followers of `W` form exactly one residue class mod `2^{S+1}`, `{y_{rep}+k\cdot2^{S+1}:k\in\mathbb Z}`, unbounded in both directions. Since `2^{S+1}` is coprime to `3`, successive members in *either* direction (increasing or decreasing `k`) cycle through residues mod `3` with period `3` (`14.15.1.7`'s own argument, which never assumed a direction), so at least one in every three consecutive members on each side is live. Pick a live representative `y_{−p}` of the requested sign; the remaining chain `y_{−p+i}:=G^i(y_{−p})` realizes `W` exactly and stays live throughout by `14.15.6.2`(1)–(2), applied at each step regardless of sign, exactly as `14.15.4.2`'s own proof proceeds. The one point needing a signed check — whether such a chain can pass through `−1` partway and break off — does not arise: membership in the composed cylinder class is *equivalent* to following `W` in full (Lemma `14.15.1.4`'s induction constructs the class exactly as the set of integers satisfying the stratum conditions at every step, an iff, not merely a necessary condition), and `−1` never lies in **any** single-stratum residue class in the first place (`14.15.1.3`(i)'s congruence: `−1` trivially satisfies the class's first, purely divisibility, condition for every `m`, since `y+1=0` is divisible by every power of `2`, but its own `q=(y+1)/2^m=0` is even, while the class's own residue `3^{−m}(1+2^r) mod 2^{r+1}` is always odd — a mismatch, so `−1` is excluded from every cylinder class structurally, not merely because no chain happens to reach it). Consequently every candidate genuinely drawn from the class already avoids `−1` at every intermediate position, with nothing extra to verify. ∎

**Content.** This extends `14.15.2`'s verdict — the word is free at every finite level — one sector at a time: prescribing a sign costs nothing either, at any finite window. Together with `14.15.6.4`, both halves of the finite apparatus (`14.15.1`–`14.15.4`) transfer to the signed domain with no obstruction anywhere at finite depth.

**Verified** — `experiments/signed_diagonal.py`, fresh code, functions `test_admissibility_class_signed`, `test_two_sector_bicylinder`, `test_minus1_never_in_cylinder_class`. Signed admissibility-class lemma: `150` random words (length `≤3`, `m<3`,`r<4`), existence-vs-congruence checked for both signs over the full scan range (`|z|<z_bound`, `z_bound=min(4\cdot3^{M_n},3000)`), `44,370` `(word,z)` checks, `0` failures. Two-sector bicylinder: `377` random windows (`p,q≤3`, `m,r≤3`), a live segment of **each** sign constructed and independently re-verified to realize the full window exactly, `0` failures on either side. The `−1`-exclusion structural check: `3,000` random `(m,r)` pairs (`m,r<10`), `−1 mod 2^{m+r+1}` compared against the class's own residue, `0` matches (seeds `55011`–`55013`, 2026-07-16).

### (c) The signed characterization

**Definition 14.15.6.6 (signed integral realization).** As `14.15.3.5`, with doors drawn from the signed door space: a bi-infinite word `W` is **integrally realized** iff some live door `y_0 ≠ −1` follows the right-infinite half exactly and has an actual integer chain of live-door predecessors realizing the left-infinite half exactly. Liveness and `−1`-avoidance need no separate hypothesis, exactly as in `14.15.5.3`'s proof: any realizing `y_0` is forced to be a `G`-image of its own first backward-chain door (`14.15.6.2`(2) gives liveness; and `y_0 = −1` is impossible because `y_0` must carry a well-defined forward orbit realizing `W`'s future, while `stratum`/`G` are undefined at `−1` — one sentence, no separate argument needed).

**Theorem 14.15.6.7 (signed diagonal characterization).** `W` is integrally realized by a nonzero odd integer `y_0` ⟺ `y_2(W) = y_3(W) = y_0 ∈` the nonzero odd integers.

**Proof.** The positive case is `14.15.3.6` (⟹) plus `14.15.5.3`/`14.15.5.4` (⟸), cited not re-proved. The negative case runs the identical argument through `14.15.6.3`–`14.15.6.5` in place of `14.15.4.1`/`14.15.5.1`/`14.15.4.2`: `14.15.3.6`'s trivial-direction proof (`y_2 = y_0` from following every finite forward prefix, `y_3 = y_0` from the Cauchy limit of `14.15.3.3`) never used the sign of `y_0` — it is pure `2`-adic and `3`-adic nesting, exactly as already established generally in `14.15.1`–`14.15.3`. `14.15.5.3`'s converse proof needs, at each step: the admissibility-class lemma to convert the `3`-adic Cauchy estimate into backward-chain existence (`14.15.6.4`, proved sign-blind), truncation-compatibility from the letter-prescribed predecessor's uniqueness (`14.15.6.3`, proved sign-blind), and liveness/`−1`-avoidance as a *derived*, not assumed, fact (`14.15.6.2`–`14.15.6.3` again). Every ingredient is now available in the signed setting, so the proof transfers verbatim with `y_0` ranging over either sign. ∎

**Content.** `−1` is impossible as a value of `y_0` here for the same one-sentence reason given in Definition `14.15.6.6`: forward realization of any `W` requires a well-defined forward orbit, and `stratum`/`G` are undefined at `−1` — the diagonal criterion excludes it automatically, without a separate exclusion clause, exactly as `14.15.3`(a)'s own Remark already excludes it from every `y_2(W)`.

**Definition 14.15.6.8 (per-sector window and height).** Fix a bi-infinite word `W` and a window `(p,q)` around `W`'s fixed origin. For a sign `σ ∈ {+1,−1}`, let

```text
R^σ_{p,q}(W) := { y_0 : y_0 a live door of sign σ (automatically y_0≠−1),
                  stratum(G^j(y_0))=(m_j,r_j) for j=0,…,q−1,
                  and the 14.15.6.3 letter-prescribed backward chain
                  exists to depth p with live deepest door },
```

and `H^σ_{p,q}(W) := min\{|y_0| : y_0 ∈ R^σ_{p,q}(W)\}` whenever `R^σ_{p,q}(W) ≠ ∅`. For `σ=+1` this is `14.15.4.3`'s own `R_{p,q}`/`H_{p,q}`, restated only for uniform notation; `σ=−1` is the new **negative-sector height** the brief asks for.

**Theorem 14.15.6.9 (per-sector basic properties).** `14.15.4.4`'s three properties hold for each sign `σ` separately: `R^σ_{p,q}(W) ≠ ∅` for every `p,q≥0`; `R^σ_{p,q+1}(W) ⊆ R^σ_{p,q}(W)` and `R^σ_{p+1,q}(W) ⊆ R^σ_{p,q}(W)`; `H^σ_{p,q}(W)` is a positive integer, nondecreasing in `(p,q)`.

**Proof.** Non-emptiness is `14.15.6.5`(the two-sector bicylinder) applied to `W`'s own length-`p` past and length-`q` future window, on sign `σ`. The inclusions are `14.15.4.4`(2)'s own set-theoretic argument verbatim: a longer forward or backward realization restricts to a shorter one, and the deepest retained door of a truncated backward chain is a `G`-image, hence live automatically (`14.15.6.2`(2)) — neither step references sign. For (3): `|y_0|` ranges over the positive integers regardless of `σ` (the map `y_0 ↦ |y_0|` is an order-reversing bijection between the negative integers and the positive integers, and the identity map on the positive integers when `σ=+1`), so the minimum of a nonempty subset of the positive integers exists exactly as before, and the inclusion-implies-ordered-minima argument of `14.15.4.4`(3) applies to `|y_0|` unchanged. ∎

**Theorem 14.15.6.10 (per-sector equivalence theorem).** For each sign `σ`: `W` is integrally realized by a door of sign `σ` iff `(H^σ_{p,q}(W))_{p,q}` is bounded, iff it is eventually constant.

**Proof.** `14.15.4.5`'s three-part proof (bounded ⟺ eventually constant; realized ⟹ bounded; bounded ⟹ realized) uses exactly three ingredients, checked here one at a time: (a) well-ordering of the positive integers, applied to `|y_0|` rather than `y_0` directly — unaffected by sign, per `14.15.6.9`'s proof; (b) the nested-inclusion property of `R^σ_{p,q}` — `14.15.6.9`(2), sign-independent; (c) truncation-compatibility of backward chains, which rests entirely on the letter-prescribed predecessor's *uniqueness* (`14.15.6.3`), proved sign-blind in item 1. No other fact is used anywhere in `14.15.4.5`'s proof. Substituting `|y_0|` for `y_0` throughout and citing `14.15.6.3`/`14.15.6.5`/`14.15.6.9` in place of `14.15.4.1`/`14.15.4.2`/`14.15.4.4` reproduces the proof exactly, sign held fixed. ∎

**Content — the height transfer, checked precisely, not assumed.** Every step of `14.15.4.4`–`14.15.4.5` transfers without modification once `|·|` replaces the positive minimum; no snag was found. This was checked in both directions, not only asserted: the two known negative periodic diagonal points — `-5` (`14.15.6`(d) below) and `-17` — are verified members of their own `R^-_{n,n}` for `n=0,…,6`, giving `H^-_{n,n} ≤ 5` and `≤ 17` respectively at every window tested (**bounded**, the height-mechanism form of the reconciliation in `14.15.6`(d)); and the trivial word `(1,1)^∞`, whose *unique* rational fixed point `14.14.8.4` supplies is the positive integer `1` (never a negative integer, so it cannot be signed-integrally-realized by any negative door), has a negative height that **escapes** exactly as the equivalence theorem predicts — computed exactly by a CRT-plus-progression-scan construction generalizing `14.15.5`(c)'s own method, `n=1,…,5`, cross-checked against brute force at `n=1,2`, strictly increasing throughout (`H^-_{n,n}(y=23,287,3455,41471,497663)` for `n=1,…,5`). Fixed-origin nested-window monotonicity was also checked directly on real negative integer orbits (mirroring `14.15.4`(c)'s own check, one sector at a time): `20` real negative orbits, `H^-_{n,n}` at `n=1,2` computed by exhaustive search, `0` shortfalls, `0` monotonicity violations, `18/20` strictly grew. The criterion is non-vacuous and behaves correctly in both the bounded and the escaping direction, in the negative sector exactly as in the positive one.

**Verified** — `experiments/signed_diagonal.py`, fresh code, functions `test_signed_converse_mechanism`, `test_forward_half_nesting_signed`, `test_negative_realized_cycles_bounded`, `test_negative_height_escapes_for_positive_word`, `test_height_monotonicity_negative_real_orbits`. Signed converse mechanism: `300` random `y_0` (both signs, `|y_0|<10^5`) with real depth-`12` backward chains, `3,600` Cauchy-estimate checks, reconstruction, and liveness/`−1`-avoidance all `0` failures. Forward-half nesting: `2,000` random `(y_0,n)` (both signs), `1,990` checked (`10` skipped for hitting forward mortality mid-orbit — the expected occasional footprint of item 1(4), not a failure), `0` mismatches. Negative realized cycles bounded: direct membership of `-5` and `-17` in their own `R^-_{n,n}`, `n=0,…,6`, all `True`; `-5`'s minimality among live negative odd integers confirmed by enumeration (`|y|<5`: only `±1` and `±3`, both excluded — singular or dead). Negative height escapes for the `(1,1)^∞` word: `n=1,…,5` computed exactly, `0` cross-check mismatches at `n=1,2` (bound `4\times10^5`), strictly increasing throughout. Monotonicity on real negative orbits: `20/20` built, `0` shortfalls (search bound `2^{15}`), `0` violations, `18/20` strictly grew (seeds `55021`–`55023`, 2026-07-16).

### (d) Reconciliations, flat

**(i) The `-5` instance, upgraded.** `14.15.5`(c)'s `-5` instance — stated there as a boundary exception to the positive-only diagonal locus — is, under the signed characterization (`14.15.6.7`), an ordinary integrally realized point: the word `((2,1))^∞` **is** integrally realized in the signed sense, by `-5`. `14.15.5`(c) is cross-referenced, not edited, per the brief.

**(ii) The period-7 cycle.** The classical period-`7` accelerated negative `T`-cycle `{-17,-25,-37,-55,-41,-61,-91}` is exactly the `G`-period-`2` word `((4,1),(3,3))`: `stratum(-17)=(4,1)`, `G(-17)=-41`; `stratum(-41)=(3,3)`, `G(-41)=-17`; the composed fixed point `y^*=-17` exactly (Corollary `14.14.8.4`'s formula, applied to this `2`-letter word); block lengths `4+3=7`, matching `14.14.7.1`'s own return-time identity and the classical cycle's length. This word is therefore integrally realized in the signed sense by `-17` (equivalently `-41`, one period-`2` orbit).

**(iii) `{-1}` stays genuinely outside the coding.** Unlike `{-5,-7}` and the period-`7` cycle, the classical fixed point `T(-1)=-1` has **no** counterpart in the signed diagonal locus: its would-be door is the singular point `-1` itself, where `stratum`/`G` are undefined (`14.15.6.1`–`14.15.6.2`). No word can be integrally realized "by `-1`," because integral realization requires a well-defined forward orbit (Definition `14.15.6.6`), and none exists at `-1`. This is recorded as the honest boundary of the signed picture, not smoothed into the other two reconciliations: the signed extension enlarges the locus from one sector to two, but it does not — and structurally cannot — reach every classical negative cycle.

**(iv) The known-cycle census.** The known `G`-periodic integer diagonal points are exactly `y=1` (word `((1,1))`, the trivial cycle), `y=-5` (word `((2,1))`, the classical `\{-5,-7\}` cycle), and `\{-17,-41\}` (word `((4,1),(3,3))`, the classical period-`7` cycle) — three points, verified exactly above. Whether the positive sector has any beyond `y=1` is precisely cycle exclusion (cycles.md §12, parked); this section supplies no new lever on that question, in either sector. The classical fact that these (together with `{-1}`, outside the signed coding per (iii)) are the only *known* `3x+1` cycles is classical, not a finding of this program: J. C. Lagarias, *The `3x+1` problem and its generalizations*, Amer. Math. Monthly 92 (1985), 3–23 (already pinned in publication.md for `14.15.3`(a)), surveys the known cycles including the negative ones; pinned again here, in the register's own style, for this specific use (publication.md).

**Verified** — `experiments/signed_diagonal.py`, fresh code, functions `test_negative_5_instance`, `test_period7_cycle`, `test_minus1_outside_coding`, `test_known_cycle_census`. The `-5` instance, independently recomputed with this file's own primitives (matching `14.15.5`(c)'s already-merged result, per AGENTS.md's independent-verification norm): `y^*=-5` exactly, `stratum(-5)=(2,1)`, `G(-5)=-5`, `T(-5)=-7`, `T(T(-5))=-5`, all matched. Period-7 cycle: `stratum(-17)=(4,1)`, `G(-17)=-41`, `stratum(-41)=(3,3)`, `G(-41)=-17`, composed fixed point `y^*=-17` exactly (`Fraction` algebra), and `7` iterations of `T` from `-17` reproduce `\{-17,-25,-37,-55,-41,-61,-91\}` in order and return to `-17` exactly. `{-1}` outside the coding: `stratum_and_G(-1)` raises as expected; `T(-1)=-1` confirmed classically (the gap is specifically in the door/stratum coding, not the classical dynamics); `2,000` random multi-letter words checked, `0` times does `-1` fall in a forward cylinder class. Known-cycle census: all three census facts (`y=1`, `y=-5`, `\{-17,-41\}`) verified together, `0` mismatches (seed `55031`, 2026-07-16).

### (e) Accounting and closing status

**Accounting.** The signed extension relocates a hypothesis, not the Bridge: the positivity that ran through `14.15.3`–`14.15.5` structurally in exactly one place — `14.15.4.1`'s sign conclusion — is now a sector choice (`14.15.6.3`), with one genuine exception recorded precisely rather than smoothed: `−1` is a one-sided singular point, reachable as a `G`-image only from the negative sector (`14.15.6.2`(4)) and never producible by the letter-prescribed predecessor construction at all (`14.15.6.3`). Deciding which words lie on the signed diagonal — in either sector — is exactly as hard as deciding it was on the positive-only diagonal: `14.15.6.7`'s characterization is a relabeling of `14.15.5.4`'s, not a new lever. Bridge status unchanged (`14.14.6`).

**What changed.** The known negative cycles — `{-5,-7}` and the period-`7` cycle — are now ordinary periodic diagonal points of the signed characterization, not boundary exceptions (`14.15.6`(d)(i)–(ii)); the finite apparatus (`14.15.1`–`14.15.4`) and the per-sector realization height transfer to the negative sector with no obstruction found at any step, checked in both the bounded and the escaping direction (`14.15.6`(c)); and the positive-domain restriction that ran through `14.15.3`–`14.15.5` is now visibly a sector choice rather than a structural asymmetry, apart from `−1`'s one-sided mortality.

**What did not change.** The Bridge (bridge.md §16) is unmoved: both escape routes — equidistribution for typical words (aeh.md §13), rigidity for periodic words beyond the classical candidates (cycles.md §12, `16.4.4`) — stand exactly where `14.15.5`(d)'s closing status left them, in both sectors now rather than one. The positive sector's own open content (whether `y=1` is the only positive `G`-periodic diagonal point) is precisely cycle exclusion, parked, and this section supplies no new lever on it. Per the brief's stop line: no search for further negative or positive cycles beyond the three known instances named in `14.15.6`(d)(iv); no attempt to decide `y_2=y_3` for word families beyond those named periodic instances; no growth study of any height variant beyond the two prescribed instances above; no cycle-exclusion attempt; no equidistribution proof attempt; no extension of the domain beyond the nonzero odd integers (`2`-adic or rational doors were not investigated, and no observation about them arose in the course of this work — recorded honestly, per the stop line, rather than invented). This closes the brief's items 1–5 at the primary bar: all five items proved, with the one flagged obstruction (item 3's height transfer) resolved affirmatively — checked precisely, no snag found — rather than forced or hidden.

## 14.15.7. Exact height laws on integer-fixed-point periodic words

*(`14.15.1`–`14.15.6` are merged and closed and are not edited here; the two published height tables — `14.15.5`(c) for `((2,1))^∞`, `14.15.6`(c) for `(1,1)^∞` — are cross-referenced, never edited. For periodic words whose fixed point is a known live integer, the height's growth is an elementary exact law, trivial in both directions (the upper bound because the fixed point caps the class representative, the lower bound because the class representative **is** the fixed point). The rigidity content of height growth therefore begins strictly beyond such words; the Bridge (bridge.md §16) is unmoved. Register flat throughout.)*

### (a) The constant-word mechanism lemma

**Lemma 14.15.7.1 (single-letter fixed-point facts).** Fix a letter `(m,r)`, `m,r ≥ 1`, with affine constants `α = 3^m/2^{m+r}`, `β = (3^m−2^m)/2^{m+r}` (`14.14.4.1`) and fixed point `y^* = β/(1−α) = (3^m−2^m)/d`, `d := 2^{m+r}−3^m` (`14.14.8.4`; `d` is odd and nonzero). Write `Q_1 := 2^{m+r+1}·3^m`. If `y^*` is an **integer**, then automatically:

1. `y^*` is odd, live (`3 ∤ y^*`), never `0` and never `−1` — liveness is not a separate hypothesis for single letters;
2. `stratum(y^*) = (m,r)` and `G(y^*) = y^*` — the constant chain at `y^*` is an actual integer chain realizing `((m,r))^∞` in both directions;
3. `2|y^*| < Q_1`.

**Proof.** Integrality means `d | 3^m−2^m`. (1): `y^*` is a quotient of odd by odd, hence odd; mod `3`, `3^m−2^m ≡ −2^m ≢ 0` and `d ≡ 2^{m+r} ≢ 0`, so `3 ∤ y^*`; `y^* = 0` needs `3^m = 2^m`, impossible; `y^* = −1` needs `2^m = 2^{m+r}`, i.e. `r = 0`, excluded. (2): `y^*+1 = (β+1−α)/(1−α) = 2^m(2^r−1)/d` with `2^r−1` and `d` odd, so `v_2(y^*+1) = m` exactly; and with `q^* := (y^*+1)/2^m = (2^r−1)/d`, direct algebra gives `3^m q^* − 1 = 2^r(3^m−2^m)/d = 2^r y^*`, so `v_2(3^m q^*−1) = r` exactly (`y^*` odd) and `G(y^*) = 2^r y^*/2^r = y^*`. So `y^*` follows every forward prefix of the constant word, and — being its own letter-prescribed predecessor, by `14.15.6.3`'s uniqueness applied to `G(y^*)=y^*` on stratum `(m,r)` — admits the letter-prescribed backward chain to every depth, with every chain door equal to `y^*`. (3): `|d| ≥ 1` gives `|y^*| ≤ |3^m−2^m| < 3^m`, so `2|y^*| < 2·3^m ≤ 2^{m+r}·3^m < Q_1`. ∎

**Theorem 14.15.7.2 (constant-word mechanism lemma).** Let `W = ((m,r))^∞` be a constant word whose fixed point `y^*` is an integer (hence live and realizing `W`, by `14.15.7.1`). Fix `n ≥ 1`, `Q_n := 2^{(m+r)n+1}·3^{mn}`, and a sector `σ' ∈ {+1,−1}`. Then:

1. **(The class.)** The odd integers that follow `W`'s length-`n` forward prefix *and* admit the letter-prescribed backward chain to depth `n` are exactly `{y ≡ y^* (mod Q_n)}`. Consequently `R^{σ'}_{n,n}(W)` (Definition `14.15.6.8`) is exactly this class intersected with the sign condition, liveness of `y_0`, and liveness of the deepest chain door `y_{−n}`.
2. **(Liveness of `y_0` is automatic.)** `3 | Q_n`, so every class member `y_0 = y^* + κQ_n` (`κ ∈ Z`) has `y_0 ≡ y^* (mod 3)` — live whenever `y^*` is, i.e. always here.
3. **(The deepest door and the `n`-independent mod-3 law.)** For a class member `y_0 = y^* + κQ_n`, the chain doors are `y_{−j} = y^* + κQ_n/A_j` (`A_j = (3^m/2^{m+r})^j`, `14.14.8.2`); in particular `y_{−n} = y^* + κ·2^{2(m+r)n+1}`. The factor `2^{2(m+r)n+1}` is an odd power of `2`, hence `≡ 2 (mod 3)` for **every** `n`, so deepest-door liveness reads `y^* + 2κ ≢ 0 (mod 3)`, equivalently `κ ≢ y^* (mod 3)` — a condition on `κ mod 3` alone, independent of `n`.
4. **(Closed form.)** Write `σ := sign(y^*)`. **Capped sector** (`σ' = σ`): `κ = 0` gives `y^* ∈ R^σ_{n,n}(W)`, and since `2|y^*| < Q_n` every `κ ≠ 0` member has `|y_0| ≥ Q_n − |y^*| > |y^*|`, so `H^σ_{n,n}(W) = |y^*|` exactly, for every `n` — bounded and constant. **Escaping sector** (`σ' = −σ`): the members of sign `σ'` are exactly `y_0 = y^* + σ'kQ_n`, `k ≥ 1`, with `|y_0| = kQ_n + σ'y^*` strictly increasing in `k`; all are live by (2); membership reduces by (3) to the mod-3 law on `κ = σ'k`; exactly one residue class of `κ mod 3` dies (`κ ≡ y^*`), and it is nonzero (`y^*` live), so with

```text
k₀ := the least k ≥ 1 with y^* + 2σ'k ≢ 0 (mod 3)
    = 1 if σ'y^* ≡ 2 (mod 3),   2 if σ'y^* ≡ 1 (mod 3)     (σ'y^* ≡ 0 impossible),
```

`k₀ ∈ {1,2}` always, and

```text
H^{σ'}_{n,n}(W) = |y^* + σ'k₀Q_n| = k₀Q_n + σ'y^*        for every n ≥ 1
```

— escape at exactly the per-window CRT-modulus rate, with constant offset the fixed point itself.

**Proof.** (1) *Forward:* the followers of the length-`n` prefix form exactly one residue class mod `2^{S_n+1}`, `S_n = (m+r)n` (Theorem `14.15.1.5`, read over the signed domain per `14.15.6.5`'s proof: membership in the composed cylinder class is equivalent to following the word, for both signs, with `−1` structurally excluded from every class). `y^*` follows the prefix (`14.15.7.1`(2)), so that class is `{y ≡ y^* (mod 2^{S_n+1})}`. *Backward:* the `z` admitting the letter-prescribed chain to depth `n` form exactly one class mod `3^{M_n}`, `M_n = mn` (`14.15.6.4`); `y^*` admits the chain to every depth (`14.15.7.1`(2)), so that class is `{y ≡ y^* (mod 3^{M_n})}`. The moduli are coprime; the Chinese remainder theorem gives exactly `{y ≡ y^* (mod Q_n)}`, `Q_n = 2^{S_n+1}·3^{M_n}`. The second clause is Definition `14.15.6.8` read against these two iff's: its forward window condition *is* "follows the prefix", its backward condition *is* "chain exists to depth `n`", and what remains is exactly sign, liveness of `y_0`, and deepest-door liveness (intermediate chain doors need no liveness — `14.15.5.1`'s remark). (2) `mn ≥ 1`, so `3 | Q_n`. (3) The depth-`j` composed constants of the constant deepest-first word satisfy `A_j y^* + B_j = y^*` (induction from `αy^*+β = y^*`); a class member's chain exists by (1) and its doors satisfy `y_0 = A_j y_{−j} + B_j` (`14.14.8.2`, applied to the chain read forward, each door on stratum `(m,r)` by construction), so `y_{−j} = y^* + (y_0−y^*)/A_j = y^* + κQ_n/A_j`; at `j = n`, `Q_n/A_n = 2^{S_n+1}3^{M_n}·2^{S_n}/3^{M_n} = 2^{2(m+r)n+1}`. Mod `3`: `2^{odd} ≡ 2`, so `y_{−n} ≡ y^* + 2κ`, and `y^* + 2κ ≡ 0 ⟺ κ ≡ −2y^* ≡ y^* (mod 3)` (`−2 ≡ 1`). (4) `2|y^*| < Q_1 ≤ Q_n` by `14.15.7.1`(3). Capped sector: `y^*` passes every condition in (1)'s description (sign `σ`, live, deepest door `y^*` itself live), so `H^σ ≤ |y^*|`; any `κ ≠ 0` member of either sign has `|y_0| ≥ Q_n − |y^*| > |y^*|`, forcing equality. Escaping sector: `κ = 0` has sign `σ ≠ σ'`, and for `|κ| ≥ 1` the sign of `y_0` is the sign of `κ` (since `Q_n > |y^*|`), so the sector's members are `k ≥ 1` as displayed, `|y_0| = kQ_n + σ'y^*` strictly increasing in `k` (positive since `kQ_n > |y^*|`); the least member of `R^{σ'}_{n,n}` is therefore the least `k` passing the mod-3 law, and exactly one nonzero `κ`-class dies, so among `k ∈ {1,2}` at least one survives. ∎

**One sentence on sectors, reconciled against `14.15.4.5`/`14.15.6.10`.** The sector containing `y^*` is capped (`H^σ_{n,n} ≡ |y^*|`, bounded — consistent with the per-sector equivalence theorem `14.15.6.10`, since `y^*` itself integrally realizes `W` in sector `σ`; for `((2,1))^∞` this is the realized case `14.15.6`(c) already records as `H^-_{n,n} ≤ 5`, now sharpened to equality), and the opposite sector escapes (`H^{−σ}_{n,n} = k₀Q_n − |y^*| → ∞` — consistent again, since `W`'s unique diagonal point `y^*` (`14.15.3.6`/`14.15.6.7`) has sign `σ`, so no door of sign `−σ` realizes `W`).

**Verified** — `experiments/height_exact_laws.py`, fresh code (imports nothing from `realization_height.py`, `diagonal_converse.py`, `signed_diagonal.py`, `itinerary_coding.py`, `block_map.py`, or `door_seam.py`; exact integer/`Fraction` arithmetic at every pass/fail decision), functions `test_single_letter_fixed_point_facts`, `test_class_equals_fixed_point_class`, `test_deepest_door_law`, `test_capped_sector`, `test_escaping_sector_closed_form`. Lemma `14.15.7.1`: `564` letters (all `m,r ≤ 8` plus `500` random up to `30`, seed `65001`), exact `Fraction` identities for `y^*`, `y^*+1`, the liveness units, and `2|y^*| < Q_1`, `0` failures; the `2` integral instances in the scan (`(1,1)`, `(2,1)` — the two already on file, no new family sought per the stop line) additionally checked for `stratum(y^*)=(m,r)`, `G(y^*)=y^*`, liveness, and the identity `3^m q^*−1 = 2^r y^*`, `0` failures. Theorem `14.15.7.2`(1): exhaustive two-directional scan (does {follows forward `n` letters ∧ backward chain exists to depth `n`} equal `{y ≡ y^* mod Q_n}`?), both words, `n = 1,2`, all odd `y` with `|y| ≤ 4Q_n+50`, both signs: `43,492` checks, `0` discrepancies either direction. Clause (3): `190` `(word, n, κ)` chains (`n ≤ 5`, `κ = −9..9`), deepest door equal to `y^* + κ·2^{2(m+r)n+1}` exactly and liveness matching the mod-3 law exactly, `0` failures. Clause (4): `y^*` a verified member of its own sector's `R^σ_{n,n}` for `n = 1..6` with brute-force sector minimum `= |y^*|` at `n = 1,2` (both words); escaping-sector class walk finds first surviving index `= k₀` at `n = 1..4` (both words), `0` failures. Total `47,314` checks, `0` failures (2026-07-17).

### (b) The two published instances, as corollaries

**Corollary 14.15.7.3 (the `((2,1))^∞` law).** `y^* = −5` (`14.15.5`(c)), `Q_n = 2^{3n+1}·3^{2n} = 2·72^n`. Positive sector: `σ'y^* = −5 ≡ 1 (mod 3)`, so `k₀ = 2` and

```text
H_{n,n}(((2,1))^∞) = 2·(2·72^n) − 5 = 4·72^n − 5        for every n ≥ 1.
```

Negative sector: capped, `H^-_{n,n} = 5` exactly (sharpening `14.15.6`(c)'s recorded `≤ 5` to equality). One line from `14.15.7.2`; the published table (`14.15.5`(c), `n = 1..8`) is reproduced exactly — checking rows: `n=1`: `4·72−5 = 283`, `n=8`: `4·72^8−5 = 2,888,816,545,234,939`.

**Corollary 14.15.7.4 (the `(1,1)^∞` law).** `y^* = 1`, `Q_n = 2^{2n+1}·3^n = 2·12^n`. Negative sector: `σ'y^* = −1 ≡ 2 (mod 3)`, so `k₀ = 1` and

```text
H^-_{n,n}((1,1)^∞) = 2·12^n − 1        for every n ≥ 1.
```

Positive sector: capped, `H_{n,n} = 1` (the trivial fixed point — `14.15.4`(c)'s own verification already recorded `H_{n,n} = 1` directly). One line from `14.15.7.2`; the published table (`14.15.6`(c), `n = 1..5`) is reproduced exactly — checking rows: `n=1`: `23`, `n=5`: `497,663`.

**Stated plainly.** These two corollaries upgrade the two published tables from single named instances to exact laws valid at every `n`: what was recorded as computed data (`14.15.5`(c)'s eight rows, `14.15.6`(c)'s five) is now the value of a closed form, with the tables' own numbers reproduced exactly and the mechanism — CRT class centered at the word's own fixed point, one `n`-independent mod-3 liveness condition — identified rather than conjectured.

**Verified** — `experiments/height_exact_laws.py`, functions `test_instance1_law`, `test_instance2_law`. Instance `((2,1))^∞`, positive sector: closed-form value confirmed a member of `R^+_{n,n}` by direct simulation (forward stratum match, backward chain via the predecessor formula, `y_0` and deepest-door liveness) for `n = 1..12`, with the `k = 1` candidate failing at exactly the deepest door for every `n`; all `8` published rows matched; brute-force minimality (dumb scan of all positive odd integers, no class reasoning) at `n = 1, 2`; `k = 1..9` dead/live pattern at `n = 1,2,3` matching the mod-3 law exactly (dead iff `k ≡ 1 (mod 3)`). Instance `(1,1)^∞`, negative sector: same battery with `n = 1..10` membership, all `5` published rows matched, brute force at `n = 1, 2`, `k = 1..9` pattern at `n = 1,2,3` (dead iff `k ≡ 2 (mod 3)`). `0` failures (2026-07-17).

### (c) The whole-period extension and the period-7 cycle's word

**Theorem 14.15.7.5 (whole-period extension).** Let `P = ((m_0,r_0),…,(m_{p−1},r_{p−1}))` be a period, `W = P^∞`, `S_P = Σ_i(m_i+r_i)`, `M_P = Σ_i m_i`, `A_P, B_P` its composed-affine constants (`14.14.8.2`), `y^* = B_P/(1−A_P)`. Hypotheses: **(H1)** `y^*` is an integer whose `G`-orbit realizes `W` (`stratum(G^j(y^*)) = P_{j mod p}` for all `j ≥ 0`; automatic for `p = 1` by `14.15.7.1`(2), and holding by construction whenever `W` is the word of an actual `G`-cycle — the only source of such instances on file); **(H2)** `2|y^*| < Q_1 := 2^{S_P+1}·3^{M_P}` (automatic for `p = 1` by `14.15.7.1`(3)). Liveness of `y^*` needs no hypothesis at any `p`: writing `y^* = N/(2^{S_P}−3^{M_P})` with `N = 2^{S_P}B_P ∈ Z`, every term of `N`'s expansion carries a positive power of `3` except the last, which is `(3^{m_{p−1}}−2^{m_{p−1}})·2^{Σ_{i<p−1}(m_i+r_i)} ≡ −2^{…} ≢ 0 (mod 3)`, and the denominator is `≡ 2^{S_P} ≢ 0 (mod 3)` — so `3 ∤ y^*` given integrality alone.

Then, for **whole-period diagonal windows** — window `(np, np)` in letters, i.e. `n` periods each side, `n ≥ 1` — all four clauses of `14.15.7.2` hold verbatim with `Q_n := 2^{nS_P+1}·3^{nM_P}`: the combined class is exactly `{y ≡ y^* (mod Q_n)}`; `y_0`-liveness is automatic; the deepest door is `y_{−np} = y^* + κ·2^{2nS_P+1} ≡ y^* + 2κ (mod 3)` — the same `n`-independent law, since `Q_n/A_P^n = 2^{2nS_P+1}` is again an odd power of `2`; and the heights are `H^σ_{np,np}(W) = |y^*|` (capped sector, `σ = sign(y^*)`) and `H^{σ'}_{np,np}(W) = k₀Q_n + σ'y^*` (escaping sector), with `k₀ ∈ {1,2}` by the same rule.

**Proof.** `14.15.7.2`'s proof used exactly four ingredients, each available here. (i) `y^*` follows every forward prefix and admits the letter-prescribed chain to every depth: (H1) gives the forward half directly; for the backward half, the periodic integer chain behind `y^*` (door `y_{−j} := G^{(p−j) mod p}(y^*)`, i.e. the orbit read backward, repeating with period `p`) has each door the letter-prescribed predecessor of the next by uniqueness (`14.15.6.3`), since `G` maps each onto the next with the past letter's stratum, by (H1) and periodicity. (ii) The two class iff's (`14.15.1.5` over the signed domain, `14.15.6.4`) are word-general, not single-letter facts. (iii) The composed relation at whole periods: the past `np` letters read deepest-first are exactly `P` repeated `n` times (`p | np`, so letter `−np` is `P_0`), with composed constants `(A_P^n, B_{np})` and `A_P^n y^* + B_{np} = y^*` (`y^*` is fixed by one period's composition, hence by `n`); `v_3(A_P^n) = nM_P`, so `Q_n/A_P^n = 2^{2nS_P+1} ≡ 2 (mod 3)` by the same computation. (iv) `2|y^*| < Q_1 ≤ Q_n` — (H2). No step of `14.15.7.2`'s argument referenced `p = 1` beyond these four. ∎

**Scope, per the brief.** Whole-period diagonal windows only. Windows that cut a period partway (per-letter refinement — shifted fixed points, one per rotation of `P`) are genuinely new machinery and are **not** developed here.

**Corollary 14.15.7.6 (the period-7 cycle's word).** `P = ((4,1),(3,3))`, the `G`-period-`2` word of the classical period-`7` negative cycle, `y^* = −17` realized by its actual cycle (`14.15.6`(d)(ii) — (H1) holds by construction); `S_P = 11`, `M_P = 7`, `Q_n = 2^{11n+1}·3^{7n} = 2·(2^{11}·3^7)^n`; (H2) holds with room to spare (`34 < 8,957,952`). Positive sector: `σ'y^* = −17 ≡ 1 (mod 3)`, so `k₀ = 2` and

```text
H_{2n,2n}(W) = 4·(2^{11}·3^7)^n − 17 = 4·4478976^n − 17        (n whole periods each side)
```

— `n=1`: `17,915,887`; `n=2`: `80,244,904,034,287`. Negative sector: capped, `H^-_{2n,2n} = 17` exactly. This was the brief's stated prediction, and it is **verified below, not assumed**; it did not fail.

**Verified** — `experiments/height_exact_laws.py`, functions `test_period7_fixed_point_facts`, `test_period7_law`, `test_period7_brute_force`. Fixed point `y^* = −17` exact (`Fraction` algebra); the orbit realizes the word (`stratum(−17)=(4,1)`, `G(−17)=−41`, `stratum(−41)=(3,3)`, `G(−41)=−17`); the liveness mechanism (`N` and denominator both units mod `3`) exact; the class iff at `n = 1` whole period checked **exhaustively** over all `8,957,951` odd `y` in one full modulus width, both signs, `0` discrepancies either direction; the deepest-door formula `y_{−2n} = y^* + κ·2^{22n+1}` on `44` chains (`n ≤ 4`, `κ = −5..5`), exact. The law: closed-form value confirmed a member of `R^+_{2n,2n}` by direct simulation for `n = 1..6` whole periods, the `k = 1` candidate dying at exactly the deepest door every time; `k = 1..9` pattern at `n = 1,2,3` matching the mod-3 law (dead iff `k ≡ 1 (mod 3)`); capped sector `−17 ∈ R^-_{2n,2n}` for `n = 1..6` with brute-force sector minimum `17` at `n = 1,2`. Minimality: at `n = 1`, full dumb scan (no class reasoning) of all positive odd integers up to `17,915,887` finds exactly the formula value; at `n = 2` the formula value is `≈ 8.0·10^{13}` and a literal dumb scan is infeasible — **deviation from the brief's brute-force prescription, recorded honestly**: the `n = 2` scan is restricted to the forward cylinder class (representative itself found by dumb scan and equal to `−17 mod 2^{23}`; by the already-merged `14.15.1.5` the class provably contains every forward follower), and every member below the formula value — `9,565,938` of them — is then checked by direct simulation, finding exactly the formula value; this uses the merged cylinder theorem but nothing from `14.15.7`'s own CRT/fixed-point reasoning. `0` failures (2026-07-17).

### (d) Accounting and closing status

**Accounting.** These are exact laws on the **decided** shelf: for periodic words whose fixed point is a live integer, the escape rate of the per-sector realization height is now a theorem, and it is exactly the per-window CRT-modulus rate with a constant offset that is the fixed point itself — `H = k₀Q_n + σ'y^*`, `Q_n = 2^{nS_P+1}·3^{nM_P}` the window's own modulus, `k₀ ∈ {1,2}`. What this does **not** do: bound `H` on any word whose fixed point is not a live integer; touch aperiodic words; or move the Bridge (bridge.md §16) — the height's boundedness question for general words is exactly as open as `14.15.4`(d) left it, and the rigidity content of height growth begins strictly beyond the integer-fixed-point words closed here. Bridge status unchanged (`14.14.6`).

**The second-progression-step remark, explained.** `14.15.5`(c) recorded, as an observation, that its `H_{n,n}` search "always found a live-deepest-door candidate within the second CRT-progression step". That is now proved rather than observed: by `14.15.7.2`(3)–(4), exactly one residue class of the progression index mod `3` dies — the class `κ ≡ y^* (mod 3)`, nonzero since `y^*` is live — so the least surviving index is always `1` or `2`.

**Closing status.** What changed: the two published height tables (`14.15.5`(c), `14.15.6`(c)) are now corollaries of an exact law (`14.15.7.3`–`14.15.7.4`); the mechanism — CRT class centered at the word's own fixed point, one `n`-independent mod-3 liveness law on the progression index — is a theorem (`14.15.7.2`), extended to whole-period windows of multi-letter periodic words (`14.15.7.5`); and a third instance, the period-7 cycle's word, is on file with its predicted law verified (`14.15.7.6`). What did not change: the Bridge is unmoved — these are instance-level closures below it, and deciding boundedness of `H` for any word beyond the integer-fixed-point periodic family remains exactly the diagonal-locus question as `14.15.4`(d)/`14.15.5`(d) posed it. Per the brief's stop line: no `H` computed on any word beyond the three named instances; no statistical or distributional study of `H`; no aperiodic word; no attempt to decide integral realization for new word families (the verification code's letter scan checks the lemma's exact identities only, and the two integral single-letter instances it encounters are the two already on file); no per-letter refinement of the whole-period extension; no cycle-exclusion attempt; no equidistribution proof attempt.

## 14.15.8. The non-integral mechanism: exact height laws on the remaining single-letter periodic words

*(Empirical precursor: `briefs/h-nonintegral-probe-findings.md`. These theorems close the non-integral single-letter shelf the way `14.15.7` closed the integer one; no new empirical scope is added, and the Bridge (bridge.md §16) is unmoved.)*

### (a) The setup lemma and the class theorem

**Lemma 14.15.8.1 (single-letter non-integral facts).** Fix a letter `(m,r)`, `m,r ≥ 1`, with affine constants `α = 3^m/2^{m+r}`, `β = (3^m−2^m)/2^{m+r}` (`14.14.4.1`), `d := 2^{m+r}−3^m` (odd, nonzero), and fixed point `y^* = β/(1−α) = (3^m−2^m)/d` (`14.14.8.4`), assumed **not** an integer. Write `y^* = a/q` in lowest terms with `q > 0` (so `a = ±(3^m−2^m)/gcd`, `q = |d|/gcd`, the sign carried by `a`). Then:

1. `q > 1`, `gcd(q,6) = 1`, `a` odd, `3 ∤ a`, and `0 < |a| ≤ 3^m−2^m < 3^m < Q_1 := 2^{m+r+1}·3^m`.
2. **(2-adic stratum facts.)** Since `q` is odd, `y^* ∈ Z₂`, and it is a `2`-adic unit (`a` odd). Re-running `14.15.7.1`(2)'s forced-valuation algebra `2`-adically: `y^*+1 = 2^m(2^r−1)/d` with `(2^r−1)/d` a `2`-adic unit (odd over odd), so `v₂(y^*+1) = m` exactly; and with `q^* := (y^*+1)/2^m = (2^r−1)/d`, direct algebra gives `3^m q^*−1 = 2^r(3^m−2^m)/d = 2^r y^*` with `y^*` a `2`-adic unit, so `v₂(3^m q^*−1) = r` exactly. Hence `y^*` satisfies both congruences of Lemma `14.15.1.3`(i), and `G`'s defining formula (`14.15.6.1`), read as rational arithmetic, fixes it: `G(y^*) = 2^r y^*/2^r = y^*`.
3. **(3-adic congruence.)** Since `3 ∤ q`, `y^* ∈ Z₃`. For every `n ≥ 1`, with `A_n = α^n`, `B_n` the composed-affine constants of the constant word (`14.14.8.2`; all orderings agree for a constant word) and `M_n := mn`: `A_n y^* + B_n = y^*` (induction from `αy^*+β = y^*`), so `y^*−B_n = A_n y^*` and, since `v₃(A_n) = M_n`, `y^* ≡ B_n (mod 3^{M_n})`.

**Proof.** (1) `q > 1` is the non-integrality hypothesis. `d` is even-minus-odd, hence odd, and `d ≡ 2^{m+r} ≢ 0 (mod 3)`, so `q | |d|` is odd and coprime to `3`: `gcd(q,6) = 1`. `3^m−2^m` is odd and `≡ −2^m ≢ 0 (mod 3)`, so `a` is odd and `3 ∤ a`. Magnitude: `0 < 3^m−2^m < 3^m` for `m ≥ 1`. (2) and (3) are the displayed computations; each is a one-line exact identity in `Q`, checked below as exact `Fraction` identities. ∎

**Theorem 14.15.8.2 (non-integral class theorem).** Let `W = ((m,r))^∞` have non-integral fixed point `y^* = a/q` as above. Fix `n ≥ 1`, `S_n := (m+r)n`, `M_n := mn`, `Q_n := 2^{S_n+1}·3^{M_n}`, and let `ρ_n := a·q^{−1} mod Q_n` — the CRT lift of `y^*` as a simultaneous `2`-adic and `3`-adic integer, well defined by `gcd(q,6) = 1`, odd (`a`, `q` both odd), taken as the representative in `(0, Q_n)`. Then, over the signed domain:

1. **(The class.)** The odd integers that follow `W`'s length-`n` forward prefix *and* admit the letter-prescribed backward chain to depth `n` are exactly `{y ≡ ρ_n (mod Q_n)}`. Consequently `R^σ_{n,n}(W)` (Definition `14.15.6.8`) is exactly this class intersected with the sign condition and liveness of the deepest chain door.
2. **(Liveness of `y₀` automatic; `−1` excluded.)** `3 | Q_n`, and every class member is `≡ ρ_n ≡ a·q^{−1} ≢ 0 (mod 3)` (`3 ∤ a`), hence live; and `−1` is never in the class — it fails the forward condition (`stratum`/`G` undefined at `−1`, `14.15.6.1`) and the class equals the follower set, so equivalently `ρ_n ≢ −1 (mod Q_n)`, with nothing to check case by case.

**Proof.** *Forward.* Claim: the followers of the length-`n` prefix are exactly `{y ≡ y^* (mod 2^{S_n+1})}` (congruence in `Z₂`, i.e. `qy ≡ a mod 2^{S_n+1}`). One-step fact: if `u` is an odd-denominator rational with `v₂(u−y^*) ≥ m+r+1`, then `u` satisfies both congruences of Lemma `14.15.1.3`(i) — they are conditions on `u mod 2^{m+1}` and on `(u+1)/2^m mod 2^{r+1}`, determined by `u mod 2^{m+r+1}`, and `y^*` satisfies them by Lemma `14.15.8.1`(2), `14.15.1.3`(i)'s congruence arithmetic being valid verbatim for odd-denominator rationals — so an *integer* `u` in that congruence lies on stratum `(m,r)`, and `G(u)−y^* = G(u)−G(y^*) = 3^m(u−y^*)/2^{m+r}` (the affine formula `14.14.4.1` as a rational identity, applied at `u` and at `y^*`), giving `v₂(G(u)−y^*) = v₂(u−y^*)−(m+r)`. Now let `y` be any odd integer with `v₂(y−y^*) ≥ S_n+1 = n(m+r)+1`. By induction, `v₂(G^i(y)−y^*) ≥ (n−i)(m+r)+1 ≥ m+r+1` for `i = 0,…,n−1`, so every iterate lies on stratum `(m,r)`: `y` follows the prefix. By Theorem `14.15.1.5` — read over the signed domain, per `14.15.6.5`'s proof — the followers form exactly one residue class mod `2^{S_n+1}`; it contains the full class `{y ≡ y^* (mod 2^{S_n+1})}`, and one residue class mod `2^{S_n+1}` containing another equals it. *Backward.* By the signed admissibility-class lemma (`14.15.6.4`), the `z` admitting the letter-prescribed chain to depth `n` are exactly one class mod `3^{M_n}`, namely `B_n mod 3^{M_n}`; by Lemma `14.15.8.1`(3) that class is `{z ≡ y^* (mod 3^{M_n})}`. *CRT.* The moduli are coprime, and `ρ_n` is the unique residue mod `Q_n` congruent to `y^*` at both places, giving the displayed class. The second clause is Definition `14.15.6.8` read against the two iffs, exactly as `14.15.7.2`(1): the forward window condition *is* "follows the prefix", the backward condition *is* "chain exists to depth `n`", and what remains is sign, liveness of `y₀`, and deepest-door liveness (intermediate chain doors need none — `14.15.5.1`'s remark); liveness of `y₀` then drops out by (2). (2) `M_n ≥ 1` gives `3 | Q_n`; the residue computation is displayed; the `−1` sentence is the iff itself. ∎

**Verified** — `experiments/nonintegral_mechanism.py`, fresh code (imports nothing from `h_nonintegral_probe.py`, `height_exact_laws.py`, `realization_height.py`, `diagonal_converse.py`, `signed_diagonal.py`, `itinerary_coding.py`, `block_map.py`, or `door_seam.py`; exact integer/`Fraction` arithmetic at every pass/fail decision; deterministic, no RNG), functions `test_setup_facts`, `test_class_theorem`. Lemma `14.15.8.1`: all seven non-integral words (`(1,2), (1,3), (2,2), (2,3), (3,1), (3,2), (3,3)`; `y^* = 1/5, 1/13, 5/7, 5/23, −19/11, 19/5, 19/37`), every clause as exact `Fraction` identities, including `A_n y^*+B_n = y^*` and `v₃(y^*−B_n) ≥ M_n` at `n = 1..6`, `0` failures. Theorem `14.15.8.2`: exhaustive two-directional scan (does {follows forward `n` letters ∧ chain exists to depth `n`} equal `{y ≡ ρ_n mod Q_n}`?) over one full modulus width per sign, both signs, forward and backward conditions decided by direct simulation only — `n = 1` for all seven words, `n = 2` for the five words with `Q_2 ≤ 5·10^5` — `593,424` exhaustive iff decisions, `0` discrepancies in either direction; on every class member encountered, `y₀`-liveness confirmed automatic, `−1` confirmed absent, and the `R^σ` description (sign + deepest-door liveness only) confirmed against `in_R` membership by direct simulation (2026-07-17).

### (b) The four mechanism identities and the P1–P3 corollaries

**Theorem 14.15.8.3 (the mechanism identities).** Setting `g := 2^{m+r}·3^m mod q` (a unit mod `q`, by `gcd(q,6) = 1`) and parametrizing the class of `14.15.8.2` as `y₀ = ρ_n + κQ_n` (`κ ∈ Z`) — so that, since `0 < ρ_n < Q_n`, the positive sector's members are exactly `κ = k ≥ 0` and the negative sector's exactly `κ = −k`, `k ≥ 1`, each in strictly increasing `|y₀|`:

1. **(Identity 1: the progression offset.)** `qρ_n − a = j_n Q_n` for a unique integer `j_n`; `j_n ∈ {1,…,q−1}`; and

```text
j_n = −a·2^{−1}·g^{−n} mod q,
```

purely periodic in `n` from `n = 1` with period **exactly** `P := ord_q(g)`.

2. **(Identity 2: the deepest door.)** For the class member `y₀ = ρ_n + σkQ_n` (`σ` the sector sign), the letter-prescribed chain's deepest door is

```text
y_{−n} = y^* + (y₀ − y^*)/A_n = (a + (j_n + σkq)·2^{2(m+r)n+1})/q        exactly,
```

and, since `2^{2(m+r)n+1}` is `2` to an odd power, hence `≡ 2 (mod 3)` for every `n`,

```text
y_{−n} ≡ t_n + 2σk (mod 3),        t_n := (a + 2j_n)·q^{−1} mod 3.
```

3. **(Identity 3: the mod-3 death law and the first-viable rule.)** Exactly one progression-index class mod `3` dies per sector — `k ≡ t_n (mod 3)` in the positive sector, `k ≡ −t_n (mod 3)` in the negative — and every other candidate is a member of `R^σ_{n,n}(W)`, so the first-viable indices are

```text
k⁺_n = [t_n = 0],        k⁻_n = 1 + [t_n = 2].
```

4. **(Identity 4: closed forms.)** For every `n ≥ 1`,

```text
H⁺_{n,n}(W) = ρ_n + [t_n = 0]·Q_n,        H⁻_{n,n}(W) = (1 + [t_n = 2])·Q_n − ρ_n.
```

**Proof.** (1) *Well-defined:* `qρ_n ≡ a (mod Q_n)` by definition of `ρ_n`, so `qρ_n − a = j_n Q_n` for a unique `j_n ∈ Z`. *Range:* `0 < ρ_n < Q_n` and `|a| < Q_n` (Lemma `14.15.8.1`(1), `|a| < Q_1 ≤ Q_n`) give `−1 < −a/Q_n < j_n < q − a/Q_n < q+1`, so `j_n ∈ {0,…,q}`; `j_n = 0` would force `ρ_n = a/q ∉ Z` and `j_n = q` would force `ρ_n − Q_n = a/q ∉ Z` (`q > 1`, `gcd(a,q) = 1`), so `j_n ∈ {1,…,q−1}`. *Closed form:* mod `q`, `0 ≡ qρ_n = a + j_n Q_n`, and `Q_n = 2·(2^{m+r}3^m)^n ≡ 2g^n (mod q)`, so `j_n ≡ −a·2^{−1}·g^{−n} (mod q)`, pinned exactly by the range. *Period:* `j_n = f(g^{−n} mod q)` with `f(u) = −a·2^{−1}·u mod q`; `n ↦ g^{−n} mod q` is purely periodic from `n = 1` with period `ord_q(g^{−1}) = P`, and `f` is injective on units (multiplication by the unit `−a·2^{−1}`), so `(j_n)` has period exactly `P` and no pre-period. (2) By `14.15.8.2`(1) the chain exists; each chain door lies on stratum `(m,r)` (forced, `14.15.6.3`), so the chain read forward follows the constant itinerary and `14.14.8.2` gives `y₀ = A_j y_{−j} + B_j`; subtracting `A_j y^* + B_j = y^*` (Lemma `14.15.8.1`(3)) gives `y_{−j} = y^* + (y₀−y^*)/A_j`. At `j = n`: `y₀ − y^* = (qρ_n − a)/q + σkQ_n = (j_n + σkq)Q_n/q`, and `Q_n/A_n = 2^{S_n+1}3^{M_n}·2^{S_n}/3^{M_n} = 2^{2S_n+1}`, giving the displayed formula — an integer, being an actual chain door. Mod `3`: `2^{2S_n+1} ≡ 2`, so `y_{−n} ≡ (a + 2j_n)·q^{−1} + 2σk·(q·q^{−1}) = t_n + 2σk (mod 3)`. (3) By `14.15.8.2`, every sector candidate passes every condition of `R^σ_{n,n}` except possibly deepest-door liveness (class membership by construction, sign by the parametrization, `y₀`-liveness and `y₀ ≠ −1` by `14.15.8.2`(2)). Death: `y_{−n} ≡ 0 (mod 3)` ⟺ `2σk ≡ −t_n` ⟺ `σk ≡ t_n (mod 3)` (`2^{−1} ≡ 2`, `−2 ≡ 1`): one `κ`-class mod `3`, as displayed per sector. First-viable: positive sector, `k = 0` dies iff `t_n = 0`, and then `k = 1` survives (`1 ≢ 0`); negative sector, `k = 1` dies iff `1 ≡ −t_n`, i.e. `t_n = 2`, and then `k = 2` survives (`2 ≢ 1 (mod 3)`). (4) `|y₀| = ρ_n + kQ_n` resp. `kQ_n − ρ_n` is strictly increasing in `k` within each sector, so `H^σ_{n,n}` is the value at the first-viable index. ∎

**Corollary 14.15.8.4 (P1: pure periodicity of the normalized height).** Define, per sector,

```text
v_n := H^σ_{n,n}(W)/Q_n − σ·a/(qQ_n).
```

Then `v_n = j_n/q + k⁺_n` (positive sector) and `v_n = k⁻_n − j_n/q` (negative sector) exactly; `(v_n)_{n≥1}` is purely periodic from `n = 1` with period **exactly** `P = ord_q(g)`, both sectors.

**Proof.** Substitute Identity 4: `H⁺/Q_n = ρ_n/Q_n + k⁺ = a/(qQ_n) + j_n/q + k⁺`, and `H⁻/Q_n = k⁻ − ρ_n/Q_n = k⁻ − j_n/q − a/(qQ_n)`; the displayed forms follow. Since `t_n`, hence `k^σ_n`, is a function of `j_n` alone, `v_n = V_σ(j_n)` for an explicit function `V_σ`, so `(v_n)` is purely periodic with period dividing `P`. Exactness: `V_σ` is injective — `v_n` is never an integer (`j_n/q ∉ Z`), so `v_n ∈ (0,1) ∪ (1,2)` determines `k` (`k⁺ = ⌊v_n⌋`, `k⁻ = ⌈v_n⌉`) and then `j_n = q·|v_n − k^σ_n|` — so a shorter period for `(v_n)` would be a shorter period for `(j_n)`, contradicting Identity 1. ∎

**Corollary 14.15.8.5 (P2: the lower bound and the sharp constant).** `v_n ≥ 1/q` for every `n ≥ 1`, both sectors — so `H^σ_{n,n}(W) ≥ Q_n/q − |a|/q`: escape at the full CRT-modulus rate on the entire non-integral shelf, with a denominator-bounded constant. The sharp per-word, per-sector constant is the minimum of `V_σ` over the visited orbit `O := {j_n : n ≥ 1} = (−a·2^{−1}·⟨g⟩) mod q`, `|O| = P`, attained periodically. In the positive sector this equals `j_min/q`, `j_min := min O`, whenever `t(j_min) ≠ 0` — the case for all seven words on file — and the generic bound `1/q` is attained iff `1 ∈ O` with `t(1) ≠ 0` (positive sector) resp. `q−1 ∈ O` with `t(q−1) ≠ 2` (negative sector).

**Proof.** Positive: `v_n = j_n/q + k⁺_n ≥ j_n/q ≥ 1/q`. Negative: `v_n = k⁻_n − j_n/q ≥ 1 − (q−1)/q = 1/q`. The sharp constant is `min_O V_σ` by pure periodicity (every orbit value is visited infinitely often). If `t(j_min) ≠ 0` then `V_+(j_min) = j_min/q`, which is `≤ V_+(j)` for every `j ∈ O` (any `j` with `t(j) = 0` has `V_+(j) = j/q + 1 > 1 > j_min/q`). Equality cases: `V_+(j) = 1/q` forces `k⁺ = 0`, `j = 1`; `V_−(j) = 1/q` forces `k⁻ = 1`, `j = q−1`. ∎

**Corollary 14.15.8.6 (P3: one extra progression step).** `k⁺_n ∈ {0,1}` and `k⁻_n ∈ {1,2}` for every `n` — the first-viable candidate is never more than one progression step beyond the sector's least class member. And, in contrast to `14.15.7.2`(4), **no capped sector exists**: both sectors escape at rate `Q_n`, consistent with the per-sector equivalence theorem (`14.15.6.10`), since `W`'s unique diagonal point `y^* = a/q` (`14.15.6.7`) is not an integer, so no door of either sign integrally realizes `W`.

**Proof.** Immediate from Identity 3; the consistency sentence is `14.15.6.10` cited, not re-derived, plus P2's lower bound. ∎

**Verified** — `experiments/nonintegral_mechanism.py`, functions `test_identities`, `test_brute_force`. All four identities and all three corollaries checked on all seven words, both sectors, `n = 1..25` (`350` word/sector/`n` rows, matching the probe's full range), with every quantity on the simulation side produced by direct simulation only: every candidate on the class progression (`k = 0..6` positive, `1..7` negative — two full mod-3 cycles past the first viable) was checked to follow the forward prefix by iterating `G`, to admit the backward chain by the unique-predecessor formula with integrality checked at every step, to be live, odd, `≠ −1`, and of the right sign; the deepest door was compared against Identity 2's closed form and its mod-3 value (exact integer arithmetic); the dead/live pattern against Identity 3's death law at every candidate; the first-viable index against the rule; `H` against Identity 4's closed form and confirmed a member of `R^σ_{n,n}`; `v_n` against P1's exact form (`Fraction` arithmetic), with pure periodicity verified at period exactly `P` (and every `p < P` verified *not* a period), `P = 2, 3, 3, 11, 5, 2, 3` for the seven words; P2's bound at every row, and the sharp constant recomputed from the orbit's closed form matching the observed 25-row minimum, with `c⁺ = j_min/q` confirmed for all seven words (`2/5, 2/13, 1/7, 1/23, 1/11, 2/5, 9/37`); P3 at every row. Brute-force minimality (dumb scan of all odd integers of the sector in increasing `|y|`, no class reasoning, membership decided by direct simulation): `n = 1` and `n = 2`, all `14` word/sector pairs, `28/28` agree with the closed forms — reproducing, with fresh code, the probe's own 28-entry cross-check table exactly. Total `23,269` checks, `0` failures, deterministic, ~5 s (2026-07-17).

### (c) Reconciliation

**(i) Against `14.15.7`: one law, with the integer case as the degenerate `q = 1`.** Both shelves obey the same statement: *on a periodic single-letter word, `R^σ_{n,n}` is the residue class mod `Q_n` of the CRT lift of the word's own fixed point, exactly one progression-index class mod `3` has a dead deepest door, and `H^σ_{n,n}` is the absolutely least surviving member of the sector.* The mod-3 law itself is one formula: the dead class is `κ ≡ t_n (mod 3)` with `t_n = (a + 2j_n)·q^{−1} mod 3`, and at `q = 1` (where `a = y^*` and `j_n` degenerates to `0`, the progression offset vanishing because `ρ_n` is then `y^*` itself, up to one shift by `Q_n`) this is exactly `14.15.7.2`(3)'s `κ ≡ y^* (mod 3)`. The only divergence is where the class's absolutely least member sits: for `q = 1` the lift is the *`n`-independent integer* `y^*` (`2|y^*| < Q_n`), so the sector containing it is capped at `|y^*|` forever and only the opposite sector escapes (`14.15.7.2`(4)); for `q > 1` the lift `ρ_n = (a + j_n Q_n)/q` itself grows like `(j_n/q)·Q_n`, no bounded member exists in either sector, and both escape at the modulus rate with the unit-orbit constant of `14.15.8.4`–`14.15.8.5`. In the honest headline form: on every periodic single-letter word, height growth is now a theorem — escape at the CRT-modulus rate, with a constant that is either the fixed point itself (integer case) or a purely periodic, denominator-bounded unit-orbit value (non-integral case).

**(ii) Against the probe.** `briefs/h-nonintegral-probe-findings.md` is this section's empirical precursor: its instance grid is Lemma `14.15.8.1`'s seven words, its §3 identities 1–4 are Theorem `14.15.8.3`'s identities 1–4, and its P1/P2/P3 verdicts are Corollaries `14.15.8.4`–`14.15.8.6`, now proved for every `n` rather than verified for `n ≤ 25`. Its tables (`350` rows, plus the `28` brute-force cross-checks) sit under proof, reproduced here by independent code; its stated caveat — "verified empirical identities over the tested range only, not theorems" — is discharged by this section, including the two calibrations it flagged: the sharp escape constant is `j_min/q` only because `t(j_min) ≠ 0` happens to hold on all seven words (`14.15.8.5` states the exact condition), and the `o(1)` in its P2 gloss is the exact two-sided term `σa/(qQ_n)` (`14.15.8.4`'s normalization, sign included — for `(3,1)`, `a < 0` puts the positive-sector ratio slightly *below* its periodic value, exactly as the probe observed).

### (d) Accounting and closing status

**Accounting.** The whole single-letter periodic shelf is now closed by theorems: on every periodic single-letter word, height growth is a theorem — escape at the CRT-modulus rate `Q_n = 2^{(m+r)n+1}·3^{mn}`, with a constant that is either the fixed point itself (integer case, `14.15.7`, one sector capped at `|y^*|`) or a purely periodic, denominator-bounded unit-orbit value (non-integral case, this section, both sectors escaping with `v_n ∈ [1/q, 2)`). These are exact laws on the **decided** shelf: for such words the two adelic limits are pinned by the single rational `y^*`, and realization or escape is elementary arithmetic — the unit-group orbit of `Q_n mod q` and the parity of the exponent in `2^{2(m+r)n+1} mod 3`. What this does **not** do: bound `H` on any multi-letter or aperiodic word; move the Bridge (bridge.md §16) — the boundedness question for general words is exactly as open as `14.15.4`(d) left it, and the rigidity content of height growth now provably begins beyond periodic single-letter words. Bridge status unchanged (`14.14.6`).

**Closing status.** What changed: the probe's four mechanism identities and three verdicts are theorems with proofs (`14.15.8.2`–`14.15.8.6`), the single-letter periodic shelf is closed at every `n` in both sectors for **every** letter `(m,r)` — integer fixed point by `14.15.7`, non-integral by this section, the two cases exhaustive — with the probe's grid (`1 ≤ m,r ≤ 3`: two integer words, seven non-integral) as the verified instance set, and the empirical caveat of `briefs/h-nonintegral-probe-findings.md` is discharged. What did not change: the Bridge is unmoved — these are instance-level closures below it, on words whose adelic limits a single rational already pins. Per the brief's stop line: no multi-letter word, empirical or proved (a parallel brief owns that shelf; nothing here reads or anticipates it); no aperiodic word; no `H` computation beyond what verification of the stated theorems required on the probe's own seven words; no cycle-exclusion attempt; no equidistribution proof attempt.

## 14.15.9. Whole-period height laws for every periodic word

*(This section proves the composed-unit identities in whole-period generality: every periodic word, any period, both sectors, integer or non-integral fixed point, at whole-period windows. The sharp escape constant is the minimum over the orbit of `j/q + k(t(j))`, not `j_min/q` (the single-letter form fails on some multi-letter words); that corrected form is used throughout below. The Bridge (bridge.md §16) is unmoved: height growth on a periodic word is pinned exactly once its fixed-point denominator `q` is known, but determining `q` for an arbitrary period — i.e. ruling out `q = 1` beyond the known instances — is periodic cycle exclusion, not closed by this section.)*

**Setup and notation, fixed once.** `P = ((m_0,r_0),…,(m_{p−1},r_{p−1}))` is a period (`p ≥ 1`, every `m_i,r_i ≥ 1`), `W = P^∞` its bi-infinite periodic word, and `P^{(i)} = ((m_i,r_i),…,(m_{i+p−1},r_{i+p−1}))` (indices mod `p`) its `i`-th rotation, `W^{(i)} = (P^{(i)})^∞`. `S_P := Σ_i(m_i+r_i)`, `M_P := Σ_i m_i` (shared by all rotations). `g_j(u) := α_j u + β_j` is letter `j`'s affine map (`14.14.4.1`), and all composed constants `A, B` below apply letters **in index order** — `14.14.8.2`'s recursion, which is simultaneously the forward composition over one period and the deepest-first reading of a whole-period past (`14.15.5.1`'s order note); so `A_P = 3^{M_P}/2^{S_P}`, common to all rotations. `y^* = y^*_0 := B_P/(1−A_P)` is `P`'s composed fixed point (`14.14.8.4`), `y^*_i` the `i`-th rotation's; `y^* = a/q` in lowest terms, `q > 0`, the sign carried by `a`. `Q_n := 2^{nS_P+1}·3^{nM_P}` (the window-`(np,np)` CRT modulus), `g_P := 2^{S_P}·3^{M_P} mod q` (the composed unit), `ρ_n := a·q^{−1} mod Q_n` (representative in `(0,Q_n)`). The instance grid is the two probes' 20 words (7 single-letter non-integral, 13 multi-letter) plus the three integer-fixed-point words (`1`, `−5`, `−17`); no new empirical grid is opened.

### (a) The fixed-point arithmetic, the rotation lemma, and the adelic anchor

**Lemma 14.15.9.1 (fixed-point arithmetic).** For every period `P`, with `N := Σ_{i=0}^{p−1} (3^{m_i}−2^{m_i})·3^{Σ_{j>i}m_j}·2^{Σ_{j<i}(m_j+r_j)}` and `D := 2^{S_P}−3^{M_P}`:

1. `y^* = N/D` exactly. `N` is a positive odd integer with `3 ∤ N` and `4N < 2^{S_P}·3^{M_P}`; `D` is odd, nonzero, `D ≡ 2^{S_P} ≢ 0 (mod 3)`; and `sign(y^*) = sign(2^{S_P}−3^{M_P})`.
2. Consequently, in lowest terms `y^* = a/q`: `q | 2^{S_P}−3^{M_P}`, `gcd(q,6) = 1`, `a` is odd, `3 ∤ a` — so the question "can `3 | a` occur?" is settled: never — `2|a| < Q_1/4 < Q_1`, `y^* ≠ 0`, and `y^* ∈ Z₂ ∩ Z₃`, a unit at both places.

**Proof.** (1) Unwinding `14.14.8.2`'s recursion, `B_P = Σ_i β_i·Π_{j>i}α_j`, and multiplying through by `2^{S_P}` clears every denominator: `2^{S_P}B_P = N` term by term. Then `y^* = B_P/(1−A_P) = 2^{S_P}B_P/(2^{S_P}−3^{M_P}) = N/D`. Each term of `N` is positive (`3^m > 2^m` for `m ≥ 1`), so `N ≥ 1`. Parity: the `i = 0` term is odd·odd·`2^0`, odd; every `i ≥ 1` term carries `2^{Σ_{j<i}(m_j+r_j)}` with exponent `≥ 2`, even — so `N` is odd. Mod `3`: every term with `i < p−1` carries `3^{Σ_{j>i}m_j}` with exponent `≥ 1`, `≡ 0`; the `i = p−1` term is `≡ −2^{m_{p−1}+Σ_{j<p−1}(m_j+r_j)} ≢ 0` — so `3 ∤ N`. The bound: term `i` is `< 3^{Σ_{j≥i}m_j}·2^{Σ_{j<i}(m_j+r_j)} = 2^{S_P}3^{M_P}·3^{−Σ_{j<i}m_j}·2^{−Σ_{j≥i}(m_j+r_j)} ≤ 2^{S_P}3^{M_P}·3^{−i}·4^{−(p−i)}` (each `m_j ≥ 1`, each `m_j+r_j ≥ 2`); summing the geometric series, `N < 2^{S_P}3^{M_P}·3·(3^{−p}−4^{−p})`, and `3(3^{−p}−4^{−p}) ≤ 1/4` for every `p ≥ 1` (value `1/4` at `p = 1`, `7/48` at `p = 2`, and `≤ 3^{1−p} ≤ 1/9` for `p ≥ 3`). `D` is even-minus-odd, odd; `D ≡ 2^{S_P} (mod 3)` since `M_P ≥ 1`; `D ≠ 0` (even ≠ odd); `sign(y^*) = sign(D)` since `N > 0`. (2) `q` divides the odd, `3`-coprime `|D|` and `a = ±N/gcd(N,|D|)` inherits `N`'s parity and `3`-coprimality; `2|a| ≤ 2N < 2^{S_P}3^{M_P}/2 = Q_1/4`; `y^* ≠ 0` by `N ≥ 1`; odd `q` coprime to `3` puts `a/q` in `Z₂ ∩ Z₃`, and `a` odd, `3 ∤ a` makes it a unit at both places. ∎

**Lemma 14.15.9.2 (rotation lemma).** Let `F_i` be the composed affine map of `P^{(i)}` (letters `i, i+1, …, i+p−1` in application order), with unique fixed point `y^*_i` (`A_P ≠ 1`: `v₂(A_P) = −S_P ≠ 0`). Then:

1. **(One affine orbit.)** `y^*_{i+1} = α_i y^*_i + β_i` for every `i` (indices mod `p`): the `p` rotated fixed points are a single orbit of the per-letter affine maps, closing up after one period.
2. **(One denominator.)** All `p` rotations have the **same** reduced denominator `q`.
3. **(The mod-3 residues.)** `ε_i := y^*_i mod 3 = a_i·q^{−1} mod 3 ∈ {1,2}` (well defined by Lemma `14.15.9.1` applied to `P^{(i)}`), and `ε_{i+1} = −(−1)^{r_i} mod 3` — `1` if `r_i` is odd, `2` if `r_i` is even: each rotation's residue is pinned by the *preceding* letter's `r`-parity alone.

**Proof.** (1) Since `g_{i+p} = g_i`, both `F_{i+1}∘g_i` and `g_i∘F_i` equal `g_i∘g_{i+p−1}∘…∘g_{i+1}∘g_i` read with different bracketing: `F_{i+1}∘g_i = g_i∘F_i`. Hence `F_{i+1}(g_i(y^*_i)) = g_i(F_i(y^*_i)) = g_i(y^*_i)`, and uniqueness of `F_{i+1}`'s fixed point gives `y^*_{i+1} = g_i(y^*_i)`. (2) Both directions, as elementary denominator bookkeeping. Forward: writing `y^*_i = a_i/q_i` reduced, `g_i(y^*_i) = (3^{m_i}a_i + (3^{m_i}−2^{m_i})q_i)/(2^{m_i+r_i}q_i)`, so the reduced denominator `q_{i+1}` divides `2^{m_i+r_i}q_i`; being odd (Lemma `14.15.9.1` for `P^{(i+1)}`), no factor of `2` can survive reduction into it, so `q_{i+1} | q_i`. Backward: `g_i^{−1}(v) = (2^{m_i+r_i}v − (3^{m_i}−2^{m_i}))/3^{m_i}` likewise gives `q_i | 3^{m_i}q_{i+1}`, and `q_i` is coprime to `3`, so `q_i | q_{i+1}`. Hence `q_{i+1} = q_i` for every `i`. (3) Mod `3` (in `Z₃`, where every `y^*_i` lives): `v₃(α_i) = m_i ≥ 1`, so `y^*_{i+1} = α_i y^*_i + β_i ≡ β_i = (3^{m_i}−2^{m_i})·2^{−(m_i+r_i)} ≡ −2^{−r_i} ≡ −(−1)^{r_i} (mod 3)` (`2 ≡ −1`). ∎

*(Integer form.)* In integer form this lemma is the transport recurrence on `12.6.1`'s rotation numerators `R_r` (cycles.md): via the seam identity `N_r + q = 2^{m_r} R_r` — `N_r` the rotated numerator of Lemma `14.15.9.1`, `R_r` and `q = 2^{S_P}−3^{M_P}` (unreduced) as in `12.6.1` — clause (1)'s orbit equation is the recurrence cleared of denominators, and clause (2) is the divisibility collapse; statement and provenance at Remark `12.6.1.1` (cycles.md).

**Theorem 14.15.9.3 (adelic anchor).** For every rotation `i`, the two adelic limits of `W^{(i)}` (`14.15.3.1`, `14.15.3.3`) are the rotated fixed point:

```text
y₂(W^{(i)}) = y^*_i  in Z₂        and        y₃(W^{(i)}) = y^*_i  in Z₃.
```

In particular `y₂(W) = y₃(W) = y^*` — the `2`-adic half, which `14.15.3`'s periodic-word identification did not previously cover (its mandatory identification is the `3`-adic half only), is now on file.

**Proof.** *`3`-adic half.* The left-infinite half of `W^{(i)}`, read deepest-first at whole periods, has length-`np` prefix `(P^{(i)})^n`, with composed constants `(A_P^n, B^{(i)}_{np})`. Induction from `F_i(y^*_i) = y^*_i` gives `A_P^n y^*_i + B^{(i)}_{np} = y^*_i`, so `v₃(y^*_i − B^{(i)}_{np}) = v₃(A_P^n y^*_i) ≥ nM_P` (`y^*_i ∈ Z₃`, `v₃(A_P^n) = nM_P`). By Theorem `14.15.3.3` the full offset sequence converges to `y₃(W^{(i)})`; its subsequence `B^{(i)}_{np}` converges to `y^*_i`; the limits agree.

*`2`-adic half.* Write `y₂ := y₂(W^{(i)})` (`14.15.3.1`; follower classes over the signed domain per `14.15.6.5`'s proof). For each `n ≥ 1` pick an integer `y_n` in the follower class of `W^{(i)}`'s length-`(n+1)p` prefix, so `v₂(y_n − y₂) ≥ (n+1)S_P + 1`. Since `y_n` follows the first `p` letters, `G^p(y_n) = F_i(y_n)` (`14.14.8.2`, sign-blind per `14.15.6`); and `G^p(y_n)` follows the length-`np` prefix of the `p`-shifted word, which is `W^{(i)}` again, so `v₂(F_i(y_n) − y₂) ≥ nS_P + 1`. Meanwhile `F_i(y₂) − F_i(y_n) = A_P(y₂ − y_n)` has `v₂ ≥ (n+1)S_P + 1 − S_P = nS_P + 1`. By the ultrametric inequality `v₂(F_i(y₂) − y₂) ≥ nS_P + 1` for every `n`, forcing `F_i(y₂) = y₂` in `Q₂`. The affine equation `(1−A_P)y = B` has exactly one solution in `Q₂` (`A_P ≠ 1`), and `y^*_i ∈ Q ⊂ Q₂` solves it; so `y₂ = y^*_i`. ∎

**Corollary 14.15.9.4 (per-position stratum facts; realization discharged).**

1. `v₂(y^*_i + 1) = m_i` exactly and, with `q^*_i := (y^*_i+1)/2^{m_i}` (a `2`-adic unit), `v₂(3^{m_i}q^*_i − 1) = r_i` exactly. In particular `y^*_i ≠ −1` for every `i`, and `G`'s defining formula, read as exact rational arithmetic, moves along the orbit: `3^{m_i}q^*_i − 1 = 2^{r_i}·y^*_{i+1}`, i.e. `G(y^*_i) = y^*_{i+1}`.
2. Any odd-denominator rational `u` with `v₂(u − y^*_i) ≥ m_i+r_i+1` satisfies both congruences of Lemma `14.15.1.3`(i) for the letter `(m_i,r_i)`; an **integer** such `u` lies on stratum `(m_i,r_i)`, with `G(u) − y^*_{i+1} = α_i(u − y^*_i)`.
3. **(The integer case: `14.15.7.5`'s hypotheses are theorems.)** If `y^*` is an integer (`q = 1`), then every `y^*_i` is an integer (Lemma `14.15.9.2`(2)), `stratum(y^*_i) = (m_i,r_i)`, `G(y^*_i) = y^*_{i+1}`, and every `y^*_i` is live — the `G`-orbit of `y^*` realizes `W`, which is `14.15.7.5`'s hypothesis (H1). And Lemma `14.15.9.1`(2) gives `2|y^*| < Q_1` unconditionally — (H2), which `14.15.7.5` carried as its one surviving smallness hypothesis (automatic only for `p = 1` there), is in fact automatic for **every** period. `14.15.7.5` therefore holds hypothesis-free; it is cross-referenced here, not edited.

**Proof.** (1) By Theorem `14.15.9.3`, `y^*_i = y₂(W^{(i)})` lies in every follower class of `W^{(i)}`'s prefixes, in particular in the first letter's cylinder class mod `2^{m_i+r_i+1}` (`14.15.1.5`/`14.15.1.3`(i), over the signed domain per `14.15.6.5`). The class's two congruences pin `v₂(y+1) = m_i` and `v₂(3^{m_i}q−1) = r_i` exactly for every `y ∈ Z₂` in the class — they are exact valuation statements determined by `y mod 2^{m_i+1}` and `q mod 2^{r_i+1}` respectively, valid verbatim for `2`-adic integers. Finiteness of `v₂(y^*_i+1)` gives `y^*_i ≠ −1`. The displayed identity is one line: `3^{m_i}q^*_i − 1 = (3^{m_i}(y^*_i+1) − 2^{m_i})/2^{m_i} = 2^{r_i}·(α_i y^*_i + β_i) = 2^{r_i}y^*_{i+1}` (Lemma `14.15.9.2`(1)), consistent with `v₂ = r_i` since `y^*_{i+1}` is a `2`-adic unit. (2) `14.15.1.3`(i)'s conditions are congruences mod `2^{m_i+r_i+1}`, satisfied by `y^*_i` per (1), hence by `u`; for integer `u` they *are* the stratum conditions; the affine difference identity is `14.14.4.1` applied at `u` and (as rational arithmetic) at `y^*_i` on the same stratum. (3) Immediate from (1)–(2), Lemma `14.15.9.1` (`3 ∤ a_i`), and Lemma `14.15.9.2`. ∎

### (b) The class theorem at whole-period windows

**Theorem 14.15.9.5 (whole-period class theorem).** Fix `n ≥ 1` and write `S_n := nS_P`, `M_n := nM_P`, so `Q_n = 2^{S_n+1}·3^{M_n}`. Over the signed domain:

1. **(Forward.)** The odd integers following `W`'s length-`np` forward prefix are exactly `{y : qy ≡ a (mod 2^{S_n+1})}` — the `2`-adic congruence class of `y^*`.
2. **(Backward.)** The odd `z` admitting the letter-prescribed backward chain to depth `np` are exactly `{z : qz ≡ a (mod 3^{M_n})}` — the `3`-adic congruence class of `y^*`.
3. **(Combined.)** The odd integers satisfying both are exactly `{y ≡ ρ_n (mod Q_n)}`, `ρ_n = a·q^{−1} mod Q_n`, an odd residue with `ρ_n ≢ 0 (mod 3)`. Every class member is live (`3 ∤ a`, settled by Lemma `14.15.9.1`(2)), and `−1` is never a member. Consequently `R^σ_{np,np}(W)` (Definition `14.15.6.8`) is exactly this class intersected with the sign condition and liveness of the deepest chain door — nothing else.

**Proof.** *Forward.* By Theorem `14.15.1.5` — read over the signed domain, per `14.15.6.5`'s proof — the followers form exactly one residue class mod `2^{S_n+1}`. It suffices to show the (nonempty) integer class `{qy ≡ a (mod 2^{S_n+1})}` is contained in it, since one class mod `2^{S_n+1}` containing another equals it. Let `y` be an odd integer with `v₂(y − y^*) ≥ S_n+1`. Induction along the rotations: for `0 ≤ j < np`, assume `v₂(G^j(y) − y^*_{j mod p}) ≥ S_n + 1 − Σ_{l<j}(m_{l mod p}+r_{l mod p})`; the right side is `≥ m_{j mod p}+r_{j mod p}+1`, because the letters not yet consumed sum to at least the current letter. By Corollary `14.15.9.4`(2), `G^j(y)` lies on stratum `(m_{j mod p},r_{j mod p})` and `G^{j+1}(y) − y^*_{(j+1) mod p} = α_{j mod p}·(G^j(y) − y^*_{j mod p})`, dropping `v₂` by exactly `m_{j mod p}+r_{j mod p}` — the induction closes, and `y` follows all `np` letters. *Backward.* By the signed admissibility-class lemma (`14.15.6.4`), the admitting `z` form exactly one class mod `3^{M_n}`, namely `B_n mod 3^{M_n}` for the deepest-first depth-`np` word — which is `P^n` (position `−np` carries letter `P_0`), whose composed constants are `(A_P^n, B_{np})` with `A_P^n y^* + B_{np} = y^*`, so `v₃(y^* − B_{np}) ≥ M_n` (Theorem `14.15.9.3`'s computation): the class is `{qz ≡ a (mod 3^{M_n})}`. *Combined.* The moduli are coprime and `ρ_n` is the unique residue mod `Q_n` congruent to `y^*` at both places; `ρ_n` is odd (`a`, `q` odd) and `ρ_n ≡ a·q^{−1} ≢ 0 (mod 3)`. `−1` is never in the class: every class member satisfies the first letter's cylinder congruence (the forward half just proved), which `−1` structurally never does (`14.15.6.5`'s proof: its `q`-part is even where the class's is odd). The `R^σ` clause is Definition `14.15.6.8` read against the two iffs, exactly as in `14.15.8.2`: the forward window condition *is* "follows the prefix", the backward condition *is* "chain exists to depth `np`" (intermediate chain doors need no liveness — `14.15.5.1`'s remark), `y₀`-liveness is automatic by (3), and what remains is sign and deepest-door liveness. ∎

**Verified** — `experiments/periodic_shelf.py`, fresh code (imports nothing from `multiletter_h_probe.py`, `h_nonintegral_probe.py`, `nonintegral_mechanism.py`, `height_exact_laws.py`, `realization_height.py`, `diagonal_converse.py`, `signed_diagonal.py`, `itinerary_coding.py`, `block_map.py`, or `door_seam.py`; exact integer/`Fraction` arithmetic at every pass/fail decision; deterministic, no RNG), functions `check_fixed_point_arithmetic`, `check_adelic_anchor`, `check_class_theorem`. Lemma `14.15.9.1`/`14.15.9.2` and Corollary `14.15.9.4`(1): every clause as exact `Fraction` identities — the `N/D` form, parity, `3`-coprimality, the bound `4N < 2^{S_P}3^{M_P}`, the sign law, `q | 2^{S_P}−3^{M_P}`, `gcd(q,6)=1`, `2|a| < Q_1`, the rotation orbit `y^*_{i+1} = α_i y^*_i + β_i`, the shared denominator, the `ε`-law, the two per-position `2`-adic stratum facts, and `3^{m_i}q^*_i−1 = 2^{r_i}y^*_{i+1}` — over the algebraic scan of **all** periods `p ≤ 3` with letters `m,r ≤ 3` (819 words, all rotations; the letter scan mirrors `14.15.7`'s own verification precedent, pure algebra, no heights computed) and over the full mandated grid (13 multi-letter probe words + 7 single-letter + the three integer words `1`, `−5`, `−17`, all rotations). Theorem `14.15.9.3`: `3`-adic offset bound `v₃(y^* − B_{P^k}) ≥ kM_P` at `k = 1..4` per rotation; `2`-adic half by **direct simulation** — the integer lift `a·q^{−1} mod 2^{nS_P+1}` follows the length-`np` prefix, `n = 1..3`, one positive and one negative representative each (signed domain); integer words' orbits realize their words by direct `G`-iteration. Theorem `14.15.9.5`: exhaustive two-directional scan (does {follows forward `np` letters ∧ chain exists to depth `np`} equal `{y ≡ ρ_n mod Q_n}`?) at `n = 1` over one full modulus width per sign, forward and backward decided by direct simulation only, on five words spanning periods 1–3, integer and non-integral, positive and negative fixed points (`(2,2)`; `(2,1)`; `((1,1),(1,2))`; `((2,1),(2,2))`; `((1,1),(1,2),(1,2))`): `35,563` exhaustive iff decisions, `0` discrepancies either direction; on every class member, `y₀`-liveness confirmed automatic, `−1` confirmed absent, and the `R^σ` description (sign + deepest-door liveness only) confirmed against direct-simulation membership. Total `69,802` checks, `0` failures, `0.2` s (2026-07-17).

### (c) The unified identities

**Theorem 14.15.9.6 (the identities, unified over `q ≥ 1`).** Parametrize the class of Theorem `14.15.9.5` as `y₀ = ρ_n + κQ_n` (`κ ∈ Z`); since `0 < ρ_n < Q_n`, the positive sector's members are exactly `κ = k ≥ 0` and the negative sector's exactly `κ = −k`, `k ≥ 1`, each in strictly increasing `|y₀|`. Then, for every period `P` — integer or non-integral fixed point — every `n ≥ 1`, and both sectors:

1. **(The progression offset.)** `j_n := (qρ_n − a)/Q_n` is an integer with `0 ≤ j_n ≤ q`. For `q > 1`: `j_n ∈ {1,…,q−1}`, and

```text
j_n = −a·2^{−1}·g_P^{−n} mod q,
```

purely periodic in `n` from `n = 1` with period **exactly** `ord_q(g_P)`. For `q = 1`: `j_n = [y^* < 0]`, constant (the degenerate orbit, matching `ord_1 = 1`).

2. **(The deepest door.)** For the class member `y₀ = ρ_n + κQ_n`, the letter-prescribed chain's deepest door is

```text
y_{−np} = y^* + (y₀ − y^*)/A_P^n = (a + (j_n + κq)·2^{2nS_P+1})/q        exactly,
```

and, since `2^{2nS_P+1}` is `2` to an odd power, hence `≡ 2 (mod 3)` for every `n`,

```text
y_{−np} ≡ t_n + 2κ (mod 3),        t_n := (a + 2j_n)·q^{−1} mod 3.
```

3. **(The death law and the first-viable rule.)** Within each sector exactly one progression-index class mod `3` has a dead deepest door — `κ ≡ t_n (mod 3)` — and every other candidate is a member of `R^σ_{np,np}(W)`; so the first-viable indices are `k⁺_n = [t_n = 0]` (positive sector) and `k⁻_n = 1 + [t_n = 2]` (negative sector).

4. **(Closed forms.)** For every `n ≥ 1`:

```text
H⁺_{np,np}(W) = ρ_n + [t_n = 0]·Q_n,        H⁻_{np,np}(W) = (1 + [t_n = 2])·Q_n − ρ_n.
```

**Proof.** (1) `qρ_n ≡ a (mod Q_n)` by definition, so `j_n ∈ Z`; `0 < ρ_n < Q_n` and `2|a| < Q_n` (Lemma `14.15.9.1`(2)) give `−1/2 < j_n < q + 1/2`, so `j_n ∈ {0,…,q}`. For `q > 1`, `j_n = 0` would force `ρ_n = a/q ∉ Z` and `j_n = q` would force `ρ_n − Q_n = a/q ∉ Z`, so `j_n ∈ {1,…,q−1}`; mod `q`, `0 ≡ qρ_n = a + j_nQ_n` and `Q_n = 2·(2^{S_P}3^{M_P})^n ≡ 2g_P^n (mod q)`, so `j_n ≡ −a·2^{−1}·g_P^{−n}`, pinned exactly by the range. Period: `n ↦ g_P^{−n} mod q` is purely periodic from `n = 1` with period `ord_q(g_P^{−1}) = ord_q(g_P)`, and multiplication by the unit `−a·2^{−1}` is injective, so `(j_n)` has that exact period and no pre-period. For `q = 1`: `ρ_n = a + j_nQ_n` with `0 < ρ_n < Q_n` and `|a| < Q_n` forces `j_n = 0` for `a > 0` and `j_n = 1` for `a < 0`. (2) The chain exists by Theorem `14.15.9.5` and each chain door lies on its prescribed stratum (forced, `14.15.6.3`), so the chain read forward follows `P^n` and `14.14.8.2` gives `y₀ = A_P^n y_{−np} + B_{np}`; subtracting `A_P^n y^* + B_{np} = y^*` (Theorem `14.15.9.3`'s computation) gives `y_{−np} = y^* + (y₀ − y^*)/A_P^n`. Then `y₀ − y^* = (qρ_n − a)/q + κQ_n = (j_n + κq)Q_n/q` and `Q_n/A_P^n = 2^{S_n+1}3^{M_n}·2^{S_n}3^{−M_n} = 2^{2nS_P+1}`, giving the displayed formula — an integer, being an actual chain door. Mod `3`: `2^{2nS_P+1} ≡ 2`, so `y_{−np} ≡ (a + 2j_n)q^{−1} + 2κ = t_n + 2κ`. (3) By Theorem `14.15.9.5`(3), every sector candidate passes every condition of `R^σ_{np,np}` except possibly deepest-door liveness. Death: `y_{−np} ≡ 0 (mod 3)` ⟺ `2κ ≡ −t_n` ⟺ `κ ≡ t_n (mod 3)` (`2^{−1} ≡ 2`, `−2 ≡ 1`) — one `κ`-class. First-viable: positive sector, `k = 0` dies iff `t_n = 0` and then `k = 1` survives; negative sector, `k = 1` dies iff `−1 ≡ t_n`, i.e. `t_n = 2`, and then `k = 2` survives. (4) `|y₀| = ρ_n + kQ_n` resp. `kQ_n − ρ_n` is strictly increasing in `k` within each sector, so `H^σ` is the value at the first-viable index. ∎

**Corollary 14.15.9.7 (the integer case folded in; `14.15.7.5` reconciled).** For `q = 1` (so `a = y^*`, `ρ_n = y^*` or `y^* + Q_n`), Theorem `14.15.9.6`'s closed forms hold verbatim and evaluate as follows: the sector containing `y^*` is **capped at `|y^*|` for every `n`** — for `y^* > 0`, `t_n = y^* mod 3 ≠ 0` gives `H⁺ = ρ_n = y^*`; for `y^* < 0`, `t_n = (y^*+2) mod 3 ≠ 2` (since `3 ∤ y^*`) gives `H⁻ = Q_n − ρ_n = |y^*|` — and the opposite sector escapes with `H = k₀Q_n + σ'y^*`, `k₀ = 1+[t_n=2]` resp. `1+[t_n=0]` `∈ {1,2}`, exactly `14.15.7.2`(4)/`14.15.7.5`'s `k₀`-rule. So `14.15.7`'s capped/escaping dichotomy is the `q = 1` degenerate case of the one law — the class's CRT lift sits at the `n`-independent distance `|y^*|` from the sector boundary `{0, Q_n}`, so one sector's minimum is the constant `|y^*|` instead of growing — and its instances (`14.15.7.3`, `14.15.7.4`, `14.15.7.6`) are reproduced verbatim. The reconciliation, stated precisely: `14.15.7.5` proved this law under two hypotheses; both are now discharged — (H1)'s realization clause is a theorem (Corollary `14.15.9.4`(3): integrality alone implies the orbit realizes `W`), and (H2), which `14.15.7.5` carried as the one surviving smallness condition (automatic only at `p = 1` there), is unconditional at every period (Lemma `14.15.9.1`(2): `2|a| < Q_1/4`). No hypothesis survives. `14.15.7` is cross-referenced throughout, never edited.

**Stated plainly (the headline of this section).** On any periodic word, the per-sector realization height at whole-period windows obeys an exact law: capped at `|y^*|` in the realized sector when `y^*` is an integer — the smallness that makes the cap work now being automatic — and escaping at the CRT-modulus rate `Q_n = 2^{nS_P+1}·3^{nM_P}` with a purely periodic, denominator-bounded constant otherwise. Both behaviors are read off one closed form; the entire distinction is whether the reduced denominator `q` of the word's own adelic fixed point is `1`.

**Verified** — `experiments/periodic_shelf.py`, function `check_identities`. All four identities and the fold-in on the full grid (20 probe words + 3 integer words), both sectors, `n ∈ {1, 2, n_probe_max+1}` per word — the extrapolation row lying strictly beyond each probe's published range (single-letter: `n = 26`; multi-letter: each word's own `n_max+1`, up to `n = 63`, heights `≈ 10^{264}`) — with every quantity on the simulation side produced by direct simulation only: every candidate on the class progression (`k = 0..6` positive, `1..7` negative — two full mod-3 cycles past the first viable) checked to follow the forward prefix by iterated `G`, to admit the backward chain by the unique-predecessor formula with integrality at every step, to be live, odd, `≠ −1`, of the right sign; the deepest door compared against Identity 2's closed form and its mod-3 value; the dead/live pattern against the death law at every candidate; the first-viable index against the rule; `H` against Identity 4 and `v_n` against its exact form (`Fraction` arithmetic). `144` word/sector/`n` rows, `0` failures. Published tables: all `80` brute-force entries of both probes (`28` single-letter + `52` multi-letter, `n = 1, 2`) reproduced exactly by the closed forms. Integer case: the three words' `14.15.7` laws (`H⁺ = 1`/`H⁻ = 2·12^n−1`; `H⁺ = 4·72^n−5`/`H⁻ = 5`; `H⁺ = 4·4478976^n−17`/`H⁻ = 17`) reproduced exactly at `n = 1..3` (and the capped/escaping evaluation at `n ∈ {1,2,3,7}`), `0` failures (2026-07-17).

### (d) The corollaries: periodicity, the corrected sharp constant, the spectrum law, rotations

Throughout, `q > 1` (the non-integral case; for `q = 1` the corollaries hold trivially with `ord_1 = 1` and the capped/escaping evaluation of Corollary `14.15.9.7`). Write `t(j) := (a + 2j)·q^{−1} mod 3` (so `t_n = t(j_n)`), and

```text
V₊(j) := j/q + [t(j) = 0],        V₋(j) := 1 + [t(j) = 2] − j/q.
```

**Corollary 14.15.9.8 (P1: pure periodicity of the normalized height).** Define, per sector, `v_n := H^σ_{np,np}(W)/Q_n − σ·a/(qQ_n)`. Then `v_n = V₊(j_n)` (positive sector) and `v_n = V₋(j_n)` (negative sector) exactly, and `(v_n)_{n≥1}` is purely periodic from `n = 1` with period **exactly** `P_alg := ord_q(g_P)`, both sectors.

**Proof.** Substituting Theorem `14.15.9.6`(4) and `ρ_n/Q_n = a/(qQ_n) + j_n/q` gives the displayed forms; since `t_n` is a function of `j_n`, `(v_n)` is purely periodic with period dividing `P_alg` (Theorem `14.15.9.6`(1)). Exactness: `V_σ` is injective on `{1,…,q−1}` — `v_n` is never an integer (`j_n/q ∉ Z`), so `v_n ∈ (0,1) ∪ (1,2)` determines the added indicator (`⌊v_n⌋` resp. `⌈v_n⌉ − 1`) and then `j_n` — so a shorter period for `(v_n)` would be a shorter period for `(j_n)`, contradicting Theorem `14.15.9.6`(1)'s exactness. ∎

**Corollary 14.15.9.9 (P2: the lower bound and the sharp constant, corrected form).** `v_n ≥ 1/q` for every `n ≥ 1`, both sectors — so `H^σ_{np,np}(W) ≥ (Q_n − |a|)/q`: escape at the full CRT-modulus rate on the entire non-integral shelf, with a denominator-bounded constant. The sharp per-word, per-sector constant is

```text
c_σ(W) := min_n v_n = min over the visited orbit O := (−a·2^{−1}·⟨g_P⟩ mod q) of V_σ(j),
```

`|O| = P_alg`, attained periodically — a joint function of the coset orbit **and** the mod-3 door law, not of the orbit alone. It reduces to the orbit minimum in the positive sector — `c₊ = j_min/q`, `j_min := min O` — **iff `t(j_min) ≠ 0`** (and dually `c₋ = 1 − j_max/q` iff `t(j_max) ≠ 2`); the generic bound `1/q` is attained iff `1 ∈ O` with `t(1) ≠ 0` (positive sector) resp. `q−1 ∈ O` with `t(q−1) ≠ 2` (negative). The reduction genuinely fails: on the multi-letter probe's grid the six words `((1,1),(1,2))` (`c₊ = 2/23` vs `j_min/q = 1/23`), `((1,1),(2,1))` (`3/5` vs `2/5`), `((2,1),(2,2))` (`2/47` vs `1/47`), `((1,1),(1,1),(2,1))` (`10/47` vs `5/47`), `((1,1),(1,2),(1,2))` (`13/229` vs `2/229`), and `((1,1),(1,2),(2,2))` (`26/431` vs `13/431`) all have `t(j_min) = 0` — the probe's M2 refutation instances, now the theorem's own equality-failure cases — while on all seven single-letter words `t(j_min) ≠ 0` happens to hold, which is why the single-letter shortcut `j_min/q` (`14.15.8.5`) survived there.

**Proof.** Positive sector: `v_n = j_n/q + k⁺_n ≥ j_n/q ≥ 1/q`. Negative: `v_n = k⁻_n − j_n/q ≥ 1 − (q−1)/q = 1/q`. The constant is `min_O V_σ` by pure periodicity (every orbit value is visited infinitely often, Corollary `14.15.9.8`). If `t(j_min) ≠ 0` then `V₊(j_min) = j_min/q ≤ V₊(j)` for every `j ∈ O`; if `t(j_min) = 0` then `V₊(j_min) = j_min/q + 1` and every other `V₊(j) ≥ j/q > j_min/q`, so `c₊ > j_min/q` strictly. The dual and the equality cases (`V₊(j) = 1/q` forces `j = 1`, `t(1) ≠ 0`; `V₋(j) = 1/q` forces `j = q−1`, `t(q−1) ≠ 2`) are immediate. ∎

**Corollary 14.15.9.10 (P3: one extra progression step; no capped sector).** `k⁺_n ∈ {0,1}` and `k⁻_n ∈ {1,2}` for every `n`. For `q > 1` **no capped sector exists**: both sectors escape at rate `Q_n` — consistent with the per-sector equivalence theorem (`14.15.6.10`), since `W`'s unique diagonal point `y^* = a/q` (`14.15.6.7`, Theorem `14.15.9.3`) is not an integer, so no door of either sign integrally realizes `W`.

**Proof.** Immediate from Theorem `14.15.9.6`(3) and Corollary `14.15.9.9`'s lower bound; the consistency sentence cites `14.15.6.10`, not re-derived. ∎

**Theorem 14.15.9.11 (P4: the spectrum law — the coincidence proved, in corrected form).** Define the **signature** of a periodic word `W` with fixed point `y^* = a/q`:

```text
sig(W) := (q, g_P, C, ε),    C := −a·2^{−1}·⟨g_P⟩ ⊆ (Z/q)^×,    ε := y^* mod 3 = a·q^{−1} mod 3 ∈ {1,2}.
```

Then `t(j) = ε + 2j·q^{−1} mod 3` — a function of `(q, ε)` and `j` alone — so:

1. **(Coincidence.)** The per-sector spectrum `Spec_σ(W) := {v_n : n ≥ 1} = V_σ(C)` is a function of `sig(W)` alone. Two periodic words with equal signatures — any periods, any rotations — have identical spectra in both sectors.
2. **(Sector swap.)** If `sig(W') = (q, g_P, −C, −ε)` — the negation of `sig(W)`, both entries flipped — then `Spec₊(W') = Spec₋(W)` and `Spec₋(W') = Spec₊(W)`. Proof in two lines: `j ↦ q−j` bijects `C`'s representatives with `(−C)`'s, and `t'(q−j) = −ε + 2(q−j)q^{−1} = 2 − t(j) (mod 3)`, so `[t'=2] = [t=0]` and `[t'=0] = [t=2]`, giving `V'₋(q−j) = V₊(j)` and `V'₊(q−j) = V₋(j)` term by term.
3. **(Reconciliation with the probe; `ε` is not redundant.)** The probe's coincidence pair — `((1,2),(2,2))` (`49/101`) and `((1,1),(1,1),(1,2))` (`37/101`) — has **equal signatures** (`q = 101`, `g_P = 22`, same coset, `ε = 2` both), and its swap pair — `((2,1),(2,2))` (`85/47`) and `((1,1),(1,1),(2,1))` (`143/47`) — has **negated signatures** (`ε = 2` vs `1`): both observations are instances of (1)–(2). But the probe's phrasing through the triple `(q, g_P, coset)` alone does not survive in general — `ε` is an independent datum, pinned by the preceding letter's `r`-parity (Lemma `14.15.9.2`(3)), not by the triple. Witness, inside the mandated verification grid: rotations `0` and `1` of `((1,1),(1,2))` — fixed points `7/23` and `11/23` — share `(q, g_P, C) = (23, 12, the quadratic-residue coset)` yet have `ε = 2` resp. `1` (the word's two `r`'s have opposite parity), and their positive-sector spectra differ: `{2,3,6,8,9,12,18,24,27,36,39}/23` vs `{1,3,4,6,9,12,13,16,18,25,31}/23`, both realized by direct simulation over full periods. This corrects the probe's §5 phrasing the same way the probe corrected the single-letter sharp constant: the exact invariant is the signature, one datum finer than the observed triple. On the probe's own 13-word grid the triple happened to determine `ε` on every compared pair, which is why the coarser phrasing survived there.

**Proof of (1).** `Spec_σ(W) = {V_σ(j_n)} = V_σ(O)` with `O = C`'s representatives (Theorem `14.15.9.6`(1), Corollary `14.15.9.8`), and `V_σ` depends on `j` only through `j/q` and `t(j) = (a+2j)q^{−1} = ε + 2j·q^{−1} (mod 3)` — every ingredient a function of the signature. ∎

**Corollary 14.15.9.12 (P5: rotations).** Every rotation `P^{(i)}` is itself a period, so Theorems `14.15.9.5`–`14.15.9.6` and Corollaries `14.15.9.8`–`14.15.9.10` apply to `W^{(i)}` verbatim with the **same** `(S_P, M_P, Q_n, g_P, q)` and its own numerator `a_i` (Lemma `14.15.9.2`): one cyclic word carries a `p`-tuple of exact laws over one shared denominator — per-rotation offsets `j^{(i)}_n = −a_i·2^{−1}·g_P^{−n} mod q` (whence the probe's observed unit-multiple relation `j^{(i+1)}_n ≡ (a_{i+1}·a_i^{−1})·j^{(i)}_n (mod q)`), per-rotation residues `ε_i = −(−1)^{r_{i−1}}`, and per-rotation signatures and spectra per Theorem `14.15.9.11` — the `ε`-witness there showing that two rotations of one word can already have different spectra while sharing the triple. This is the probe's M4 in whole-period generality. ∎

**Verified** — `experiments/periodic_shelf.py`, functions `check_P1_periods`, `check_P2_P3`, `check_P4_spectra`, `check_P5_rotations`. P1: `(j_n)` and `(v_n)`, both sectors, computed over two full algebraic periods plus two (`n` up to `102` for `q = 101`), exact minimal period equal to `ord_q(g_P)` (every shorter candidate period tested and rejected), all 20 words, `ord` matching both probes' detected periods. P2/P3: the visited `j`-set over one period equals the coset orbit exactly; `min_O V_σ ≥ 1/q`; the sharp constants match both probes' published per-word minima `40/40` (both sectors); the six M2-refutation instances confirmed with the cause `t(j_min) = 0` in every case, and `c₊ = j_min/q` confirmed on the remaining fourteen; the reduction criteria checked as iffs; `k`-ranges exact. P4: the signature function reproduces every word's two spectra and its realized `v`-set; the coincidence pair's signatures equal and spectra equal; the swap pair's signatures negated and spectra swapped; the negation involution verified as pure algebra on all 20 words; the `ε`-witness verified end to end — triples equal, `ε = 2` vs `1`, spectra as displayed — **including direct simulation of all four spectra** (both rotations, both sectors, `n = 1..11`; rows `7..11` lie beyond the probe's M4 range `n ≤ 6`). P5: all `12` rotations of the probe's five M4 words (`q = 23, 5, 37, 175, 229`): shared `q`, per-rotation closed forms simulation-checked at `n = 1, 2` both sectors, `j`-law at `n = 1..6`, unit-multiple relation between consecutive rotations. Full run: `83,573` exact checks, `0` failures, `0.4` s (2026-07-17).

### (e) Scope, accounting, and closing status

**Scope note (the one residual formulation gap).** Everything above is for **whole-period diagonal windows** — window `(np, np)` in letters, `n` periods each side, `14.15.7.5`'s convention. Per-letter (period-cutting) windows are genuinely open machinery: a window that cuts a period partway anchors its partial past at a *rotated* fixed point rather than at `y^*` — the fixed points rotate mid-window — and no height law at such windows is stated or claimed here. Recorded as the shelf's one residual formulation gap, explicitly not pursued (stopping-rules register; open-problems.md 11.9).

**Accounting.** The periodic shelf is now closed by theorem at whole-period windows: on **any** periodic word — any period, both sectors, integer or non-integral fixed point — the per-sector realization height obeys an exact law, capped at `|y^*|` in the realized sector when `y^*` is an integer (the smallness that makes the cap work now proved automatic) and escaping at the CRT-modulus rate `Q_n = 2^{nS_P+1}·3^{nM_P}` with a purely periodic, denominator-bounded constant otherwise. These are exact laws on the **decided** shelf: for every periodic word the two adelic limits are pinned by the single rational `y^*` (Theorem `14.15.9.3` — now including the `2`-adic half), and realization or escape is elementary arithmetic in the unit-group orbit of `Q_n mod q` and the parity of the exponent in `2^{2nS_P+1} mod 3`. So height growth itself now contributes no further obstruction once a periodic word's fixed-point denominator `q` is known: at `q = 1` the realized sector is capped exactly at `|y^*|`; at `q > 1` both sectors escape at the CRT-modulus rate. What this does **not** close is periodic cycle exclusion — determining which arbitrary periods have `q = 1` is exactly determining which composed rational fixed points are integers, i.e. which periodic words give integer cycles (Corollary `14.15.9.4`), and that remains open beyond the known instances. Separately, the Bridge (bridge.md §16) is unmoved: nothing here bounds `H`, gives it a recurrence, or bounds its escape rate on any non-periodic word. Bridge status unchanged (`14.14.6`).

**Closing status.** What changed: the multi-letter probe's four identities and four verdicts are theorems with proofs for every period and every `n` (`14.15.9.5`–`14.15.9.12`), with the adelic anchor and rotation lemma (`14.15.9.1`–`14.15.9.4`) supplying the two facts the probes could only observe — the fixed point *is* both adelic limits, and the rotations share one denominator. The empirical caveats of **both** probe findings docs (`briefs/h-nonintegral-probe-findings.md`, `briefs/multiletter-h-probe-findings.md` — "verified identities over the tested range only, not theorems") are discharged; the two probes' 20 words, with rotations, are the verified instance set. Two of the shelf's simplifications ended corrected rather than confirmed, both in the same direction — the exact invariant is finer than the observed one: the sharp escape constant is `min_O V_σ`, not `j_min/q` (the probe's own M2 correction, now with its exact failure criterion `t(j_min) = 0`), and the escape-spectrum invariant is the signature `(q, g_P, C, ε)`, not the triple (this section's correction, witnessed inside the mandated grid). `14.15.7.5`'s two hypotheses are discharged — its law now holds hypothesis-free — and `14.15.7`/`14.15.8` stand as the `p = 1` and `q = 1` faces of one law, cross-referenced, never edited. What did not change: the Bridge is unmoved — these are closures on the decided side of the boundary, and deciding boundedness of `H` for any word beyond the periodic family remains exactly the diagonal-locus question as `14.15.4`(d)/`14.15.5`(d) posed it. Per the brief's stop lines: no per-letter/period-cutting window; no aperiodic word; no new empirical grid beyond what verification required on the probes' 20 words, their rotations, and the three integer words; no cycle-exclusion attempt; no equidistribution proof attempt.
