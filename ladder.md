---
status: CLOSED as a local law (15.1–15.2, verified, zero failures); the author's divergence question answered exactly (15.3)
scope: new section 15 (post-monolith)
updated: 2026-09-13
source: the author's question "where do (ω,d) and (ω,d+1) diverge?"; builds on §3 anchor machinery
---

> **Current state.** The vertical structure of the state space, solved. Adjacent depths at a fixed core obey `A(ω,d+1) = 3·A(ω,d) + 2`, which forces an exact dichotomy (15.1): off-spike (`s = 1`), the deeper state's exit is *one Collatz step ahead* of the shallower one's — same integer orbit, offset by one step, divergence never; at a spike (`s ≥ 2`), the exits split by the explicit kick `e ↦ 3·2^(s−1)e + 1` — divergence immediate and total. Since `s = 1` occupies alternating depths, every column of the anchor field is a perfect braid of single Collatz steps and affine kicks (15.2). The spikes — the anchor's digit matches — are exactly the divergence points of the depth ladder (15.3). A hoped-for stronger form (columns encoding long orbit stretches) is false and recorded as such. At the valuation level the ladder is now identified as the third face of stage3's target-shift mechanism (15.5): depth steps slide the valuation target along `c = 3^(−k)`, even steps are anchor-coordinate translations, and the alternation follows ultrametrically — the integer-level kick is not recovered by that frame.

# 15. The Depth Ladder

What relates `(ω, d)` and `(ω, d+1)`? They share every digit of the core — identical anchors `M(ω)` — and differ by one unit of displacement. The answer turns out to be a commutation law between the vertical ladder and the Collatz flow itself.

## 15.1. The ladder law

Write `e(ω,d) = x_exit(ω,d)` and `s(ω,d)` for the exit data. The elementary identity

```text
A(ω, d+1) = 3^(d+1)·ω − 1 = 3·A(ω,d) + 2
```

forces:

**Theorem 15.1.1 (ladder dichotomy).** For every valid state,

```text
s(ω,d) = 1   ⟹   e(ω, d+1) = T( e(ω,d) ),
s(ω,d) ≥ 2   ⟹   e(ω, d+1) = 3·2^(s−1)·e(ω,d) + 1,   and   s(ω,d+1) = 1.
```

**Proof.** Let `s = s(ω,d)`, `e = e(ω,d)`, so `A = 2^s e`. Then `A' = 3·2^s e + 2`. If `s = 1`: `A' = 2(3e + 1)`, so `e' = (3e+1)/2^(v₂(3e+1)) = T(e)` with `s' = 1 + v₂(3e+1) − ...` absorbing exactly the halvings of the Collatz step. If `s ≥ 2`: `A' = 2·(3·2^(s−1)e + 1)` with the bracket odd, so `s' = 1` and `e' = 3·2^(s−1)e + 1`. ∎

**Verification.** `30,000` random states: `9,906` off-spike cases and `10,085` spike cases, zero failures in both branches. Code: `experiments/ladder.py`.

## 15.2. The braid

By the first-layer classification, `s = 1` occurs at *alternating* depths in every column (for each `ω mod 8`, exactly one parity of `d` gives `s = 1`; the other gives `s = 2` or the lifting shells). Consequently a column of the anchor field, read upward, is a strict alternation:

```text
Collatz step,  kick,  Collatz step,  kick,  …
```

with the kick's magnitude `3·2^(s−1)e + 1` determined by the spike height `s` — that is, by the anchor digits. Consecutive genuine Collatz steps never occur vertically. **Recorded overreach:** the stronger hope that columns encode long orbit stretches was tested and is false — the run-length histogram of consecutive `T`-steps is supported entirely on length `1` (`39,324` runs) apart from boundary zeros. The braid, not the orbit, is the vertical structure.

## 15.3. The divergence answer

The author's question — *where is the divergence point between `(ω,d)` and `(ω,d+1)`?* — has an exact answer:

* If `s(ω,d) = 1` (the off-spike case, every second depth): **nowhere**. The two states' exit trajectories are the *same integer orbit*, offset by one Collatz step; their futures are identical from the first block onward.
* If `s(ω,d) ≥ 2` (a spike): **immediately**. The kick `e ↦ 3·2^(s−1)e + 1` throws the deeper exit onto a different (generically unrelated) orbit, with separation growing with the spike height.

