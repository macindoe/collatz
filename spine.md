---
status: proved
scope: monolith sections 1-9
updated: 2026-07-22
source: sources/drafts/collatz_reduction_rewrite_v078.md (last monolith)
---

> **Current state.** The formal spine: reduced formalism, block determinism, the reduced map F, and all proved structural properties, including the convergence translation (9.8) — the exact equivalence between the Collatz conjecture and "every F-orbit reaches (1,1)". Everything here is established; open material lives in program.md, stage1-3, and open-problems.md.

# 1. Purpose and Scope

This document develops a reduced structural formalism for the Collatz map by factoring out deterministic valuation behavior into extended valuation blocks and studying the induced dynamics on reduced states `(ω,d)`. The objective is not to analyze the iteration step-by-step, but to isolate the arithmetic structure that remains once these deterministic block effects are compressed. In particular, the reduced formalism ultimately yields a self-map on reduced states, so the reduced state space is not merely a quotient interpretation of the dynamics but a dynamical system in its own right.

The central hope of this framework is that the reduced dynamics may reveal a more connected and intelligible state structure than is visible in the raw iteration. In particular, the goal is to understand how reduced states relate to one another, whether transitions admit further reduction, and whether the induced map exposes structural regularities that are obscured in the standard formulation.

No claim is made here regarding convergence or a resolution of the Collatz conjecture. The purpose of this note is only to define the reduced formalism clearly, establish its exact algebraic properties, and identify which additional patterns appear to merit further investigation. The formalism is, however, a faithful arena for the conjecture rather than a lossy summary of it. Section `9.8` proves an equivalence — the conjecture holds if and only if every orbit of the reduced map reaches the fixed state `(1,1)`, and nontrivial Collatz cycles correspond bijectively to nontrivial cycles of the reduced map. What is proved is the equivalence itself, not either side of it: the statement "every reduced orbit reaches `(1,1)`" is exactly as open as the conjecture, because it is the conjecture, in reduced coordinates. The value of the equivalence is two-way transfer — any future proof or counterexample at either layer settles the other with no further argument — and the guarantee that the reduced problem is neither lossy nor secretly easier.

# 2. Layered View of the Collatz Map

The reduction developed in this note is best understood as a layered compression of the ordinary Collatz dynamics rather than as a single reformulation. Each layer isolates a different kind of structure, and only the final layer introduces the genuinely reduced state space studied here.

## Layer 1. Raw Collatz Iteration

At the first layer sits the ordinary Collatz map on the positive integers. This is the classical step-by-step dynamics, whose local behavior is easy to define but whose longer-range arithmetic structure is difficult to read directly from iteration alone.

## Layer 2. Extended Valuation Blocks

The second layer groups together contiguous stretches of the dynamics in which the valuation behavior of `x + 1` evolves deterministically. These extended valuation blocks compress repeated local behavior that does not need to be re-analyzed at every step. This layer is still an exact reformulation of the same dynamics, but organized around deterministic block structure rather than individual Collatz steps.

## Layer 3. BlockEntry Coordinates `(u,m)`

The third layer records each block at its entry in canonical coordinates. Here `u` denotes the odd seed associated with the block entry and `m` records the local entry depth. These coordinates describe the block exactly and provide the natural input data for the structural step formula developed later. They also provide the scaffolding through which the reduced map is first derived and the route by which its well-definedness is proved.

## Layer 4. Reduced Structural States `(ω,d)`

The fourth layer passes from exact block coordinates to reduced structural states. Writing `u = 3^a ω` with `3` not dividing `ω`, the reduced state is obtained by retaining the structural odd core `ω` together with the full combined depth `d = m + a`. This is the genuinely reduced layer: different BlockEntry coordinates may determine the same reduced state, and the reduced state space ultimately carries its own intrinsic self-map, which is the main object studied in this note.

The first three layers should be viewed primarily as exact organization of the dynamics: they isolate deterministic structure, choose convenient coordinates, and prepare the quotient. The fourth layer is the novel step of the framework, where part of the arithmetic data is factored out and the dynamics are studied through the induced transition on reduced states. In this sense, Layer 3 provides the scaffolding and proof route, while Layer 4 is not merely a quotient space but a dynamical system in its own right.

No claim is made here that the earlier layers are historically new in themselves. The point is instead that they provide the scaffolding needed to define the reduced structural state space cleanly and to formulate the induced map on that space.

## Running Example

A small example helps illustrate how the same local trajectory appears at each layer. Consider the odd value `23`. Then

```text
23 + 1 = 24 = 2^3 · 3,
```

so the associated block-entry data are `u = 3` and `m = 3`, since `23 = 2^m u - 1`. In reduced form, `u = 3^1 · 1`, so `a = 1`, `ω = 1`, and `d = m + a = 4`.

Viewed through the four layers:

- At Layer 1, one follows the ordinary Collatz trajectory beginning at `23`.
- At Layer 2, one isolates the deterministic valuation block beginning from the representation `23 = 2^3 · 3 - 1`.
- At Layer 3, that block is recorded exactly by the BlockEntry coordinates `(u,m) = (3,3)`.
- At Layer 4, the same block is represented only by the reduced structural state `(ω,d) = (1,4)`.

This example is intentionally small. Its purpose is only to show how one and the same trajectory fragment is successively reorganized, first into exact block coordinates and then into a reduced quotient state.

# 3. Definitions and Notation

This section introduces the objects used throughout the note in the same order as the layered reduction described above. The aim is to define each level of structure clearly before the induced map on reduced states is studied.

## 3.1. The Collatz Map

Let `T` be the Collatz map on the positive integers, defined by

```text
T(x) = x/2      if x is even,
T(x) = 3x + 1   if x is odd.
```

The ordinary dynamics of the conjecture are obtained by iterating `T` step-by-step.

## 3.2. Extended Valuation Blocks

An extended valuation block is a contiguous stretch of the Collatz dynamics beginning at an odd value of the form

```text
x = 2^m u - 1,
```

where `u` is odd and `m >= 1`. Along such a block, repeated odd-to-odd steps along the block remove exactly one factor of `2` at each stage until the block reaches its odd exit. The exact deterministic evolution of these blocks is established later; here the term is introduced only as the basic compressed unit of the dynamics.

## 3.3. BlockEntry Coordinates

A BlockEntry is the pair `(u,m)` associated with an odd value `x` of the form

```text
x = 2^m u - 1,
```

with `u` odd and `m >= 1`. These coordinates record the odd seed `u` and the `2`-adic entry depth `m` at the beginning of the block.

Whenever convenient, the corresponding odd value `x` may be recovered from `(u,m)` by the same formula.

## 3.4. Structural Odd Core and 3-adic Content

For a BlockEntry seed `u`, write

```text
u = 3^a ω,
```

