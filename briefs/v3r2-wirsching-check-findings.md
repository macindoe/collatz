# Findings: Wirsching's inverse-map `3`-adic Markov process does **not** cover `13.6.3`(v) or `13.6.5` (v3 round 2, final gate)

**Task:** `briefs/v3r2-wirsching-check-brief.md`. Read-only round; the only file written is this one.
**Read at:** `main` = `e4dac49`.

**Grades, used on every claim below.**

* **[P]** — *verified-primary.* Read by me, this session, from the source document itself.
* **[S]** — *secondary-description.* Someone else's description of a source I did not read.
* **[C]** — *computed by me* this session, exact rational arithmetic (`fractions.Fraction`), no floating point.
* **[?]** — *unconfirmed.*

**What I could and could not obtain, stated first because it governs everything.** I did **not** obtain LNM 1681 itself (rung 1 — see §5). I did obtain, and read in full, **Wirsching's own 18-page restatement of exactly the chapters at issue**, with his own explicit page- and theorem-level cross-references into the monograph (rung 2). That is the load-bearing source, and it is primary. It is corroborated independently at rung 3 (publisher-deposited chapter titles) and rung 4 (Lagarias's chapter-by-chapter annotation of the book, Chamberland's survey, and Tao's footnote read from Tao's own LaTeX).

---

## 0. Verdict

**Object 1 — `aeh.md` `13.6.3`(v), the joint product/renewal law: NOT COVERED.** Not partially. Wirsching's process has no `2`-adic variable at all. Its two coordinates are a *normalised predecessor count* in `[0,1]` and a `3`-adic root in `Z_3^×`; `13.6.3`(v)'s two coordinates are a `2`-adic residue `ω mod 2^{k+2}` and a depth `d = m + a`. The pair of variables whose independence `13.6.3`(v) asserts does not exist in his framework. **[P]**

**Object 2 — `aeh.md` `13.6.5`, the absorption law: NOT COVERED. Wirsching does not predate Tao, and the drafted attribution should name Tao alone.** This is not a judgement call; it is a computation with a one-line cause. Wirsching's `3`-adic step weights the inverse branches **uniformly** over a full period of `2` mod `3^s`, because he is *counting* predecessors. Tao's — and ours — weights the branch by `2^{-a}`, because it is measuring a *typical orbit*. Uniform weights give **Haar**; `2^{-a}` weights give **`Syrac(Z_3)`**. The two laws already disagree at level one:

```text
Wirsching's limiting 3-adic law   =  Haar(Z_3^x)   =  ( 0,  1/2,  1/2 )  on residues 0,1,2 mod 3
aeh.md 13.6.5's nu_1              =  Syrac/2       =  ( 0,  2/3,  1/3 )
```

Wirsching says the uniformity himself, in the one sentence that settles the whole brief (§2.3): *"the operator `S_∞` just integrates over all of `Z_3^×`."* **[P + C]**

**`publication.md` L21: correct in its conclusion, wrong in two factual particulars, and too narrow in scope.** All three need fixing. Replacement drafted at §4.1. **[P]**

**Nothing in the AEH section changes.** Object 1 is not covered, so the paper's framing stands as `briefs/v3r2-contraction-literature-findings.md` and `briefs/v3r2-syrac-identity-findings.md` left it. No `\bibitem` is *owed*. One is *worth adding* for a different and better reason — Wirsching turns out to be a 1998 precedent for the **shape** of AEH, and saying so is to the paper's credit (§4.3).

**A caution about this round's momentum, stated because the brief asked for it.** Three checks in a row found prior art. This one does not, and I want to be explicit that I looked for it: I read Wirsching's own account of the process rather than a summary, I checked the exact object Tao's footnote points at, and the negative result rests on a numerical disagreement I computed rather than on absence of evidence. §5 lists what would overturn it.

---

## 1. Tao's footnote, verbatim — and it says less than the brief supposes

Read from Tao's own arXiv e-print source (`https://arxiv.org/e-print/1909.03562`; `tao.tar.gz` sha256 `ba81acd6…`, `collatz.tex` sha256 `bfbc3943…` — both hashes reproduce `briefs/v3r2-syrac-identity-findings.md` §1 exactly, an independent confirmation of that artifact). The footnote hangs off the phrase "the discrete Markov process" in Remark 1.13, at `collatz.tex` L393. Verbatim, complete: **[P]**

> This Markov process **may possibly be related to** the `3`-adic Markov process for the *inverse* Collatz map studied in [wirsch]. See also a recent investigation of `3`-adic irregularities of the Collatz iteration in [thomas].