So the spikes of the anchor field — the depths where `d` matches the 2-adic digits of `M(ω)` — are precisely the tear-lines of the depth ladder: below current, adjacent depths flow together; at an anchor match, they rip apart by an explicit affine map. In the anchor-field explorer this is visible directly: within a column, each cool cell shares its future with the cell above it; each hot cell is a divergence point.

## 15.4. Standing

This closes the vertical question as a local law. Open connections worth recording, not yet pursued: the ladder gives a second exact mechanism relating *different states with the same anchor* (at the valuation level identified in `15.5` as the target-shift lemma read in the depth variable), which is raw material for the fiber-to-orbit bridge (stage2.md `11.8.5.6`; consolidated as the Bridge, bridge.md §16) — the bridge asks how anchors vary along orbits, and the ladder shows how orbits vary along an anchor; whether the two exact laws compose into anything is unexamined. The mirror front has its dual ladder: reverse.md `14.10` relates predecessors at adjacent branches `s` and `s+2` at a fixed door (step size `2` forced by the parity constraint), with an exact dichotomy gated by the `3`-adic anchor's first digit — the mirror of `15.1`'s tear-line.

## 15.5. The ladder as a face of the target-shift lemma

Theorem `15.1.1` was proved by one line of integer algebra, and that proof remains the proof of record. This subsection records a second reading, at the valuation level only: the depth ladder is the target-shift mechanism of stage3.md `11.8.6.3` read in the depth variable. Neither page cited the other before this identification; the two mechanisms are one.

**Lemma 15.5.1 (depth steps are target shifts).** For every valid state `(ω, d)` and every `k >= 1`,

```text
s(ω, d+k) = v_2(3^d ω - 3^(-k)),
```

where `3^(-k)` is the `2`-adic inverse of `3^k`.

**Proof.** `3^(d+k) ω - 1 = 3^k · (3^d ω - 3^(-k))`, and `3^k` is a `2`-adic unit. ∎

Climbing the ladder at a fixed core is therefore sliding the valuation target along the family `c = 3^(-k)`: the whole column above `(ω, d)` is the valuation of the single `2`-adic number `3^d ω` against a moving target, in exactly the sense of stage3's shifted-target problem `v_2(3^d ω - c)`.

**Proposition 15.5.2 (even steps are anchor translations).** Let `ω ≡ 1 (mod 8)`, `d = 2n`, and `k = 2j` with `j >= 1`. Then the target `9^(-j)` lies in `1 + 8 Z_2` with `N(9^(-j)) = j`, and Lemma `11.8.6.3.1` applies:

```text
s(ω, d + 2j) = v_2(3^d ω - 9^(-j)) = 3 + v_2(n + j - N(ω)).
```

The even steps of the ladder are pure translations `n ↦ n + j` in the anchor coordinate — literal instances of the target-shift lemma — and the right side is nothing other than the `c = 1` global law of `11.8.4.1` re-indexed at depth `d + 2j`.

**Proof.** `9 ≡ 1 (mod 8)`, so `9^(-j) ∈ 1 + 8 Z_2`; and `9^(N(c)) = c^(-1) = 9^j` forces `N(9^(-j)) = j`, since `z ↦ 9^z` is injective on `Z_2` (apply `log` and divide by `log 9 ≠ 0`, Lemma `11.8.3.6.5`). Lemma `11.8.6.3.1` with `c = 9^(-j)` gives the display, provided `n + j - N(ω) ≠ 0`; equality would force `9^(n+j) ω = 1` in `Z_2` with `9^(n+j) ω` a positive integer `>= 9`, and distinct integers remain distinct in `Z_2`. The identification with the `c = 1` law is Lemma `15.5.1` read backwards: `v_2(3^d ω - 9^(-j)) = s(ω, 2(n+j)) = 3 + v_2((n+j) - N(ω))`. ∎

Component bookkeeping: the proposition holds verbatim on the odd component (`ω ≡ 3 (mod 8)`, `d = 2n + 1`) through the companion parameter — `3^(d+2j) ω = 9^(n+j) · (3ω)` by Proposition `11.8.1.6.2`, so the same translation law reads `s(ω, d + 2j) = 3 + v_2(n + j - N(3ω))`. An *odd* shift `k` flips the residue-parity component (the same `3ω` bookkeeping moves the parameter between `ω` and its companion), landing the state on whichever class the first-layer table assigns; the anchor lemma governs the two lifting classes, and the `s = 1` and `s = 2` classes are the shallow targets of Theorem `15.5.3` and of stage3's `11.8.6.3.5`.