where `a = v_3(u)` and `3` does not divide `ω`. The quantity `a` records the `3`-adic content of `u`, while `ω` is the structural odd core obtained after removing all factors of `3` from `u`.

## 3.5. Reduced Structural State

The reduced structural state associated with a BlockEntry `(u,m)` is the pair `(ω,d)`, where

```text
d = m + a.
```

Thus the reduced state retains the structural odd core `ω` together with the full combined depth parameter `d`, while no longer distinguishing between different decompositions of that total depth into separate contributions from `m` and `a`.

## 3.6. The Projection `R`

Define the projection `R` from BlockEntry coordinates to reduced structural states by

```text
R(u,m) = (ω,d),
```

where `u = 3^a ω` with `3` not dividing `ω` and `d = m + a`.

This projection passes from exact block coordinates to the reduced state space studied in the rest of the note.

## 3.7. Induced Reduced Dynamics

The structural step on BlockEntry coordinates determines a corresponding transition on reduced states by passing through the projection `R`. At the level of construction, one may describe the reduced map by the sequence:

- start from a BlockEntry `(u,m)`,
- compute its structural-step output,
- project the result back to a reduced structural state.

This is the route by which the reduced map is first derived.

Equivalently, once the structural exit is expressed in reduced variables, the reduced dynamics may be written intrinsically on the reduced state space itself. If `x_exit(ω,d)` denotes the deterministic odd exit associated with the reduced state `(ω,d)`, then

```text
F(ω,d) = R(x_exit(ω,d)).
```

Thus the reduced map may be understood in two equivalent ways: as the projection of the BlockEntry structural step, or as the direct reduction of the structural exit computed from `(ω,d)` alone.

The fact that these constructions depend only on the reduced state `(ω,d)`, and not on the particular BlockEntry representative chosen, is a substantive result and is proved later in Section 8.

# 4. Dictionary of Symbols

This section collects the main symbols used throughout the note for quick reference. The formal definitions remain those of Section 3.

## 4.1. Layer 1: Raw Collatz Iteration

- `T`: the Collatz map on the positive integers.
- `x`: an integer in the raw Collatz dynamics; when discussing a block entry, typically an odd value of the form `x = 2^m u - 1`.

## 4.2. Layer 2: Extended Valuation Blocks

- **extended valuation block**: a deterministic block segment of the dynamics beginning from an odd value of the form `x = 2^m u - 1` and continuing until its odd exit.

## 4.3. Layer 3: Exact Block Coordinates

- `u`: the odd seed in the BlockEntry coordinates.
- `m`: the `2`-adic entry depth in the BlockEntry coordinates; equivalently, `m = v_2(x + 1)`. Note: this renders `m = 0` meaningless.
- `(u,m)`: the BlockEntry coordinates associated with an odd value `x = 2^m u - 1`.
- `E`: the structural step on BlockEntry coordinates.

## 4.4. Layer 4: Reduced Structural States

- `a`: the `3`-adic content of `u`, defined by `a = v_3(u)`.
- `ω`: the structural odd core of `u`, defined by `u = 3^a ω` with `3` not dividing `ω`.
- `d`: the full combined depth parameter, defined by `d = m + a`.
- `(ω,d)`: the reduced structural state associated with a BlockEntry.
- `R`: the projection from BlockEntry coordinates to reduced structural states, given by `R(u,m) = (ω,d)`.
- `F`: the reduced self-map on structural states, equivalently defined by passing the structural step through `R` or by `F(ω,d)=R(x_exit(ω,d))`.

## 4.5. Symbols for a Single Structural Step

- `A`: the structural-step numerator `A = 3^d ω - 1`.
- `s`: the `2`-adic valuation of `A`, namely `s = v_2(A)`.
- `x_exit`: the deterministic odd exit associated with the reduced state `(ω,d)`, given by `x_exit = A / 2^s`.
- `m_+`: the next-entry depth, defined by `m_+ = v_2(x_exit + 1)`.
- `u_+`: the next odd seed, defined by `u_+ = (x_exit + 1) / 2^(m_+)`.
- `a_+`: the `3`-adic content of `u_+`, defined by `a_+ = v_3(u_+)`.
- `ω_+`: the structural odd core of `u_+`, defined by `u_+ = 3^(a_+) ω_+` with `3` not dividing `ω_+`.
- `d_+`: the next reduced depth parameter, defined by `d_+ = m_+ + a_+` when the next BlockEntry is formed.

When no ambiguity arises, the subscripts `+` indicate the corresponding quantities attached to the next block entry or next reduced state produced by a single structural step.

# 5. Coordinate Maps and Structural Transforms

This section records the main maps used in the reduced formalism as explicit transforms between the different coordinate domains. Some of these are changes of representation, while others are genuinely dynamical. The distinction matters.

The odd integers `x` and the BlockEntry coordinates `(u,m)` are in bijection, so they may be regarded as two exact representations of the same entry data. By contrast, the passage from `(u,m)` to a reduced state `(ω,d)` is many-to-one, and the passage from `(ω,d)` to `x_exit` is a forward structural transform rather than a change of coordinates. In particular, `(ω,d)` determines `x_exit`, but `x_exit` need not determine a unique predecessor reduced state, since the same odd value may arise as the exit of different structural cascades.

A useful schematic is:

```text
x <-> (u,m) -> (ω,d) -> x_exit -> (u_+,m_+) -> (ω_+,d_+).
```

## 5.1. Transform `X -> B`: Odd Integer to BlockEntry

**Domain.** Odd positive integers `x`.

**Codomain.** BlockEntry pairs `(u,m)` with `u` odd and `m >= 1`.

**Formula.** Given an odd integer `x`, define

```text
m = v_2(x + 1),
u = (x + 1) / 2^m.
```

Then `u` is odd and

```text
x = 2^m u - 1.
```

Accordingly, the associated BlockEntry is

```text
B(x) = (u,m).
```

**Inverse formula.** Given a BlockEntry `(u,m)`, the corresponding odd integer is

```text
x = 2^m u - 1.
```

Thus the transform `X -> B` is a bijection between odd positive integers and valid BlockEntry pairs.

## 5.2. Transform `B -> R`: BlockEntry to Reduced State

**Domain.** BlockEntry pairs `(u,m)` with `u` odd and `m >= 1`.

**Codomain.** Reduced structural states `(ω,d)` with `ω` odd and `3` not dividing `ω`.

**Formula.** Given `(u,m)`, write

```text
u = 3^a ω,
```

where

```text
a = v_3(u)
```

and `3` does not divide `ω`. Then define

```text
d = m + a.
```

Accordingly, the associated reduced structural state is

```text
R(u,m) = (ω,d).
```

This transform is surjective but not injective.

**Representative fiber.** For a fixed reduced state `(ω,d)`, the full BlockEntry fiber is

```text
R^(-1)(ω,d) = {(3^r ω, d - r) : 0 <= r <= d - 1}.
```

