# 1. Purpose and Scope

This document develops a reduced structural formalism for the Collatz map by factoring out deterministic valuation behavior into extended valuation blocks and studying the induced dynamics on reduced states `(ω,d)`. The objective is not to analyze the iteration step-by-step, but to isolate the arithmetic structure that remains once these deterministic block effects are compressed. In particular, the reduced formalism ultimately yields a self-map on reduced states, so the reduced state space is not merely a quotient interpretation of the dynamics but a dynamical system in its own right.

The central hope of this framework is that the reduced dynamics may reveal a more connected and intelligible state structure than is visible in the raw iteration. In particular, the goal is to understand how reduced states relate to one another, whether transitions admit further reduction, and whether the induced map exposes structural regularities that are obscured in the standard formulation.

No claim is made here regarding convergence or a resolution of the Collatz conjecture. The purpose of this note is only to define the reduced formalism clearly, establish its exact algebraic properties, and identify which additional patterns appear to merit further investigation.

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

The next proposition records the exact internal structure represented by a reduced structural state `(ω,d)`.

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

## 9.1. The Structural Numerator Governs the Step

For a reduced structural state `(ω,d)`, the corresponding structural step is governed by the quantity

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

**Proposition 9.6.1.1** Let `(ω,d)` be a reduced structural state, and let

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

**Proof.** By Proposition 9.0.1, the unique terminal interior position of the reduced block `(ω,d)` is

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

## 9.6.1. Interpretation

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

## 9.6.2. Scope of the Result

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

# 10. Empirical Observations

The detailed empirical observations that motivated the Route A synthesis — including family-by-family tower analysis, halo geometry, and the primary-branch congruence picture — have been moved to Appendix A (Sections A.4–A.6). The formal lifting-branch mechanism is developed in Section `11.8.1`.

# 11. Conjectures and Open Questions

The previous sections now establish the reduced formalism at a stronger structural level than in earlier drafts. The reduced map is well-defined on structural states `(ω,d)`, the block-exit law is explicit, the role of the structural numerator

```text
A = 3^d ω - 1
```

has been isolated, and the internal representative structure of each reduced block has been clarified. In particular, the terminal interior predecessor of a reduced block is now identified canonically, and every reduced state is represented inside the fixed-exit family of its own exit value.

The observations and examples that led to these conclusions are recorded in Appendix A; they should be read as exploratory context rather than proved claims.

Accordingly, the main open problems are no longer foundational questions about whether the reduced formalism is coherent. The remaining questions are now more focused: how much of the arithmetic complexity of the reduced map can be classified, compressed, or controlled?

## 11.1. The Main Arithmetic Bottleneck: Controlling `s = v_2(3^d ω - 1)`

The quantity

```text
s = v_2(3^d ω - 1)
```

is the central arithmetic input governing the block exit. It determines the length of the forced `2`-adic cascade at exit, and through its parity it determines whether the next odd seed gains a factor of `3`.

Thus, although the reduced map is now structurally explicit, much of its unresolved behavior has been concentrated into the valuation of the single quantity `A = 3^d ω - 1`.

Open questions include:

* For fixed `ω`, what regularity does `s` exhibit as `d` varies?
* For fixed `d`, how is `s` organized by residue classes of `ω`?
* Are there natural families in which the parity of `s` is periodic, eventually periodic, or rigidly constrained?
* Which aspects of the behavior of `s` follow from standard `2`-adic lifting phenomena, and which are specific to the present reduced formulation?

The last question now has a calibrated answer (developed in `11.8.3.6` and `11.8.3.11`): the first valuation layer is elementary lifting-the-exponent; the family-dependent structure is the `2`-adic logarithm `N(ω) = -log ω / log 9`, with unconditional polylogarithmic bounds on `s` imported from `p`-adic Baker theory; and the residual content — the fine digit statistics of those logarithms — lies beyond current theory and is in no way specific to the Collatz formulation.

A deeper understanding of this valuation appears to be the main bottleneck in any further classification of the reduced dynamics.

## 11.2. Explicit Classification of the Reduced Transition

The reduced map `F` now admits a clean intrinsic description:

```text
F(ω,d) = R(x_exit(ω,d)).
```

The remaining question is whether the transition

```text
(ω,d) ↦ (ω_+,d_+)
```

can be described more directly, without repeatedly unpacking the full sequence of valuation and reduction steps.

More specifically:

* Can `d_+ - d` be expressed directly in terms of a small arithmetic package attached to `A = 3^d ω - 1`?
* Can `ω_+` be described by a more transparent residue law?
* Can the combined step from `(ω,d)` to `(ω_+,d_+)` be decomposed into a small number of sharply classified cases?
* Is there a direct structural formula for the next reduced state that avoids most of the nested bookkeeping presently needed?

The reduced formalism has already compressed the ordinary Collatz step substantially. The next natural question is whether the reduced transition itself admits a second-level classification.

## 11.3. Distribution and Dynamical Role of `3`-gain

Section 9 proved that the parity of `s` controls whether the next odd seed gains a factor of `3`. In that sense, the immediate mechanism of `3`-gain is already understood.

What remains open is the broader dynamical role of repeated `3`-gain events inside the reduced system.

Questions here include:

* How frequently do `3`-gain events occur along reduced trajectories?
* Can the occurrence of `3`-gain be predicted efficiently from bounded residue data?
* To what extent does repeated `3`-gain influence long-term movement through the reduced state space?
* Do repeated `3`-gain patterns explain any of the visible clustering, locking, or average-drift effects seen empirically?

The local trigger is now explicit; the unresolved issue is the global arithmetic and dynamical significance of that trigger.

## 11.4. Canonical Normal Forms for Reduced States

The current reduced state space is parameterized by pairs `(ω,d)`. This description is now mathematically justified, but the strengthened structural results suggest that other equivalent normal forms may also be natural.

In particular, each reduced block now comes equipped with at least three closely related descriptions:

* the reduced state `(ω,d)`,
* its canonical terminal interior predecessor,
* and its exit data, namely the pair consisting of the block exit value and the associated valuation.

This raises a new structural question: which of these descriptions is most natural for analysis?

Open questions include:

* Is `(ω,d)` the best coordinate system for the reduced dynamics, or merely the most convenient one discovered so far?
* Can the canonical terminal interior predecessor be used as a more natural representative of the reduced block?
* Is there a useful normal form based on exit data such as `(x_exit,s)`?
* Are there equivalent state descriptions in which the reduced transition becomes simpler or more symmetric?

The issue is no longer whether the reduced state is well-defined; it is whether the present coordinates are the most informative ones.

## 11.5. Reduced Predecessor Structure and Inversion

The strengthened fixed-exit analysis now sharply separates two notions that were easier to conflate in earlier drafts:

* internal representatives of a single reduced block,
* and genuinely upstream predecessors belonging to special fixed-exit families.

This suggests a natural inversion problem for the reduced system.

Questions include:

* Given a reduced state, how can all reduced-level predecessors be classified?
* Given a fixed odd exit value `x_exit`, which reduced states map to it as their deterministic block exit?
* How are upstream fixed-exit families organized arithmetically?
* Is there a clean reduced analogue of the predecessor-tree viewpoint from classical Collatz analysis?

The present note now identifies one canonical representative inside the fixed-exit family of a state’s own exit value. A natural next step is to understand the full upstream geometry of these families.

## 11.6. Finite-State Shadows and Residue Control

The empirical observations suggest that residue data may organize substantial portions of the visible reduced dynamics. This raises the question of whether some part of the system admits a meaningful finite-state shadow.

Possible formulations include:

* Is there a bounded residue system that predicts the parity of `s` in large families?
* Can one isolate a finite collection of residue variables that explains most observed `3`-gain behavior?
* Is there a finite-state approximation that predicts the coarse direction of the reduced transition, even when it does not predict the exact next state?
* Does the full arithmetic complexity of the system inevitably reappear once deeper `2`-adic data are tracked?

The strongest possible outcome would be a finite residue mechanism that controls large regions of the reduced state space. Even a weaker coarse-state model would already be significant.

## 11.7. Relationship to Classical Collatz Formulations

The reduced formalism reorganizes the ordinary Collatz dynamics by compressing deterministic block structure and then quotienting by internal representative families. An important long-term question is how this framework relates to more classical odd-to-odd or accelerated Collatz maps.

In particular:

* Does the reduced map `F` recover known structures in a disguised form?
* Does the quotient by representative families reveal genuinely new organization not visible in the standard odd map?
* Can predecessor-tree viewpoints from classical Collatz analysis be translated into the language of fixed-exit families?
* Can existing results about valuations, residue graphs, or accelerated dynamics be reinterpreted more cleanly inside this reduced setting?

This comparison matters for two reasons. First, it may show that some parts of the reduced formalism are already latent in classical formulations. Second, it may clarify which features of the present framework are genuinely new and therefore deserve further study.

One concrete point of contact is now established (`11.8.3.11`): the valuation `s` on the lifting branch is a linear form in two `2`-adic logarithms, and the effective theory that bounds it — `p`-adic Baker theory together with lattice-reduction methods — is the same machinery underlying the known lower bounds on nontrivial Collatz cycle lengths (Steiner; Simons–de Weger). The reduced formalism and the classical cycle analyses therefore terminate on common arithmetic ground, which calibrates both the novelty and the expected difficulty of the remaining questions.

## 11.8. A Guarded Route A Program

The present note has already localized the main unresolved arithmetic difficulty. The reduced transition is intrinsic, and the next state is governed by the structural numerator

```text
A = 3^d ω - 1,
```

its `2`-adic valuation

```text
s = v_2(A),
```

and the derived quantity

```text
C = A + 2^s.
```

Indeed, the reduced map may be written explicitly in terms of these quantities, with

```text
ω_+ = C / (2^(v_2(C)) 3^(v_3(C))),
d_+ = v_2(C) - s + v_3(C).
```

Accordingly, the central issue is no longer whether the reduced state is well-defined, but whether the arithmetic of `A` can be classified more sharply. The main bottleneck remains control of

```text
s = v_2(3^d ω - 1),
```

whose parity already determines whether the next stage gains a factor of `3`. 

A natural next direction is therefore an exact local program, here called **Route A**. Its purpose is not to guess a global law for the full reduced dynamics immediately, but to prove rigorous structural statements on natural infinite families. The basic idea is to begin where the arithmetic is most concentrated, convert valuation results into dynamical statements, and postpone finer classification of the full next state until the main mechanisms are better understood.

### Guardrail Against Residue-Chasing

Because the reduced map is strongly sensitive to valuation structure, it is tempting to pursue increasingly fine residue partitions whenever an observed pattern begins to fail. That approach risks producing an illusion of progress while merely replacing one uncontrolled arithmetic problem with another.

For that reason, the Route A program should be subject to the following guardrail.

A residue-based analysis is pursued only when it yields at least one of the following:

1. an exact theorem on a fixed infinite family,
2. a classification whose modulus is fixed in advance,
3. or a reduction to a standard valuation mechanism rather than an indefinitely refined partition.

By contrast, progressive increases in modulus introduced only to preserve an empirical pattern should be treated as heuristic exploration rather than structural progress.

A second guardrail is that a proposed classification should control at least one of the following genuinely dynamical outputs:

* the parity of `s`,
* the occurrence of `3`-gain,
* or the behavior of `d_+ - d`.

If it does not advance one of these, then it should not be regarded as a central theorem target.

### Stage 1. Valuation Families for `s = v_2(3^d ω - 1)`

The first stage of Route A is to build a bank of exact results for the valuation

```text
s = v_2(3^d ω - 1).
```

The objective here is not a complete global classification. Rather, it is to identify natural infinite families on which `s` can be described exactly, periodically, or through effective bounds.

The most basic theorem targets are:

* criteria for when `v_2(3^d ω - 1) >= k` on fixed families,
* exact or periodic descriptions of the parity of `s`,
* and families in which `s` is rigidly constrained by low-order arithmetic data.

This direction is natural because the reduced formalism has already isolated `s` as the central arithmetic input governing the block exit and because the parity of `s` already has an exact dynamical meaning.

### 11.8.1. Stage 1 entry map: from first-layer classification to lifting-branch congruences

Stage 1 of Route A no longer needs to carry the full historical sequence of family-by-family discovery in the main text. That material remains useful for intuition, but the formal burden is now narrower.

At this stage, two outputs are structurally central:

1. the first-layer classification of the valuation problem by the residue class of `ω (mod 8)`,
2. the exact reformulation of the lifting branch as a congruence problem in the exponent variable for the base `9`.

Worked examples that historically revealed these structures are now collected in Appendix A. The purpose of the present subsection is therefore not to reproduce the discovery path in detail, but to extract the formal entry points needed for the later tower synthesis.

#### 11.8.1.1. Family examples as calibration cases

Several fixed families were important in discovering the Stage 1 structure. In particular:

- the families `ω = 1, 5, 7` showed that the first valuation layer is strongly constrained by low-order residue data,
- the family `ω = 17` suggested that deeper lifting is organized around an anchor rather than by `d` alone,
- and the family `ω = 25` showed that the lifting branch can refine through a clean nested congruence tower.

These examples are now retained in Appendix A as calibration cases and historical references.

#### 11.8.1.2. #TODO: renumber

#### 11.8.1.3. First formal output of Stage 1

The first structural split in the valuation

```text
s = v_2(3^d ω - 1)
```

is controlled by the residue class of `ω (mod 8)`. This does not determine the full value of `s`, but it does determine the first valuation layer and thereby separates the genuinely lifting branch from the non-lifting branches.

#### 11.8.1.4. First-layer residue classification modulo `8`

**Proposition 11.8.1.4.1 (first-layer mod `8` classification).** Let `ω` be odd, and define

```text
A = 3^d ω - 1,
s = v_2(A).
```

Then:

```text
If d is odd,  A ≡ 3ω - 1 (mod 8).
If d is even, A ≡ ω - 1 (mod 8).
```

Consequently:

```text
ω ≡ 1 (mod 8)  =>  s = 1 for odd d, and s >= 3 for even d.
ω ≡ 5 (mod 8)  =>  s = 1 for odd d, and s = 2 for even d.
ω ≡ 7 (mod 8)  =>  s = 2 for odd d, and s = 1 for even d.
ω ≡ 3 (mod 8)  =>  s >= 3 for odd d, and s = 1 for even d.
```

**Proof.** Since `3 ≡ 3 (mod 8)` and `3^2 = 9 ≡ 1 (mod 8)`, the powers of `3` modulo `8` depend only on the parity of `d`:

```text
3^d ≡ 3 (mod 8)   if d is odd,
3^d ≡ 1 (mod 8)   if d is even.
```

Therefore:

* if `d` is odd, then

```text
A = 3^d ω - 1 ≡ 3ω - 1 (mod 8);
```

* if `d` is even, then

```text
A = 3^d ω - 1 ≡ ω - 1 (mod 8).
```

Now examine each odd residue class of `ω (mod 8)`.

If `ω ≡ 1 (mod 8)`, then:

```text
3ω - 1 ≡ 3·1 - 1 ≡ 2 (mod 8),
ω - 1  ≡ 1 - 1 ≡ 0 (mod 8).
```

Hence `A ≡ 2 (mod 8)` for odd `d`, so `s = 1`; and `A ≡ 0 (mod 8)` for even `d`, so `s >= 3`.

If `ω ≡ 5 (mod 8)`, then:

```text
3ω - 1 ≡ 3·5 - 1 ≡ 14 ≡ 6 (mod 8),
ω - 1  ≡ 5 - 1 ≡ 4 (mod 8).
```

Hence `A ≡ 6 (mod 8)` for odd `d`, so `s = 1`; and `A ≡ 4 (mod 8)` for even `d`, so `s = 2`.

If `ω ≡ 7 (mod 8)`, then:

```text
3ω - 1 ≡ 3·7 - 1 ≡ 20 ≡ 4 (mod 8),
ω - 1  ≡ 7 - 1 ≡ 6 (mod 8).
```

Hence `A ≡ 4 (mod 8)` for odd `d`, so `s = 2`; and `A ≡ 6 (mod 8)` for even `d`, so `s = 1`.

If `ω ≡ 3 (mod 8)`, then:

```text
3ω - 1 ≡ 3·3 - 1 ≡ 8 ≡ 0 (mod 8),
ω - 1  ≡ 3 - 1 ≡ 2 (mod 8).
```

Hence `A ≡ 0 (mod 8)` for odd `d`, so `s >= 3`; and `A ≡ 2 (mod 8)` for even `d`, so `s = 1`.

This proves the first-layer classification. ∎

The proposition should be read as a coarse entry theorem for Route A. It determines the first valuation layer, but not the full value of `s` on the genuinely lifting branch.

#### 11.8.1.5. Worked examples and discovery path

The historical route by which this first-layer split and the later lifting-branch picture were discovered is now moved to Appendix A.