**Theorem 15.5.3 (ultrametric reading of the dichotomy).** The adjacent targets `1` and `3^(-1)` satisfy

```text
v_2(1 - 3^(-1)) = v_2(2 · 3^(-1)) = 1.
```

Write `X = 3^d ω`, `s = s(ω,d) = v_2(X - 1)`, `e = e(ω,d)`. By Lemma `15.5.1` with `k = 1`, `s(ω, d+1) = v_2(X - 3^(-1))`, and

```text
X - 3^(-1) = (X - 1) + (1 - 3^(-1)).
```

* If `s >= 2`: the summands have distinct valuations `s` and `1`, so the ultrametric equality gives `s(ω, d+1) = 1` — the spike branch's valuation conclusion, with no computation.
* If `s = 1`: the summands tie at valuation `1`; the ultrametric inequality gives only `s(ω, d+1) >= 2`, and the tie is resolved exactly by the Collatz step: `X - 1 = 2e` with `e` odd, so `3X - 1 = 2(3e + 1)` and

```text
s(ω, d+1) = v_2(3X - 1) = 1 + v_2(3e + 1) >= 2,
```

since `3e + 1` is even. ∎

In particular `s = 1` forces `s(ω,d+1) >= 2` and `s >= 2` forces `s(ω,d+1) = 1`: the alternation of `15.2` is a corollary of the dichotomy alone, independently of the first-layer classification from which it was first derived.

**Calibration.** What is unified here, and what is not. At the valuation level, the depth ladder is the target-shift mechanism read in the depth variable — the third face of the mechanism whose first two faces, boundary-shell localization and forced carry, stage3's Interpretation paragraph (`11.8.6.3`) already names. The unification stops there. The integer-level half of the ladder law — the exact affine kick `e ↦ 3·2^(s-1)·e + 1` and the exact identity `e(ω,d+1) = T(e(ω,d))` — is content about the exits themselves, and the valuation frame does not recover it: `15.1.1`'s elementary proof remains the proof of record, and the ladder law is not a corollary of the target-shift lemma. Nothing about any open problem moves; in particular the fiber-to-orbit bridge (`11.8.5.6`) is exactly as open as before. This subsection adds understanding, not leverage.

**Verification.** Fresh independent code (`experiments/ladder_targetshift.py`, seed `20260723`, 2026-07-23; imports nothing from `experiments/ladder.py`): Lemma `15.5.1` on `12,000` random `(state, k)` pairs (`ω < 10^6`, `d <= 60`, `k <= 40`, targets `3^(-k)` as residues mod `2^512`), zero failures; Proposition `15.5.2` on `72,000` triples `(ω, n, j)` per component (`300` cores each of `ω ≡ 1` and `ω ≡ 3 (mod 8)`, `n <= 24`, `j <= 10`, anchors mod `2^64` by digit-by-digit discrete log, calibrated against the published `N(17), N(25), N(33) mod 2^8`), zero failures on both components, plus `N(9^(-j)) = j` and `9^(-j) ≡ 1 (mod 8)` confirmed for `j <= 10`; Theorem `15.5.3` on `5,000` random states (`2,503` spike / `2,497` off-spike), zero failures, including the `k = 1` target-shift identity and the integer-level cross-check against `15.1.1` (`e' = T(e)` off-spike, the affine kick at spikes). Exact integer arithmetic at every pass/fail decision; zero precision flags.

## 15.7. Guaranteed neighbours: the two commutation laws

*(On this branch, 15.6 does not exist yet — the parallel branch
`ladder-afterlife` owns it (the tear afterlife); this section is appended
directly after 15.5, and the main session orders the sections at merge.)*

The author's proposal (2026-09-09): pin a family — a core `ω` at all
depths — and list its forward neighbour families `Ω(ω,d) := F(ω,d)`'s
core. The list is exact already: `Ω(ω,d)` is the core of stage4's
`C = 3^dω - 1 + 2^s`, so its residues are stage4.md 11.8.7.3.1's, and its
own core is the Bridge object (bridge.md §16 — pointer only, no claim
about the Bridge is made here). This section proves the two exact
relations the family list obeys as depth climbs within one column, closes
the search for further such relations by an elementary Diophantine
argument, and unifies both under one lemma.

