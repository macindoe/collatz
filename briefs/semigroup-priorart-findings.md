# Findings: prior art on the affine composition semigroup `S`

*Delegated session, branch `semigroup-priorart`, 2026-07-26. Answers `briefs/semigroup-priorart-brief.md`. Literature and framing assessment only — no wiki edits, no cycle work, no attempt at Q1 or Q3.*

## Verdict

**(B) — related but distinct, with one correction to the gate question's premise.** `S` as stated in the brief's §1 — the accelerated `(m,r)` stratum alphabet, over `Q` read `3`-adically — is not a named object in the literature, and no source was found that forms it. But the *framing* the brief treats as the one thing not yet on file ("treating the composed maps as a **semigroup** rather than one at a time") is **standard prior art in two separate literatures**, and `S` is a sub-semigroup of a named, studied object whose freeness is a published theorem. Specifically: `g_{m,r} = T_0^r ∘ T_1^m` exactly, where `T_0(x) = x/2` and `T_1(x) = (3x+1)/2` are the two raw affine branches of the Collatz map — and the semigroup those two generate is proved free on two generators by Misiurewicz and Rodrigues (2005). The verification of that identification is `experiments/semigroup_priorart_check.py` (22,289 exact-`Fraction` checks, 0 failures).

The honest shape of the result is a **closure, not a lever**, and it closes in the direction the brief predicted, by a route the brief did not anticipate. The brief's §5 hypothesis is **refuted** (§5 below), but its underlying intuition — that the known semigroup objects discard exactly the information in which the cycle question lives — is **confirmed**, and confirmed more strongly than the hypothesis proposed, by a published theorem rather than by an analogy.

One point of process worth stating flatly at the top: the brief's provenance paragraph records that "the word 'semigroup' appears nowhere in the wiki or in `briefs/` (verified by grep, 2026-07-26)." That is a true fact about *this repository*. It was read — reasonably, but wrongly — as evidence that the framing was unexplored. It is not. The framing is roughly fifty years old on the general-theory side (Klarner–Rado 1974, Klarner 1982) and twenty on the Collatz-specific side (Misiurewicz–Rodrigues 2005). Absence from our own wiki is not absence from the literature, and the two were conflated.

---

## 1. Citation ledger

Every item below was verified against a primary or publisher record actually read in this session. Where a detail could not be confirmed it says **unconfirmed**. Nothing here is propagated from the brief's recollections without independent confirmation.

### 1.1 The brief's §3 leads

**Lead 1 — Applegate & Lagarias, "The 3x+1 semigroup". CONFIRMED, including the page range.**

