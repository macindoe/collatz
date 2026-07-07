---
status: closed (proved + imported bounds); anchor digit statistics exported to classical p-adic analysis
scope: monolith 11.8.1-11.8.4
updated: 2026-07-07
source: sources/drafts/collatz_reduction_rewrite_v078.md (last monolith)
---

> **Current state.** Stage 1: the valuation synthesis. First-layer mod-8 classification, lifting-branch congruences, the 2-adic anchor N(ω) = -log ω / log 9, the exact global law s = 3 + v_2(n - N(ω)), imported p-adic Baker bounds (11.8.3.11), the frequency/size ledgers (11.8.4.4), and the status snapshot (11.8.4.5).

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

#### 11.8.1.2. First formal output of Stage 1

The first structural split in the valuation

```text
s = v_2(3^d ω - 1)
```

is controlled by the residue class of `ω (mod 8)`. This does not determine the full value of `s`, but it does determine the first valuation layer and thereby separates the genuinely lifting branch from the non-lifting branches.

#### 11.8.1.3. First-layer residue classification modulo `8`

**Proposition 11.8.1.3.1 (first-layer mod `8` classification).** Let `ω` be odd, and define

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

#### 11.8.1.4. Worked examples and discovery path

The historical route by which this first-layer split and the later lifting-branch picture were discovered is now moved to Appendix A.

In particular, Appendix A records:

* the calibration families `ω = 1, 5, 7`,
* the anchor-discovery example `ω = 17`,
* and the clean tower example `ω = 25`.

Those examples are useful for intuition, but they are no longer needed in the main formal line.

#### 11.8.1.5. Transition to the lifting branch

By Proposition `11.8.1.3.1`, the first-layer congruence forces

```text
v_2(3^d ω - 1) >= 3
```

in exactly two of the eight residue-parity classes:

```text
ω ≡ 1 (mod 8),   d even    (the even lifting component),
ω ≡ 3 (mod 8),   d odd     (the odd lifting component).
```

Both components are nonempty in the valid reduced setting `3 ∤ ω`: the even component contains, for example, `(ω, d) = (17, 2)`, and the odd component contains `(ω, d) = (11, 1)`, where `A = 3·11 - 1 = 32` and `s = 5`. Earlier drafts developed the lifting machinery only on the even component; the odd component is equally real and must be carried through the synthesis. It will be handled by an exact reduction to the even-component formalism (Proposition `11.8.1.6.2` below), so no new machinery is required — but the scope statements must include it.

So once Stage 1 reaches the lifting regime, the natural next question is no longer merely whether deeper lifting occurs, but how it is generated arithmetically.

The key point is that on both lifting components the valuation problem becomes a congruence problem in the exponent variable, in the same base `9`.

#### 11.8.1.6. Lifting on the even branch as a congruence problem in base `9`

**Proposition 11.8.1.6.1.** Let `ω` be odd and let `d = 2n` be even. For any integer `k >= 1`,

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

**Proposition 11.8.1.6.2 (odd branch via the companion parameter).** Let `ω` be odd and let `d = 2n + 1` be odd. Define the companion parameter

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

so the companion parameter lies in exactly the residue class in which the even-branch congruence formalism of Proposition `11.8.1.6.1` and the later anchor machinery operate.

**Proof.** Since `d = 2n + 1`,

```text
3^d ω = 3^(2n+1) ω = 9^n · (3ω) = 9^n · ω̃.
```

The chain of equivalences is then identical to that of Proposition `11.8.1.6.1` with `ω` replaced by `ω̃`: `v_2(9^n ω̃ - 1) >= k` if and only if `9^n ω̃ ≡ 1 (mod 2^k)`, and since `ω̃` is odd it is invertible modulo `2^k`, giving `9^n ≡ ω̃^(-1) (mod 2^k)`. Finally, if `ω ≡ 3 (mod 8)` then `3ω ≡ 9 ≡ 1 (mod 8)`. ∎

**Remark (validity of the companion substitution).** The companion parameter `ω̃ = 3ω` is divisible by `3`, so `(ω̃, 2n)` is not itself a valid reduced state. This is harmless: `ω̃` enters only as an arithmetic parameter of the congruence problem `9^n ≡ ω̃^(-1) (mod 2^k)`, and every result of the Stage 1 synthesis in `11.8.3` uses only that the parameter is odd and congruent to `1 (mod 8)` — the hypothesis `3 ∤ ω` is never invoked there. The dynamical conclusions are then read back on the genuine reduced state `(ω, d)` through the identity `v_2(3^d ω - 1) = v_2(9^n ω̃ - 1)`.

