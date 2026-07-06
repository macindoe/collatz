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

## 3.6. The Projection `Q`

Define the projection `Q` from BlockEntry coordinates to reduced structural states by

```text
Q(u,m) = (ω,d),
```

where `u = 3^a ω` with `3` not dividing `ω` and `d = m + a`.

This projection passes from exact block coordinates to the reduced state space studied in the rest of the note.

## 3.7. Induced Reduced Dynamics

The structural step on BlockEntry coordinates determines a corresponding transition on reduced states by passing through the projection `Q`. At the level of construction, one may describe the reduced map by the sequence:

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
- `m`: the `2`-adic entry depth in the BlockEntry coordinates; equivalently, `m = v_2(x + 1)`.
- `(u,m)`: the BlockEntry coordinates associated with an odd value `x = 2^m u - 1`.
- `E`: the structural step on BlockEntry coordinates.

## 4.4. Layer 4: Reduced Structural States

- `a`: the `3`-adic content of `u`, defined by `a = v_3(u)`.
- `ω`: the structural odd core of `u`, defined by `u = 3^a ω` with `3` not dividing `ω`.
- `d`: the full combined depth parameter, defined by `d = m + a`.
- `(ω,d)`: the reduced structural state associated with a BlockEntry.
- `Q`: the projection from BlockEntry coordinates to reduced structural states, given by `Q(u,m) = (ω,d)`.
- `F`: the reduced self-map on structural states, equivalently defined by passing the structural step through `Q` or by `F(ω,d)=R(x_exit(ω,d))`.

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
R(u,m) = Q(u,m) = (ω,d).
```

This transform is surjective but not injective.

**Representative fiber.** For a fixed reduced state `(ω,d)`, the full BlockEntry fiber is

```text
Q^(-1)(ω,d) = {(3^r ω, d - r) : 0 <= r <= d - 1}.
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

naturally appears as the structural numerator governing the transition to the next block.

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

Applying the projection `Q` to the output of the structural step produces the corresponding reduced state. That is, if

```text
E(u,m) = (u_+, m_+),
```

then the next reduced structural state is obtained from

```text
Q(u_+, m_+) = (ω_+, d_+),
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

where `0 <= r <= d - 1`. Indeed, if `Q(u,m) = (ω,d)`, then writing `u = 3^a ω` with `3` not dividing `ω` gives `d = m + a`, so necessarily `u = 3^a ω` and `m = d - a`. Conversely, every such pair projects to the same reduced state `(ω,d)`.

Here `r` indexes the different BlockEntry representatives of the same reduced state. Increasing `r` shifts one unit of the total depth `d` from the entry-depth parameter `m` into the `3`-adic content of `u`, without changing the reduced state itself. Thus `r` measures movement within a representative family, not dynamical time evolution.

Thus, if two BlockEntry coordinates `(u,m)` and `(u',m')` satisfy

```text
Q(u,m) = Q(u',m') = (ω,d),
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

once projected by `Q`, always produces the same reduced state regardless of which representative `(u,m)` with `Q(u,m) = (ω,d)` was chosen initially.

## 8.3. Main Proposition

**Proposition 8.3.1.** If two BlockEntry coordinates satisfy

```text
Q(u,m) = Q(u',m'),
```

then

```text
Q(E(u,m)) = Q(E(u',m')).
```

**Proof.** By Section 7.1, the reduced state `(ω,d)` uniquely determines the structural numerator `A = 3^d ω - 1`. By Section 7.2, `A` uniquely determines `s`, `x_exit`, `m_+`, and `u_+`, and hence determines the projected output reduced state. Therefore the result of applying `E` and then projecting by `Q` depends only on `(ω,d)`, not on the representative chosen. This proves the claim.

## 8.4. The Induced Reduced Map

Because the projected output depends only on the reduced state, the induced reduced map `F` is well-defined. Accordingly, one may define

```text
F(ω,d) = Q(E(u,m))
```

for any BlockEntry representative `(u,m)` satisfying `Q(u,m) = (ω,d)`.

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

Before recording the formal properties of the reduced map, it is helpful to state the phenomenology of a single reduced block `(ω,d)`.

A reduced block is not merely an abstract equivalence class. It corresponds to a finite deterministic odd subsequence in the Collatz dynamics. Its canonical representatives are the BlockEntry states

```text
(u,m) = (3^a ω, d-a),   0 <= a <= d-1,
```

equivalently indexed by

```text
(m,a) = (d,0), (d-1,1), ..., (1,d-1).
```

The associated odd values are

```text
x_a = 2^(d-a) 3^a ω - 1,   0 <= a <= d-1.
```

Along this chain, each odd-to-odd transition is separated by exactly one halving move. Thus the odd values

```text
x_0, x_1, ..., x_(d-1)
```

