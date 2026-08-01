# Findings: Thomas (2017) proves a non-uniformity **bound**, not a law — no contact with `13.6.3`(v) or `13.6.4` (v3 round 2, closing Tao's footnote)

**Task:** `briefs/v3r2-thomas-check-brief.md`. Read-only round; the only file written is this one.
**Read at:** `main` = `e4dac49`.

**Grades, used on every claim below.**

* **[P]** — *verified-primary.* Read by me, this session, from the source document itself.
* **[S]** — *secondary-description.* Someone else's description of a source I did not read.
* **[C]** — *computed by me* this session, exact rational arithmetic (`fractions.Fraction`), no floating point in any comparison that decides anything.
* **[?]** — *unconfirmed.*

**What I obtained, stated first.** I have **the author's own LaTeX source**, not a rendering, a review, or a summary. Thomas posted the paper as `arXiv:1512.05852`; `v2` (9 Nov 2016) is the accepted manuscript, and I read all 472 lines of it. Sourcing succeeded outright — the brief's fallback to reviews was not needed.

---

## 0. Verdict

**(a) Thomas exhibits no limiting law at all, so there is nothing that could be our `ν` or Tao's `Syrac`. [P]**

This is not a near-miss that fails a numerical comparison, as Wirsching's did. It is a category difference. The words *measure*, *Haar*, *Markov*, *stationary*, *invariant*, *random*, *probability*, *equidistribution*, *converges* and *`p`-adic* **do not occur anywhere in the paper**. (The single case-insensitive hit for "adic" is the word "contr**adic**t".) **[P + C]** There is no measure on `Z_3`, no process, no stationary law, no distribution of any kind. The brief anticipated extracting low-level values and comparing them against `ν_1 = (0, 2/3, 1/3)` and `13.6.5`'s `2/3, 19/63, 2/63`. **There are no such values in the paper to extract.**

What Thomas proves is a **counting bound that rules out near-uniformity**, with no candidate for what the true distribution is. His only numbers are (i) the threshold `1/6 + 0.0215`, which is an optimisation artifact tuned so that his entropy exponent lands at `0.9998 < 1`, (ii) the integer weights `(2,1,0,3,2,3)`, and (iii) a 26-orbit toy tally in a remark.

**(b) Direction of the result: it points *with* the record, not against it, and it is strictly weaker.** **[C]**

Thomas's object — the empirical frequencies of one orbit over `I = {1,5,7,11,13,17} mod 18` — is, once decoded, the empirical distribution of the forward Syracuse orbit over the **units of `Z/9Z`**, because every element of `I` is odd and `(Z/18Z)^× = {1} × (Z/9Z)^×`. That is exactly level two of the object `13.6.5` and Tao are about. Its conjectural limit, under the record's own hypothesis, is `Syrac(Z/9Z)` on the units. Setting the two side by side in exact arithmetic:

```text
i mod 18                :   1      5      7     11     13     17
conjectural limit       : 8/63   4/63   2/63  16/63  11/63  22/63     (= Syrac(Z/9Z))
Thomas's threshold      : all six would have to be <= 1/6 + 0.0215 = 1129/6000
max is 22/63 = 0.3492  >  1129/6000 = 0.18817     (132000 > 71127)
```

So the law the record asserts **implies** Thomas's conclusion, with room to spare — indeed the **level-one** law alone suffices: `Syrac(Z/3Z) = (0, 1/3, 2/3)` puts `2/3` on three of the six cells, so pigeonhole forces a cell of frequency `≥ 2/9`, and `2/9 > 1129/6000` (`12000 > 10161`). **[C]** Thomas proves rigorously, by a completely different method, a far weaker shadow of what §13 asserts exactly.

**(c) `13.6.3`(v) — NOT COVERED. `13.6.4` — NOT COVERED. No citation is owed. [P]**

`13.6.3`(v) needs a `2`-adic residue variable and a depth `d = m + a` with `m ⊥ a`. Thomas has no `2`-adic variable: the `18` in "mod 18" contributes only the parity bit, and on `⊓` that bit is the constant `1`. Verified: the six classes of `I` are distinct mod `9` and the map `I → (Z/9Z)^×` is a bijection, so **"mod 18" carries exactly the mod-9 data and nothing more**. **[C]** No depth, no valuation law, no independence claim, no product measure.

`13.6.4` is an *equivalence between two genericity conditions on a single orbit*, with no measure on starting values. Thomas's theorem quantifies over starting values *by density*, concerns one 6-cell statistic at one fixed level, proves a negative rather than an identification, and neither implies nor is implied by either side of `13.6.4`.

