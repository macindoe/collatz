---
status: CLOSED as a local law (15.1–15.2, verified, zero failures); the author's divergence question answered exactly (15.3)
scope: new section 15 (post-monolith)
updated: 2026-07-23
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

This closes the vertical question as a local law. Open connections worth recording, not yet pursued: the ladder gives a second exact mechanism relating *different states with the same anchor* (at the valuation level identified in `15.5` as the target-shift lemma read in the depth variable), which is raw material for the fiber-to-orbit bridge (stage4.md, `11.8.5.6`) — the bridge asks how anchors vary along orbits, and the ladder shows how orbits vary along an anchor; whether the two exact laws compose into anything is unexamined. The mirror front has its dual ladder: reverse.md `14.10` relates predecessors at adjacent branches `s` and `s+2` at a fixed door (step size `2` forced by the parity constraint), with an exact dichotomy gated by the `3`-adic anchor's first digit — the mirror of `15.1`'s tear-line.

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
