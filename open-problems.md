---
status: open / calibrated
scope: monolith sections 11-11.7 (section 10 was absorbed into index.md); 11.8 added post-monolith (citation-debt record); 11.9 added post-monolith (per-letter window height laws, itinerary.md 14.15.9)
updated: 2026-07-23
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

The local trigger is now explicit; the unresolved issue is the global arithmetic and dynamical significance of that trigger. The first question also has a predicted answer: under the equidistribution heuristic the `3`-gain rate is exactly `1/3`, matched empirically to three decimal places (`11.8.4.4`); under AEH it is a conditional theorem (aeh.md `13.3.2`), and what remains open is its unconditional derivation along orbits.

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

**Calibration note.** One such normal form now exists: the door coordinate (reverse.md `14.14`) — the live door `y` of a reduced edge, a single integer determining the edge, with its own total presentation `G` of the reduced dynamics (semiconjugate to `F`). The question is thereby reframed — which coordinate is most informative for which purpose — rather than open as posed.

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

**Calibration note.** Closed on the mirror front: reverse.md `14.1` gives the complete predecessor characterization (which states reach a given exit, with the exact branching law), and the unique-predecessor lemma (itinerary.md `14.15.4`) pins the letter-prescribed backward predecessor as unique. The classical predecessor-tree viewpoint translates through the same apparatus (reverse.md `14.4`–`14.6`, the density program).

## 11.6. Finite-State Shadows and Residue Control

The empirical observations suggest that residue data may organize substantial portions of the visible reduced dynamics. This raises the question of whether some part of the system admits a meaningful finite-state shadow.

Possible formulations include:

* Is there a bounded residue system that predicts the parity of `s` in large families?
* Can one isolate a finite collection of residue variables that explains most observed `3`-gain behavior?
* Is there a finite-state approximation that predicts the coarse direction of the reduced transition, even when it does not predict the exact next state?
* Does the full arithmetic complexity of the system inevitably reappear once deeper `2`-adic data are tracked?

The first question is answered, and the answer calibrates the others. Off the lifting branch, `ω (mod 8)` and the parity of `d` determine `s` outright (`11.8.1.3.1`) — a bounded residue system in the strongest sense. On the lifting branch no fixed modulus suffices: the parity of `s` is governed by the anchor displacement `v_2(d - M(ω))` (`11.8.5.6.2`), so any finite-state shadow there is a truncation of the anchor digits, exact to its depth and silent beyond it. This is also a sharp answer to the last question: the full `2`-adic complexity reappears exactly at the anchor, and nowhere earlier.

The strongest possible outcome would be a finite residue mechanism that controls large regions of the reduced state space. Even a weaker coarse-state model would already be significant.