In particular, Appendix A records:

* the calibration families `ω = 1, 5, 7`,
* the anchor-discovery example `ω = 17`,
* and the clean tower example `ω = 25`.

Those examples are useful for intuition, but they are no longer needed in the main formal line.

#### 11.8.1.6. Transition to the lifting branch

By Proposition `11.8.1.4.1`, the first-layer congruence forces

```text
v_2(3^d ω - 1) >= 3
```

in exactly two of the eight residue-parity classes:

```text
ω ≡ 1 (mod 8),   d even    (the even lifting component),
ω ≡ 3 (mod 8),   d odd     (the odd lifting component).
```

Both components are nonempty in the valid reduced setting `3 ∤ ω`: the even component contains, for example, `(ω, d) = (17, 2)`, and the odd component contains `(ω, d) = (11, 1)`, where `A = 3·11 - 1 = 32` and `s = 5`. Earlier drafts developed the lifting machinery only on the even component; the odd component is equally real and must be carried through the synthesis. It will be handled by an exact reduction to the even-component formalism (Proposition `11.8.1.7.2` below), so no new machinery is required — but the scope statements must include it.

So once Stage 1 reaches the lifting regime, the natural next question is no longer merely whether deeper lifting occurs, but how it is generated arithmetically.

The key point is that on both lifting components the valuation problem becomes a congruence problem in the exponent variable, in the same base `9`.

#### 11.8.1.7. Lifting on the even branch as a congruence problem in base `9`

**Proposition 11.8.1.7.1.** Let `ω` be odd and let `d = 2n` be even. For any integer `k >= 1`,

```text
v_2(3^d ω - 1) >= k
    if and only if
3^d ω ≡ 1 (mod 2^k)
    if and only if
9^n ω ≡ 1 (mod 2^k)
    if and only if
9^n ≡ ω^(-1) (mod 2^k).
```

Here `ω^(-1)` denotes the inverse of `ω` modulo `2^k`, which exists because `ω` is odd.

**Proof.** By definition,

```text
v_2(3^d ω - 1) >= k
```

if and only if `2^k` divides `3^d ω - 1`, which is equivalent to

```text
3^d ω - 1 ≡ 0 (mod 2^k),
```

hence to

```text
3^d ω ≡ 1 (mod 2^k).
```

Now assume `d = 2n`. Then

```text
3^d = 3^(2n) = 9^n,
```

so the congruence becomes

```text
9^n ω ≡ 1 (mod 2^k).
```

Since `ω` is odd, it is invertible modulo `2^k`, and multiplying by `ω^(-1)` gives

```text
9^n ≡ ω^(-1) (mod 2^k).
```

This proves the chain of equivalences. ∎

This proposition is the formal bridge from first-layer lifting to tower structure. It shows that on the even branch the valuation problem is naturally a base-`9` congruence problem in the exponent variable `n`, not merely a problem about the raw depth variable `d`.

The odd lifting component reduces to exactly the same congruence problem via a companion parameter.

**Proposition 11.8.1.7.2 (odd branch via the companion parameter).** Let `ω` be odd and let `d = 2n + 1` be odd. Define the companion parameter

```text
ω̃ = 3ω.
```

Then

```text
3^d ω = 9^n · ω̃,
```

so for any integer `k >= 1`,

```text
v_2(3^d ω - 1) >= k
    if and only if
9^n ≡ ω̃^(-1) (mod 2^k).
```

Moreover, if `ω ≡ 3 (mod 8)`, then

```text
ω̃ = 3ω ≡ 9 ≡ 1 (mod 8),
```

so the companion parameter lies in exactly the residue class in which the even-branch congruence formalism of Proposition `11.8.1.7.1` and the later anchor machinery operate.

**Proof.** Since `d = 2n + 1`,

```text
3^d ω = 3^(2n+1) ω = 9^n · (3ω) = 9^n · ω̃.
```

The chain of equivalences is then identical to that of Proposition `11.8.1.7.1` with `ω` replaced by `ω̃`: `v_2(9^n ω̃ - 1) >= k` if and only if `9^n ω̃ ≡ 1 (mod 2^k)`, and since `ω̃` is odd it is invertible modulo `2^k`, giving `9^n ≡ ω̃^(-1) (mod 2^k)`. Finally, if `ω ≡ 3 (mod 8)` then `3ω ≡ 9 ≡ 1 (mod 8)`. ∎

**Remark (validity of the companion substitution).** The companion parameter `ω̃ = 3ω` is divisible by `3`, so `(ω̃, 2n)` is not itself a valid reduced state. This is harmless: `ω̃` enters only as an arithmetic parameter of the congruence problem `9^n ≡ ω̃^(-1) (mod 2^k)`, and every result of the Stage 1 synthesis in `11.8.3` uses only that the parameter is odd and congruent to `1 (mod 8)` — the hypothesis `3 ∤ ω` is never invoked there. The dynamical conclusions are then read back on the genuine reduced state `(ω, d)` through the identity `v_2(3^d ω - 1) = v_2(9^n ω̃ - 1)`.

**Worked check.** Take `(ω, d) = (11, 1)`, so `n = 0` and `ω̃ = 33`. Directly, `A = 3·11 - 1 = 32`, so `s = 5`. On the companion side, `33^(-1) ≡ 33 (mod 64)` and `9^4 = 6561 ≡ 33 (mod 64)`, so the anchor satisfies `N(33) ≡ 4 (mod 8)` and

```text
s = 3 + v_2(0 - N(33)) = 3 + 2 = 5,
```

in agreement (using the anchor-displacement law of Theorem `11.8.3.9.1`, stated later, applied to `ω̃ = 33`).

#### 11.8.1.8. Congruence towers on the lifting branch

Proposition `11.8.1.7.1` suggests the following definitions.

**Definition 11.8.1.8.1 (raw congruence level).** Let `ω` be odd, and let `k >= 4`. The level-`k` congruence set of `ω` is

```text
T_k(ω) = { n (mod 2^(k-3)) : 9^n ≡ ω^(-1) (mod 2^k) },
```

whenever this congruence is considered on the even branch `d = 2n`.

Equivalently, the corresponding level-`k` residue set in the original depth variable is

```text
D_k(ω) = { d = 2n : n in T_k(ω) }.
```

These are exactly the residue classes on which

```text
v_2(3^d ω - 1) >= k.
```

**Definition 11.8.1.8.2 (lifting branch).** The lifting branch is the locus on which the first-layer mod `8` classification forces

```text
v_2(3^d ω - 1) >= 3.
```

By Proposition `11.8.1.4.1`, in the valid reduced setting with `3 ∤ ω` it has exactly two components:

```text
even component:  ω ≡ 1 (mod 8),   d = 2n,
odd component:   ω ≡ 3 (mod 8),   d = 2n + 1.
```

On the even component the relevant congruence parameter is `ω` itself. On the odd component, by Proposition `11.8.1.7.2`, the relevant congruence parameter is the companion `ω̃ = 3ω ≡ 1 (mod 8)`, and the level-`k` congruence sets are `T_k(ω̃)` in the exponent variable `n`, with depth-side classes `d = 2n + 1` rather than `d = 2n`. All tower definitions below apply verbatim on the odd component after this substitution.

**Definition 11.8.1.8.3 (distinguished congruence tower).** Suppose that for a fixed `ω` there exists a compatible nested choice of residue classes

```text
n_k (mod 2^(k-3)) in T_k(ω)
```

such that each class reduces to the preceding one as `k` decreases. Then this nested sequence is called a distinguished congruence tower for `ω`.

The corresponding distinguished depth classes are

```text
d_k = 2 n_k.
```

When such a compatible sequence exists, the visible lifting residues in `d` are interpreted as finite truncations of that tower.

**Remark 11.8.1.8.4 (historical tower-type labels — dissolved).** Earlier drafts introduced here a provisional dichotomy of distinguished towers into "regular" (`ω = 25, 49, 73`) and "irregular" (`ω = 17, 41, 65, 89`) visible geometries, together with a conjectured mod-`3` classifier. Both are dead, and no definition is made. The visible refinement of a tower is determined digit-by-digit by the anchor `N(ω)` of `11.8.3.6` — the level-`k` class changes exactly when digit `k - 3` of `N(ω)` is `1` — and the historical labels correspond to nothing more than high versus low digit density in the observation window: a continuous statistic, not two classes. The mod-`3` classifier was refuted outright by a computational audit. The closing note of `11.8.4.3` records the resolution; Appendix `A.4.6` preserves the historical observation and the audit data. Where Appendix A uses the words regular and irregular, they are period labels for these seven calibration families only.

These definitions deliberately separate three issues:

1. the exact congruence reformulation of the valuation problem,
2. the existence of compatible nested solution classes,
3. the empirical geometry of the resulting tower.

Only the first of these is fully formal at this stage. The later synthesis will show that much of the remaining structure can also be formalized.

The worked examples that historically revealed these steps are now collected in Appendix A. The next subsection proceeds directly to the pre-synthesis tower map.

#### 11.8.1.9. #TODO: renumber

### 11.8.2. Pre-synthesis tower map

This subsection maps the visible tower geometry at the level needed before `11.8.3` begins: the formal mechanism is already in hand; what remains is to record the tower archetypes and mark the boundary between the exact and the empirical.

#### 11.8.2.1. #TODO: renumber

#### 11.8.2.2. #TODO: renumber

#### 11.8.2.3. Tower archetypes visible before synthesis

The computed examples suggest that the lifting branch does not present one uniform visible geometry. Before the formal synthesis is stated, it is useful to name the main tower archetypes that the data currently displays.

**(a) Global anchor model.**
The family

```text
ω = 1
```

is the fundamental anchored family. On the even branch one has the exact law

```text
v_2(3^d - 1) = 2 + v_2(d),
```

so the lifting behavior is globally organized around the depth origin itself. In this family there is no separate distinction between a family-dependent branch and a surrounding halo; the anchored law is already global.

**(b) Towers with dense visible refinement.**
The families

```text
ω = 25, 49, 73
```

lie on the valid lifting branch and, in the current data, exhibit clean nested towers. Their visible exceptional residue classes are recovered by the congruence mechanism

```text
9^n ≡ ω^(-1) (mod 2^k),
d = 2n.
```

In these cases, the visible lifting geometry appears to be exhausted by the distinguished congruence branch itself, with no separate surrounding halo structure.

**(c) Towers with sparse refinement and visible halos.**
The families

```text
ω = 17, 41, 65, 89
```

also lie on the valid lifting branch and again admit a distinguished congruence branch generated by the same base-`9` mechanism. What differs is the visible local geometry around that branch. In these examples, the main branch is accompanied by a structured halo rather than by a clean one-branch-at-a-time refinement.

The current evidence suggests that this halo is not arbitrary family-specific noise. After centering at the primary spike, the same dyadic shell template appears repeatedly across these examples.

**(d) Collapsed or absorbed families.**
When

```text
3 ∣ ω,
```

the `3`-adic content is absorbed before a genuinely new reduced lifting family is obtained. These cases should therefore be kept separate from the genuinely new tower types in the valid reduced setting.

So, at the level of a pre-synthesis map, the visible tower taxonomy is:

```text
global anchor model             : ω = 1
dense-refinement towers         : ω = 25, 49, 73
sparse-refinement halo towers   : ω = 17, 41, 65, 89
collapsed / absorbed families   : 3 ∣ ω
```

This taxonomy is organizational: it tells the reader what the later synthesis must — and does — explain. The dense/sparse contrast in the middle two rows is a continuous digit-density statistic of the anchor, not a structural dichotomy (Remark `11.8.1.8.4`).

#### 11.8.2.4. What is empirical in the tower map

Not every feature of the visible tower geometry should be treated at the same logical level.

At the formal level already established before `11.8.3`, one has:

* the first-layer mod `8` partition,
* the isolation of the valid lifting branch,
* and the exact congruence reformulation
  `9^n ≡ ω^(-1) (mod 2^k)`.

By contrast, the following remain pre-synthesis observations rather than theorem-level inputs here:

* the visible differences in refinement density among family towers,
* the translated-shell relation among the sparse-refinement families,
* and the centered dyadic halo template around primary spikes.

(A finer arithmetic classifier of tower geometry was once conjectured at this point in the program; it has since been refuted, and the underlying dichotomy dissolved — see Remark `11.8.1.8.4`. It is not carried forward in this map.)

So this subsection deliberately stops short of synthesis. It records the visible map, but it does not yet identify which parts of that map are exhausted by the congruence branch and which parts require a new local law. That is exactly the role of `11.8.3`.

#### 11.8.2.5. Transition to the Stage 1 synthesis

The pre-synthesis tower map now points to a sharper question than the earlier family-by-family discussion did.

The exact arithmetic mechanism on the lifting branch is already clear:

```text
9^n ≡ ω^(-1) (mod 2^k).
```

What is not yet clear at the level of the present map is how much of the visible tower geometry is already encoded by the compatible branch generated by this congruence, and how much additional structure survives after that branch is identified.

This is the point at which `11.8.3` begins.

The next subsection no longer treats the primary branch as merely an empirical feature of some families. It identifies it formally, assembles it into the global `2`-adic anchor (recognized in `11.8.3.6` as a `2`-adic logarithm), proves the universal local valuation law below spike height, localizes all possible off-spike excess to the boundary shell, and rewrites the remaining valuation refinement in anchor-displacement coordinates.

### 11.8.3. Stage 1 synthesis on the lifting branch

The pre-synthesis tower map of `11.8.2` isolates the correct entry point for Stage 1: on the even lifting component

```text
ω ≡ 1 (mod 8),   d = 2n,
```

the valuation problem is governed not by an ad hoc pattern in the raw depth variable `d`, but by the congruence mechanism

```text
9^n ≡ ω^(-1) (mod 2^k).
```

The purpose of the present subsection is to state the resulting Stage 1 synthesis directly.

**Convention (transfer to the odd component).** Throughout `11.8.3`, all statements are written for a parameter `ω` that is odd and congruent to `1 (mod 8)`, with even depth `d = 2n`. By Proposition `11.8.1.7.2`, every such statement applies verbatim to the odd lifting component `ω ≡ 3 (mod 8)`, `d = 2n + 1`, upon substituting the companion parameter `ω̃ = 3ω` for `ω` and reading `n` from `d = 2n + 1`; the identity `v_2(3^d ω - 1) = v_2(9^n ω̃ - 1)` transports every valuation conclusion back to the genuine reduced state. No result in this subsection uses `3 ∤ ω`, so the divisibility of `ω̃` by `3` is immaterial here. To avoid doubling every statement, the transfer is left implicit until the dynamical conversion in `11.8.5`, where the odd-component form is recorded explicitly.

Its central claim is that the lifting-branch valuation picture decomposes into two parts:

* a family-dependent primary congruence branch, which assembles into a single global `2`-adic anchor,
* and a universal local valuation geometry after centering at that anchor.

More precisely, the family-dependent datum is the compatible branch itself, equivalently the additive anchor `N(ω)`. Off the spike, the local valuation law is universal below spike height. The only possible excess beyond that universal law is localized on a single dyadic boundary shell, and even there the valuation refinement is governed by normalized anchor error rather than by a second independent family-specific invariant.

This is the formal Stage 1 synthesis on the lifting branch.

**Convention.**
Throughout `11.8.3`, the branch quantities

```text
n_k(ω) (mod 2^(k-3)),    d_k^*(ω) = 2n_k(ω) (mod 2^(k-2))
```

are considered only for levels

```text
k >= 4.
```

The underlying congruence

```text
9^n ≡ ω^(-1) (mod 2^k)
```

still makes sense for smaller `k`, but the branch formalism in terms of residue classes modulo `2^(k-3)` begins only at `k = 4`, where the lifting-branch structure becomes nondegenerate in the present formulation.

#### 11.8.3.1. The primary congruence branch on the lifting branch

The lifting-branch congruence condition already isolates the family-dependent anchor as an exact arithmetic object.

**Theorem 11.8.3.1.1 (existence, uniqueness, and compatibility of the primary congruence branch).**
Let `ω` be odd with

```text
ω ≡ 1 (mod 8),
```

and let `k >= 4`. Then there exists a unique congruence class

```text
n_k(ω) (mod 2^(k-3))
```

satisfying

```text
9^n ≡ ω^(-1) (mod 2^k).
```

Equivalently, there exists a unique congruence class

```text
d_k^*(ω) = 2 n_k(ω) (mod 2^(k-2))
```

on the even depth branch satisfying

```text
v_2(ω·3^d - 1) >= k.
```

Moreover, these classes are compatible under reduction: if `k >= 4`, then the class

```text
n_(k+1)(ω) (mod 2^(k-2))
```

reduces to the class

```text
n_k(ω) (mod 2^(k-3)).
```

**Proof.**
Fix `k >= 4`. Since `ω ≡ 1 (mod 8)`, its inverse modulo `2^k` also satisfies