Throughout, `A(ω,d) = 3^dω-1`, `s(ω,d)=v_2(A)`, `e(ω,d)=A/2^s` (the exit /
door), `C=A+2^s`, `e+1 = 2^{m₊}3^{a₊}Ω`, `D=m₊+a₊`, `F(ω,d)=(Ω,D)` — the
notation of spine.md §5.4–5.6 and stage3.md 11.8.6, per symbols.md frames
1–2. `T` is the odd-to-odd map of spine.md §9.8. The ladder recursion
`A(ω,d+1) = 3A(ω,d)+2` (15.1) gives, by induction, `A(ω,d+k) = 3^k A(ω,d)
+ (3^k-1)` for every `k ≥ 1`.

**Lemma 15.7.1 (law (i): merge/skip by `m₊`).** Fix `(ω,d)` with
`s(ω,d)=1`, and write `m=m₊(ω,d)`. If `m ≥ 2`: `F(ω,d+1) = F(ω,d)`. If
`m=1`: `F(ω,d+1) = F(F(ω,d))`.

**Proof.** `A(ω,d)=2e` (`e` odd, `e+1=2^m3^aΩ`). `3e+1 =
2^m3^{a+1}Ω-2 = 2(2^{m-1}3^{a+1}Ω-1)`, so `(3e+1)/2 = 2^{m-1}3^{a+1}Ω-1`.
If `m≥2` this is odd, so `v_2(3e+1)=1` and `e(ω,d+1)=T(e)=(3e+1)/2 =
2^{m-1}3^{a+1}Ω-1`; reading off `e(ω,d+1)+1 = 2^{m-1}3^{a+1}Ω` gives
`F(ω,d+1)=(Ω,(m-1)+(a+1))=(Ω,m+a)=F(ω,d)`. If `m=1` the same quantity is
`3^{a+1}Ω-1 = A(Ω,D)` (`D=1+a` here), so `v_2(3e+1)=1+s(Ω,D)` and
`e(ω,d+1)=T(e) = A(Ω,D)/2^{s(Ω,D)} = e(Ω,D)`, giving `F(ω,d+1)=F(Ω,D)=
F(F(ω,d))`. ∎

**Corollary 15.7.2 (the `ω mod 8` reading).** At every off-spike depth:
`ω ≡ 5, 7 (mod 8)` gives the merge (`F(ω,d+1)=F(ω,d)`); `ω ≡ 1, 3
(mod 8)` gives the skip (`F(ω,d+1)=F(F(ω,d))`).

**Proof.** By stage1.md 11.8.1.3.1, off-spike occurs at exactly one
parity of `d` per `ω mod 8`, on which `3^dω ≡ 7 (mod 8)` (`ω≡5,7`) or
`≡ 3 (mod 8)` (`ω≡1,3`). Since `C=3^dω+1` here (`s=1`), `m=v_2(C)-1`:
`3^dω≡7` gives `v_2(C)≥3` so `m≥2`; `3^dω≡3` gives `v_2(C)=2` exactly so
`m=1`. Apply 15.7.1. ∎

**Verification.** `experiments/ladder_family_graph.py` PART A, `40,000`
off-spike states constructed from the `ω mod 8` table (`19,883` merge,
`20,117` skip), zero failures on the `m₊` split and zero failures cross-
checking the `ω mod 8` reading against it, 2026-09-13.

**Lemma 15.7.3 (law (ii): the two-row commutation).** Fix `(ω,d)` with
`s(ω,d)=3` and `m=m₊(ω,d) ≥ 4`. Then `F(ω,d+2) = F(ω,d) - (0,1)`, and the
letter at `d+2` is `(6, m-3)`.

**Proof.** `A(ω,d)=8e`. `A(ω,d+2)=9A(ω,d)+8=8(9e+1)`, and
`9e+1 = 9(e+1)-8 = 9·2^m3^aΩ-8 = 8(9·2^{m-3}3^aΩ-1)` (`m≥4` so `m-3≥1`,
the bracket odd). So `s(ω,d+2)=3+3=6` and `e(ω,d+2) =
9·2^{m-3}3^aΩ-1 = 2^{m-3}3^{a+2}Ω-1`; reading off `e(ω,d+2)+1 =
2^{m-3}3^{a+2}Ω` gives `F(ω,d+2)=(Ω,(m-3)+(a+2))=(Ω,(m+a)-1)=
(Ω,D-1)`. ∎

