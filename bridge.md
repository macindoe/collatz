---
status: OPEN — the program's terminal open object, consolidated; states the object and its observed mechanisms, no proof effort on this page
scope: new section 16 (post-monolith); cross-cutting — owned by neither stage4.md nor reverse.md §14
updated: 2026-07-23
source: consolidation of 11.8.5.6 (forward bridge), 11.8.7.7 (digit budget), 14.13 (reverse precision loss); the author's framing — "the bridge between the M(ω)'s is itself the question"
---

# 16. The Bridge: the anchor increment at unbounded depth

> **Current state.** This page consolidates the program's terminal open object, until now scattered across three loci: the forward anchor-increment identity (stage2.md 11.8.5.6), the digit budget that forbids bounded-window closure (stage4.md 11.8.7.7), and the reverse precision loss that obstructs a stationary residue system (reverse.md 14.13). It states the object once and records its observed mechanisms; it points to the owning pages rather than restating their facts (one-fact-one-page, AGENTS.md). No new theorem and no proof effort live here. The register is deliberately flat: this page exists so the open object is one findable thing rather than three fragments, and it seeds space that is not yet explored — no significance beyond that is claimed.

## 16.1. The object

The per-step arithmetic of the reduced map is formal to low order: from a state's finite window, the next step's exit valuation `s`, its depth, its `3`-gain, and the anchor increment `ΔM mod 2^k` are all exact (stage4.md 11.8.7.3.1, 11.8.7.6.1). The single thing no bounded window determines is the anchor increment *at unbounded depth* — how `M(ω)` passes to `M(ω_+)` in its high digits. This is **the bridge** (named at stage2.md 11.8.5.6, via the increment identity `ΔM = N((ω_+/ω)^2)`): the forward open object on which convergence for typical orbits depends. Its reverse mirror is the passage `M₃(y) → M₃(y')` (reverse.md 14.13), on which the backward density program depends.

The author's framing, adopted here: *the bridge between successive anchors is itself the question.* Everything else is either downstream of it — the per-step laws are the bridge's bounded-depth shadow — or a statement of what closing it would buy: the statistical half forward (AEH, §13), the density half reverse (§14).

**The door-centred formulation (2026-07-14).** `ΔM` and the reduced map both admit a coordinate change onto one shared integer, the live door `y` of a reduced edge — reverse.md 14.14. In door coordinates the increment is a mismatch of one fixed operation on the two integers flanking `y` (14.14.2), and the reduced map's door-coordinate presentation `G` — semiconjugate to `F`, not strictly conjugate (14.14.3) — obeys a *total*, constant-modulus graded law for the `3`-adic anchor along forward orbits (14.14.5) — sharper in form than the forward law above or the reverse mirror's own top-door version (14.8.2). This is not new leverage on the object: 14.14.6 shows the gain is bought at exactly the core-extraction deficit's price (`16.2` below), relocated onto the same `2`-adic digit data `11.8.7.7` already prices, not escaped. The hole this page states is unchanged; it now has a second, independently-derived coordinate system pointing at it.

**The itinerary language (2026-07-16).** A further layer (itinerary.md `14.15`) proves the seam's own stratum word is fully characterized at finite level — a full shift, the classical Collatz coding in door coordinates — and formulates a two-sided `Z_2 × Z_3` coding whose diagonal compatibility locus is exactly this page's open object, under a symbolic name. The hole is unchanged.

**Equivalent names.** The mirror side also names this object as boundedness versus escape of the positive realization height `(H_{p,q})` (itinerary.md 14.15.4.5, the equivalence theorem; 14.15.5.4, the combined three-way characterization; 14.15.9, the whole-period form). The equivalence is stated and owned there; this page only lists it among the object's equivalent forms.

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

It does **not** narrow what is provable. Closing the bridge still requires the statistical hypothesis (AEH, §13) for typical orbits, or a rigidity argument on finite closed anchor walks (`Σ ΔM_t = 0`, spine.md 9.8.4; effective `p`-adic tools, stage1-synthesis.md 11.8.3.11) for cycles — exactly as before. The deficit explains the wall; it does not lower it.