Thus many BlockEntry coordinates represent the same reduced structural state.

## 5.3. Direct Transform `X -> R`: Odd Integer to Reduced State

Composing the previous two transforms gives a direct passage from an odd integer `x` to its reduced structural state.

**Domain.** Odd positive integers `x`.

**Codomain.** Reduced structural states `(ω,d)`.

**Formula.** Given odd `x`, define

```text
m = v_2(x + 1),
u = (x + 1) / 2^m,
a = v_3(u),
ω = u / 3^a,
d = m + a.
```

Then

```text
R(x) = (ω,d).
```

Equivalently, if one writes

```text
odd(n) = n / 2^(v_2(n))
```

for the odd part of `n`, then

```text
ω = odd(x + 1) / 3^(v_3(odd(x + 1))),
d = v_2(x + 1) + v_3(odd(x + 1)).
```

Thus the transform `X -> R` is many-to-one: distinct odd integers may determine the same reduced state.

## 5.4. Structural Exit Map `R -> X_exit`

This is the first genuinely dynamical transform in the formalism.

**Domain.** Reduced structural states `(ω,d)`.

**Codomain.** Odd positive integers `x_exit`.

**Formula.** Given `(ω,d)`, define

```text
A = 3^d ω - 1,
s = v_2(A),
x_exit = A / 2^s.
```

Equivalently,

```text
x_exit(ω,d) = (3^d ω - 1) / 2^(v_2(3^d ω - 1)).
```

This is the deterministic odd exit associated with the reduced state `(ω,d)`.

Unlike the transforms `X <-> B`, this is not a bidirectional change of coordinates. It is a forward structural map: a reduced state determines its structural exit, but the same odd value may occur as the exit of different structural cascades.

## 5.5. Transform `X_exit -> R`: Exit to Next Reduced State

Once the odd exit is formed, it may be reduced again exactly as any other odd integer.

**Domain.** Odd positive integers `x_exit`.

**Codomain.** Reduced structural states `(ω_+,d_+)`.

**Formula.** Given `x_exit`, define

```text
m_+ = v_2(x_exit + 1),
u_+ = (x_exit + 1) / 2^(m_+),
a_+ = v_3(u_+),
ω_+ = u_+ / 3^(a_+),
d_+ = m_+ + a_+.
```

Then

```text
R(x_exit) = (ω_+,d_+).
```

Equivalently,

```text
ω_+ = odd(x_exit + 1) / 3^(v_3(odd(x_exit + 1))),
d_+ = v_2(x_exit + 1) + v_3(odd(x_exit + 1)).
```

This is not a new reduction rule; it is the same transform `R` applied to the odd exit.

## 5.6. Combined Structural Map on Reduced States

Combining Sections 5.4 and 5.5 gives the reduced self-map.

**Domain.** Reduced structural states `(ω,d)`.

**Codomain.** Reduced structural states `(ω_+,d_+)`.

**Formula.** The reduced map is the composition

```text
(ω,d) -> x_exit(ω,d) -> R(x_exit(ω,d)).
```

That is,

```text
F(ω,d) = R(x_exit(ω,d))
       = R((3^d ω - 1) / 2^(v_2(3^d ω - 1))).
```

This is the intrinsic endomorphism on reduced states.

The transform should be understood asymmetrically:

- `x` and `(u,m)` are exact equivalent representations.
- `(u,m)` and `x` both reduce many-to-one to `(ω,d)`.
- `(ω,d)` determines `x_exit` uniquely.
- `x_exit` then determines the next reduced state uniquely by reduction.
- But `x_exit` does not in general determine a unique predecessor reduced state.

Thus the reduced formalism consists of exact coordinate maps on the entry side, followed by a genuinely forward structural transition on reduced states.

To make the induced map more explicit, define

```text
A := 3^d ω - 1,
s := v_2(A),
C := A + 2^s.
```

Since

```text
x_exit = A / 2^s,
```

we have

```text
x_exit + 1 = A / 2^s + 1
           = (A + 2^s) / 2^s
           = C / 2^s.
```

The next entry valuation is therefore

```text
m_+ = v_2(x_exit + 1)
    = v_2(C / 2^s)
    = v_2(C) - s.
```

The next odd entry seed is

```text
u_+ = (x_exit + 1) / 2^m_+
    = (C / 2^s) / 2^(v_2(C) - s)
    = C / 2^(v_2(C)).
```

So `u_+` is exactly the odd part of `C`.

Now reduce `u_+` by its 3-adic valuation:

```text
a_+ = v_3(u_+)
    = v_3(C),
```

since dividing by a power of 2 does not affect `v_3`.

Hence

```text
ω_+ = u_+ / 3^a_+
    = C / (2^(v_2(C)) 3^(v_3(C))),
```

and

```text
d_+ = m_+ + a_+
    = v_2(C) - s + v_3(C).
```

Substituting back gives the explicit form of the induced reduced map:

```text
A = 3^d ω - 1,
s = v_2(3^d ω - 1),
C = 3^d ω - 1 + 2^(v_2(3^d ω - 1)),
```

```text
ω_+ = C / (2^(v_2(C)) 3^(v_3(C))),
d_+ = v_2(C) - v_2(3^d ω - 1) + v_3(C).
```

Equivalently,

```text
F(ω,d) = ( C / (2^(v_2(C)) 3^(v_3(C))),
           v_2(C) - v_2(3^d ω - 1) + v_3(C) )
```

with

```text
C = 3^d ω - 1 + 2^(v_2(3^d ω - 1)).
```

So the next reduced state is governed entirely by the valuation profile of the single derived quantity `C`, together with the initial 2-adic valuation `v_2(3^d ω - 1)`.

This isolates the main arithmetic bottleneck in the reduced dynamics: understanding the interaction between

```text
v_2(3^d ω - 1)
```

and

```text
v_2(C), v_3(C),
where C = 3^d ω - 1 + 2^(v_2(3^d ω - 1)).
```

# 6. Determinism of Extended Valuation Blocks

This section establishes the exact algebraic behavior of an extended valuation block. The key point is that when an odd value is written in the form

```text
x = 2^m 3^a ω - 1,
```

with `m >= 1`, `a >= 0`, and `ω` odd with `3` not dividing `ω`, the next odd iterate preserves the same shape while decreasing the `2`-adic exponent by one and increasing the `3`-adic exponent by one. This is the mechanism underlying the deterministic block structure.

## 6.1. One-Step Preservation

Let

```text
x = 2^m 3^a ω - 1,
```

where `m >= 1`, `a >= 0`, and `ω` is odd with `3` not dividing `ω`. Then the next odd iterate of `x` is

```text
T_{odd}(x) = (3x + 1) / 2.
```

Indeed,

```text
3x + 1 = 3(2^m 3^a ω - 1) + 1 = 2^m 3^(a+1) ω - 2 = 2(2^(m-1) 3^(a+1) ω - 1).
```