**This is a hedge, not an attribution.** Tao writes "may possibly be related to". He does not say Wirsching has this process, or an earlier form of it, or anything about priority. The brief's paraphrase — "Tao's own footnote **credits** Wirsching with the `3`-adic Markov process for the inverse Collatz map" — reads the sentence one notch stronger than it is. What Tao credits Wirsching with is *a* `3`-adic Markov process for the inverse Collatz map; whether it is *this* one he explicitly declines to assert.

Having now read what Wirsching's process is, Tao's hedge is exactly right, and it is right in the informative direction: the two processes **are** related — same map, same prime, both built backwards — and they are **not** the same, because they carry different weights and therefore different invariant measures. §2 and §3.

---

## 2. What Wirsching's `3`-adic process actually is

### 2.1 Provenance of the source, and why it stands in for the monograph

I read **G. J. Wirsching, *On positive predecessor density in `3n+1` dynamics*, 18 pp., PDF titled "(preliminary version)", hosted at `https://www.math.uni-bielefeld.de/baake/algdyn/posden.pdf`**. Published as *Discrete Contin. Dynam. Systems* **9** (2003), no. 3, 771–787 (MR 2004f:39028), per Lagarias's bibliography **[S]**; the copy I read is the author's preliminary version, so its internal section numbers are mine to quote but its pagination may not match the published paper. **[P for content, S for the journal reference]**

It stands in for the monograph because **Wirsching cross-references the monograph explicitly, by chapter, theorem and page, throughout**, citing it as `[4]`: "chapter III of [4]", "theorem III.5.1 in [4]", "theorem III.5.2", "theorem IV.1.14 in [4]", "theorem IV.4.1 in [4]", "cf. [4], p. 103", "[4], p. 107", "cf. [4], section II.4". The material he is restating is therefore author-certified as the monograph's Chapters III and IV. **[P]**

And Chapter IV is precisely the target. The publisher-deposited chapter list (Crossref, `filter=isbn:9783540639701`, 7 records) is: **[P]**

```text
10.1007/bfb0095986  Introduction                                   pp.   1-9
10.1007/bfb0095987  Some ideas around 3n+1 iterations              pp.  10-30
10.1007/bfb0095988  Analysis of the Collatz graph                  pp.  31-75
10.1007/bfb0095989  3-adic averages of counting functions          pp.  76-95
10.1007/bfb0095990  An asymptotically homogeneous Markov chain     pp.  96-122
10.1007/bfb0095991  Mixing and predecessor density                 pp. 123-140
```

The Markov chain is Chapter IV, pp. 96–122 — and Wirsching (2003) cites `[4]` pp. 103 and 107 and Theorems IV.1.14 and IV.4.1, all inside it. Lagarias's annotation of **Wirsching (1994), *A Markov chain underlying the backward Syracuse algorithm*, Rev. Roumaine Math. Pures Appl. 39 (1994), no. 9, 915–926** likewise closes with "The results of this paper are included in Chapter IV". **[S]** So the 1994 paper, Chapter IV, and Wirsching (2003) are three presentations of one object, and I have read one of them in full.

### 2.2 The object, from Wirsching's own text **[P]**

**The counting functions.** `e_ℓ(k,a) := |E_{ℓ,k}(a)|`, the number of predecessors `b` reaching `a` by a `T`-path with `k` even and `ℓ` odd steps. Wirsching's (1.2): `a ≡ b mod 3^ℓ ⟹ e_ℓ(k,a) = e_ℓ(k,b)`, and this — *and only this* — is what lets `a` be taken `3`-adic: "Property (1.2) allows to admit arbitrary `3`-adic numbers `a ∈ Z_3` as arguments for the second variable."

**The measure on the `3`-adic side is Haar, by construction and from the first line.** His (1.4), verbatim: "Denoting by `da` the normalized **Haar measure** on `Z_3^×`, we have the following *averages* of Elka functions (for `ℓ ≥ 1`): `ē_ℓ(k) := ∫_{Z_3^×} e_ℓ(k,a) da = (1/(2·3^{ℓ-1})) · C(k+ℓ, k)`."

**The backward step in `Z_3`.** His (2.1), the generator recursion, verbatim:

```text
g_{ℓ+1}(k,a)  :=   sum_{j=0}^{2·3^ℓ − 1}   g_ℓ( k − j ,  (2^{j+1} a − 1)/3 )        for ℓ ∈ N_0.
```

