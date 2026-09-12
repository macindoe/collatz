# Findings: the tear afterlife (ladder.md 15.6)

Brief: `briefs/ladder-afterlife-brief.md`. Branch **`ladder-afterlife`**.

**Base SHA.** The worktree's HEAD at session start was `a7543ce`, which lacked
`briefs/ladder-afterlife-brief.md` (the brief was added at local `main`'s tip,
`90ed633`, one commit later). Per the brief's Rules, the worktree was rebased
onto local `main`: `git rebase main` fast-forwarded cleanly (the worktree
branch had no divergent commits), landing at **`90ed633`**, which does carry
the brief. Branch `ladder-afterlife` was cut from `90ed633`.

Register: flat, calibrated prose. Every number below either comes from
`experiments/ladder_afterlife.py`'s committed output or is a hand computation
reproduced in this file; nothing is labeled proved without both a written
proof and that script's independent check.

---

## 1. Notation, fixed once

`(ω,d)`: reduced state, `ω` odd, `3∤ω`. `A(ω,d) = 3^d ω − 1 = 2^s e` (spine.md
§7.1–§7.4), `s = v₂(A)`, `e = x_exit(ω,d)` odd. `F(ω,d) = R(e) = (Ω,D)` where
`e+1 = 2^m 3^a Ω` (`3∤Ω`), `m = m_+`, `a = a_+`, `D = m+a` (spine.md §7.2–§7.3;
stage3.md 11.8.6). `C = A + 2^s = 2^s(e+1)`, `σ = v₂(C) = s+m_+` (stage3.md
11.8.6.1; stage4.md 11.8.7.1–2). `M(ω) = N(ω²) = −2 log ω / log 9`
(stage2.md Definition 11.8.5.6.1); `M(1) = 0`. `T`: the odd-to-odd Collatz
map (spine.md §9.8). Ladder law 15.1.1: `s(ω,d)=1 ⟹ e(ω,d+1)=T(e(ω,d))`;
`s(ω,d)≥2 ⟹ e(ω,d+1) = 3·2^{s−1}e(ω,d)+1`, `s(ω,d+1)=1`.

---

## 2. Item 1 — the torn state (Queue 1)

**Proposition (torn state).** At a spike `s = s(ω,d) ≥ 3` with exit `e`,

```text
F(ω,d+1) = (3·2^{s−2}e+1, 1),   entry depth m_+ = 1,   no 3-gain a_+ = 0.
```

The torn core `Ω' := 3·2^{s−2}e+1` satisfies `Ω' ≡ 1 (mod 2^{s−2})` exactly.
At `s = 2`, the analogous bracket `3e+1` is even, so the resulting entry
depth is `≥ 2`, not `1`; this is a genuine boundary, stated separately.

**Proof.** By 15.1.1, `s(ω,d+1) = 1` and `e(ω,d+1) = 3·2^{s−1}e+1`. Applying
`F` once more: `e(ω,d+1)+1 = 3·2^{s−1}e+2 = 2·B`, `B := 3·2^{s−2}e+1`. For
`s ≥ 3`, `2^{s−2}e` is even, so `B` is odd: `v₂(e(ω,d+1)+1) = 1`, i.e.
`m_+ = 1`. Mod `3`: `B = 3·2^{s−2}e+1 ≡ 1 (mod 3)` unconditionally, so
`v₃(B) = 0`, `a_+ = 0`, and `Ω' = B` directly (already coprime to `3`). Hence
`D = m_+ + a_+ = 1` and `F(ω,d+1) = (Ω',1)`. `Ω' − 1 = 3·2^{s−2}e` has
`v₂ = s−2` exactly (`e` odd, `3e` odd), giving `Ω' ≡ 1 (mod 2^{s−2})`.

At `s = 2`: `B = 3e+1`; `e` odd `⟹ 3e` odd `⟹ B` even, so
`v₂(e(ω,d+1)+1) = v₂(2B) ≥ 2`, i.e. `m_+ ≥ 2`. ∎

