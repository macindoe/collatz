---
status: closed (3-gain law proved on both lifting components); fiber-versus-orbit bridge OPEN
scope: monolith 11.8.5
updated: 2026-07-22
source: sources/drafts/collatz_reduction_rewrite_v078.md (last monolith)
---

> **Current state.** Stage 2: the exact 3-gain law, the orbit anchor M(ω) = N(ω^2), the unified depth-side law s = 2 + v_2(d - M(ω)), and the fiber-versus-orbit gap (11.8.5.6) — the program's terminal open problem, equivalent to Stage 4. Sub-question 1 of the bridge question (low-order law for ΔM) is now closed: Theorem 11.8.7.3.1, stage4.md.

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

**Proof.** By Proposition `11.8.1.6.2`, `3^d ω = 9^n ω̃` with `ω̃ = 3ω ≡ 1 (mod 8)`, so

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

Theorem `11.8.5.2.1` and Corollary `11.8.5.2.2` together cover both components of the lifting branch as defined in `11.8.1.7.2`: odd `ω ≡ 1 (mod 8)` with `d` even, and odd `ω ≡ 3 (mod 8)` with `d` odd. The remaining residue-parity classes of Proposition `11.8.1.3.1` — namely `(ω ≡ 1, d odd)`, `(ω ≡ 5, any d)`, `(ω ≡ 7, any d)`, and `(ω ≡ 3, d even)` — have `s` pinned at `1` or `2` at the first layer; for these, the parity of `s`, and hence `3`-gain, is decided outright by the mod `8` classification, and no anchor machinery is needed.

What the theorem does not close is the arithmetic of the anchor itself. By Theorem `11.8.3.6.6`, the anchors in question are the quantities

```text
N(ω) = -log ω / log 9,   N(3ω) = -log(3ω) / log 9,
```

so the remaining open question is precisely: describe the `2`-adic digit patterns of logarithms of small integers. This calibrates expectations. Digit questions about `p`-adic logarithms of integers belong to transcendence theory, are expected to be genuinely hard, and the digits themselves are expected to behave pseudo-randomly. The effective side of that theory is not empty — `p`-adic Baker theory yields the unconditional polylogarithmic bounds of `11.8.3.11`, which cap spike heights and digit matches — but the finer statistics remain out of reach. The anchor formalism should therefore be valued for the reduction it achieves — the entire `3`-gain pattern of a family is compressed into one classical `2`-adic number, computable to any precision by a convergent series — rather than for the prospect of a closed-form description of that number's digits.

The `3`-gain law is therefore closed as a formal theorem on the entire lifting branch. What remains open on the anchor side is expected to remain open: any further "arithmetic organization" of the digits of `N(ω)` would constitute progress on the digit behavior of `2`-adic logarithms, a problem independent of, and older than, the present program.

#### 11.8.5.6. The fiber-versus-orbit gap: from statics to dynamics

**Status: template.** This subsection poses a question; it proves nothing beyond bookkeeping. It exists because the gap it names is the structural boundary of everything proved so far.

Everything in Stages 1 and 2 fixes `ω` and varies `d`. But the reduced map `F` changes `ω` at every step. Applying the `3`-gain law along an actual orbit `(ω_0, d_0), (ω_1, d_1), ...` therefore requires a fresh anchor at each step, and no result so far relates the anchor of `ω_(t+1)` to the anchor of `ω_t`. Without such a relation, the Stage 1–2 synthesis is a fiber-by-fiber statics of a map whose dynamics move between fibers.

The question is well-posed, and stating it cleanly requires one piece of bookkeeping: an anchor attached to every odd `ω`, not only to `ω ≡ 1 (mod 8)`.

**Definition 11.8.5.6.1 (orbit anchor).** For every odd `ω`, set

```text
M(ω) = N(ω^2) = -2·log ω / log 9   in   Z_2,
```

which is well-defined because `ω^2 ≡ 1 (mod 8)` for every odd `ω`. For `ω ≡ 1 (mod 8)` one has `M(ω) = 2N(ω)`, and for `ω ≡ 3 (mod 8)` one has `M(ω) = 2N(3ω) + 1`, so `M` carries the anchors of both lifting components in a single depth-side coordinate.

**Proposition 11.8.5.6.2 (unified depth-side law).** On both lifting components — `(ω ≡ 1 (mod 8), d even)` and `(ω ≡ 3 (mod 8), d odd)` — the exact valuation law takes the single form

```text
s = v_2(3^d·ω - 1) = 2 + v_2(d - M(ω))      whenever d ≠ M(ω).
```

Moreover the parity of `M(ω)` records the lifting depth-parity: `M(ω)` is even for `ω ≡ ±1 (mod 8)` and odd for `ω ≡ ±3 (mod 8)`, and on the lifting components the lifting depths satisfy `d ≡ M(ω) (mod 2)`.