The `3`-adic move is `a ↦ (2^{j+1}a − 1)/3`, i.e. exactly the **inverse** of `x ↦ (3x+1)/2^{j+1}` — Tao's branch run backwards. **The sum is unweighted**: `j` runs over `0 … 2·3^ℓ − 1`, a full period of `2` mod `3^{ℓ+1}`, with coefficient `1` on every term. That is the whole difference from Tao's `2^{-a}`, and it is not an accident: Wirsching is *counting predecessors*, so every branch must count once.

**The state space is a product of a size coordinate and a `3`-adic coordinate.** `X := I_3 × Z_3^×`, where `I_3` is the base-`3` digit-sequence completion of `[0,1)` (his "digital topology") carrying the normalised count `k/3^ℓ`, and the reference measure is `ϱ =` (lifted Lebesgue on `I_3`) `⊗` (normalised Haar on `Z_3^×`).

**The transition operators**, his (4.2):

```text
S_ℓ f(x,a)  :=  (1/(2·3^{ℓ-3}))  sum_{0 ≤ j < 2·3^{ℓ-1}}  f( 3x − j/3^{ℓ-1} ,  (2^{j+1}a − 1)/3 ).
```

### 2.3 The sentence that settles Object 2 **[P]**

His §5, the limiting transition operator, (5.1) and the remark immediately following it, verbatim:

> `(S_∞ f)(x,a) := (3/2) ∫_{{t ∈ I_3 : 3x−2 ≤ t ≤ 3x}} ∫_{Z_3^×} f(t,b) db dt.`
>
> Note that, in fact, `(S_∞f)(x,a)` **does not depend on `a ∈ Z_3^×`**; w.r.t. the second variable, the operator `S_∞` **just integrates over all of `Z_3^×`**.

In the limit the `3`-adic variable is averaged out against Haar and carries no law of its own. There is no non-trivial stationary measure on `Z_3` anywhere in this construction.