**(d) He is nonetheless worth citing, for the same reason Wirsching was, and a better one.** He is the second name in Tao's footnote; a referee will follow it. And his result is a rigorous strike against exactly the alternative the Wirsching round distinguished us from — **uniformity in the `3`-direction**. Saying so is to the paper's credit. Drafted at §6.

**(e) One genuine and rather pretty point of contact, which is not prior art.** Thomas's admissibility table `(cases)` **is exactly the support of Tao's Lemma 1.12 recursion** at level `9`, verified cell by cell. He counts those branches; Tao and we weight them by `2^{-a}`. **This is the same "count vs. weight" split that cleared Wirsching, appearing a second time in a second paper** — and here the two uses even agree on which residue is rarest. §5.

---

## 1. Primary source, obtained

```text
https://arxiv.org/e-print/1512.05852
  -> thomas.tar.gz        sha256 efd7d47fe26f24158433567025bad191d101167247558db29ab9702d11ae28ce
  -> 3x+1_revised.tex     sha256 88013daa44ff3836c1ed36d598bb08ecdefe1c6d3e38ec84a4abcaa44d0080e9
                          27,347 bytes, 472 lines, archive mtime 2016-11-09
  -> OAB.pdf              sha256 fe5c4aa3c15a2c161ed85bc4c654bf20526cc2f9718247aff1fb8e9532487362
                          (a figure: the triangle OAB of Appendix B)
```

`amsart`, `b5paper`, `\usepackage[applemac]{inputenc}` (the file is Mac Roman, not UTF-8). Author: Alain Thomas, Aix-Marseille University / I2M, address Plan d'Aups Sainte Baume. Dedicated to the memory of Pierre Liardet. **[P]**

**Version and publication, cross-checked three ways. [P]**

| | |
|---|---|
| arXiv abs page | v1 18 Dec 2015, **v2 9 Nov 2016**; journal-ref "Acta Arithmetica (to publish)"; MSC 11B37, 11A99, 11B83 |
| Publisher (impan.pl, ToC of vol. 178 no. 2) | *A non-uniform distribution property of most orbits, in case the `3x+1` conjecture is true*, Alain Thomas, **pp. 125–134**, DOI **10.4064/aa8385-9-2016** |
| Publisher article page (via DOI) | same title/author/volume/pages; **MSC 11B37, 11A99, 11B83 — identical to the `\subjclass` line in the tex** |

The DOI suffix encodes acceptance in **9-2016**, which *precedes* the v2 posting of Nov 2016; the page span `125–134` is 10 pages, matching the tex's length; and the MSC triple matches the source exactly. I therefore treat **arXiv v2 as the accepted manuscript**. I did not obtain the published PDF (Acta Arithmetica is paywalled) and did not compare it line by line — see §7.1. **[P for the three rows; the identification of v2 with the print version is [P]-corroborated but formally [?]]**

**Tao's own bibliography entry, read from his source this session** (`collatz.tex` L1944–1946), matches the brief's citation to the letter: **[P]**

```latex
\bibitem{thomas}
A. Thomas, \emph{A non-uniform distribution property of most orbits, in case the $3x+1$ conjecture is true},
Acta Arith. \textbf{178} (2017), no. 2, 125--134.
```

(`tao.tar.gz` sha256 `ba81acd6…`, `collatz.tex` sha256 `bfbc3943…` — a **third** independent reproduction of the hashes in `briefs/v3r2-syrac-identity-findings.md` §1 and `briefs/v3r2-wirsching-check-findings.md` §1.)

**And Tao's footnote clause about Thomas is weaker still than the Wirsching clause.** Verbatim, `collatz.tex` L393, the footnote in full: **[P]**

> This Markov process may possibly be related to the `3`-adic Markov process for the *inverse* Collatz map studied in [wirsch]. **See also a recent investigation of `3`-adic irregularities of the Collatz iteration in [thomas].**

The Wirsching clause at least hedges a relation ("may possibly be related to"). The Thomas clause asserts **no relation at all** — it is a bare "see also" pointing at related reading. Having now read Thomas, that is exactly right, and the description "`3`-adic irregularities" is a generous gloss: Thomas's paper is not `3`-adic in any technical sense, it works with residues mod `18` and never completes anything.

---

## 2. What Thomas proves, verbatim **[P]**

The paper has one theorem. Verbatim from the source (line 81–99), notation preserved:

> **Theorem.** We put
> `O_n := {m ∈ Z : ∃k ≥ 0, m = T^k(n)}` (orbit of the integer `n`),
> `c_i(n) := #{m ∈ O_n : m ≡ i mod.18}` (finite or infinite),
> `I := {1,5,7,11,13,17}`,
> `W := { n ∈ Z : ∃k ≥ 0, T^k(n) = 1 and ∀i ∈ I, c_i(n)/Σ_{i∈I} c_i(n) ≤ 1/6 + 0.0215 }`.
> We have for any `N` large enough
> `#W ∩ {1,…,N} ≤ N^{0.9999}`.

Here `T(n) = 3n+1` for `n` odd, `n/2` for `n` even, on `Z`. Note `O_n` is a **set**, so `c_i` counts *distinct orbit elements*, not visits.

The abstract's corollary, verbatim: "*We prove that `W ∩ N` has density `0` in `N`. Consequently, if the `3x+1` conjecture is true, most of the positive integers `n` satisfy `max_{i∈I} c_i(n) / Σ_{i∈I} c_i(n) > 1/6 + 0.0215`.*"

**What is assumed and what is concluded, precisely.** The theorem itself is **unconditional**. The `3x+1` conjecture enters *only* to make the clause "`∃k, T^k(n) = 1`" in the definition of `W` vacuous, so that "density `0` among integers that reach `1`" upgrades to "density `0` in `N`", i.e. so that "most" means what one wants it to mean. The title's conditional is doing that and nothing else. **[P]**

**The method.** Thomas says it himself (L103): "*To prove this theorem we use the same method as Krasikov and Lagarias [Kr], it consists in describing the set of the antecedents of `1` by the powers of `T`.*" He works with Sinai's accelerated map `S : ⊓ → ⊓`, `S(n) = (3n+1)/2^k`, on `⊓ = {n odd, n ∉ 3Z} = {1,5,7,11,13,17} + 18Z`, builds a bijective index `n : (N∖{1}) × N^{α−1} ↔ ⊓_α` for the `α`-th preimage layer of `1`, derives the lower bound (his eq. `(lb)`)

```text
n(i_1,…,i_α) >= 2^{3(i_1+…+i_α) − c(n(i_1,…,i_{α−1})) + α'} / (α 3^α),
c(n) := 2c_1(n) + c_5(n) + 3c_11(n) + 2c_13(n) + 3c_17(n),
```

and closes with a multinomial/entropy optimisation (`φ(x,y)` on a triangle, Appendices A–B) whose maximum he computes numerically as `w_0 − 0.9998 ∈ (0, 10^{-4})`. **[P]**

**The `0.0215` is an artifact of that optimisation, not a distributional quantity.** The weights sum to `11` (`2+1+0+3+2+3`), so near-uniformity caps `c(n) ≤ 11(1/6 + 0.0215)·#{odd elements}` (his eq. `(c(n))`), which is what feeds the exponent. The constant is chosen to make `w_0 < 1` by a hair. It carries no information about any limiting law. **[P + C]**

---

## 3. What his object actually is: "mod 18" is "mod 9 on units"

`I = {1,5,7,11,13,17}` are the units of `Z/18Z`, and all are odd. Since `18 = 2 · 3^2` and `(Z/2Z)^×` is trivial,

```text
(Z/18Z)^x  =  {1} x (Z/9Z)^x ,     |(Z/9Z)^x| = 6.
```

Reducing: `1,5,7,11,13,17 mod 9 = 1,5,7,2,4,8` — a bijection onto `(Z/9Z)^× = {1,2,4,5,7,8}`. **[C]**

**So Thomas's statistic is the empirical distribution of the forward Syracuse orbit at `3`-adic precision `9`, and the "2" in `18` contributes nothing.** This matters because `mod 18 = 2 × 9` is precisely the shape a referee might mistake for a joint `2`-adic × `3`-adic object of `13.6.3`(v)'s kind. It is not one; the `2`-part is a constant on `⊓`. Stating this explicitly is the cheapest way to foreclose that misreading.

**The correct comparison target is `Syrac`, not `ν`.** Thomas counts *every* Syracuse orbit point. Our `y_3`/`ν` is the door coordinate, which per `briefs/v3r2-syrac-identity-findings.md` §5.2 is Tao's chain **observed at renewal times** — the Syracuse points immediately after an exponent `≥ 2`. That subsampling is exactly the `×2^{-1}` Palm tilt. So a full-orbit frequency has conjectural limit `Syrac(Z/9Z)`, while `ν_2` is its renewal-tilted cousin; comparing Thomas's cells against `ν_2` directly would be off by the unit `2`. Recorded because it is an easy error to make.

