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
- `m`: the `2`-adic entry depth in the BlockEntry coordinates; equivalently, `m = v_2(x + 1)`. Note: this renders `m = 0` meaningless.
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

The next proposition records the exact internal structure represented by a reduced structural state `(ω,d)`.

**Proposition 9.0.1 (Characterization of a Reduced Block).** Fix a reduced structural state `(ω,d)`. Its BlockEntry representatives are exactly

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

### 10.6. Regular and irregular lifting towers in the `ω ≡ 1 (mod 8)` branch

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

This proposed split should be regarded as empirical only. It is not yet a proved classification law, but it is a useful guide for Stage 1 of Route A. At minimum, it suggests that once the first-layer mod `8` lifting condition is met, the parameter `ω` may further control the geometry of the anchor tower through a finer arithmetic invariant. Determining whether this invariant is genuinely `ω (mod 3)`, or a shadow of a deeper structural mechanism, remains an open task.

The observed anchor towers suggest that for valid lifting families `(\omega \equiv 1 \pmod 8)`, the distinguished exponent may be a `2`-adic quantity `d_\infty(\omega)` characterized informally by

```text
3^(d_\infty) · ω = 1.
```

The visible residue towers would then be finite truncations of this `2`-adic anchor.

### 10.7. Congruence-generated anchor towers in the regular lifting branch

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

this additional example also strengthens the provisional observation of Section `10.6` that the regular tower type may be associated with the subclass

```text
ω ≡ 1 (mod 3)
```

inside the valid lifting branch `ω ≡ 1 (mod 8)`.

### 10.8. Translated halo shells in the irregular lifting branch

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

### 10.9. Centered dyadic halo template in the irregular branch

The translated-shell observation of Section `10.8` admits a sharper formulation. The irregular families do not merely appear to be related by translation in the depth variable `d`. After recentering at the primary spike, they exhibit the same raw halo template.

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

### 10.10. Relative offset branches between irregular families

The centered halo template of Section `10.9` isolates the family-independent shell geometry of the irregular branch. The remaining family-specific data is the placement of that template through the primary spike `d*(ω)`.

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

### 10.11. Primary congruence branch and 2-adic anchor in the lifting branch

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

Under this interpretation, the irregular halo law of Section `10.9` becomes more coherent. The family-specific data lies in the anchor location, while the off-spike valuations appear to follow the same centered law as the family `ω = 1`. Namely, if `d_k^*(ω)` is a primary spike at the chosen level and `Δ` is even with `Δ != 0`, then the computations suggest

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

## 10.12. Status of These Observations

The observations above are included to mark where the reduced formalism appears most suggestive, not to enlarge the proved content of the note. They indicate directions where the reduced dynamics may admit further compression or classification, but they should not be interpreted as settled structural laws.

The next section records open questions suggested by this empirical picture.

# 11. Conjectures and Open Questions

The previous sections now establish the reduced formalism at a stronger structural level than in earlier drafts. The reduced map is well-defined on structural states `(ω,d)`, the block-exit law is explicit, the role of the structural numerator

```text
A = 3^d ω - 1
```

has been isolated, and the internal representative structure of each reduced block has been clarified. In particular, the terminal interior predecessor of a reduced block is now identified canonically, and every reduced state is represented inside the fixed-exit family of its own exit value.

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

#### 11.8.1.1. The family `ω = 1`

The simplest fixed family in Stage 1 is obtained by holding

```text
ω = 1
```

and allowing `d` to vary. In this case the structural numerator becomes

```text
A = 3^d - 1,
```

so the valuation of interest is

```text
s(d) = v_2(3^d - 1).
```

This family already exhibits a rigid exact law.

**Proposition 11.8.1.1.1.** For every integer `d >= 1`,

```text
v_2(3^d - 1) =
    1,              if d is odd,
    2 + v_2(d),     if d is even.
```

**Proof.** First suppose `d` is odd. Then

```text
3^d - 1 = (3 - 1)(3^(d-1) + 3^(d-2) + ··· + 3 + 1).
```

The first factor contributes exactly one factor of `2`. The second factor is a sum of `d` odd terms. Since `d` is odd, that sum is odd. Hence

```text
v_2(3^d - 1) = 1.
```

Now suppose `d` is even. Write

```text
d = 2^r q
```

with `r = v_2(d)` and `q` odd. Then

```text
3^d - 1 = (3^(2^r))^q - 1.
```

Because `q` is odd, the odd-exponent factorization gives

```text
v_2((3^(2^r))^q - 1) = v_2(3^(2^r) - 1).
```

So it is enough to compute `v_2(3^(2^r) - 1)`. We do this by induction on `r`.

For `r = 1`,

```text
3^2 - 1 = 8,
```

so

```text
v_2(3^2 - 1) = 3 = 2 + 1.
```

Now assume

```text
v_2(3^(2^r) - 1) = r + 2.
```

Then

```text
3^(2^(r+1)) - 1 = (3^(2^r) - 1)(3^(2^r) + 1).
```

Since `3^(2^r) ≡ 1 (mod 8)` for `r >= 1`, one has

```text
3^(2^r) + 1 ≡ 2 (mod 8),
```

and therefore

```text
v_2(3^(2^r) + 1) = 1.
```

It follows that

```text
v_2(3^(2^(r+1)) - 1)
= v_2(3^(2^r) - 1) + v_2(3^(2^r) + 1)
= (r + 2) + 1
= r + 3.
```

Thus by induction,

```text
v_2(3^(2^r) - 1) = r + 2.
```

Since `r = v_2(d)`, this gives

```text
v_2(3^d - 1) = 2 + v_2(d)
```

for even `d`. Combining the odd and even cases proves the result. ∎

Two immediate corollaries are useful for the Route A program.

**Corollary 11.8.1.1.2.** In the family `ω = 1`, the value `s = 2` never occurs.

**Proof.** If `d` is odd, then `s = 1`. If `d` is even, then

```text
s = 2 + v_2(d) >= 3.
```

So `s = 2` is impossible. ∎

**Corollary 11.8.1.1.3.** In the family `ω = 1`, the quantity

```text
s - v_2(d)
```

is completely determined by the parity of `d`, namely

```text
s - v_2(d) =
    1,    if d is odd,
    2,    if d is even.
```

**Proof.** If `d` is odd, then `v_2(d) = 0` and the proposition gives `s = 1`. If `d` is even, then the proposition gives

```text
s = 2 + v_2(d),
```

so

```text
s - v_2(d) = 2.
```

This proves the claim. ∎

This family is the natural first theorem of Stage 1 because it gives a complete exact valuation law on an infinite reduced family. It also shows immediately that the valuation parity is highly structured: for odd `d` one has `s = 1`, while for even `d` one has `s >= 3` with exact growth controlled by `v_2(d)`. In particular, this provides a first rigorous example of a family on which the arithmetic bottleneck

```text
s = v_2(3^d ω - 1)
```

is not merely bounded or approximated, but determined exactly.

#### 11.8.1.2. The family `ω = 5`

A second fixed family with a fully rigid valuation law is obtained by holding

```text
ω = 5
```

and allowing `d` to vary. In this case the structural numerator becomes

```text
A = 5·3^d - 1,
```

so the valuation of interest is

```text
s(d) = v_2(5·3^d - 1).
```

Unlike the family `ω = 1`, where the even branch grows with `v_2(d)`, the family `ω = 5` is completely determined by the parity of `d`.

**Proposition 11.8.1.2.1.** For every integer `d >= 1`,