**Calibration (2026-07-16, itinerary.md 14.15.2).** For the door/exit seam's own stratum word — the sequence `(m_i,r_i)` that stage4.md `11.8.7.3.1`'s finite-state remark leaves unresolved "at unbounded depth" — the question above is now answered sharply and negatively at every *finite* depth, not merely left open at the infinite one: the itinerary language is proved to be the **full shift** on `{(m,r):m,r≥1}` (itinerary.md `14.15.1`–`14.15.2`), meaning every finite word is realized and no finite collection of forbidden transitions exists to find. So no finite-state approximation of any kind — bounded residue system, coarse-direction predictor, or otherwise — can organize the stratum word beyond what is already known (`11.8.1.3.1`'s bounded system off the lifting branch); the search is closed by proof, not left for further testing.

## 11.7. Relationship to Classical Collatz Formulations

The reduced formalism reorganizes the ordinary Collatz dynamics by compressing deterministic block structure and then quotienting by internal representative families. An important long-term question is how this framework relates to more classical odd-to-odd or accelerated Collatz maps.

In particular:

* Does the reduced map `F` recover known structures in a disguised form?
* Does the quotient by representative families reveal genuinely new organization not visible in the standard odd map?
* Can predecessor-tree viewpoints from classical Collatz analysis be translated into the language of fixed-exit families?
* Can existing results about valuations, residue graphs, or accelerated dynamics be reinterpreted more cleanly inside this reduced setting?

This comparison matters for two reasons. First, it may show that some parts of the reduced formalism are already latent in classical formulations. Second, it may clarify which features of the present framework are genuinely new and therefore deserve further study.

One concrete point of contact is now established (`11.8.3.11`): the valuation `s` on the lifting branch is a linear form in two `2`-adic logarithms, and the effective theory that bounds it — `p`-adic Baker theory together with lattice-reduction methods — is the same machinery underlying the known lower bounds on nontrivial Collatz cycle lengths (Steiner; Simons–de Weger). The reduced formalism and the classical cycle analyses therefore terminate on common arithmetic ground, which calibrates both the novelty and the expected difficulty of the remaining questions.

A second contact point is established on the mirror front: itinerary.md `14.15.1` identifies the itinerary coding of the door/exit seam as the classical Terras/Everett/Lagarias parity-vector coding, read in door coordinates.

## 11.8. Citation and constant debt: discharged

Housekeeping, not a new mathematical question layer. No live `#TODO` marker remains in the wiki (`sources/` excluded, immutable per AGENTS.md): the debt indexed here after the bridge-perimeter stress test (bridge.md 16.4.4) is fully discharged, and every citation is now written in place at its use site rather than deferred. This section is retained as the record of what the debt was and how it closed.

**Citations pinned in place** (bibliography in publication.md; now cited inline at each location):

* stage1-synthesis.md 11.8.3.11 — `p`-adic Baker theory: K. Yu; Bugeaud–Laurent (1996).
* stage1-synthesis.md 11.8.3.11 (remark after `11.8.3.11.2`) — Steiner (1977); Simons–de Weger (2005).
* cycles.md 12.2.3 — Steiner, *A theorem on the Syracuse problem* (1977).
* cycles.md 12.6.3 — Barina, verification frontier, `n < 2^71` (2025).
* cycles.md 12.7.3 — Hercher, `m <= 91` (arXiv:2201.00406); confirms the wiki's own crossover threshold "`p > 91`" was already correctly calibrated.

**Resolved** — all three items from the bridge-perimeter stress test (bridge.md 16.4.4) are closed:

* **The effective irrationality measure for `log 3 / log 2`** — cycles.md 12.5.3 and 12.7.5 now cite and use G. Rhin's explicit bound directly (via Simons–de Weger 2005, Lemma 12), with the numeric contradiction checked by computation.
* **The spike-height exponent** — stage1-synthesis.md 11.8.3.11 now cites and uses Bugeaud–Laurent's Corollaire 2 (the `g=1` case, automatic for `p=2`) directly, giving `C(ω) = 208·log9·logω` and confirming the exponent is exactly `2`, with a numeric sanity check.
* **cycles.md 12.8.2's explicit `n_0(p)`** — the `γ ↔ Λ` conversion is a full proof: `Λ < exp(p - γ·log2)` unconditionally (via `q=2^(K-γ)`, `log(1+x)<x`, and the crude-but-unconditional `Λ<p` from Corollary 12.1.2), combined with Rhin's bound and Theorem 12.8.1 gives an explicit equation defining `n_0(p)`, solved numerically for a table of periods (`n_0(91) ~ 3*10^21`, etc.) and checked that the contradiction persists for all larger `n` (no reversal). See cycles.md 12.8.2 for the full derivation.

Nothing substantive remains open from this stress test. What's left is the ordinary residue of any pinned bound: whether a sharper published measure (post-1987 Rhin improvements, or a p-adic analogue) would improve the constants — not attempted, since the corollaries already close what they need to close.

The chase itself is discharged; the citations are pinned inline at their use sites (stage1-synthesis.md 11.8.3.11; cycles.md 12.5.3, 12.7.5, 12.8.2), and the derivations live there. One methodological guard retained: Rhin's `μ(γ) < 8.616` irrationality measure for fixed `γ ∈ Q log 2 + Q log 3` is the wrong tool for the two-integer-variable linear form the cycle corollaries need — the right statement is the Proposition on p. 160 of the same 1987 paper, applied as in Simons–de Weger (2005) Lemma 12 (pinned at cycles.md 12.5.3); recorded so the mistake isn't repeated.

## 11.9. Per-letter (period-cutting) window height laws

itinerary.md `14.15.9`'s whole-period height laws hold only for windows aligned to a full period (`(np, np)` in letters). A window that cuts a period partway anchors its partial past at a *rotated* fixed point rather than at the word's own `y^*`, and no height law at such windows is established.

**What is already known.** The *class* characterization appears to extend past whole-period boundaries with no new machinery: the forward follower class equals the `2`-adic class of `y^*` at every prefix length `L` (the contraction induction along rotations never uses `p | L`), and the backward admissibility class at every depth `ℓ` equals `{qz ≡ a (mod 3^{M_ℓ})}`, because the depth-`ℓ` deepest-first prefix map carries the rotated fixed point `y^*_{(p−ℓ) mod p}` to `y^*`. What rotates mid-window is only the deepest-door analysis: the deepest door of a depth-`ℓ` chain sits near the rotated fixed point `y^*_{(p−ℓ) mod p}`, so a per-letter mod-3 door law would run through that rotation's own numerator `a_{(p−ℓ) mod p}` and residue `ε_{(p−ℓ) mod p}` (itinerary.md `14.15.9.2`) rather than through `a` and `ε`.

**Open question.** Do per-letter window height laws follow from the existing whole-period apparatus (itinerary.md `14.15.9.5`–`14.15.9.12`) plus the rotation lemma's `p`-tuple of numerators, applied at the rotation matching each cut depth? Closure would look like an exact law for `H^σ_{p,q}(W)` at arbitrary `(p,q)`, not just `(np,np)`, reducing to `14.15.9`'s results when `p = q = np`.

