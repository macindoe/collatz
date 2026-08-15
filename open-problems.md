---
status: open / calibrated
scope: monolith sections 11-11.7 (section 10 was absorbed into index.md); 11.8 added post-monolith (citation-debt record); 11.10 added post-monolith (per-letter window height laws, itinerary.md 14.15.9; recorded as 11.9 in pre-2026-07-23 briefs); 11.11 added post-monolith (what AEH's budget clause supplies, aeh.md 13.2.3); 11.12 added post-monolith (which door-letter indexing the record standardizes on, aeh.md 13.2 and 13.6.3(i))
updated: 2026-08-03
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

**Calibration note (2026-08-02, aeh.md `13.2.4`).** The first question is now closed unconditionally inside the digit budget: for every horizon rate `θ < 1/4` block per bit, the `3`-gain rate `1/3` and the frequency ledger hold — at every block length, as marginals of `π_{k,D}` — for all but a vanishing density of starting values of each size, by the classical cylinder count (aeh.md `13.2.4`(d)–(e), `13.2.4.1`), with the exceptional set of natural density zero in the integers at dyadic-shell scale (`13.2.5`). The rate is exactly `0` at `θ = 1/4`, so what remains open is the range past the budget, where the statement is AEH-conditional as above, and the derivation along an individual orbit, which no density statement supplies (aeh.md `13.3.3`).

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

## 11.10. Per-letter (period-cutting) window height laws

itinerary.md `14.15.9`'s whole-period height laws hold only for windows aligned to a full period (`(np, np)` in letters). A window that cuts a period partway anchors its partial past at a *rotated* fixed point rather than at the word's own `y^*`, and no height law at such windows is established.

**What is already known.** The *class* characterization appears to extend past whole-period boundaries with no new machinery: the forward follower class equals the `2`-adic class of `y^*` at every prefix length `L` (the contraction induction along rotations never uses `p | L`), and the backward admissibility class at every depth `ℓ` equals `{qz ≡ a (mod 3^{M_ℓ})}`, because the depth-`ℓ` deepest-first prefix map carries the rotated fixed point `y^*_{(p−ℓ) mod p}` to `y^*`. What rotates mid-window is only the deepest-door analysis: the deepest door of a depth-`ℓ` chain sits near the rotated fixed point `y^*_{(p−ℓ) mod p}`, so a per-letter mod-3 door law would run through that rotation's own numerator `a_{(p−ℓ) mod p}` and residue `ε_{(p−ℓ) mod p}` (itinerary.md `14.15.9.2`) rather than through `a` and `ε`.

**Open question.** Do per-letter window height laws follow from the existing whole-period apparatus (itinerary.md `14.15.9.5`–`14.15.9.12`) plus the rotation lemma's `p`-tuple of numerators, applied at the rotation matching each cut depth? Closure would look like an exact law for `H^σ_{p,q}(W)` (itinerary.md Definition `14.15.6.8`) at arbitrary `(p,q)`, not just `(np,np)`, reducing to `14.15.9`'s results when `p = q = np`.

## 11.11. What AEH's budget clause supplies past the digit budget

aeh.md `13.2.3` records what the hypothesis says about its own exponent budget, and `13.2.4`(g) what the cylinder count proves inside it; neither is restated here. On the reading those two fix, the Cesàro statement `T_N^(−1)Σ_(n<T_N)(m_n + r_n) → 4` is a theorem inside the digit budget and does not follow past it. Two questions are left open by that reading. A candidate argument for both is drafted at `briefs/v3r4-clock-findings.md` §2 and §7.8; neither is claimed by any page, and `13.3.2` stands as written until the first closes.

**Open question 1: may `τ` be taken down to `4θ`, and what does the in-budget prefix carry if it may?** `13.2.1` is quantified "for every admissible `(τ, θ)`". Fix `θ` and put `n* = min{n ≤ T_N : S_n ≥ Λ_N}`, so the in-budget prefix is blocks `0, …, n*−1`. The drafted argument bounds `T_N^(−1)Σ_(n<n*−1)(m_n + s_n)` above by `Λ_N/T_N → τ/θ` (block `n*−1` is tallied) and below by `4` (Fatou on the letter marginals of `13.2.2` at `L = 1`), then takes `τ_k = θ(4 + 1/k)` — admissible for every large `k` — and diagonalizes in `k` to pin the prefix mean at `4`, hence `Σm/T_N → 2`, `Σs/T_N → 2` and a block drift of `−β` along the prefix. The hinge is the quantifier: whether the hypothesis is to be read as asserted at pairs with `τ` arbitrarily close to `4θ`, or only with slack bounded away from it. **Closure is checkable in either direction:** a reason inside the record to prefer a fixed slack (which deletes the prefix statement outright), or an argument that the quantifier is as written *together with* the prefix statement written out at that quantifier, including the altitude step's per-step `O(1/x_exit)` error summed inside the budget. It is also unmeasured: the calibration campaign reports pooled full-horizon frequencies, and no run reports the distribution across orbits of `S_(n*−1)/T_N` at `τ/θ` near `4`, which is the quantity the statement is about (aeh.md `13.4`, `13.5`).

**Open question 2: does `13.3.2`'s first reason need rescoping, and if so to what?** `13.3.2` declines a drift consequence for two independent reasons, the first being that convergence of window-state frequencies at each fixed `k` gives `liminf` bounds but no `limsup` on the unbounded `m_+`. That is correct at a fixed admissible pair. **If** question 1 closes affirmatively it is incomplete over the admissible family, because the missing `limsup` would then be supplied along the prefix by the *budget* clause rather than by the frequency clause. **Closure:** either question 1 closes negatively and `13.3.2`'s first reason is already exactly right, or it closes affirmatively and the first reason is restated as a fixed-pair statement — with `13.3.2`'s second reason becoming the load-bearing one, which it can carry, since admissibility caps `τ` at `4.8188…`, itself Inselmann's horizon, so any such prefix lies by construction inside a two-sided envelope that is unconditional and uniform in the time. Nothing about the second reason, or about `13.3.2`'s conclusion, is in question either way.

## 11.12. Which door-letter indexing the record standardizes on

Three indexings of the door letter are in play across aeh.md `13.2` and `13.6.3`(i), and no page fixes one. Write `y_i = G^i(x)` for the doors of an odd start `x`, so `y_0 = x` and `y_(i+1) = x_exit(i)`. **(A)** letter `i = stratum(y_i)` — the letter word of `x` itself, and the word itinerary.md Theorem `14.15.1.5` is stated about. **(B)** letter `i = stratum(y_(i+1)) = stratum(x_exit(i)) = (m_(+,i), s_(i+1))` — what `13.2.1`, `13.2.4` and `13.6.3`(i)(a) define, and what reverse.md `14.14.6`'s seam identification supplies. **(C)** letter `i = (m_i, s_(i+1))`, pairing block `i`'s own `m` with block `i+1`'s `s` — not a door stratum, defined on no page, but the pairing `13.2.3`'s clause "`r_i = s_(i+1)`" reads as on its own. The budget sum `Σ_(i<n)(m_i + s_i)` of `13.2.1` and `13.2.3` runs over (A)'s word — `(m_i, s_i) = stratum(y_i)` exactly, which is what makes `x_exit(n−1) = T_1^(S_n)(x)` hold — so its `m_i` is `13.2.4`'s `m_(i−1)`, and the one symbol carries two meanings inside `13.2.3` alone. The measurements are at `briefs/v3r4-fix-findings.md` §3.3 and §8, and `experiments/aeh_word_shift.py`.

The choice is not cosmetic. Under (A) the budget count and the letter word's total exponent are the *same* number, `13.2.3`'s gap is `0`, and `13.2.4`(a) is `14.15.1.5` with nothing to correct. Under (B), which is what `13.2.4` in fact defines, the word (a) speaks of is the letter word of `x` with its *first* letter deleted, whose cylinder classes need that letter's own exponent too — so (a)'s tail term has to run over `n + 1` letters, and `13.2.4`(a) and (c) are written that way: `TV(Law(ℓ_0, …, ℓ_(n−1)), B^(⊗n)) ≤ 2^(J+2)/N + P_B(S_(n+1) ≥ J)`, and an altitude line carrying `stratum(x)` explicitly. What that letter is worth is the size of the difference the convention makes, and is on record: at `N = 2^b` and `J = b`, where (a)'s window term is `0`, the exact total variation of the one-letter law over every odd start of `[2^b, 2^(b+1))` is `2279/2^20` at `b = 16`, `685/2^21` at `b = 20` and `2163/2^26` at `b = 24`, against `n`-letter terms `1/2^11`, `5/2^17` and `3/2^20` — factors `4.45`, `8.56` and `11.27`, growing with `b` — and inside the `(n+1)`-letter terms `9/2^9`, `145/2^16` and `1/2^12` in every one of `18` measured cells; the same quantities on (A)'s word are `743/2^21` and `227/2^23`, inside the `n`-letter term throughout. No *conclusion* of `13.2.4` is at stake either way: (b)'s identity is general in `n`, `(g)`'s rate `I(θ, τ)` has the same value at `n = T_N + 1` as at `T_N`, and (d)–(f), Corollary `13.2.4.1` and Theorem `13.6.4` read identically; `13.2.4`(g)'s offset clause was written to hold under all three readings and does.

**Open question: which indexing should the record carry, and what has to move with it?** Standardizing on **(A)** makes (a) exactly `14.15.1.5`, makes (c)'s altitude line exact from `y_0 = x` with no leading letter to subtract, and collapses both `13.2.3`'s gap clause and `13.2.4`(g)'s offset parenthetical to nothing; its cost is that `13.2.1`'s letter, `13.6.3`(i)(a)'s letter-per-block identification and Corollary `13.2.4.1`'s "`13.2.1`'s tallied word is the letter word of `13.2.4`(d)" are each stated in (B) and would each have to be restated, together with the seam sentence at reverse.md `14.14.6` they rest on. Keeping **(B)** costs the extra letter now carried in `13.2.4`(a)'s tail term and `13.2.4`(c)'s altitude line, and leaves every other statement where it stands; that price is paid, so what is open here is the convention and not a defect. **(C)** is not a candidate: it is not a door stratum and no page defines it. **Closure is checkable:** the chosen convention written into `13.2.1`, `13.2.3`, `13.2.4` and `13.6.3`(i) with one symbol per quantity, and every statement citing them re-read against it — in particular `13.2.4`(a)'s tail term, `13.2.3`'s gap clause, and `13.2.4`(g)'s offset clause, which no longer needs to hedge across readings once one is fixed.