**Worked check.** Take `(ω, d) = (11, 1)`, so `n = 0` and `ω̃ = 33`. Directly, `A = 3·11 - 1 = 32`, so `s = 5`. On the companion side, `33^(-1) ≡ 33 (mod 64)` and `9^4 = 6561 ≡ 33 (mod 64)`, so the anchor satisfies `N(33) ≡ 4 (mod 8)` and

```text
s = 3 + v_2(0 - N(33)) = 3 + 2 = 5,
```

in agreement (using the anchor-displacement law of Theorem `11.8.3.9.1`, stated later, applied to `ω̃ = 33`).

#### 11.8.1.7. Congruence towers on the lifting branch

Proposition `11.8.1.6.1` suggests the following definitions.

**Definition 11.8.1.7.1 (raw congruence level).** Let `ω` be odd, and let `k >= 4`. The level-`k` congruence set of `ω` is

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

**Definition 11.8.1.7.2 (lifting branch).** The lifting branch is the locus on which the first-layer mod `8` classification forces

```text
v_2(3^d ω - 1) >= 3.
```

By Proposition `11.8.1.3.1`, in the valid reduced setting with `3 ∤ ω` it has exactly two components:

```text
even component:  ω ≡ 1 (mod 8),   d = 2n,
odd component:   ω ≡ 3 (mod 8),   d = 2n + 1.
```

On the even component the relevant congruence parameter is `ω` itself. On the odd component, by Proposition `11.8.1.6.2`, the relevant congruence parameter is the companion `ω̃ = 3ω ≡ 1 (mod 8)`, and the level-`k` congruence sets are `T_k(ω̃)` in the exponent variable `n`, with depth-side classes `d = 2n + 1` rather than `d = 2n`. All tower definitions below apply verbatim on the odd component after this substitution.

**Definition 11.8.1.7.3 (distinguished congruence tower).** Suppose that for a fixed `ω` there exists a compatible nested choice of residue classes

```text
n_k (mod 2^(k-3)) in T_k(ω)
```

such that each class reduces to the preceding one as `k` decreases. Then this nested sequence is called a distinguished congruence tower for `ω`.

The corresponding distinguished depth classes are

```text
d_k = 2 n_k.
```

When such a compatible sequence exists, the visible lifting residues in `d` are interpreted as finite truncations of that tower.

**Remark 11.8.1.7.4 (historical tower-type labels — dissolved).** Earlier drafts introduced here a provisional dichotomy of distinguished towers into "regular" (`ω = 25, 49, 73`) and "irregular" (`ω = 17, 41, 65, 89`) visible geometries, together with a conjectured mod-`3` classifier. Both are dead, and no definition is made. The visible refinement of a tower is determined digit-by-digit by the anchor `N(ω)` of `11.8.3.6` — the level-`k` class changes exactly when digit `k - 3` of `N(ω)` is `1` — and the historical labels correspond to nothing more than high versus low digit density in the observation window: a continuous statistic, not two classes. The mod-`3` classifier was refuted outright by a computational audit. The closing note of `11.8.4.3` records the resolution; Appendix `A.4.6` preserves the historical observation and the audit data. Where Appendix A uses the words regular and irregular, they are period labels for these seven calibration families only.

These definitions deliberately separate three issues:

1. the exact congruence reformulation of the valuation problem,
2. the existence of compatible nested solution classes,
3. the empirical geometry of the resulting tower.

Only the first of these is fully formal at this stage. The later synthesis will show that much of the remaining structure can also be formalized.

The worked examples that historically revealed these steps are now collected in Appendix A. The next subsection proceeds directly to the pre-synthesis tower map.

### 11.8.2. Pre-synthesis tower map

This subsection maps the visible tower geometry at the level needed before `11.8.3` begins: the formal mechanism is already in hand; what remains is to record the tower archetypes and mark the boundary between the exact and the empirical.

#### 11.8.2.1. Tower archetypes visible before synthesis

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

This taxonomy is organizational: it tells the reader what the later synthesis must — and does — explain. The dense/sparse contrast in the middle two rows is a continuous digit-density statistic of the anchor, not a structural dichotomy (Remark `11.8.1.7.4`).

#### 11.8.2.2. What is empirical in the tower map

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

(A finer arithmetic classifier of tower geometry was once conjectured at this point in the program; it has since been refuted, and the underlying dichotomy dissolved — see Remark `11.8.1.7.4`. It is not carried forward in this map.)

So this subsection deliberately stops short of synthesis. It records the visible map, but it does not yet identify which parts of that map are exhausted by the congruence branch and which parts require a new local law. That is exactly the role of `11.8.3`.

