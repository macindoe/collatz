# Findings: paper 1 v4 content lock — the claims ledger

**Task:** `briefs/paper1-content-lock-brief.md`. Branch `paper1-content-lock`, base **`e7a3f5e`** (the worktree was cut at `8370638` and fast-forwarded to `e7a3f5e`, the brief's commit on `main`, before any work). Done 2026-10-19.

**Rules kept.** `paper/collatz-reduced-v4.tex` was read in full and not edited. No wiki page was edited. Nothing outward: no network use at all. Files were written with Edit/Write only.

**Deliverables:**
- `paper/collatz-reduced-v4-claims.md`: the ledger. Table A holds the mathematical claims, Table B the prose claims and the "not claimed" list, Table C the open author items and the build placeholders.
- This file.

## 1. How the ledger was built

- **Coverage.** Every numbered statement of v4 has at least one row. So does every sentence with mathematical content in the abstract, introduction, related work, the unnumbered paragraphs of §4 ("The dictionary with `m`-cycles", "Configurations", "The threshold, explicitly", "Verification and record"), §5 and the Discussion. Claims made inside proofs (the target-shift lemma, the digit-determinacy facts, the construction, the constants) have their own rows. The rewrite may move proof material, and these are the claims most easily lost when it does.
- **IDs.** Numbered statements take their PDF number: `C-4.6(iii)a` is Theorem 4.6(iii), first clause. The numbers were checked on `pdftotext paper/collatz-reduced-v4.pdf`. Unnumbered material takes a section prefix and a short name (`C-4.thr.3`, `C-5.TV`, `C-RW.14`).
- **Statements** are verbatim, or compressed with every quantifier, constant and scope word kept. Where v4 hedges ("indicates", "strongly suggests", "in part", "≈"), the hedge is in quotation marks in the row.
- **Grades.** The brief named five grades: proved here, proved in the record, cited, conjectured, measured. v4 needs six more: def, rederived, heuristic, interpretation, asserted, and open. Without them, Heuristic 3.9, the interpretive remarks and a few unsupported sentences would have had to be forced into a grade they do not have. The legend at the top of the ledger defines each one.
- **Verification column.** It quotes what v4 itself records. Where v4 records nothing, it says so. A record line is added only where one was actually read for this ledger: `cycles.md` §12.4, `stage4.md`'s undecided-rate remark, and `spine.md` §9.8.
- **Independent check of the printed constants.** A scratch script recomputed every decimal constant v4 prints, at 40 digits. It is `consts.py` in the session scratchpad and is not committed. The constants are `ϑ`, `Γ*`, `δ_hi`, `φ(δ_lo)`, the arc length, `1 − 13ϑ`, `λ₀`, `2^{−(λ₀+1.5)}`, `β`, `1/β`, `4/β = (1 − log₂√3)^{−1}`, `log₄3 = 1 − β/4`, `L^{16}`, the "> 78" and "> p + 900" margins at `p = 16`, the `3.33` bound on `Γ′`, and the `p = 7` instance's `γ = 6.7438` (with `K = 149`). **All agree with v4.** The `3.33` margin is tight: `1.05 L^p κ_p + L/(L−1) = 3.3241` at `p = 16`. I also re-checked Lemma 5.2's four residues and the example in C-5.product by hand.

## 2. Counts

**Table A: 190 rows**, by primary grade (the first grade named; compound grades are counted once):

| Grade | Rows |
|---|---|
| proved here (incl. sketch / outline) | 85 |
| cited | 29 |
| def (incl. scope statements) | 18 |
| proved in record | 13 |
| interpretation | 13 |
| measured | 12 |
| rederived | 7 |
| heuristic | 6 |
| conjectured | 3 |
| asserted | 3 |
| open (stated) | 1 |
| **total** | **190** |

Eight rows carry "asserted" somewhere in their grade: three as the primary grade and five as a component. All are listed in §3.

By section:
- abstract 18;
- introduction 16;
- related work 23;
- §2: 7;
- §3: 25;
- §4: 62;
- §5: 36;
- Discussion 3.

**Table B:** 38 prose claims (`P-1`–`P-38`) and 16 "not claimed" items (`N-1`–`N-16`).

**Table C:** 7 author items (`A-1`–`A-7`) and 8 placeholder rows (`PH-1`–`PH-8`).

## 3. v4 content that could not be stated cleanly as a claim

None of these is a false theorem. Each is a sentence whose grade, scope or wording is looser than the statement it summarizes, or a claim with no support in v4. The rewrite must not copy the looseness into a plain-language layer, where it would read as a stronger claim. The author decides whether to repair any of them; repairing one is a content change and belongs before the lock, not in the rewrite.

| # | Rows | Issue |
|---|---|---|
| U1 | C-Abs.2, C-Int.11, C-D.1 | "All governed by one 2-adic quantity" and "every quantity above obeys an exact law in the anchor displacement `d − M(ω)`" are broader than §3. The absorption `a₊` is a 3-adic function of `ω` (Lemma 3.4), and Theorem 3.7 itself carves `a₊` out ("This last clause does not extend to `a₊`"). The abstract half-carves it out ("together with a stated 3-adic absorption law"); the introduction does not. |
| U2 | C-Int.9 vs C-4.6(iii)a, C-Abs.12, C-RW.20 | Contribution (v) says every element "above" any threshold `X₀`. The theorem says `x_min ≥ X₀`, and the abstract and related work say "at least". A strict/non-strict mismatch. |
| U3 | C-Int.13, C-3.9(a) | "An elementary accounting argument *shows* each decision consumes digits irreversibly". Heuristic 3.9 states consumption as a fact inside a Heuristic environment. Thm 3.7 proves only that the residues to depth `σ + k + 2` are *sufficient*. That they are needed, and that "nothing regenerates" them, is not proved. The verb "shows" in the introduction is stronger than the environment. |
| U4 | C-RW.11 | "The law recorded here implies [Thomas's] conclusion, its level-one form already forcing some class to frequency at least `2/9`": no proof and no pointer in v4. |
| U5 | C-3.8.rate | Theorem 3.8 ends "under the law `π_{k,D}` … the undecided rate is `≈ 2^{−(k+1)}`". A theorem statement carrying "≈", with no derivation in v4. The record (`stage4.md`, Remark "undecided rate") derives it under "the uniformity heuristic" from `P(lifting) ≈ 1/4`, and measures `0.0275` against `0.03125` at `k = 4`. Under `π_{k,D}` the rate is an exact computation, so v4 should give it exactly or label it heuristic. |
| U6 | C-4.6.close, C-D.2 | "Uniform cycle exclusion therefore requires the divisibility system — *equivalently*, rigidity of the closed anchor walk `Σ ΔM_t = 0`". The equivalence of the divisibility system with the closed-walk condition is not proved or pointed to in v4. "Requires" is a statement about what size arguments cannot do, which (i)–(iii) prove; it is not a theorem about cycles. The Discussion then files Theorem 4.6 under "arithmetic … whether closed anchor walks are rigid", which Theorem 4.6 does not address. |
| U7 | C-4.8(b) vs C-4.8(d) | Remark 4.8 says "At the scale of Theorem 4.6(iii) a unit block is excluded", unqualified. Two sentences later the exclusion is shown only where a stated inequality holds: at `p₁(X₀)` and `p₁(X₀) + 20` for `X₀` from `2^{20}` to `2^{200}`, with the unit crash "undecided" below that. The first sentence needs the second's scope. |
| U8 | C-5.exc | "By Heuristic 3.9 it cannot be reached by finite-window computation": a definite "cannot" resting on a heuristic. |
| U9 | C-3.9(b), C-4.3, C-4.6(i)c, C-4.thr.1, C-4.8(d), C-5.cal, C-5.limits vs P-33 | Appendix A says "every computational claim cites a runnable script". In v4 itself, no script is named for: the empirical mean `σ ≈ 4.0`; Lemma 4.3's `p ≤ 5` inspection; the exhibitions at `p ∈ {2, 4}` (the verification paragraph covers `3..32` "apart from `p = 4`" and does not mention `p = 2`); `p₁` at `X₀ = 5·2^{60}` and the ranges `X₀ ≤ 16` and `2^8 ≤ X₀ ≤ 2^{12}` (the named script computes `X₀ = 2^j`); Remark 4.8's tabulated range; and the whole calibration campaign, which is cited only to `aeh.md` §13.4–13.5. The record may carry every one of these scripts; I did not check. Either the protocol sentence reads "the record cites" or the rewrite's verification index names them. |
| U10 | C-D.3 | "Three directions have defined success criteria." The criteria are not stated in v4. |
| U11 | P-18 | The Rackl thesis (Klagenfurt, 2021) is discussed in related work, but has no `\bibitem` and no title. |
| U12 | C-Abs.11 vs C-4.6(i)b–c | The abstract says "slack between two absolute constants at every period (… `p ∈ {2,4}` by exhibition)". The theorem places `3 ≤ p ≤ 15` "in the same bracket" but claims only *existence* of size-passers at `p ∈ {2,4}`, with no bracket. "Every period" also leaves `p = 1` unaddressed: neither the theorem nor the abstract mentions it. |
| U13 | C-4.2, C-4.3, C-4.5(d), C-3.N, C-3.1, C-4.6.φ | Stated without proof in v4: Corollary 4.2 ("obtained in four lines", which are not shown); Lemma 4.3 (no proof environment; the record pointer is only in Thm 4.4's outline); Theorem 4.5's second and third displays (the printed proof covers the first only); and three elementary facts (`N` an isomorphism; `M(ω)` even iff `ω ≡ ±1 (8)`; `φ` a decreasing involution). An appendix "where the nerds can dispute" should carry a proof or an explicit pointer for each. |
| U14 | C-5.2, C-5.TV, C-4.6.constr, C-4.cfg(c), C-5.1 | Notation collisions that a non-specialist cannot resolve: the class `(1,1)` of Lemma 5.2 (`ω ≡ 1 (8)`, `d = 1`) against the fixed state `(1,1)`; `η` used for `φ(s_c)` in §4 and for the slack in `J ≤ (1−η)b` in §5; `Λ` for `K log 2 − n log 3` and `Λ_N` for the budget; `T` for the map, `T_N` for the horizon and `T_j` for partial sums; `ε` for the anchor displacement, `ε_t` in Cor 4.2 and `ε` in Hyp 5.1; `M_t` against `M(ω)`, which v4 itself flags. |
| U15 | C-5.cal | "Four apparent violations" are listed in three clauses. The four are: the `s = 3` marginal excess, the pair correlations, the digit biases, and the `5σ` bias. The rewrite should enumerate them. |
| U16 | C-5.past | "…and can fail by any amount": asserted, with no example or pointer. |
| U17 | C-5.ratio | "…one residue of the unique class with a self-loop channel": the uniqueness is asserted. |
| U18 | C-Abs.13 | "The family realizes Rozier's 1991 extremal" follows both the all-`p` and the threshold statements. Has content only at the threshold scale (C-4.thr.6). For the family of (i), `κ_p n ≈ 0.59`, so `κ_p n ≤ ρ₀ ≤ κ_p n + 4.6` holds trivially. This was already flagged in `briefs/paper1-v4-draft-findings.md` §5. |
| U19 | C-Abs.15 | The abstract's one-line form of Hypothesis 5.1 drops the budget tally and "for every admissible `(τ, θ)`". That is fine for an abstract. A main-text layer that states the hypothesis in words must keep both clauses, or it states a different conjecture. |

## 4. Proposed layer map (a suggestion, not the rewrite)

**One constraint first.** v4's Version note says "No statement is renumbered" (P-6). Theorem 4.6 is cited by number outside the paper: in the joint note, the Merle ledger and the version history. Moving statements between layers and appendices will renumber them unless numbers are pinned by hand. Either keep v4's numbers through manual numbering, or print a v4 concordance and correct P-6. Which one is the author's choice, but it must be made before the rewrite starts.

Each layer lists what the main text carries (by claim ID) and what moves to an appendix. Each opens with one sentence on what the non-specialist reader needs.

**Layer 0 — the map** (front matter and opening):
- *Reader needs:* what the Collatz map is, that this paper re-describes it without loss, proves exact one-step laws, and measures exactly how far size-counting can go against cycles — and what it does not claim.
- *Main:* P-1–P-6, P-12, C-Int.1, the abstract rows C-Abs.1–18 as a plain summary, C-RW.12, and a "what this paper does not claim" box drawn from N-1, N-3, N-9, N-11, N-13 and N-15.
- *The Author's note* stays in the main text, in the author's voice (A-1 to A-3).

**Layer 1 — blocks (the 2-for-3 trade):**
- *Reader needs:* one worked example in binary showing each rising step swap a factor of 2 for a factor of 3 until the 2s run out, then a single burst of halvings. For example `x = 7`: `x + 1 = 8 = 2³`, then `7 → 11` (`12 = 2²·3`), then `11 → 17` (`18 = 2·3²`), then `17 → 13`, since `A = 3³ − 1 = 26` and `s = 1`.
- *Main:* C-Int.3, C-2.2(i)–(ii), C-4.dict(a), P-20 (classical: Steiner; the author's 2023 note).
- *Appendix:* the proof of Prop 2.2.

**Layer 2 — states `(ω, d)` and `F`:**
- *Reader needs:* every block is labelled by two numbers, `F` is the label-to-label map, and the equivalence theorem in words: nothing the conjecture depends on is lost.
- *Main:* C-Int.4, C-2.1 (in words, with the formulas set aside), C-2.2(iii), C-2.3(a)–(c) (statement), C-RW.22–23, P-21, P-22.
- *Appendix:* Def 2.1 in full, the proof of Thm 2.3.

**Layer 3 — the exact laws:**
- *Reader needs:*
  - what a 2-adic valuation is: the number of trailing zeros in binary;
  - that the anchor `M(ω)` is one infinite binary string per `ω`;
  - that `s` is read off by how many low binary digits `d` and `M(ω)` share, plus 2;
  - that a factor of 3 is gained exactly when `s` is even;
  - that a finite window either answers exactly or correctly says "deep event";
  - that the digit-budget conclusion is a heuristic, labelled as one.
- *Main:*
  - C-3.1 (in words);
  - C-3.3(a)–(b) (the law and the eight-class table);
  - C-3.4's last sentence;
  - C-3.5 in words;
  - C-3.7 in words;
  - C-3.8 (with C-3.8.rate, once U5 is settled);
  - C-3.9(a)–(e), with the Heuristic label kept;
  - C-3.post, C-Int.11–14 (with U1 and U3 settled first);
  - one line each from Remarks 3.6 and 3.10: what was checked, by independent code.
- *Appendix:* C-3.N, C-3.eq1, C-3.2 and its proof, C-3.3(c)–(d) (the Baker clause and the `ω = 1` case), C-3.4 in full, C-3.5 in full, C-3.5.TS, C-3.7.pf, every proof, and the full counts of C-3.6 and C-3.10.

**Layer 4 — cycles and the limit of counting:**
- *Reader needs:*
  - a cycle forces `2^K` and `3^n` to be nearly equal, and "size-counting" means arguing from how near;
  - the classical trim (Rozier; Simons–de Weger) says how near, with a constant that decays exponentially in the number of blocks;
  - the staircase passes every size test at that same scale, so size alone cannot exclude cycles uniformly;
  - what is left is divisibility.
- *Main:*
  - the cycle side: C-4.dict(b)–(d) (a `p`-block cycle is an `m`-cycle, so Hercher's `p ≤ 91` applies); C-4.1 in words ("a cycle needs `q` to divide every rotation's sum"); C-4.1.BS (credit);
  - the trim: C-4.4 with P-24 and N-2; C-4.5(a), (c) in words, with C-4.5.cr, P-16 and N-3;
  - the staircase: C-4.6(i)a and (i)d, C-4.6(iii)a (the headline brackets, with N-4 and N-5); C-4.6(iv) as the concrete example (the `p = 7` staircase); C-4.7;
  - framing and scope: C-4.6.close with HH's credit (after U6); C-Abs.13 / C-RW.20 (after U18); C-4.ver(d) / N-9.
- *Appendix:*
  - definitions and identities: C-4.setup, C-4.cfg(a)–(d), C-4.eq2, C-4.6.eq3, C-4.2, C-4.3;
  - the small periods and the trim: C-4.4.p1, C-4.4.p23, C-4.5(b), C-4.5(d);
  - Theorem 4.6 in full: C-4.6.φ, C-4.6(ii)a–c, C-4.6(iii)b–c, C-4.6.pf.a, C-4.6.constr, C-4.6.crashD, C-4.6.minimax, C-4.const, C-4.6.pf.iii;
  - the threshold and the crash block: C-4.thr.1–7 (with N-5 to N-7), C-4.8(a)–(d) (after U7);
  - verification: C-4.ver(a)–(c).

**Layer 5 — the equidistribution conjecture:**
- *Reader needs:*
  - the classical heuristic treats each block's two numbers as independent coin-flip counts, so a block letter `(m, r)` has probability `2^{−(m+r)}`;
  - the conjecture says real orbits of typical large starts keep looking like that after the start's own binary digits are used up;
  - up to that point it is a theorem;
  - what it would and would not buy;
  - four apparent anomalies in the tests were all explained.
- *Main:*
  - the law and the hypothesis: C-Int.16; C-5.piledger in words (`P(s = j) = 2^{−j}`, the rate `1/3`, "drift is a property of the law only"); C-5.1 in words, keeping the budget tally and the admissibility clause (U19);
  - the base case: C-5.thm (the base case `θ < 1/4`) and C-5.clock;
  - what it buys and does not: C-5.ledger, C-5.supplies, C-5.exc (after U8), N-11 to N-15;
  - the calibration: C-5.cal and C-5.limits in summary (after U15), with the routing story of C-5.2 told in words.
- *Appendix:*
  - the window law: C-5.null, C-5.depth, C-5.syrac, C-5.joint, C-5.W, C-5.pi, C-5.product;
  - the hypothesis's machinery: C-5.adm, C-5.eq, C-5.lim, C-5.alt, C-5.cut, C-5.prot, C-5.cons, C-5.4mean, C-5.past, C-5.rates;
  - the base case: C-5.base, C-5.TV;
  - relation to other results: C-5.Korec, C-5.dyadic, C-5.union, C-5.descent, C-5.block;
  - the routing lemma C-5.2 as stated, and C-5.ratio, C-5.nocut.

**Layer 6 — discussion:**
- *Reader needs:* the two places the difficulty lives, and why the staircase suggests they are one.
- *Main:* C-D.1–3 (after U10), C-3.post.

**Credit and related work:**
- *Reader needs:* who did what, in one place.
- *Main:* a short credit section carrying P-13 to P-23, C-RW.13–21, and the credit columns of Thm 4.4 to 4.6.
- *Appendix:* the density line and the 3-adic comparisons, C-RW.1–11, as a "Related work in detail" appendix.

**Proposed appendices:**
- A — Methodology, responsibility and records: v4's Appendix A unchanged, P-30 to P-34. Keep it adjacent to the main text, not buried.
- B — Proofs for the reduced system and the exact laws (Layers 1–3).
- C — The cycle apparatus and the proof of Theorem 4.6 (Layer 4).
- D — The hypothesis in full (Layer 5).
- E — Related work in detail.
- F — A verification index: every `measured` row with its script and its count. This also resolves U9.

## 5. Open author items

From Table C:

1. **A-1.** The Author's note sentence at L65–71 is wrong in its second item ("a uniform trim that caps what size-counting can achieve"). The trim is Rozier's and Simons–de Weger's. One option: "a proof that the classical cap on what size-counting can achieve against cycles is the true one".
2. **A-2, A-3.** Delete the `% AUTHOR:` comments: L58 once A-1 is settled; L61 now (that sentence is accurate as written, per the decision of 2026-10-19).
3. **A-4.** Appendix A's "the AI collaborators carried out the mathematical development" now spans the ChatGPT phase. Narrow it if that phase should read as exploratory only.
4. **A-5.** D3's canonical-scale sentence at the end of "The threshold, explicitly": keep or cut.
5. **A-6.** Optional items left out: the gcd rotation-invariance; the Tao p. 2 / Prop 1.11 refinement; the Knight clause.
6. **A-7.** The Sós 1958 entry has not been checked at source.
7. **Placeholders PH-1 to PH-8:**
   - `\vfourdoi` (L26, L52);
   - `\recordcommit` (L29, L330, L540), which must name a commit reachable on the public repository, and the record's `main` is not yet pushed;
   - the two months (L36, L53);
   - the "record is public" sentences (P-11, P-34), which depend on that push.

New from this window, for the author before the lock:

8. **§3, U1–U19.** Decide which to repair in v4's content and which to carry as they are. Each repair is a content change, so make it before the lock commit is tagged, or the ledger must be re-cut.
9. **§4, numbering.** Pin the v4 numbers or print a concordance. P-6 ("No statement is renumbered") must stay true or be corrected.

## 6. Record

**Commits on the branch:**
- the ledger;
- this file.

**Encoding:** `python experiments/encoding_scan.py` was run before the final commit (result in that commit's message).

**Scratch:** `consts.py`, in the session scratchpad, not committed. It recomputes v4's decimal constants at 40 digits with `mpmath`.