**Proof.** For `ω ≡ 1 (mod 8)`, `d = 2n`: `v_2(d - M(ω)) = v_2(2n - 2N(ω)) = 1 + v_2(n - N(ω))`, so the right side is `3 + v_2(n - N(ω))`, which is the exact law of `11.8.4.1`. For `ω ≡ 3 (mod 8)`, `d = 2n + 1`: by the homomorphism law, `M(ω) = N(ω^2) = N((3ω)^2) - N(9) = 2N(3ω) + 1`, so `v_2(d - M(ω)) = v_2(2n - 2N(3ω)) = 1 + v_2(n - N(3ω))`, and the right side is `3 + v_2(n - N(3ω))`, which is Corollary `11.8.5.2.2`. The parity statements follow from `v_2(log ω) = v_2(ω^2 - 1) - 1` on each mod-`8` class. (Numerically confirmed across both components and all tested depths.) ∎

**The increment identity.** Because `N` is a homomorphism (Theorem `11.8.3.7.1`), the anchor increment along one reduced step is

```text
ΔM = M(ω_+) - M(ω) = N((ω_+/ω)^2) = -2·log(ω_+/ω) / log 9,
```

and `ω_+` is explicitly determined by the derived quantity `C`:

```text
ω_+ = C / (2^(v_2(C)) · 3^(v_3(C))).
```

So the anchor increment is not a new unknown. It is a deterministic function of the current state's `C` — that is, of exactly the quantity Stage 3 sets out to control. In anchor coordinates, Stage 3 and the fiber-to-orbit bridge are the same problem:

```text
control of C   ⟺   law for the anchor increment ΔM.
```

(With the valuation components of `C` now formal per step — `v_2(C)` by the entry-depth law of `11.8.6.3`, `v_3(C)` by the absorption law of `11.8.6.2` — the unresolved content of both sides of this equivalence is precisely the odd core `ω_+ = C / (2^(v_2 C)·3^(v_3 C))`. The bridge is therefore the terminal open problem of the program at the valuation level.)

**Question 11.8.5.6.3 (anchor increment law; resolved to low order and at bounded depth, stage4.md).** Does `ΔM` admit a usable description in terms of the current state's data — the residue class of `ω`, the valuation `s`, the anchor displacement `d - M(ω)`, or finitely many digits of `M(ω)`?

Three graded sub-questions, in increasing order of ambition:

1. *Low-order law.* Is there an exact law for `ΔM` modulo small powers of `2` — equivalently, for the leading digits of `-2·log(ω_+/ω)/log 9` — in terms of `(ω mod 2^j, s)` for some fixed `j`?
2. *Displacement propagation.* The next `3`-gain decision depends only on `v_2(d_+ - M(ω_+))`. Can this be bounded or determined from `v_2(d - M(ω))` and low-order data, without full knowledge of `ΔM`?
3. *Statistical behavior.* Along typical orbits, do the successive anchors `M(ω_t)` equidistribute in `Z_2` (as fair-coin digit behavior of logarithms would suggest), and does the `3`-gain sequence inherit the corresponding shell-parity statistics?

A positive answer at any of the three levels would convert the Stage 1–2 statics into orbit-level statements. A negative structural answer — for instance, that `ΔM` is as hard as the digits of the logarithms themselves — would locate the difficulty of the full problem precisely at the fiber-to-orbit bridge.

**Status.** Sub-question `1` is answered in the affirmative: `ΔM mod 2^k` obeys an exact law in the state's residues modulo `σ`-graded powers of `2`, with modulus fixed in advance per `(s, m_+)` stratum — Theorem `11.8.7.3.1` (stage4.md), verified independently (`11.8.7.4`). Sub-question `2` is answered in its bounded-depth form: one-step propagation (Theorem `11.8.7.6.1`) decides the next `3`-gain from the window in an error-free trichotomy, undecided only at rate `≈ 2^(-(k+1))`; the digit-budget accounting (`11.8.7.7`) marks this as the complete deterministic content, with the impossibility-of-infinite-horizon reading recorded there as the organizing heuristic. The unbounded-depth residue of the bridge is therefore exactly sub-question `3` for typical orbits (anchor equidistribution, now the precise missing hypothesis) and rigidity for cycles.

**Remark (relation to the trivial cycle).** The fixed point of the reduced dynamics is `(ω, d) = (1, 1)` with `M(1) = 0`, and by the convergence translation (Theorem `9.8.3`) the conjecture is exactly the statement that every orbit drives the pair `(d - M(ω), M(ω))` to `(1, 0)`. The reformulation in anchor coordinates fixes the language in which the increment question above would have to be answered; nothing beyond the translation is claimed.