And the "strongly stable Markov chain" of his §6 — the phrase Tao's footnote is pointing at — lives on the **real interval**, not on `Z_3`. His (6.1): `W_3 f(x) = (3/2)∫_{3x−2}^{3x} f(t) dt`, with Corollary 7: a unique `φ ∈ L^1` with `supp φ ⊂ [0,1]`, `∫_0^1 φ = 1`, `W_3 φ = φ`, which is `C^∞` and piecewise polynomial off the classical Cantor set, satisfying `φ'(x) = (9/2)φ(3x)` on `[0, 2/3]`. **[P]**

That `φ` is the invariant density of the *normalised predecessor count*. It is a density on `[0,1]` against Lebesgue. It is not a measure on `Z_3`, it is not `ν`, and it is not `Syrac(Z_3)`.

### 2.4 The reason the `3`-adic side collapses to Haar, verified exactly

Wirsching states the mechanism on p. 12, verbatim: **[P]**

> For any `a ∈ Z_3^×` and any integer `s > 0`, the set `{(2^{j+1}a − 1)/3 : j = 0, …, 2·3^s − 1}` intersects each residue class modulo `3^s` in exactly one point.

I verified this exactly. Of the `2·3^s` values of `j`, exactly `3^s` give a `3`-adic integer (`3 | 2^{j+1}a − 1` fixes the parity of `j`), and those `3^s` images are a **bijection** onto `Z/3^s Z`: **[C]**

```text
s = 1..6, every unit a in Z/3^{s+1}Z :  the 3^s admissible images tile Z/3^s Z exactly once.  0 failures.
```

So one application of the uniform-weight inverse step maps **any** law on `Z_3` exactly to Haar. Haar is not merely invariant for Wirsching's `3`-adic kernel — it is reached in a single step, and no other law can be invariant for it. Tao's kernel does not have this property, because its weights `2^{-a}` are not constant across the period; that is exactly why `Syrac(Z_3)` exists as a non-trivial stationary law at all.

**This is the whole finding in one line:** *counting* the inverse branches gives Haar; *weighting* them by orbit probability gives `Syrac`. Wirsching counts. Tao weights. We weight.

### 2.5 Corroboration at rung 4

* **Lagarias**, annotated bibliography, on Wirsching (1994): the Markov chain is "defined on the state space `[0,1] × Z_3^×`", built from `g_n(k,a)` renormalised by `Γ_n = 2^{1-n}3^{-(n-1)(n-2)/2}(3^n − n)`, with the limiting transition measure having "a density taking the form of a **product measure** `(3/2)χ_{[x/3,(x+2)/3]} ⊗ φ`". Same two coordinates, same product shape. **[S]**
  *One discrepancy, recorded honestly.* Lagarias's phrasing attaches `φ` to `Z_3^×` ("a nonnegative integrable function on `Z_3^×`"), whereas Wirsching's own (5.1) puts plain Haar `db` on `Z_3^×` and makes `φ` the invariant density on `[0,1]`. I cannot resolve which presentation the 1994 paper uses without reading it **[?]**, and it does not move the verdict: §2.4's exact tiling forbids *any* non-Haar invariant law for that kernel, so if a non-constant `φ` on `Z_3^×` appears in the 1994 paper it is a finite-`ℓ` transient or a Radon–Nikodym bookkeeping factor, not a stationary law, and in no case can it be the `2^{-a}`-stationary law.
* **Lagarias**, on the book: Chapter III "observes that the counting functions `e_ℓ(k,a)` … actually are well-defined when the variable `a` is a `3`-adic integer", proves `s_n(a)` is "a nonnegative integrable function of a `3`-adic variable", and estimates its **expected value** `s̄_n`. Averaging, not a stationary law. **[S]**
* **Chamberland**, *An Update on the `3x+1` Problem*, read from the PDF: "The functions `e_l(k,·)` are integrable with respect to `Z_3^×`'s **unique normalized Haar measure**, yielding the `3`-adic average `ē_l(k) := ∫ e_l(k,a) da = (1/(2·3^{l-1})) C(k+l, l)`", and "This application of `3`-adic integers to the `3x+1` Problem was first seen in Wirsching (1994)." **[P]**
* **Wirsching (1997)**, title alone: *`3n+1` Predecessor Densities and **Uniform Distribution in `Z_3^*`***, Proc. Conf. Elementary and Analytic Number Theory (Hlawka Festschrift), Vienna 1996, pp. 230–240 (Zbl 883.11010). Lagarias: it "formulates a kind of **equidistribution hypothesis** on `3`-adic integers under backwards iteration". **[S]** Wirsching's `3`-adic target is uniformity. Ours is explicitly non-uniform.

Four independent sources, one picture: **Haar on the `3`-adic side, throughout Wirsching's programme.**

---

## 3. The two objects, decided

### 3.1 Object 2 first, because it is the cleaner of the two

**Does Wirsching predate Tao for `13.6.5`'s absorption law? No.**

`13.6.5`'s law is the `2^{-a}`-weighted stationary measure `ν` on `Z_3`, `= Syrac(Z_3)/2`. Wirsching's `3`-adic limit is Haar on `Z_3^×`. They differ at the coarsest possible level:

```text
residue mod 3            :   0      1      2
Haar(Z_3^x)  (Wirsching) :   0     1/2    1/2
nu_1         (13.6.5)    :   0     2/3    1/3
```

I re-derived `ν_j` independently this session — a fresh implementation of the letter kernel `Y ↦ β + αY`, with the geometric tails in `m` and `r` summed in **closed form** rather than truncated, so the result is exact and not an approximation. It reproduces `Syrac/2` at every level checked, from the other side: **[C]**

```text
nu_1 = (0, 2/3, 1/3)                                         ==  law(Syrac(Z/3Z)/2)    True
nu_2 = (0, 16/63, 11/63, 0, 22/63, 8/63, 0, 4/63, 2/63)      ==  law(Syrac(Z/9Z)/2)    True
nu_3 (27 values)                                             ==  law(Syrac(Z/27Z)/2)   True
```

and my `Syrac` implementation, coded from Tao's Lemma 1.12 as read from his source, reproduces his printed `Syrac(Z/9Z) = 0, 8/63, 16/63, 0, 11/63, 4/63, 0, 2/63, 22/63` exactly before any comparison is made. **This independently confirms `briefs/v3r2-syrac-identity-findings.md`'s central identity by a separate code path** — worth recording, since that finding is now carrying the AEH section's attribution.

**Consequence for the attribution.** `briefs/v3r2-syrac-identity-findings.md` §9.1–9.3's drafted `\bibitem{tao}` and attribution paragraphs are **correct as they stand** and need no second source added. Tao (2019/2022) is the right and only citation for `13.6.5`'s law.

### 3.2 Object 1 — `13.6.3`(v)'s joint product/renewal law

**Not covered.** In substance, `13.6.3`(v) says: under `B`, the conditional law of `y_n` given the past is exactly Haar-odd; hence `(m_n, q_n) ⊥` the whole past, `m_n` geometric(1/2), `q_n` Haar-odd given `m_n`; `a_{n+1}` is a function of the past alone; and the reconstructed window state has the exact product law `(ω`-residue Haar-uniform-odd`) ⊗ (d = m + a, m ⊥ a)`.

Set against Wirsching's framework, point by point: **[P for each left-hand fact; the coverage judgement is my inference from them, flagged as such]**

| `13.6.3`(v) needs | Wirsching has |
|---|---|
| a `2`-adic residue variable `ω mod 2^{k+2}` | nothing `2`-adic anywhere; his second coordinate is `Z_3^×` |
| Haar-**odd** (i.e. `2`-adic) conditional law of the door given the past | Haar on `Z_3^×`, a `3`-adic statement |
| `m_n` geometric(1/2), the `2`-adic valuation of `y+1` | a normalised **count** `k/3^ℓ ∈ [0,1]`, whose invariant density `φ` solves `φ' = (9/2)φ(3·)` and is Cantor-supported-off; not geometric, not a valuation |
| absorption `a = v_3(y+1)` with the explicit law `2/3, 19/63, 2/63` | no valuation variable and no non-Haar `3`-adic law |
| independence of `ω`-residue from depth, **exact at every finite `n`** under `B` | independence of the count from the `3`-adic root, **only in a weak renormalised limit**, and even then as a conjecture-laden programme |
| a renewal decomposition of the exponent sequence at entries `≥ 2` | a block-of-zeros encoding of parity vectors — the classical coding, already conceded classical at `publication.md` L19/L40 and `aeh.md` L76 |