**In bit language.** Writing `X=3^dω`, the low `σ=s+m` bits of `X` (bit 0
first) are exactly the letter in unary, `1,0^{s-1},1^m` (Remark 15.7.6
below); here `s=3` this reads `1,0,0,1^m`. Since `3^{d+2}ω=9X` and the
new letter is `(6,m-3)` with the same total `σ`, the low bits of `9X`
read `1,0^5,1^{m-3}` — multiplying the numerator by `9` rewrites
`1 0 0 1^m …` into `1 0^5 1^{m-3} …`.

**Verification.** PART B, `3,000` states with `s=3, m₊≥4` (`ω<4000,
d<400`): the state-level identity and letter, and the bit rewrite, both
zero failures, 2026-09-13. Box census (`ω<4,000, d≤40`, `53,320` states,
PART B2): `794` non-adjacent same-core pairs, of which `789` are
explained by this lemma; `5` unexplained small-number coincidences, all
landing on core `1` (the most frequent target in the box, 15.7.8), listed
in the findings.

**Proposition 15.7.4 (the repunit equation, Zsigmondy closure).** Climbing
`k` rows, `A(ω,d+k) = 3^k2^s u - c`, `u=e(ω,d)+1`, `c = 3^k(2^s-1)+1`. A
value of `c` that is a pure power of `2` (so the resulting core depends on
`u` alone) requires

```text
c = 3^k(2^s-1)+1 = 2^t
```

for some `t ≥ 1`, and the only solutions `(k,s,t)` are `(1,1,2)` and
`(2,3,6)`.

**Proof.** Write `N_j=2^j-1`; the equation is `N_t = N_s·3^k` with `s<t`
(forced: `s≥t` gives `N_t/N_s ≤ 1`, no room for `k≥1`), hence `s | t`
(since `N_s | N_t ⟺ s|t`). If `t=2`: `s=1` forced (only divisor `<2`),
giving `1+2=3`, `(k,s,t)=(1,1,2)`. If `t=6` (Zsigmondy's own exception for
base `2`): divisors `s∈{1,2,3}` give `N_6/N_s ∈ {63,21,9}`; only `9=3^2`
is a power of `3`, giving `(2,3,6)`. If `t≥3, t≠6`: by Zsigmondy/Bang's
theorem (Bang 1886, base `2`), `N_t` has a primitive prime divisor `p`
(dividing no `N_j`, `j<t`), and `p ≡ 1 (mod t)` by Fermat applied to
`ord_p(2)=t`; since `t≥3`, `p≥t+1≥4`, so `p≠3`. As `p` is primitive and
`s<t`, `p ∤ N_s`, so `p | N_t/N_s`; if `N_t/N_s=3^k` its only prime factor
is `3`, forcing `p=3` — contradiction. No solution for `t≥3,t≠6`. ∎

**Verification.** PART C: length-2 scan `s=1..59` finds exactly `(s,k) =
(1,1),(3,2)`; the elementary length-3 argument (`v_3(1+x+x^2)=1` for
`x=2^s`, `s` even) checked for `s=2..198`, zero failures; general search
`k,s≤200` (`40,000` pairs) finds exactly the two solutions; Zsigmondy
exceptions for base `2` over `t=3..30` (full trial-division
factorization) found to be exactly `{6}`, matching the theorem, 2026-09-13.

**Lemma 15.7.5 (the unified statement).** For `(k,s,t)` one of the two
solutions of 15.7.4, fix `(ω,d)` with `s(ω,d)=s`, `m=m₊(ω,d)`,
`F(ω,d)=(Ω,D)`.

```text
m ≥ t-s+1:  F(ω,d+k) = (Ω, D+s-t+k)
m = t-s:    F(ω,d+k) = F(Ω, D+s-t+k)
m < t-s:    no claim (finite coincidence only)
```

**Proof.** With `u=e(ω,d)+1=2^m3^aΩ`: `A(ω,d+k) = 2^{s+m}·3^{k+a}Ω - 2^t`.
If `s+m>t`: `= 2^t(2^{s+m-t}·3^{k+a}Ω-1)`, odd bracket, giving
`e(ω,d+k)+1 = 2^{s+m-t}3^{k+a}Ω` and `F(ω,d+k)=(Ω, (s+m-t)+(k+a)) =
(Ω,D+s-t+k)`. If `s+m=t`: `= 2^t(3^{k+a}Ω-1) = 2^t·A(Ω,k+a)`, so
`e(ω,d+k)=e(Ω,k+a)` and `F(ω,d+k)=F(Ω,k+a)=F(Ω,D+s-t+k)` (since
`m=t-s` gives `D+s-t+k=a+k`). If `s+m<t`, the `2^{s+m}` term dominates and
`e(ω,d+k)` carries no forced relation to `Ω,D`. ∎