Therefore

```text
T_{odd}(x) = (3x + 1) / 2 = 2^(m-1) 3^(a+1) ω - 1.
```

Thus the same structural form is preserved under one odd step, with

```text
m -> m - 1, a -> a + 1, ω -> ω.
```

In particular, exactly one factor of `2` is removed at this stage.

## 6.2. Deterministic Drift Along the Block

Iterating the one-step preservation identity yields the deterministic evolution of the entire block.

**Lemma 6.2.1.** Let

```text
x_0 = 2^m 3^a ω - 1,
```

with `m >= 1`, `a >= 0`, and `ω` odd with `3` not dividing `ω`. For each integer `j` with `0 <= j <= m - 1`, define `x_j` by repeated application of the odd-step map. Then

```text
x_j + 1 = 2^(m-j) 3^(a+j) ω.
```

Equivalently,

```text
x_j = 2^(m-j) 3^(a+j) ω - 1.
```

**Proof.** The case `j = 0` is immediate from the definition of `x_0`. If the formula holds for some `j < m - 1`, then

```text
x_j = 2^(m-j) 3^(a+j) ω - 1,
```

so by the one-step preservation identity,

```text
x_(j+1) = 2^(m-j-1) 3^(a+j+1) ω - 1.
```

This is exactly the required formula with `j` replaced by `j + 1`. The result follows by induction.

## 6.3. Endpoint of the Deterministic Block

At the final stage of the deterministic block, taking `j = m - 1` gives

```text
x_(m-1) + 1 = 2 · 3^(a+m-1) ω,
```

so

```text
x_(m-1) = 2 · 3^(a+m-1) ω - 1.
```

Applying one further odd step gives

```text
3x_(m-1) + 1 = 2(3^(a+m) ω - 1).
```

Thus the odd exit of the block is obtained by dividing

```text
3^(a+m) ω - 1
```

by its full `2`-adic valuation.

## 6.4. Interpretation

An extended valuation block therefore evolves in a completely rigid way up to its odd exit: each deterministic odd-to-odd step replaces

```text
x = 2^m 3^a ω - 1
```

by

```text
T_{odd}(x) = 2^(m-1) 3^(a+1) ω - 1,
```

so one factor of `2` is removed from `x + 1`, one factor of `3` is gained, and the structural odd core `ω` remains unchanged.

This is why the entire block can be compressed exactly and why the quantity

```text
3^(a+m) ω - 1
```

naturally appears as the structural numerator governing the transition to the next block. Hence the term BlockEntry.

Because BlockEntry coordinates are attached to odd values `x = 2^m u - 1`, one necessarily has `x + 1` even, so `m = v_2(x + 1) >= 1`. Thus every BlockEntry begins with at least one forced halving, while the case `m = 0` does not occur in the odd BlockEntry formalism.

# 7. Construction of the Reduced Structural Step

Section 6 showed that an extended valuation block evolves deterministically up to its odd exit. The purpose of this section is to derive the intrinsic reduced map from BlockEntry data. The BlockEntry formalism is still the natural route for obtaining the construction, but it now serves primarily as the scaffolding from which the reduced endomorphism is extracted.

## 7.1. From BlockEntry Data to the Structural Numerator

Start with a BlockEntry `(u,m)`, and write

```text
u = 3^a ω,
```

where `a = v_3(u)` and `3` does not divide `ω`. Then the corresponding odd block-entry value is

```text
x = 2^m u - 1 = 2^m 3^a ω - 1.
```

Applying Section 6 shows that the deterministic block evolves up to its endpoint according to the rigid drift formula, and that its odd exit is governed by the numerator

```text
3^(m+a) ω - 1.
```

Define the reduced structural depth by

```text
d = m + a.
```

With this notation, the structural numerator becomes

```text
A = 3^d ω - 1.
```

Thus the BlockEntry data determine the structural numerator entirely through the reduced variables `(ω,d)`. This is the key step in the derivation: the block-level evolution first expressed in `(u,m)` collapses to an arithmetic object depending only on the reduced state.

It is worth noting that the deterministic block evolution preserves the sum `m + a`: each odd-to-odd step decreases `m` by one and increases `a` by one. The reduced parameter `d` is exactly this preserved block-level invariant.

## 7.2. The Structural Step on BlockEntry Coordinates

One may therefore define the structural step `E` on BlockEntry coordinates as the intermediate construction from which the intrinsic reduced map is obtained.

Given `(u,m)`:

1. write `u = 3^a ω` with `a = v_3(u)` and `3` not dividing `ω`,
2. define the reduced structural depth `d = m + a`,
3. form the structural numerator `A = 3^d ω - 1`,
4. let `s = v_2(A)`,
5. define the odd exit `x_exit = A / 2^s`, which is odd by construction, since `s = v_2(A)` removes the full `2`-adic valuation of `A`,
6. define the next-entry depth `m_+ = v_2(x_exit + 1)`,
7. define the next odd seed `u_+ = (x_exit + 1) / 2^(m_+)`.

The resulting next BlockEntry is

```text
E(u,m) = (u_+, m_+).
```

Thus a full deterministic block is compressed into a single transition from one BlockEntry to the next. This construction remains exact and useful, but its main role is now to provide the derivation route to the intrinsic reduced map on `(ω,d)`.

## 7.3. Passage to Reduced Structural States

Applying the projection `R` to the output of the structural step produces the corresponding reduced state. That is, if

```text
E(u,m) = (u_+, m_+),
```

then the next reduced structural state is obtained from

```text
R(u_+, m_+) = (ω_+, d_+),
```

where `u_+ = 3^(a_+) ω_+` with `3` not dividing `ω_+` and

```text
d_+ = m_+ + a_+.
```

Equivalently, since every odd integer determines a unique BlockEntry and hence a unique reduced state, the deterministic odd exit `x_exit` associated with `(ω,d)` determines the next reduced state directly by

```text
F(ω,d) = R(x_exit(ω,d)).
```

As noted in Section 5.6, `x_exit` is not another representative of the original reduced state `(ω,d)`, but the deterministic odd output of the structural step. From `x_exit` one constructs the next BlockEntry `(u_+,m_+)`, and hence the next reduced state `(ω_+,d_+)`.

This gives the candidate reduced transition associated with the original BlockEntry.

## 7.4. Interpretation

The structural step isolates the entire effect of one deterministic block in a single arithmetic object,

```text
A = 3^d ω - 1.
```

The quantity `s = v_2(A)` measures the length of the `2`-adic cascade at the block exit, while the resulting odd value `x_exit` determines the entry depth and odd seed of the next block. Originally this construction is derived through BlockEntry coordinates, but the outcome is an intrinsic reduced map on the state space itself:

```text
F(ω,d) = R(x_exit(ω,d)).
```