The two variables whose independence `13.6.3`(v) asserts do not both exist in Wirsching's framework, so his product measure cannot be ours regardless of any coordinate dictionary. There is no dictionary to look for: `2`-adic data is simply absent from his construction.

**The one honest point of structural kinship, and it is worth the paper saying out loud.** Wirsching's `ϱ = ` Lebesgue `⊗` Haar *is* a "the arithmetic coordinate becomes uniform and independent of the size coordinate" statement — but in the **other prime**, and pointing the other way. He needs the `3`-adic coordinate to equidistribute; we need the `2`-adic one to, and our `3`-adic coordinate is provably *non*-uniform. These are two faces of the same missing genre of theorem — precisely the `×2×3` framing `aeh.md` `13.6.7` already names. That is a related-work observation, not prior art, and §4.3 drafts it.

### 3.3 The secondary question: `13.6.1` and `13.6.2`

**No exposure, and nothing to change.** Wirsching's path encoding — the `(α_0, α_1, …, α_μ)` blocks-of-zeros encoding of the parity vector **[S**, Lagarias**]** — is one more instance of the classical Collatz coding. `aeh.md` L59/L76 already frames `13.6.1`–`13.6.2` as classical with Terras/Everett/Lagarias/Bernstein–Lagarias pinned and disclaims novelty for the door-alphabet form; `publication.md` L40 says the same for `14.15.1`. Wirsching's encoding is consistent with that concession and does not enlarge it. **No change needed.**

---

## 4. What the record must say

### 4.1 `publication.md` L21 — wrong in two particulars, and too narrow

The current text reads:

> `3`-adic material checked and found *not* to be the same object as `14.15.3`(c)'s two-sided coding: G. Wirsching, *The Dynamical System Generated by the `3n+1` Function*, Lecture Notes in Math. 1681, Springer, 1998 (**3-adic averages of stopping-time counting functions** — a different `3`-adic use); …

Three defects. **[P for all three]**

1. **"stopping-time counting functions" is wrong.** They are **predecessor** counting functions: `e_ℓ(k,a)` counts the `b` with `T^{k+ℓ}(b) = a`. Chapter III is titled "`3`-adic averages of counting functions"; the counting is of predecessors, and the book's whole object is predecessor density. Stopping time is Terras's variable, not Wirsching's.
2. **The scope is too narrow, exactly as the brief anticipated.** The verdict was aimed at `14.15.3`(c)'s two-sided `Z_2 × Z_3` coding. It is now also the standing verdict for `13.6.3`(v) and `13.6.5`, and the page must say which objects it covers.
3. **The conclusion itself is correct** — "a different `3`-adic use" is right, and now for a stateable reason rather than an impression.

The same wording error sits at `itinerary.md` L126, which additionally says Wirsching "treats the **starting value** as a `3`-adic variable". That is also inaccurate: the `3`-adically completed variable is the **root** `a` of the predecessor tree — the *destination* of the forward iteration, the *source* of the backward one — not the starting value. Read-only here; flagged for whoever edits.