```text
v_2(5·3^d - 1) =
    1,    if d is odd,
    2,    if d is even.
```

**Proof.** First suppose `d` is odd. Since `3 ≡ -1 (mod 4)`, one has

```text
3^d ≡ -1 ≡ 3 (mod 4).
```

Also `5 ≡ 1 (mod 4)`, so

```text
5·3^d - 1 ≡ 1·3 - 1 ≡ 2 (mod 4).
```

Therefore `5·3^d - 1` is divisible by `2` but not by `4`, and hence

```text
v_2(5·3^d - 1) = 1.
```

Now suppose `d` is even. Then `d = 2k` for some integer `k >= 1`, and since

```text
3^2 = 9 ≡ 1 (mod 8),
```

it follows that

```text
3^d = (3^2)^k ≡ 1^k ≡ 1 (mod 8).
```

Because `5 ≡ 5 (mod 8)`, one obtains

```text
5·3^d - 1 ≡ 5·1 - 1 ≡ 4 (mod 8).
```

Therefore `5·3^d - 1` is divisible by `4` but not by `8`, and hence

```text
v_2(5·3^d - 1) = 2.
```

Combining the odd and even cases proves the result. ∎

Two immediate consequences are useful for Route A.

**Corollary 11.8.1.2.2.** In the family `ω = 5`, the valuation `s` is completely determined by the parity of `d`.

**Proof.** This is exactly the content of Proposition 11.8.1.2.1. ∎

**Corollary 11.8.1.2.3.** In the family `ω = 5`, `3`-gain occurs if and only if `d` is even.

**Proof.** By Lemma 9.3.1, `3`-gain occurs if and only if `s` is even. By Proposition 11.8.1.2.1, one has `s = 1` when `d` is odd and `s = 2` when `d` is even. Thus `3`-gain occurs exactly in the even case. ∎

This family provides a second exact Stage 1 theorem with a markedly different character from `ω = 1`. In the family `ω = 1`, the even branch exhibits unbounded lifting through the term `v_2(d)`. In the family `ω = 5`, by contrast, the valuation is rigidly locked at `2` on the entire even branch. Thus the reduced structural parameter `ω` can sharply change the valuation mechanism governing the block exit.

#### 11.8.1.3. The family `ω = 7`

A third fixed family with a fully rigid valuation law is obtained by holding

```text
ω = 7
```

and allowing `d` to vary. In this case the structural numerator becomes

```text
A = 7·3^d - 1,
```

so the valuation of interest is

```text
s(d) = v_2(7·3^d - 1).
```

Like the family `ω = 5`, this family is completely determined by the parity of `d`, but with the roles of the odd and even branches reversed.

**Proposition 11.8.1.3.1.** For every integer `d >= 1`,

```text
v_2(7·3^d - 1) =
    2,    if d is odd,
    1,    if d is even.
```

**Proof.** First suppose `d` is odd. Since `3 ≡ 3 (mod 8)`, one has

```text
3^d ≡ 3 (mod 8).
```

Also `7 ≡ 7 (mod 8)`, so

```text
7·3^d - 1 ≡ 7·3 - 1 = 21 - 1 = 20 ≡ 4 (mod 8).
```

Therefore `7·3^d - 1` is divisible by `4` but not by `8`, and hence

```text
v_2(7·3^d - 1) = 2.
```

Now suppose `d` is even. Then `d = 2k` for some integer `k >= 1`, and since

```text
3^2 = 9 ≡ 1 (mod 8),
```

it follows that

```text
3^d = (3^2)^k ≡ 1^k ≡ 1 (mod 8).
```

Because `7 ≡ 7 (mod 8)`, one obtains

```text
7·3^d - 1 ≡ 7·1 - 1 = 6 (mod 8).
```

Therefore `7·3^d - 1` is divisible by `2` but not by `4`, and hence

```text
v_2(7·3^d - 1) = 1.
```

Combining the odd and even cases proves the result. ∎

Two immediate consequences are useful for Route A.

**Corollary 11.8.1.3.2.** In the family `ω = 7`, the valuation `s` is completely determined by the parity of `d`.

**Proof.** This is exactly the content of Proposition 11.8.1.3.1. ∎

**Corollary 11.8.1.3.3.** In the family `ω = 7`, `3`-gain occurs if and only if `d` is odd.

**Proof.** By Lemma 9.3.1, `3`-gain occurs if and only if `s` is even. By Proposition 11.8.1.3.1, one has `s = 2` when `d` is odd and `s = 1` when `d` is even. Thus `3`-gain occurs exactly in the odd case. ∎

This family provides a third exact Stage 1 theorem and complements the families `ω = 1` and `ω = 5`. In the family `ω = 1`, the even branch exhibits deeper lifting governed by `v_2(d)`. In the family `ω = 5`, the valuation is rigidly locked at `1` on odd `d` and at `2` on even `d`. In the family `ω = 7`, that parity law is reversed: the odd branch is locked at `2`, while the even branch is locked at `1`. Together, these examples show that the reduced structural parameter `ω` strongly controls the first-layer valuation pattern governing block exit.

#### 11.8.1.4. First-layer residue classification modulo `8`

The families `ω = 1`, `ω = 5`, and `ω = 7` suggest that the first arithmetic split in the valuation

```text
s = v_2(3^d ω - 1)
```

is controlled not by the full value of `ω`, but first by its residue class modulo `8`.

This does **not** determine the exact value of `s` in every case. Rather, it determines the first valuation layer: whether `s = 1`, `s = 2`, or `s >= 3`.

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

The proposition should be read as a coarse entry theorem for Stage 1. It determines the first valuation layer, but it does **not** in general determine the full value of `s`. In particular, when the congruence only forces

```text
A ≡ 0 (mod 8),
```

the exact value of `s` may still vary.

For example, in the family `ω = 9`, one has `ω ≡ 1 (mod 8)`, so the proposition predicts

```text
s = 1   for odd d,
s >= 3  for even d.
```

That prediction is correct, but the exact even-branch values vary:

```text
d = 2  =>  s = 4,
d = 4  =>  s = 3,
d = 6  =>  s = 5,
d = 8  =>  s = 3,
...
```

Thus the residue class of `ω (mod 8)` gives the first branching law, while deeper lifting inside the branches with `s >= 3` requires finer analysis.

This makes modulo `8` the natural first classifier in Route A: it does not solve the valuation problem completely, but it sharply partitions the reduced state space into families with different first-layer valuation behavior.

#### 11.8.1.5. Anchored lifting: the family `ω = 17`

The family `ω = 17` provides the first clear indication that deeper lifting is organized around a distinguished exponent, rather than directly by `d` alone. Restricting to the lifting branch `d` even, define

```text
A_d = 17·3^d - 1,
s(d) = v_2(A_d).
```

Direct computation gives:

```text
d =  2  =>  s = 3
d =  4  =>  s = 5
d =  6  =>  s = 3
d =  8  =>  s = 4
d = 10  =>  s = 3
d = 12  =>  s = 8
d = 14  =>  s = 3
d = 16  =>  s = 4
d = 18  =>  s = 3
d = 20  =>  s = 5
d = 22  =>  s = 3
d = 24  =>  s = 4
d = 26  =>  s = 3
d = 28  =>  s = 6
...
```

This pattern is not explained by `v_2(d)` alone. Instead, it is centered at the distinguished exponent

```text
d_0 = 12,
```

for which

```text
17·3^12 - 1 = 9034496,
v_2(17·3^12 - 1) = 8.
```

The surrounding values are then governed by the distance from this anchor.