In this way, the internal drift proved in Section 6 becomes not merely a block-to-block rule in auxiliary coordinates, but a self-map on reduced states expressed directly through the reduced variables `(ω,d)`.

The next section shows that this construction depends only on the reduced state `(ω,d)`, and not on the particular BlockEntry representative chosen.

# 8. Well-definedness of the Reduced Map

The central formula of the reduced formalism is

```text
F(ω,d) = R(x_exit(ω,d))
       = R((3^d ω - 1) / 2^(v_2(3^d ω - 1))).
```

This exhibits the reduced dynamics as an intrinsic endomorphism of the reduced state space. The purpose of the present section is to justify that formula from the BlockEntry construction by proving that the reduced transition depends only on the reduced state `(ω,d)`, and not on the particular BlockEntry representative chosen.

Section 7 constructed the structural step on BlockEntry coordinates and showed how a corresponding reduced transition is obtained by projection. The purpose of this section is to prove that this reduced transition depends only on the reduced state `(ω,d)`, and not on the particular BlockEntry representative chosen. In other words, the reduced map is well-defined.

## 8.1. Representative-Independence

For a fixed reduced structural state `(ω,d)`, the BlockEntry representatives are precisely those pairs of the form

```text
(u,m) = (3^r ω, d - r),
```

where `0 <= r <= d - 1`. Indeed, if `R(u,m) = (ω,d)`, then writing `u = 3^a ω` with `3` not dividing `ω` gives `d = m + a`, so necessarily `u = 3^a ω` and `m = d - a`. Conversely, every such pair projects to the same reduced state `(ω,d)`.

Here `r` indexes the different BlockEntry representatives of the same reduced state. Increasing `r` shifts one unit of the total depth `d` from the entry-depth parameter `m` into the `3`-adic content of `u`, without changing the reduced state itself. Thus `r` measures movement within a representative family, not dynamical time evolution.

Thus, if two BlockEntry coordinates `(u,m)` and `(u',m')` satisfy

```text
R(u,m) = R(u',m') = (ω,d),
```

then they belong to the same representative family and may be written as

```text
(u,m) = (3^a ω, d - a), (u',m') = (3^(a') ω, d - a'),
```

for suitable integers `a,a' >= 0`.

For every such representative, the structural numerator is the same:

```text
3^m u - 1 = 3^(d-a) 3^a ω - 1 = 3^d ω - 1,
```

and likewise,

```text
3^(m') u' - 1 = 3^(d-a') 3^(a') ω - 1 = 3^d ω - 1.
```

Thus the quantity

```text
A = 3^d ω - 1
```

is determined entirely by the reduced state `(ω,d)`, independent of the chosen BlockEntry representative.

## 8.2. Consequences for the Structural Step

Since `A` depends only on `(ω,d)`, the same is true of its `2`-adic valuation

```text
s = v_2(A),
```

and therefore also of the odd exit

```text
x_exit = A / 2^s.
```

From `x_exit`, the next-entry depth

```text
m_+ = v_2(x_exit + 1)
```

and the next odd seed

```text
u_+ = (x_exit + 1) / 2^(m_+)
```

are likewise uniquely determined. Hence the resulting next BlockEntry

```text
E(u,m) = (u_+, m_+),
```

once projected by `R`, always produces the same reduced state regardless of which representative `(u,m)` with `R(u,m) = (ω,d)` was chosen initially.

## 8.3. Main Proposition

**Proposition 8.3.1.** If two BlockEntry coordinates satisfy

```text
R(u,m) = R(u',m'),
```

then

```text
R(E(u,m)) = R(E(u',m')).
```

**Proof.** By Section 7.1, the reduced state `(ω,d)` uniquely determines the structural numerator `A = 3^d ω - 1`. By Section 7.2, `A` uniquely determines `s`, `x_exit`, `m_+`, and `u_+`, and hence determines the projected output reduced state. Therefore the result of applying `E` and then projecting by `R` depends only on `(ω,d)`, not on the representative chosen. This proves the claim.

## 8.4. The Induced Reduced Map

Because the projected output depends only on the reduced state, the induced reduced map `F` is well-defined. Accordingly, one may define

```text
F(ω,d) = R(E(u,m))
```

for any BlockEntry representative `(u,m)` satisfying `R(u,m) = (ω,d)`.

Equivalently, the same map may be written intrinsically in reduced variables as

```text
F(ω,d) = R(x_exit(ω,d))
       = R((3^d ω - 1) / 2^(v_2(3^d ω - 1))).
```

Thus the reduced dynamics close on the reduced state space itself: the next reduced state is determined entirely by the current reduced state, without any residual dependence on a chosen BlockEntry representative.

## 8.5. Interpretation

Sections 6 and 7 compressed a full deterministic block into a single structural step, and Section 8 shows more than mere compatibility with the reduction from exact BlockEntry coordinates to reduced structural states. It shows that the reduced dynamics close on the reduced state space itself. Equivalently, all BlockEntry representatives of the same reduced state produce the same next reduced state, so the reduced formalism supports an intrinsic self-map on pairs `(ω,d)`.

This is why the reduced dynamics may be studied directly on the state space of pairs `(ω,d)`, rather than only through the more detailed coordinates `(u,m)`.

# 9. Proved Structural Properties

With the reduced map now shown to be well-defined, one may ask which arithmetic features genuinely control the reduced dynamics. This section records the properties that follow directly from the structural-step construction and are established exactly. The purpose is to isolate what is already secure before turning later to empirical or conjectural patterns.

## 9.1. The Reduced Block and Its Structural Numerator

The first proposition records the exact internal structure represented by a reduced structural state `(ω,d)`.

**Proposition 9.1.1 (Characterization of a Reduced Block).** Fix a reduced structural state `(ω,d)`. Its BlockEntry representatives are exactly

```text
(u,m) = (3^a ω, d-a),   0 <= a <= d-1.
```

Equivalently, these are indexed by

```text
(m,a) = (d,0), (d-1,1), ..., (1,d-1).
```

The corresponding odd values are

```text
x_a = 2^(d-a) 3^a ω - 1,   0 <= a <= d-1.
```

These form a deterministic odd chain inside the same reduced block, and successive terms satisfy

```text
x_(a+1) = (3x_a + 1)/2.
```

Equivalently, along this chain the quantity `m` decreases by one while the `3`-adic exponent `a` increases by one, so the total depth

```text
d = m + a
```

remains fixed throughout.

In particular, the unique terminal interior position is the state

```text
(m,a) = (1,d-1),
```

and from there the block exits through the common structural numerator

```text
A = 3^d ω - 1.
```

If

```text
s = v_2(3^d ω - 1),
```

then the forced halving cascade has length `s`, and the odd exit is

```text
x_exit = (3^d ω - 1) / 2^s.
```

Thus every BlockEntry representative of the same reduced state shares the same exit law.