```text
ω^(-1) ≡ 1 (mod 8).
```

So `ω^(-1)` lies in the subgroup

```text
1 + 8 Z / 2^k Z.
```

This subgroup has cardinality `2^(k-3)`.

Now consider the powers of `9` modulo `2^k`. Since

```text
9 = 1 + 8,
```

the standard lifting law for powers of `1 + 8` gives, for every integer `t >= 0`,

```text
v_2(9^(2^t) - 1) = 3 + t.
```

Hence `9^(2^(k-3)) ≡ 1 (mod 2^k)`, while for `0 <= t < k-3` one has

```text
9^(2^t) not≡ 1 (mod 2^k).
```

So the order of `9` modulo `2^k` is exactly

```text
ord_(2^k)(9) = 2^(k-3).
```

Therefore the cyclic subgroup generated by `9` has exactly `2^(k-3)` elements. Since every power of `9` is congruent to `1 (mod 8)`, one has

```text
<9> ⊆ 1 + 8 Z / 2^k Z,
```

and because both sets have the same cardinality, equality holds:

```text
<9> = 1 + 8 Z / 2^k Z.
```

It follows that there exists some `n` such that

```text
9^n ≡ ω^(-1) (mod 2^k).
```

Uniqueness modulo `2^(k-3)` follows from the fact that the order of `9` modulo `2^k` is exactly `2^(k-3)`.

Now let `n_(k+1)(ω)` be the unique class modulo `2^(k-2)` satisfying

```text
9^n ≡ ω^(-1) (mod 2^(k+1)).
```

Reducing this congruence modulo `2^k` shows that the reduced class also solves

```text
9^n ≡ ω^(-1) (mod 2^k).
```

By uniqueness at level `k`, this reduced class must equal `n_k(ω) (mod 2^(k-3))`. This proves compatibility.

Finally, by Proposition `11.8.1.7.1`, on the even branch `d = 2n` the congruence condition is equivalent to

```text
v_2(ω·3^d - 1) >= k.
```

So the corresponding depth-side class

```text
d_k^*(ω) = 2 n_k(ω)
```

is uniquely determined as well. ∎

**Interpretation.**
The primary branch is therefore not a special empirical artifact of particular families. It is the canonical lifting-branch congruence object attached to every parameter `ω ≡ 1 (mod 8)` — whether that parameter is a valid family on the even component, or the companion `ω̃ = 3ω` of a family `ω ≡ 3 (mod 8)` on the odd component. The family-dependent datum is the compatible branch itself.

#### 11.8.3.2. Universal centered halo law around a branch point

Once a branch point is fixed, the surrounding local valuation geometry is universal up to the height of that point.

**Theorem 11.8.3.2.1 (centered halo law below spike height).**
Let `ω` be odd, let `d_*` be even, and define

```text
H = v_2(ω·3^(d_*) - 1).
```

Then for every even displacement `Δ != 0` satisfying

```text
2 + v_2(Δ) < H,
```

one has

```text
v_2(ω·3^(d_* + Δ) - 1) = 2 + v_2(Δ).
```

**Proof.**
Write

```text
ω·3^(d_*) - 1 = 2^H u
```

with `u` odd. Then

```text
ω·3^(d_*) = 1 + 2^H u.
```

Let `Δ` be even and nonzero. Then

```text
ω·3^(d_* + Δ) - 1
= (ω·3^(d_*)) 3^Δ - 1
= (1 + 2^H u)3^Δ - 1
= (3^Δ - 1) + 2^H u 3^Δ.
```

Now write

```text
Δ = 2r.
```

Then

```text
3^Δ = 9^r,
```

so

```text
v_2(3^Δ - 1) = v_2(9^r - 1).
```

By the `ω = 1` valuation law of Proposition `11.8.1.1.1` applied to `9^r - 1 = 3^(2r) - 1`,
one has

```text
v_2(3^Δ - 1) = 2 + v_2(Δ).
```

The second term

```text
2^H u 3^Δ
```

has valuation exactly `H`. By hypothesis,

```text
2 + v_2(Δ) < H,
```

so the two summands have distinct `2`-adic valuations, and the smaller one dominates. Therefore

```text
v_2(ω·3^(d_* + Δ) - 1)
= v_2(3^Δ - 1)
= 2 + v_2(Δ).
```

This proves the claim. ∎

**Interpretation.**
Off the spike itself, the valuation depends only on the even displacement `Δ` from the branch point and not on the family `ω`. In this precise sense, the centered halo law is universal. The family-specific information lies only in the branch location and spike height.

In retrospect (see the isometry remark following Theorem `11.8.3.6.6`), this universality is the isometry property of the `2`-adic logarithm — equivalently, the lifting-the-exponent identity: the valuation of `9^ε - 1` is `3 + v_2(ε)`, a function of the displacement alone.

#### 11.8.3.3. Boundary-shell localization and the dyadic refinement barrier

The centered halo law of `11.8.3.2.1` already shows that no distinct displacement can match the spike height before the scale `2^(H-2)`. The next calculation shows more: once one reaches and passes that scale, the only shell on which genuinely higher off-spike lifting can occur is the first allowable boundary shell itself.

**Proposition 11.8.3.3.1 (boundary-shell localization).**
Let `ω` be odd, let `d_*` be even, and define

```text
H = v_2(ω·3^(d_*) - 1).
```

Fix an even displacement `Δ != 0`.

Then:

1. if

   ```text
   v_2(Δ) < H - 2,
   ```

   one has

   ```text
   v_2(ω·3^(d_* + Δ) - 1) = 2 + v_2(Δ);
   ```

2. if

   ```text
   v_2(Δ) > H - 2,
   ```

   one has

   ```text
   v_2(ω·3^(d_* + Δ) - 1) = H;
   ```

3. if

   ```text
   v_2(Δ) = H - 2,
   ```

   then writing

   ```text
   3^Δ - 1 = 2^H α
   ```

   with `α` odd, and

   ```text
   ω·3^(d_*) - 1 = 2^H u
   ```

   with `u` odd, one has

   ```text
   ω·3^(d_* + Δ) - 1 = 2^H (α + u·3^Δ),
   ```

   and therefore

   ```text
   v_2(ω·3^(d_* + Δ) - 1) = H + v_2(α + u·3^Δ).
   ```

In particular, every off-spike displacement satisfying

```text
v_2(ω·3^(d_* + Δ) - 1) > H
```

must lie on the boundary shell

```text
v_2(Δ) = H - 2.
```

**Proof.**
Write

```text
ω·3^(d_*) - 1 = 2^H u
```

with `u` odd. Then

```text
ω·3^(d_*) = 1 + 2^H u.
```

Hence for every even `Δ`,

```text
ω·3^(d_* + Δ) - 1
= (ω·3^(d_*))3^Δ - 1
= (1 + 2^H u)3^Δ - 1
= (3^Δ - 1) + 2^H u·3^Δ.
```

Now let

```text
Δ = 2^(H-2+r) m
```

with `m` odd and `r >= 0` whenever `v_2(Δ) >= H-2`.

Because `Δ` is even, Proposition `11.8.1.1.1` gives

```text
v_2(3^Δ - 1) = 2 + v_2(Δ).
```

So if `v_2(Δ) < H-2`, then

```text
2 + v_2(Δ) < H,
```

and Theorem `11.8.3.2.1` yields

```text
v_2(ω·3^(d_* + Δ) - 1) = 2 + v_2(Δ).
```

This proves (1).

Now suppose `v_2(Δ) >= H-2`, so that

```text
Δ = 2^(H-2+r) m
```

with `m` odd and `r >= 0`. Then

```text
v_2(3^Δ - 1) = H + r,
```

so we may write

```text
3^Δ - 1 = 2^(H+r) α
```

with `α` odd. Substituting into the decomposition above gives

```text
ω·3^(d_* + Δ) - 1
= 2^(H+r) α + 2^H u·3^Δ
= 2^H(2^r α + u·3^Δ).
```

If `r >= 1`, then `2^r α` is even, while `u·3^Δ` is odd. So

```text
2^r α + u·3^Δ
```

is odd, and therefore

```text
v_2(ω·3^(d_* + Δ) - 1) = H.
```

This proves (2).

If `r = 0`, equivalently `v_2(Δ) = H-2`, then

```text
ω·3^(d_* + Δ) - 1 = 2^H(α + u·3^Δ),
```

with `α` odd and `u·3^Δ` odd. Hence

```text
v_2(ω·3^(d_* + Δ) - 1) = H + v_2(α + u·3^Δ).
```

This proves (3).

The final statement follows immediately: if the valuation is strictly greater than `H`, then case (2) is impossible, and case (1) gives a value strictly less than `H`, so one must be in case (3), namely

```text
v_2(Δ) = H - 2.
```

∎

**Corollary 11.8.3.3.2 (dyadic refinement barrier, sharpened form).**
Let `ω` be odd, let `d_*` be even, and let

```text
H = v_2(ω·3^(d_*) - 1).
```

If `Δ` is even and nonzero and satisfies

```text
v_2(ω·3^(d_* + Δ) - 1) >= H,
```

then necessarily

```text
v_2(Δ) >= H - 2,
```

equivalently,

```text
2^(H-2) divides Δ.
```

If moreover

```text
v_2(ω·3^(d_* + Δ) - 1) > H,
```

then necessarily

```text
v_2(Δ) = H - 2.
```

So no distinct point can exceed the spike height except on the first allowable dyadic shell.

**Interpretation.**
The local valuation geometry around a spike of height `H` splits into three regions:

```text
below the boundary shell      : universal transplanted law  2 + v_2(Δ),
beyond the boundary shell     : exact return to height H,
on the boundary shell itself  : the only place where further off-spike lifting can occur.
```

Thus the unresolved part of the global halo problem is concentrated on one dyadic shell, namely

```text
v_2(Δ) = H - 2.
```

#### 11.8.3.4. Arithmetic normal form on the boundary shell

Proposition `11.8.3.3.1` shows that once a spike point

```text
d_*
```

of height

```text
H = v_2(ω·3^(d_*) - 1)
```

is fixed, all off-spike behavior is already determined except on the single boundary shell

```text
v_2(Δ) = H - 2.
```

So the remaining local problem is to write the valuation on that shell in a normalized arithmetic form.

Write

```text
ω·3^(d_*) - 1 = 2^H u,
```

where `u` is odd. Thus

```text
ω·3^(d_*) = 1 + 2^H u.
```

Now restrict to the boundary shell. Every even displacement `Δ` satisfying

```text
v_2(Δ) = H - 2
```

may be written uniquely in the form

```text
Δ = 2^(H-2)t,
```

with `t` odd.

For such a displacement, Proposition `11.8.3.3.1` gives

```text
v_2(3^Δ - 1) = H,
```

so one may define the normalized shell coefficient

```text
α_H(t) = (3^(2^(H-2)t) - 1)/2^H.
```

Since `v_2(3^Δ - 1) = H`, the quantity `α_H(t)` is an odd integer.

Substituting

```text
ω·3^(d_*) = 1 + 2^H u
```

and

```text
3^Δ - 1 = 2^H α_H(t)
```

into the identity

```text
ω·3^(d_* + Δ) - 1
= (ω·3^(d_*))3^Δ - 1
= (3^Δ - 1) + 2^H u·3^Δ,
```

one obtains

```text
ω·3^(d_* + 2^(H-2)t) - 1
= 2^H(α_H(t) + u·3^(2^(H-2)t)).
```

This motivates the following definition.

**Definition 11.8.3.4.1 (boundary-shell correction term).**
For a spike point `d_*` of height `H`, with normalized spike unit

```text
u = (ω·3^(d_*) - 1)/2^H,
```

define the boundary-shell correction term by

```text
B_H(u,t) = α_H(t) + u·3^(2^(H-2)t),
```

for odd integers `t`, where

```text
α_H(t) = (3^(2^(H-2)t) - 1)/2^H.
```

Then the valuation on the boundary shell is given exactly by

```text
ω·3^(d_* + 2^(H-2)t) - 1 = 2^H B_H(u,t),
```

and hence

```text
v_2(ω·3^(d_* + 2^(H-2)t) - 1) = H + v_2(B_H(u,t)).
```

Thus the full local valuation picture around `d_*` has the following form.

* If

  ```text
  v_2(Δ) < H - 2,
  ```

  then

  ```text
  v_2(ω·3^(d_* + Δ) - 1) = 2 + v_2(Δ).
  ```

* If

  ```text
  v_2(Δ) > H - 2,
  ```

  then

  ```text
  v_2(ω·3^(d_* + Δ) - 1) = H.
  ```

* If

  ```text
  Δ = 2^(H-2)t,   t odd,
  ```

  then

  ```text
  v_2(ω·3^(d_* + Δ) - 1) = H + v_2(B_H(u,t)).
  ```

So every possible deviation from the two universal off-spike regimes is concentrated in the arithmetic of the single function

```text
B_H(u,t).
```

**Lemma 11.8.3.4.2 (first universal divisibility on the boundary shell).**
Let `Δ = 2^(H-2)t` with `t` odd. Then:

1. `α_H(t)` is odd;
2. `u·3^(2^(H-2)t)` is odd;
3. `B_H(u,t)` is even.

Consequently,

```text
v_2(B_H(u,t)) >= 1,
```

and therefore every boundary-shell point satisfies

```text
v_2(ω·3^(d_* + 2^(H-2)t) - 1) >= H + 1.
```

**Proof.**
The first claim follows from

```text
v_2(3^(2^(H-2)t) - 1) = H.
```

The second is immediate since both factors are odd. Hence `B_H(u,t)` is the sum of two odd integers, so it is even. The valuation statement follows from

```text
ω·3^(d_* + 2^(H-2)t) - 1 = 2^H B_H(u,t).
```

∎

**Interpretation.**
The boundary shell is the unique shell on which the valuation can rise above the spike height `H`, and the excess valuation there is measured exactly by

```text
v_2(B_H(u,t)).
```

So the local structure near a spike is completely reduced to the arithmetic of the boundary-shell correction term.

#### 11.8.3.5. Ratio law for relative branch offsets

Because the primary branch is unique at each level, relative offsets between families are governed by the same congruence mechanism as the branches themselves.

**Theorem 11.8.3.5.1 (ratio-law encoding of relative branch offsets).**
Let `ω_1` and `ω_2` be odd integers satisfying

```text
ω_1 ≡ ω_2 ≡ 1 (mod 8),
```

and let `k >= 4`. Then the difference class

```text
n_k(ω_2) - n_k(ω_1) (mod 2^(k-3))
```

is the unique solution class to

```text
9^m ≡ ω_1 · ω_2^(-1) (mod 2^k).
```

Equivalently, the relative displacement of the corresponding depth-side branches is governed by the same base-`9` congruence mechanism as the branches themselves.

**Proof.**
By Theorem `11.8.3.1.1`, one has

```text
9^(n_k(ω_1)) ≡ ω_1^(-1) (mod 2^k),
9^(n_k(ω_2)) ≡ ω_2^(-1) (mod 2^k).
```

Since `9` is a unit modulo `2^k`, one may divide the second congruence by the first, obtaining

```text
9^(n_k(ω_2) - n_k(ω_1))
≡ ω_2^(-1) · ω_1
≡ ω_1 · ω_2^(-1)
(mod 2^k).
```

So the difference class is a solution to

```text
9^m ≡ ω_1 · ω_2^(-1) (mod 2^k).
```

Now

```text
ω_1 · ω_2^(-1) ≡ 1 (mod 8),
```

since both factors lie in `1 (mod 8)`. Therefore Theorem `11.8.3.1.1` applies again, this time to the ratio `ω_1 · ω_2^(-1)`, and yields a unique solution class modulo `2^(k-3)`. Hence the difference class above is exactly that unique class.

This proves the claim. ∎

**Interpretation.**
Relative branch placement is not a secondary phenomenon requiring a new mechanism. It is governed by the same congruence law as the branch itself, now applied to the ratio of the two family parameters. So family-to-family displacement is already encoded by the primary branch mechanism.

Once the anchor is identified as a logarithm (Theorem `11.8.3.6.6` below), this theorem becomes the statement `log(ω_1/ω_2) = log ω_1 - log ω_2`, truncated to level `k`.

#### 11.8.3.6. The global `2`-adic anchor `N(ω)`

The finite-level primary congruence branches now assemble canonically into a single global `2`-adic coordinate on the lifting branch.

**Definition 11.8.3.6.1 (global exponent-side anchor).**
Let `ω` be odd with

```text
ω ≡ 1 (mod 8).
```

For each `k >= 4`, let

```text
n_k(ω) (mod 2^(k-3))
```

denote the unique compatible solution class from Theorem `11.8.3.1.1`, characterized by

```text
9^n ≡ ω^(-1) (mod 2^k).
```