One asymmetry, recorded honestly: the forward state is two-dimensional — both `ω` and `d` feed `2`-adic precision — while the reverse door `y` is a single coordinate that determines its state. So the duality is exact at the level of *core-extraction loss*, not of the whole state. This matches the mirror asymmetries already noted in §14 (the forward trichotomy collapsing to a reverse dichotomy, door mortality having no forward analogue).

## 16.4. The perimeter: mapping the edges

The open object is narrow and well-surrounded. Everything below charts the known ground that borders it: where each result stops touching the Bridge is where the solid ground ends. This is a map — pointers only; each fact lives on its own page (AGENTS.md), and is characterized here solely by *how it bounds the open object*.

### 16.4.1. The floor — what is determined, below the open part

- **The increment is not a new unknown.** `ΔM = N((ω_+/ω)^2)` is a deterministic function of the current `C` (stage2.md 11.8.5.6). In anchor coordinates the fiber-to-orbit bridge and Stage 3 are literally the same problem; with `v₂(C)` and `v₃(C)` formal per step (stage3.md 11.8.6.3, 11.8.6.2), the *entire* unresolved content of `ΔM` is the odd core `ω_+` itself.
- **Low order is closed.** `ΔM mod 2^k` obeys an exact law, modulus fixed in advance per `(s, m_+)` stratum — sub-question 1 of 11.8.5.6.3, answered (stage4.md 11.8.7.3.1).
- **Bounded depth is closed.** The depth-`k` window decides the next `3`-gain in an error-free trichotomy, undecided only at rate `≈ 2^(−(k+1))` — sub-question 2 in its bounded-depth form (stage4.md 11.8.7.6.1).
- **A finite-state chart exists.** Composing the per-step laws yields an exact countable-state transition chart whose only unresolved inputs are the shell labels at unbounded depth (stage4.md 11.8.7.3.1, finite-state remark; this answers the finite-state-shadow question, open-problems.md 11.6).

### 16.4.2. The wall — why the floor stops

The core-extraction deficit (16.2): the forward digit budget (stage4.md 11.8.7.7) and the reverse precision loss (reverse.md 14.13), one phenomenon read from both ends.

### 16.4.3. The forward escape — what closing the Bridge buys typical orbits

- **The exact missing hypothesis.** Anchor equidistribution in its precise bulk form `π_k` (aeh.md 13.2); the conditional theorems fix what it buys — the frequency ledger, the `1/3` `3`-gain rate, the classical drift, all almost-everywhere — and what it cannot — individual staircase tails (aeh.md 13.3, esp. 13.3.3); its symbolic name is the genericity form (aeh.md 13.6): bulk Bernoulli-genericity of the integers' door letter words.
- **The empirical texture.** Fair-coin anchor digits, density `0.497` (stage1.md 11.8.4.2); the frequency and size ledgers, empirically sharp to three decimals (stage1.md 11.8.4.4).
- **The regime split.** The open object lives in the *bulk* (while `x` is large), where uniformity stands unqualified; the wild statistics are confined to the fixed *bottom* drainage basin of small integers (aeh.md 13.1).
- **The single-sequence endpoints.** The anchor's own bit string was searched for internal structure — statistical batteries, an automaticity/algebraicity screen, operation lenses, PractRand — and came back clean at every endpoint (anchor-digit-search.md §17.7): calibration for this escape, not progress on it.

### 16.4.4. The cycle escape — rigidity, where finite data can beat depth

