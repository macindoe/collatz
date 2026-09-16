# Findings: the comb as the word (comb.md 18.7)

Delegated session, branch `comb-dictionary`. Supports `briefs/comb-dictionary-brief.md`.

## Base SHA and branch

The worktree's HEAD at spawn was `a7543ce` (2026-09-13), which predates the brief: `briefs/comb-dictionary-brief.md` did not exist there and the worktree had no commits of its own. `git reset --hard main` fast-forwarded it onto local `main` at `2d0bca6` (2026-09-16, the brief's own delegation commit), and `comb-dictionary` was cut from there.

**Base SHA: `2d0bca6`.**

## Notation

As on comb.md: a node `v = (ω,d)` has peak `A = 3^d ω − 1 = 2^s y`, `s = v₂(A)`, `y` the exit; `state(y) = (Ω, D)` with `y + 1 = 2^m 3^a Ω`, `D = m + a` (door recovery, reverse.md 14.6.5.1), so `y` is the door `y_a` of `state(y)`; `node(y, s)` is the state at branch `s` on door `y`, `2^s y + 1 = 3^d ω`. The exit map is `G(y) = (3^m q − 1)/2^r` with `q = (y+1)/2^m`, `r = v₂(3^m q − 1)`, and `stratum(y) = (m, r)` (reverse.md 14.14.3–14.14.4; itinerary.md 14.15.1.1). Two facts used throughout, both on file: `G(y)` is the exit of `state(y)` (14.14.3.2's proof: `3^m q = 3^D Ω`, so `3^m q − 1` is the peak of `state(y)`), and hence `r(y) = s(state(y))` for every door `y` of a state — all doors of one state share `r` (14.14.6).

## Item A — Lemma 18.7.1, derived

Let `v ≠ (1,1)` be a comb node with `F`-orbit `v = v₀, v₁, …, v_η = (1,1)`, `η = η(v) ≥ 1` the first index at which the orbit is `(1,1)`. For `i < η` write `s_i = s(v_i)`, `y^{(i)}` for the exit of `v_i` (a door of `v_{i+1}`), and `a_i = v₃(y^{(i)} + 1)` for its door index in `v_{i+1}` (`y^{(i)} = y_{a_i}` of `v_{i+1}` by door recovery; `a_i = a₊ = v₃(C)` of the step by 14.14.1.1).

**(a) Edges.** From `v_i`, at branch `s_i` on door `y^{(i)}`, Proposition 18.2.2(b) gives `⌊(s_i − 1)/2⌋` cascade edges to the lowest sibling `w_i` on that door. If `w_i` is not the root, its parent edge is the door edge to `state(y^{(i)}) = F(v_i) = v_{i+1}`, entering through the door `y^{(i)} = y_{a_i}(v_{i+1})`. `w_i` is the root iff `y^{(i)} = 1`: the root is the branch-`1` node of door `1`, the lowest sibling on door `1` is at branch `1`, and a node on a door `y ≠ 1` is not on door `1`. And `y^{(i)} = 1` iff `v_{i+1} = state(1) = (1,1)` (the only door of `(1,1)` is `y₀ = 2·1 − 1 = 1`; conversely `state(1) = (1,1)`), iff `i + 1 = η` (`(1,1)` is `F`-fixed and `η` is the first hitting index). So for `i ≤ η − 2` the path carries `⌊(s_i − 1)/2⌋` cascade edges and one door edge into `v_{i+1}` through door `a_i`; for `i = η − 1` it carries `(s_{η−1} − 1)/2` cascade edges on door `1` down to the root and no door edge (`y = 1 ≡ 1 (mod 3)`, so `s_{η−1}` is odd; `v_{η−1} ≠ (1,1)` is on door `1` at branch `≥ 3`, so this run is at least one edge). Hence

```text
door edges = η − 1,     λ(v) = Σ_{i<η} ⌊(s_i − 1)/2⌋ + (η − 1),
```

Proposition 18.3.2(b) with the cascade count written out. Holds as the brief states it.

**(b) Letters.** Let `W = ((m_0,r_0), …, (m_{η−1},r_{η−1}))` be the itinerary word of the exit `y^{(0)}` (Definition 14.14.8.1 / itinerary.md 14.15.1.2): `y^{(i+1)} = G(y^{(i)})`, since `G(y^{(i)})` is the exit of `state(y^{(i)}) = v_{i+1}`. Then `m_i = v₂(y^{(i)} + 1) = D_{i+1} − a_i` (door recovery, `D_{i+1} = d(v_{i+1})`) and `r_i = s(state(y^{(i)})) = s_{i+1}`, with `s_η = s(1,1) = 1`; the last letter is the letter of door `1`, `(1,1)`. So `η` is the letter count, and

```text
λ(v) = ⌊(s_0 − 1)/2⌋ + Σ_{i<η} ⌊(r_i − 1)/2⌋ + (η − 1),
```

where `s_0` is the `r`-component of the letter of any door of `v` (all doors of `v` share `r = s(v)`). Letter `i ≤ η − 2` is the door edge into `v_{i+1}` through door `a_i = D_{i+1} − m_i` followed by `v_{i+1}`'s own cascade run of `⌊(r_i − 1)/2⌋` edges; the last letter `(1,1)` contributes nothing — its door edge would be the root's self-loop, excluded, and its run `⌊(1−1)/2⌋` is empty; the run of `v` itself, `⌊(s_0 − 1)/2⌋`, precedes the word.

**What the brief's phrasing left implicit.** "The node's itinerary word read from its own door" is exact if the word is started one letter early, at any door of `v` (letter `(m, s_0)`): then every letter is one door edge plus a run of `⌊(r − 1)/2⌋` cascade edges, the first letter's door edge being the edge *into* `v` (below `v`, not on the path) and the last letter's the excluded self-loop. Started at the exit `y^{(0)}` instead, the word has exactly `η` letters and `v`'s own run has to be added. The page states the second form (letter count `= η` is the cleaner sentence) and says where `v`'s run comes from. No correction to the mathematics.

**Worked instance `(107,1)`.** `A = 320 = 2^6·5`, `s_0 = 6`, exit `5`, `5 + 1 = 2·3`, so `a_0 = 1` (side door of `state(5) = (1,2)`, whose doors are `3` dead and `5`); `(1,2)` has `A = 8 = 2^3`, `s_1 = 3`, exit `1`. Path: two cascade edges `(107,1) → (1,4) → (7,1)` (branches `6, 4, 2` on door `5`), the door edge `(7,1) → (1,2)`, one cascade edge `(1,2) → (1,1)`. `η = 2`, `λ = 2 + 1 + 1 = 4`. Letters: door `5` carries `(1, 3)` (`m = 1`, `q = 3`, `r = v₂(9 − 1) = 3 = s_1`), door `1` carries `(1,1)`; `λ = ⌊5/2⌋ + ⌊2/2⌋ + ⌊0/2⌋ + 1 = 4`. Confirmed by hand and by the script's first canary.

## Item B — Proposition 18.7.2, derived

**The identity (exact, no ledger).** For `v ≠ (1,1)`, `deg(v) = 1 + D(v) − [top door of v dead]` (Proposition 18.2.3); `deg(1,1) = 1`. Every child of a level-`λ` node is at level `λ + 1` and every level-`(λ+1)` node is the child of exactly one level-`λ` node, so

```text
n_{λ+1} = Σ_{v at level λ} deg(v),   i.e.   n_{λ+1}/n_λ = 1 + (mean D at level λ) − (dead-top fraction at level λ)   for λ ≥ 1.
```

The ratio of consecutive level counts *is* the mean degree of the lower level — an integer identity, checked exactly at every level by the script (`Σ deg = n_{λ+1}` and `Σ deg = n_λ + Σ D − #dead`).

**The value `2`, under the ledger.** If the depths at a level follow the backward depth ledger `P(D = j) = 2·3^{−j}` then the mean depth is `Σ_j j·2·3^{−j} = 2·(1/3)/(1 − 1/3)² = 3/2`; if the top door is dead on half the nodes (Theorem 14.5.1: dead iff `2^D Ω ≡ 1 (mod 3)`, two of the four residue–parity classes) then the mean number of door children is `3/2 − 1/2 = 1` and the mean degree is `2`. Both inputs are measured laws on the comb's levels: the ledger is the measured law of 14.2.4's remark (exact only per window of `3^k` consecutive branches on one door, 14.6.5.2 — a comb level is not such a window), and the `1/2` is a density over residue classes with no uniform measure behind it (14.5.1's own caveat). The proposition is therefore: *given* those two inputs, the level growth is exactly `2`; the census's ratio `2.000` from level `22` (18.5) is the statement that the inputs hold on the levels to three decimals. Measured here per level to level `20`: mean `D`, dead-top fraction, mean degree, level ratio, depth distribution against `2·3^{−j}` — see the verification record.

## Item C — pointers only

Written as one paragraph on the page: along door edges toward the root the next `k` letters are fixed by the door modulo `2^N` (Theorem 14.15.1.5; the digit budget, stage4.md 11.8.7.7 — finite prefixes cheap, unbounded ones the Bridge); along a cascade chain on a fixed door everything is exact (14.10.1's step; the depth sequence `d = 1 + v₃(s − M₃(y))`, 14.2.4, with the exact ternary ledger 14.6.5.2). The seam between them is the door edge seen from the 3-adic side — Item D. Nothing derived.

## Item D — Theorem 18.7.3, derived

**Setting.** A door edge: parent door `y` (odd, `3 ∤ y`), branch `s₀ ∈ {1,2}` (`s₀ = 1` iff `y ≡ 1 (mod 3)`), child `(ω, d)` with `2^{s₀} y + 1 = 3^d ω`, the child's doors `y'_a = 2^{d−a} 3^a ω − 1`, `0 ≤ a ≤ d − 1`. "Same `d`" below means two edges `y ↦ (ω,d)`, `ỹ ↦ (ω̃, d̃)` with `d̃ = d`.

**(1) `d` from `y`.** `v₃(2^{s₀} y + 1) ≥ k` iff `y ≡ −2^{−s₀} (mod 3^k)` — a condition on `y mod 3^k` (ladder.md 15.7.6's congruence). So "`d ≥ k`" is decided by `y mod 3^k`, and `d` itself (`≥ d` and not `≥ d + 1`) by `y mod 3^{d+1}`; equivalently `d = 1 + v₃(s₀ − M₃(y))` (14.2.4). `s₀` is decided by `y mod 3`. Two doors agreeing mod `3^k` with `k ≥ 1` share `s₀`, and if `k ≥ d + 1` they share `d`. Holds as the brief states it. Not decided by `y mod 3^d`: `ỹ = y + 2t·3^d` with `ω + 2^{s₀+1} t ≡ 0 (mod 3)` has `d̃ ≥ d + 1` (the script constructs one at every sampled edge).

**(2)–(3) The exact identity.** For two door edges with the same `s₀` and the same `d`, and any `0 ≤ a < d`,

```text
v₃(y − ỹ) ≥ d,   and   v₃(y'_a − ỹ'_a) = v₃(y − ỹ) − (d − a).
```

*Proof.* `2^{s₀} y + 1` and `2^{s₀} ỹ + 1` are both `≡ 0 (mod 3^d)`, so their difference `2^{s₀}(y − ỹ)` is, and `v₃(y − ỹ) ≥ d`. Then `ω − ω̃ = 2^{s₀}(y − ỹ)/3^d` has `v₃ = v₃(y − ỹ) − d` (`2^{s₀}` a unit), and `y'_a − ỹ'_a = 2^{d−a} 3^a (ω − ω̃)` has `v₃ = v₃(y − ỹ) − d + a`. ∎

Consequences, which are the brief's claims 2 and 3:

- **Top door (`a = 0`).** For `j ≥ 1`: `ỹ ≡ y (mod 3^{j+d})` forces `d̃ = d` (`j + d ≥ d + 1`, by (1)) and then `ỹ'_0 ≡ y'_0 (mod 3^j)`. Sharp: same `d` and `v₃(ỹ − y) = j + d − 1` give `v₃(ỹ'_0 − y'_0) = j − 1 < j`. The "same `d`" hypothesis in the sharpness clause is needed only at `j = 1`, where agreement mod `3^d` does not fix `d` (of the three lifts `y + 2t·3^d`, `t mod 3`, exactly one has `d̃ ≥ d + 1`; the other two have the same `d` and top doors differing mod `3`). So `j` output digits consume `j + d` input digits, and the map from the `(j+d)`-th digit of `y` to the `j`-th digit of `y'_0` (lower digits fixed) is a bijection of `Z/3` — `y'_0 = 2^{d+s₀} 3^{−d} y + (2^d 3^{−d} − 1)` on the admissible class, a unit multiplier. Holds as the brief states it.
- **Side doors (`a ≥ 1`).** `v₃(y'_a + 1) = v₃(2^{d−a} 3^a ω) = a` exactly, so `y'_a ≡ −1 (mod 3^a)` and `≢ −1 (mod 3^{a+1})`: the low `a` digits are fixed by the door index alone, whatever `y`. For `j > a`: `ỹ ≡ y (mod 3^{j−a+d})` forces `d̃ = d` and `ỹ'_a ≡ y'_a (mod 3^j)`; sharp at `3^{j−a+d−1}` with the same `d` (again needed only when `j − a = 1`). **At `j ≤ a`** the residue `y'_a mod 3^j = −1` is constant — a function of `a` and of no digit of `y`; the count `j − a + d` is then a sufficient number of digits (it is `≥ d`, and any same-`d` pair agrees) but not a sharp one, since zero digits suffice. The brief's "derive the exact statement, including what happens at `j ≤ a`" is answered by the identity: it holds at every `j`, and for `j ≤ a` it says `v₃(y'_a − ỹ'_a) ≥ a ≥ j` automatically.

**Identification (what the theorem is).** The child door `y'_a` has stratum `(m, r) = (d − a, s₀)`: `m = v₂(y'_a + 1) = d − a`, and `r = s(state(y'_a)) = s(ω,d) = s₀`; and `G(y'_a) = y` (the exit of the child). So the identity above is Theorem 14.14.4.1 — `v₃(G(y') − G(z')) = v₃(y' − z') + m` on a fixed stratum — read backward along the door edge, with `m = d − a`. Nothing new is computed. The theorem's content is the count in comb coordinates, and the two things the count settles:

- the **precision loss** across a door edge into door `a` of the child is exactly `d − a` digits (`d` to the exact division by `3^d`, `a` back from the factor `3^a` of `y'_a + 1`), and `d − a = m(y'_a)`, the 2-adic entry depth of the door entered — 14.14.6's identification of the stratum's `m` with the step's `m₊`; every door edge costs at least one digit (`a ≤ d − 1`);
- at 14.6's **designated door** (`a = 0` when `d = 1`, `a = d − 1` when `d ≥ 2`; the collapse identity 14.6.1) the loss is exactly **one** digit at every edge, which is the "one digit of precision loss per generation" of 14.6.5's honest assessment; at the **top door** it is `d`, which is 14.13's "exactly `d` digits" (that section's residue system tracked the child through its full residue, i.e. the quotient `ω`, and lost `d`). The two figures on record are the two ends `a = d − 1` and `a = 0` of one count; neither is wrong, and they are not the same count.

**(4) The reading, and what it does not do.** Under the depth ledger (a measured law) the mean loss at the top door is `E[d] = 3/2` digits per door edge. Along a cascade edge the door is unchanged and no digit of it is consumed: the identity holds with any admissible branch `s` in place of `s₀` (same proof, `d = d(y,s)`), so the count from a door `y` to the doors of the node at branch `s` on `y` is `d(y,s) − a` at every branch, and a cascade run only changes which `d` is charged at the next door edge. `M₃` does not propagate: `M₃(y'_a) mod 3^k` is a function of `y'_a mod 3^{k+1}` (14.7.1(a')) and hence of `y mod 3^{k+1+d−a}` — a function of finitely many digits of the parent door because the child door itself is one, which is 14.6.5's affine obstruction with its price written down, not a way around it.

**Boundary cases.**

- `y = 1`: `s₀ = 1`, `2 + 1 = 3`, `d = 1`, `ω = 1` — the child is the root itself, `y'_0 = 1`; the algebra (the collapse map `y ↦ (4y − 1)/3` at `s₀ = 1, d = 1` fixes `1`) describes the excluded self-loop, and no door edge of the comb has parent door `1` (the root has no door child, 18.2.3; door `1`'s higher branches hang by cascade edges).
- `j = 0`: every residue mod `3^0` is `0`; the agreement clause is vacuous and the sharpness clause has no content. `d` itself needs `d + 1` digits (by (1)), so "`j + d` digits" at `j = 0` is one digit short of fixing `d` — the top-door clause is stated for `j ≥ 1`.
- Dead top door: `y'_0 ≡ 0 (mod 3)` iff `2^d ω ≡ 1 (mod 3)` (14.5.1). The identity does not see liveness: `y'_0` is an integer either way, and the clause at `j = 1` says its residue mod `3` — hence whether the child's top door is dead — is a function of `y mod 3^{d+1}` and `s₀`. A dead `y'_0` is not a comb edge (no door child there); the count `d − 0` is then the cost of a door that is not taken.

**Pre-check claims against the derivation.** Claims 1–4 hold as stated. Two things are sharper than the brief: the single exact identity `v₃(y'_a − ỹ'_a) = v₃(y − ỹ) − (d − a)` replaces the two "function of / not a function of" clauses, and the identification with 14.14.4.1 (backward) makes the theorem a dictionary entry rather than a new law. One thing is more careful than the brief: the sharpness clause needs "same `d`" as a hypothesis at `j = 1` (top door) and `j − a = 1` (side doors), since agreement mod `3^d` alone does not fix `d`. And one in-record tension is resolved rather than repeated: 14.6.5 says one digit per generation, 14.13 says `d` digits per step; the brief attributes "one digit" to 14.13. Both figures are instances of `d − a` (designated door, top door).

## Verification record

*(Filled after the run; see below.)*

## For the main session at merge

*(Filled at the end.)*