Reproduced this session before any comparison, exactly: **[C]**

```text
Tao Syrac(Z/3Z) : 0, 1/3, 2/3                                          -- matches his printed line
Tao Syrac(Z/9Z) : 0, 8/63, 16/63, 0, 11/63, 4/63, 0, 2/63, 22/63       -- matches his printed line
repo nu_1       : 0, 2/3, 1/3          (experiments/aeh_symbolic.py::nu_exact, imported unmodified)
repo nu_2       : 0, 16/63, 11/63, 0, 22/63, 8/63, 0, 4/63, 2/63
nu_j(x) == Syrac(2x mod 3^j) at j = 1, 2                               -- confirmed
```

Transported to Thomas's index set:

```text
i mod 18        :    1      5      7     11     13     17
Syrac on I      :  8/63   4/63   2/63  16/63  11/63  22/63     (sums to 1)
                                  ^min                  ^max
```

---

## 4. The five questions, answered

### Q1 — What does Thomas prove?
§2. **[P]** A counting theorem: among integers whose orbit reaches `1`, those whose mod-`18` frequencies over `I` are *all* below `1/6 + 0.0215` number at most `N^{0.9999}` up to `N`. Assumed: nothing (the `3x+1` conjecture only removes the reachability clause). Concluded: a density-`0` upper bound. About: the empirical residue frequencies of individual finite forward orbits.

### Q2 — Is his non-uniform distribution law our `ν` / Tao's `Syrac`?
**No, and not because of a numerical disagreement — because there is no law.** **[P]** The paper exhibits no limiting measure, on `Z_3` or `Z_3^×` or anywhere else. The brief's decisive test ("a level-one disagreement settles it negatively; agreement at levels one *and* two is strong evidence") cannot be run, because Thomas prints no level-one or level-two values. His theorem is compatible with a large family of limiting laws — every law whose maximum on the six cells exceeds `1129/6000` — of which `Syrac|units` is one.

The one comparison that *can* be made is the converse one, and it is favourable: **[C]**

```text
Thomas's threshold  1/6 + 0.0215 = 1129/6000
Syrac max on I      22/63           > 1129/6000     (132000 > 71127)   -> his conclusion holds
level-one alone     max cell >= 2/9 > 1129/6000     ( 12000 > 10161)   -> already sufficient
his weight cap      11*(1/6+0.0215) = 12419/6000  vs  Syrac value  Sum w_i p_i = 52/21
                                    ~ 2.06983     vs                ~ 2.47619   -> exceeded
                    (uniform value would be 11/6 ~ 1.83333)
```

### Q3 — Does he predate Tao as the correct primary attribution for `13.6.5`?
**Moot, and no.** **[P]** He is two years earlier in print, but he does not contain the law, does not construct any measure, and does not treat the `2^{-a}`-weighted process. `briefs/v3r2-syrac-identity-findings.md` §9.1–9.3's drafted attribution, naming **Tao alone**, stands unchanged and needs no second source. Both names in Tao's footnote have now been checked and neither displaces him.

### Q4 — Does he bear on `13.6.3`(v) or `13.6.4`?
Answered separately from Q2, as the brief required.

**`13.6.3`(v) — no.** **[P for each left column; the coverage judgement is my inference from them]**

| `13.6.3`(v) needs | Thomas has |
|---|---|
| a `2`-adic residue `ω mod 2^{k+2}` | nothing `2`-adic; his mod-`18` classes reduce to mod-`9` classes with a constant parity bit (§3) |
| Haar-odd conditional law of the door given the past | no conditional laws; no measure |
| `m_n` geometric(1/2) | the exponents `ε_j` appear, but only through the *support* constraint `(cases)` and an unweighted index `i ∈ N`; no law on them |
| absorption `a = v_3(y+1)` with law `2/3, 19/63, 2/63` | no valuation variable, no `3`-adic law |
| independence of `ω`-residue from depth | no two variables to be independent |
| a product/renewal decomposition | a multinomial counting bound |

**`13.6.4` — no.** The two statements differ in every structural dimension: **[P + inference]**

| | `13.6.4` | Thomas |
|---|---|---|
| quantifier | **orbit by orbit**, "no measure on starting values is invoked" | over starting values, by **density in `N`** |
| logical form | an **equivalence** between two genericity conditions, both unproved | a one-directional **upper bound** on an exceptional set |
| statistic | full window-state block process, every `k` and `L`, with `2`-adic residue and depth | one 6-cell frequency vector at one fixed level |
| content | a positive **identification** with an explicit product law | a negative: near-uniformity fails |
| method | symbolic dictionary + finite-window reconstruction | backward-tree counting (Krasikov–Lagarias) + entropy optimisation |
| status | hypothesis-grade on both sides | **theorem** |