- **The exact target.** A nontrivial cycle is a finite closed anchor walk with `Σ ΔM_t = 0` (spine.md 9.8.4, anchor form); cycle exclusion is a rigidity statement about such walks.
- **The tools with traction.** Effective `p`-adic Baker theory (stage1-synthesis.md 11.8.3.11): an unconditional polylogarithmic spike-height bound and an effective irrationality measure for the anchor — the one regime where existing mathematics bites the object directly; the spent `|q| = 1` stock and this digit-match ceiling are one rigidity boundary at this target (cycles.md 12.6.1.3).
- **The constants, pinned.** The traction claim's numeric parameters are pinned and numerically checked from the primary sources: G. Rhin's effective bound (via Simons–de Weger 2005, Lemma 12) gives `K log2 - n log3 > exp(-13.3(0.46057+log n))` unconditionally, closing cycles.md 12.5.3 and 12.7.5's `n > 20,000` cases by thousands of bits; Bugeaud–Laurent's Corollaire 2 (1996; the `g=1` case, automatic for `p=2`) gives `v_2(9^n·ω-1) <= 208·log9·logω·(max{...})^2`, fixing the spike-height exponent at exactly `2` with an explicit `C(ω)`; and cycles.md 12.8.2's explicit `n_0(p)` is closed by the full `γ↔Λ` conversion (`Λ < exp(p - γ·log2)` unconditionally), combined with Theorem 12.8.1 and Rhin's bound into an explicit equation, solved and tabulated (`n_0(91) ~ 3*10^21`, e.g.). Derivations in stage1-synthesis.md 11.8.3.11 and cycles.md 12.5.3/12.7.5/12.8.2; the discharge record is open-problems.md §11.8. Verified numerically 2026-07-12.
- **The counting limit.** A trim uniform in `p` exists and gives effective finiteness at every period (cycles.md 12.8.1–2), but its constant degrades like `1.585^(−p)`; the staircase family proves no size-counting argument does better (cycles.md 12.8.3).

### 16.4.5. The reverse face — the mirror

- **The object's mirror.** The exact backward branching law carried by the `3`-adic anchor (reverse.md 14.2.4).
- **Placeable in reverse.** The steering laws show the anchor walk — unsolved forward — can be *placed* backward, via the same identity as the forward valuation law read from the other end (reverse.md 14.12, 14.12.3).
- **The mirror wall, and what backward buys.** Reverse precision loss (reverse.md 14.13) is the deficit's other face; the rigorous density program and its proved bound live on this side (reverse.md 14.4–14.6).
- **The door/exit seam.** A third coordinate on the same edge, neither the forward core nor the backward predecessor: the live door `y` (reverse.md 14.14). It gives `ΔM` a fixed-operation form (14.14.2) and the reduced map a total, mortality-free door-coordinate presentation with a constant-offset graded `3`-adic law (14.14.3–14.14.5) — and, per 14.14.6, relocates rather than escapes the deficit, landing exactly on `16.2`'s and `11.8.7.7`'s own `(s, m_+)` accounting. A corollary layer (reverse.md 14.14.7–14.14.8, 2026-07-15) reads `G` as `T`'s own variable-return-time block map and composes the graded law along fixed itineraries; the composed fixed point is identified with the classical cycle candidate (cycles.md §12.1) — a reconciliation, not a new lever. This object is unmoved by it. A further layer (itinerary.md 14.15, 2026-07-16) proves the seam's stratum word is a full shift at finite level and formulates a two-sided `Z_2 × Z_3` coding whose diagonal compatibility locus (definition and trivial direction only) is this page's object under a symbolic name; periodic words reconcile with the same classical cycle candidate. A fourth block (itinerary.md 14.15.4, 2026-07-16) proves the letter-prescribed backward predecessor is unique (hence automatically positive), that every finite two-sided itinerary window is realized by an actual positive live integer segment (no finite obstruction, ever, at any finite depth), and gives the diagonal locus an equivalent **boundedness criterion**, the *positive realization height* `H_{p,q}(W)`: integral realization holds iff `H_{p,q}(W)` is bounded — the precise archimedean condition the `Z_2 × Z_3` diagonal embedding forgets. A fifth block (itinerary.md 14.15.5, 2026-07-16) proves the converse of the trivial diagonal direction (`14.15.3.6`): `W` is integrally realized iff `y₂(W)=y₃(W)` at a single **positive odd integer**, completing the diagonal locus's characterization into a three-way equivalence (integrally realized ⟺ diagonal limits agree at a positive integer ⟺ `H_{p,q}` bounded) and reconciling the periodic word `((2,1))^∞`'s negative diagonal point (`y₂=y₃=-5`) with the classical negative `T`-cycle `{-5,-7}`, whose positive realization height is verified to escape (`n=1..8`). This is a further symbolic name for this page's object, not an estimate of it: no bound, recurrence, or growth rate for `H` is supplied, and no method is supplied for deciding the boundedness condition on any word family beyond the periodic case. This object remains unmoved. A sixth block (itinerary.md 14.15.6, 2026-07-16) restates the fifth's apparatus over the **nonzero odd integers**, relocating the positivity hypothesis to a sector choice rather than a structural requirement, with one genuine one-sided exception recorded precisely (`G` can output the singular point `-1` from the negative sector only, never the positive — forward mortality with no backward analogue). The three-way characterization, the finite bicylinder corollary, and the realization height all transfer sign-blind, checked step by step rather than assumed (the height transfer in particular — the one place a genuine snag could plausibly have appeared — was found to hold with no obstruction, verified in both the bounded and the escaping direction). The known negative cycles (`{-5,-7}`, and the period-`7` cycle `{-17,-25,-37,-55,-41,-61,-91}`, identified as the `G`-period-`2` word `((4,1),(3,3))` with fixed point `y^*=-17`) become ordinary periodic diagonal points under this reading rather than boundary exceptions; `{-1}` alone stays genuinely outside the coding. This is a further relabeling, over a larger domain, of the same open object — not new leverage on it. This object remains unmoved. Subsequent blocks (itinerary.md 14.15.7–14.15.9) close the exact height laws through the whole-period classification: for every fixed periodic word, realization heights obey one unified law conditional on the word's fixed-point denominator `q`, so height growth contributes no further obstruction once `q` is known — pointer, not restatement; the object is still unmoved; the per-cycle door-word ↔ near-miss-anchor dictionary is stated once at itinerary.md 14.15.10 (a naming of the census cross-frame, not a lever).