**Proof.** By Section 8.1, the BlockEntry representatives of `(ω,d)` are exactly the pairs

```text
(u,m) = (3^a ω, d-a),   0 <= a <= d-1.
```

For each such representative, the corresponding odd value is

```text
x_a = 2^m u - 1 = 2^(d-a) 3^a ω - 1.
```

Applying the deterministic drift law of Section 6.2 to the initial representative

```text
x_0 = 2^d ω - 1
```

shows that repeated odd-to-odd steps produce precisely the chain

```text
x_a = 2^(d-a) 3^a ω - 1,   0 <= a <= d-1,
```

with each step decreasing `m` by one and increasing `a` by one. Hence the interior positions are exactly

```text
(m,a) = (d,0), (d-1,1), ..., (1,d-1),
```

so the unique terminal interior position is the final one,

```text
(m,a) = (1,d-1).
```

Substituting `a = d-1` into the odd value formula gives

```text
x_(d-1) = 2 · 3^(d-1) ω - 1,
```

and one further odd-step numerator is therefore

```text
3x_(d-1) + 1 = 3(2 · 3^(d-1) ω - 1) + 1 = 2(3^d ω - 1).
```

Thus the block exits through the common structural numerator

```text
A = 3^d ω - 1.
```

Writing

```text
s = v_2(A),
```

the forced halving cascade has length `s`, and the odd exit is

```text
x_exit = A / 2^s = (3^d ω - 1)/2^s.
```

This depends only on `(ω,d)`, so every representative of the same reduced state shares the same exit law. ∎

The remaining results of this section now record structural consequences of this characterization and of the reduced-step construction.

In summary, for a reduced structural state `(ω,d)`, the corresponding structural step is governed by the quantity

```text
A = 3^d ω - 1.
```

By Sections 7 and 8, this numerator is determined entirely by the reduced state and is independent of the chosen BlockEntry representative. Its full `2`-adic valuation

```text
s = v_2(A)
```

therefore determines the odd exit

```text
x_exit = A / 2^s,
```

and hence determines the next-entry depth and next odd seed. Thus the reduced transition is governed intrinsically by

```text
F(ω,d) = R((3^d ω - 1) / 2^(v_2(3^d ω - 1))).
```

## 9.2. 2-adic Proximity to -1

The next-entry depth is measured by the `2`-adic proximity of `x_exit` to `-1`.

**Lemma 9.2.1.** For any odd integer `y` and any integer `n >= 1`,

```text
v_2(y + 1) >= n if and only if y ≡ -1 mod 2^n.
```

**Proof.** By definition, `v_2(y + 1) >= n` exactly when `2^n` divides `y + 1`. This is equivalent to `y + 1 ≡ 0 mod 2^n`, or `y ≡ -1 mod 2^n`.

In particular, if `y = x_exit`, then the next-entry depth

```text
m_+ = v_2(x_exit + 1)
```

records exactly how close `x_exit` lies to `-1` in the `2`-adic sense.

Because `x_exit = A / 2^s`, the exit value is the odd part of the structural numerator `A`. Thus `A` and `x_exit` encode the same post-cascade odd content, while the removed factor `2^s` records the full halving depth of the cascade. Accordingly, proximity questions about `x_exit` to `-1` should be read as shifted odd-part information arising after the powers of `2` in `A` have been stripped away.

## 9.3. Parity of `s` Controls 3-gain

A central exact consequence of the reduced formalism is that the parity of `s` determines whether the next odd seed gains a factor of `3`.

**Lemma 9.3.1.** Let

```text
A = 3^d ω - 1,
```

with `s = v_2(A)` and `x_exit = A / 2^s`. Then

```text
3 divides x_exit + 1 if and only if s is even.
```

Equivalently, the next odd seed `u_+` acquires a factor of `3` precisely when `s` is even.

**Proof.** Since `A = 3^d ω - 1`, one has `A ≡ -1 mod 3`. Therefore

```text
x_exit + 1 = A / 2^s + 1 ≡ -2^(-s) + 1 mod 3.
```

Modulo `3`, one has `2 ≡ -1`, so `2^(-s) ≡ (-1)^s mod 3`. Hence

```text
x_exit + 1 ≡ 1 - (-1)^s mod 3.
```

If `s` is even, this is congruent to `0 mod 3`. If `s` is odd, it is congruent to `2 mod 3`. This proves the claim.

Thus the parity of the `2`-adic cascade at the block exit determines whether the next stage gains additional `3`-adic content.

This matters because a `3`-gain changes how the next block is represented at the reduced level. When `3` divides `x_exit + 1`, the next odd seed `u_+` carries additional `3`-adic content, so more of the next block-entry data is absorbed into `a_+` rather than remaining in the structural odd core `ω_+`. Equivalently, a `3`-gain affects how the next state decomposes into its reduced coordinates, and therefore influences the future evolution of both `ω` and `d`. In this sense, the parity of `s` does not merely record a congruence condition: it controls whether the next reduced state undergoes an additional structural absorption of a factor of `3`.

## 9.4. Special Case: `ω = 1`

The family `ω = 1` provides a fully explicit test case for the reduced dynamics. Here

```text
A = 3^d - 1.
```

Its `2`-adic valuation is given by the standard formula

```text
v_2(3^n - 1) =
1, if n is odd,
2 + v_2(n), if n is even.
```

Applying this with `n = d` gives the following.

**Proposition 9.4.1.** If `ω = 1`, then

```text
s = v_2(3^d - 1)
```

satisfies

```text
s = 1 when d is odd,
s = 2 + v_2(d) when d is even.
```

In particular, for `ω = 1` the parity and size of `s` may be read off directly from `d`.

This family serves as a useful reference model because the reduced step is governed by an explicit valuation law rather than by a general mixed parameter pair `(ω,d)`.

## 9.5. Special Upstream Families of a Fixed Exit Value

Fix an odd exit value `x_exit`. Its admissible upstream predecessors are values of the form

```text
x_S = (x_exit 2^(S+1) - 1) / 3,
```

whenever this is integral.

Here `S` is the structural cascade depth attached to the predecessor family. The adjacent boundary case is `S = 0`, while the genuine cascade regime is `S >= 1`.

The predecessor identity is

```text
3x_S + 1 = x_exit 2^(S+1).
```

Thus the family is upstream rather than representative: the values `x_S` need not lie in the same reduced-state family, and in general they do not.

**Lemma 9.5.1.** Let `x_exit` be an integer. Then

```text
x_S = (x_exit 2^(S+1) - 1) / 3
```

is integral if and only if `3` does not divide `x_exit` and the parity of `S` is determined by the residue of `x_exit mod 3` as follows:

```text
S odd   if x_exit ≡ 1 mod 3,
S even  if x_exit ≡ 2 mod 3.
```

**Proof.** Integrality is equivalent to