Since these classes are compatible under reduction, they define a unique element

```text
N(ω) in Z_2
```

such that for every `k >= 4`,

```text
N(ω) ≡ n_k(ω) (mod 2^(k-3)).
```

We call `N(ω)` the **global `2`-adic anchor** of the lifting family `ω`.

Equivalently,

```text
N(ω) = lim← n_k(ω).
```

**Definition 11.8.3.6.2 (global depth-side anchor).**
Define the corresponding depth-side anchor by

```text
D^*(ω) = 2 N(ω) in 2 Z_2.
```

Then for each `k >= 4`,

```text
D^*(ω) ≡ d_k^*(ω) (mod 2^(k-2)),
```

where

```text
d_k^*(ω) = 2 n_k(ω)
```

is the primary branch class of Theorem `11.8.3.1.1`.

So the compatible finite truncations `d_k^*(ω)` are exactly the finite-level shadows of the single global `2`-adic anchor `D^*(ω)`.

**Proposition 11.8.3.6.3 (characterizing property of `N(ω)`).**
For every lifting family `ω ≡ 1 (mod 8)`, the element

```text
N(ω) in Z_2
```

is uniquely characterized by the condition that for every `k >= 4` its reduction modulo `2^(k-3)` is the unique solution class to

```text
9^n ≡ ω^(-1) (mod 2^k).
```

Equivalently, `D^*(ω) = 2N(ω)` is the unique depth-side `2`-adic class whose levelwise reductions recover the primary branch classes `d_k^*(ω)`.

**Proof.**
This is immediate from Theorem `11.8.3.1.1`. Existence and compatibility of the finite classes `n_k(ω)` give an inverse-limit element of `Z_2`, and uniqueness follows because an element of `Z_2` is uniquely determined by its reductions modulo `2^m` for all `m >= 1`. ∎

**Proposition 11.8.3.6.4 (global ratio law).**
Let `ω_1, ω_2` satisfy

```text
ω_1 ≡ ω_2 ≡ 1 (mod 8).
```

Then

```text
N(ω_2) - N(ω_1) = N(ω_1 · ω_2^(-1))
```

in `Z_2`.

Equivalently, on the depth side,

```text
D^*(ω_2) - D^*(ω_1) = D^*(ω_1 · ω_2^(-1))
```

in `2 Z_2`.

**Proof.**
For each `k >= 4`, Theorem `11.8.3.5.1` shows that the difference class

```text
n_k(ω_2) - n_k(ω_1) (mod 2^(k-3))
```

is the unique solution to

```text
9^m ≡ ω_1 · ω_2^(-1) (mod 2^k).
```

But by definition this unique class is exactly

```text
n_k(ω_1 · ω_2^(-1)).
```

So for every `k >= 4` one has

```text
n_k(ω_2) - n_k(ω_1) ≡ n_k(ω_1 · ω_2^(-1)) (mod 2^(k-3)).
```

Passing to the inverse limit gives

```text
N(ω_2) - N(ω_1) = N(ω_1 · ω_2^(-1)).
```

Multiplying by `2` gives the depth-side statement. ∎

**Interpretation.**
The family-dependent anchor is no longer best viewed as a collection of unrelated finite congruence classes. It is a single global `2`-adic coordinate on the lifting branch, and the finite classes

```text
n_k(ω), d_k^*(ω)
```

are simply truncations of that one object.

The anchor is, moreover, not a new arithmetic object at all. It is a `2`-adic logarithm, and naming it as such collapses several of the surrounding proofs. The next two statements record this.

**Lemma 11.8.3.6.5 (the `2`-adic logarithm on `1 + 8 Z_2`).**
For `u in 1 + 8 Z_2`, the series

```text
log u = Σ_(i>=1) (-1)^(i+1) (u - 1)^i / i
```

converges in `Z_2`, and the map `log : 1 + 8 Z_2 -> 8 Z_2` is an isomorphism of topological groups (from the multiplicative to the additive structure). Moreover it is an isometry in the sense that

```text
v_2(log u) = v_2(u - 1)
```

for all `u in 1 + 8 Z_2`.

**Proof.** Write `x = u - 1`, so `v_2(x) >= 3`. For `i >= 2`,

```text
v_2(x^i / i) - v_2(x) >= (i - 1)·3 - v_2(i) > 0,
```

since `v_2(i) <= log_2(i) < 3(i - 1)` for all `i >= 2`. Hence the general term tends to `0` `2`-adically (so the series converges), and every term beyond the first has valuation strictly greater than `v_2(x)`. By the ultrametric inequality the valuation of the sum equals that of the dominant first term:

```text
v_2(log u) = v_2(x) = v_2(u - 1).
```

The homomorphism property `log(uv) = log u + log v` and the bijectivity onto `8 Z_2` (with inverse the exponential series `exp`, convergent on `8 Z_2` by the same term-domination estimate) are the standard properties of the `2`-adic (Iwasawa) logarithm on the domain `v_2(u - 1) >= 2`, and hold a fortiori on `1 + 8 Z_2`. ∎

**Theorem 11.8.3.6.6 (logarithmic identification of the anchor).**
For every `ω ≡ 1 (mod 8)`,

```text
N(ω) = - log ω / log 9,
```

where `log` is the `2`-adic logarithm of Lemma `11.8.3.6.5`. The quotient lies in `Z_2` because

```text
v_2(log 9) = v_2(9 - 1) = 3
```

and `v_2(log ω) = v_2(ω - 1) >= 3`.

**Proof.** The defining congruences `9^(n_k(ω)) ≡ ω^(-1) (mod 2^k)` are compatible for all `k >= 4`, so they assemble in `1 + 8 Z_2` to the exact identity

```text
9^(N(ω)) = ω^(-1),
```

where `z ↦ 9^z` is the continuous extension of integer exponentiation to `Z_2` (continuity holds because `9^(2^t) -> 1` as `t -> ∞`). Applying `log` and using the homomorphism property,

```text
N(ω) · log 9 = - log ω,
```

and dividing by `log 9` (valuation exactly `3`, hence nonzero) gives the claim. Integrality of the quotient follows from the isometry: `v_2(log ω) >= 3 = v_2(log 9)`. ∎

**Remark (computability of the anchor).** The identification replaces level-by-level congruence solving by a convergent power series: truncating the series for `log ω` and `log 9` after `i` terms determines `N(ω)` modulo `2^(3i - ⌊log_2 i⌋ - 3)` or better, so any fixed number of `2`-adic digits of `N(ω)` is obtained by finitely many ring operations. As a cross-check, the series gives

```text
N(17) ≡ 38 (mod 2^8),   N(25) ≡ 245 (mod 2^8),   N(33) ≡ 236 (mod 2^8),
```

each agreeing with the congruence-defined classes `n_k`; note `N(17) ≡ 6 (mod 8)` matches the first visible lifting class `d ≡ 12 (mod 16)` of the family `ω = 17`, and `N(33) ≡ 4 (mod 8)` matches the companion-anchor computation of Proposition `11.8.1.7.2`.

**Remark (companion anchors).** On the odd lifting component the same formula reads

```text
N(3ω) = - log(3ω) / log 9 = - (log 3ω) / log 9,
```

which is well-defined because `3ω ≡ 1 (mod 8)` there; no logarithm of `3` itself is ever needed.

**Remark (the isometry is the valuation engine).** Every `3 + v_2(·)` law in this section is an instance of the isometry of Lemma `11.8.3.6.5` — equivalently, of the lifting-the-exponent identity. Indeed,

```text
s = v_2(9^n ω - 1) = v_2(log(9^n ω)) = v_2(n·log 9 + log ω)
  = v_2(log 9) + v_2(n - N(ω)) = 3 + v_2(ε),
```

valid whenever `ε = n - N(ω) ≠ 0`. This one display subsumes the anchor-displacement laws proved below by elementary lifting; those elementary proofs are retained for self-containedness.

#### 11.8.3.7. The anchor map `N(ω)` as the additive coordinate on the lifting branch

The inverse-limit construction of `11.8.3.6` may now be sharpened. The compatible congruence classes do not merely define a family of finite truncations; they define the natural additive coordinate on the lifting branch. By Theorem `11.8.3.6.6` this coordinate is the (negated, base-`9`) `2`-adic logarithm, so the additive structure below is not an accident of the construction but a classical fact wearing congruence-tower clothing. Both proofs are given: the logarithmic one for concept, the elementary one for self-containedness.

**Theorem 11.8.3.7.1 (additive coordinate property of `N`).**
Let

```text
G = 1 + 8 Z_2,
```

viewed as a multiplicative subgroup of the odd `2`-adic units. For each `ω in G`, let

```text
N(ω) in Z_2
```

be the inverse-limit anchor defined in `11.8.3.6.1`, so that for every `k >= 4`,

```text
N(ω) ≡ n_k(ω) (mod 2^(k-3)),
```

where `n_k(ω)` is the unique class satisfying

```text
9^n ≡ ω^(-1) (mod 2^k).
```

Then `N` is a group isomorphism from the multiplicative group `G` to the additive group `Z_2`. Equivalently, for all `ω_1, ω_2 in G`,

```text
N(ω_1 ω_2) = N(ω_1) + N(ω_2),
```

and `N` is bijective.

**Conceptual proof (via the logarithm).**
By Theorem `11.8.3.6.6`, `N` is the composition of `log : 1 + 8 Z_2 -> 8 Z_2`, which is a group isomorphism by Lemma `11.8.3.6.5`, with division by `-log 9`, which is an isomorphism of additive groups `8 Z_2 -> Z_2` because `v_2(log 9) = 3` exactly. A composition of group isomorphisms is a group isomorphism. ∎

**Elementary proof.**
By Theorem `11.8.3.1.1`, for each `k >= 4` there is a unique class

```text
n_k(ω) (mod 2^(k-3))
```

satisfying

```text
9^n ≡ ω^(-1) (mod 2^k),
```

and these classes are compatible under reduction. Hence `N(ω)` is well-defined as an element of `Z_2`.

To prove the homomorphism law, fix `ω_1, ω_2 in G`. For each `k >= 4`, one has

```text
9^(n_k(ω_1)) ≡ ω_1^(-1) (mod 2^k),
9^(n_k(ω_2)) ≡ ω_2^(-1) (mod 2^k).
```

Multiplying gives

```text
9^(n_k(ω_1)+n_k(ω_2)) ≡ (ω_1 ω_2)^(-1) (mod 2^k).
```

By uniqueness of the level-`k` solution class,

```text
n_k(ω_1 ω_2) ≡ n_k(ω_1) + n_k(ω_2) (mod 2^(k-3)).
```

Passing to the inverse limit yields

```text
N(ω_1 ω_2) = N(ω_1) + N(ω_2).
```

Injectivity follows immediately: if `N(ω) = 0`, then for every `k >= 4`,

```text
0 ≡ n_k(ω) (mod 2^(k-3)),
```

so

```text
9^0 ≡ ω^(-1) (mod 2^k),
```

hence

```text
ω ≡ 1 (mod 2^k)
```

for all `k >= 4`. Therefore `ω = 1` in `Z_2`.

For surjectivity, let `n in Z_2`. For each `k >= 4`, define

```text
ω_k ≡ 9^(-n mod 2^(k-3)) (mod 2^k).
```

Since every power of `9` lies in `1 + 8 Z / 2^k Z`, each `ω_k` lies in that subgroup, and the classes are compatible under reduction. Hence they determine a unique element

```text
ω in 1 + 8 Z_2.
```

By construction, for every `k >= 4`,

```text
9^n ≡ ω^(-1) (mod 2^k),
```

so by uniqueness,

```text
N(ω) ≡ n (mod 2^(k-3))
```

for all `k >= 4`. Therefore `N(ω) = n`.

Thus `N` is a group isomorphism

```text
N : 1 + 8 Z_2 -> Z_2.
```

∎

**Interpretation.**
The family-dependent primary branch is therefore not best viewed as a sequence of unrelated finite congruence classes. It is the truncation of a single additive `2`-adic coordinate on the lifting branch — explicitly, `N(ω) = -log ω / log 9`.

In this language, the ratio law of Theorem `11.8.3.5.1` is simply the statement that relative branch placement is given by subtraction of logarithms:

```text
N(ω_2) - N(ω_1) = -(log ω_2 - log ω_1) / log 9.
```

#### 11.8.3.8. Anchor-displacement reformulation of spike height

The additive-coordinate theorem of `11.8.3.7.1` shows that the family-dependent anchor is not merely an inverse-limit bookkeeping device. It is the negated base-`9` `2`-adic logarithm (Theorem `11.8.3.6.6`), and hence the natural exponent-side coordinate on the lifting branch

```text
ω ≡ 1 (mod 8).
```

The next step is to rewrite the spike-height problem directly in that coordinate.

By Definition `11.8.3.6.1`, the global anchor `N(ω)` is characterized by the compatible congruences

```text
9^(N(ω)) ≡ ω^(-1) (mod 2^k)
```

at every finite level. Since these congruences are compatible for all `k >= 4`, they assemble in `Z_2` to the identity

```text
9^(N(ω)) = ω^(-1)
```

inside the multiplicative group

```text
1 + 8 Z_2.
```

Equivalently,

```text
ω = 9^(-N(ω)).
```

Now remain on the lifting branch and write

```text
d = 2n.
```

Then

```text
ω·3^d - 1 = ω·9^n - 1.
```

Substituting the anchor form of `ω` gives

```text
ω·3^d - 1
= 9^(-N(ω)) 9^n - 1
= 9^(n - N(ω)) - 1.
```

So the lifting-branch valuation problem may be rewritten exactly as

```text
v_2(ω·3^(2n) - 1) = v_2(9^(n - N(ω)) - 1).
```

**Proposition 11.8.3.8.1 (anchor-displacement form of the valuation law).**
Let `ω` be odd with

```text
ω ≡ 1 (mod 8),
```

and let `d = 2n` be even. Then

```text
v_2(ω·3^d - 1) = v_2(9^(n - N(ω)) - 1).
```

Equivalently, if one defines the anchor displacement

```text
ε = n - N(ω) in Z_2,
```

then

```text
v_2(ω·3^d - 1) = v_2(9^ε - 1).
```

**Proof.**
The identity

```text
ω = 9^(-N(ω))
```

holds in `1 + 8 Z_2` by the defining property of `N(ω)`. Therefore, for `d = 2n`,

```text
ω·3^d - 1
= ω·9^n - 1
= 9^(-N(ω)) 9^n - 1
= 9^(n - N(ω)) - 1.
```

Taking `v_2` of both sides gives the result. ∎

**Interpretation.**
The valuation is no longer best viewed as depending on two independent pieces of data, namely the family parameter `ω` and the exponent `n`. It depends only on the single displacement variable

```text
ε = n - N(ω).
```

So the family dependence on the lifting branch has been absorbed into translation by the anchor coordinate. Combined with the isometry remark of `11.8.3.6`, this yields `v_2(9^ε - 1) = 3 + v_2(ε)` in one step; the elementary derivation below reaches the same law without logarithms.

#### 11.8.3.9. Boundary-shell term in anchor-displacement form

The boundary-shell correction term of `11.8.3.4` is not independent of the global anchor coordinate `N(ω)`. It is exactly the valuation shadow of the normalized anchor truncation error.

**Theorem 11.8.3.9.1 (anchor-displacement form of spike height).**
Let `ω ≡ 1 (mod 8)` and let `d_* = 2n_*` be an even branch point. Define

```text
e = n_* - N(ω) in Z_2.
```

If `e ≠ 0`, then

```text
v_2(ω·3^(d_*) - 1) = v_2(9^e - 1) = 3 + v_2(e).
```

In particular, if

```text
H = v_2(ω·3^(d_*) - 1),
```

then

```text
e = 2^(H-3) q
```

for a unique odd `2`-adic unit `q`.

**Proof.**
By Proposition `11.8.3.8.1`,

```text
ω·3^(d_*) - 1 = 9^e - 1.
```

Now `9^x ≡ 1 (mod 2^k)` holds if and only if `x ≡ 0 (mod 2^(k-3))`, since `9` has
exact order `2^(k-3)` modulo `2^k`. Therefore

```text
v_2(9^e - 1) = 3 + v_2(e).
```

This proves the claim. ∎

**Interpretive bridge.**
The anchor-displacement reformulation makes the primary branch transparent. On the exponent side, the primary branch is precisely the zero-displacement locus

```text
n = N(ω),
```

and a finite spike occurs because the chosen integer branch point `n_*` only approximates that `2`-adic anchor. The spike height is therefore not an independent datum layered on top of the branch: it measures the valuation of the anchor truncation error

```text
e = n_* - N(ω).
```

So the natural local variable is displacement from the global anchor itself, not merely displacement from a selected finite spike location.

**Theorem 11.8.3.9.2 (boundary-shell valuation in anchor-error coordinates).**
Retain the notation above, and let