form the deterministic interior of the same reduced block: the structural odd core `ω` remains fixed, the total depth `d = m + a` remains fixed, and each step transfers one unit of `2`-adic depth into one unit of `3`-adic content.

The terminal interior position occurs at

```text
(m,a) = (1,d-1).
```

From there the block exits through the structural numerator

```text
A = 3^d ω - 1.
```

Its full `2`-adic valuation

```text
s = v_2(3^d ω - 1)
```

determines the forced halving cascade, and the odd exit is

```text
x_exit = (3^d ω - 1) / 2^s.
```

Thus every representative of the same reduced block shares the same exit law. The case `s = 1` is the boundary case in which the block exits after a single halving beyond the terminal interior position, while the case `s >= 2` is the genuine multi-halving cascade regime. In either case, the exit is determined entirely by `(ω,d)`.

In this sense, a reduced structural state `(ω,d)` packages an entire finite deterministic odd chain together with its common exit law. The reduced map does not record the interior positions separately; it compresses the whole block to the single structural datum governing its eventual odd exit and the next reduced state.


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

## 9.5. Special Upstream Families of a Fixed Target

A different kind of exact family appears when one fixes a downstream odd target `x` and studies admissible upstream predecessors of the form

```text
x_S = (x 2^(S+1) - 1) / 3,
```

whenever this is integral.

Here the index `S` is the structural cascade depth attached to the predecessor family.The full predecessor identity is

```text
3x_S + 1 = x 2^(S+1),
```

but once the predecessor lies in the terminal BlockEntry regime `m_S = 1`, the first factor of `2` is absorbed into its BlockEntry coordinate

```text
u_S = (x_S + 1)/2,
```

and the remaining `2`-adic depth is exactly the valuation of the structural numerator

```text
A_S = 3^(d_S) ω_S - 1.
```

Thus `S` is the natural index on the reduced-state side.

This construction is upstream rather than representative: the values `x_S` need not lie in the same reduced-state family, and in general they do not. Instead, they form a family of structural predecessors of the fixed target `x`, indexed by structural cascade depth.

The first question is when such predecessors exist.

**Lemma 9.5.1.** Let `x` be an integer. Then

```text
x_S = (x 2^(S+1) - 1) / 3
```

is integral if and only if `3` does not divide `x` and the parity of `S` is determined by the residue of `x mod 3` as follows:

```text
S odd   if x ≡ 1 mod 3,
S even  if x ≡ 2 mod 3.
```

**Proof.** Integrality is equivalent to

```text
x 2^(S+1) ≡ 1 mod 3.
```

If `3` divides `x`, this is impossible. If `x ≡ 1 mod 3`, then one must have `2^(S+1) ≡ 1 mod 3`, which holds exactly when `S+1` is even, i.e. when `S` is odd. If `x ≡ 2 mod 3`, then one must have `2^(S+1) ≡ 2 mod 3`, which holds exactly when `S+1` is odd, i.e. when `S` is even.

Now suppose `x` is odd with `3` not dividing `x`, and let `x_S` be an admissible predecessor.

The key structural point is that Lemma 6.2.1 governs deterministic drift within a block: each odd step transfers one unit from entry depth into `3`-adic content while preserving `d = m + a`. Thus a genuine cascade does not arise at an arbitrary interior point of a block, but only at its terminal end, after the available entry depth has been exhausted.

For a non-boundary cascade predecessor, the upstream entry is already reduced to the terminal regime

```text
m_S = 1.
```

Hence

```text
u_S = (x_S + 1) / 2.
```

Let `(ω_S,d_S)` be the reduced state associated to `x_S`, and define

```text
A_S = 3^(d_S) ω_S - 1,
s_S = v_2(A_S).
```

Since `m_S = 1`, one has

```text
d_S = 1 + v_3(u_S),
ω_S = u_S / 3^(v_3(u_S)),
```

and therefore

```text
3^(d_S) ω_S = 3 u_S.
```

It follows that

```text
A_S = 3 u_S - 1
    = 3(x_S + 1)/2 - 1
    = (3x_S + 1)/2.
```

But by construction of the predecessor family,

```text
3x_S + 1 = x 2^(S+1).
```

So

```text
A_S = x 2^S.
```

Therefore

```text
s_S = v_2(A_S) = v_2(x) + S.
```

This proves the main proposition.

**Proposition 9.5.2.** Let `x` be odd with `3` not dividing `x`, and let

```text
x_S = (x 2^(S+1) - 1) / 3
```

be an admissible non-boundary cascade predecessor. Then

```text
m_S = 1,
A_S = x 2^S,
s_S = v_2(x) + S.
```

In particular, if `x` is odd then `v_2(x) = 0`, so

```text
s_S = S.
```

Thus any admissible odd target `x` gives an exact identity between structural cascade depth and the valuation of the predecessor structural numerator along its stabilized upstream cascade family.