```text
x_exit 2^(S+1) ≡ 1 mod 3.
```

If `3` divides `x_exit`, this is impossible. If `x_exit ≡ 1 mod 3`, then one must have `2^(S+1) ≡ 1 mod 3`, which holds exactly when `S` is odd. If `x_exit ≡ 2 mod 3`, then one must have `2^(S+1) ≡ 2 mod 3`, which holds exactly when `S` is even.

**Lemma 9.5.2.** Let

```text
x_S = (x_exit 2^(S+1) - 1) / 3
```

be an admissible upstream predecessor. If `S >= 1`, then the BlockEntry depth of `x_S` is

```text
m_S = v_2(x_S + 1) = 1.
```

Equivalently, `x_S` lies at the terminal interior position of its own reduced block.

**Proof.** Since `x_S` is admissible, it is an integer. From the predecessor formula,

```text
x_S + 1
= (x_exit 2^(S+1) - 1)/3 + 1
= (x_exit 2^(S+1) + 2)/3
= 2 (x_exit 2^S + 1)/3.
```

Because `S >= 1` and `x_exit` is odd, the quantity `x_exit 2^S` is even, so

```text
x_exit 2^S + 1
```

is odd. Hence `(x_exit 2^S + 1)/3` is also odd, since `x_S` is assumed integral. Therefore `x_S + 1` is exactly twice an odd integer, and so

```text
v_2(x_S + 1) = 1.
```

Thus `m_S = 1`. By the deterministic block description of Section 6, BlockEntry depth `m = 1` is exactly the terminal interior position of a reduced block.

**Proposition 9.5.3.** Let `x_exit` be odd with `3` not dividing `x_exit`, and let

```text
x_S = (x_exit 2^(S+1) - 1) / 3
```

be an admissible cascade predecessor with `S >= 1`. Then

```text
m_S = 1,
A_S = x_exit 2^S,
s_S = v_2(x_exit) + S.
```

In particular, since `x_exit` is odd,

```text
s_S = S.
```

**Proof.** By Lemma 9.5.2,

```text
m_S = v_2(x_S + 1) = 1,
```

so

```text
u_S = (x_S + 1)/2.
```

Let `(ω_S,d_S)` be the reduced state associated to `x_S`. Then

```text
d_S = 1 + v_3(u_S),
ω_S = u_S / 3^(v_3(u_S)),
```

hence

```text
3^(d_S) ω_S = 3u_S.
```

Therefore

```text
A_S = 3^(d_S) ω_S - 1
    = 3u_S - 1
    = 3(x_S + 1)/2 - 1
    = (3x_S + 1)/2.
```

Using

```text
3x_S + 1 = x_exit 2^(S+1),
```

one obtains

```text
A_S = x_exit 2^S,
```

and so

```text
s_S = v_2(A_S) = v_2(x_exit) + S.
```

If `x_exit` is odd, this reduces to

```text
s_S = S.
```

This proves the claim.

The only excluded cases are structurally accounted for: exit values divisible by `3` have no odd predecessors, even exit values are collapsed by the EntryBlock formalism, and the boundary case `S = 0` remains within the same reduced-state family.

## 9.6. Every Reduced State Arises from the Fixed-Exit Family of Its Own Exit Value

The fixed-exit predecessor family of Section 9.5 is not merely an external upstream construction. Every reduced structural state appears canonically inside such a family, namely as the terminal interior predecessor attached to its own exit value.

**Proposition 9.6.1.** Let `(ω,d)` be a reduced structural state, and let

```text
A = 3^d ω - 1,
s = v_2(A),
x_exit = A / 2^s.
```

Then the unique terminal interior odd value of the reduced block `(ω,d)` is

```text
x_(d-1) = 2 · 3^(d-1) ω - 1,
```

and this value satisfies

```text
x_(d-1) = (x_exit 2^(s+1) - 1)/3.
```

Equivalently, `x_(d-1)` is exactly the `S = s` member of the fixed-exit predecessor family

```text
x_S = (x_exit 2^(S+1) - 1)/3.
```

Thus every reduced structural state is represented by the terminal interior predecessor in the fixed-exit family of its own exit value.

**Proof.** By Proposition 9.1.1, the unique terminal interior position of the reduced block `(ω,d)` is

```text
x_(d-1) = 2 · 3^(d-1) ω - 1.
```

Applying one further odd step gives

```text
3x_(d-1) + 1
= 3(2 · 3^(d-1) ω - 1) + 1
= 2(3^d ω - 1).
```

Since

```text
A = 3^d ω - 1
```

and

```text
A = x_exit 2^s,
```

it follows that

```text
3x_(d-1) + 1 = 2A = x_exit 2^(s+1).
```

Solving for `x_(d-1)` yields

```text
x_(d-1) = (x_exit 2^(s+1) - 1)/3.
```

But this is exactly the fixed-exit predecessor formula of Section 9.5 with parameter `S = s`:

```text
x_S = (x_exit 2^(S+1) - 1)/3.
```

Hence

```text
x_(d-1) = x_s.
```

Therefore the reduced state `(ω,d)` is recovered canonically as the reduction of the `S = s` predecessor in the fixed-exit family attached to its own exit value. ∎

### 9.6.2. Interpretation

This identifies the correct global role of the fixed-exit family. Section 9.5 does not classify all upstream predecessors of a fixed odd value into a single reduced-state family. Rather, for each reduced state `(ω,d)`, its own terminal interior representative appears as the distinguished member indexed by

```text
S = s = v_2(3^d ω - 1)
```

inside the fixed-exit family over its associated exit value `x_exit`.

Equivalently, every reduced state determines a canonical pair `(x_exit,s)` satisfying

```text
3^d ω - 1 = x_exit 2^s,
```

and its terminal interior representative is recovered from that pair by

```text
x_(d-1) = (x_exit 2^(s+1) - 1)/3.
```

So the reduced state may be located canonically inside a fixed-exit predecessor family, not as an arbitrary member, but precisely as its terminal interior predecessor.

### 9.6.3. Scope of the Result

This is a structural classification result, not yet a new explicit algorithm for the reduced map. It shows that every reduced state admits a canonical description through its own exit data `(x_exit,s)`, but obtaining that pair from `(ω,d)` still requires computing

```text
s = v_2(3^d ω - 1).
```

Accordingly, the theorem gives a global normal form for reduced states through their terminal interior representatives, while leaving the main valuation bottleneck unchanged.

## 9.7. What the Reduced Dynamics No Longer Need

For the purpose of computing the next reduced state, the separate values of the BlockEntry parameters `a = v_3(u)` and `m = v_2(x+1)` do not matter once `ω` and `d = m + a` are fixed. Section 7 showed that different representatives in the same family

```text
(u,m) = (3^r ω, d - r)
```

all produce the same reduced output.

