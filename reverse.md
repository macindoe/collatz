---
status: ACTIVE — mirror machinery exact; dead ends mapped (14.5: door mortality + Gardens of Eden, both proved); renewal equation resolved heuristically with mortality (supercritical, margin 1.52 — predicts full density); rigorous density bound PROVED (14.6 summary; canonical five-lemma proof in paper 2: π̃(X) ≥ 2^(−3.6)X^0.3, c* = 0.3304); steering laws back-ported with the one-identity synthesis (14.12); the forward per-step machinery is fully dualized (14.7–14.10: digit-determinacy, anchor increment, one-step dichotomy, depth ladder — all proved and verified); KL–LP refinement (branch `kl-lp`, CLOSED per brief stop criterion): 14.6.5 multi-door renewal PROVED, small lift to c* ≈ 0.33515; 14.13 stages 2–3 (mod-3^k LP, exact anchor phases) hit a precisely-recorded structural obstruction (affine collapse map ⇒ no free residue/anchor propagation), 0.43 bar not reached
scope: new section 14 (post-monolith)
updated: 2026-07-11
source: new material; the author's reversal question; builds on 9.8 (spine.md), 11.5 (open-problems.md), §3 anchor machinery
---

> **Current state.** The reduced map run backward. The predecessor structure of `F` is completely characterized (14.1, verified exactly against brute force), and it is governed by a **3-adic anchor** `M₃(y)` — an affine logarithm base 2 — through the exact law `d = 1 + v₃(s − M₃(y))` (14.2): the precise mirror of the forward 2-adic law, with the roles of 2 and 3, and of `s` and `d`, exchanged (duality table, 14.3). The backward branching ledger is `P(d = j) = 2·3^(−j)`, verified. The backward tree from `(1,1)` is enumerable exactly in increasing `ω`; its empirical growth exponent is ≈ 0.97–0.98 and rising with the cutoff, consistent with density one (14.4). Honest scope: backward reachability of all states *is* the conjecture (9.8), so this front proves no shortcut — its target is the density program: an exact renewal equation for the tree from the exact branching law, aimed at the Krasikov–Lagarias-type exponents. The first naive renewal equation was wrong (representative multiplicity) and is recorded as the open item. **The queue of dual per-step theorems (14.7–14.10) is now closed**: digit-determinacy, the anchor-increment law, the one-step decision procedure, and the depth ladder all have exact 3-adic mirrors, each verified independently — and each also carries a genuine, non-forced asymmetry against its forward counterpart, precisely identified rather than papered over (no cross-prime step in 14.7's division; a hard mortality-freeze in 14.8 with no forward analogue; a trichotomy collapsing to a dichotomy in 14.9; a forced step-size-2 in 14.10's ladder).

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

1. *Naive stationary residue tracking.* First construction: states = `y mod 3^k`; transition for admissible `s` computed directly from a `k`-digit representative, claiming the child's *full* `k`-digit residue is representative-independent whenever `d = v₃(N) < k`. This is **false** and was caught by an explicit counter-check (540 transitions tested against varied higher digits of `y`, 224 failures) — the correct statement (re-derived and verified with zero failures over 4,160 checks) is that a parent known mod `3^k` pins the child only mod `3^(k−d)`: dividing by `3^d` costs exactly `d` digits of precision, and since admissible `s` forces `d ≥ 1` always, **no step is free** — a strictly stationary, same-`k`-forever residue system does not exist. This is the concrete, verified form of the affine-map obstruction flagged in 14.6.5's honest assessment.

2. *Drop-on-overflow.* Second construction: states = `(j, r)` — "known to `j` digits, currently `r mod 3^j`" — with `j` strictly decreasing each step (by `d`) and any transition that would exhaust precision simply dropped (zero credit, a valid but conservative simplification). Because `j` strictly decreases with every edge, the resulting transition graph is a **finite DAG with no cycles** — its spectral radius is identically `0` for every `c`. This construction can never certify supercriticality at *any* exponent; it is mathematically correct but useless (confirmed directly: bisection collapses to the search floor for every `k` tried, 1–6).

3. *Generic fallback credited at weight 1.* Third construction: same `(j,r)` states, but instead of dropping an exhausted-precision transition, credit it at weight `1` (as if the child trivially satisfies `f(child,X) ≥ (X/child)^c`) and solve the resulting acyclic system bottom-up. This produces attractive-looking numbers (`k=2`: `c*≈0.41`; `k=3`: `c*≈0.50`; `k=6`: `c*≈0.57`, still climbing) — **but the construction is unsound**: crediting weight `1` unconditionally is only valid once the *accumulated size* from the true root has already crossed the renewal threshold (Lemma renewal's actual base case, paper §8), not merely once residue precision runs out. Precision exhaustion and size-threshold crossing are different events — a child can run out of tracked digits while still being small relative to `X` — and the construction conflates them. No fix was found and verified in-session; **these numbers are not claimed**, only recorded so the trap is not walked into twice (precedent: 14.4's discarded single-type renewal equation).

**Diagnosis.** All three failures trace to one fact, first surfaced in 14.6.5: the collapse map `y ↦ (2^(s+1)y − 1)/3` is *affine*, not multiplicative, so neither the anchor `M₃(y)` nor a truncated residue `y mod 3^k` propagates to the child without irreducible loss (exactly `d` digits per step, `d ≥ 1` always). Krasikov–Lagarias do not face this: their difference-inequality system tracks the map's residue behavior directly, without an analogue of our door/collapse structure, and — per 14.6.5 — their inequalities *bound* branching where our anchor law would give it *exactly*, but exactness only helps if it can be carried forward, and here it provably cannot be carried forward for free.

**Answering the 14.6 remark's open question.** *Whether exactness buys anything beyond `0.84`* is not resolved in the affirmative by this program: the one avenue that would have delivered it (a stationary exact-residue LP exploiting `14.2.4`) is obstructed by the precision loss above. The multi-door resource (14.6.5) is exact and does compose, and it buys a real but small lift. Whether a *correctly* size-threshold-coupled version of construction 3 recovers real gains from residues remains open — it is a well-defined technical question (couple the DAG in `(j,r)` to the outer renewal induction's own accumulated-offset variable, rather than crediting exhaustion for free) but was not resolved here.

**Status.** Primary success bar (`c > 0.43`, Krasikov 1989) **not reached** as a verified theorem. Stage 1 (14.6.5) stands as the session's one verified gain: `c* : 0.3304 → 0.33515`. Stages 2–3 close with the obstruction above, precisely stated, per the brief's equally-valid stop condition. No code from attempt 3 is presented as a result; the diagnostic scripts are not committed (dead ends recorded here in prose, per house norms, rather than as unrunnable/misleading code).