### 16.4.6. The seam — where the two escapes meet

- **One configuration, both halves.** The staircase — a divergent-orbit profile bent into a loop — is simultaneously the cycle-sharpness family (cycles.md 12.8.3) and the AEH-exceptional set (aeh.md 13.3.3): size analysis cannot forbid it as a cycle for the same reason drift cannot forbid divergence (cycles.md 12.8.4). Strong evidence the statistics-half and the rigidity-half are one problem.
- **The vertical neighbor.** The depth ladder relates `(ω,d)` and `(ω,d+1)` at fixed core by an exact dichotomy — one Collatz step off-spike, an affine kick at spikes — answering the divergence question as a local law (ladder.md §15); it borders the divergence half from the fixed-core direction.
- **The seam identity.** The cycle-side transport recurrence (cycles.md Remark 12.6.1.1) and the mirror-side rotation lemma (itinerary.md 14.15.9.2) are the same fact under the seam identity — the two escapes' cycle bookkeeping meets on one identity.

## 16.5. What the map shows (the grounding)

The open object is narrow and completely encircled. The floor (16.4.1) determines everything up to the odd core's unbounded-depth digits; the wall (16.4.2) is exactly why it stops there; and on every side — statistics (16.4.3), rigidity (16.4.4), mirror (16.4.5) — the known ground runs right up to the same edge and no further. Two escapes are marked, equidistribution and rigidity; they share one exceptional configuration (16.4.6); and only the second touches tools that presently have traction (11.8.3.11), which is why the program's stated bet (README; stage1.md 11.8.4.4) is the cycle side. That is the grounding: the perimeter is solid and mutually consistent, and the hole is precisely the unbounded-depth anchor digits — one object, bounded on all sides by proved statements, open in exactly one place.

**Verification.** The grounding claim was checked edge by edge against its owning theorems, with the cycle-rigidity edge's constants (Rhin's measure, the Bugeaud–Laurent exponent, cycles.md 12.8.2's `n_0(p)`) pinned and numerically verified (16.4.4, cycles.md 12.5.3/12.7.5/12.8.2, stage1-synthesis.md 11.8.3.11; 2026-07-12). The perimeter's claim of solidity is checked, not merely asserted; it does not narrow the hole.

