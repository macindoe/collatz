---
status: CLOSED as a local law (15.1–15.2, verified, zero failures); the author's divergence question answered exactly (15.3)
scope: new section 15 (post-monolith)
updated: 2026-07-22
source: the author's question "where do (ω,d) and (ω,d+1) diverge?"; builds on §3 anchor machinery
---

> **Current state.** The vertical structure of the state space, solved. Adjacent depths at a fixed core obey `A(ω,d+1) = 3·A(ω,d) + 2`, which forces an exact dichotomy (15.1): off-spike (`s = 1`), the deeper state's exit is *one Collatz step ahead* of the shallower one's — same integer orbit, offset by one step, divergence never; at a spike (`s ≥ 2`), the exits split by the explicit kick `e ↦ 3·2^(s−1)e + 1` — divergence immediate and total. Since `s = 1` occupies alternating depths, every column of the anchor field is a perfect braid of single Collatz steps and affine kicks (15.2). The spikes — the anchor's digit matches — are exactly the divergence points of the depth ladder (15.3). A hoped-for stronger form (columns encoding long orbit stretches) is false and recorded as such.

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

This closes the vertical question as a local law. Open connections worth recording, not yet pursued: the ladder gives a second exact mechanism relating *different states with the same anchor*, which is raw material for the fiber-to-orbit bridge (stage4.md, `11.8.5.6`) — the bridge asks how anchors vary along orbits, and the ladder shows how orbits vary along an anchor; whether the two exact laws compose into anything is unexamined. The mirror front has its dual ladder: reverse.md `14.10` relates predecessors at adjacent branches `s` and `s+2` at a fixed door (step size `2` forced by the parity constraint), with an exact dichotomy gated by the `3`-adic anchor's first digit — the mirror of `15.1`'s tear-line.