Accordingly, the reduced dynamics do not depend on the individual decomposition of `d` into a `3`-adic contribution `a` and an entry-depth contribution `m`. What remains active is the reduced pair `(ω,d)` together with the valuation behavior of the associated structural numerator

```text
A = 3^d ω - 1.
```

The new upstream family above shows the complementary phenomenon: even when different predecessors lie outside the same representative family, their induced valuation structure may still obey rigid exact laws. Thus the reduction discards the internal split of `d`, but it does not erase the arithmetic constraints carried by `A`.

This identifies the exact level at which information has been compressed: the discarded distinctions do not affect the next reduced state, but the arithmetic of `A` still does.

## 9.8. The Convergence Translation

The note repeatedly disclaims resolving the Collatz conjecture. This section records what resolution would mean, exactly, in the note's own language. Everything here is an immediate consequence of results already proved; it is stated explicitly because it anchors the entire program: the reduced system is not merely an interesting quotient of the Collatz dynamics — it is a faithful arena for the conjecture itself.

One caution against misreading, before the statements. The theorems below are equivalences. They prove that the conjecture and its reduced reformulation stand or fall together; they do not prove that either holds. After this section, "every `F`-orbit reaches `(1,1)`" is exactly as open as the Collatz conjecture — that is the point. What the equivalence buys is bidirectional transfer (a proof or a counterexample at either layer settles the other) and the assurance that the reduction, despite being many-to-one, loses nothing that the conjecture depends on.

Throughout, `T` denotes the odd-to-odd Collatz map `x ↦ (3x+1)/2^(v_2(3x+1))` on positive odd integers, and the trivial cycle is the fixed point `T(1) = 1`.

**Proposition 9.8.1 (the trivial state).** The state `(ω, d) = (1, 1)` is a fixed point of `F`, and its fiber under the projection `R` is exactly `{1}`.

**Proof.** For `(1,1)`: `A = 3·1 - 1 = 2`, `s = 1`, `x_exit = 1`, and `R(1) = (1,1)` since `1 + 1 = 2^1·1`. So `F(1,1) = R(x_exit) = (1,1)`. For the fiber: by Proposition `9.1.1`, the odd representatives of `(1,1)` are `x_a = 2^(1-a)·3^a·1 - 1` for `0 <= a <= 0`, that is, `x = 1` alone. ∎

**Lemma 9.8.2 (orbit projection).** Let `x` be an odd positive integer with `R(x) = (ω, d)`. Then the odd values of the `T`-orbit of `x` are tiled by the representative chains (Proposition `9.1.1`) of the reduced states `F^t(ω, d)`, `t >= 0`; in particular, the sequence of reduced states visited by the `T`-orbit of `x` is exactly the `F`-orbit of `R(x)`. Moreover, every valid reduced state `(ω, d)` is realized by an odd integer, namely `x = 2^d·ω - 1`.

**Proof.** The first statement is the content of Sections `6`–`8`: the block from any representative of `(ω, d)` runs deterministically to the exit `x_exit(ω, d) = A/2^s` (Section `6`), the exit is the entry of the next block, and the projected next state is `F(ω, d)` independently of the representative (Proposition `8.3.1`, Section `8.4`). The realization statement is the representative `a = 0` of Proposition `9.1.1`. ∎

**Theorem 9.8.3 (convergence translation).** The Collatz conjecture holds if and only if every `F`-orbit from a valid reduced state reaches the fixed point `(1, 1)`.

**Proof.** Suppose the conjecture holds, and let `(ω, d)` be a valid reduced state. Its representative `x = 2^d·ω - 1` has a `T`-orbit reaching `1`; the reduced state of the odd value `1` is `(1,1)`, so by Lemma `9.8.2` the `F`-orbit of `(ω, d)` reaches `(1,1)`.

Conversely, suppose every `F`-orbit reaches `(1,1)`, and let `x` be an odd positive integer. The `F`-orbit of `R(x)` reaches `(1,1)`, so by Lemma `9.8.2` the `T`-orbit of `x` visits an odd value in the `R`-fiber of `(1,1)`. By Proposition `9.8.1` that fiber is `{1}`. ∎

**Theorem 9.8.4 (cycle correspondence).** Projection by `R` is a bijection between nontrivial cycles of `T` and cycles of `F` other than the fixed point `{(1,1)}`.

**Proof.** A nontrivial `T`-cycle is a finite set of odd values, tiled by blocks; its sequence of reduced states is periodic, hence an `F`-cycle (Lemma `9.8.2`), and it avoids `(1,1)` because the cycle avoids the value `1` and the fiber of `(1,1)` is `{1}`.

Conversely, let `S_0 -> S_1 -> ... -> S_(p-1) -> S_0` be an `F`-cycle avoiding `(1,1)`. The block entries `e_t = x_exit(S_(t-1))` are deterministic functions of the states, so the sequence `(e_t)` is periodic, and consecutive entries are joined by genuine `T`-iteration (Lemma `9.8.2`). Hence `e_0` is a `T`-periodic odd value, and its cycle is nontrivial since no `e_t` equals `1` (else `S_t = R(1) = (1,1)`).

The two constructions are mutually inverse: the entries of a `T`-cycle are determined by its state sequence (each block entry is the exit of the previous state), and the state sequence of the constructed `T`-cycle is the given `F`-cycle. ∎

**Corollary 9.8.5 (trichotomy).** Every `F`-orbit satisfies exactly one of:

1. it reaches the fixed point `(1, 1)`;
2. it is eventually periodic without reaching `(1,1)` — equivalently, the corresponding `T`-orbits fall into a nontrivial cycle;
3. the exit sizes `x_exit(F^t(ω,d))` are unbounded — equivalently, the corresponding `T`-orbits are divergent.

The Collatz conjecture is the assertion that case `1` always occurs.

**Remark (numerical confirmation of the bookkeeping).** The fiber statement was checked by exhaustive search over odd `x < 3·10^6` (only `x = 1` projects to `(1,1)`); the orbit-projection lemma was checked along `300` random orbits, whose block exits track the `F`-orbit exactly and reach `x = 1` precisely when the reduced orbit reaches `(1,1)`; and no interior odd value of any block `(u, m)` with `u < 400`, `m <= 11` equals `1`.

**Remark (anchor form).** In the coordinates of `11.8.5.6`, Theorem `9.8.3` says the conjecture is the statement that orbits drive `(d - M(ω), M(ω))` to `(1, 0)`, and Theorem `9.8.4` says a nontrivial cycle is a periodic anchor-increment sequence — a finite closed walk in `Z_2` whose increments `ΔM_t`, each a deterministic function of `C_t`, sum to `0`. Cycle exclusion is thus an exact-rigidity statement about such closed walks, which is precisely the regime where the effective tools of `11.8.3.11` operate. The cycle frame built on this correspondence is cycles.md §12. The rigidity reading of the closed anchor walk is charted at bridge.md 16.4.4.