**Observation 11.8.1.5.1.** In the family `ω = 17`, the sampled even branch satisfies

```text
s(d) = 2 + v_2(d - 12)
```

for every even `d != 12` in the computed range, while at the anchor itself one has

```text
s(12) = 8.
```

Equivalently, the valuation pattern is symmetric about `d = 12` and increases according to the `2`-adic order of the displacement from that center.

For example:

```text
d = 10  =>  d - 12 = -2   =>  s = 2 + v_2(2)  = 3
d =  8  =>  d - 12 = -4   =>  s = 2 + v_2(4)  = 4
d =  4  =>  d - 12 = -8   =>  s = 2 + v_2(8)  = 5
d = 20  =>  d - 12 =  8   =>  s = 2 + v_2(8)  = 5
d = 28  =>  d - 12 = 16   =>  s = 2 + v_2(16) = 6.
```

This suggests that the correct local variable is not `d`, but the displacement

```text
e = d - d_0
```

from an anchor exponent `d_0`.

The mechanism can be seen by writing `d = 12 + e`. Since

```text
17·3^12 = 1 + 2^8 u
```

for some odd integer `u`, one has

```text
17·3^d - 1
= 17·3^(12+e) - 1
= (1 + 2^8 u)3^e - 1
= (3^e - 1) + 2^8 u·3^e.
```

When `e` is even and nonzero, Proposition 11.8.1.1.1 gives

```text
v_2(3^e - 1) = 2 + v_2(e).
```

The second term has valuation `8`, so whenever

```text
2 + v_2(e) < 8,
```

the first term dominates and yields

```text
v_2(17·3^d - 1) = 2 + v_2(e) = 2 + v_2(d - 12).
```

At `e = 0`, the first term vanishes, and the anchor value

```text
v_2(17·3^12 - 1) = 8
```

is recovered.

This does not yet amount to a general theorem for all lifting families, but it strongly suggests the next structural principle:

> deeper lifting is organized around anchor exponents `d_0(ω)` satisfying high-power congruences of the form
> `3^d0 ω ≡ 1 (mod 2^k)`.

Near such an anchor, the valuation appears to follow a translated `ω = 1` law in the displacement variable `d - d_0`, up to the height of the anchor itself.

Thus the family `ω = 17` provides the first evidence that the lifting problem is not merely a matter of parity or of `v_2(d)`, but of `2`-adic proximity to a distinguished exponent.

#### 11.8.1.6. Nested anchor tower: the family `ω = 25`

The family `ω = 25` provides a cleaner example of nested lifting than the family `ω = 17`. Restricting again to the lifting branch `d` even, define

```text
A_d = 25·3^d - 1,
s(d) = v_2(A_d).
```

Direct computation begins:

```text
d =  2  =>  s = 5
d =  4  =>  s = 3
d =  6  =>  s = 4
d =  8  =>  s = 3
d = 10  =>  s = 7
d = 12  =>  s = 3
d = 14  =>  s = 4
d = 16  =>  s = 3
d = 18  =>  s = 5
d = 20  =>  s = 3
d = 22  =>  s = 4
d = 24  =>  s = 3
d = 26  =>  s = 6
d = 28  =>  s = 3
d = 30  =>  s = 4
...
```

Unlike the family `ω = 17`, where the first visible anchor at `d = 12` was already mixed with secondary refinement, the family `ω = 25` exhibits an exact first shell on congruence classes modulo `16`:

```text
d ≡  0, 4, 8, 12 (mod 16)  =>  s = 3,
d ≡  6, 14       (mod 16)   =>  s = 4,
d ≡  2           (mod 16)   =>  s = 5,
d ≡ 10           (mod 16)   =>  deeper lifting.
```

Thus the entire even branch is rigid except for the single class

```text
d ≡ 10 (mod 16),
```

which carries the full lifting tower.

Sampling that class gives:

```text
d =  10  =>  s =  7
d =  26  =>  s =  6
d =  42  =>  s =  8
d =  58  =>  s =  6
d =  74  =>  s =  7
d =  90  =>  s =  6
d = 106  =>  s =  9
d = 122  =>  s =  6
d = 138  =>  s =  7
d = 154  =>  s =  6
d = 170  =>  s =  8
d = 186  =>  s =  6
d = 234  =>  s = 10
d = 490  =>  s = 12
d = 1514 =>  s = 17
...
```

This shows that the exceptional class modulo `16` does not merely contain one isolated anchor. Rather, it refines into a nested sequence of distinguished congruence classes modulo higher powers of `2`.

A representative refinement chain is:

```text
10  (mod 16)
10  (mod 32)
42  (mod 64)
106 (mod 128)
234 (mod 256)
...
```

and the observed behavior is:

```text
d ≡ 26  (mod 32)   =>  s = 6,
d ≡ 10  (mod 32)   =>  further lifting;

d ≡ 10  (mod 64)   =>  s = 7,
d ≡ 42  (mod 64)   =>  further lifting;

d ≡ 42  (mod 128)  =>  s = 8,
d ≡ 106 (mod 128)  =>  further lifting;

d ≡ 106 (mod 256)  =>  s = 9,
d ≡ 234 (mod 256)  =>  further lifting.
```

So the family `ω = 25` suggests a sharper structural principle than a single anchor exponent:

> the lifting branch may be governed by an `ω`-dependent nested tower of congruence classes in `d`.

In this family, the tower is especially clean: each stage splits the current exceptional class into one stabilized branch of fixed valuation and one deeper branch that continues to lift.

This gives a more precise picture of the role of `ω` in Stage 1. The parameter `ω` does not merely determine whether lifting is possible. It appears to determine the geometry of the lifting tower itself: the distinguished residue classes in `d` along which progressively higher `2`-adic contact occurs.

Accordingly, the family `ω = 25` should be regarded as the first clear example of a nested anchor tower in the reduced lifting regime.

#### 11.8.1.7. Lifting on the even branch as a congruence problem in base `9`

The empirical anchor-tower phenomena of Section `10` admit an exact first reformulation inside Route A. The key point is that on the lifting branch, the structural valuation problem is naturally a problem in the exponent variable for the base `9`.

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

This proposition does not yet classify the lifting branch completely, but it shows that once one is in the even branch `d = 2n`, the valuation problem is no longer most naturally viewed as a problem about powers of `3`. It becomes a congruence problem in the exponent variable for the base `9`.

Accordingly, the condition

```text
v_2(3^(2n) ω - 1) >= k
```

is exactly the condition that `n` lie in a solution class of

```text
9^n ≡ ω^(-1) (mod 2^k).
```

This is the first exact bridge between the formal Route A program and the anchor towers observed empirically in Section `10`. In particular, the distinguished residue classes seen in the regular lifting families are naturally interpreted as successive truncations of congruence solutions in the exponent variable `n`, transported back to `d = 2n`.

Thus the appearance of the base `9` in the regular lifting branch is not accidental. It is forced by the even-branch lifting condition itself.

#### 11.8.1.8. Congruence towers on the lifting branch

Proposition `11.8.1.7.1` shows that on the even branch `d = 2n`, the valuation condition

```text
v_2(3^d ω - 1) >= k
```

is equivalent to the congruence

```text
9^n ≡ ω^(-1) (mod 2^k).
```

This suggests the following definitions.

**Definition 11.8.1.8.1 (raw congruence level).** Let `ω` be odd, and let `k >= 4`. The level-`k` congruence set of `ω` is

```text
T_k(ω) = { n (mod 2^(k-3)) : 9^n ≡ ω^(-1) (mod 2^k) },
```