```text
Δ = 2^(H-2) t
```

with `t` odd. Then

```text
v_2(ω·3^(d_* + Δ) - 1) = H + v_2(q + t).
```

Equivalently, if `B_H(u,t)` is the boundary-shell correction term of
Definition `11.8.3.4.1`, then

```text
v_2(B_H(u,t)) = v_2(q+t).
```

**Proof.**
Since `d_* = 2n_*`, the exponent-side displacement corresponding to `Δ` is

```text
Δ/2 = 2^(H-3)t.
```

Hence

```text
ω·3^(d_* + Δ) - 1
= ω·9^(n_* + Δ/2) - 1
= 9^(e + 2^(H-3)t) - 1.
```

Writing `e = 2^(H-3)q` gives

```text
ω·3^(d_* + Δ) - 1 = 9^(2^(H-3)(q+t)) - 1.
```

Applying Theorem `11.8.3.9.1` yields

```text
v_2(ω·3^(d_* + Δ) - 1)
= 3 + v_2(2^(H-3)(q+t))
= H + v_2(q+t).
```

Comparing with

```text
v_2(ω·3^(d_* + Δ) - 1) = H + v_2(B_H(u,t))
```

gives

```text
v_2(B_H(u,t)) = v_2(q+t).
```

∎

**Interpretation.**
The boundary-shell correction term is therefore not a new family-dependent invariant.
Its valuation is completely determined by the normalized anchor truncation error `q`
together with the universal shell coordinate `t`. What survives beyond spike height
is not a second invariant independent of the anchor, but the odd part of the anchor
displacement itself.

#### 11.8.3.10. Synthesis statement

Taken together, the preceding results give the formal Stage 1 synthesis on the lifting branch:

```text
family-dependent anchor N(ω) = -log ω / log 9
+ exact global valuation law s = 3 + v_2(n - N(ω)).
```

This is the formal endpoint of Stage 1 on the lifting branch, up to one further external input: an unconditional upper bound on how large `v_2(n - N(ω))` can be at a given depth, imported next.

#### 11.8.3.11. Effective bounds: contact with `p`-adic Baker theory

The exact law is complete but relative: it expresses `s` through `v_2(n - N(ω))` without bounding that quantity as a function of `n`. The logarithmic identification places exactly this question inside a classical effective theory.

By Theorem `11.8.3.6.6` and the isometry of Lemma `11.8.3.6.5`, for `d = 2n`,

```text
s = v_2(ω·3^d - 1) = v_2(n·log 9 + log ω),
```

so `s` is the `2`-adic valuation of a linear form in two `2`-adic logarithms of fixed integers, with integer coefficients `(n, 1)`. Equivalently, in exponential form, `s = v_2(9^n·ω - 1)` measures the `2`-adic distance of a two-term power product from `1`. Effective upper bounds for exactly such quantities are the subject of `p`-adic Baker theory: linear forms in `p`-adic logarithms (Yu), with sharper two-logarithm bounds by Bugeaud–Laurent via Padé approximation.