#### 11.8.2.3. Transition to the Stage 1 synthesis

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

**Convention (transfer to the odd component).** Throughout `11.8.3`, all statements are written for a parameter `ω` that is odd and congruent to `1 (mod 8)`, with even depth `d = 2n`. By Proposition `11.8.1.6.2`, every such statement applies verbatim to the odd lifting component `ω ≡ 3 (mod 8)`, `d = 2n + 1`, upon substituting the companion parameter `ω̃ = 3ω` for `ω` and reading `n` from `d = 2n + 1`; the identity `v_2(3^d ω - 1) = v_2(9^n ω̃ - 1)` transports every valuation conclusion back to the genuine reduced state. No result in this subsection uses `3 ∤ ω`, so the divisibility of `ω̃` by `3` is immaterial here. To avoid doubling every statement, the transfer is left implicit until the dynamical conversion in `11.8.5`, where the odd-component form is recorded explicitly.

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

Finally, by Proposition `11.8.1.6.1`, on the even branch `d = 2n` the congruence condition is equivalent to

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

By the `ω = 1` valuation law of Proposition `9.4.1` applied to `9^r - 1 = 3^(2r) - 1`,
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

Because `Δ` is even, Proposition `9.4.1` gives

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

each agreeing with the congruence-defined classes `n_k`; note `N(17) ≡ 6 (mod 8)` matches the first visible lifting class `d ≡ 12 (mod 16)` of the family `ω = 17`, and `N(33) ≡ 4 (mod 8)` matches the companion-anchor computation of Proposition `11.8.1.6.2`.

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

**Proof.** On the even component `d = 2n` this is the imported bound directly. On the odd component `d = 2n + 1`, Proposition `11.8.1.6.2` gives `s = v_2(9^n·(3ω) - 1)`, and the imported bound applies to the companion parameter `3ω`. ∎

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

and, via the companion parameter `ω̃ = 3ω` of Proposition `11.8.1.6.2`, equally the odd component

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

So even if the lifting-branch valuation picture is largely understood, that alone does not yet classify the next reduced step. Of the required conversions, two are now complete per reduced step: `3`-gain (Stage 2, `11.8.5`) and the depth evolution `d_+ = v_2(C) - s + v_3(C)` (Stage 3, closed on all residue classes by the target-shift entry-depth law of `11.8.6.3` together with the absorption law of `11.8.6.2`). What remains is:

* the refined odd core `ω_+` — equivalently, by `11.8.5.6`, the anchor increment.

This is why the next stages of Route A remain dynamical rather than purely valuation-theoretic. The required passage is:

```text
anchor-displacement valuation control
    -> parity of s and 3-gain
    -> control of C
    -> laws for d_+
    -> only then a sharper description of ω_+.
```

The structural form of this gap deserves its name: the Stage 1–2 results are statements on fibers of fixed `ω`, while the dynamics moves between fibers. This fiber-versus-orbit gap is posed precisely in `11.8.5.6`, where it is shown to coincide, in anchor coordinates, with the control of `C`.

**Closing note: two former entries of this ledger.** Earlier drafts carried two further open questions here. Both are closed. The globalization of the off-spike halo law is resolved positively: the anchor-displacement law `s = 3 + v_2(n - N(ω))` is globally exact (`11.8.4.1`), so the once-open possibility of new structure beyond the proved local range is excluded. The classification of tower types is resolved by dissolution: there are no types, only the digit density of the anchor, and the once-conjectured mod-`3` classifier is refuted by computation (Remark `11.8.1.7.4`; historical record and audit data in Appendix `A.4.6`).

#### 11.8.4.4. Frequency and size accounting: what Route A can and cannot deliver

The synthesis so far is exact but unweighted: it says nothing about how often orbits meet the lifting branch, and the reduced coordinates deliberately suppress the magnitude of `x`. This subsection supplies both ledgers and states plainly what they imply about the scope of Route A.

**Frequency ledger.** Combining the first-layer classification (Proposition `11.8.1.3.1`) with the exact global law, under the equidistribution heuristic — residue classes of `ω (mod 8)` and depth parities occur uniformly along orbits, and `d - M(ω)` has geometric `2`-adic valuation, i.e. anchor-digit equidistribution — the per-block distribution of `s` is

```text
P(s = 1) = 1/2,
P(s = 2) = 1/4,
P(s = k) = 2^(-k)   for k >= 3,
```

hence `E[s] = 2`, and (by Lemma `9.3.1`) the `3`-gain rate is

```text
P(s even) = 1/4 + 2^(-4) + 2^(-6) + ... = 1/3.
```

