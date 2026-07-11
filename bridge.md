---
status: OPEN — the terminal open object of the program, consolidated. The forward increment law is proved to low order (11.8.7.3.1) and the reverse mirror is verified (14.13); what is open in both directions is the increment at unbounded depth, and that is the whole remaining difficulty. No proof effort lives on this page — it states the object and records its observed mechanisms.
scope: new section 16 (post-monolith); cross-cutting — owned by neither stage4.md nor reverse.md §14
updated: 2026-07-11
source: consolidation of 11.8.5.6 (forward bridge), 11.8.7.7 (digit budget), 14.13 (reverse precision loss); the author's framing — "the bridge between the M(ω)'s is itself the question"
---

# 16. The Bridge: the anchor increment at unbounded depth

> **Current state.** This page consolidates the program's terminal open object, until now scattered across three loci: the forward anchor-increment identity (stage2.md 11.8.5.6), the digit budget that forbids bounded-window closure (stage4.md 11.8.7.7), and the reverse precision loss that obstructs a stationary residue system (reverse.md 14.13). It states the object once and records its observed mechanisms; it points to the owning pages rather than restating their facts (one-fact-one-page, AGENTS.md). No new theorem and no proof effort live here. The register is deliberately flat: this page exists so the open object is one findable thing rather than three fragments, and it seeds space that is not yet explored — no significance beyond that is claimed.

## 16.1. The object

The per-step arithmetic of the reduced map is formal to low order: from a state's finite window, the next step's exit valuation `s`, its depth, its `3`-gain, and the anchor increment `ΔM mod 2^k` are all exact (stage4.md 11.8.7.3.1, 11.8.7.6.1). The single thing no bounded window determines is the anchor increment *at unbounded depth* — how `M(ω)` passes to `M(ω_+)` in its high digits. This is **the bridge** (named at stage2.md 11.8.5.6, via the increment identity `ΔM = N((ω_+/ω)^2)`): the forward open object on which convergence for typical orbits depends. Its reverse mirror is the passage `M₃(y) → M₃(y')` (reverse.md 14.13), on which the backward density program depends.

The author's framing, adopted here: *the bridge between successive anchors is itself the question.* Everything else is either downstream of it — the per-step laws are the bridge's bounded-depth shadow — or a statement of what closing it would buy: the statistical half forward (AEH, §13), the density half reverse (§14).

## 16.2. Observed mechanism: the core-extraction deficit

Why is the bridge open — why can more digits not close it? Because one step, in either direction, forms a raw combination and then extracts a coprime core by dividing out a power of the anchor's own prime:

- **Forward** (`2`-adic anchor): `C = 3^d ω − 1 + 2^s`, then `ω_+ = (C / 2^σ)·3^(−a_+)`, where `σ = v₂(C)` (stage4.md 11.8.7.2).
- **Reverse** (`3`-adic anchor): `N = 2^s y + 1`, then `ω' = N / 3^d`, where `d = v₃(N)` (reverse.md 14.1–14.2).

The division is exact but precision-lossy in the anchor's own prime, and the number of anchor digits consumed per step is *exactly the stripped exponent*:

```text
forward:  knowing ω to 2^(σ+r)  pins ω_+ to only 2^r    (σ = v₂(C) digits lost)
reverse:  knowing y to 3^(d+r)  pins ω' to only 3^r      (d = v₃(N) digits lost)
```

and that exponent is `≥ 1` every step in both directions — `σ ≥ 2` forward (`C = 2^s(odd+1)` with `s ≤ σ`), `d ≥ 1` reverse (admissible `s` force `3 | N`). Nothing regenerates the supply, so **no bounded-precision iterate of the anchor exists in either direction.** Call this the **core-extraction deficit**: the bridge is open because the map's defining act — pulling a coprime core out of a raw number — spends anchor precision it cannot recover.

The two directions are one fact under the `2↔3` mirror (14.3). The forward digit budget (11.8.7.7), which localizes typical-orbit difficulty to the anchor digit supply, and the reverse affine-collapse obstruction (14.13), which forbids a stationary residue LP, are the same phenomenon read from opposite ends: forward strips `2^σ` from `C`, reverse strips `3^d` from `N`, and each pays its own prime's digits.

**Verified** — `experiments/digit_duality.py`, fresh implementations importing nothing from the repo (AGENTS.md house norm). Forward precision law with the depth coordinate held fixed to isolate the `ω`-tail, `d ∈ {5, 7, 12}`: zero conflicts pinning `ω_+ mod 2^r` from `ω mod 2^(σ+r)`, and a broken pin one digit shorter — `σ` digits lost, exactly. Reverse precision law: zero conflicts pinning `ω' mod 3^r` from `y mod 3^(d+r)`, broken one digit shorter — `d` digits lost, exactly. Measured mean loss per step: `σ ≈ 4.0` (min `2`) forward, `d ≈ 1.5` (min `1`) reverse.

## 16.3. What this does and does not do

The deficit is a **diagnostic, not a lever.** It answers, once and uniformly, the question that recurs whenever a new attack is proposed — *can this be closed with bounded or finite data?* — with: not if it must cross the core-extraction step, which is every step. It would have priced the KL–LP stationary-residue detour (14.13) as doomed before it was attempted; it is recorded here so the next such temptation, forward or reverse, is checked against it first.

It does **not** narrow what is provable. Closing the bridge still requires the statistical hypothesis (AEH, §13) for typical orbits, or a rigidity argument on finite closed anchor walks (`Σ ΔM_t = 0`, spine.md 9.8.4; effective `p`-adic tools, stage1.md 11.8.3.11) for cycles — exactly as before. The deficit explains the wall; it does not lower it.

One asymmetry, recorded honestly: the forward state is two-dimensional — both `ω` and `d` feed `2`-adic precision — while the reverse door `y` is a single coordinate that determines its state. So the duality is exact at the level of *core-extraction loss*, not of the whole state. This matches the mirror asymmetries already noted in §14 (the forward trichotomy collapsing to a reverse dichotomy, door mortality having no forward analogue).