whenever this congruence is considered on the even branch `d = 2n`.

Note that while `11.8.1.7.1` applies to all k >= 1, for tower-congruence discussion k < 4 is not meaningful in this formulation.

Equivalently, the corresponding level-`k` residue set in the original depth variable is

```text
D_k(ω) = { d = 2n : n in T_k(ω) }.
```

These sets record exactly the residue classes on which

```text
v_2(3^d ω - 1) >= k.
```

**Definition 11.8.1.8.2 (lifting branch).** The lifting branch is the branch on which the first-layer mod `8` classification forces

```text
v_2(3^d ω - 1) >= 3.
```

In the valid reduced setting with `3 ∤ ω`, this occurs for

```text
ω ≡ 1 (mod 8),   d even.
```

Accordingly, the congruence tower is primarily studied on this branch.

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

**Definition 11.8.1.8.4 (regular congruence tower).** A distinguished congruence tower is called regular if, empirically, at each stage one branch stabilizes at a fixed valuation while a unique deeper branch continues to lift. In the current data, this is the behavior observed for

```text
ω = 25, 49, 73.
```

By contrast, families such as

```text
ω = 17, 41
```

still appear to admit anchor structure, but the refinement is not cleanly one-branch-at-a-time. Those cases will be referred to provisionally as irregular.

These definitions deliberately separate three issues:

1. the exact congruence reformulation of the valuation problem,
2. the existence of compatible nested solution classes,
3. the empirical regularity or irregularity of the resulting tower.

At present, only the first of these is fully formal. The second and third remain partly empirical, though strongly supported by the computed examples.

#### 11.8.2. Provisional map of tower structures

This subsection is a synthesis layer for Route A. The preceding subsections develop individual valuation families, empirical lifting examples, and the first exact congruence reformulation. The purpose of the present subsection is to collect the emerging tower structures in one place so that the global picture does not remain fragmented across family-by-family examples.

The guiding distinction is that Route A now appears to have three structural layers:

1. a first-layer partition of the valuation problem by the residue class of `ω (mod 8)`,
2. a congruence-tower mechanism on the lifting branch, expressed through the base-`9` congruences
   `9^n ≡ ω^(-1) (mod 2^k)`,
3. and an empirical classification of tower geometries, including regular, irregular, and collapsed families.

The following subsections record this map provisionally.

##### 11.8.2.1. First-layer partition of the reduced state space

This subsection will summarize the first-layer mod `8` classification proved in `11.8.1.4`.

Provisional contents:
- the non-lifting branches,
- the lifting branch,
- the exact first-layer conclusions for `s = 1`, `s = 2`, and `s >= 3`,
- and the restriction to valid reduced families with `3 ∤ ω`.

Intended role:
- to give the coarse partition of the valuation problem before any tower analysis begins.

##### 11.8.2.2. Lifting branch and congruence-tower mechanism

This subsection will summarize the exact reformulation proved in `11.8.1.7` and the definitions introduced in `11.8.1.8`.

Provisional contents:
- the even-branch substitution `d = 2n`,
- the equivalence
  `v_2(3^(2n) ω - 1) >= k  <=>  9^n ≡ ω^(-1) (mod 2^k)`,
- the raw congruence sets `T_k(ω)`,
- the induced residue sets in `d`,
- and the notion of a distinguished congruence tower.

Intended role:
- to identify the exact arithmetic object that generates tower behavior on the lifting branch.

##### 11.8.2.3. Tower archetypes observed so far

The computed examples now suggest that the lifting branch does not exhibit a single uniform tower geometry. Instead, several distinct archetypes have appeared.

**(a) Global anchor model.** The family

```text
ω = 1
```

is the fundamental anchored lifting family. On the even branch one has the exact law

```text
v_2(3^d - 1) = 2 + v_2(d),
```

so the lifting behavior is globally anchored at

```text
d0 = 0.
```

This family does not exhibit a separate halo structure. Its even branch is already governed by the global anchor law itself.

**(b) Regular congruence-generated towers.** The families

```text
ω = 25, 49, 73
```

all lie in the valid lifting branch

```text
ω ≡ 1 (mod 8),   3 ∤ ω,
```

and, in the current data, exhibit the same regular tower behavior. In these families:

* the even branch first splits rigidly by residue classes modulo `16`,
* exactly one exceptional class carries deeper lifting,
* and that exceptional class refines cleanly through higher powers of `2`.

Moreover, the distinguished lifting classes are recovered by solving the congruence tower

```text
9^n ≡ ω^(-1) (mod 2^k),
d = 2n.
```

Thus the regular branch appears to be governed directly by a distinguished congruence tower, with no visible halo surrounding the main branch.

**(c) Irregular congruence-centered halo towers.** The families

```text
ω = 17, 41, 65, 89
```

also lie in the valid lifting branch, and again admit a distinguished congruence branch obtained from

```text
9^n ≡ ω^(-1) (mod 2^k),
d = 2n.
```

However, unlike the regular cases, the main branch is accompanied by a visible halo structure. The current data suggests the following more precise picture:

* each family has a primary congruence branch `d*_k(ω)`,
* the shell profile around that branch is not family-specific noise,
* after recentering at the primary spike, the same centered dyadic halo template appears,
* and the different irregular families are related by translation of this common template in the depth variable `d`.

So the irregular branch is no longer best described as merely “mixed.” It appears to realize a coherent geometry of the form

```text
primary congruence branch  +  universal centered dyadic halo template.
```

**(d) Collapsed or absorbed families.** Families with

```text
3 ∣ ω
```

do not appear as genuinely new reduced lifting families in the same way. Instead, the `3`-adic content is absorbed before a new reduced family is obtained. These should therefore be treated separately from the genuinely new tower archetypes above.

At present, the observed tower taxonomy may be summarized as follows.

```text
global anchor model                 : ω = 1
regular congruence-generated towers : ω = 25, 49, 73
irregular halo towers               : ω = 17, 41, 65, 89
collapsed / absorbed families       : 3 ∣ ω
```

This taxonomy is still partly empirical, but it is already strong enough to guide the Route A program. In particular, the lifting branch now appears to divide not simply into “families with formulas” and “families without formulas,” but into different geometric tower types with different governing mechanisms.

A further refinement has now emerged inside the irregular tower archetype. The irregular families do not merely exhibit a main congruence tower together with surrounding residual structure. After centering at the primary spike `d*(ω)`, the residual shells appear to follow a universal dyadic halo template, independent of the particular family.

Empirically, at modulus `2^m`, the centered halo shells occur at

```text
Δ = 0,
Δ = 2^(m-1),
Δ = odd multiples of 2^(m-2),
Δ = odd multiples of 2^(m-3),
Δ = odd multiples of 2^(m-4),
...
```

modulo `2^m`, and the shell profile at modulus `2^(m+1)` appears as a one-level extension of the profile at modulus `2^m`.

Moreover, around a high primary spike `d*`, the irregular halo appears to satisfy the transplanted `ω = 1` valuation law off the spike:

```text
v_2(ω·3^(d*+Δ) - 1) = 2 + v_2(Δ)
```

for even `Δ != 0`, while the spike itself carries the exceptional height

```text
v_2(ω·3^(d*) - 1) = A.
```

Thus the irregular archetype is now provisionally understood as

```text
primary congruence branch  +  universal centered dyadic halo template,
```

with family dependence entering through the placement of the primary spike and its height.

##### 11.8.2.4. Provisional arithmetic classifiers

This subsection will collect classifier hypotheses that are still empirical.