Three remarks on the status of this ledger. First, it is a heuristic, but its only nontrivial ingredient — the geometric tail on the lifting branch — is exactly the anchor-digit pseudo-randomness for which Appendix `A.4.6` provides direct evidence and `11.8.3.11` provides the unconditional worst-case cap. Second, it is empirically sharp: over `48,000` block steps of orbits launched from random seeds near `10^18`, the observed frequencies match the table to three decimal places, and the observed `3`-gain rate is `0.3338`. Third, it locates the deep-cascade machinery correctly: generic block steps are shallow (`s <= 2` with probability `3/4`), and Stages 1–2 govern an exceptional set with geometric tail — the machinery is a theory of the rare events, not of the typical step.

**Size ledger.** The reduced coordinates hide `|x|`; it is restored as follows. A block entry `x = 2^m·u - 1` has exit `x_exit = (3^m·u - 1)/2^s` (the `3`-adic content `a` of `u` cancels between `d = m + a` and `u = 3^a ω`), so

```text
log x_exit - log x = m·log 3 - (m + s)·log 2 + O(1/x).
```

Each block consists of `m` odd Collatz steps and `m + s` halvings. With the heuristic values `E[m] = 2` and `E[s] = 2`, the expected log-size increment is

```text
E[Δ log x] = 2·log 3 - 4·log 2 = log(9/16) < 0
```

per block, equivalently `log 3 - 2·log 2 = log(3/4)` per odd step — precisely the classical drift heuristic. The reduced formalism is therefore consistent with the standard drift picture and adds arithmetic structure to it; it does not replace it.

**What the ledgers imply for Route A.** The size ledger shows where growth lives: a block increases `log x` exactly when `s < m·(log 3 / log 2 - 1) ≈ 0.585·m`, that is, in long blocks with shallow exits. Deep cascades are the strongly contracting events, and the anchor machinery is the exact theory of when they occur (close `2`-adic approaches of the depth to the orbit anchor `M(ω)`). Route A can deliver: the exact structure of the exceptional set, the exact `3`-gain trigger and its predicted rate, and a well-posed fiber-to-orbit bridge (`11.8.5.6`) whose resolution would make the frequency ledger rigorous along orbits. Route A cannot deliver, even on full success of Stages 3–4: convergence itself, in the precise internal sense of Theorem `9.8.3`. A classified transition law plus favorable average drift is not a proof; the failure modes — divergent orbits and nontrivial cycles — are precisely sustained deviations from the ledgers above, and excluding them requires either measure-theoretic control of the exceptional statistics or exact rigidity statements of the kind `p`-adic Baker theory supplies for cycles (`11.8.3.11`). The honest reading is that Route A is a program for converting the rare-event structure from heuristic to exact, on top of a drift picture that was never the hard part.

#### 11.8.4.5. Compact status snapshot

At this point, the status of the Route A program may be summarized as follows.

```text
formal:
    primary congruence branch,
    global anchor N(ω) = -log ω / log 9  (2-adic logarithm),
    exact global valuation law s = 3 + v_2(n - N(ω)), both lifting components,
    uniform 3-gain law on the lifting branch,
    unconditional polylog spike-height bound (imported: p-adic Baker theory),
    target-shift entry-depth law m_+ and per-step depth law d_+,
        all residue classes (11.8.6.3),
    low-order anchor-increment law ΔM mod 2^k,
        σ-graded moduli, fixed per stratum (11.8.7.3, stage4.md),
    one-step displacement propagation: next s and 3-gain from the
        window, error-free trichotomy (11.8.7.6, stage4.md)

dissolved or exported:
    tower-type classification (no dichotomy: anchor digit density),
    digit behavior of the anchors (classical: digits of 2-adic logarithms;
        effective floor imported, finer statistics beyond current theory)

heuristic, empirically sharp (11.8.4.4):
    frequency ledger P(s=1)=1/2, P(s=2)=1/4, P(s=k)=2^(-k),
    3-gain rate 1/3,
    drift log(3/4) per odd step (classical)

open:
    intrinsic form of the correction term beyond valuation,
    the unbounded-depth residue of the bridge (11.8.7.7) — split:
        typical orbits: anchor equidistribution (11.8.5.6.3 sub-q. 3),
            now the precise missing statistical hypothesis
        cycles: rigidity of closed anchor walks — front OPEN (§12,
            cycles.md): period 1 closed (Steiner contact, 12.2.3),
            stratum congruence system stated, period 2 next
        (bounded-depth content fully formal: 11.8.7.3, 11.8.7.6)
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