> D. Applegate, J. C. Lagarias, *The 3x+1 semigroup*, Journal of Number Theory **117** (2006), no. 1, 146–159. DOI [10.1016/j.jnt.2005.06.010](https://doi.org/10.1016/j.jnt.2005.06.010). Preprint: [arXiv:math/0411140](https://arxiv.org/abs/math/0411140) (v2, 4 May 2005).

The main session's recollection of `117` (2006) `146–159` is **exactly right**. Two metadata discrepancies found in the wild, recorded so a later session does not "correct" the citation into error: (i) the **arXiv journal-ref field says 147–159**; the Crossref publisher record says **146–159**, which is authoritative and is what the main session had. (ii) **Lagarias's own annotated bibliography II and his 2021 Overview survey both print the volume as `177`** — a typo in his own bibliography; the correct volume is `117`.

The claim that "the weak 3x+1 semigroup conjecture is believed to be proved there" is **confirmed** and is the paper's main theorem, read from the paper itself (§1, p. 2):

> **Theorem 1.1.** *The `3x+1` semigroup `S` equals the set of all positive rationals `a/b` in lowest terms having the property that `b ≢ 0 (mod 3)`. In particular, it contains every positive integer.*

**Lead 2 — H. M. Farkas. CONFIRMED, with the title corrected.**

> H. M. Farkas, *Variants of the `3N+1` conjecture and multiplicative semigroups*, in: M. Entov, Y. Pinchover, M. Sageev (eds.), *Geometry, Spectral Theory, Groups, and Dynamics: Proceedings in Memory of Robert Brooks*, Contemporary Mathematics **387** (= Israel Mathematical Conference Proceedings), Amer. Math. Soc., Providence RI, 2005, pp. 121–127. DOI [10.1090/conm/387/07238](https://doi.org/10.1090/conm/387/07238).

The main session's guess of "a *Contemporary Mathematics* volume chapter, mid-2000s" is **right**. **Title correction:** Applegate–Lagarias's own reference [1] prints it as "Variants of the `3N + 1` **problem** and multiplicative semigroups" (and as "to appear"); the published title uses **conjecture**, per the Crossref record and the AMS volume contents. Use *conjecture*. The volume is jointly a Contemporary Mathematics volume and an Israel Mathematical Conference Proceedings volume, which is why the two venue names both appear in the literature; both are correct.

**Lead 3 — Lagarias's annotated bibliographies. CONFIRMED as instruments and swept.** [arXiv:math/0309224](https://arxiv.org/abs/math/0309224) (1963–1999) and [arXiv:math/0608208](https://arxiv.org/abs/math/0608208) (II, 2000–2009), plus the survey [arXiv:2111.02635](https://arxiv.org/abs/2111.02635) (*The 3x+1 Problem: An Overview*). The sweep of these is where the decisive material came from, and it is the single most productive angle in this pass. Two results worth recording:

- Lagarias himself frames the affine-map strand as part of the problem, in bibliography I's own introduction: the `3x+1` problem "can also be rephrased as a problem concerning sets of integers generated using affine maps … Therefore this bibliography includes work on sets of integers generated by iteration of affine maps, tracing back to Isard and Zwicky (1970) and Klarner and Rado (1974)." The Overview's closing research-directions section proposes continuing "the study, initiated by Klarner and Rado, of sets of integers (or integer vectors) closed under the action of a finitely generated semigroup of affine maps."
- **"Cocycle" occurs zero times in all three documents.** A clean negative: the cocycle coordinate `β` is not a term of art in this literature. That does not make `β` new — it is the standard affine-composition constant — but no one appears to have named it as a cocycle here or studied it as one.
- **Caraiani (2010) is absent from bibliography II**, including from v6 (Feb 2012), which postdates it.

**Lead 4 — Wirsching, LNM 1681. CONFIRMED as a citation, DISCARDED as prior art for this object.**

> G. J. Wirsching, *The Dynamical System Generated by the `3n+1` Function*, Lecture Notes in Mathematics **1681**, Springer, Berlin, 1998.

No semigroup or monoid treatment of the `3n+1` tree was found. The monograph's subject is predecessor sets analysed by elementary number theory, combinatorics, asymptotic analysis and measure theory. This agrees with the wiki's existing verdict at `itinerary.md` 14.15.3(d) and `publication.md`, which already distinguishes Wirsching's `3`-adic material from ours; nothing there needs revising. (Note: Applegate–Lagarias's reference [8] renders the title as "The dynamical system **on the natural numbers** generated by the `3n+1` function"; the published Springer title is as given above, which is what the wiki already uses.)

**Lead 5 — Matthews & Watts. CONFIRMED as existing; DISCARDED as prior art for this object.**

> K. R. Matthews, A. M. Watts, *A generalization of Hasse's generalization of the Syracuse algorithm*, Acta Arithmetica **43** (1984), no. 2, 167–175.

Verified via EUDML. Their generalized mapping `T(x) := (m_i x − r_i)/d` for `x ≡ i (mod d)` is genuinely the closest *ambient* setting to our `Z_3` picture, and these maps are affine on residue classes. But the object of study is the map and its ergodic behaviour on `Z_d` (measure-preserving, strongly mixing, the Matthews–Watts uniform-distribution conjecture) — **not a semigroup generated by the branches**. No semigroup treatment found. I did **not** obtain the full text of the 1984 paper; the description above is from the EUDML record and secondary sources, so the "no semigroup treatment" finding for this specific paper is **based on abstract and keywords, not full text** — recorded as a limitation rather than smoothed over.

**Lead 6 — Bernstein & Lagarias, *The 3x+1 conjugacy map*. Already pinned in the wiki; re-checked as instructed, nothing to add.** No semigroup treatment in it or, so far as the sweep reached, in its citing literature. The conjugacy `Φ` is a single map, not a semigroup; the wiki's use of it at `itinerary.md` 14.15.3(a) is unaffected.

**Lead 7 — general theory of affine semigroups. CONFIRMED to exist, and it is the substantive part of this lead.** See §1.2 and §2.6 below. It is much less thin than the brief allowed for: sub-semigroups of `Aff(1,·)`, freeness criteria, and infinite-alphabet IFS all have real literatures. What is genuinely thin — and this is the one place where the sweep's negative is sharp rather than merely unfound — is the intersection of *infinitely generated*, *deterministic*, and *non-archimedean*. Every freeness criterion located is finitely generated; the one non-archimedean criterion (Breuillard) is two-generator; the infinite-alphabet IFS theory is Euclidean. Details and the reasons each fails on `S` are in §2.6.

### 1.2 Items the brief's list did not contain — the affine strand

These are the finds that decide the verdict. All four are pinned against Crossref or arXiv records read in this session.

> **M. Misiurewicz, A. Rodrigues**, *Real 3x+1*, Proceedings of the American Mathematical Society **133** (2005), no. 4, 1109–1118. DOI [10.1090/S0002-9939-04-07696-8](https://doi.org/10.1090/S0002-9939-04-07696-8). *(Note the author's name is* **Rodrigues**, *not "Rodriguez"; Lagarias's bibliography annotation spells it both ways in different places.)*

> **D. A. Klarner**, *A sufficient condition for certain semigroups to be free*, Journal of Algebra **74** (1982), no. 1, 140–148. DOI [10.1016/0021-8693(82)90010-2](https://doi.org/10.1016/0021-8693(82)90010-2). *(Lagarias's Overview reference [53] prints the pages as 40–48; Crossref gives* **140–148**, *which is what bibliography I also gives. Use 140–148.)*

> **V. Bergelson, M. Misiurewicz, S. Senti**, *Affine actions of a free semigroup on the real line*, Ergodic Theory and Dynamical Systems **26** (2006), no. 5, 1285–1305. DOI [10.1017/S014338570600037X](https://doi.org/10.1017/S014338570600037X).

> **A. Kolpakov, A. Talambutsa**, *On free semigroups of affine maps on the real line*, Proceedings of the American Mathematical Society **150** (2022), no. 6, 2301–2307. DOI [10.1090/proc/15832](https://doi.org/10.1090/proc/15832). Preprint [arXiv:2105.09387](https://arxiv.org/abs/2105.09387). *(An earlier draft of this file recorded "journal reference: none on arXiv, unconfirmed"; the Crossref record settles it — it is published, and the arXiv page simply lacks the journal-ref. Corrected.)*

And — the item that most directly vindicates the verdict, because it is Lagarias himself connecting the affine-semigroup freeness circle to `3x+1`:

> **J. C. Lagarias**, *Erdős, Klarner, and the `3x+1` problem*, American Mathematical Monthly **123** (2016), no. 8, 753–776. DOI [10.4169/amer.math.monthly.123.8.753](https://doi.org/10.4169/amer.math.monthly.123.8.753). Reprinted as ch. 8, pp. 139–168, of *Connections in Discrete Mathematics*, Cambridge University Press, 2018, DOI [10.1017/9781316650295.009](https://doi.org/10.1017/9781316650295.009).

This is a survey of the Erdős/Klarner/Rado work on **semigroups of integer affine maps** written explicitly around the `3x+1` problem, and it records that several of the freeness problems Klarner posed in 1982 **remain unsolved**. Its existence is the single cleanest answer to the gate question: the affine-semigroup framing of `3x+1` is not merely present in the literature, it has a survey article by the field's principal bibliographer, in the Monthly, ten years ago.

Also in this strand, from the same sweep and pinned, though secondary for our purposes: D. A. Klarner, *An algorithm to determine when certain sets have 0 density*, J. Algorithms **2** (1981), 31–43; D. A. Klarner, *m-recognizability of sets closed under certain affine functions*, Discrete Appl. Math. **21** (1988), no. 3, 207–214; D. A. Klarner, R. Rado, *Arithmetic properties of certain recursively defined sets*, Pacific J. Math. **53** (1974), no. 2, 445–463.

### 1.3 Items the brief's list did not contain — the piecewise-affine (RCWA) strand

> **S. Kohl**, *Restklassenweise affine Gruppen*, Dissertation, Universität Stuttgart, 2005.

> **S. Kohl**, *A reformulation of the `3n+1` conjecture in terms of a mapping from the free monoid of rank 2 to the positive integers*, short note, 3 pp., 2007. **Self-published on the author's page; no journal venue found — treat as an unrefereed note.** Read in full in this session.

> **S. Kohl**, *Wildness of iteration of certain residue-class-wise affine mappings*, Advances in Applied Mathematics **39** (2007), no. 3, 322–328.

> **S. Kohl**, *The Collatz conjecture in a group theoretic context*, Journal of Group Theory **20** (2017), no. 5, 1025–1030. DOI [10.1515/jgth-2017-0012](https://doi.org/10.1515/jgth-2017-0012). Read in full in this session.

Kohl's `Rcwa(Z)` — all `f : Z → Z` affine on each residue class mod some `m` — is **a monoid of piecewise-affine maps under composition**, and both the Collatz map and `T` belong to it.

### 1.4 The follow-up that decides §5

> **A. Caraiani**, *Multiplicative semigroups related to the `3x+1` problem*, Advances in Applied Mathematics **45** (2010), no. 3, 373–389. DOI [10.1016/j.aam.2010.01.009](https://doi.org/10.1016/j.aam.2010.01.009). Read in full (opening sections) in this session.

### 1.5 Checked and set aside

- **M. Trümper**, *The Collatz problem in the light of an infinite free semigroup*, Chinese Journal of Mathematics **2014**, Article ID 756917, 21 pp. DOI [10.1155/2014/756917](https://doi.org/10.1155/2014/756917). Title and abstract verified from two independent listings; **full text not obtained** (Wiley/Hindawi returned 403 and Cloudflare blocked direct download), so the internal content is **unconfirmed**. From the published abstract, the "free semigroup" is the abstract semigroup of formal *T-words under concatenation* — free by construction — with "diophantine and rational functions" then *defined on* it; that is a word space plus an evaluation map, structurally the same posture as our itinerary alphabet plus `W ↦ (A_W, B_W)`, and not a proof that a semigroup of maps is free. The abstract's "one-parameter family of start numbers compatible with any given T-word" is, on its face, the cylinder theorem (`itinerary.md` 14.15.1.5) in different coordinates — which the wiki already concedes is classical (Terras/Everett). The abstract's "intimate relationship between the `3m+1` and `3m−1` problems" is the sector correspondence the wiki carries at 14.15.6. Venue is weak (Hindawi, discontinued). **Recorded, not cited as prior art**, pending a reader who can obtain the full text.
- **S. Angermund**, *A Two-Operator Calculus for Arithmetic-Progression Paths in the Collatz Graph*, [arXiv:2506.19115](https://arxiv.org/abs/2506.19115) (23 June 2025). Category **math.GM** (General Mathematics), no journal reference — **not peer-reviewed**. Uses affine operators on arithmetic progressions and closed formulas for prescribed parity words, and describes its operator pair as generating "a particularly simple rcwa subgroup." Adjacent in language; **not cited as prior art**, per the house standard applied at `itinerary.md` 14.15.3(d) to non-peer-reviewed near-misses.
- **Peres, Simon & Solomyak**, *Absolute continuity for random iterated function systems with overlaps*, J. London Math. Soc. **74** (2006), no. 2, 739–756 — bears on a question of Sinai motivated by `3x+1`. This is affine-recursion/random-IFS territory and therefore **out of scope by the brief's forbidden list**; one-line pointer only, no engagement.
- **Bergelson–Misiurewicz–Senti's Theorems D and E** (invariant measures for the free affine action, Lyapunov exponent `λ(ν) = ν(C_0)ln a + ν(C_1)ln b`, existence iff `λ(ν) < 0`) are likewise the affine-recursion/statistical front. **One-line pointer, no engagement**, per the forbidden list.

---

## 2. The comparative assessment (the brief's §4 — the deliverable)

Five questions per item, in order, flatly. The fifth — *would our scaffolding have changed the outcome?* — is answered **no** in every case but one, and the one exception runs in the opposite direction to the one the brief was hoping for.

### 2.1 Applegate & Lagarias (2006) — the object that owns the name

**1. What object did they form?** The **multiplicative** semigroup `S_AL` of *positive rational numbers*, i.e. a sub-semigroup of `Q*_{>0}`, generated by `{n/T(n) : n ≥ 1}` — concretely by `2` together with `{(2k+1)/(3k+2) : k ≥ 0}`, so `S_AL = ⟨2, 1/2, 3/5, 5/8, 7/11, …⟩`. The generators are **point-ratios**: the ratio of an integer to its image. They depend on the integer `n`, not on a branch label. Farkas (2005) formed it; Applegate–Lagarias solved it.

**2. Relationship to `S`.** **Not the same object, not a quotient, and not the image of `S` under `α`.** Two facts settle it. First, `α(S) = {3^M/2^N : M ≥ 1, N ≥ M+1}` consists entirely of `{2,3}`-units (verified: `experiments/semigroup_priorart_check.py`), whereas `S_AL` contains `3/5`, `5/8`, `7/11`, … and, by Theorem 1.1, *every* positive rational with denominator prime to `3`. Second, the containment that does hold — `α(S) ⊊ S_AL`, since `3^M/2^N` has denominator `2^N` — is **vacuous**, because Theorem 1.1 makes `S_AL` essentially all of `Q_{>0}`; containment in it carries no information about anything.

The exact relationship, stated so it is not "similar in spirit": for a word `W` and a point `y` following it, `G^{|W|}(y)/y = A_W + B_W/y`. The Applegate–Lagarias-type object is built from the **secant** ratio `y/G^{|W|}(y)`; our `α` is the **derivative** `A_W`. They agree only in the archimedean limit `y → ∞`. Their generating set is indexed by *points*; ours by *branches*. These are two different homomorphic shadows of the same dynamics, neither a quotient of the other.

**3. What did they prove?** Theorem 1.1 (quoted in §1.1 above): `S_AL` is exactly `{a/b in lowest terms : 3 ∤ b}`; in particular it contains every positive integer, which is Farkas's weak `3x+1` conjecture, and it also settles Lagarias's Wild Numbers Conjecture. The proof is a see-saw induction on `k ≥ 12` over three simultaneous inductive hypotheses, computer-assisted (Tables 1–3 give multiplier certificates for residue classes mod 4096), closed with Rosser–Schoenfeld prime-counting inequalities.

**4. What stopped them?** They state it themselves, twice, and both statements are worth having verbatim. The structural one (p. 2):

> "The weak `3x+1` conjecture appears a potentially easier question to resolve than the `3x+1` conjecture, since the semigroup `S` permits some representations of integers as products of generators **not corresponding to `3x+1` iteration**."

That is the whole thing in the authors' own words: the semigroup is easier *because* it has forgotten which products are realized by actual orbits. It is not that they failed to extract the orbit information — they deliberately discarded it, and that discard is what made the problem tractable. Earlier on the same page they note that the argument which *would* keep the orbit information "would prove more, namely the `3x+1` conjecture itself. Since this problem seems out of reach, we considered a modification of this approach."

The technical one, from their §2 (pp. 4–5): the multiplier method eliminates every residue class mod `2^j` **except** `−1 (mod 2^j)`, and they prove this class can never be eliminated by that method —

> "a new method will be needed to handle integers in the 'bad' congruence class `−1 (mod 2^j)`, and it will be necessary to consider an infinite set of multipliers in `W`."

**5. Would our scaffolding have changed the outcome? No.** Their difficulty is not a shortage of exact local structure; it is that the object they chose is defined by throwing exact local structure away. Supplying the exact branching law, the stratum alphabet, the cylinder theorem or the whole-period height laws does not give them more multipliers in `W` — it re-imposes the realizability constraint whose removal is the only reason their theorem is provable. Moreover the specific classical input they lean on is already the cylinder fact in raw-bit form (they cite Lagarias's Theorem B: the first `j` steps are determined by `n mod 2^j`), which is precisely what our 14.15.1.5 is a coordinate change of. We have nothing to add to their toolkit that they were missing.

*One resonance, recorded because it is exact and then explicitly discounted.* Their intractable class is `−1 (mod 2^j)`; the one point at which our door coordinate's own formula fails is `y = −1 ∈ Z_2`, where `m(y) = v_2(y+1)` is undefined (`itinerary.md` 14.15.3(a), Remark), and `14.15.9.5` proves `−1` is never a member of a follower class. The agreement is not a coincidence — `−1` is the fixed point of `T` on the all-odd branch, so it is the accumulation point of integers with arbitrarily long non-decreasing runs in both frameworks. **This is a resonance, not leverage.** Theirs is a genuine proof obstruction about integers near `−1`; ours is a definitional edge case that 14.15.9.5 already disposes of. Nothing follows for either side, and no attempt is made here to make anything follow.

### 2.2 Farkas (2005) — the originator

**1. Object.** The same multiplicative strand: semigroups of positive rationals generated by specified infinite sets, e.g. `⟨{d(n)/n : n ≥ 1}⟩` (`d` = divisor function) and the `3x+1` one. **2. Relationship to `S`.** As §2.1: multiplicative, point-indexed, unrelated to `S` as a semigroup of maps. **3. Proved.** That `⟨{d(n)/n}⟩` represents exactly the positive odd integers; posed the `3x+1` case as open. **4. What stopped them?** Nothing stated as an obstruction — the paper poses the question; Applegate–Lagarias answered it. **5. Scaffolding?** No, for the reasons in §2.1; the question is one about representability in a multiplicative semigroup and has no orbit-order content to supply.

### 2.3 Caraiani (2010) — the decisive item for §5

**1. Object.** A family of multiplicative semigroups `S(A,B,C,D) = ⟨{(An+B)/(Cn+D) : n ≥ 0}⟩` in `Q*`, generalizing Farkas/Applegate–Lagarias to the `qx+1` problems; principally `W_q = ⟨{(qn + (q+1)/2)/(2n+1) : n ≥ 0} ∪ {1/2}⟩` for odd prime `q`. Note that the generators are **ratios of affine expressions**, but the semigroup remains **multiplicative in `Q*`**, not a semigroup of maps.

**2. Relationship to `S`.** None as objects, for the reason in §2.1. Its evidential relationship to our question is what matters, and it is decisive.

**3. What did they prove?** That `W_5[5,−1] = Q*` — the semigroup problem attached to the `5x+1` iteration has a **positive** answer — and general "largeness after finitely many extra generators" results for `S_q` under the hypothesis that `2` is a primitive root mod `q`.

**4. What stopped them?** Not a technical obstruction: a *proved insensitivity*, which the author states plainly (§1, p. 2):

> "The `qx + 1` conjecture is false in general. For example, it fails for `q = 5`, since the iteration starting at `13` goes through the cycle `13, 33, 83, 208, 104, 52, 26, 13` and never reaches `1`. … In this paper, we nevertheless prove that `W_5[5,−1]` is equal to `Q*`. Thus the semigroup problem associated to the `5x+1` problem has a 'positive' answer. Thus, our findings indicate that **the results of these semigroup problems shed no information on the truth or falsity of the `3x+1` problem, or the `5x+1` problem**."

This is the strongest single result in the sweep. It is not a heuristic that the multiplicative semigroup cannot see cycles — it is a **theorem-grade demonstration**: there is a case where a genuine non-trivial cycle exists, the conjecture is false, and the semigroup formulation nonetheless returns the same "positive" answer it returns for `3x+1`. The formulation is provably blind to exactly the phenomenon the cycle front is about.

**5. Would our scaffolding have changed the outcome? No, and the question is moot.** No amount of exact local structure rescues an object that has been proved insensitive to the distinction it would be asked to make. This is the cleanest "no" in the assessment.

### 2.4 Misiurewicz & Rodrigues (2005) — the closest object to `S`

**1. What object did they form?** The **semigroup of affine maps of `R_{>0}` generated by `T_0(x) = x/2` and `T_1(x) = (3x+1)/2`** under composition — the two raw affine branches of the Collatz map, decoupled from the parity condition that ordinarily decides which one applies. Ambient structure: `Aff(1,R)` acting on `R_+`, with words indexed by `⋃_n {0,1}^n` and `T_ω = T_{ω_{n−1}} ∘ … ∘ T_{ω_0}` (leftmost index applied **first** — the same order convention as `reverse.md` 14.14.8.2).

**2. Relationship to `S`.** **`S` is a sub-semigroup of theirs**, under an exact and verified identification:

```text
g_{m,r} = T_0^r ∘ T_1^m        (apply T_1 m times, then T_0 r times)
```

so the letter `(m,r)` is the word `T_1^m T_0^r` in their alphabet. This is not an analogy: `(3/2)^m · (1/2)^r = 3^m/2^{m+r} = α_{m,r}` and the composed offset is `((3/2)^m − 1)/2^r = (3^m − 2^m)/2^{m+r} = β_{m,r}`, matching `reverse.md` 14.14.4.1 term for term. It is also exactly what `14.14.7.1` already says in valuation-word form (`(m,r)` expands to the `T`-valuation word `(1,…,1,r+1)`), read one level further down into raw branches. Verified in `experiments/semigroup_priorart_check.py`: algebraically on the grid `m,r ≤ 12`, pointwise on 4,000 random rationals, and on all odd `y < 20,000` as honest Collatz blocks with integral images.

The differences that remain are real but are differences of *setting*, not of framing: (i) our alphabet is the **accelerated** one, so `S` is the sub-semigroup generated by the specific words `{T_1^m T_0^r : m,r ≥ 1}` rather than by `T_0, T_1` themselves; (ii) our ambient field is `Q` read `3`-adically (each generator a `3`-adic contraction of exact ratio `3^{−m}`), theirs is `R_+` with its archimedean metric; (iii) our questions are integrality and divisibility, theirs are topological.

**3. What did they prove?** (a) The semigroup generated by `T_0` and `T_1` **is free on two generators**. (b) Every orbit `{T_ω(x)}_{ω ∈ G}` is **dense** in `R_+` (their Cor. 3.2, quoted as "Theorem A" by Bergelson–Misiurewicz–Senti). (c) Periodic points are dense. (d) A full characterization of the **group** of homeomorphisms of the line generated by `T_0, T_1`: it consists of all maps `x ↦ 2^k 3^l x + m/(2^i 3^j)` with `k,l,m ∈ Z` and `i,j ≥ 0` — and **that group is not free**.

**4. What stopped them?** They do not state an obstruction, because they were not attempting the conjecture — and that is itself the finding, so it is reported rather than dressed up as one. The paper's own framing is that *instead of* choosing which map to apply according to the parity of `x`, one applies both independently of `x`. The realizability constraint is dropped at the outset, deliberately, and what is left is a clean, fully solvable object. The one technical limitation on record is stated by Bergelson–Misiurewicz–Senti, who observe that Misiurewicz–Rodrigues's Theorem 3.1 "cannot be generalized for all `T_0` and `T_1` … since it requires **rational independence of `log a` and `log b`**" — i.e. their proof leans on exactly the multiplicative independence of `2` and `3` that our `α` coordinate leans on.

**5. Would our scaffolding have changed the outcome? No — and here the direction of the "no" matters.** Their theorems are theorems about the *constraint-free* object. Our scaffolding is precisely the constraint: 14.15.1.5 says which single residue class mod `2^{S+1}` follows a given word; 14.15.9 says what the whole-period heights are. Handing them that does not strengthen density or minimality — it converts their tractable object back into the Collatz problem. There is nothing to add, because they were solving a different and deliberately easier question.

This is also where the closure lands hardest. Our `itinerary.md` 14.15.2 already records, by proof, that the itinerary language is the **full shift** — no forbidden word, no admissibility rigidity to find. Misiurewicz–Rodrigues's freeness theorem is the semigroup-theoretic face of that same fact, one alphabet down. Two independent literatures have now arrived at the same verdict: the word structure is free, and the entire content is in which words are *integrally realized* — the Bridge (`bridge.md` §16), unchanged.

### 2.5 Bergelson, Misiurewicz & Senti (2006)

**1. Object.** The free semigroup on two generators acting on `R_+` by one contracting and one expanding affine map with distinct fixed points, normalized to `T_0(x) = ax`, `T_1(x) = bx + 1`, `0 < a < 1 < b` — a direct generalization of Misiurewicz–Rodrigues, with `3x+1` the case `a = 1/2, b = 3/2`. **2. Relationship to `S`.** Same as §2.4, one level more general; our `S` is again a sub-semigroup of the `a=1/2, b=3/2` instance. **3. Proved.** Theorem B: every orbit dense in `R_+`. Theorems C, D, E: existence, uniqueness and description of invariant measures, governed by the Lyapunov exponent `λ(ν) = ν(C_0)ln a + ν(C_1)ln b`, with a measure existing iff `λ(ν) < 0`. **4. What stopped them?** Nothing stated as an obstruction to Collatz; the paper is not aimed at it. **5. Scaffolding?** No. Their content is invariant measures for a random affine recursion — **the parked statistical front, explicitly out of scope by the brief's forbidden list**. Recorded as a one-line pointer and dropped; no engagement, no statistics, no AEH connection drawn.

### 2.6 The general theory of affine semigroups (the brief's §3 lead 7)

This lead turned out to be the substantive one, and it is reported in more detail because the brief asked for the state of the general theory "insofar as it bears on `S`". The short version: **the theory is well developed for finitely many generators and essentially absent for countably many, and every criterion strong enough to decide freeness fails on `S` for a concrete, checkable reason.** That is a clean negative and is reported as one.

**1. What objects did they form?** Exactly ours, in the finitely generated case. Klarner (1982) studies the semigroup generated **under composition** by affine maps `f_i(x) = a_i x + b_i`, and gives sufficient conditions for freeness; he orders the generators by the fixed-point parameter `p_j = b_j/(a_j − 1)` — which is our `y^* = β/(1−α)` for a single letter — and observes that `p_j = p_{j+1}` forces `f_j`, `f_{j+1}` to commute, giving a relation. Kolpakov–Talambutsa (2022) redo and extend this via the **ping-pong lemma**. Since an affine map `ax+b` *is* the upper-triangular matrix `[[a,b],[0,1]]`, the algorithmic literature on freeness of matrix semigroups applies verbatim.

**2. Relationship to `S`.** `S` is an instance of precisely this class, with two differences that turn out to be exactly the differences that matter: our family is **countably infinite**, and our natural metric is **`3`-adic**.

**3. What did they prove?** Pinned:

- **Kolpakov–Talambutsa (2022).** Thm 1 (ping-pong): if all `a_i > 1`, with fixed points `s_1 < … < s_n` and `(s_n − b_i)/a_i ≤ (s_1 − b_{i+1})/a_{i+1}`, the semigroup is free. Thm 2: for two maps with `1/a + 1/c ≤ 1`, they either commute or generate a free semigroup. Thm 3: for positive **integer** multipliers with `Σ 1/a_i > 1`, **not** free. Finitely many generators throughout; no `p`-adic content.
- **Breuillard**, *On uniform exponential growth for solvable groups*, Pure Appl. Math. Q. **3** (2007), 949–967 (arXiv:math/0602076) — *journal volume/pages lightly confirmed via search metadata only, not the publisher page; treat as* **unconfirmed**. His Lemma 2.1 is the only **non-archimedean** affine ping-pong criterion found: over a non-archimedean local field, two affine maps with distinct fixed points and multipliers of absolute value `< 1` generate a free semigroup — the ultrametric inequality does the separation work for free. Two generators.
- **Decidability.** Freeness is undecidable for `3×3` integer matrices (Klarner–Birget–Satterfield, Int. J. Algebra Comput. **1** (1991), 223–226) and for `3×3` over `N`, even triangular (Cassaigne–Harju–Karhumäki, Int. J. Algebra Comput. **9** (1999), 295–305). But for **`2×2` upper-triangular rational matrices — that is, for two `Q`-affine maps — freeness is an open problem**, stated as such in the survey: J. Cassaigne, F. Nicolas, *On the decidability of semigroup freeness*, RAIRO Theor. Inform. Appl. **46** (2012), no. 3, 355–399, DOI [10.1051/ita/2012010](https://doi.org/10.1051/ita/2012010). It becomes decidable when products are restricted to bounded languages (É. Charlier, J. Honkala, *The freeness problem over matrix semigroups and bounded languages*, Inform. and Comput. **237** (2014), 243–256). *Caution, recorded: an erratum exists — J.-C. Birget, A. L. Talambutsa, Int. J. Algebra Comput.* **32** *(2022), no. 6 (page range* **unconfirmed***) — noting that the original `3×3` undecidability proof works for a symmetric variant of the Post Correspondence Problem but not for general PCP; undecidability survives via that route.* **Which of the two undecidability papers is being corrected was not resolved in this sweep** — read the erratum before citing either.
- **Infinite-alphabet IFS.** Mature in the Euclidean setting: R. D. Mauldin, M. Urbański, *Dimensions and measures in infinite iterated function systems*, Proc. London Math. Soc. (3) **73** (1996), 105–154, and their monograph *Graph Directed Markov Systems*, Cambridge Tracts in Math. **148**, CUP, 2003. Non-archimedean IFS is thin: K. G. Hare, T. Vávra, *Self-similar sets and self-similar measures in the `p`-adics* (arXiv:2307.07375; J. Fractal Geom., **volume/pages unconfirmed**), which appears to be finite-alphabet and dimension-theoretic rather than freeness-theoretic.
- **Nearest conceptual relative to the `α`-abelianization framing:** R. Aoun, K. Mallahi-Karai, *Random free semigroups of affine groups*, arXiv:2607.05219 (2026) — freeness of a *random* affine semigroup governed by an "abelian shadow", the projected walk on the multiplicative group of the multiplier. **Unpublished; abstract read only; do not cite specifics.** It is random, two-generator, and assumes a common linear part, so it is a relative and not an ancestor.

**4. What stopped them?** Nothing aimed at Collatz. The relevant statement is Lagarias's own, in the 2016 Monthly survey: several of Klarner's 1982 freeness problems **remain unsolved**. And the decidability record says the difficulty is real at the smallest scale — two `Q`-affine maps is already open.

**5. Would our scaffolding have changed the outcome? No — and here the flow runs the other way, so it is worth being precise about what the general theory does and does not give us.** Our scaffolding is about which integers realize which words; it has nothing to offer a question about abstract freeness. Conversely the general theory does not reach `S` either, for three checkable reasons (the last two verified in `experiments/semigroup_priorart_check.py`):

- **Klarner / Kolpakov–Talambutsa do not apply.** Their Thm 1 needs *all* multipliers `> 1`; ours straddle `1`, since `α_{m,r} = 3^m/2^{m+r} > 1` exactly when `r < m·log₂(3/2) ≈ 0.585m`, so both contractions and expansions occur. Thm 3 (non-freeness) needs **integer** multipliers, and `3^m/2^{m+r}` is never an integer. All are finitely generated.
- **Ultrametric ping-pong closes on finite sub-families but not on the whole alphabet.** Every generator has `|α_{m,r}|₃ = 3^{−m} < 1`, so Breuillard's criterion gives freeness of every finitely generated sub-semigroup with distinct fixed points. But every letter's fixed point `p_{m,r} = (3^m − 2^m)/(2^{m+r} − 3^m)` is a **`3`-adic unit** (verified, 225 checks), so the whole family's fixed points lie in the compact set `Z_3^×` and accumulate; `inf_j |p_i − p_j|₃ = 0`, and single-ball ping-pong cannot close on the infinite family.
- **Infinite-IFS separation fails at level one.** `S` *is* a genuine countable IFS of `3`-adic similarities, each of exact contraction ratio `3^{−m}`, so Mauldin–Urbański machinery is the right shape. But `g_{m,r}(Z_3) = β_{m,r} + 3^m Z_3`, and for fixed `m` two letters share that ball **exactly when `2·3^{m−1} | r′ − r`** (the multiplicative order of `2` mod `3^m`) — verified as an iff on the grid `m ≤ 6`, `r,r′ ≤ 40`, with the collision exhibited. So the open set condition is not available for the taking. *This is not evidence against freeness — distinct affine maps may share an image ball — only evidence that the standard separation route does not open by inspection.*

### 2.7 Kohl — the RCWA monoid, and a free monoid of rank 2 for `3n+1`

Two distinct items, both genuinely related, and the second is the most directly informative thing found about Q1.

**(a) `Rcwa(Z)` and `RCWA(Z)`.** **1. Object.** The **monoid** `Rcwa(Z)` of all `f : Z → Z` that are affine on each residue class mod some modulus `m`, under composition, and its group of units `RCWA(Z) < Sym(Z)`. Both the Collatz map and `T` lie in `Rcwa(Z)`. **2. Relationship to `S`.** Related but distinct in a specific way worth stating: `Rcwa` elements are **globally-defined piecewise-affine** maps, and `G` itself is such a map; `S` is generated by the **individual affine branches** of `G`, extended to global affine maps of `Q`. So Kohl's monoid is generated by whole maps, ours by their branches. Composing branches means *following an itinerary*, which is the IFS-style viewpoint, not the RCWA one. **3. Proved.** `RCWA(Z)` is not finitely generated, has finite subgroups of every isomorphism type, trivial centre, acts highly transitively on `Z`; tame/wild dichotomy by boundedness of the modulus of the `k`-th iterate, with surjective-not-injective RCWA mappings forced wild. **4. What stopped them?** Nothing claimed toward the conjecture; this is structure theory plus software (the GAP package `RCWA`). **5. Scaffolding?** No. Different question entirely.

**(b) The free monoid of rank 2 note (2007).** **1. Object.** Kohl builds an explicit pair of injective residue-class-wise affine maps `L, R : Z → Z` whose images partition `Z`, so that the binary tree they generate is complete, and defines `C` as **the free monoid of rank 2 generated by their restrictions to the positive integers**. **2. Relationship to `S`.** The same *kind* of object as `S` — a monoid of (piecewise) affine maps of the integers under composition, with words over a finite alphabet — differing in that his alphabet is engineered to rank 2 with `L, R` covering `Z` exactly, whereas ours is the countable stratum alphabet arising from the dynamics. **3. Proved.**

> **Theorem 4.2.** *The `3n+1` Conjecture is equivalent to the assertion that the mapping `γ : C → N, c ↦ c(1)` is bijective.*
> **Remark 4.3.** *It is obvious that the mapping `γ` … is injective. The problem is to show that it is surjective.*
> **Theorem 4.4.** *The `3n+1` Conjecture is equivalent to the assertion that the monoids `C` and `C_0 := ⟨n ↦ 2n, n ↦ 2n+1⟩` are conjugate in the full symmetric group `Sym(N)`.*

**4. What stopped them?** Nothing is claimed to be proved beyond the reformulation; the note is three pages and presents itself as a restatement. The content is entirely relocated into the surjectivity of `γ`.

**5. Would our scaffolding have changed the outcome? No — and this is the most useful "no" in the assessment, because of what it says about freeness.** Kohl already *has* a free monoid of affine branch maps attached to `3n+1`. Freeness is present, by construction, and it buys nothing: the whole difficulty moves intact into whether the word-to-integer evaluation map is onto. That is the same relocation our own 14.15.2/14.15.3(c) performs — free word space, all content in integral realization — reached independently and a decade earlier, in a different alphabet. Our scaffolding would add exact height and cylinder data to his words, but it would not make `γ` surjective, and nothing in his setup was blocked for want of that data.

**(c) The group-theoretic reformulation (2017).** **1. Object.** A group, not a semigroup: subgroups of `CT(Z) < Sym(Z)` generated by **class transpositions** (involutions interchanging two disjoint residue classes) — residue-class-wise affine *permutations*. **2. Relationship to `S`.** Distinct: invertible, involutive generators, no contraction. **3. Proved.** `G_T := ⟨τ_{0(2),1(2)}, τ_{1(2),2(4)}, τ_{1(4),2(6)}⟩` acts transitively on `N_0` **iff** the Collatz conjecture holds; plus an infinite series of finitely generated simple groups whose intersection is Thompson's group `V` (`CT_{2}(Z) ≅ Higman's G_{2,1}`). **4. What stopped them?** A reformulation, not an attack; no obstruction claimed. Kohl's Remark 2.3 is worth one line because it is a genuine negative: a comparison group `G_5` has a *finite* subset `S` such that every `n > 0` is decreased by some `g ∈ S`, whereas `G_T` provably has **no finite subset with that property**. That is a "no finite certificate" statement of the same family as our digit-budget observation (stage4.md §11.8.7.7) — noted as kindred, claimed as nothing. **5. Scaffolding?** No.

---

## 3. The brief's §5 hypothesis: **refuted**

> *The hypothesis under test:* "If the literature's `3x+1` semigroup is *multiplicative* (a sub-semigroup of `Q*`) while ours is *affine*, then theirs may be the image of ours under the multiplier homomorphism `α` — i.e. the abelianization, which forgets exactly the letter-order information in which the cycle question lives."

**Refuted, on two independent grounds. The second is the more important one.**

**Ground 1 — the identification is false.** `α(S) = {3^M/2^N : M ≥ 1, N ≥ M+1}`, every element a `{2,3}`-unit (verified, `experiments/semigroup_priorart_check.py`). The Applegate–Lagarias semigroup contains `3/5` among its generators and, by their Theorem 1.1, equals `{a/b : 3 ∤ b}` — so it contains every prime except `3`. `S_AL` is therefore not `α(S)`, not isomorphic to it, and not a quotient of it. The containment `α(S) ⊊ S_AL` does hold, but is uninformative for the reason given in §2.1: Theorem 1.1 makes `S_AL` so large that containment in it says nothing. The generating principles differ in kind — point-ratios versus branch-multipliers, secants versus derivatives — and no homomorphism carries one family to the other.

**Ground 2 — the premise misdescribes the literature.** The hypothesis is conditioned on "*if* the literature's `3x+1` semigroup is multiplicative … while ours is affine." That antecedent is false as a description of the field. There are **two** semigroup literatures attached to `3x+1`, and the affine one is the older and the closer:

- the **multiplicative** strand in `Q*` — Farkas 2005, Applegate–Lagarias 2006, Lagarias's wild/Wooley numbers, Caraiani 2010;
- the **affine** strand in `Aff(1,·)` under composition — Klarner 1981/1982/1988 in general, Misiurewicz–Rodrigues 2005 for the Collatz branches specifically, Bergelson–Misiurewicz–Senti 2006, Kolpakov–Talambutsa 2022, surveyed by Lagarias himself in the Monthly in 2016; with Kohl's RCWA monoid and his free monoid of rank 2 as a piecewise-affine cousin.

Our `S` is not a preimage of the first strand under any map. It is a **sub-semigroup of the second**, via `g_{m,r} = T_0^r ∘ T_1^m`. The hypothesis reached for a relationship across the gap between the two strands; the actual relationship is an inclusion *within* the strand the brief did not know was there.

**Two secondary corrections, both to §1 of the brief rather than to §5:**

- **`α` is not the abelianization.** It factors through it, but is far coarser. The abelianization of a free semigroup on the alphabet `A = {(m,r)}` is the free commutative semigroup `N^{(A)}` of infinite rank, which records the multiplicity of *every letter*. `α` collapses that to **rank 2** by recording only the totals `(M, S) = (Σ m_i, Σ(m_i + r_i))`. So `α` forgets not only letter order but almost all of the letter census too. The brief's operative claim — that `α` is blind to order and recovers only the totals — is correct and is stated correctly in its own §1; only the word "abelianization" is wrong.
- **`β` is not `R_0` up to normalisation.** The relation carries an additive shift as well as a scaling: `2^{S_P}·B_P = N_P` (`itinerary.md` 14.15.9.1), and `N_r + q = 2^{m_r} R_r` (the seam identity, `cycles.md` 12.6.1.1). So `β` determines `R_0` *given* `q`, but "up to normalisation" understates the relation.
- **The cocycle orientation in the brief is correct.** With the order convention "leftmost letter applied first" — `reverse.md` 14.14.8.2's own recursion `A_{i+1} = α_i A_i`, `B_{i+1} = α_i B_i + β_i` — one has `β(W·W') = α(W')·β(W) + β(W')`, exactly as the brief writes it. Checked, not assumed: the reversed convention fails on 2,997 of 3,000 random pairs (`experiments/semigroup_priorart_check.py`). Misiurewicz–Rodrigues and Bergelson–Misiurewicz–Senti use the same orientation (`T_ω = T_{ω_{n−1}} ∘ … ∘ T_{ω_0}`), so our convention agrees with the affine strand's.

**What survives, and is confirmed more strongly than proposed.** The intuition behind the hypothesis — that the known semigroup objects discard precisely the information in which the cycle question lives — is **correct**, and does not need the homomorphism to be true. It has better evidence than an analogy: Caraiani's `q = 5` result (§2.3) is a *proof* that the multiplicative semigroup formulation is insensitive to the existence of non-trivial cycles, since it returns a positive answer in a case where a cycle demonstrably exists and the conjecture is false. And Applegate–Lagarias say the same thing in prose about their own object: it is tractable *because* it "permits some representations of integers as products of generators not corresponding to `3x+1` iteration."

This also reproduces, from outside, a split the wiki already owns: `q = 2^{S} − 3^{M}` is `α`-data alone, and the `|q| = 1` mechanism is a finite spent stock (`cycles.md` 12.6.1.2, 12.6.1.3); the residual condition `q | R_0` is `β`-data, i.e. order-dependent. So "the open content sits in the `β` coordinate" is right — but it is right as a restatement of `cycles.md` 12.6.1.2, not as a discovery imported from the literature.

---

## 4. Search record (auditable)

Recorded so a later session does not repeat this blind. A well-documented negative on any angle is a result, not a gap.

**By object name.** `"3x+1 semigroup"`; `"weak 3x+1 semigroup conjecture"`; `Collatz + semigroup/monoid`; `Collatz + "free semigroup"`; `Collatz + "affine group"`, `"ax+b group"`; `Collatz + "iterated function system"`, self-affine, attractor, inverse branches; `residue-class-wise affine` / `RCWA`; `"free monoid" + 3n+1`.

**By author.** Applegate; Lagarias (publication list, preprints page, both annotated bibliographies, the 2021 Overview, the 2016 Monthly survey); Farkas; Wirsching; Matthews & Watts; Bernstein & Lagarias; Caraiani; Kohl; Misiurewicz; Rodrigues; Bergelson; Senti; Klarner; Klarner & Rado; Kolpakov & Talambutsa; Trümper; Breuillard; Cassaigne & Nicolas; Cassaigne–Harju–Karhumäki; Charlier & Honkala; Klarner–Birget–Satterfield; Birget & Talambutsa; Mauldin & Urbański; Hare & Vávra; Aoun & Mallahi-Karai; Shamazov & Talambutsa.

**Method note.** Two of the three sweeps were delegated in parallel (the Lagarias-bibliography sweep and the general-affine-theory sweep) and their returns were **not taken on trust**: every citation this file relies on was independently re-pinned against a Crossref record or an arXiv page fetched in this session, and two errors were caught that way — Kolpakov–Talambutsa reported as unpublished when it is in Proc. AMS, and the author name "Rodriguez" for "Rodrigues". Items that could not be re-pinned are marked **unconfirmed** in place.

**By mathematical content.** composition of affine maps; affine branches of the Collatz map; semigroup generated by branch maps; cocycle (**zero hits across all three Lagarias documents** — a clean negative); fixed-point denominator; `p_j = b_j/(a_j − 1)` as the freeness-relevant fixed-point parameter; parity words / prescribed parity word; sets of integers closed under affine maps; freeness criteria and ping-pong; counting distinct compositions.

**By general theory (lead 7).** freeness of matrix semigroups and its decidability (`2×2` vs `3×3`, integer vs rational, upper-triangular); the ping-pong lemma for semigroups; free sub-semigroups of solvable groups and the Tits alternative over local fields; `Aff(1,·)` over `Q` and over `Q_p`; infinite/countable-alphabet IFS and separation conditions (OSC, weak separation, generalized finite type); `p`-adic and ultrametric IFS, self-similar sets over local fields; random affine semigroups and "abelian shadow"; targeted searches on the literal generators `3^m/2^{m+r}` and `(3^m − 2^m)/2^{m+r}` — **nothing**. No source was found that forms `S` itself.

**Primary sources read in full or in substantial part.** Applegate–Lagarias arXiv:math/0411140 v2 (all 16 pp., including the references page, from which Farkas's citation was recovered); Caraiani, `semigroups.pdf` (opening 4 pp.); Kohl, the free-monoid note (all 3 pp.); Kohl, *The Collatz conjecture in a group theoretic context* (pp. 1–4); Bergelson–Misiurewicz–Senti (pp. 1–3); Lagarias bibliographies I and II and the Overview (full-text regex sweeps, via the delegated sweep). Bibliographic pinning via **Crossref API records** for Applegate–Lagarias, Caraiani, Farkas, Misiurewicz–Rodrigues, Klarner 1982, Bergelson–Misiurewicz–Senti; arXiv abstract pages for math/0411140, 2506.19115, 2105.09387.

**Obstructions hit, recorded not deleted.**
- ScienceDirect (both Applegate–Lagarias and Caraiani landing pages), Wiley, Hindawi and the AMS `proc` PDF all returned **HTTP 403**; the AMS-hosted Misiurewicz–Rodrigues PDF could not be read directly, so its theorem statements are taken from Bergelson–Misiurewicz–Senti's restatement (which quotes Cor. 3.2 as "Theorem A") plus Lagarias's bibliography annotation, **not** from the paper's own text. Flagged as such rather than presented as a direct reading.
- Trümper (2014) full text unobtainable (403 + Cloudflare); abstract only. See §1.5.
- Klarner (1982) full text not obtained; content from Lagarias's annotation plus Kolpakov–Talambutsa's abstract. **This is the largest remaining gap.**
- Matthews–Watts (1984) full text not obtained; abstract and keywords only.
- PDF fetches returned compressed streams unreadable by the fetch tool; the working route was to read the locally saved PDF directly, page by page. Recorded because it will recur.

**Angles tried that returned nothing.** No cocycle treatment anywhere in the `3x+1` literature. No treatment of an *infinitely generated* affine semigroup attached to Collatz. No non-archimedean/`p`-adic IFS treatment of the Collatz branches found. No source found that forms `S` itself, in the accelerated `(m,r)` alphabet.

---

## 5. Off-brief observations

**Logged and stopped, per the brief's §7. Not developed, not verified beyond what is stated, and not to be treated as results.**

- **On Q1 (freeness of `S`).** The embedding `g_{m,r} = T_0^r ∘ T_1^m` places `S` inside a semigroup that Misiurewicz–Rodrigues prove is free on `{T_0, T_1}`. A sub-semigroup of a free semigroup generated by a set of words is free on those words exactly when the set is a code. So Q1 appears to reduce to a question about the word set `{T_1^m T_0^r : m,r ≥ 1}` in a free monoid on two letters — elementary combinatorics on words rather than number theory. **I have not carried this out and am not asserting the answer.** Two things bear on the recommendation, though. First, this route matters *because* the direct routes are blocked: §2.6 records that Klarner's and Kolpakov–Talambutsa's criteria do not apply to `S`, that ultrametric ping-pong cannot close on the infinite family (the fixed points accumulate in `Z_3^×`), that IFS separation fails at level one, and that freeness for even two `Q`-affine maps is a stated open problem. Borrowing Misiurewicz–Rodrigues's theorem sidesteps all of that. Second, per §2.4 and §2.7(b), a positive answer would be the semigroup-theoretic restatement of the full-shift verdict `itinerary.md` 14.15.2 already proves — a citation-grade closure, not new content.
- **On the shape of the whole framing.** Three independent constructions — Applegate–Lagarias's multiplicative semigroup, Misiurewicz–Rodrigues's free affine semigroup, Kohl's free monoid of rank 2 — all do the same thing: drop the realizability constraint, obtain a clean and fully solvable object, and relocate the entire difficulty into a single surjectivity/realization question. Our 14.15.2/14.15.3(c) is the fourth instance. That the pattern is this robust is itself the argument that the semigroup framing is a reformulation device, not a lever.
- **On Q3 (the unbounded-length limit).** Nothing found bearing on it, and no opinion formed. The nearest literature (Bergelson–Misiurewicz–Senti's invariant measures) is on the forbidden statistical front and was not pursued.

---

## 6. What this changes, and what it does not

**What it changes.** Nothing that is proved, and nothing on any page. It creates **one citation obligation and one framing correction**, both for the main session to place if it chooses:

1. If the semigroup framing is ever written up, `S` must be introduced as a **sub-semigroup of the Misiurewicz–Rodrigues semigroup**, with `g_{m,r} = T_0^r ∘ T_1^m` stated, and with Klarner (1982) / Kolpakov–Talambutsa (2022) cited for the general freeness theory and **Lagarias (2016)** for the fact that this circle of questions is an established part of the `3x+1` literature. Claiming the affine-semigroup framing as unexplored would be a register violation of exactly the kind `publication.md` already guards against for 14.15.1 ("explicitly not novel; claim only the coordinate change"). The same verdict applies here, and for the same reason.
2. The name **"the `3x+1` semigroup" is taken**, by Applegate–Lagarias's multiplicative object. Ours must not be called that. If it needs a name, it should be named for the branch composition, and distinguished from `S_AL` explicitly.
3. `publication.md`'s standing pre-submission item — "sweep Lagarias's bibliographies for anchor-like coordinates" — is **partially discharged** by this pass for the semigroup/affine/IFS angles specifically. It is not discharged for anchor-like coordinates, which were not the object of this sweep.
4. One genuine gap in the literature is worth recording without being claimed as ours: no source was found treating an **infinitely generated, deterministic, non-archimedean** affine semigroup. Every freeness criterion located is finitely generated, the one `p`-adic criterion is two-generator, and the infinite-alphabet IFS theory is Euclidean. That is a gap in the general theory, not a result of ours, and it should be stated as a gap if it is stated at all — `S` being an instance of an under-theorized class is not the same as `S` being new mathematics.

**What it does not change.** The parked cycle front stays parked; nothing here is a divisibility-aware idea and nothing here excludes a single cycle. The long-range AEH front is untouched — the one place the sweep brushed it (Bergelson–Misiurewicz–Senti's invariant measures, Peres–Simon–Solomyak on Sinai's question) is on the forbidden list and was recorded in one line and dropped. The Bridge (`bridge.md` §16) is exactly as open as it was: indeed the sweep's main effect is to confirm, from outside and independently, that the Bridge is where the difficulty sits, since three separate literatures relocate their difficulty to the same place. `itinerary.md` 14.15.2's full-shift verdict and 14.15.3(c)'s formulation of the Bridge in symbolic form both stand unaltered and are, if anything, better corroborated.

**Recommendation on a second round for Q1 and Q3.** **Q1: worth one short pass, as a citation-and-closure task, not as a lever.** The reduction sketched in §5 suggests it is cheap, and settling it lets the framing be written down correctly or dropped cleanly; but the expected payoff is a restatement of 14.15.2, and it should be commissioned with that expectation stated so the session does not go looking for leverage that §2.4 and §2.7(b) indicate is not there. **Q3: not worth a round now.** Nothing in the sweep bears on it, the nearest literature is on the parked statistical front, and the two-sided coding it would refine is already recorded at 14.15.3 as formulation-grade only. If the main session wants one more literature action, the higher-value one is closing this pass's largest gap — obtaining the full text of **Klarner (1982)** and of **Misiurewicz–Rodrigues (2005)**, both of which are currently cited from annotations and restatements rather than from their own pages, and of **Lagarias (2016)**, which is the natural single citation for the whole affine strand and was pinned here from its Crossref record rather than read. Secondary: resolve which paper the **Birget–Talambutsa erratum** corrects, before any of the undecidability results is cited.