Neither implies the other. Thomas is not prior art for `13.6.4`, and `13.6.4` does not subsume Thomas (his is a rigorous theorem where ours is an equivalence between hypotheses).

**But there is a real relation, worth recording and worth saying in the paper.** Under AEH, `13.6.4`'s equidistribution forces the mod-`9` frequencies to `Syrac|units`, whose maximum `22/63` clears Thomas's threshold — so **Thomas's conclusion is a weak consequence of what the record asserts, made unconditional and proved by other means.** Equivalently: the natural rival hypothesis, that Collatz orbits equidistribute *uniformly* over the admissible residues (Haar in the `3`-direction — exactly Wirsching's regime), is now **refuted for a density-`1` set of starting integers, rigorously.** That is a rigorous strike in the record's favour, and it is the only one this round has found.

### Q5 — Should he be cited regardless?
**Yes — not owed, but worth it, on the Wirsching pattern.** He is the second name in Tao's footnote; the paper now cites Remark 1.13, so a referee has a signposted path to him. One `\bibitem` and two sentences convert an obvious question into a demonstration that the distinction is understood, and the answer happens to be flattering. Drafted at §6.

---

## 5. The one genuine point of contact: his `(cases)` table is Tao's support, counted rather than weighted

Thomas's eq. `(cases)` records which backward exponents are admissible from each residue: **[P]**

```text
n_j = 1 mod 18  ->  eps in {2,4} mod 6        n_j = 11 mod 18 ->  eps in {1,3} mod 6
n_j = 5 mod 18  ->  eps in {3,5} mod 6        n_j = 13 mod 18 ->  eps in {2,6} mod 6
n_j = 7 mod 18  ->  eps in {4,6} mod 6        n_j = 17 mod 18 ->  eps in {1,5} mod 6
```

It comes from requiring `(2^ε n_j − 1)/3 ∈ ⊓`, i.e. `2^ε n_j ≡ 1 (mod 3)` and `≢ 1 (mod 9)`. I reproduced all six rows from scratch. **[C]**

**This is exactly the support of Tao's Lemma 1.12 recursion at level `9`.** Tao's sum ranges over `a` with `2^a x ≡ 1 (mod 3)`; his extra exclusion is enforced automatically, because `Syrac` vanishes on multiples of `3`, so the summand dies there. Verified cell by cell, and the level-`9` masses recomputed *through that support* reproduce Tao's printed line exactly: **[C]**

```text
i mod18 | x mod9 | Tao a-classes with nonzero summand | Thomas (cases) | min a | Syrac(x)
      1 |      1 |                             [2, 4] |         [2, 4] |     2 |  8/63
      5 |      5 |                             [3, 5] |         [3, 5] |     3 |  4/63
      7 |      7 |                             [4, 6] |         [4, 6] |     4 |  2/63
     11 |      2 |                             [1, 3] |         [1, 3] |     1 | 16/63
     13 |      4 |                             [2, 6] |         [2, 6] |     2 | 11/63
     17 |      8 |                             [1, 5] |         [1, 5] |     1 | 22/63
```

**And the two uses of that one table agree on which residue is rarest.** Thomas's Remark observes empirically that `c_7` is smallest and says his proof shows why: residue `7 mod 18` forces `ε ≥ 4`, the largest floor of the six, so the backward tree grows fastest through it and such integers are scarcer below `N`. Under the `2^{-a}` weighting the *same* table makes `Syrac(7) = 2/63` the smallest mass. Grouping by minimal admissible exponent, the `Syrac` masses are **strictly separated between groups, monotonically decreasing**: **[C]**

```text
min eps = 1 : i=11 -> 16/63,  i=17 -> 22/63
min eps = 2 : i= 1 ->  8/63,  i=13 -> 11/63
min eps = 3 : i= 5 ->  4/63
min eps = 4 : i= 7 ->  2/63
```

**This is the round's "count vs. weight" split appearing a second time, in a second paper.** Wirsching's kernel weighted its inverse branches uniformly because he was counting predecessors, and got Haar. Thomas indexes his admissible exponents `1, 2, 3, …` with no weight at all, because he too is counting the backward tree, and gets a counting bound. Tao and `13.6.5` weight the same branches by `2^{-a}`, because they are measuring a typical orbit, and get a law. Same elementary table; different arithmetic on top of it; different genre of conclusion. **Nothing to attribute — the table is the definition of `⊓` plus `ord(2 mod 9) = 6`, elementary and classical.**