Provisional contents:

* the mod `3` split currently suggested by computation,
* namely
  `ω ≡ 1 (mod 3)` as a candidate regular subclass,
  `ω ≡ 2 (mod 3)` as a candidate irregular subclass,
  and `ω ≡ 0 (mod 3)` as absorbed into the `3`-adic content,
* together with a reminder that this remains heuristic rather than proved.

Intended role:

* to keep conjectural classification separate from proved structure.

##### 11.8.2.5. Relationship between family examples and the tower map

This subsection will explain how the earlier family-by-family subsections should now be read.

Provisional contents:

* `11.8.1.1` through `11.8.1.4` as first-layer valuation families,
* `11.8.1.5` and `11.8.1.6` as initial tower-discovery examples,
* `11.8.1.7` and `11.8.1.8` as the formal bridge from valuation behavior to congruence towers.

Intended role:

* to prevent the preceding examples from reading as isolated computations rather than pieces of a single structural program.

#### 11.8.2.6. Primary congruence branch, universal halo law, and the remaining arithmetic problem

The lifting-branch valuation condition is governed by a congruence tower in the exponent variable. Section `11.8.1.7.1` makes this precise: writing

```text
d = 2n,
```

the condition

```text
v_2(3^d ω - 1) >= k
```

is equivalent to

```text
9^n ≡ ω^(-1) (mod 2^k).
```

So the primary branch should first be understood as a congruence-theoretic object on the valid lifting branch `ω ≡ 1 (mod 8)`. The distinction between regular and irregular families enters only at the next level: in regular families, the visible lifting geometry appears to be exhausted by this branch alone; in irregular families, the same branch appears together with a universal local halo law after centering.

The evidence of Sections `10.9`–`10.11` therefore suggests the following decomposition:

* a **family-dependent primary congruence branch**, and
* a **universal local valuation law** after centering at that branch.

This is the key conceptual shift. The main unresolved problem is no longer to describe the halo geometry itself. The centered halo appears to be universal. The remaining problem is to identify the arithmetic law governing the family-dependent anchor.

**Convention.**
Throughout the remainder of `11.8.2.6`, the branch quantities
```text
n_k(ω) \pmod{2^(k-3)}, \qquad d_k^*(ω) = 2n_k(ω) \pmod{2^(k-2)}
```

are considered only for levels

```text
k >= 4.
```

The underlying congruence

```text
9^n ≡ ω^(-1) \pmod{2^k}
```

still makes sense for smaller `k`, but the branch formalism in terms of residue classes modulo `2^(k-3)` begins only at `k = 4`, where the lifting-branch structure becomes nondegenerate in the present formulation.

##### 11.8.2.6.1. The primary congruence branch on the lifting branch

The lifting-branch congruence condition already isolates the family-dependent anchor as an exact arithmetic object.

**Theorem 11.8.2.6.1 (existence, uniqueness, and compatibility of the primary congruence branch).**  
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
`n_(k+1)(ω) (mod 2^(k-2))` reduces to the class `n_k(ω) (mod 2^(k-3))`.

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

Uniqueness modulo `2^(k-3)` follows from the fact that the order of `9` modulo `2^k`
is exactly `2^(k-3)`.

Now let `n_(k+1)(ω)` be the unique class modulo `2^(k-2)` satisfying

```text
9^n ≡ ω^(-1) (mod 2^(k+1)).
```

Reducing this congruence modulo `2^k` shows that the reduced class also solves

```text
9^n ≡ ω^(-1) (mod 2^k).
```

By uniqueness at level `k`, this reduced class must equal `n_k(ω) (mod 2^(k-3))`. This proves compatibility.

Finally, by Proposition `11.8.1.7.1`, on the even branch `d = 2n` the congruence
condition is equivalent to

```text
v_2(ω·3^d - 1) >= k.
```

So the corresponding depth-side class

```text
d_k^*(ω) = 2 n_k(ω)
```

is uniquely determined as well. ∎

**Interpretation.**
The primary branch is therefore not a special empirical artifact of the irregular families. It is the canonical lifting-branch congruence object attached to every valid family `ω ≡ 1 (mod 8)`. The family-dependent datum is the compatible branch itself.

##### 11.8.2.6.2. Universal centered halo law around a branch point

Once a branch point is fixed, the surrounding local valuation geometry is universal up to the height of that point.

**Theorem 11.8.2.6.2 (centered halo law below spike height).**
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

##### 11.8.2.6.3. Boundary-shell localization and the dyadic refinement barrier

The centered halo law of `11.8.2.6.2` already shows that no distinct displacement can match the spike height before the scale `2^(H-2)`. The next calculation shows more: once one reaches and passes that scale, the only shell on which genuinely higher off-spike lifting can occur is the first allowable boundary shell itself.

**Proposition 11.8.2.6.3 (boundary-shell localization).**
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

and Theorem `11.8.2.6.2` already yields

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
3^Δ - 1 = 2^(H+r) a
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

**Corollary 11.8.2.6.3A (dyadic refinement barrier, sharpened form).**
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
The local centered halo law therefore has a much sharper consequence than the original divisibility barrier alone. The valuation geometry around a spike of height `H` splits into three regions:

```text
below the boundary shell      : universal transplanted law  2 + v_2(Δ),
beyond the boundary shell     : exact return to height H,
on the boundary shell itself  : the only place where further off-spike lifting can occur.
```

Thus the unresolved part of the global halo problem is no longer spread across all large displacements. It is concentrated on one dyadic shell, namely

```text
v_2(Δ) = H - 2.
```

So the next arithmetic question is not whether the transplanted halo law can fail arbitrarily far from the spike. It is whether the boundary-shell term

```text
α + u·3^Δ
```

admits a further universal description, or whether it carries the remaining family-specific refinement mechanism.

##### 11.8.2.6.3B. Arithmetic normal form on the boundary shell

Proposition `11.8.2.6.3` shows that once a spike point

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