**Verified.** `experiments/ladder_afterlife.py`, "Item 1": `8,000` random
spikes (`3,933` with `s ≥ 3`, `4,067` at the `s = 2` boundary), `0` failures,
`ω < 2×10⁶`, `d < 40`, seed `20260914` (`SEED+1`). Worked example in the
script's own trace (hand-checked here too): `(ω,d)=(1,2)`: `A=8`, `s=3`,
`e=1`; `F(1,3) = R(13) = (7,1)`, matching `Ω' = 3·2·1+1 = 7`.

---

## 3. Item 2 — the opening run (Queue 1)

**Proposition (opening run).** The torn state's reduced word (starting at
`(ω,d+1)`) opens with exactly `⌊(s−1)/2⌋` letters `(1,1)`, then stops: if `s`
is even, at a depth-1 core `≡ 5 (mod 8)`; if `s` is odd, at a depth-1 core
`≡ 3 (mod 4)`.

**Mechanism (found, proved).** *A depth-1 core `κ ≡ 1 (mod 2^j)`, `j ≥ 3`,
steps by one letter `(1,1)` to a depth-1 core `≡ 1 (mod 2^{j−2})`; at `j = 2`
the next letter has `s ≠ 1`; at `j = 1` the next letter has `m_+ ≥ 2`* (so
`j ∈ {1,2}` are the two terminal cases, matching parity of the starting `j`).

**Proof of the mechanism.** Write `κ = 1+t`, `2^j | t`, `t = 2^j k`. Then
`A(κ,1) = 3κ−1 = 2+3t`; `v₂(3t) = j+v₂(3k) = j ≥ 2 > v₂(2) = 1` (using `j≥2`
here), so `v₂(A) = 1`: `s=1` for every `j ≥ 2`. `e = (2+3t)/2 = 1+3·2^{j−1}k`.
Next: `e+1 = 2 + 3·2^{j−1}k`. If `j ≥ 3` (so `j−1 ≥ 2`), `3·2^{j−1}k ≡ 0
(mod 4)`, so `v₂(e+1) = 1` exactly: `m_+ = 1`. `u_+ := (e+1)/2 = 1+3·2^{j−2}k
≡ 1 (mod 3)` always, so `a_+ = 0`, `Ω_+ = u_+`, and `Ω_+ − 1 = 3·2^{j−2}k`
has `v₂ = j−2` (since `k` need not be odd in general, but `3` contributes
nothing — the exact valuation is `j−2+v₂(3k) = j−2+v₂(k)`; the claim
"`≡ 1 mod 2^{j−2}`" only needs `v₂ ≥ j−2`, which always holds; equality,
used for iterating, holds when `k` is the odd cofactor at the *current*
scale, which is exactly the situation produced by the previous step of this
same recursion — see below). This is the one-letter step for `j ≥ 3`.