This also shows that such a family does not remain inside a single reduced-state representative class. Indeed, Section 8 showed that within any fixed reduced-state family the quantity

```text
A = 3^d ω - 1
```

is constant across all representatives. But here

```text
A_S = x 2^S
```

varies strictly with `S`. Thus distinct admissible values of `S` in this cascade regime must correspond to distinct reduced-state families.

The running example `x = 23` illustrates this exactly. Since `23 ≡ 2 mod 3`, only even `S` are admissible. For every admissible non-boundary cascade predecessor one obtains

```text
A_S = 23 · 2^S,
s_S = S.
```

## Bridge to 9.6

Section 9.5 studies exact upstream predecessor families of a fixed odd target and shows that, even when such predecessors are parametrized by a simple halving-depth variable `S`, they generally do not remain inside a single reduced-state class. This reinforces an important distinction: reduced-state families are intrinsic forward structural objects, whereas predecessor families are external inverse constructions built relative to a chosen target.

The next section returns to the intrinsic reduced-state viewpoint. Rather than fixing a target and generating upstream predecessors, it studies how the reduced quantities attached to a given state `(ω,d)` constrain the forward structural transition and the organization of reduced blocks themselves.

## 9.6. What the Reduced Dynamics No Longer Need

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

This section records observations that appear repeatedly in computation and experimentation within the reduced structural framework, but which are not established here as theorems. They are included because they may help guide future reductions, suggest useful residue descriptions, or point toward stronger structural questions. Unless explicitly stated otherwise, the claims in this section should be read as empirical patterns or research heuristics rather than proved facts.

## 10.1. Residue Clustering in the Reduced Dynamics

Across computational samples, reduced states with the same or closely related residue data often appear to exhibit similar transition behavior. In particular, the valuation

```text
s = v_2(3^d ω - 1)
```

and the resulting `3`-gain pattern seem to cluster by congruence classes of `ω` and by parity data attached to `d`.

At present, this is best regarded as a structural hint rather than a theorem. The reduced map is provably controlled by the arithmetic of `A = 3^d ω - 1`, so it is plausible that residue-class organization should emerge; however, the extent to which finitely many congruence patterns govern the dynamics remains open.

## 10.2. Apparent Locking of `s`-parity in Some Families

In some experimentally explored families, the parity of

```text
s = v_2(3^d ω - 1)
```

appears to follow stable or repeating behavior over ranges of reduced states. Since Section 9.3 showed that the parity of `s` exactly controls whether the next stage gains a factor of `3`, any such parity regularity would have direct dynamical consequences.

At present, this should be treated only as an observed pattern. The note does not prove periodicity, eventual stability, or finite-state control of `s`-parity in general.

## 10.3. Near-Deterministic Average Behavior Within Some Residue Classes

Some residue classes appear empirically to produce reduced transitions with similar average behavior, even when individual steps still vary. This suggests that certain residue descriptions may organize the dynamics more rigidly than the raw pair `(ω,d)` alone makes obvious.

No exact mechanism for this apparent near-determinism is established here. In particular, the note does not prove that any bounded residue system captures the full reduced dynamics.

## 10.4. Possible Finite-State Shadow of the Reduced Map

The reduced formalism naturally raises the question of whether the dynamics admit a finite-state shadow: that is, whether some bounded collection of residue variables captures a large part of the observable step-to-step structure, while the unbounded behavior is carried mainly by the `2`-adic depth variables.

This possibility is motivated by computational behavior, not by proof. The current results establish only that the reduced map is governed by the arithmetic of `A = 3^d ω - 1` and by the valuations extracted from it. Whether this arithmetic can be organized into a genuinely useful finite-state model remains an open question.

## 10.5. The Role of the Approximate One-Third Phenomenon

Some computational patterns suggest that an approximate one-third-type behavior may emerge in families where the parity of `s` alternates or where `3`-gain occurs with a visible regularity. The significance of this is that repeated `3`-gain events do not simply mark local divisibility accidents: they repeatedly alter how much of the next step is absorbed into the reduced-coordinate decomposition, and so may influence longer-scale movement through the reduced state space. At present, this is only a heuristic interpretation of numerical patterns, not a proved statistical law.

If such behavior is real, it would likely need to be explained through the interaction between the `2`-adic cascade length `s`, the induced `3`-gain mechanism of Section 9.3, and the residue structure of `ω` and `d`. Establishing or refuting such a mechanism remains future work.

## 10.6. Status of These Observations

The observations above are included to mark where the reduced formalism appears most suggestive, not to enlarge the proved content of the note. They indicate directions where the reduced dynamics may admit further compression or classification, but they should not be interpreted as settled structural laws.

The next section records open questions suggested by this empirical picture.

# 11. Conjectures and Open Questions