So the remaining problem is not a diffuse global failure of the centered halo law. It is concentrated in one arithmetic correction term on that shell. The purpose of the present subsection is to isolate that term in a normalized form.

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
Δ = 2^(H-2) t,
```

with `t` odd.

For such a displacement, Proposition `11.8.2.6.3` gives

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

**Definition 11.8.2.6.3B.1 (boundary-shell correction term).**
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

So the full off-spike valuation picture now has the following form.

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

Thus every possible failure of the universal centered halo law is reduced to the arithmetic of the single function

```text
B_H(u,t).
```

Equivalently, once the spike height `H` and normalized spike unit `u` are fixed, the remaining unresolved part of the halo problem is a valuation problem in the odd shell parameter `t`.

This is the desired arithmetic normal form for the boundary shell.

**Interpretation.**
The family dependence has now been compressed further than in `11.8.2.6.3`. After centering at the spike and normalizing by the spike height, the boundary-shell problem no longer depends on the original pair `(ω,d_*)` directly. It depends only on:

* the spike height `H`,
* the normalized spike unit

  ```text
  u = (ω·3^(d_*) - 1)/2^H,
  ```
* and the odd shell coordinate `t`.

So the remaining Route A Stage `1B` question may be restated as follows:

> does the valuation `v_2(B_H(u,t))` admit a universal law in `t`, or does the normalized spike unit `u` carry a genuine residual family-specific invariant beyond the anchor coordinate?

In this form, the unresolved part of the global halo picture is no longer a broad geometric question. It is the arithmetic problem of understanding the correction term

```text
B_H(u,t) = α_H(t) + u·3^(2^(H-2)t)
```

on odd `t`.

**Lemma 11.8.2.6.3B.2 (first universal divisibility on the boundary shell).**
Let `d_*` be a spike point of height

```text
H = v_2(ω·3^(d_*) - 1),
```

and write

```text
ω·3^(d_*) - 1 = 2^H u
```

with `u` odd. Let

```text
Δ = 2^(H-2)t
```

with `t` odd, and let

```text
B_H(u,t) = α_H(t) + u·3^(2^(H-2)t),
```

where

```text
α_H(t) = (3^(2^(H-2)t) - 1)/2^H.
```

Then:

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
By construction,

```text
α_H(t) = (3^(2^(H-2)t) - 1)/2^H.
```

Since `t` is odd, the displacement

```text
Δ = 2^(H-2)t
```

satisfies

```text
v_2(Δ) = H - 2.
```

So Proposition `11.8.2.6.3` gives

```text
v_2(3^Δ - 1) = H.
```

Therefore

```text
3^Δ - 1 = 2^H α_H(t)
```

with `α_H(t)` odd. This proves (1).

Next, `u` is odd by definition, and `3^(2^(H-2)t)` is odd because it is a power of the odd integer `3`. Hence their product

```text
u·3^(2^(H-2)t)
```

is odd. This proves (2).

Now `B_H(u,t)` is the sum of the two odd integers `α_H(t)` and `u·3^(2^(H-2)t)`, so `B_H(u,t)` is even. This proves (3), and hence

```text
v_2(B_H(u,t)) >= 1.
```

Finally, by Definition `11.8.2.6.3B.1`,

```text
ω·3^(d_* + 2^(H-2)t) - 1 = 2^H B_H(u,t).
```

Taking `v_2` on both sides yields

```text
v_2(ω·3^(d_* + 2^(H-2)t) - 1)
= H + v_2(B_H(u,t))
>= H + 1.
```

This proves the claim. ∎

**Interpretation.**
The boundary shell is not merely the first shell on which off-spike excess may occur. It is a shell on which one always gains at least one additional factor of `2` beyond the spike height `H`. Thus every boundary-shell displacement satisfies

```text
v_2(ω·3^(d_* + Δ) - 1) >= H + 1.
```

So the remaining issue is no longer whether the boundary shell can exceed height `H` at all. It always does. The real arithmetic question is how large

```text
v_2(B_H(u,t))
```

can be, and whether that higher-order cancellation is governed universally or depends essentially on the normalized spike unit `u`.

**Lemma 11.8.2.6.3B.3 (boundary-shell correction term modulo `4`, corrected form).**
Let `d_*` be a spike point of height

```text
H = v_2(ω·3^(d_*) - 1),
```

and write

```text
ω·3^(d_*) - 1 = 2^H u
```

with `u` odd. Let

```text
Δ = 2^(H-2)t
```

with `t` odd, and let

```text
B_H(u,t) = α_H(t) + u·3^(2^(H-2)t),
```

where

```text
α_H(t) = (3^(2^(H-2)t) - 1)/2^H.
```

Then for every `H >= 3` and every odd `t` one has

```text
α_H(t) ≡ t (mod 4),
```

and

```text
3^(2^(H-2)t) ≡ 1 (mod 4).
```

Consequently,

```text
B_H(u,t) ≡ t + u (mod 4).
```

Hence

```text
v_2(B_H(u,t)) >= 2
if and only if
u ≡ t (mod 4).
```

**Proof.**

First, since `H >= 3` and `t` is odd, the exponent

```text
2^(H-2)t
```

is even. Therefore

```text
3^(2^(H-2)t) ≡ 1 (mod 4),
```

because every even power of `3` is congruent to `1 mod 4`. Hence

```text
u·3^(2^(H-2)t) ≡ u (mod 4).
```

So it remains to compute `α_H(t) mod 4`.

By definition,

```text
α_H(t) = (3^(2^(H-2)t) - 1)/2^H.
```

To determine this modulo `4`, it is enough to compute

```text
3^(2^(H-2)t)
```

modulo `2^(H+2)`.

We first record the base congruence

```text
3^(2^(H-2)) ≡ 1 + 2^H (mod 2^(H+2))
```

for every `H >= 3`.

For `H = 3`, this says

```text
3^2 = 9 ≡ 1 + 8 (mod 32),
```

which is immediate.

For `H >= 4`, one has

```text
v_2(3^(2^(H-2)) - 1) = H
```

by Proposition `11.8.1.1.1`, so we may write

```text
3^(2^(H-2)) = 1 + 2^H β
```

with `β` odd. Reducing modulo `8`, one has

```text
3^(2^(H-2)) = (3^4)^(2^(H-4)) ≡ 1^(2^(H-4)) ≡ 1 (mod 16)
```

for `H >= 4`, so after subtracting `1` and dividing by `2^H` it follows that `β ≡ 1 (mod 4)` from 1 (mod 16). Hence

```text
3^(2^(H-2)) ≡ 1 + 2^H (mod 2^(H+2)).
```

Now raise this congruence to the odd power `t`. Since `H >= 3`, the square of `2^H` is divisible by `2^(H+2)`, because

```text
2^(2H) = 2^(H+2) · 2^(H-2).
```

So by the binomial theorem,

```text
(1 + 2^H)^t ≡ 1 + t·2^H (mod 2^(H+2)).
```

Therefore

```text
3^(2^(H-2)t)
=
(3^(2^(H-2)))^t
≡
(1 + 2^H)^t
≡
1 + t·2^H
(mod 2^(H+2)).
```

Subtracting `1` and dividing by `2^H` gives

```text
α_H(t) = (3^(2^(H-2)t) - 1)/2^H ≡ t (mod 4).
```

This proves the first claim.

Combining this with

```text
u·3^(2^(H-2)t) ≡ u (mod 4)
```

yields

```text
B_H(u,t) = α_H(t) + u·3^(2^(H-2)t) ≡ t + u (mod 4).
```

Finally, Lemma `11.8.2.6.3B.2` shows that `B_H(u,t)` is always even, so

```text
v_2(B_H(u,t)) >= 2
if and only if
B_H(u,t) ≡ 0 (mod 4).
```

By the congruence just proved, this is equivalent to

```text
t + u ≡ 0 (mod 4).
```

Since `t` and `u` are odd, this is the same as

```text
u ≡ t (mod 4).
```

This proves the lemma. ∎

**Interpretation.**
The first higher-order cancellation on the boundary shell is governed by a single uniform rule, independent of the spike height `H`:

```text
v_2(B_H(u,t)) >= 2
if and only if
u ≡ t (mod 4).
```

So the first refinement beyond the universal evenness of the boundary-shell correction term is not a separate `H = 3` versus `H >= 4` phenomenon. It is a universal congruence matching condition between the normalized spike unit `u` and the odd shell coordinate `t`.

In particular, the first nontrivial boundary-shell jump is already controlled by a very small arithmetic package:

* the shell coordinate `t (mod 4)`, and
* the spike unit `u (mod 4)`.

This is the first exact sign that the residual family dependence on the boundary shell may be much smaller than the original `(ω,d_*)` data.

##### 11.8.2.6.4. Ratio law for relative branch offsets

Because the primary branch is unique at each level, relative offsets between families are governed by the same congruence mechanism as the branches themselves.

**Theorem 11.8.2.6.4 (ratio-law encoding of relative branch offsets).**
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
By Theorem `11.8.2.6.1`, one has

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

since both factors lie in `1 (mod 8)`. Therefore Theorem `11.8.2.6.1` applies again, this time to the ratio `ω_1 · ω_2^(-1)`, and yields a unique solution class modulo `2^(k-3)`. Hence the difference class above is exactly that unique class.

This proves the claim. ∎

**Interpretation.**
Relative branch placement is therefore not a secondary phenomenon requiring a new mechanism. It is governed by the same congruence law as the branch itself, now applied to the ratio of the two family parameters. So family-to-family displacement is not additional family-specific data beyond the primary branch mechanism; it is already encoded by that mechanism.

##### 11.8.2.6.5. The global 2-adic anchor `N(ω)`

The finite-level primary congruence branches now assemble canonically into a single global `2`-adic coordinate on the lifting branch.

**Definition 11.8.2.6.5.1 (global exponent-side anchor).**
Let `ω` be odd with

```text
ω ≡ 1 (mod 8).
```

For each `k >= 4`, let

```text
n_k(ω) (mod 2^(k-3))
```

denote the unique compatible solution class from Theorem `11.8.2.6.1`, characterized by

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

We call `N(ω)` the **global 2-adic anchor** of the lifting family `ω`.

Equivalently,

```text
N(ω) = lim← n_k(ω).
```

**Definition 11.8.2.6.5.2 (global depth-side anchor).**
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

is the primary branch class of Theorem `11.8.2.6.1`.

So the compatible finite truncations `d_k^*(ω)` are exactly the finite-level shadows of the single global `2`-adic anchor `D^*(ω)`.

**Proposition 11.8.2.6.5.3 (characterizing property of `N(ω)`).**
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
This is immediate from Theorem `11.8.2.6.1`. Existence and compatibility of the finite classes `n_k(ω)` give an inverse-limit element of `Z_2`, and uniqueness follows because an element of `Z_2` is uniquely determined by its reductions modulo `2^m` for all `m >= 1`. ∎

**Proposition 11.8.2.6.5.4 (global ratio law).**
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
For each `k >= 4`, Theorem `11.8.2.6.4` shows that the difference class

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
The family-dependent anchor is therefore no longer best viewed as a collection of unrelated finite congruence classes. It is a single global `2`-adic coordinate on the lifting branch.

The finite classes

```text
n_k(ω), d_k^*(ω)
```

are simply truncations of that one object.

In particular:

* the family-dependent datum is the global anchor `N(ω)` (or equivalently `D^*(ω)`),
* the relative displacement between families is additive in this coordinate,
* and the local halo law of Theorem `11.8.2.6.2` should be read as a universal law in displacement from that anchor, not as additional family-specific structure.

So the conceptual picture becomes

```text
family-dependent global 2-adic anchor
+ universal centered valuation law.
```

**Transition.**
The preceding results define `N(ω)` intrinsically as an inverse-limit anchor. The next subsection shows that this anchor is not merely a formal inverse-limit object: it is the natural additive coordinate on the lifting branch.

##### 11.8.2.6.6. The anchor map `N(ω)` as the additive coordinate on the lifting branch

The inverse-limit construction of `11.8.2.6.5` may now be sharpened. The compatible congruence classes do not merely define a family of finite truncations; they define the natural additive coordinate on the lifting branch.

**Theorem 11.8.2.6.6.1 (additive coordinate property of `N`).**
Let
```text
G = 1 + 8\mathbf{Z}_2,
```

viewed as a multiplicative subgroup of the odd `2`-adic units. For each `ω in G`, let

```text
N(ω) in \mathbf{Z}_2
```

be the inverse-limit anchor defined in `11.8.2.6.5.1`, so that for every `k >= 4`,

```text
N(ω) ≡ n_k(ω) \pmod{2^(k-3)},
```

where `n_k(ω)` is the unique class satisfying

```text
9^n ≡ ω^(-1) \pmod{2^k}.
```

Then `N` is a group isomorphism from the multiplicative group `G` to the additive group `\mathbf{Z}_2`. Equivalently, for all `ω_1, ω_2 in G`,

```text
N(ω_1 ω_2) = N(ω_1) + N(ω_2),
```

and `N` is bijective.

**Proof.**
By Theorem `11.8.2.6.1`, for each `k >= 4` there is a unique class

```text
n_k(ω) \pmod{2^(k-3)}
```

satisfying

```text
9^n ≡ ω^(-1) \pmod{2^k},
```

and these classes are compatible under reduction. Hence `N(ω)` is well-defined as an element of `\mathbf{Z}_2`.

To prove the homomorphism law, fix `ω_1, ω_2 in G`. For each `k >= 4`, one has

```text
9^(n_k(ω_1)) ≡ ω_1^(-1) \pmod{2^k},
9^(n_k(ω_2)) ≡ ω_2^(-1) \pmod{2^k}.
```

Multiplying gives

```text
9^(n_k(ω_1)+n_k(ω_2)) ≡ (ω_1 ω_2)^(-1) \pmod{2^k}.
```

By uniqueness of the level-`k` solution class,

```text
n_k(ω_1 ω_2) ≡ n_k(ω_1) + n_k(ω_2) \pmod{2^(k-3)}.
```

Passing to the inverse limit yields

```text
N(ω_1 ω_2) = N(ω_1) + N(ω_2).
```

Injectivity follows immediately: if `N(ω) = 0`, then for every `k >= 4`,

```text
0 ≡ n_k(ω) \pmod{2^(k-3)},
```

so

```text
9^0 ≡ ω^(-1) \pmod{2^k},
```

hence

```text
ω ≡ 1 \pmod{2^k}
```

for all `k >= 4`. Therefore `ω = 1` in `\mathbf{Z}_2`.

For surjectivity, let `n in \mathbf{Z}_2`. For each `k >= 4`, define

```text
ω_k ≡ 9^(-n mod 2^(k-3)) \pmod{2^k}.
```

Since every power of `9` lies in `1 + 8\mathbf{Z}/2^k\mathbf{Z}`, each `ω_k` lies in that subgroup, and the classes are compatible under reduction. Hence they determine a unique element

```text
ω in 1 + 8\mathbf{Z}_2.
```

By construction, for every `k >= 4`,

```text
9^n ≡ ω^(-1) \pmod{2^k},
```

so by uniqueness,

```text
N(ω) ≡ n \pmod{2^(k-3)}
```

for all `k >= 4`. Therefore `N(ω) = n`.

Thus `N` is a group isomorphism

```text
N : 1 + 8\mathbf{Z}_2 \xrightarrow{\sim} \mathbf{Z}_2.
```

∎

**Interpretation.**
The family-dependent primary branch is therefore not best viewed as a sequence of unrelated finite congruence classes. It is the truncation of a single additive `2`-adic coordinate on the lifting branch.

Equivalently, the global anchor

```text
N(ω)
```

is the arithmetic coordinate whose finite reductions recover the branch classes

```text
n_k(ω),
d_k^*(ω) = 2n_k(ω).
```

In this language, the ratio law of Theorem `11.8.2.6.4` is simply the statement that relative branch placement is given by subtraction in the additive coordinate `N`.

**Remark.**
The present theorem is purely algebraic and does not require `2`-adic logarithm or exponential theory. If a later argument identifies the universal centered halo law globally off the spike, then the irregular lifting families would be reduced, at the valuation level, to exactly two ingredients:

```text
family-dependent anchor coordinate N(ω)
+ universal centered halo law.
```

In that stronger form, the apparent family-specific complexity of the irregular branch would be exhausted by anchor placement alone.

##### 11.8.2.6.7. Route A Stage 1B restated

With the preceding structure in place, the task of Route A Stage `1B` can now be stated more sharply.

The family-dependent primary branch is no longer best viewed as a collection of finite congruence classes. By `11.8.2.6.5` and `11.8.2.6.6`, it is the finite shadow of a single global additive `2`-adic coordinate
```text
N(ω) in \mathbf{Z}_2
```

on the lifting branch

```text
ω ≡ 1 (mod 8),
```

with corresponding depth-side anchor

```text
D^*(ω) = 2N(ω) in 2\mathbf{Z}_2.
```

So the family-dependent datum is now concentrated in the anchor coordinate itself.

On the other hand, `11.8.2.6.2` and `11.8.2.6.3` show that once a branch point `d_*` of height

```text
H = v_2(ω·3^(d_*) - 1)
```

is fixed, the surrounding local valuation geometry is universal below spike height: for every even displacement `Δ != 0` satisfying

```text
2 + v_2(Δ) < H,
```

one has

```text
v_2(ω·3^(d_* + Δ) - 1) = 2 + v_2(Δ),
```

and any competing point of valuation at least `H` must lie at a displacement divisible by

```text
2^(H-2).
```

Thus the current formal picture is already:

```text
family-dependent additive anchor coordinate N(ω)
+ universal centered halo law below spike height.
```

Accordingly, Route A Stage `1B` is now reduced to the following sharpening problem:

> determine whether the boundary-shell correction term `B_H(u,t)` admits a universal valuation law on odd `t`.

Equivalently, whether any residual family dependence survives beyond the anchor coordinate once the spike is normalized by height and centered displacement.

If that strengthening holds, then the irregular lifting families collapse, at the valuation level, to the structure

```text
N(ω) determines the branch location,
the off-spike valuation law is universal,
relative family offsets are subtraction in N.
```

So Stage `1B` is no longer primarily about discovering a new family-specific irregular mechanism. It is about testing whether the irregular branch contains any further family dependence once the anchor coordinate has been identified.

#### 11.8.2.7. Status of the synthesis map

The synthesis map now contains ingredients of three different logical types, and these should be kept distinct.

**(a) Formal.** The following components are now part of the formal structure developed in Stage 1:

- the first-layer mod `8` classification of the valuation problem,
- the isolation of the lifting branch
  `ω ≡ 1 (mod 8), d = 2n`,
- the exact reformulation
  `v_2(3^(2n) ω - 1) >= k  <=>  9^n ≡ ω^(-1) (mod 2^k)`,
- the existence, uniqueness, and compatibility of the primary congruence branch
  `n_k(ω), d_k^*(ω)`,
- the ratio law governing relative branch offsets,
- the inverse-limit global anchor
  `N(ω), D^*(ω)`,
- the additive-coordinate property of `N` on the lifting branch,
- the local centered halo law below spike height,
- the sharpened boundary-shell localization theorem:
  below the boundary shell one has the transplanted law
  `2 + v_2(Δ)`,
  beyond the boundary shell the valuation returns exactly to height `H`,
  and every off-spike displacement with valuation strictly above `H` is confined to the single shell
  `v_2(Δ) = H - 2`.
- and the arithmetic normal form of the boundary shell via `B_H(u,t)`.

These results do not yet prove the full empirical halo picture, but they do isolate both the exact arithmetic object governing the family-dependent branch and the exact local mechanism governing all off-spike valuations except the boundary shell itself.

**(b) Empirical but strongly supported.** The following components are not yet formally derived, but are now supported by repeated computation across multiple families:

- the existence of regular congruence-generated towers in the families
  `ω = 25, 49, 73`,
- the existence of irregular towers in the families
  `ω = 17, 41, 65, 89`,
- the translated shell relation among the irregular examples,
- the universal centered dyadic halo template in the irregular branch beyond the presently proved local range,
- and the interpretation that the visible irregular family dependence is exhausted by anchor placement together with a universal off-spike law.

Thus the irregular branch should no longer be regarded merely as a repository of unresolved exceptions. It already exhibits a coherent empirical geometry, and the formal results now explain part of that geometry rather than leaving it entirely heuristic.

**(c) Conjectural.** The following components remain open and should still be treated as conjectural:

- the global claim that the centered halo law holds off the spike without the present spike-height restriction,
- the resulting global claim that irregular family dependence is exhausted entirely by the additive anchor coordinate `N(ω)`,
- the possibility of a universal arithmetic description of the boundary-shell term that would complete the halo theorem,
- the proposed arithmetic classifier separating regular and irregular tower types,
- the possibility that the split is governed by `ω (mod 3)`,
- the global claim that all valid `ω ≡ 1 (mod 3)` families are regular,
- the global claim that all valid `ω ≡ 2 (mod 3)` families are irregular,
- and any complete description of how `ω` determines the primary spike offset and spike-height profile in the irregular branch.

So the present status of the tower map is as follows.

```text
formal:
    first-layer mod 8 partition,
    lifting branch d = 2n,
    congruence reformulation in base 9,
    primary congruence branch,
    ratio law for relative offsets,
    global anchor N(ω),
    additive-coordinate structure on the lifting branch,
    local centered halo law below spike height,
    boundary-shell localization of all possible off-spike excess
    arithmetic normal form of the boundary shell