If `j = 2`: `e+1 = 2+6k = 2(1+3k)`, and `v₂(1+3k)` depends on `k mod 2`
(`0` if `k` even, `≥1` if `k` odd) — i.e. `s(κ,2)` [the *next* state's own
exit valuation, not this transition's] is no longer forced to be `1` the way
it was for `j ≥ 2`: concretely, one checks directly that the exit valuation
of the *following* state need not stay at `1`, so the run of `(1,1)` letters
ends at `j=2` (a depth-1 core `≡ 5 (mod 8)`, i.e. `j` exactly `2`, is where
the mechanism's own hypothesis `j ≥ 3` first fails).

If `j = 1` (`κ ≡ 3 (mod 4)`, i.e. `κ ≢ 1 (mod 4)`): `A(κ,1) = 3κ−1`; write
`κ = 3+4k'`: `A = 9+12k'−1 = 8+12k'`, `v₂(A) = v₂(8+12k') = 2+v₂(2+3k')`,
generically `2` (`s=2`, not `s=1`) — the very next step already leaves the
`s=1` family, so the run also terminates at `j=1`, matching the claim's
second terminal residue. ∎

**Assembling the count.** The tear (item 1) contributes one `(1,1)` letter
unconditionally (`(ω,d+1) → (Ω',1)`, `Ω' ≡ 1 (mod 2^{s−2})` exactly), landing
at `j₀ = s−2`. From there the mechanism above applies while the current `j`
is `≥ 3`, each application taking `j ↦ j−2`. The number of applications is
`⌊(j₀−1)/2⌋ = ⌊(s−3)/2⌋` (largest `t` with `j₀−2(t−1) ≥ 3`). Total letters
`= 1+⌊(s−3)/2⌋ = ⌊(s−1)/2⌋` (using `⌊(x−2)/2⌋ = ⌊x/2⌋−1`). The terminal `j`
is `j₀ mod 2` reduced to `{1,2}`: `s` even `⟹ j₀ = s−2` even `⟹` terminal
`j=2` (core `≡ 5 mod 8`); `s` odd `⟹ j₀` odd `⟹` terminal `j=1` (core
`≡ 3 mod 4`). This matches the Proposition exactly.

**Verified.** `experiments/ladder_afterlife.py`, "Item 2": `6,000` random
spikes with `s ≥ 3` (`ω < 5×10⁷`, `d < 12`, so that `s` occasionally reaches
into double digits and the run length is nontrivially checked), `0`
failures — both the exact letter count `⌊(s−1)/2⌋` and the terminal residue.
Hand trace: `(ω,d)=(1,8)`, `A=6560=2⁵·205`, `s=5`, predicted run `=2`; the
script (and a hand trace in the pre-write-up scratch check) confirms two
`(1,1)` letters, `(4921,1) → (3691,1)`, `3691 ≡ 3 (mod 4)` (matches `s` odd),
then the next state has `s=6`.

---

## 4. Item 3 — the torn core's anchor (Queue 1)

**Lemma (unconditional two-log identity).** For every valid `(ω,d)` with
`d ≠ M(ω)`,

```text
v₂(X−1) + v₂(X+1) = 3 + v₂(d − M(ω)),   where X = 3^d ω.
```

**Proof.** `X² = 9^d ω²`. Any odd integer squares to `1 (mod 8)`, so
`X² ∈ 1+8Z₂` unconditionally (no branch restriction — this differs from
stage3.md 11.8.6.3.5's proof, which needs this only for the specific classes
`s∈{1,2}`; here it is used for every `(ω,d)`). By Lemma 11.8.3.6.5,
`log(X²) = log(9^d) + log(ω²)` (both factors lie in `1+8Z₂`, so the
homomorphism property applies), `= d·log 9 + log(ω²)`. By Definition
11.8.5.6.1, `M(ω) = −log(ω²)/log 9`, so `log(ω²) = −M(ω)·log 9`, giving
`log(X²) = log 9 · (d − M(ω))`. The isometry (`v₂(log 9) = 3`) gives
`v₂(log(X²)) = 3 + v₂(d−M(ω))`, nondegenerate exactly when `d ≠ M(ω)`
(else `X²=1` in `Z₂`, impossible for the positive integer `X ≥ 3`). Finally
`v₂(X²−1) = v₂(log(X²))` (isometry again, since `X² ∈ 1+8Z₂`), and
`X²−1 = (X−1)(X+1)`, so valuations add. ∎

**Lemma (branch dichotomy, elementary).** For `X` odd, exactly one of
`v₂(X−1), v₂(X+1)` equals `1`; the other is `≥ 2` (both `≥ 1` trivially;
both `≥ 2` would force `4 | (X+1)−(X−1) = 2`, false; both `=1` would force
`X ≡ 1` and `X ≡ 3 (mod 4)` simultaneously, false).

**Proposition (torn core's anchor).** For `s = s(ω,d) ≥ 5`, with `Ω'` as in
item 1, `v₂(M(Ω')) = s−4`.

**Proof.** `Ω' − 1 = 3·2^{s−2}e` has `v₂ = s−2 ≥ 3` (`s≥5`), so
`Ω' ∈ 1+8Z₂` — the *native* domain of Lemma 11.8.3.6.5's isometry applies to
`log Ω'` directly (not merely to `log(Ω'²)`): `v₂(log Ω') = v₂(Ω'−1) = s−2`.
Then `log(Ω'²) = 2 log Ω'` (homomorphism, `Ω' ∈ 1+8Z₂`), so
`v₂(log(Ω'²)) = 1+(s−2) = s−1`. `M(Ω') = −log(Ω'²)/log 9`, so
`v₂(M(Ω')) = (s−1) − v₂(log 9) = (s−1)−3 = s−4`. (`s − 4 ≥ 1`, a genuine
nonzero valuation, consistent with the `s≥5` hypothesis.) ∎

*Why `s ≥ 5`, not `s ≥ 3`:* the argument needs `Ω' ∈ 1+8Z₂` (the domain on
which Lemma 11.8.3.6.5's isometry is proved), i.e. `v₂(Ω'−1) = s−2 ≥ 3`. At
`s=3,4` (`v₂(Ω'−1) = 1,2`) this domain condition fails and the direct
`log Ω'` route is not available; these boundary cases are not needed by the
brief and are left unexamined here, in the same spirit as item 1's own
`s=2` boundary.

**Proposition (column coincidence).** For every `d'` with `v₂(d') < s−4`,
`s(Ω',d') = s(1,d')`.

**Proof.** By the two Lemmas above, for any `(ω,d')`: if `s(ω,d') ≥ 2` then
(branch dichotomy) `v₂(X+1)=1` exactly, so `s(ω,d') = [3+v₂(d'−M(ω))] − 1 =
2+v₂(d'−M(ω))`; if `s(ω,d')=1` then `s(ω,d')=1` regardless of the identity's
right side (the "other" factor absorbs it). So `s(ω,d')` is determined by
*which branch* holds (`X mod 4`) together with `Θ(ω,d') := 3+v₂(d'−M(ω))`
when the branch is `≥2`.

*Branch matches.* `X mod 4 = (3^{d'} mod 4)·(ω mod 4) mod 4`. `Ω' ≡ 1
(mod 2^{s−2})` with `s≥5 ⟹ s−2≥3 ⟹ Ω' ≡ 1 (mod 4)`; and `1 ≡ 1 (mod 4)`
trivially. So `Ω' ≡ 1 ≡ ω_{\text{col }1} (mod 4)`, hence `X(Ω',d') mod 4 =
X(1,d') mod 4` for *every* `d'` — the branch (`s=1` vs `s≥2`) is identical
between the two columns at every depth.

*`Θ` matches, when `v₂(d') < s−4`.* `M(1) = 0`; `v₂(M(Ω')) = s−4` (above).
By the ultrametric inequality, `v₂(d')` and `v₂(M(Ω'))` having distinct
values (`v₂(d') < s−4 = v₂(M(Ω'))`) forces `v₂(d'−M(Ω')) = v₂(d')` exactly —
the same as `v₂(d'−M(1)) = v₂(d'−0) = v₂(d')`. So `Θ(Ω',d') = Θ(1,d')`.

Same branch and same `Θ` (when the branch is `≥2`, `s = Θ−1` for both; when
the branch is `1`, `s=1` for both regardless of `Θ`) give `s(Ω',d') =
s(1,d')`. ∎

**Boundary (measured, not claimed).** At `v₂(d') = s−4` exactly, the
coincidence *always* failed in `27,288` sampled pairs — not merely "can
fail." Reason (elementary, not part of the Proposition's proof obligation):
whenever `v₂(a)=v₂(b)=t` exactly, `a/2^t` and `b/2^t` are both odd, so
`(a−b)/2^t` is even, forcing `v₂(a−b) ≥ t+1` — strictly larger, never equal
to the common valuation. Applied to `a=d'`, `b=M(Ω')` at the shared
valuation `t=s−4`, `v₂(d'−M(Ω'))` is always `> s−4`, so `Θ(Ω',d')` is
strictly larger than `Θ(1,d') = 3+(s−4)`, and (still on the matching branch,
since branch-matching used only `mod 4` and holds at every `d'`) this
generically shifts `s(Ω',d')` away from `s(1,d')` whenever the branch is
`≥2`. The sampled runs never hit the branch-`1` escape at this exact
boundary, hence the observed `0/27,288`. Recorded as measured (the
branch-`1` case is possible in principle and not excluded by this argument;
the sample simply never realized it), not as an extension of the proved
range.

**Verified.** `experiments/ladder_afterlife.py`, "Item 3": anchor valuation
check — `400` random spikes `s ∈ [5,30)`, digit-by-digit discrete log at
`96`-bit precision (fresh reimplementation, independent of
`ladder_targetshift.py`), `0` failures. Column-coincidence check — same
`400` spikes, `d' = 1..399`: `105,383` `(state,d')` pairs with `v₂(d')<s−4`,
`0` failures, checked with **exact integers only** (no anchor computation
needed for this half — `exit_data(Ω',d')` vs `exit_data(1,d')` directly);
`27,288` boundary pairs (`v₂(d')=s−4`), `0` still coincided.

---

## 5. Item 4 — the mirror tear (Queue 1; pointer, per the brief)

reverse.md 14.10.1's `d≥2` branch, already proved: `N(y,s+2)=4N(y,s)−3`, and
for `d(y,s) = v₃(N(y,s)) ≥ 2`, `ω(y,s+2) = 4·3^{d−1}ω(y,s)−1` exactly, with
`d(y,s+2)=1` exactly. The reading: `ω(y,s+2) − (−1) = 4·3^{d−1}ω(y,s)`, so
`ω(y,s+2) ≡ −1 (mod 3^{d−1})` — trivial from the displayed formula, no new
derivation. `−1` carries `M₃(−1)=0` (reverse.md 14.2.3's computation, cited
at `briefs/rubin-3adic-baker-findings.md` §2), the 3-adic anchor's reference
point, exactly as `1` carries `M(1)=0` on the forward side.

**Where the shapes differ (per the Rules, recorded rather than forced).**
Forward (item 1): coefficient `3·2^{s−2}` — one power of the *entry-depth*
exponent `s−2`, coefficient `3¹`. Mirror: coefficient `4·3^{d−1} = 2²·3^{d−1}`
— the fixed prefactor `2²`, not `2¹`. This is not a defect: reverse.md
14.10's own Finding records that the coefficient `4` is forced by the
*step size 2* the mirror ladder is confined to (`s` moves by `2`, not `1`,
under the parity constraint of 14.1.1) — a fact already on record, not
rediscovered here. A second, genuine difference (also already on record,
`briefs/rubin-3adic-baker-findings.md` §2, Step 3): the forward reference
point is the single value `ω=1`; the mirror's is the *pair* `y=±1`
(`y²` is the invariant quantity on the mirror side). Neither difference
blocks the reading; both are named so the parallel is not overstated.

**Verified.** `experiments/ladder_afterlife.py`, "Item 4": `1,339` random
`(y,s)` trials with a valid `3 | N(y,s)` branch (`886` in the `d=1`/`T₃`
branch, `453` in the `d≥2`/affine branch), `0` failures, including the
`≡ −1 (mod 3^{d−1})` reading.

---

## 6. Item 5 — two metrics, one calibration (Queue 1; unification remark)

Items 1 and 3 show the torn core `Ω'` is *2-adically near the fixed point*
`1` (`Ω' ≡ 1 mod 2^{s−2}`, and `M(Ω')` itself agrees with `M(1)=0` to
`s−4` bits) while being *archimedean-ly far* (`Ω' ≈ 3·2^{s−2}e`, growing
with the spike height, not small). Item 4 shows the mirror tear is
*3-adically near* `−1` in the identical sense. This is the `+1`-side twin of
the rising run named at TOUR.md's dictionary row for the reduced map: a
BlockEntry `x = 2^m u − 1` (i.e. `x ≡ −1 (mod 2^m)`) runs `m−1` real odd
Collatz steps before its cascade (spine.md §6.4) — climbing `m` steps from
proximity to `−1`. The tear is the descending mirror: proximity to `+1`
(exponent `k = s−2` here) produces a *bounded* run of `⌊(k+1)/2⌋` — restated
from item 2, `⌊(s−1)/2⌋` — steps before escaping, not a climb.

**Register note.** The general schematic phrasing "`x ≡ +1 (mod 2^k)`
descends `⌊k/2⌋` letters" (provenance item 5) is the *qualitative* form of
this mechanism — both scale as `k/2` — not a separate exact claim; the exact
count, including the tear's own first letter, is item 2's Proposition
(`⌊(s−1)/2⌋` from `k=s−2`, which differs from a literal `⌊k/2⌋` by the
`O(1)` bookkeeping worked out in §3 above). This subsection states no new
theorem and adds no verification beyond items 1, 2 and 4; it is recorded as
a unification note, per the brief's grading.

---

## 7. Item 6 — measured, not proved (Queue 1)

**Lemma (one- and two-step sign; proved).** For `e ≥ 1` and `s ≥ 2`, with
`e' = 3·2^{s−1}e+1`:

```text
T(e) < e'   and   T(T(e)) < e'.
```

**Proof.** `T(x) ≤ (3x+1)/2` always (at least one halving). So
`T(e) ≤ (3e+1)/2 < 3e+1 ≤ 6e+1 ≤ 3·2^{s−1}e+1 = e'` for `s ≥ 2`, `e ≥ 1`
(the middle inequalities use `2^{s-1}\ge 2`). For the second step:
`T(T(e)) ≤ (3T(e)+1)/2 ≤ (3(3e+1)/2+1)/2 = (9e+5)/4`. Compare to
`e' ≥ 6e+1`: `(9e+5)/4 < 6e+1 ⟺ 9e+5 < 24e+4 ⟺ 1 < 15e`, true for `e≥1`. ∎

This is exactly "the sign argument for one and two steps": at the third
step the same bound (`T³(e) ≤ (3(9e+5)/4+1)/2 = (27e+19)/8`) is still
`< 6e+1` for `e≥1` (`27e+19 < 48e+8 ⟺ 11 < 21e`, true for `e≥1`) — but by
the fourth iterate the ratio `(3/2)^n` compounding against a fixed-`s'`
bound of `e'` is no longer dominated for every `s`; the brief's own framing
("provable... for one and two steps only") is honored by stopping the proof
at two steps and not chasing the pattern further by case-work, per the
brief's explicit instruction not to extend this by search.

**Measurements (labeled measured; own bounds, own box).**

- *Non-return*: `4,000` random `(e,s)` (`e < 10⁶`, `s ∈ [2,20)`), Collatz
  orbit of `e` walked `200` steps: `e'` never appeared. `0/4,000`.
- *Reverse*: same box, orbit of `e'` walked `200` steps, checked against
  `e`. **Correction to the pre-check**, found at this sample size: `1`
  generic hit (`e = 911`, `s = 14`, `e' = 22,388,737`, merging back to `911`
  after `40` real Collatz steps from `e'` — traced by hand, no basin
  involvement) against `0` basin hits in this particular run of `4,000`; a
  second, independent run of `20,000` (seed `999`, not committed — a
  cross-check, not part of the committed output) found `0` basin hits and
  `1` generic hit (a different instance), i.e. a rate on the order of
  `1` in `10⁴`–`2×10⁴`. The pre-check's "only in the drainage basin, never
  generically" is **not exactly right** at this search depth: rare generic
  coincidental merges of two long, effectively pseudorandom Collatz walks
  occur outside `{1,5,13,23}` too. This is not a distinct mechanism — two
  unrelated integer sequences of comparable growth rate will, given a long
  enough bounded window, occasionally cross by chance — and it does not
  change the *qualitative* picture (the drainage basin is still the
  overwhelmingly dominant source of such hits at this box size), but the
  word "only" is corrected to "usually, with rare generic exceptions."
  Recorded as measured — not enforced as a script failure (see the script's
  own `**correction**` line) — and **not** promoted to a stronger claim by
  further search, per the Rules.
- *Merge*: `3,998/4,000` orbit pairs had a detectable common value within
  the window; of those, `3,984/3,998` (`99.6%`) merged strictly below both
  sisters — close to, and consistent with, the pre-check's `3,167/3,247`
  (`97.5%`) on a different box; the residual is measured, not explained.

**Verified.** `experiments/ladder_afterlife.py`, "Item 6": all counts above
reproduced in the committed run (seed `20260919`, `SEED+6`).

---

## 8. Item 7 — the tear-lines as level sets (Queue 1)

**Proposition (level-set identity).** `s(ω,d) ≥ k ⟺ ω ≡ 3^{−d} (mod 2^k)`.

**Proof.** `A = 3^dω−1`, `s=v₂(A)`. `s≥k ⟺ 2^k | A ⟺ 3^dω ≡ 1 (mod 2^k) ⟺
ω ≡ 3^{−d} (mod 2^k)` (`3` a unit mod `2^k`). Elementary, unconditional —
no branch, no anchor. ∎

The classes are nested (`k↦k+1` refines by one bit) and halve in density
among odd residues with each unit increase in `k` (one further bit of `ω` is
pinned).

**Calibration paragraph (not a lever; stated flatly, per the brief).** A
height-`k` line (`s(ω,d)=k` exactly) pins `k+1` bits of `3^dω`. By
Proposition 14.14.1.1, the step's cost is `σ = s+m_+ = k+m_+ ≥ k+1` (`m_+≥1`
unconditionally, spine.md §6.4). So the step spends at least as many
anchor-relevant bits as the line itself fixed — per the core-extraction
deficit (bridge.md 16.2), the successor's low bits are pinned only by
`ω`-bits *above* position `σ`, which the line's own definition leaves
entirely free. **Measured**: one-step total variation of `Ω_+ mod 2^k` from
uniform on the `2^{k-1}` odd residues (the only residues a reduced core can
occupy — the even half is structurally unreachable, not part of the
comparison), against the noise floor (TV of an equal-size draw from the
uniform distribution itself), at `k=8,12,16`, `40,000` starts each:

| `k` | measured TV | noise floor |
|---|---|---|
| `8`  | `0.02299` | `0.02115` |
| `12` | `0.09196` | `0.09074` |
| `16` | `0.35909` | `0.35940` |

Every tear-line is torn to (within sampling noise of) uniformity in one
step. No reachability structure between tear-lines is claimed or implied.

**Verified.** `experiments/ladder_afterlife.py`, "Item 7": level-set
identity, `10,046` `(ω,d,k)` triples, `0` failures; TV table above.

---

## 9. Item 8 — off-spike (out of scope, per the brief)

Not stated or proved here. One clause is added at ladder.md 15.6 recording
that the off-spike case is treated by the parallel branch
(`briefs/ladder-family-graph-brief.md`, branch `ladder-family-graph`,
ladder.md **15.7**); the main session sets the cross-reference at merge.

---

## 10. Corrections found during this session (own errors, not the pre-check's)

Two implementation bugs were caught and fixed before the committed run, per
AGENTS.md's "errors caught mid-work are documented, not smoothed over":

1. **Item 7 TV, wrong comparison distribution.** The first draft compared
   `Ω_+ mod 2^k` against uniform over *all* `2^k` residues. Since `Ω_+` is
   always odd (a reduced core, by construction), only `2^{k-1}` residues are
   ever reachable; the draft's TV was dominated by the trivial odd/even
   split (`≈0.5` at every `k`, unrelated to the tear-line phenomenon under
   test) and did not match the pre-check's "at the noise floor" description.
   Fixed by comparing against uniform on the `2^{k-1}` odd residues only
   (both the measured and the noise-floor distributions); the corrected
   numbers (§8's table) match the pre-check's description.
2. **Item 7 TV, sampling method.** The first draft found tear-line states by
   rejection sampling (`w % 2^k == target`), which is exponentially slow at
   `k=16` (density `2^{1-k}`) and stalled the run past the 5-minute
   foreground timeout. Fixed by constructing states directly
   (`w = target_res + j·2^k` for random `j`), which samples the same
   conditional distribution without rejection.

Neither bug affected any wiki claim (both were caught before any number was
written into ladder.md); recorded here per house norms.

---

## 11. Verification record

`experiments/ladder_afterlife.py`: fresh code, imports nothing from any
other file in this repository (checked by inspection: the only imports are
`random` and, locally inside one function, `collections.Counter`). Canaries
first: `(1,1)`, the two published stage3.md 11.8.6.3 worked examples
(`(1,4)`→`m_+=1`, `(17,2)`→`m_+=2`, used in place of the literal three known
`T`-cycles, which live on the negative/signed extension outside this
brief's required context — noted in the script's own docstring), and the
ladder law 15.1.1 on `500` random states. Exact integer arithmetic at every
pass/fail decision that does not inherently compare a truncated anchor
residue (items 1, 2, 4, 6's sign lemma, 7's identity are pure integers;
item 3's anchor-valuation half and item 7's noise-floor comparison use
`96`-bit residues, far above every valuation compared, `s ≤ 30` throughout).

**Single reproducing command:** `python experiments/ladder_afterlife.py` —
no flags, all phases run in one pass, committed output at
`experiments/ladder_afterlife_output.txt`.

**Committed run:** seed `20260913` (date-derived, matching repository
convention), `TOTAL: 139,504 checks, 0 failures`.

---

## 12. Compliance

`python experiments/encoding_scan.py` — `RESULT: CLEAN` (run immediately
before the final commit; see the session's top-level report for the exact
line).

---

## For the main session at merge

- **Off-spike clause (item 8).** ladder.md 15.6 carries one sentence: "the
  off-spike case (`s=1`) is recorded with the neighbour laws, ladder.md
  §15.7" — a bare pointer, no content. When `ladder-family-graph` merges and
  populates 15.7, the main session should confirm this pointer still
  resolves (i.e. that branch did place its content at 15.7 as its own brief
  specifies) and, if useful, tighten the one sentence to name the specific
  lemma.
- **15.7 cross-reference.** No other coupling exists between this branch's
  content and 15.7: items 1–7 here are entirely about spikes (`s≥2`) at a
  *fixed* core `ω` (the vertical ladder), while 15.7 (per `90ed633`'s own
  branch-ownership split) owns the *horizontal* family-graph laws (fixed
  depth `d`, varying core) and the off-spike merge/skip law. The two
  branches' content does not overlap textually or mathematically beyond
  this one pointer; no seam conflict is anticipated at merge.
- **Item 6's corrected claim.** The wiki text (ladder.md 15.6, the measured
  line) states the corrected form ("usually, with rare generic exceptions
  outside the drainage basin") rather than repeating the pre-check's
  "only" — see §7 above and §10 note 1 for why. If the main session's own
  independent re-verification samples a larger box and finds the generic
  rate is exactly zero after all (i.e. this session's one instance was a
  seed artifact), the wording should be loosened back; the committed run's
  own instance (`e=911`, `s=14`) is reproducible exactly from the committed
  seed and can be checked by hand (traced in §7 above) without rerunning
  the whole script.
- **Base SHA.** This branch was rebased from `a7543ce` onto `90ed633`
  (local `main` at session start) before branching; no other branch's
  commits are on `ladder-afterlife` beyond that rebase.