[#TODO cite precisely at formal writeup: K. Yu, *Linear forms in p-adic logarithms* I–III (Compositio Math. 1990, ...); Y. Bugeaud, M. Laurent, *Minoration effective de la distance p-adique entre puissances de nombres algébriques*, J. Number Theory 61 (1996), 311–342.]

**Imported bound (qualitative form).** For each fixed odd `ω ≡ 1 (mod 8)` there is an effectively computable constant `C(ω)` such that for all `n >= 2`,

```text
v_2(9^n·ω - 1) <= C(ω) · (log n)^2.
```

The exponent `2` is the conservative shape given by the general two-logarithm statements; particular variants and parameter regimes yield `log n`. Every use below survives with either exponent. [#TODO: pin the exponent to the precise theorem version at formal writeup.]

**Corollary 11.8.3.11.1 (unconditional spike-height bound).** On both lifting components, spike heights grow at most polylogarithmically in depth: there is an effective `C(ω)` with

```text
s(ω, d) <= C(ω) · (log d)^2      for all d >= 2,
```

hence `max_(d <= D) s = O((log D)^2)` for each family, unconditionally.

**Proof.** On the even component `d = 2n` this is the imported bound directly. On the odd component `d = 2n + 1`, Proposition `11.8.1.7.2` gives `s = v_2(9^n·(3ω) - 1)`, and the imported bound applies to the companion parameter `3ω`. ∎

**Corollary 11.8.3.11.2 (effective irrationality measure for the anchor).** For every integer `n >= 2`,

```text
v_2(n - N(ω)) <= C(ω) · (log n)^2 - 3.
```

Equivalently: an integer of size `n` can match at most `O((log n)^2)` leading `2`-adic digits of `N(ω)`. This is the first unconditional statement about the anchor digits in this note — an effective `2`-adic irrationality measure for `-log ω / log 9`.

**Proof.** Immediate from the imported bound and `s = 3 + v_2(n - N(ω))`. ∎

**Remark (relation to known cycle-length bounds).** This is not a new toolbox invented for the present program. Effective linear forms in logarithms — Archimedean forms in `log 2, log 3` and their `p`-adic counterparts, combined with de Weger's lattice-reduction methods — are exactly what underlies the known lower bounds on the length of hypothetical nontrivial Collatz cycles (Steiner; Simons–de Weger). Route A's Stage 1 thus terminates on the same classical ground as the strongest known partial results on the cycle side. [#TODO cite: R. Steiner (1977); J. Simons, B. de Weger, *Theoretical and computational bounds for m-cycles of the 3n+1 problem* (2005).]

**Remark (what the constants are and are not good for).** The constants `C(ω)` are effectively computable but astronomically large. They are useful for unconditional asymptotic statements — spike heights cannot grow like a power of `d`, digit matches cannot persist — and useless for window computations, where the exact law plus direct series computation of `N(ω)` (Remark after Theorem `11.8.3.6.6`) is strictly better.

**Remark (Stage 3 relevance).** The valuation `s` enters the depth evolution through `d_+ = v_2(C) - s + v_3(C)`. An unconditional cap on `s` at given depth therefore bounds one term of the depth-evolution law before Stage 3 begins; this is recorded here for later use.

Section `11.8.4` separates what this synthesis has genuinely reduced from what remains open.

### 11.8.4. What Stage 1 has reduced and what remains

The purpose of `11.8.3` was to state the formal Stage 1 synthesis on the lifting branch directly. The purpose of the present subsection is different. It is to say, as clearly as possible, what that synthesis has already reduced, what parts of the picture are imported from classical theory, and where the true remaining bottleneck now lies.

This distinction matters because the Route A program has shifted. The central open problem is no longer whether the lifting branch possesses a family-dependent primary branch, nor whether the valuation is controlled by anchor displacement — those points are now formal, exact, and global. The remaining issue is the conversion of that valuation control into genuinely dynamical control of the reduced step.

#### 11.8.4.1. What Stage 1 has formally reduced

The formal results of `11.8.3` show that, on the lifting branch — the even component

```text
ω ≡ 1 (mod 8),   d = 2n,
```

and, via the companion parameter `ω̃ = 3ω` of Proposition `11.8.1.7.2`, equally the odd component

```text
ω ≡ 3 (mod 8),   d = 2n + 1,
```

— the valuation problem has already been reduced much further than the earlier tower map alone suggested.

First, the family-dependent object is now formal: for each valid lifting family, there is a unique compatible primary congruence branch

```text
n_k(ω),   d_k^*(ω) = 2n_k(ω),
```

and these finite truncations assemble into the global `2`-adic anchor

```text
N(ω) in Z_2,
```

equivalently the depth-side anchor

```text
D^*(ω) = 2N(ω).
```

Second, that anchor is not merely an inverse-limit bookkeeping device. It is the natural additive coordinate on the lifting branch, identified exactly as `N(ω) = -log ω / log 9` in the `2`-adic logarithm. So the primary family dependence has already been compressed into a single classical arithmetic quantity: the `2`-adic logarithm of the family parameter.

Third, the valuation law is not merely local. Combining the anchor-displacement identity of Proposition `11.8.3.8.1` with the isometry of Lemma `11.8.3.6.5` gives the exact global law

```text
s = v_2(ω·3^(2n) - 1) = 3 + v_2(n - N(ω))    for every n with n ≠ N(ω),
```

with the odd component covered verbatim through the companion anchor `N(3ω)`. Every earlier partial statement — the centered halo law below spike height (`11.8.3.2.1`), the boundary-shell localization (`11.8.3.3.1`), and the boundary-shell valuation law `v_2(B_H(u,t)) = v_2(q+t)` (`11.8.3.9.2`) — is a finite-truncation shadow of this one law: centering at an integer branch point `n_*` merely re-expresses `v_2(n - N(ω))` through the digit interaction between the displacement and the anchor error `n_* - N(ω)`.

Taken together, Stage 1 has formally reduced the lifting-branch valuation picture to:

```text
family-dependent anchor N(ω) = -log ω / log 9
+ exact global valuation law s = 3 + v_2(n - N(ω)).
```

That is the main formal output of Stage 1, and on the `s`-side it is complete.

#### 11.8.4.2. What remains empirical

On the `s`-side: nothing. The global law of `11.8.4.1` is exact for every family on both lifting components, so the visible tower geometries recorded in `11.8.2` — dense and sparse refinement patterns, translated shells, centered halo templates — are fully accounted for. Each is a finite-window shadow of the one universal law translated by the family anchor. The observations that once seemed to demand separate mechanisms are preserved in Appendix `A.4`–`A.5` as discovery-path records, not as open phenomena.

Exactly one empirical statement survives, and it faces outward rather than inward: the digit statistics of the anchors `N(ω)` are consistent with fair-coin behavior (digit density `0.497` across `2,499` families; Appendix `A.4.6`), as expected for `2`-adic logarithms of integers. Confirming or refining that expectation is a question about classical `p`-adic analysis, not about the Collatz reduction, and nothing in the later stages depends on resolving it. Nor is it entirely out of reach: `p`-adic Baker theory already supplies an unconditional effective floor — an integer of size `n` matches at most `O((log n)^2)` leading anchor digits (Corollary `11.8.3.11.2`). What lies beyond current theory is only the finer statistical behavior.

#### 11.8.4.3. What remains genuinely open

After the Stage 1 synthesis, exactly two questions on the lifting branch remain open, and only the second lies on Route A's critical path.

**(a) Intrinsic form of the correction term beyond valuation.**
At the valuation level, the boundary-shell refinement is already reduced to anchor error. What remains open is whether the correction term itself admits a cleaner intrinsic identification beyond its valuation shadow.

In particular, one may now ask not merely for

```text
v_2(B_H(u,t)),
```

but for a more direct structural meaning of

```text
B_H(u,t)
```

itself.

The effective bounds of `11.8.3.11` constrain this question quantitatively: within any depth window `d <= D`, every valuation the correction term can influence is capped at `C(ω)·(log D)^2`, so an intrinsic identification, if one exists, must operate entirely within that polylogarithmic range.

**(b) Conversion from valuation synthesis to reduced dynamics.**
Most importantly, the Stage 1 synthesis is still a valuation theorem package. The reduced map is governed not only by

```text
s = v_2(3^d ω - 1),
```

but also by the derived quantity

```text
C = 3^d ω - 1 + 2^s.
```

So even if the lifting-branch valuation picture is largely understood, that alone does not yet classify the next reduced step. The remaining work is to convert the valuation synthesis into information about:

* `3`-gain,
* depth evolution
  `d_+ = v_2(C) - s + v_3(C)`,
* and only later the refined odd core `ω_+`.

This is why the next stages of Route A remain dynamical rather than purely valuation-theoretic. The required passage is:

```text
anchor-displacement valuation control
    -> parity of s and 3-gain
    -> control of C
    -> laws for d_+
    -> only then a sharper description of ω_+.
```

**Closing note: two former entries of this ledger.** Earlier drafts carried two further open questions here. Both are closed. The globalization of the off-spike halo law is resolved positively: the anchor-displacement law `s = 3 + v_2(n - N(ω))` is globally exact (`11.8.4.1`), so the once-open possibility of new structure beyond the proved local range is excluded. The classification of tower types is resolved by dissolution: there are no types, only the digit density of the anchor, and the once-conjectured mod-`3` classifier is refuted by computation (Remark `11.8.1.8.4`; historical record and audit data in Appendix `A.4.6`).

#### 11.8.4.4. #TODO: renumber

#### 11.8.4.5. Compact status snapshot

At this point, the status of the Route A program may be summarized as follows.

```text
formal:
    primary congruence branch,
    global anchor N(ω) = -log ω / log 9  (2-adic logarithm),
    exact global valuation law s = 3 + v_2(n - N(ω)), both lifting components,
    uniform 3-gain law on the lifting branch,
    unconditional polylog spike-height bound (imported: p-adic Baker theory)

dissolved or exported:
    tower-type classification (no dichotomy: anchor digit density),
    digit behavior of the anchors (classical: digits of 2-adic logarithms;
        effective floor imported, finer statistics beyond current theory)

open:
    intrinsic form of the correction term beyond valuation,
    control of C,
    laws for d_+,
    eventual refinement of ω_+
```

The first part of the conversion from valuation synthesis to reduced dynamics is now complete. Section `11.8.5` proves the exact `3`-gain law for all families on both components of the lifting branch,

```text
ω ≡ 1 (mod 8), d even    and    ω ≡ 3 (mod 8), d odd,
```

with the `ω = 1` case and the spike-level criterion as explicit corollaries.

However, this does not yet classify the full reduced transition. The reduced map is still governed by the derived quantity

```text
C = 3^d ω - 1 + 2^s,
```

and the next depth satisfies

```text
d_+ = v_2(C) - s + v_3(C).
```

Thus the conversion from valuation theory to reduced dynamics is only partially complete:

```text
completed:
    parity of s,
    3-gain

still open:
    control of C,
    laws for d_+,
    eventual refinement of ω_+
```

This compact snapshot should be read only as a checkpoint. Its purpose is not to replace the fuller discussion of `11.8.4.1`–`11.8.4.4`, but to gather the current state of the program into one visible ledger before Route A passes from Stage 2 into the later dynamical stages.

#### 11.8.4.6. Transition to Stage 2

Under this interpretation, the next step of Route A is forced.

Since Section `9.3` shows that the parity of

```text
s = v_2(3^d ω - 1)
```

already determines whether the next odd seed gains a factor of `3`, any exact valuation theorem immediately becomes a dynamical theorem about `3`-gain.

So the natural continuation after Stage 1 is not to remain indefinitely inside tower language. It is to convert the newly formal valuation structure into reduced-dynamical outputs.

That is the purpose of `11.8.5`.

### 11.8.5. Stage 2: The `3`-gain law on the lifting branch

Stage 2 is the first completed conversion of the Stage 1 valuation synthesis into a reduced-dynamical statement.

Section `9.3` proved that the parity of

```text
s = v_2(3^d ω - 1)
```

controls whether the next odd seed gains a factor of `3`. Stage 1 then rewrote the lifting-branch valuation in anchor-displacement form. Combining these two results gives an exact `3`-gain criterion on the lifting branch.

Thus the purpose of this section is no longer merely to propose `3`-gain theorem targets. It is to record the first successful dynamical consequence of the anchor formalism:

```text
on the lifting branch, 3-gain is controlled by the parity of v_2(n - N(·)),
```

where the anchor parameter is `ω` on the even component and the companion `ω̃ = 3ω` on the odd component.

More precisely, for the even component

```text
ω ≡ 1 (mod 8),   d = 2n,
```

with anchor displacement

```text
ε = n - N(ω),
```

and for the odd component

```text
ω ≡ 3 (mod 8),   d = 2n + 1,
```

with anchor displacement

```text
ε̃ = n - N(3ω),
```

the next odd seed gains a factor of `3` exactly when the relevant `v_2(ε)` (resp. `v_2(ε̃)`) is odd.

This is a genuine reduction of the dynamics. Once the family anchor `N(ω)` is fixed, the `3`-gain pattern is determined by dyadic shell parity around that anchor; no further family-specific input enters.

What remains open is not the `3`-gain trigger itself, but the later dynamical data carried by

```text
C = 3^dω - 1 + 2^s,
```

especially the quantities

```text
v_2(C) - s,
v_3(C),
d_+,
ω_+.
```

So Stage 2 closes the first conversion step from valuation theory to reduced dynamics, while preparing the handoff to Stage 3.

#### 11.8.5.1. The key bridge from Stage 1

Two results from Stage 1 now compose directly.

The first is Lemma `9.3.1`: `3`-gain occurs at depth `d` if and only if `s = v_2(3^d ω - 1)` is even.

The second is the anchor-displacement valuation law of Theorem `11.8.3.9.1`: for `ω ≡ 1 (mod 8)` and `d = 2n`, defining the anchor displacement

```text
ε = n - N(ω)  in  Z_2,
```

one has

```text
s = v_2(ω · 3^d - 1) = 3 + v_2(ε)
```

whenever `ε ≠ 0`.

Combining these two results requires no additional argument.

#### 11.8.5.2. Uniform 3-gain law on the lifting branch

**Theorem 11.8.5.2.1 (3-gain law on the lifting branch).** Let `ω ≡ 1 (mod 8)`, let `d = 2n` be even, and define the anchor displacement

```text
ε = n - N(ω)  in  Z_2.
```

If `ε ≠ 0`, then `3`-gain occurs at depth `d` if and only if `v_2(ε)` is odd.

**Proof.** By Theorem `11.8.3.9.1`,

```text
s = 3 + v_2(ε).
```

By Lemma `9.3.1`, `3`-gain occurs if and only if `s` is even. Since `3` is odd,

```text
s even  iff  v_2(ε) odd.
```

∎

**Corollary 11.8.5.2.2 (3-gain law on the odd component).** Let `ω ≡ 3 (mod 8)` with `3 ∤ ω`, let `d = 2n + 1` be odd, and define the companion anchor displacement

```text
ε̃ = n - N(3ω)  in  Z_2,
```

where `N(3ω)` is the global anchor of Definition `11.8.3.6.1` attached to the companion parameter `ω̃ = 3ω ≡ 1 (mod 8)`.

If `ε̃ ≠ 0`, then

```text
s = v_2(3^d ω - 1) = 3 + v_2(ε̃),
```

and `3`-gain occurs at depth `d` if and only if `v_2(ε̃)` is odd.

**Proof.** By Proposition `11.8.1.7.2`, `3^d ω = 9^n ω̃` with `ω̃ = 3ω ≡ 1 (mod 8)`, so

```text
s = v_2(3^d ω - 1) = v_2(ω̃ · 3^(2n) - 1).
```

The anchor-displacement valuation law of Theorem `11.8.3.9.1` applies to the parameter `ω̃` (its hypotheses are only that the parameter is odd and `≡ 1 (mod 8)`; `3 ∤ ω̃` is not required), giving `s = 3 + v_2(ε̃)` whenever `ε̃ ≠ 0`. By Lemma `9.3.1`, applied to the genuine reduced state `(ω, d)`, `3`-gain occurs if and only if `s` is even, i.e. if and only if `v_2(ε̃)` is odd. ∎

**Worked check.** For `(ω, d) = (11, 1)`: `n = 0`, `ω̃ = 33`, `N(33) ≡ 4 (mod 8)`, so `v_2(ε̃) = 2` and `s = 5` — no `3`-gain, matching `A = 32` directly. For `(ω, d) = (11, 5)`: `n = 2`, `ε̃ = 2 - N(33)` has `v_2 = 1`, so `s = 4` and `3`-gain occurs — matching `3^5 · 11 - 1 = 2672 = 2^4 · 167` directly.

**Interpretation.** The `3`-gain question on the lifting branch is completely determined by the parity of `v_2(ε)`, which measures how closely `n` approximates the relevant anchor (`N(ω)` on the even component, `N(3ω)` on the odd component) in `2`-adic terms. Once that anchor is known, the `3`-gain pattern at every non-anchor depth is explicit.

In particular, the non-anchor depths partition into two infinite sets according to the parity of `v_2(ε)`: the `3`-gain set consists of all depths where `v_2(ε)` is odd, and the no-`3`-gain set consists of all depths where `v_2(ε)` is even. This is a partition by dyadic shell parity, not a sequential alternation in `d`.

#### 11.8.5.3. Anchor-free formulation: the `ω = 1` case

The family `ω = 1` is distinguished by having anchor `N(1) = 0`, since `9^0 = 1 = 1^(-1)` in `1 + 8 Z_2`. The anchor displacement therefore reduces to `ε = n`, and Theorem `11.8.5.2.1` yields an explicit closed form.

**Corollary 11.8.5.3.1 (3-gain law for `ω = 1`).** For `ω = 1` and even `d = 2n` with `n ≠ 0`, `3`-gain occurs if and only if `v_2(n)` is odd. Equivalently, `3`-gain occurs if and only if `v_2(d)` is even and at least `2`.

**Proof.** Set `N(1) = 0` in Theorem `11.8.5.2.1`. Then `ε = n`, and the condition is `v_2(n)` odd. For the equivalent statement in `d`: since `d = 2n` one has `v_2(d) = 1 + v_2(n)`, so `v_2(n)` is odd if and only if `v_2(d)` is even and at least `2`. ∎

This is consistent with Proposition `9.4.1`, which gives `s = 2 + v_2(d)`, making `s` even precisely when `v_2(d)` is even.

#### 11.8.5.4. 3-gain at spike depths

A level-`k` spike is a depth `d_* = 2n_*` for which

```text
v_2(n_* - N(ω)) = k - 3,
```

equivalently `s = k`. By Theorem `11.8.5.2.1`, `3`-gain occurs at this spike depth if and only if `k - 3` is odd, equivalently if and only if `k` is even.

**Corollary 11.8.5.4.1 (spike-level `3`-gain criterion).** At a level-`k` spike depth on the lifting branch, `3`-gain occurs if and only if `k` is even.

This criterion is exact and readable directly from the spike level, without computing `s` at the depth. It applies uniformly to all lifting-branch families, and — via Corollary `11.8.5.2.2`, with spike depths `d_* = 2n_* + 1` and `v_2(n_* - N(3ω)) = k - 3` — equally on the odd component.

#### 11.8.5.5. Scope and the remaining open question

Theorem `11.8.5.2.1` and Corollary `11.8.5.2.2` together cover both components of the lifting branch as defined in `11.8.1.8.2`: odd `ω ≡ 1 (mod 8)` with `d` even, and odd `ω ≡ 3 (mod 8)` with `d` odd. The remaining residue-parity classes of Proposition `11.8.1.4.1` — namely `(ω ≡ 1, d odd)`, `(ω ≡ 5, any d)`, `(ω ≡ 7, any d)`, and `(ω ≡ 3, d even)` — have `s` pinned at `1` or `2` at the first layer; for these, the parity of `s`, and hence `3`-gain, is decided outright by the mod `8` classification, and no anchor machinery is needed.

What the theorem does not close is the arithmetic of the anchor itself. By Theorem `11.8.3.6.6`, the anchors in question are the quantities

```text
N(ω) = -log ω / log 9,   N(3ω) = -log(3ω) / log 9,
```

so the remaining open question is precisely: describe the `2`-adic digit patterns of logarithms of small integers. This calibrates expectations. Digit questions about `p`-adic logarithms of integers belong to transcendence theory, are expected to be genuinely hard, and the digits themselves are expected to behave pseudo-randomly. The effective side of that theory is not empty — `p`-adic Baker theory yields the unconditional polylogarithmic bounds of `11.8.3.11`, which cap spike heights and digit matches — but the finer statistics remain out of reach. The anchor formalism should therefore be valued for the reduction it achieves — the entire `3`-gain pattern of a family is compressed into one classical `2`-adic number, computable to any precision by a convergent series — rather than for the prospect of a closed-form description of that number's digits.

The `3`-gain law is therefore closed as a formal theorem on the entire lifting branch. What remains open on the anchor side is expected to remain open: any further "arithmetic organization" of the digits of `N(ω)` would constitute progress on the digit behavior of `2`-adic logarithms, a problem independent of, and older than, the present program.

### 11.8.6. Stage 3: First Decomposition of `C`

Stage 2 classified the first dynamical consequence of the valuation

```text
s = v_2(3^dω - 1),
```

namely whether the next odd seed gains a factor of `3`. The next stage is to move from the parity of `s` to the actual depth evolution of the next reduced state.

Recall that the reduced map is governed by

```text
A = 3^dω - 1,
s = v_2(A),
C = A + 2^s,
```

with

```text
d_+ = v_2(C) - s + v_3(C).
```

Thus Stage 3 does not begin by trying to classify the full odd core `ω_+`. It begins by decomposing the next depth into its two valuation components:

```text
m_+ = v_2(C) - s,
a_+ = v_3(C),
d_+ = m_+ + a_+.
```

This separates the Stage 3 problem into two parts:

```text
2-adic entry-depth problem:      m_+ = v_2(C) - s,
3-adic absorption problem:       a_+ = v_3(C).
```

The second of these is more immediately accessible, because `C` can also be written as

```text
C = 3^dω + (2^s - 1),
```

which exposes its `3`-adic structure. The first remains the harder entry-depth problem, since it asks how close the odd exit lies to `-1` in the `2`-adic sense.

The purpose of this section is therefore to make the first decomposition of `C` explicit, then isolate the part of Stage 3 that can be attacked before attempting a full classification of `d_+`.

#### 11.8.6.1. Exit-unit normalization of `C`

Let

```text
A = 3^dω - 1,
s = v_2(A),
x_exit = A / 2^s.
```

Then

```text
A = 2^s x_exit.
```

Since

```text
C = A + 2^s,
```

one obtains

```text
C = 2^s x_exit + 2^s
  = 2^s(x_exit + 1).
```

Therefore

```text
v_2(C) = s + v_2(x_exit + 1),
```

and hence

```text
v_2(C) - s = v_2(x_exit + 1).
```

But the next-entry depth is exactly

```text
m_+ = v_2(x_exit + 1),
```

so this recovers

```text
m_+ = v_2(C) - s.
```

Likewise, since multiplication by `2^s` does not affect `3`-adic valuation,

```text
v_3(C) = v_3(x_exit + 1).
```

Thus the next `3`-adic absorption is

```text
a_+ = v_3(C) = v_3(x_exit + 1).
```

Combining these gives the normalized depth formula

```text
d_+ = v_2(x_exit + 1) + v_3(x_exit + 1).
```

Equivalently,

```text
d_+ = m_+ + a_+,
```

where

```text
m_+ = v_2(x_exit + 1),
a_+ = v_3(x_exit + 1).
```

This normalization shows that Stage 3 is not merely a problem about the formal expression

```text
C = 3^dω - 1 + 2^s.
```

It is the problem of understanding the arithmetic of the next entry quantity

```text
x_exit + 1.
```

In particular:

```text
m_+ = v_2(x_exit + 1)
```

measures the `2`-adic proximity of the odd exit to `-1`, while

```text
a_+ = v_3(x_exit + 1)
```

measures how much `3`-adic content is absorbed into the next reduced depth.

So the first Stage 3 decomposition is:

```text
Stage 3A: classify v_3(C), equivalently v_3(x_exit + 1);
Stage 3B: classify v_2(C) - s, equivalently v_2(x_exit + 1).
```

The next subsection begins with Stage 3A, because the identity

```text
C = 3^dω + (2^s - 1)
```

makes the `3`-adic part of `C` accessible before the harder `2`-adic entry-depth problem is solved.

#### 11.8.6.2. Exact `3`-adic law for `C`

The `3`-adic part of `C` is more accessible than the `2`-adic entry-depth part because

```text
C = A + 2^s
  = 3^dω - 1 + 2^s
  = 3^dω + (2^s - 1).
```

Since `3 ∤ ω`, the first summand has exact `3`-adic valuation

```text
v_3(3^dω) = d.
```

Thus the only additional input needed is the `3`-adic valuation of

```text
2^s - 1.
```

Define

```text
h(s) = v_3(2^s - 1).
```

Then:

```text
h(s) =
    0,              if s is odd,
    1 + v_3(s),     if s is even.
```

Indeed, if `s` is odd, then `2^s ≡ -1 (mod 3)`, so

```text
2^s - 1 ≠ 0 (mod 3),
```

and hence `h(s) = 0`.

If `s` is even, the standard lifting law gives

```text
v_3(2^s - 1) = v_3(2^2 - 1) + v_3(s/2)
             = v_3(3) + v_3(s)
             = 1 + v_3(s).
```

This gives an exact comparison law for the `3`-adic contribution to the next depth.

**Proposition 11.8.6.2.1 (exact `3`-adic law for `C`).**
Let

```text
A = 3^dω - 1,
s = v_2(A),
C = A + 2^s.
```

Assume `3 ∤ ω`, and define

```text
h(s) = v_3(2^s - 1).
```

Then:

1. if

   ```text
   h(s) < d,
   ```

   then

   ```text
   v_3(C) = h(s);
   ```

2. if

   ```text
   h(s) > d,
   ```

   then

   ```text
   v_3(C) = d;
   ```

3. if

   ```text
   h(s) = d,
   ```

   then

   ```text
   v_3(C) = d + v_3(ω + β),
   ```

   where

   ```text
   β = (2^s - 1)/3^d.
   ```

**Proof.**
Using

```text
C = 3^dω + (2^s - 1),
```

the two summands have `3`-adic valuations

```text
v_3(3^dω) = d
```

and

```text
v_3(2^s - 1) = h(s).
```

If `h(s) < d`, the two summands have distinct `3`-adic valuations, and the smaller valuation dominates. Therefore

```text
v_3(C) = h(s).
```

If `h(s) > d`, the same argument gives

```text
v_3(C) = d.
```

It remains only to consider the resonant case

```text
h(s) = d.
```

Then both summands are divisible by exactly `3^d` before possible cancellation. Since `3 ∤ ω`, and since

```text
β = (2^s - 1)/3^d
```

is an integer, one may factor

```text
C = 3^dω + (2^s - 1)
  = 3^d(ω + β).
```

Hence

```text
v_3(C) = d + v_3(ω + β).
```

This proves the trichotomy. ∎

Since

```text
a_+ = v_3(C),
```

this proposition gives an exact law for the `3`-adic absorption component of the next reduced depth.

In particular, away from the resonant comparison

```text
h(s) = d,
```

the next `3`-adic absorption is simply

```text
a_+ = min(d, h(s)).
```

The only case in which additional `3`-adic cancellation can occur is the resonant case

```text
h(s) = d,
```

where the residual unit

```text
ω + (2^s - 1)/3^d
```

must be examined.

**Corollary 11.8.6.2.2 (non-resonant `3`-gain magnitude).**
If `s` is even and

```text
1 + v_3(s) < d,
```

then

```text
v_3(C) = 1 + v_3(s).
```

Equivalently, in this non-resonant range,

```text
a_+ = 1 + v_3(s).
```

**Proof.**
If `s` is even, then

```text
h(s) = v_3(2^s - 1) = 1 + v_3(s).
```

The hypothesis says exactly that

```text
h(s) < d.
```

Therefore Proposition `11.8.6.2.1` gives

```text
v_3(C) = h(s) = 1 + v_3(s).
```

Since `a_+ = v_3(C)`, the result follows. ∎

**Corollary 11.8.6.2.3 (no `3`-absorption when `s` is odd).**
If `s` is odd, then

```text
v_3(C) = 0.
```

Equivalently, the next odd seed gains no factor of `3`.

**Proof.**
If `s` is odd, then

```text
h(s) = v_3(2^s - 1) = 0.
```

Since `d >= 1`, one has

```text
h(s) < d.
```

Therefore Proposition `11.8.6.2.1` gives

```text
v_3(C) = h(s) = 0.
```

This is consistent with Lemma `9.3.1`, which states that `3`-gain occurs if and only if `s` is even. ∎

**Interpretation.**
Stage 2 classified whether `3`-gain occurs. Proposition `11.8.6.2.1` begins Stage 3 by classifying how much `3`-adic absorption occurs in the next depth, except for the resonant case where

```text
v_3(2^s - 1) = d.
```

Thus the `3`-adic component of the depth evolution is largely controlled by the comparison

```text
d
    versus
v_3(2^s - 1).
```

Using the explicit law for `h(s)`, this comparison becomes

```text
d
    versus
0
```

when `s` is odd, and

```text
d
    versus
1 + v_3(s)
```

when `s` is even.

So the first part of Stage 3 is now sharply separated from the remaining bottleneck. The `3`-adic absorption term

```text
a_+ = v_3(C)
```

is controlled by this comparison law, while the harder entry-depth term

```text
m_+ = v_2(C) - s = v_2(x_exit + 1)
```

remains the next unresolved target.

#### 11.8.6.3. Remaining bottleneck: the 2-adic entry-depth term

The preceding subsection gives the first genuine Stage 3 theorem: the `3`-adic absorption term

```text
a_+ = v_3(C)
```

is controlled by comparing

```text
d
```

with

```text
h(s) = v_3(2^s - 1).
```

Thus one part of the next-depth formula is no longer opaque.

What remains is the `2`-adic entry-depth term

```text
m_+ = v_2(C) - s.
```

Using the exit-unit normalization of `11.8.6.1`, this can be rewritten as

```text
m_+ = v_2(x_exit + 1).
```

So the remaining Stage 3 bottleneck is the problem of controlling how close the odd exit

```text
x_exit = (3^dω - 1)/2^s
```

lies to `-1` in the `2`-adic sense.

This is harder than the `3`-adic absorption problem because the identity

```text
C = 3^dω + (2^s - 1)
```

exposes the `3`-adic comparison structure directly, but does not by itself give an equally transparent law for

```text
v_2(C) - s.
```

Accordingly, the current state of Stage 3 is:

```text
partially classified:
    a_+ = v_3(C)

still open:
    m_+ = v_2(C) - s = v_2(x_exit + 1)
```

Since

```text
d_+ = m_+ + a_+,
```

a full law for `d_+` still requires control of this entry-depth term. The next live Stage 3 question is therefore not how much `3`-adic absorption occurs, but whether the `2`-adic proximity

```text
x_exit ≡ -1 mod 2^r
```

admits a comparable structural description.

### 11.8.7 Stage 4. Only Then Refine `ω_+`

The final stage is a sharper classification of the odd core

```text
ω_+ = C / (2^(v_2(C)) 3^(v_3(C))).
```

This should be treated as a later objective rather than the first one. The quantity `ω_+` is the most refined part of the next reduced state, and attempts to classify it too early are especially likely to fall into unproductive case-splitting.

Accordingly, the natural order of difficulty is:

1. control `s`,
2. understand `3`-gain,
3. obtain laws for `d_+`,
4. and only then seek a more transparent description of `ω_+`.

### 11.8.8 Strategic Summary

Route A should therefore be understood as a family-first and mechanism-first program. Its aim is to prove exact local theorems on infinite families rather than to force a premature global classification. In particular, it should privilege arguments that arise from valuation structure, periodicity with fixed modulus, or transparent arithmetic mechanisms, and it should resist the temptation to replace one unresolved quantity with endlessly increasing congruence bookkeeping.

In this sense, the decisive test for any residue-based proposal is whether it stabilizes into a theorem. If deeper and deeper residue refinement is continually required merely to preserve the appearance of regularity, then that line of investigation should be demoted to heuristic status rather than treated as a main structural advance.

Under this guarded interpretation, Route A provides a disciplined path forward: first classify valuation behavior for `s`, then convert those results into exact `3`-gain laws, then use the explicit reduced-step formula to study `d_+`, and only afterward attempt a more detailed classification of the full next reduced state.

## 11.9. Closing Perspective

The framework developed in this note still does not resolve the Collatz conjecture. But the status of the reduction has changed: the main issue is no longer whether the reduced system is mathematically legitimate, but whether its arithmetic can be classified at a deeper level.

The strongest structural questions now seem to be these:

* how to control the valuation `s = v_2(3^d ω - 1)`,
* how to classify the reduced transition more explicitly,
* how to understand the role of `3`-gain,
* and how to organize reduced states through canonical normal forms and predecessor structure.

These questions remain open. They now form the natural continuation of the present program.

## Appendix A. Historical examples and exploratory heuristics for Route A

This appendix collects examples and exploratory observations that were useful in discovering the Route A structure but are no longer part of the main formal spine of the note.

The main text now carries a sharper synthesis: on the even lifting component `ω ≡ 1 (mod 8)` with `d = 2n` (and, via the companion parameter `ω̃ = 3ω`, equally on the odd component `ω ≡ 3 (mod 8)` with `d = 2n + 1`), the valuation problem is governed by the congruence

```text
9^n ≡ ω^(-1) (mod 2^k),
```

the primary branch assembles into the global `2`-adic anchor `N(ω)`, and the local off-spike valuation geometry is organized by centered displacement from that anchor. In that setting, the role of the present appendix is only illustrative.

Accordingly, the examples below should be read as worked discovery references and not as independent theorem targets. Their purpose is to preserve intuition while removing clutter from the formal development.

### A.1. First-layer valuation examples

Before the lifting-branch synthesis was visible, several fixed families served as calibration examples for the valuation

```text
s = v_2(3^d ω - 1).
```

These examples remain useful as reference points, but the main text no longer needs to linger on them in detail.

#### A.1.1. The family `ω = 1`

The family

```text
ω = 1
```

gives the exact law

```text
v_2(3^d - 1) =
    1,              if d is odd,
    2 + v_2(d),     if d is even.
```

Historically, this was the first fully rigid family and remains the model for the centered halo law. Its conceptual importance is not that it is an isolated example, but that the later off-spike local law is a translated version of this same valuation pattern.

#### A.1.2. The families `ω = 5` and `ω = 7`

The families

```text
ω = 5,   ω = 7
```

provided the first examples in which the valuation is completely parity-locked rather than governed by deeper lifting.

For `ω = 5`,

```text
v_2(5·3^d - 1) =
    1,    if d is odd,
    2,    if d is even.
```

For `ω = 7`,

```text
v_2(7·3^d - 1) =
    2,    if d is odd,
    1,    if d is even.
```

These families are best read as illustrations of the first-layer residue split rather than as structural endpoints in their own right.

#### A.1.3. What these examples now mean

Taken together, the families

```text
ω = 1, 5, 7
```

showed early on that the first layer of the valuation problem is governed by the residue class of `ω (mod 8)`, but that this first-layer split does not by itself determine the deeper lifting geometry.

That role is now formalized in the main text by the mod `8` classification itself. The worked families are therefore retained here only as examples.

### A.2. Early tower-discovery examples

Two families played an especially important role in revealing that deeper lifting is organized around distinguished branch structure rather than by `d` alone.

#### A.2.1. The family `ω = 17`

The family

```text
ω = 17
```

was the first clear example suggesting that deeper lifting is centered at a distinguished exponent rather than controlled directly by `v_2(d)`.

On the even branch, one observes a prominent spike at

```text
d_0 = 12,
```

with

```text
v_2(17·3^12 - 1) = 8,
```

and the surrounding values satisfy the translated law

```text
v_2(17·3^d - 1) = 2 + v_2(d - 12)
```

through the visible off-spike local range.

Historically, this example was important because it suggested three things at once:

1. the correct local variable is displacement from a spike,
2. the off-spike law resembles the family `ω = 1`,
3. and the family-specific content may lie mainly in spike placement and spike height.

This was the first strong hint of the later anchor-displacement viewpoint.

#### A.2.2. The family `ω = 25`

The family

```text
ω = 25
```

was the first clean example of a regular nested tower.

On the even branch, the valuation first splits rigidly by congruence classes modulo `16`, with the unique exceptional class

```text
d ≡ 10 (mod 16)
```

carrying deeper lifting. That class then refines through higher powers of `2` in a clean one-branch-at-a-time manner.

Historically, this example mattered because it suggested that the visible tower is generated by a congruence mechanism rather than by ad hoc local spikes. In retrospect, this is precisely the phenomenon later formalized by the congruence condition

```text
9^n ≡ ω^(-1) (mod 2^k).
```

#### A.2.3. How these examples should now be read

The families

```text
ω = 17, 25
```

should no longer be read as carrying independent rhetorical weight in the main argument. Their function is historical and illustrative:

* `ω = 17` is the early discovery example for centered local halo behavior;
* `ω = 25` is the early discovery example for a clean congruence-generated tower.

Once the primary congruence branch, global anchor, centered halo law, and boundary-shell localization are formalized, these examples become explanatory references rather than load-bearing steps.

### A.3. Early heuristic observations now subordinate to the later synthesis

Several observations recorded earlier in the note were useful in orienting the search before the current Route A synthesis was available. They are preserved here only so that the discovery path is not lost.

#### A.3.1. Residue clustering and apparent parity locking

Early computation suggested that reduced states with similar residue data often exhibit similar valuation behavior, and that in some families the parity of

```text
s = v_2(3^d ω - 1)
```

appears to lock into repeating patterns.

These observations were directionally useful, but the later synthesis now gives a sharper framework: on the lifting branch, the real organizing object is not a vague residue cluster but the primary congruence branch and its anchor coordinate.

So the earlier language of “residue clustering” and “parity locking” should be read as a rough precursor to the later congruence-anchor picture rather than as a separate research direction.

#### A.3.2. Near-deterministic behavior within residue classes

Some families appeared to show similar average behavior across residue classes even when individual values still varied. This helped motivate the search for a deeper finite organization.

At present, however, this observation remains too coarse to play a formal role. It is better treated as a historical note than as a live structural claim.

#### A.3.3. Possible finite-state shadow

The question of whether some bounded residue package captures a significant part of the reduced dynamics remains conceptually interesting, but at the present stage it is secondary.

The main text no longer needs this as part of its immediate formal rhetoric. If retained at all, it is best treated as a long-range speculative question rather than as part of the current Route A narrative.

#### A.3.4. The approximate one-third phenomenon

The earlier “approximate one-third” heuristic was an exploratory attempt to interpret certain average-looking numerical patterns in terms of repeated `3`-gain behavior.

At present this heuristic is too weakly integrated into the current theorem program to justify a prominent place in the main text. Unless a later section returns to it with a sharper arithmetic formulation, it is best regarded as dormant.


### A.4. Detailed lifting-branch empirical survey

The following subsections reproduce the detailed empirical observations that motivated the Route A synthesis. They are retained here in full as discovery-path references; the formal content extracted from them is now carried by Sections `11.8.1`–`11.8.3`. Unless explicitly stated otherwise, the claims should be read as empirical patterns rather than proved facts.

#### A.4.1. Historical role of the early empirical heuristics

Before the present lifting-branch synthesis was available, several broad empirical patterns were useful in orienting the search. In particular, residue clustering, apparent parity regularity in the valuation

```text
s = v_2(3^d ω - 1),
```

and family-specific worked examples suggested that the reduced dynamics were not arithmetically unstructured.

Those observations played a useful historical role, but they no longer carry the main formal burden of the note. The later Route A synthesis now identifies a sharper arithmetic spine: first-layer classification by `ω (mod 8)`, then the lifting-branch congruence mechanism

```text
9^n ≡ ω^(-1) (mod 2^k),
```

then the primary congruence branch, global anchor, and centered valuation geometry.

Accordingly, the exploratory material that helped reveal that structure is no longer kept in the main line as a bank of parallel heuristic claims. Worked examples and historical discovery notes are now collected in Appendix A.

#### A.4.2. Residue organization as a heuristic prompt

It remains plausible that residue data organizes substantial portions of the reduced dynamics, since the reduced step is governed by the arithmetic of

```text
A = 3^d ω - 1.
```

In particular, congruence conditions in `ω` and parity data in `d` naturally influence the valuation profile of `A`, and hence influence `3`-gain and the next reduced step.

At present, however, this observation should be read only as a heuristic prompt. The main text no longer treats broad residue clustering as an independent structural claim. What survives formally is the sharper arithmetic organization developed later on the lifting branch.

#### A.4.3. Parity regularity and `3`-gain

Empirical regularities in the parity of

```text
s = v_2(3^d ω - 1)
```

were historically important because Section 9 shows that the parity of `s` exactly controls whether the next stage gains a factor of `3`.

That observation remains conceptually useful, but the present note no longer elevates broad parity-locking phenomena to a separate empirical program in the main text. The current focus is narrower: prove exact valuation laws on natural families, then translate those directly into `3`-gain theorems.

#### A.4.4. Finite-state shadow as a long-range question

The possibility that the reduced map admits some finite-state shadow remains a natural long-range question. One may still ask whether bounded residue data predicts substantial parts of the visible reduced dynamics while deeper `2`-adic information carries the unbounded refinement.

At the present stage, however, this question is secondary to the more immediate Route A program. The main text therefore records it only as a background motivation rather than as a live organizing principle.

#### A.4.5. Status and pointer to Appendix A

The earlier empirical heuristics of this section should now be read as historical scaffolding rather than as parallel theorem targets. Their role was to motivate the later search for sharper arithmetic structure, not to enlarge the proved content of the note.

For worked family examples, exploratory residue patterns, and historical discovery notes that led into the present Route A synthesis, see Appendix A.

#### A.4.6. Regular and irregular lifting towers in the `ω ≡ 1 (mod 8)` branch

Computational exploration of the lifting branch has revealed a further distinction inside the valid reduced families with

```text
ω ≡ 1 (mod 8),   3 ∤ ω.
```

In all such families tested so far, the odd branch is non-lifting with

```text
s = v_2(3^d ω - 1) = 1
```

for odd `d`, while the even branch supports deeper lifting. The new phenomenon is that the lifting on the even branch does not always organize in the same way.

Two empirical tower archetypes have appeared.

**Regular tower type.** The even branch first splits into rigid congruence classes modulo `16`, with exactly one exceptional class carrying deeper lifting. That exceptional class then refines cleanly through higher powers of `2`: at each stage, one subclass stabilizes at a fixed valuation while the other continues to lift.

**Irregular tower type.** The even branch again concentrates deeper lifting on a distinguished congruence class, but the subsequent refinement is not cleanly one-branch-at-a-time. Instead, secondary peaks and non-monotone local behavior persist inside the deeper subclasses.

The tested cases currently separate as follows.

```text
regular:    ω = 25, 49
irregular:  ω = 17, 41
```

For the regular examples, the first exceptional classes were observed to be

```text
ω = 25  =>  d ≡ 10 (mod 16),
ω = 49  =>  d ≡  4 (mod 16),
```

and in both cases the deeper lifting continued through a clean nested tower of congruence classes modulo `32, 64, 128, ...`.

For the irregular examples, the first visible lifting classes were

```text
ω = 17  =>  d ≡ 12 (mod 16),
ω = 41  =>  d ≡  6 (mod 16),
```

but the subsequent refinement remained mixed, with prominent local peaks inside the deeper classes rather than a uniformly clean stabilization pattern.

These examples suggest a tentative secondary classifier inside the lifting branch:

```text
ω ≡ 0 (mod 3)  =>  powers of 3 absorbed into a,
ω ≡ 1 (mod 3)  =>  regular tower type,
ω ≡ 2 (mod 3)  =>  irregular tower type.
```

The current evidence is:

```text
25 ≡ 1 (mod 3),  49 ≡ 1 (mod 3)   =>  regular,
17 ≡ 2 (mod 3),  41 ≡ 2 (mod 3)   =>  irregular.
```

This proposed split has since been refuted, and the underlying dichotomy dissolved; it is retained here only as a record of the discovery path, together with the negative result, so that the same small sample does not regenerate the conjecture.

The refutation (summarized in the closing note of `11.8.4.3`) has two parts. First, by the logarithmic identification of Theorem `11.8.3.6.6` and the exact law `s = 3 + v_2(n - N(ω))`, the only family-dependent structure in the `s`-data is the digit expansion of `N(ω) = -log ω / log 9`; the regular/irregular impression corresponds to digit density in the viewing window. The seven historically labeled families separate exactly on this statistic — ones-counts in the first `24` digits:

```text
regular   :  ω = 25 => 14,   ω = 49 => 15,   ω = 73 => 15,
irregular :  ω = 17 => 10,   ω = 41 => 12,   ω = 65 =>  8,   ω = 89 =>  8.
```

Under a fair-coin digit model this is a `Binomial(24, 1/2)` draw: the "types" are the two tails of one unimodal distribution, not two classes. Second, a computational audit over all `2,499` valid families `ω ≡ 1 (mod 8)`, `3 ∤ ω`, `ω < 30000` (anchor digits computed at precision `2^36` from the congruence definition; statistics on the first `24` digits) found no dependence of the anchor digits on `ω (mod 3)`:

```text
mean digit-sum        : 11.930 (ω ≡ 1)  vs  11.965 (ω ≡ 2),   z = -0.36
mean longest zero-run :  3.958 (ω ≡ 1)  vs   4.016 (ω ≡ 2),   z = -0.90
max per-digit gap     :  0.036  ≈ 1.8 se over 24 positions (max ≈ 2.7 se expected under independence)
overall digit density :  0.497  ≈ 1/2, consistent with pseudo-random digits.
```

The four-versus-three split observed above was a coincidence of a seven-family sample.

The observed anchor towers suggested that for valid lifting families `(\omega \equiv 1 \pmod 8)`, the distinguished exponent may be a `2`-adic quantity `d_\infty(\omega)` characterized informally by

```text
3^(d_\infty) · ω = 1.
```

This informal characterization is now a theorem: the main text establishes `d_\infty(ω) = 2 N(ω) = -2 log ω / log 9` (Definition `11.8.3.6.2` and Theorem `11.8.3.6.6`), and the visible residue towers are its finite truncations.

#### A.4.7. Congruence-generated anchor towers in the regular lifting branch

The regular families `ω = 25` and `ω = 49` provide strong computational evidence that the anchor towers are not merely phenomenological patterns in the values of

```text
s(d) = v_2(3^d ω - 1),
```

but arise from a more definite arithmetic mechanism.

Since the lifting branch for `ω ≡ 1 (mod 8)` occurs on even `d`, write

```text
d = 2n.
```

Then

```text
3^d ω - 1 = 9^n ω - 1,
```

so high valuation occurs when

```text
9^n ω ≡ 1 (mod 2^k),
```

or equivalently when

```text
9^n ≡ ω^(-1) (mod 2^k).
```

This suggests that the distinguished anchor is more naturally an exponent `n` satisfying a congruence tower for the base `9`, with the corresponding `d`-anchor given by

```text
d = 2n.
```

In this form, the empirical anchor tower is no longer an unexplained sequence of residue classes in `d`. It is the visible shadow of the successive congruence solutions to

```text
9^n ≡ ω^(-1) (mod 2^k).
```

This mechanism matches the regular examples exactly.

For `ω = 25`, the observed lifting residues were

```text
10 (mod 16),
10 (mod 32),
42 (mod 64),
106 (mod 128),
234 (mod 256),
490 (mod 512),
1514 (mod 2048),
...
```

and these are precisely the residue classes obtained by solving

```text
9^n ≡ 25^(-1) (mod 2^k)
```

and then converting back to `d = 2n`.

Likewise, for `ω = 49`, the observed lifting residues were

```text
4    (mod 16),
36   (mod 64),
164  (mod 256),
676  (mod 1024),
1700 (mod 2048),
5796 (mod 8192),
13988 (mod 16384),
...
```

and again these are reproduced by the congruence tower

```text
9^n ≡ 49^(-1) (mod 2^k).
```

Thus, in the regular lifting branch, the anchor tower appears to be generated by a definite congruence process rather than by ad hoc local peaks. The numerical data therefore supports the following empirical interpretation:

> for regular families in the branch `ω ≡ 1 (mod 8)`, the anchor tower is generated by successive solutions of
> `9^n ≡ ω^(-1) (mod 2^k)`,
> with the visible distinguished residues in `d` given by `d = 2n`.

Equivalently, the regular tower behaves as though it were controlled by a `2`-adic exponent `d_\infty(\omega)` whose finite truncations are exactly the observed lifting classes.

At present this should still be regarded as an empirical mechanism rather than a proved theorem. The evidence is nevertheless strong: in the regular examples, the computed tower of distinguished residue classes is recovered exactly from the congruence model. This makes the congruence

```text
9^n ≡ ω^(-1) (mod 2^k)
```

the first concrete arithmetic candidate for the hidden generator of anchor towers in the lifting regime.

An additional test case confirms that this mechanism is not confined to the initial regular examples.

For `ω = 73`, direct computation again shows a regular lifting tower on the even branch. The first split by `d (mod 16)` is:

```text
d ≡ 0, 4, 8, 12 (mod 16)  =>  s = 3,
d ≡ 2, 10      (mod 16)    =>  s = 4,
d ≡ 6          (mod 16)    =>  s = 5,
d ≡ 14         (mod 16)    =>  deeper lifting.
```

So the unique exceptional class is

```text
d ≡ 14 (mod 16),
```

which places `ω = 73` in the same regular archetype as `ω = 25` and `ω = 49`.

The observed values on that exceptional class begin:

```text
d =  14  =>  s =  7
d =  30  =>  s =  6
d =  46  =>  s = 10
d =  62  =>  s =  6
d =  78  =>  s =  7
d =  94  =>  s =  6
d = 110  =>  s =  8
d = 126  =>  s =  6
d = 142  =>  s =  7
d = 158  =>  s =  6
d = 174  =>  s =  9
...
```

These distinguished residues are again reproduced by the congruence model

```text
9^n ≡ 73^(-1) (mod 2^k),
d = 2n.
```

The resulting anchor chain begins:

```text
14,
46,
302,
814,
1838,
3886,
...
```

with the corresponding congruence classes

```text
14   (mod 32),
46   (mod 128),
302  (mod 1024),
814  (mod 2048),
1838 (mod 4096),
3886 (mod 8192),
...
```

Thus `ω = 73` provides a third regular family whose lifting tower is recovered from the same congruence-generated mechanism. This materially strengthens the empirical interpretation above: in the regular branch, the distinguished lifting classes are not isolated numerical curiosities, but appear to be generated systematically by solving

```text
9^n ≡ ω^(-1) (mod 2^k).
```

Since

```text
25 ≡ 49 ≡ 73 ≡ 1 (mod 3),
```

this additional example is also consistent with the provisional observation of Section `A.4.6` that the regular tower type may be associated with the subclass

```text
ω ≡ 1 (mod 3)
```

inside the valid lifting branch `ω ≡ 1 (mod 8)`. (This association has since been refuted: an audit of `2,499` families found no mod-`3` dependence in the anchor digits, and the regular/irregular distinction itself dissolves into a continuous digit-density statistic; see Remark `11.8.1.8.4` and `A.4.6`.)

#### A.4.8. Translated halo shells in the irregular lifting branch

Computations at fixed modulus show that the irregular families `ω = 17` and `ω = 41` do not merely share the existence of a main congruence tower. They also exhibit the same surrounding halo-shell geometry.

At modulus `128`, both families display a dyadic shell profile consisting of

```text
1 main residue,
1 first halo residue,
2 second-shell residues,
4 third-shell residues,
8 fourth-shell residues,
then broad lower background.
```

At modulus `256`, this structure refines coherently to

```text
1 main residue,
1 first halo residue,
2 next-shell residues,
4 next-shell residues,
8 next-shell residues,
16 next-shell residues,
then broad lower background.
```

Thus the irregular branch does not merely contain isolated anomalous peaks. It carries a stable dyadic shell architecture surrounding the main congruence class.

More precisely, at modulus `256`, the full shell profile for `ω = 41` is obtained from that of `ω = 17` by translation through a fixed offset:

```text
d_(41) ≡ d_(17) + 202 (mod 256).
```

Equivalently,

```text
d_(41) ≡ d_(17) - 54 (mod 256).
```

This translation carries not only the main congruence class to the new main congruence class, but also carries each surrounding halo shell to its counterpart. In particular, the two irregular families appear to realize the same halo template, transported in the depth variable `d`.

The refinement from modulus `128` to modulus `256` is also coherent. In both families:

* the main congruence class remains the top peak,
* its `+128` lift becomes the first halo residue,
* and each lower halo shell duplicates by translation through `+128`.

So the irregular branch appears to possess not only a common shell profile, but also a common shell-refinement law.

This suggests that the irregular families share a stable structure of the form

```text
main congruence tower + translated dyadic halo shells.
```

At present this should still be regarded as an empirical structural observation. Its significance is that the irregular branch now appears to possess its own coherent geometry, rather than merely failing to satisfy the regular tower mechanism.

#### A.4.9. Centered dyadic halo template in the irregular branch

The translated-shell observation of Section `A.4.8` admits a sharper formulation. The irregular families do not merely appear to be related by translation in the depth variable `d`. After recentering at the primary spike, they exhibit the same raw halo template.

For each irregular family, let

```text
d*(ω)
```

denote the primary spike location at the chosen modulus, and define the centered coordinate

```text
Δ ≡ d - d*(ω) (mod 2^m).
```

Computations for the irregular families

```text
ω = 17, 41, 65, 89
```

show that after this recentering, the same halo-shell pattern appears in every case.

At modulus `256`, the centered shell template is:

```text
primary spike:        Δ = 0

first halo shell:     Δ = 128

second halo shell:    Δ = 64, 192

third halo shell:     Δ = 32, 96, 160, 224

fourth halo shell:    Δ = 16, 48, 80, 112, 144, 176, 208, 240

fifth halo shell:     Δ = 8, 24, 40, 56, 72, 88, 104, 120,
                       136, 152, 168, 184, 200, 216, 232, 248.
```

At modulus `512`, the same structure extends by one further dyadic layer:

```text
primary spike:        Δ = 0

first halo shell:     Δ = 256

second halo shell:    Δ = 128, 384

third halo shell:     Δ = 64, 192, 320, 448

fourth halo shell:    Δ = 32, 96, 160, 224, 288, 352, 416, 480

fifth halo shell:     odd multiples of 16 (mod 512)

sixth halo shell:     odd multiples of 8 (mod 512).
```

Thus the modulus does not create the halo pattern. Rather, each modulus `2^m` reveals a finite truncation of a larger centered dyadic shell tree.

Equivalently, the centered shell locations are the odd multiples of descending powers of `2` around the centered origin:

```text
Δ = 0,
Δ = 2^(m-1),
Δ = odd multiples of 2^(m-2),
Δ = odd multiples of 2^(m-3),
Δ = odd multiples of 2^(m-4),
...
```

modulo `2^m`.

This shows that the raw irregular halo is not family-specific. The family-specific data appears only in the placement of the template through the primary spike `d*(ω)`.

More importantly, the centered shell valuations are not arbitrary. Around a high primary spike `d*`, the surrounding halo satisfies the same valuation law as the family `ω = 1`, transplanted into the centered coordinate `Δ`. Namely, for even `Δ != 0`,

```text
v_2(ω·3^(d*+Δ) - 1) = 2 + v_2(Δ),
```

while at the spike itself one has

```text
v_2(ω·3^(d*) - 1) = A,
```

where `A` is the spike height.

So the irregular branch appears to have the following form:

```text
family-specific primary spike  +  universal centered dyadic halo template,
```

with the centered halo governed off the spike by the transplanted `ω = 1` law.

In this form, the irregular families no longer look like unrelated exceptions. They appear to realize one common shell architecture, translated by the position of the primary spike and capped by the spike height.

At present this remains an empirical structural observation. Its significance is that the irregular branch now appears to possess not only translated shell profiles, but a common centered halo geometry that is independent of the particular family once the primary spike is factored out.

#### A.4.10. Relative offset branches between irregular families

The centered halo template of Section `A.4.9` isolates the family-independent shell geometry of the irregular branch. The remaining family-specific data is the placement of that template through the primary spike `d*(ω)`.

A further computation shows that the displacement between two such placements is not arbitrary. It is itself governed by a dyadic lift pattern.

Let

```text
d*_k(ω) = 2 n_k(ω)
```

denote the level-`k` primary branch obtained from the congruence tower

```text
9^n ≡ ω^(-1) (mod 2^k).
```

Then for two irregular families `ω_1` and `ω_2`, the levelwise difference

```text
Δd_k = d*_k(ω_2) - d*_k(ω_1)
```

again evolves by long plateaus separated by dyadic jumps, rather than by arbitrary drift.

For example, comparing `ω = 17` and `ω = 41`, the induced differences in the primary branches begin:

```text
k =  9   =>  Δd_k ≡  74   (mod 128)
k = 10   =>  Δd_k ≡ 202   (mod 256)
k = 11   =>  Δd_k ≡ 202   (mod 512)
k = 12   =>  Δd_k ≡ 714   (mod 1024)
k = 13   =>  Δd_k ≡ 714   (mod 2048)
k = 14   =>  Δd_k ≡ 714   (mod 4096)
k = 15   =>  Δd_k ≡ 714   (mod 8192)
k = 16   =>  Δd_k ≡ 714   (mod 16384)
k = 17   =>  Δd_k ≡ 17098 (mod 32768)
k = 18   =>  Δd_k ≡ 17098 (mod 65536).
```

Thus the shift between two irregular primary branches is not constant across all precisions, but it is itself a compatible dyadic lift branch.

This is explained by the congruence relation itself. If

```text
9^(n_k(ω_1)) ≡ ω_1^(-1) (mod 2^k),
9^(n_k(ω_2)) ≡ ω_2^(-1) (mod 2^k),
```

then subtraction in the exponent gives

```text
9^(n_k(ω_2) - n_k(ω_1)) ≡ ω_1 · ω_2^(-1) (mod 2^k).
```

So the relative displacement between two primary branches is governed by the same base-`9` congruence mechanism, now applied to the ratio `ω_1 · ω_2^(-1)`.

This suggests the following empirical interpretation:

> the primary offset branch for an irregular family is not an isolated object. Differences between primary branches are themselves generated by compatible congruence lifts of the same type.

Equivalently, the family-to-family translation of the irregular halo template appears to be controlled by a secondary `2`-adic exponent attached to the ratio of the corresponding `ω` values.

At present this remains an empirical structural observation. Its significance is that the irregular branch now appears to possess not only a universal centered halo template, but also a coherent arithmetic law governing the relative placement of that template from one family to another.

### A.5. Primary congruence branch and 2-adic anchor in the lifting branch

Sections `10.9` and `10.10` suggest that the observed lifting structure is best understood in two layers:

```text
family-dependent primary branch
+ universal centered dyadic halo geometry.
```

However, the arithmetic mechanism producing the primary branch is not itself peculiar to the irregular families. On the valid lifting branch

```text
ω ≡ 1 (mod 8),
```

writing

```text
d = 2n,
```

the valuation condition

```text
v_2(3^d ω - 1) >= k
```

is equivalent to

```text
9^n ≡ ω^(-1) (mod 2^k).
```

So the primary branch should be regarded first as a lifting-branch congruence object, and only then specialized to the irregular families where a universal centered halo becomes visible around it.

Accordingly, for each lifting family `ω ≡ 1 (mod 8)`, define the level-`k` exponent-side branch by the solution classes

```text
n_k(ω) (mod 2^(k-3))
```

to

```text
9^n ≡ ω^(-1) (mod 2^k),
```

with corresponding depth classes

```text
d_k^*(ω) = 2 n_k(ω).
```

These classes are the natural candidates for the true family-dependent anchor. In regular families, they appear to account for the full visible lifting structure. In irregular families, they appear to specify the location of the primary spike, while the surrounding off-spike shell structure is then governed by a universal centered law.

This suggests the sharper structural picture:

> the family-dependent object is the compatible primary congruence branch `d_k^*(ω)` on the lifting branch, while the irregular families are distinguished by the appearance of a universal centered halo law around that branch.

Equivalently, the irregular branch should not be viewed as introducing a second competing lifting mechanism. Rather, it appears to decompose into

```text
family-specific congruence anchor
+ universal local valuation geometry after centering.
```

One may therefore view the compatible classes `d_k^*(ω)` as successive truncations of a single `2`-adic quantity

```text
d_∞(ω) in 2 Z_2,
```

or, on the exponent side,

```text
n_∞(ω) = d_∞(ω)/2,
```

informally characterized by

```text
ω·3^(d_∞(ω)) = 1
```

or equivalently

```text
9^(n_∞(ω)) = ω^(-1)
```

in the `2`-adic sense.

Under this interpretation, the irregular halo law of Section `A.4.9` becomes more coherent. The family-specific data lies in the anchor location, while the off-spike valuations appear to follow the same centered law as the family `ω = 1`. Namely, if `d_k^*(ω)` is a primary spike at the chosen level and `Δ` is even with `Δ != 0`, then the computations suggest

```text
v_2(ω·3^(d_k^*(ω) + Δ) - 1) = 2 + v_2(Δ)
```

throughout the visible halo away from the spike itself.

So the lifting picture is provisionally organized as

```text
primary congruence branch  +  transplanted ω = 1 halo law.
```

In this formulation, the primary spike is no longer an isolated anomaly. It is the point where the chosen finite depth has landed unusually close to the family-dependent `2`-adic anchor itself, while the surrounding shell structure reflects the universal dyadic valuation law in displacement from that anchor.

This also suggests a natural interpretation of spike height. If

```text
H_k(ω) = v_2(ω·3^(d_k^*(ω)) - 1)
```

denotes the height of the level-`k` primary spike, then the local centered halo law suggests that no smaller even displacement can compete with the spike before the scale

```text
2^(H_k - 2)
```

in the depth variable `d`.

So the spike height appears to determine the first dyadic scale at which a new refinement of the primary branch can occur. In the visible irregular examples, the next branch jump appears to occur exactly at that scale, while the weaker divisibility barrier is already suggested by the transplanted halo law itself.

Thus the lifting families are provisionally organized as

```text
finite truncations of a family-dependent 2-adic anchor
+ universal centered valuation law around that anchor,
```

with spike height measuring the first scale at which the current truncation can refine.

At present this remains an empirical structural interpretation rather than a proved theorem. Its significance is that it isolates what now appears to be the true family-dependent datum: not the halo geometry, but the compatible congruence anchor whose truncations produce the observed primary spikes.

### A.6. Status of These Observations

The observations above are included to mark where the reduced formalism appears most suggestive, not to enlarge the proved content of the note. They indicate directions where the reduced dynamics may admit further compression or classification, but they should not be interpreted as settled structural laws.

The next section records open questions suggested by this empirical picture.

### A.7. Role of this appendix

The examples and heuristics collected here are retained for three limited purposes:

1. to preserve the discovery path that led to the current Route A synthesis,
2. to provide worked reference cases for readers who want intuition,
3. to keep the main text focused on the later formal structure.

Accordingly, when the main text needs illustration, it should point here briefly rather than reproducing full family-by-family discussion in the formal development.

A suitable main-text pointer would be:

> For worked family examples and early exploratory heuristics that motivated the present Route A synthesis, see Appendix A.