**Drafted replacement for L21** (matching the file's bullet register; substitute for the Wirsching clause only, leaving the Monks–Yazinski clause as it stands):

```text
* 3-adic material checked, twice, and found not to be the same object as either
  `14.15.3`(c)'s two-sided coding or `aeh.md` `13.6.3`(v)/`13.6.5`: G. Wirsching,
  *The Dynamical System Generated by the `3n+1` Function*, Lecture Notes in Math.
  1681, Springer, 1998. Wirsching `3`-adically completes the *root* of the
  predecessor tree in order to average **predecessor**-counting functions
  `e_ℓ(k,a)` over it (Ch. III, "3-adic averages of counting functions"), and
  builds from the inverse map an asymptotically homogeneous Markov chain on
  `[0,1] × Z_3^×` (Ch. IV) whose size coordinate carries the invariant density
  `φ' = (9/2)φ(3·)` and whose `3`-adic coordinate is **Haar** — his limiting
  operator, in his own words, "just integrates over all of `Z_3^×`". His inverse
  branches are weighted **uniformly**, because he is counting predecessors; ours
  and Tao's are weighted `2^{-a}`, because they measure a typical orbit, and that
  is exactly why `ν` is the non-uniform `(2/3, 1/3)` at level one where
  Wirsching's law is `(1/2, 1/2)`. So Wirsching is neither prior art for
  `13.6.5`'s law (that is Tao's — see below) nor for `13.6.3`(v)'s joint law
  (which has a `2`-adic coordinate his framework does not contain). Verified
  against Wirsching's own restatement of Chs. III–IV, *On positive predecessor
  density in `3n+1` dynamics*, Discrete Contin. Dynam. Systems 9 (2003), 771–787,
  and confirmed in exact arithmetic (2026-08-02, `briefs/v3r2-wirsching-check-findings.md`).
  (14.15.3(d), 13.6.3(v), 13.6.5)
```

`publication.md` L28's neighbour-3 sentence lists "Wirsching" among the classical foundations to be cited "as prior art for §13's product law". **That phrase is now wrong and should go** — Wirsching is not prior art for §13's product law. Terras and the `2`-adic conjugacy line remain correctly listed there; only the Wirsching name should be removed from that clause, or moved to the related-work framing of §4.3 below. **[P]**

`publication.md` L29's targeted-check paragraph is accurate as far as it goes and needs only its Wirsching sentence's "stopping-time" corrected to "predecessor-counting", plus the same scope note.

### 4.2 `aeh.md` — nothing owed

`13.6.5` takes the attribution already drafted at `briefs/v3r2-syrac-identity-findings.md` §9.3, unchanged, naming Tao. `13.6.3`(v) takes nothing. No sentence in `aeh.md` is falsified by this round.

### 4.3 The `\bibitem` that is worth adding, and why it is not an admission

None is owed. One is worth having, for the opposite of the usual reason.

```latex
\bibitem{wirsching} G.~J.~Wirsching, \emph{The Dynamical System Generated by the
  $3n+1$ Function}, Lecture Notes in Math.\ 1681, Springer-Verlag, Berlin, 1998.