The previous sections isolate the exact structural core of the reduced formalism and separate it from the empirical patterns that remain unresolved. This final section records the main mathematical questions suggested by the framework. Some are immediate structural questions about the reduced map itself; others concern whether the observed residue patterns reflect genuine arithmetic laws.

## 11.1. Classification of Reduced-State Transitions

The reduced map `F` is now known to admit an intrinsic formulation,

```text
F(ω,d) = R(x_exit(ω,d)).
```

The remaining question is not whether such a formulation exists, but whether this intrinsic description can be simplified further. In particular, the central problem is to understand whether the transition

```text
(ω,d) ↦ (ω_+,d_+)
```

can be extracted more transparently from the intrinsic formula, without repeatedly unpacking the full sequence of valuations and reductions.

In particular:

- Can `d_+ - d` be expressed directly in terms of a small set of arithmetic parameters attached to `A = 3^d ω - 1`?
- Can `ω_+` be described through a more transparent residue law?
- Can the intrinsic formula for `F` be simplified so that the nested valuation and odd-part operations become more transparent or more easily controlled?

## 11.2. Structure of the Valuation `s = v_2(3^d ω - 1)`

The quantity `s` controls the `2`-adic cascade at the block exit and, through its parity, controls whether `3`-gain occurs. Understanding the reduced dynamics therefore requires a better description of the valuation sequence

```text
v_2(3^n ω - 1),
```

with `n = d`.

Open questions include:

- For fixed `ω`, what regularity does `s` exhibit as `d` varies?
- For fixed `d`, how is `s` organized by residue classes of `ω`?
- Are there natural families for which the parity of `s` is periodic, eventually periodic, or rigidly constrained?
- Which parts of the observed behavior are consequences of classical `2`-adic lifting phenomena, and which are genuinely specific to this reduced formalism?

## 11.3. Mechanisms of 3-gain

Section 9 proved that the parity of `s` determines whether the next odd seed gains a factor of `3`. What remains open is to understand the broader structural role of repeated `3`-gain events.

Questions here include:

- How strongly does repeated `3`-gain influence long-term movement through the reduced state space?
- Can `3`-gain events be predicted efficiently from bounded residue data?
- Do repeated `3`-gain patterns explain any of the observed clustering or approximate average behavior in the reduced dynamics?

## 11.4. Representative Families and Further Compression

The well-definedness result shows that all BlockEntry representatives of a fixed reduced state produce the same reduced output. This raises a further structural question: is the current reduced state still carrying redundant information?

More specifically:

- Is the pair `(ω,d)` already minimal for describing the induced map, or does the repeated appearance of the invariant `m + a = d` indicate that a cleaner parameterization exists?
- Can the notation and state description be compressed further without losing transparency?
- Is there a more natural coordinate system in which the structural numerator `A = 3^d ω - 1` appears even more directly?

## 11.5. Finite-State Shadow and Residue Control

The empirical observations suggest that residue data may organize much of the visible reduced dynamics. This leads to the question of whether the system admits a useful finite-state shadow.

Possible formulations include:

- Is there a bounded residue system that predicts the parity of `s` in large families?
- Can one isolate a finite collection of residue variables that explains most observed `3`-gain behavior?
- Does a finite-state model genuinely describe the reduced dynamics, or does the full arithmetic complexity reappear as soon as deeper `2`-adic behavior is tracked?

## 11.6. The Approximate One-Third Phenomenon

If the observed approximate one-third-type behavior reflects a real structural effect, then it should ultimately admit an arithmetic explanation inside the reduced formalism.

Open questions include:

- Is the phenomenon genuine, or only an artifact of limited computational samples?
- If genuine, does it arise from parity patterns of `s`, from frequencies of `3`-gain, or from a combination of both?
- Can it be formulated as a statistical statement on reduced-state transitions?

## 11.7. Relationship to Classical Collatz Formulations

The reduced formalism reorganizes the ordinary Collatz dynamics by compressing deterministic block structure and then quotienting by representative families. An important long-term question is how this framework relates to more classical odd-to-odd or accelerated Collatz maps.

In particular:

- Does the reduced map `F` recover known structures in a disguised form?
- Does it reveal genuinely new arithmetic organization not visible in standard formulations?
- Can insights from existing Collatz literature on valuations, accelerated maps, or residue graphs be translated cleanly into this reduced setting?

## 11.8. Closing Perspective

The framework developed in this note does not resolve the Collatz conjecture, but it does isolate a coherent reduced dynamical system whose exact structure can be stated cleanly. The main open problem is no longer whether the reduction is mathematically legitimate; that point has been established. The deeper challenge is to determine whether the reduced map `F` admits further compression, classification, or invariant structure beyond what is currently visible.

That question remains open, and it is the natural direction for any continuation of this program.

