# Findings: two loose ends — the tree's language (itinerary.md, under 14.15.2) and the family-frame weak conjecture (open-problems.md 11.14)

Delegated session, branch `tree-language-families`. Supports `briefs/tree-language-families-brief.md`.

## Base SHA and branch

The worktree's HEAD at spawn (`a7543ce`, 2026-09-13) predated the brief: `briefs/tree-language-families-brief.md` did not exist in the worktree at that commit. Checked `git merge-base --is-ancestor a7543ce main`: true (a clean fast-forward, no divergent commits on the worktree branch), and local `main`'s HEAD `a882804` is exactly one commit ahead of `a7543ce` — the brief's own delegation commit. `git checkout -b tree-language-families main` was used rather than a rebase.

**Base SHA: `a882804`** (`briefs: delegation brief for two loose ends from the author's session of 2026-09-13 ...`).

## Item A: the tree's language is the full shift

### The cylinder modulus, taken as stated

Theorem 14.15.1.5 (itinerary.md): for a word `W = ((m_0,r_0),…,(m_{n-1},r_{n-1}))`, `S := Σ_i(m_i+r_i)`, the followers of `W` form **exactly one residue class modulo `2^{S+1}`**. This is one more than the naive guess `2^S` (each letter's own single-stratum cylinder is already `2^{m+r+1}`, Corollary 14.15.1.8, not `2^{m+r}`), so `S+1`, not `S`, is the modulus's exponent; the composed-cylinder induction (Lemma 14.15.1.4) carries the same `+1` through every step. This is taken from the theorem's statement, not derived here — it is already proved on the page.

Two more cited facts, used verbatim below:

- **Lemma 14.15.1.4 (composed level shift).** With `M := Σ_i m_i`, for every integer `t`: `G^n(y_W + 2^{S+1}t) = G^n(y_W) + 2·3^M t` exactly, where `y_W` is any representative of the cylinder.
- **Corollary 14.15.1.6 (completeness).** The cylinder of every word is nonempty.

### Statement

**Lemma 14.15.2.1 (the tree's language is the full shift).** For every finite word `W = ((m_0,r_0),…,(m_{n-1},r_{n-1}))`, `m_i, r_i ≥ 1`, there is a positive odd integer `x` that follows `W` (Definition 14.15.1.2) and whose `T`-orbit reaches `1`.

(For `n = 0` — the empty word — `x = 1` follows it vacuously and reaches `1` trivially; the content is at `n ≥ 1`.)

### Proof

Write `S = Σ_i(m_i+r_i)`, `M = Σ_i m_i` (`M ≥ 1` since `n ≥ 1`, every `m_i ≥ 1`). Let `y_W` be a representative of `W`'s cylinder (Theorem 14.15.1.5; exists by Corollary 14.15.1.6) and `z_0 := G^n(y_W)` — an actual odd positive integer, since `G`'s output is always odd (itinerary.md 14.15.1.1's remark, citing reverse.md 14.14.7.1).

**Step 1 (the affine image of the cylinder, mod `3^M`).** By Lemma 14.15.1.4, as `t` ranges over all integers, `G^n(y_W + 2^{S+1}t)` ranges over `{z_0 + 2·3^M t : t ∈ Z}`. Since `2` and `3^M` are coprime, this set is exactly the residue class `z_0 (mod 2·3^M)`. Because `z_0` is odd, this class already consists entirely of odd numbers; for any odd target `c`, `c ≡ z_0 (mod 2·3^M)` iff `c ≡ z_0 (mod 3^M)` (the mod-`2` congruence is automatic between two odd numbers, and `2, 3^M` are coprime so the two moduli combine by CRT). So: **the image of the cylinder under `G^n` is exactly the set of odd integers `≡ z_0 (mod 3^M)`, one integer for each `t ∈ Z`.**

**Step 2 (the covering fact, re-derived from a lemma already on file — not the brief's original guess).** The brief's provenance ascribes the covering step to "`4` generates `1+3Z_3` modulo `3^{k+1}`," checked only empirically in the pre-check (`k ≤ 6`). Here it is derived from reverse.md **Lemma 14.2.1** (already proved, lifting-the-exponent): for even `t ≥ 2`, `v_3(2^t − 1) = 1 + v_3(t)`. Put `t = 2i` (`i ≥ 1`): `4^i = 2^{2i}`, so

```text
v_3(4^i − 1) = v_3(2^{2i} − 1) = 1 + v_3(2i) = 1 + v_3(i)      (v_3(2) = 0).
```

Consequently, for `k ≥ 1`: `4^i ≡ 1 (mod 3^{k+1})` iff `v_3(4^i−1) ≥ k+1` iff `v_3(i) ≥ k` iff `3^k | i`. So the multiplicative order of `4` modulo `3^{k+1}` is exactly `3^k` (it divides `3^k` since `4^{3^k}≡1`, and no smaller power of `3` works, by the displayed equivalence at `i = 3^{k-1}`, where `v_3(i)=k-1<k`). Hence `{4^i mod 3^{k+1} : i = 0,…,3^k−1}` are `3^k` **distinct** residues; they form a subgroup of `(Z/3^{k+1}Z)^×` (cyclic of order `2·3^k`) of order `3^k`, hence *the* unique subgroup of that order — which is exactly the set of units `≡ 1 (mod 3)` (index `2`, since reduction mod `3` is the group's unique order-`2` quotient). Since `4 ≡ 1 (mod 3)`, every `4^i` lies in this set, confirming membership; the order count shows it is hit bijectively.

Now consider `f(i) := (4^i − 1)/3`. As `i` ranges over `0,…,3^k−1`, `4^i mod 3^{k+1}` ranges bijectively over the `3^k` multiples-of-`1`-mod-`3` residues, i.e. `4^i − 1 mod 3^{k+1}` ranges bijectively over the `3^k` multiples of `3` in `[0, 3^{k+1})`, i.e. `{3j : j = 0,…,3^k−1}`, each exactly once; dividing by `3`, `f(i) mod 3^k` ranges bijectively over `{0,…,3^k−1}` — **`f` is a bijection `Z/3^kZ → Z/3^kZ`, of period exactly `3^k` in `i`.**

(`f(0) = 0` is not a positive odd integer — excluded below by using `i ≥ 1` in the same residue class, available since the period is `3^k` and `k ≥ 1` gives more than one representative.)

**Step 3 (the witness).** Take `k = M`. By Step 2 there is a unique `i_0 ∈ {0,…,3^M−1}` with `f(i_0) ≡ z_0 (mod 3^M)`; since `f` has period `3^M`, every `i ≡ i_0 (mod 3^M)`, `i ≥ 1`, satisfies the same congruence, and `f(i) = (4^i−1)/3 → ∞` as `i → ∞` along this progression. Choose such an `i` with `f(i) ≥ z_0` (possible: take `i = i_0` if `i_0 ≥ 1` and `f(i_0) ≥ z_0`, else `i = i_0 + 3^M`, else keep adding `3^M`). Set `F := (4^i−1)/3`, an odd positive integer (shown above) with `F ≡ z_0 (mod 3^M)` and `F ≥ z_0`.

By Step 1, `F` is in the image of the cylinder under `G^n`: there is an integer `t ≥ 0` with `z_0 + 2·3^M t = F`, namely `t = (F − z_0)/(2·3^M)` — an integer because `F ≡ z_0 (mod 3^M)` (the `3^M`-part) and `F, z_0` are both odd so `F − z_0` is even (the `2`-part), and `t ≥ 0` because `F ≥ z_0`. Set

```text
x := y_W + 2^{S+1} t.
```

`x` is a positive odd integer (both `y_W` and the shift are; `t ≥ 0`), it follows `W` (it is in the cylinder by construction), and `G^n(x) = z_0 + 2·3^M t = F = (4^i−1)/3` (Lemma 14.15.1.4, at this specific `t`).

**Step 4 (`F` reaches `1`, hence so does `x`).** `(4^i−1)/3` reaches `1` under `T`: `3·F + 1 = 4^i − 1 + 1 = 4^i`, so `T(F) = 4^i/2^{v_2(4^i)} = 4^i/2^{2i} = 1` — one `T`-step, exactly, for every `i ≥ 1`. So `F`'s `T`-orbit reaches `1`.

`x`'s `T`-orbit reaches `1` too: `G^n(x) = F` and `G(y) = T^{m(y)}(y)` (reverse.md 14.14.7.1, the block-map identity — `G` is a subsequence of iterated `T`), so `F` lies on `x`'s `T`-orbit, and "reaches `1`" is closed under passing to a later point of the same orbit. (Equivalently and more structurally: `x`'s `T`-orbit reaches `1` iff the `F`-orbit — spine.md's reduced map — of `state(x)` reaches `(1,1)` (Theorem 9.8.3, `R(x) = state(x)`); `G` semiconjugates to `F` via `state` (reverse.md Theorem 14.14.3.2(1)), so `state(G^n(x)) = F^n(state(x))`; `state(F) = state(1) = (1,1)`, and since the fiber of `(1,1)` is exactly `{1}` (Proposition 9.8.1), `G^n(x) = 1` would follow *if* the orbit revisited the trivial state through this particular chain — the direct argument above (F lies on x's actual T-orbit) is what is used; this remark records that "the tree from 1" can equally be read in door/`G` coordinates, not a second proof.) ∎

**No boundary case was needed.** Both steps the brief flagged as candidates for a boundary case resolved cleanly: step (ii)'s parity issue (matching mod `2·3^M` vs mod `3^M`) is handled once and for all by both `F` and `z_0` being odd (Step 1); the sign of `t` is handled by choosing `i` in its residue class large enough that `F ≥ z_0` (Step 3) — always possible since `f`'s progression in `i` is unbounded. The brief's own pre-check guess `N = Σ(m_i+r_i)` for the modulus is confirmed too small; the correct exponent, `S+1`, is Theorem 14.15.1.5's own statement, used as such throughout.

### Grade, restated for the page

A lemma about the finite level; it moves no front. Content: local statements in letter language are provable because cylinders are fat (arithmetic progressions) — 14.15.2's full-shift calibration made concrete inside the tree from `1` — and this is the same fact the digit budget (stage4.md 11.8.7.7) reads as a limitation: a *finite* window of letters is always realizable, cheaply, inside the tree; it is the *unbounded* word that the budget says no bounded window can decide.

## Item B: the family-frame weak conjecture and where it lands

### Setup, from the record

A **family** is a core `ω` together with all its depths, the states `(ω,d)`, `d ≥ 1`; its integer members are `2^m 3^a ω − 1`, `m ≥ 1`, `a ≥ 0` — the doors of `(ω, m+a)` (reverse.md 14.1.1's representative family, `y_a = 2^{D-a}3^aΩ-1` at `Ω=ω`, `D=m+a`, `a`-th representative with `m = D-a`). Write `e(ω,d) := x_exit(ω,d) = A(ω,d)/2^{s(ω,d)}`, `A(ω,d) = 3^dω-1`, `s(ω,d)=v_2(A(ω,d))` (spine.md §3.7, §9.8; ladder.md's own notation).

**W.** For every core `ω`, some depth `d ≥ 1` has `(ω,d)` reaching `(1,1)` under `F`.

**core(x)**, for a positive odd integer `x`: write `x+1 = 2^m 3^a Ω` (`3 ∤ Ω`); `core(x) := Ω`. This is exactly `state(x)`'s first component (reverse.md 14.6.5.1), and — since `x` is itself the `a`-th representative of `state(x)` — `state(x) = (core(x), m+a)` with `x = 2^m 3^a·core(x) − 1`.

**tree(1)** := the set of positive odd integers whose `T`-orbit reaches `1` (reverse.md §14.4's "tree from `1`"; equivalently, by Theorem 9.8.3 and `R = state`, the set of `x` with `F`-orbit of `state(x)` reaching `(1,1)`).

### The three readings, proved equivalent

**(a)** the exit sequence `e(ω,d)`, `d ≥ 1`, contains a member of `tree(1)`.
**(b)** the backward tree from `(1,1)` (states whose `F`-orbit reaches `(1,1)`) visits every core at some depth.
**(c)** `{core(x) : x ∈ tree(1)}` = every integer coprime to `6` (every odd core).

**Lemma B.1 (the one-step bridge).** For a core `ω` and depth `d ≥ 1`: `(ω,d)` reaches `(1,1)` under `F` **iff** `e(ω,d) ∈ tree(1)`.

*Proof.* `F(ω,d) = R(e(ω,d))` by definition of `F` (spine.md §3.7: `F(ω,d) = R(x_exit(ω,d))`), and `R = state` (spine.md's `R` and reverse.md's `state` are the same projection, both `R(u,m) = (ω,d)` for `u=3^aω`; `state` is `14.6.5.1`'s name for the identical map). So the `F`-orbit of `(ω,d)` from step `1` on is exactly the `F`-orbit of `state(e(ω,d))`, and by Theorem 9.8.3 (applied to the representative `e(ω,d)`, whose own `R`-image is `state(e(ω,d))`), `e(ω,d)`'s `T`-orbit reaches `1` iff the `F`-orbit of `state(e(ω,d))` reaches `(1,1)`. So: `(ω,d)` reaches `(1,1)` at step `≥ 1` iff `e(ω,d) ∈ tree(1)`. (Step `0`, `(ω,d) = (1,1)` itself, forces `ω=1,d=1`, `e(1,1) = A(1,1)/2^{s(1,1)} = 2/2 = 1 ∈ tree(1)` trivially — the same conclusion.) ∎

**(a) ⟺ W.** Immediate from Lemma B.1: "`(ω,d)` reaches `(1,1)` for some `d`" (`W`, at a fixed `ω`) is literally "`e(ω,d) ∈ tree(1)` for some `d`" (reading (a)), for every `ω`.

**(a) ⟺ (b).** By definition, the backward tree from `(1,1)` is `{(ω,d) : F-orbit of (ω,d) reaches (1,1)}` (reverse.md §14.4's own construction, expanding via `F^{-1}` from `(1,1)`). "Visits every core at some depth" is "for every `ω`, some `(ω,d)` is in this set" — exactly `W`, hence exactly (a) by the previous paragraph.

**(a)/(b) ⟺ (c).** ⟸: for a given `ω`, take the `a=0` representative at depth `d`, `x = 2^dω − 1`; then `state(x) = (ω,d)` exactly (`x+1=2^dω`, `v_2=d` since `ω` odd, `v_3((x+1)/2^d) = v_3(ω) = 0`), so `core(x) = ω`. If `core(x') = ω` for some `x' ∈ tree(1)` (reading (c)'s membership for `ω`), set `d` to the depth of `state(x')` — `state(x') = (ω,d)` by definition of `core`, and `x'`'s `T`-orbit reaches `1`, so by Theorem 9.8.3 the `F`-orbit of `state(x') = (ω,d)` reaches `(1,1)` — `W` holds at `ω` with this `d`. ⟹: conversely, if `(ω,d)` reaches `(1,1)` for some `d`, the representative `x = 2^dω-1` above has `state(x)=(ω,d)`, so by Theorem 9.8.3 `x ∈ tree(1)`, and `core(x)=ω` — `ω` is realized in reading (c)'s set. So the set `{core(x) : x ∈ tree(1)}` equals `{ω : W holds at ω}` exactly, and (c) (this set is every odd integer) is literally `W` for every `ω` — reading (c) restated.

All three readings, and `W` itself, are the same statement under these translations; nothing beyond Theorem 9.8.3 (already proved) and the definitions was needed.

### The two regimes under the ladder

Throughout, `e(ω,d) = x_exit(ω,d)`; ladder.md's Theorem 15.1.1 (already proved): `s(ω,d)=1 ⟹ e(ω,d+1)=T(e(ω,d))`; `s(ω,d)≥2 ⟹ e(ω,d+1) = 3·2^{s-1}e(ω,d)+1`, `s(ω,d+1)=1`.

**Regime 1: cores `ω ≡ 5, 7 (mod 8)` — no anchor, every spike has `s = 2`.**

By stage1.md **Proposition 11.8.1.3.1** (already proved, cited verbatim, not re-derived): for `ω ≡ 5 (mod 8)`, `s(ω,d) = 1` for odd `d`, `s(ω,d) = 2` for even `d`; for `ω ≡ 7 (mod 8)`, `s(ω,d) = 2` for odd `d`, `s(ω,d) = 1` for even `d`. In both cases `s(ω,d) ∈ {1,2}` **for every `d`, unconditionally** — this is the proposition's own exact classification, not a sampled absence of `s > 2`; these two residue classes never reach the lifting branch (11.8.1.5 restricts the lifting branch to `ω ≡ 1,3 (mod 8)` only).

**Lemma B.2 (the depth-two recurrence).** For `ω ≡ 5` or `7 (mod 8)`, at every depth `d` with `s(ω,d) = 2` (a "spike" depth):

```text
e(ω, d+2) = T(6·e(ω,d) + 1).
```

*Proof.* At the spike depth `d`, `s(ω,d)=2 ≥ 2`, so Theorem 15.1.1 gives `e(ω,d+1) = 3·2^{2-1}e(ω,d)+1 = 6·e(ω,d)+1`, and `s(ω,d+1)=1`. Depths `d` and `d+1` have opposite `s`-values on these classes (Proposition 11.8.1.3.1: `s` alternates exactly with the parity of `d` on each class), so `s(ω,d+1)=1` is consistent (it must be `1`, matching the theorem's own output) and Theorem 15.1.1 applies again at `d+1`: `e(ω,d+2) = T(e(ω,d+1)) = T(6·e(ω,d)+1)`. ∎

So on these classes `W` says: for the explicit sequence `e(ω,1), e(ω,3), e(ω,5), …` **or** `e(ω,2), e(ω,4), …` (whichever parity is the spike parity for the given residue class), generated by `d ↦ T(6d+1)`-style growth (growing by a factor of about `6` every two depths before the `T`-step's halving, roughly `×4.5` net, matching the brief's estimate), some term lies in `tree(1)`.

**Regime 2: lifting classes `ω ≡ 1, 3 (mod 8)` — kick heights `s ≥ 3`, and the `4X+1` identity.**

For a kick of height `s ≥ 2` at exit `e`, Theorem 15.1.1 gives the kicked exit `3·2^{s-1}e+1`. For `s ≥ 3`, write `3·2^{s-1}e = 4·(3·2^{s-3}e) = 4X`, `X := 3·2^{s-3}e` (an integer since `s-3 ≥ 0`), so the kicked exit is `4X+1`.

**The identity, general `X`.** For every positive integer `X` (odd or even), define `Θ(X) := (3X+1)/2^{v_2(3X+1)}` — the same formula as `T`, extended off the odd integers (`Θ = T` whenever `X` is odd). Then

```text
Θ(4X+1) = Θ(X)      for every positive integer X.
```

*Proof.* `3(4X+1)+1 = 12X+4 = 4(3X+1)`, so `v_2(3(4X+1)+1) = 2 + v_2(3X+1)` and `Θ(4X+1) = 4(3X+1)/2^{2+v_2(3X+1)} = (3X+1)/2^{v_2(3X+1)} = Θ(X)`. (`4X+1` is odd regardless of `X`'s parity, so `Θ(4X+1) = T(4X+1)` always — this half needs no extension.) ∎

**Correction to the brief's provenance.** The provenance states this "makes its orbit merge at once with the orbit of `X`, hence with the orbit of `3e`" **for every `s ≥ 3`**, citing `X = 3·2^{s-3}e`. The first clause is exact and needs no correction: `Θ(4X+1) = Θ(X)` literally means the two `Θ`-sequences starting one step later coincide term for term, for *every* `X`, by the identity above — an immediate, unconditional merge. The second clause — identifying "the orbit of `X`" with "the orbit of `3e`" — is **only correct at `s = 3`**, and is wrong as stated for `s ≥ 4`; re-derived and corrected here, not merely flagged.

`X = 3·2^{s-3}e` is **odd exactly when `s = 3`** (`X = 3e`, `e` odd, `3` odd) and **even for every `s ≥ 4`** (`v_2(X) = s-3 ≥ 1`).

- **`s = 3`:** `X = 3e` is odd, so `Θ(X) = T(X) = T(3e)` in the ordinary (odd-to-odd) sense, and the kicked exit's `T`-orbit, from its second term on, *is* the `T`-orbit of `3e` verbatim. The brief's claim holds exactly, as stated, at this one kick height.
- **`s ≥ 4`:** `X` is even, so `Θ(X)` is *not* `T` of anything on the classical odd-to-odd orbit of `X`'s own odd part. Computing directly: `3X = 9·2^{s-3}e`, which is even (`s-3≥1`), so `3X+1` is already odd (`v_2(3X+1)=0`), giving the closed form

```text
Θ(X) = 3X + 1 = 9·2^{s-3}e + 1      (s ≥ 4, exact, no further stripping of 2s).
```

  This is a specific odd number, generally *different* from any early term of `3e`'s own `T`-orbit. **Explicit counter-instance** (`e=1, s=4`): `X = 3·2^1·1 = 6` (even); kicked exit `= 3·2^3·1+1 = 25`; `Θ(6) = 3·6+1 = 19` — matches `T(25)`, computed directly: `3·25+1=76=4·19`, `T(25)=19`. But `T(3e) = T(3) = (10)/2 = 5`, and `19 ≠ 5`: the kicked exit's orbit does **not** land on `3e`'s orbit at the next step. (It merges with `3e = 3`'s orbit eventually — `T(19)=29`, `T(29)=11`, `T(11)=17`, `T(17)=13`, `T(13)=5` — but seven steps later, generically, not "at once.")

**Corrected statement.** For a kick of height `s`, the kicked exit's `T`-orbit reduces, by one exact step, to the `T`-orbit (extended by `Θ` when necessary) of `X = 3·2^{s-3}e`. **Only at `s=3` is this literally the orbit of `3e`**; the reduction to "does the orbit of `e` merge with the orbit of `3e`" that the brief's later "wall" paragraph builds on is exact only for kicks of height exactly `3`. For `s ≥ 4`, the one-step-reduced target is the specific value `9·2^{s-3}e+1`, and whether *that* value's orbit reaches `tree(1)` (or merges with `e`'s or `3e`'s orbit) is a further instance of the same *kind* of open question — an explicit value versus a dense set — not an instance already reduced to `e` vs. `3e` in closed form. This does not change the calibration the brief draws (regime 2's tree membership is, at every kick height, exactly an "explicit value must land in a dense set" question of the un-provable shape the "wall" names); it only narrows which specific pair of orbits that question is about, and only the `s=3` case reduces to the `e` vs. `3e` pair named in the record.

### The wall, restated (no change to its content)

"Do the orbits of `x` and `3x` merge?" is the question regime 2 reduces to *at `s=3`* (and a family of closely related "does this specific value's orbit meet the trivial one" questions at higher `s`); it would follow from the family-frame conjecture and is open on its own — an explicit thin sequence meeting a dense set, with no technique on file for that shape. This calibration is unchanged by the correction above; it only refines *which* explicit-value-vs-dense-set question is in play at each kick height.

### Flat note: the trivial family's own exits

**Claim.** `e(1,d)` is the odd part of `3^d − 1`.

*Proof.* Directly from the definition: `A(1,d) = 3^d·1 − 1 = 3^d − 1`, `s(1,d) = v_2(A(1,d)) = v_2(3^d-1)`, `e(1,d) = A(1,d)/2^{s(1,d)} = (3^d-1)/2^{v_2(3^d-1)}` — the odd part of `3^d-1`, by definition of "odd part," nothing to derive beyond unwinding `e`'s own definition. ∎

Values `d=1..7`: `1, 1, 13, 5, 121, 91, 1093` — matching `3^d-1 = 2, 8, 26, 80, 242, 728, 2186` with odd parts `1, 1, 13, 5, 121, 91, 1093` exactly (verified below). Whether every `e(1,d)` reaches `1` is `W` restricted to `ω=1` — open (it is not the trivial cycle's own statement, which is about `(1,1)` alone; the deeper members of the trivial *family*, `(1,d)` for `d>1`, are ordinary open states like any other, and nothing on file addresses them beyond the generic regime-1/2 dichotomy above, since `1 ≡ 1 (mod 8)` is a *lifting* class, not a no-anchor one).

## Grade, restated for the page (item B)

An open entry phrased checkably, in the 11.13 style; no front moves; the fiber-versus-orbit bridge of stage2.md 11.8.5.6 is its name in the record, and 11.14 is that bridge's weakest global form.

**Stopping-rule compliance.** No cycle search of any kind ran anywhere below; the `x` vs `3x` measurement is a fresh orbit-merge experiment (identities and measurements on orbits, per the brief), not a period search; the correction to regime 2 is a re-derivation from the cited identity and one hand-checked counter-instance, not a computational search for a mechanism.

## Verification record

`experiments/tree_language_families.py`, fresh code (imports nothing from any existing script: `itinerary_coding.py`, `door_seam.py`, `ladder.py`, `ladder_afterlife.py`, `ladder_family_graph.py`, `top_door_lineage.py` — the stratum/`G`/`T`/`state`/`F` primitives, the covering table, and the cylinder-construction algorithm are all reimplemented from the wiki's own definitions). Exact Python-integer arithmetic at every pass/fail decision; no floats anywhere in a check (the one printed ratio, `1212/1300 ≈ 0.932`, is reporting only, not a pass/fail test). Canaries first: `(1,1)`; the hand-checked word `((1,1))` (cylinder `y ≡ 1 (mod 8)`, five representatives in, six out); `(4^i-1)/3` reaching `1` for `i=1..5` (`i=1` gives `F=1` itself, `0` steps; `i≥2` gives `1` step — both cases checked with the correct expected step count). Seed `20260913` throughout.

Sections and counts:
- Item A(a), the covering: `k=1..7`, bijectivity, exactly-once, periodicity (`20` sampled `i` per `k`), and the order fact `v_3(4^i-1)=1+v_3(i)` (`i` up to `min(3^k,200)`).
- Item A(b), cylinder structure: `25` small words exhaustively (length `1..2`, letters `1..3`, full modulus scan), `250` random words (length `≤4`, letters `≤3`) with positive and negative controls.
- Item A(b), the constructive witness: `150` random words (length `≤3`, letters `≤2`, so `M ≤ 6` and `(4^i-1)/3` stays a manageable integer), each witness verified to follow `W`, to match the affine construction by independent `n`-fold `G`-simulation, and to reach `1` by direct `T`-simulation.
- Item B(c), the `s=2` classes: `200` random cores (`ω ≡ 5` or `7 mod 8`, up to `~8·10^6`), depths `1..60`: every `s` in `{1,2}` (`12,000` checks), the depth-two recurrence at every spike depth (`5,800` checks).
- Item B(d), the `4X+1` identity: `3,000` random `X` (general algebraic identity), `3,000` random `(e,s)` kick instances (`s=3..12`) confirming the `s=3` exact match and the `s≥4` closed form, plus the explicit `(e,s)=(1,4)` counter-instance (`T(25)=19 ≠ T(3)=5`, merging at `5` six `T`-steps later).
- Item B(e), the wall measurement: `1,300` valid trials (odd, coprime to `3`, `x < 2·10^6`), `400`-step horizon.
- Item B(f), the trivial family's exits: `d=1..29`, matching the odd-part formula exactly, `d=1..7` matching the stated sequence.

**TOTAL: checks=35530, failures=0** (run time 0.30s). Output committed verbatim at `experiments/tree_language_families_output.txt` (modulo the wall-clock `time=` line, per the standing convention).

**Single reproducing command:**

```
python experiments/tree_language_families.py
```

No phases, no flags.

`experiments/encoding_scan.py`: **RESULT: CLEAN** (re-run after every wiki edit, and again before the final commit).

## For the main session at merge

- **No branch-boundary seams expected.** This branch was cut from `a882804` (itself the sole commit ahead of the `top-door-lineage`/`ladder-afterlife`/`ladder-family-graph` arcs' own base `4ccfc09`, per HANDOFF and those branches' findings), and touches only `itinerary.md`, `open-problems.md`, and `stage2.md` — none of which those three branches touched (they touched `reverse.md`, `cycles.md`, `TOUR.md`, `open-problems.md` 11.13, and `ladder.md`). The only page in common with any of them is `open-problems.md`, and the edits are at disjoint entries (`11.13` there, `11.14` here) added in sequence — no numbering collision, since `11.14` was written after `11.13` was already on `main` at this branch's base.
- **`ladder.md` deliberately untouched.** The brief's conditional edit ("only if the `s=2` recurrence is not derivable in one line from `15.1.1` as stated") did not trigger: Lemma B.2 in the findings above derives `e(ω,d+2)=T(6·e(ω,d)+1)` in two direct applications of the already-proved Theorem `15.1.1`, using only the already-proved Proposition `11.8.1.3.1` (stage1.md) to know which depths are spikes. No new fact was needed on `ladder.md`.
- **`index.md` deliberately untouched**, matching the `top-door-lineage` branch's own precedent: the resolver lists `open-problems.md`'s page-range ownership only (`§11.1–11.7 → open-problems.md`), with `11.8`/`11.10` as the only individually listed post-`11.7` entries; `11.11`, `11.12`, and `11.13` were none of them added as individual resolver lines, so `11.14` follows the same precedent.
- **`TOUR.md`, `symbols.md` untouched**, per the brief: no new term, no new symbol. "Family" is already used at ladder.md `15.7`; `Θ` (the `T`-formula extended off the odd integers) is introduced only in prose, inside the findings and the open-problems.md entry, as a one-off notational convenience for the derivation — not registered, not reused elsewhere on the page, and not needed again once the corrected regime-2 statement is on file.
- **The correction to regime 2 is the one item worth a second look at merge.** Re-derive independently: `Θ(4X+1)=Θ(X)` from `3(4X+1)+1=4(3X+1)`, for every positive integer `X` (no parity hypothesis needed on that half); then check `X=3·2^{s-3}e` is odd only at `s=3`. The counter-instance (`e=1,s=4`: kicked exit `25`, `T(25)=19`, `T(3)=5`, `19≠5`, merging at `5` after six further `T`-steps from `19`) is small enough to re-check by hand.
- **Nothing here depends on, or was checked against, any of the three parallel ladder/top-door branches' content** — this branch's own math (Item A) and reduction (Item B) use only already-published theorems (`9.8.1`–`9.8.4`, `14.15.1.4`–`14.15.1.6`, `14.2.1`, `15.1.1`, `11.8.1.3.1`, `11.8.1.5`) that predate all four of the 2026-09-13 delegations.

## Files changed

- `experiments/tree_language_families.py` (new)
- `experiments/tree_language_families_output.txt` (new)
- `itinerary.md` (new Lemma 14.15.2.1 and proof and verification line; one clause in the three-notion separation remark; front matter `updated`; Current-state paragraph gains one clause)
- `open-problems.md` (new entry 11.14; front matter `scope`, `updated`)
- `stage2.md` (one pointer sentence at 11.8.5.6; front matter `updated`)
- `briefs/tree-language-families-findings.md` (this file)

No other files touched. `HANDOFF.md`, `README.md`, `cycles.md`, `reverse.md`, `aeh.md`, `TOUR.md`, `symbols.md`, `publication.md`, `paper/`, `sources/`, `index.md`, `ladder.md` are all untouched, per the brief's rules.