*(For completeness, since the shape can mislead: `(cases)` is a deterministic link between a `3`-adic residue and a `2`-adic exponent, which might look like it threatens `13.6.3`(v)'s independence claim. It does not. `13.6.3`(v) asserts that `(m_n, q_n)` is independent of the **past**; `(cases)` constrains the exponent by the residue of the **image**, i.e. it is the transition kernel itself, and appears identically inside Tao's Lemma 1.12. No tension.)* **[P + inference]**

**Honest note on his numerical remark.** Thomas's tally over the orbits of `n = 1,…,26` is `(c_1,c_5,c_7,c_11,c_13,c_17) = (28,22,5,10,11,13)`. The **argmin agrees** with `Syrac` (both at `7`), but the full ordering does not — his `c_1` is largest where `Syrac` ranks `1` second-smallest. This is not a disagreement of substance: 26 tiny orbits are dominated by the endgame near `1`, and he offers the tally as an illustration, not as an estimate. Recorded rather than suppressed. **[P + C]**

---

## 6. What the record should say

### 6.1 `aeh.md` — nothing owed, nothing to change

No sentence in `aeh.md` is falsified, weakened, or made to owe attribution by this paper. `13.6.5` keeps the Tao attribution drafted at `briefs/v3r2-syrac-identity-findings.md` §9.3; `13.6.3`(v) and `13.6.4` keep everything.

### 6.2 The `\bibitem` — verified against three sources

Byte-identical to Tao's own entry (§1), and independently confirmed against the publisher's ToC and article page. **[P]**

```latex
\bibitem{thomas} A.~Thomas, \emph{A non-uniform distribution property of most
  orbits, in case the $3x+1$ conjecture is true}, Acta Arith.\ \textbf{178}
  (2017), no.~2, 125--134; arXiv:1512.05852.
```

### 6.3 Related work — drafted, to sit immediately after the Wirsching paragraph of `briefs/v3r2-wirsching-check-findings.md` §4.3

Uses only `\Z`, which exists in the tex; `Syrac` is spelled out, as there is no macro for it.

```latex
Tao's footnote names a second paper, and it points the other way. Thomas
\cite{thomas} studies the empirical distribution of a single Collatz orbit over
the six residue classes $\{1,5,7,11,13,17\}$ modulo $18$ --- equivalently, since
all six are odd, over the units of $\Z/9\Z$ --- and proves that the integers
whose orbit reaches $1$ with all six frequencies below $\tfrac16 + 0.0215$ have
counting function at most $N^{0.9999}$; granted the $3x+1$ conjecture, most $n$
therefore have some class frequency above that threshold. He constructs no
limiting measure and identifies no law: the argument counts the backward tree of
$1$ in the manner of Krasikov and Lagarias. The law recorded here says much more
and implies his conclusion --- the predicted frequencies are
$\tfrac{8}{63},\tfrac{4}{63},\tfrac{2}{63},\tfrac{16}{63},\tfrac{11}{63},
\tfrac{22}{63}$ at $1,5,7,11,13,17$, being $\mathrm{Syrac}(\Z/9\Z)$ on the
units, and even the level-one law $(\tfrac13,\tfrac23)$ already forces a class of
frequency at least $\tfrac29 > \tfrac16 + 0.0215$. Read together with Wirsching,
the two references bracket the point: uniformity in the $3$-direction is what a
predecessor count produces, and Thomas shows rigorously that Collatz orbits do
not exhibit it.
```

### 6.4 `publication.md` — one optional addition, no correction

Nothing on that page is wrong about Thomas, because nothing on that page mentions him: `git grep -in thomas` over the whole repository returns only *Cover–Thomas*, a different reference, in four brief files and one script; `mod 18` appears nowhere in any tracked file. **[C]** If the L21 bullet is being rewritten anyway (the Wirsching round drafted a replacement), a one-clause addition is worth making:

```text
  ... and A. Thomas, *A non-uniform distribution property of most orbits, in
  case the 3x+1 conjecture is true*, Acta Arith. 178 (2017), 125-134 — the
  second name in Tao's footnote, checked 2026-08-02: a backward-tree counting
  theorem showing that orbits are *not* approximately uniform on the units mod
  18 (= mod 9), with no limiting measure constructed and no law identified. Not
  prior art for 13.6.5, 13.6.3(v) or 13.6.4; it is a rigorous weak consequence
  of the law asserted there, and a rigorous refutation of the uniform
  alternative. (briefs/v3r2-thomas-check-findings.md)
```

