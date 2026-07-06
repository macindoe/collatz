---
status: open / calibrated
scope: monolith sections 11-11.7 (section 10 was absorbed into index.md)
updated: 2026-07-06
source: sources/drafts/collatz_reduction_rewrite_v078.md (last monolith)
---

> **Current state.** The open-questions layer. 11.1 (valuation s) is closed and retained for orientation; the live open front is the odd core ω_+ / anchor increment law (see program.md and stage2.md 11.8.5.6). Each subsection carries its own calibration notes.

# 11. Conjectures and Open Questions

The previous sections now establish the reduced formalism at a stronger structural level than in earlier drafts. The reduced map is well-defined on structural states `(ω,d)`, the block-exit law is explicit, the role of the structural numerator

```text
A = 3^d ω - 1
```

has been isolated, and the internal representative structure of each reduced block has been clarified. In particular, the terminal interior predecessor of a reduced block is now identified canonically, and every reduced state is represented inside the fixed-exit family of its own exit value.

The observations and examples that led to these conclusions are recorded in Appendix A; they should be read as exploratory context rather than proved claims.

Accordingly, the main open problems are no longer foundational questions about whether the reduced formalism is coherent. The remaining questions are now more focused: how much of the arithmetic complexity of the reduced map can be classified, compressed, or controlled?

## 11.1. The Valuation `s = v_2(3^d ω - 1)`: A Closed Question

The quantity

```text
s = v_2(3^d ω - 1)
```

is the central arithmetic input governing the block exit. It determines the length of the forced `2`-adic cascade at exit, and through its parity it determines whether the next odd seed gains a factor of `3`.

Earlier drafts identified control of this valuation as the main arithmetic bottleneck of the program, and posed as open the regularity of `s` for fixed `ω`, its residue organization for fixed `d`, and the possible periodicity of its parity. All of these questions are now answered exactly by the Stage 1 synthesis:

* For fixed `ω`, the behavior of `s` as `d` varies is given by the exact global law `s = 3 + v_2(n - N(ω))` on the lifting branch (`11.8.4.1`), equivalently `s = 2 + v_2(d - M(ω))` in the unified depth-side form (`11.8.5.6.2`), with `s ∈ {1, 2}` constant on each residue-parity class off the lifting branch (`11.8.1.3.1`).
* For fixed `d`, the residue organization of `s` in `ω` is the mod-`8` first-layer classification together with the anchor mechanism.
* The parity of `s` is rigidly constrained on every class: it is constant off the lifting branch and determined by the shell parity of the anchor displacement on it (`11.8.5`).

What survives of the original question is calibrated in `11.8.3.6` and `11.8.3.11`: the first valuation layer is elementary lifting-the-exponent; the family-dependent structure is the `2`-adic logarithm `N(ω) = -log ω / log 9`, with unconditional polylogarithmic bounds on `s` imported from `p`-adic Baker theory; and the residual content — the fine digit statistics of those logarithms — lies beyond current theory and is in no way specific to the Collatz formulation.

The valuation is therefore no longer the bottleneck. The remaining classification burden has moved downstream, to the odd core `ω_+` and the anchor increment law (`11.8.5.6`, `11.8.7`); this section is retained because `s` remains the central input quantity, not because its law is open.

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

The first question is now closed: `d_+ = m_+ + a_+` with both terms given by exact per-step laws on every residue-parity class — the entry-depth law for `m_+` (`11.8.6.3`) and the `3`-adic absorption law for `a_+` (`11.8.6.2`) — so the depth evolution is a deterministic function of the anchor data of the current state (Corollary `11.8.6.3.6`). The remaining three questions all concentrate on the odd core `ω_+`, which is Stage 4 of the Route A program and, by `11.8.5.6`, equivalent to the anchor increment law.

The reduced formalism has already compressed the ordinary Collatz step substantially. The open second-level classification is now precisely the classification of `ω_+`.

## 11.3. Distribution and Dynamical Role of `3`-gain

Section 9 proved that the parity of `s` controls whether the next odd seed gains a factor of `3`. In that sense, the immediate mechanism of `3`-gain is already understood.

What remains open is the broader dynamical role of repeated `3`-gain events inside the reduced system.

Questions here include:

* How frequently do `3`-gain events occur along reduced trajectories?
* Can the occurrence of `3`-gain be predicted efficiently from bounded residue data?
* To what extent does repeated `3`-gain influence long-term movement through the reduced state space?
* Do repeated `3`-gain patterns explain any of the visible clustering, locking, or average-drift effects seen empirically?

The local trigger is now explicit; the unresolved issue is the global arithmetic and dynamical significance of that trigger. The first question also has a predicted answer: under the equidistribution heuristic the `3`-gain rate is exactly `1/3`, matched empirically to three decimal places (`11.8.4.4`); what remains open is its rigorous derivation along orbits.

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

The first question is answered, and the answer calibrates the others. Off the lifting branch, `ω (mod 8)` and the parity of `d` determine `s` outright (`11.8.1.3.1`) — a bounded residue system in the strongest sense. On the lifting branch no fixed modulus suffices: the parity of `s` is governed by the anchor displacement `v_2(d - M(ω))` (`11.8.5.6.2`), so any finite-state shadow there is a truncation of the anchor digits, exact to its depth and silent beyond it. This is also a sharp answer to the last question: the full `2`-adic complexity reappears exactly at the anchor, and nowhere earlier.

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

