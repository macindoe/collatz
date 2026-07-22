---
status: closed — entry map, tower map, and Stage 1 reduction summary; the synthesis proper (11.8.3) is split to stage1-synthesis.md
scope: monolith 11.8.1-11.8.2, 11.8.4 (11.8.3 → stage1-synthesis.md)
updated: 2026-07-22
source: sources/drafts/collatz_reduction_rewrite_v078.md (last monolith)
---

> **Current state.** Stage 1's entry and summary layers. First-layer mod-8 classification and the lifting-branch congruence reformulation (§11.8.1), the pre-synthesis tower map (§11.8.2), and what the synthesis reduced versus what remains — including the frequency/size ledgers (11.8.4.4) and the status snapshot (11.8.4.5). The synthesis proper — the 2-adic anchor N(ω) = -log ω / log 9, the exact global law s = 3 + v_2(n - N(ω)), and the imported p-adic Baker bounds (11.8.3.11) — is on stage1-synthesis.md (§11.8.3).

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

> **§11.8.3 (the Stage 1 synthesis on the lifting branch) now lives on its own page: `stage1-synthesis.md`.** It identifies the primary congruence branch formally, assembles the global 2-adic anchor `N(ω) = -log ω / log 9`, proves the universal local valuation law `s = 3 + v_2(n - N(ω))` and the boundary-shell localization, and imports the effective `p`-adic Baker bounds (11.8.3.11). Section numbers are unchanged (11.8.3.1-11.8.3.11); the resolver in `index.md` maps them.

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

Exactly one empirical statement survives, and it faces outward rather than inward: the digit statistics of the anchors `N(ω)` are consistent with fair-coin behavior (digit density `0.497` across `2,499` families; Appendix `A.4.6`), as expected for `2`-adic logarithms of integers. Confirming or refining that expectation is a question about classical `p`-adic analysis, not about the Collatz reduction, and nothing in the later stages depends on resolving it. Nor is it entirely out of reach: `p`-adic Baker theory already supplies an unconditional effective floor — an integer of size `n` matches at most `O((log n)^2)` leading anchor digits (Corollary `11.8.3.11.2`). What lies beyond current theory is only the finer statistical behavior. The anchor's consolidated reference is anchors.md §17; the equidistribution hypothesis this digit statistic feeds is formalized at aeh.md §13.

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
        cycles: rigidity of closed anchor walks — cycles.md §12
            (status and ledger live there)
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