---

## 7. What I did not establish, and what would settle it

1. **[?] I did not read the published Acta Arithmetica text.** Acta Arithmetica is paywalled at impan.pl; zbMATH returned **HTTP 403** (as it did in the Wirsching round), and MathSciNet is subscription-only. I therefore could not compare arXiv v2 against print line by line, and there is a residual possibility that material was added in proof. I judge this very low: the DOI encodes acceptance in **9-2016**, *before* the v2 posting; the printed span `125–134` matches the source's length; and the publisher's MSC triple `11B37, 11A99, 11B83` matches the tex's `\subjclass` exactly. **What would settle it:** the published PDF via any Acta Arithmetica subscription, or a zbMATH/MathSciNet review. A reader with either could confirm §2 in ten minutes.
2. **[?] No review located.** No zbMATH or MathSciNet review text was reachable, and no citing paper I found discusses Thomas's content beyond the title. So §2 rests on the author's manuscript alone — which is the strongest single source available, but it is one source, uncorroborated as to content.
3. **Not attempted, and correctly out of scope.** Whether `13.6.3`(v)'s joint product law or `13.6.4`'s equivalence has a counterpart anywhere *outside* Tao's footnote. That is the general novelty re-sweep the brief explicitly ruled out. This round checked the second of Tao's two named references and nothing else.
4. **Noted, not pursued.** Thomas's method — Krasikov–Lagarias backward-tree counting with an entropy optimisation over the exponent-index vector — is the same combinatorial genre as `cycles.md` §12.8's counting arguments, and his bound is driven by a linear functional of residue frequencies. Whether the record's exact law would let that optimisation be re-run with the true weights, sharpening `0.9999`, is a natural question. It is a *research* question, not an attribution one, and I make no claim about it. Flagged only so it is on file.
5. **Unchanged from the Wirsching round.** Item 5 there (G. M. Leigh, Acta Arith. 1986, a forward Matthews–Watts-genre residue process) remains untouched; nothing this round bears on it.

---

## 8. Verification table