```

Verified: title, series, volume, publisher, place, year — from Wirsching's own reference list in the 2003 paper ("Springer Lecture Notes in Mathematics **1681** (1998), 158 p."), from Tao's `\bibitem{wirsch}`, and from Lagarias's bibliography (MR 99g:11027). ISBN 9783540639701. **[P]**

Drafted sentence for Related Work, to sit near the `\cite{tao}` sentence:

```latex
A $3$-adic view of the Collatz map is not new, and the closest earlier one is
instructive precisely because it is not the same. Wirsching \cite{wirsching}
completes the root of the predecessor tree $3$-adically and studies the inverse
map as a Markov chain on $[0,1] \times \Z_3^{\times}$, in order to count
predecessors; his inverse branches therefore carry equal weight, his limiting
$3$-adic law is Haar, and what he needs is that predecessors equidistribute in
$\Z_3^{\times}$. The stationary law appearing here weights each branch by the
probability $2^{-a}$ that an orbit takes it, and is consequently \emph{not}
uniform --- it is Tao's $\mathrm{Syrac}(\Z_3)$ \cite{tao}, whose level-one law
is $(\tfrac23, \tfrac13)$ where Haar would give $(\tfrac12,\tfrac12)$. The two
programmes are nonetheless siblings in shape: Wirsching's needed hypothesis is
that a Collatz-generated object is unbiased in $3$-adic coordinates, and
Hypothesis~\ref{hyp:aeh} is that one is unbiased in $2$-adic coordinates. Both
are instances of the same missing genre of theorem.
```

Why include it. A referee who knows this literature will ask what Wirsching's `3`-adic Markov process has to do with §5, because Tao's own footnote raises the question. Answering it in one paragraph — with the weighting as the reason, and the level-one numbers as the evidence — converts an obvious referee question into a demonstration that the distinction is understood. Leaving it out invites the question to be asked adversarially. It is cheap, and it is true.

### 4.4 If Object 1 had been covered

It is not, so this section is short, as the brief allows. **Nothing about what remains novel in the AEH section changes.** The standing position from the two prior rounds holds unaltered: the descent consequence is gone (Inselmann), the first moment is gone (Inselmann Thm 1.6), `13.6.5`'s law is Tao's, and what remains is `13.6.3`(v)'s joint product/renewal law — the `ω`-residues Haar-uniform among odd residues and independent of the depth, with `d = m + a`, `m ⊥ a` — together with `13.6.4`'s orbit-by-orbit genericity equivalence and the calibration record. This round removes nothing further from that list. It is the same list, now checked against the one source that had been left on the table.

---

## 5. What I did not establish, and what would settle it

1. **I did not read LNM 1681.** Rung 1 failed: Springer gates both the book page and every chapter page behind `idp.springer.com` authentication; zbMATH returned HTTP 403; MathSciNet is subscription-only; there is no copy on archive.org; no legitimate free full text exists that I could find. **What would settle it beyond doubt: pp. 96–122 (Ch. IV, "An asymptotically homogeneous Markov chain") and pp. 123–140 (Ch. V, "Mixing and predecessor density"), via any university library with the Springer LNM series, or ILL of ISBN 9783540639701.** A reader with those 45 pages could confirm §2 in an hour. My confidence that they would confirm it is high but not total, and it rests on Wirsching's own restatement rather than on the book.
2. **[?] Chapter V, "Mixing and predecessor density" (pp. 123–140), is the one chapter with no restatement I could read.** Lagarias's chapter-by-chapter annotation stops at Chapter IV and says nothing about V. Wirsching (2003) covers Chapters III–IV. The circumstantial case that V is the `Z_3^×`-equidistribution material is strong — Wirsching (1997) is titled "*`3n+1` Predecessor Densities and **Uniform Distribution in `Z_3^*`***" and Lagarias describes it as an equidistribution hypothesis on `3`-adic integers under backward iteration **[S]** — but I did not read either. **This is the residual risk and I want it named:** if a `2^{-a}`-weighted law appears anywhere in the monograph, Chapter V is where it would be. I judge this unlikely, because a `2^{-a}` weight is orbit-probability bookkeeping and would be alien to a predecessor-*counting* programme, and because §2.4's tiling shows the kernel he actually uses cannot support one — but "unlikely on structural grounds" is not "checked".
3. **[?] Wirsching (1994) itself**, Rev. Roumaine Math. Pures Appl. 39 (1994), 915–926, not read; not online. Only Lagarias's annotation. The `φ`-placement discrepancy noted at §2.5 is the one thing in this round where two descriptions disagree, and reading the 1994 paper is what would resolve it. It does not move the verdict (§2.5 gives the reason).
4. **Not attempted, and out of this brief's scope:** Tao's footnote also names **A. Thomas**, *A non-uniform distribution property of most orbits…*, Acta Arith. **178** (2017), 125–134, for "`3`-adic irregularities of the Collatz iteration". The title's "non-uniform distribution" is the one phrase in this round's reading that points at a *non*-Haar `3`-adic law, which is the genre `ν` belongs to. `briefs/v3r2-syrac-identity-findings.md` §11 item 4 left it unread too. **It is now the only unexamined item from Tao's footnote, and it is a 2017 paper, two years before Tao.** I did not open it and I make no claim about it; I flag it as the natural successor to this round and the last thing I would want a referee to find first.
5. **Not attempted:** G. M. Leigh, *A Markov process underlying the generalized Syracuse algorithm*, Acta Arith. (1986), surfaced incidentally. It is a *forward* process on residues, the Matthews–Watts genre, and is not the inverse-map object this brief targets. No claim either way.

---

## 6. Verification table

| Fact | Source, grade |
|---|---|
| Tao's footnote text, verbatim; "may possibly be related to", not an attribution | `collatz.tex` L393, arXiv e-print `1909.03562` — **[P]** |
| `tao.tar.gz` sha256 `ba81acd6…`; `collatz.tex` sha256 `bfbc3943…` (both reproduce the sibling round's hashes) | this session — **[P]** |
| Tao `\bibitem{wirsch}` = LNM 1681, Springer, Berlin 1998 | `collatz.tex` L1948–1950 — **[P]** |
| LNM 1681 chapter titles and page ranges (6 chapters, incl. Ch. IV "An asymptotically homogeneous Markov chain", pp. 96–122) | Crossref, publisher-deposited, `isbn:9783540639701` — **[P]** |
| Wirsching (2003) restates Chs. III–IV with explicit cross-refs to `[4]` III.5.1, III.5.2, IV.1.14, IV.4.1, pp. 103, 107, §II.4 | `posden.pdf` throughout — **[P]** |
| Wirsching's (1.4): `da` is "the normalized Haar measure on `Z_3^×`"; `ē_ℓ(k) = (1/(2·3^{ℓ-1}))C(k+ℓ,k)` | ibid. p. 4 — **[P]** |
| Wirsching's (2.1): `g_{ℓ+1}(k,a) = Σ_{j=0}^{2·3^ℓ−1} g_ℓ(k−j, (2^{j+1}a−1)/3)`, **unweighted** | ibid. p. 7 — **[P]** |
| State space `X = I_3 × Z_3^×`; reference measure = Lebesgue `⊗` normalised Haar | ibid. p. 9 — **[P]** |
| Transition operators `S_ℓ`, eq. (4.2) | ibid. p. 10 — **[P]** |
| **`S_∞` "just integrates over all of `Z_3^×`"; `(S_∞f)(x,a)` independent of `a`** | ibid. p. 11, eq. (5.1) + remark — **[P]** |
| The tiling: `{(2^{j+1}a−1)/3}` meets each class mod `3^s` exactly once | ibid. p. 12 — **[P]** |
| `W_3 f(x) = (3/2)∫_{3x−2}^{3x} f`; unique invariant `φ` on `[0,1]`, `φ'(x) = (9/2)φ(3x)`, `C^∞`, piecewise polynomial off the Cantor set | ibid. pp. 13–14, 16, Cor. 7 — **[P]** |
| Tiling verified: `s = 1..6`, all units, `3^s` admissible images biject onto `Z/3^sZ`, 0 failures | exact integer arithmetic — **[C]** |
| Uniform-weight inverse kernel sends any law to Haar in one step; Haar is its only invariant law | consequence of the tiling — **[C]** |
| `ν_1 = (0, 2/3, 1/3) ≠ Haar(Z_3^×)_1 = (0, 1/2, 1/2)` | — **[C]** |
| `ν_j == law(Syrac(Z/3^jZ)/2)` for `j = 1,2,3`, independent reimplementation with closed-form geometric tails | — **[C]** |
| `Syrac(Z/9Z) = 0, 8/63, 16/63, 0, 11/63, 4/63, 0, 2/63, 22/63` reproduced from Tao's Lemma 1.12 before any comparison | — **[C]** |
| Lagarias on Wirsching (1994): chain on `[0,1] × Z_3^×`; product transition density; results included in Ch. IV | `arXiv:math/0309224` (source, v104) L6062–6110 — **[S]** |
| Lagarias on the book, Chs. I–IV; `e_ℓ(k,a)` well-defined for `3`-adic `a`; expected value `s̄_n` | ibid. L6177–6300 — **[S]** |
| Lagarias on Wirsching (1997): "equidistribution hypothesis on `3`-adic integers under backwards iteration" | ibid. L6157–6174 — **[S]** |
| Wirsching (2003) = DCDS 9 (2003), no. 3, 771–787, MR 2004f:39028 | `arXiv:math/0608208` L3540–3551 — **[S]** |
| Chamberland: `e_l(k,·)` integrable w.r.t. "`Z_3^×`'s unique normalized Haar measure"; `3`-adic application "first seen in Wirsching (1994)" | `3x_survey_eng.pdf` p. 12 — **[P]** |
| `publication.md` L21 says "stopping-time counting functions"; they are predecessor-counting functions | `publication.md` L21 vs. sources above — **[P]** |
| `itinerary.md` L126 says "starting value"; the `3`-adic variable is the predecessor tree's root | `itinerary.md` L126 vs. sources above — **[P]** |
| LNM 1681 full text: not obtainable (Springer auth-gated, zbMATH 403, no archive.org copy) | attempted this session — **[?]** |

**Scripts** (scratchpad only; nothing added to `experiments/`): `wirsching_vs_nu.py` (the tiling check; the two kernels side by side), `nu_exact_check.py` (exact `ν_j` with closed-form geometric tails; Tao's Lemma 1.12; the `ν_j = Syrac/2` cross-check). All exact `Fraction`; every distribution asserted to sum to `1` before use.