At `(1,1,2)`: `m≥2` is 15.7.1's merge, `m=1` its skip. At `(2,3,6)`:
`m≥4` is 15.7.3; `m=3` is the boundary case `F(ω,d+2)=F(Ω,D-1)`. Laws (i)
and (ii) are, together with this boundary case, the **only** primitive
commutation relations at these two solutions.

**Verification.** PART D, `5,000` cases per solution, split by regime:
zero failures in every dominant and boundary case at both solutions
(`(1,1,2)`: `2,533` dominant, `2,467` boundary; `(2,3,6)`: `584` dominant,
`628` boundary, `3,788` unclaimed), 2026-09-13. A stratum census over
`20,000` random states and `k=1..8` (PART E) confirms the same-core rate
is exactly `1.000` on `(k,s,m₊)=(1,1,≥2)` (`4,961` cases) and `(2,3,≥4)`
(`294` cases), and — corrected against an earlier, unfiled pre-check —
exactly `0.000`, not a partial rate, on the strata `(2,3,3)` (`294`
cases) and `(3,1,1)` (`5,101` cases): a diagnostic check confirmed that
even where the naive composition mechanism's structural precondition
holds, no same-core match occurs (0 of 2,058 further-sampled cases); the
findings file records the correction and the diagnostic in full. One
further stratum, `(4,4,2)`, shows a single coincidental match in `336`
cases (`0.003`), reported and not further pursued.

**Remark 15.7.6 (bits gained, read backward — a reading).** *(Of
stage3.md 11.8.6.3, reverse.md 14.14.1, itinerary.md 14.15.1.1 and
stage2.md 11.8.5; nothing here is a new fact.)* Backward, the
predecessor's numerator `3^dω = 1+2^s(2^m3^aΩ-1)` has, in its low
`σ=s+m` bits, exactly the letter in unary, `1,0^{s-1},1^m`, followed by
the bits of `3^aΩ-1` shifted up by `σ`. Forward, the door gains `d`
ternary digits, `y ≡ -2^{-s} (mod 3^d)`, fixed by `s` alone; the 3-gain
`a₊=v_3(2^s-1)` (stage2's `h(s)`) is that fixed signature's own 3-adic
valuation, read off-resonance (`h(s)<d`). No freedom lives in the gained
digits; the backward freedom is the door choice, and the signature is
that choice written out. Verified: `experiments/ladder_family_graph.py`
PART F, `20,000` states each, zero failures on the backward identity and
the forward door congruence, `19,957` non-resonant cases (of `19,957+43`)
zero failures on the 3-gain signature, 2026-09-13.

**Remark 15.7.7 (the mirror at reverse.md 14.10 — no twin, and why).**
The literal transplant of 15.7.1/15.7.3 to the dual ladder (reverse.md
14.10: fix a door `y`, examine `F` applied to predecessors at climbed
branches `s, s+2, s+4, ...`) is vacuous: by reverse.md 14.1.1's own
defining property, `F` applied to *any* predecessor of `(Ω,D)` returns
`(Ω,D)`, independent of branch — there is no dichotomy to find, because
the degree of freedom law (i)/(ii) exploit (a many-to-one map's images
coinciding across genuinely different sources) is absent once the target
is fixed by construction. Verified as a sanity check on the obstruction
itself, not a new fact: `5,000` random `(y,s)` pairs, zero failures
(`experiments/ladder_family_graph.py` PART G); a further negative control
(does the predecessor's own core repeat across climbed branches?) found
zero repeats in `3,000` doors at `k=1,2`. No remark is added at
reverse.md 14.10.

**Remark 15.7.8 (the family graph: in-degree).** Over the box `ω<4,000,
d≤40` (`53,320` states), the most frequent target cores are `1` (`114`
hits), `5` (`62`), `7` (`57`), `11` and `13` (`42` each) — this is the
backward tree of reverse.md 14.1.1 and nothing new: small cores recur as
targets across many `(ω,d)` because their representative count and
predecessor density are both larger.