empirical but strongly supported:
    regular congruence-generated towers,
    irregular congruence-centered halo towers,
    translated shell relations,
    centered dyadic halo template beyond the proved local range,
    anchor placement as the visible family-dependent irregular datum

conjectural:
    full global off-spike halo law,
    complete exhaustion of irregular family dependence by N(ω),
    universal control of the boundary-shell refinement term,
    full arithmetic classifier of tower type,
    global dependence of offset and spike profile on ω
```

This distinction is important for the discipline of Route A. The synthesis map is now substantially stronger than a purely empirical guide: the branch mechanism is formal, the anchor mechanism is formal, and the local halo mechanism has been sharpened to a single unresolved boundary shell. So the next task is not to rediscover the branch or to search broadly for halo phenomenology, but to determine whether the remaining boundary-shell term admits a universal arithmetic description that globalizes the halo law.

### Stage 2. Convert Valuation Results into `3`-gain Theorems

The second stage is to translate Stage 1 results directly into reduced-dynamical statements. Section 9 proved that the parity of `s` controls whether the next odd seed gains a factor of `3`. Thus any exact theorem about the parity of `s` immediately becomes an exact theorem about `3`-gain. 

This suggests theorem targets of the following kind:

* families on which `3`-gain always occurs,
* families on which `3`-gain never occurs,
* or families on which `3`-gain is periodic in `d` or organized by a fixed residue description of `ω`.

These are more informative than bare valuation statements because they speak directly in the language of the reduced transition rather than only in the language of auxiliary arithmetic.

### Stage 3. Depth Evolution Through `d_+ = v_2(C) - s + v_3(C)`

Once some control of `s` has been obtained, the next natural target is the depth evolution

```text
d_+ = v_2(C) - s + v_3(C),
```

where

```text
C = 3^d ω - 1 + 2^(v_2(3^d ω - 1)).
```

Here the initial priority should not be an exact formula for all families. More realistic and more structurally informative first targets are:

* lower or upper bounds on `d_+ - d`,
* exact formulas for `d_+ - d` on specific infinite families,
* or proofs that the sign or coarse size of `d_+ - d` is controlled by a small arithmetic package attached to `A`.

Such results would constitute the first substantial dynamical classification of the reduced step beyond its formal construction. 

### Stage 4. Only Then Refine `ω_+`

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

### Strategic Summary

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