| Fact | Source, grade |
|---|---|
| arXiv e-print source obtained; `thomas.tar.gz` sha256 `efd7d47f…`; `3x+1_revised.tex` sha256 `88013daa…`, 472 lines | this session — **[P]** |
| arXiv v1 2015-12-18, v2 2016-11-09; MSC 11B37, 11A99, 11B83; journal-ref "Acta Arithmetica (to publish)" | arXiv abs page — **[P]** |
| Published as Acta Arith. **178** (2017), no. 2, **125–134**, DOI **10.4064/aa8385-9-2016**; publisher MSC matches the tex exactly | impan.pl ToC + article page — **[P]** |
| Tao's `\bibitem{thomas}` matches that citation to the letter | `collatz.tex` L1944–1946 — **[P]** |
| Tao's footnote clause on Thomas is a bare "See also …", asserting no relation | `collatz.tex` L393 — **[P]** |
| `tao.tar.gz` sha256 `ba81acd6…`, `collatz.tex` sha256 `bfbc3943…` (third reproduction of both sibling rounds' hashes) | this session — **[P]** |
| Theorem statement, `W`, `c_i`, `I`, the bound `N^{0.9999}` | `3x+1_revised.tex` L81–99 — **[P]** |
| The `3x+1` conjecture is used **only** to make the "reaches 1" clause vacuous; the theorem is unconditional | ibid. L61–64, L93 — **[P]** |
| Method is Krasikov–Lagarias backward-tree counting; Sinai's map `S` on `⊓` | ibid. L103, L114–119 — **[P]** |
| Weight functional `c(n) = 2c_1 + c_5 + 3c_11 + 2c_13 + 3c_17`; weights sum to `11` | ibid. L184, L254 — **[P + C]** |
| `0.0215` is an optimisation artifact: `w_0 − 0.9998 ∈ (0,10^{-4})` | ibid. L364–373 — **[P]** |
| **No** occurrence of measure / Haar / Markov / stationary / invariant / random / probability / equidistribution / convergence / `Z_3` in the paper; the one "adic" hit is "contr**adic**t" | full-text scan of the source — **[P + C]** |
| Bibliography has no `p`-adic reference (Chamberland ×2, Korec, Krasikov–Lagarias, Lagarias ×3, Muñoz, Sinai) | ibid. L438–470 — **[P]** |
| `(Z/18Z)^× = {1} × (Z/9Z)^×`; `I → (Z/9Z)^×` is a bijection; "mod 18" carries exactly the mod-9 data on `⊓` | — **[C]** |
| Tao's `Syrac(Z/3Z)`, `Syrac(Z/9Z)` reimplemented from Lemma 1.12 and reproducing his printed lines **before** any comparison | — **[C]** |
| repo `experiments/aeh_symbolic.py::nu_exact`, imported unmodified: `ν_1 = (0,2/3,1/3)`, `ν_2` as printed; `ν_j(x) = Syrac(2x)` at `j = 1,2` | — **[C]** |
| `Syrac` on `I`: `8/63, 4/63, 2/63, 16/63, 11/63, 22/63`, summing to `1`; max `22/63` at `17`, min `2/63` at `7` | — **[C]** |
| Threshold `1/6 + 0.0215 = 1129/6000` exactly; `22/63 > 1129/6000` (`132000 > 71127`) | — **[C]** |
| Level-one alone suffices: `2/9 > 1129/6000` (`12000 > 10161`) | — **[C]** |
| Weight functional: uniform `11/6`, Thomas's cap `12419/6000`, `Syrac` value `52/21`; `52/21 > 12419/6000` | — **[C]** |
| Thomas's `(cases)` table reproduced from scratch, all six rows | — **[C]** |
| `(cases)` **=** the support of Tao's Lemma 1.12 at level `9`; masses recomputed through it reproduce Tao's printed line | — **[C]** |
| `Syrac` masses strictly separated and decreasing across groups of equal minimal admissible exponent (`1 → 2 → 3 → 4`) | — **[C]** |
| Thomas's 26-orbit tally `(28,22,5,10,11,13)`: argmin agrees with `Syrac`, full ordering does not | ibid. L105–110 + **[C]** |
| `13.6.3`(v) statement (2-adic residue, `d = m + a`, `m ⊥ a`, product law) | `aeh.md` L90–99 — **[P, repo]** |
| `13.6.4` statement (orbit-by-orbit equivalence, no measure on starting values) | `aeh.md` L101–109 — **[P, repo]** |
| `13.6.5` values `2/3, 19/63, 2/63` | `aeh.md` L118–123 — **[P, repo]** |
| No tracked file mentions Thomas (only Cover–Thomas) or "mod 18" | `git grep` — **[C]** |
| Published Acta Arith. text not obtained (paywalled; zbMATH 403; MathSciNet subscription-only) | attempted this session — **[?]** |

**Scripts** (scratchpad only; nothing added to `experiments/`): `thomas_compare.py` (Tao's Lemma 1.12; repo `nu_exact` imported unmodified; the mod-18 ↔ mod-9 reduction; the four threshold decisions; the `(cases)` reproduction), `thomas_mechanism.py` (`(cases)` vs. Tao's recursion support; the minimal-exponent/mass monotonicity). All exact `Fraction`; every distribution asserted to sum to `1` before use; every inequality decided by cross-multiplied integers.

---

## 9. Closing line

**Tao's footnote is now fully discharged.** It names exactly two works. **Wirsching** (LNM 1681) was checked in `briefs/v3r2-wirsching-check-findings.md`: an inverse-map `3`-adic Markov process with uniformly weighted branches, whose `3`-adic limit is Haar `(1/2, 1/2)` where ours is `(2/3, 1/3)` — not our object, not prior art. **Thomas** (Acta Arith. 178) is checked here: a backward-tree counting theorem with no measure, no process and no law anywhere in it — not our object, not prior art, and in fact a rigorous result in the record's own direction. Neither displaces Tao as the primary attribution for `13.6.5`'s law, and neither touches `13.6.3`(v) or `13.6.4`.

**Net effect on what §13 claims as novel: nothing is removed.** The list stands exactly as the two prior rounds left it — `13.6.3`(v)'s joint product/renewal law, `13.6.4`'s orbit-by-orbit genericity equivalence, and the calibration record — with `13.6.5`'s law attributed to Tao. Three checks this round found prior art; this one, like Wirsching's, does not, and I have said in §0(a) and §5 exactly where I looked and on what the negative rests: a full-text read of the author's own manuscript, a vocabulary scan showing the relevant notions are absent, and exact arithmetic in the one direction where a comparison was possible at all.

Two `\bibitem`s are now **worth adding and neither is owed**: `\bibitem{wirsching}` and `\bibitem{thomas}`, each with the one-paragraph explanation of why it is *not* the same object. Both drafts are in the record. That is the whole residue of the footnote.
