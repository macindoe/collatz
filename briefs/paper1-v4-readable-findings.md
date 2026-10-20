# Findings: paper 1 v4 — the readable rewrite (presentation only)

**Task:** `briefs/paper1-v4-readable-rewrite-brief.md`. Branch `paper1-v4-readable`, base **`46e7464`** (the worktree was cut at `eded178` and fast-forwarded to `46e7464`, the brief's commit on `main`, before any work). The paper at the base is identical to the tag `paper1-v4-content-lock` (`git diff paper1-v4-content-lock 46e7464 -- paper/` is empty). Done 2026-10-19.

**Deliverables:** `paper/collatz-reduced-v4.tex` rewritten in place; `paper/collatz-reduced-v4.pdf` rebuilt; this file. Nothing else was edited; nothing went outward.

## 1. What was done, and how claims were kept

**Method.** The formal text of the content-locked v4 (§2–§5, every statement, proof, remark, constant, record pointer and verification line) was moved **unchanged** into Appendices B–E, in its original order. A line-by-line comparison of the old file against the new (every old line searched for in the new file, non-matches diffed) shows that the only changes in the moved text are: (a) the symbol renames of §4 below; (b) `Section~\ref{sec:…}` → `Appendix~\ref{app:…}` where a formal sentence points at formal material, and "this section" → "this appendix" once (C-5.W); (c) "cited in Related work" → "cited in Appendix F" (C-5.descent); (d) two new labels (`def:anchor`, `rem:verify2`) so the main text can point at Definition C.1 and Remark C.10; (e) §5's `\paragraph{Calibration.}` became an unnumbered subsection heading, and Appendix E gained four more unnumbered subsection headings (`\subsection*`, so they cannot collide with Hypothesis E.1's number). No formal sentence was reworded.

The **main text** (Sections 1–8) is new prose in plain words that points at the formal statements. It was written to the ledger: every main-text sentence that states a result paraphrases a ledger row and names its formal home. The intro's "Section 3 is the technical heart" paragraph (C-Int.11–16) was split to the ends of the sections it describes, and C-3.post moved with it into §4 ("Where the difficulty is"). The Discussion (C-D.1–3) is §7 verbatim. The related-work paragraphs ¶1–¶2 are Appendix F verbatim (refs moved to the appendices); ¶3 (contemporary efforts, Rackl) and ¶4 (the provenance paragraph) are §8 verbatim.

**Kept verbatim:** the Author's note; the provenance paragraph ("The division of labor…", §8); Appendix A (the method disclosure, still Appendix A and the first appendix); the title-page footnote; the bibliography; all placeholders (`\vfourdoi`, `\recordcommit`, the two months) with their `% DOI:` / `% PIN-AT-BUILD:` comments. One placeholder **comment** was updated for location only: the `\recordcommit` comment now says "Used in Appendix D (\"Verification and record\") and Appendix A" (it said "Section 4 and Appendix A").

**Changed outside the formal text, by the brief:** the abstract (one plain opening sentence, "stated as a heuristic" added to C-Abs.7's clause, `(fair-coin)` added to C-Abs.15's, and a closing sentence on how the paper is laid out; every C-Abs row is otherwise in its v4 words); the Version note (P-6, see §6).

**Build:** `pdflatex` ×3 in the session scratchpad (`…/scratchpad/build-v4r`): **33 pages, 0 undefined references or citations, 0 multiply defined labels, 0 overfull boxes.** The PDF was copied into `paper/`. **Encoding:** `python experiments/encoding_scan.py` clean (0/0/0) before each commit.

## 2. The new outline, with page counts

| Part | Pages | Content |
|---|---|---|
| Front matter | 1–2 | Title, abstract, Version note, Author's note |
| §1 What this paper is about | 2–4 | the map in words; the three purposes; the three levels (map, blocks, states — the author's draft000 §2 layering); what is new (i)–(vi); **what this paper does not claim**; how to read |
| §2 One rising run: trading 2s for 3s | 4–5 | `x = 7` in binary (a table: `x`, `x+1`, trailing ones/zeros); `T(x)+1 = (3/2)(x+1)`; the block, entry depth, exit valuation; the one-division-map dictionary |
| §3 Blocks become states | 5–6 | `(ω, d)`; the representatives (7, 11, 17 for `(1,3)`); `F`; the orbit of 7 as `(1,3) → (7,1) → (1,2) → (1,1)`; Theorem B.3 in words |
| §4 The exact laws of one step | 6–7 | 2-adic integers and the anchor in words; the valuation law with the eight-class table; the factor of 3; the next depth; the window and the trichotomy, with the undecided rate; the digit budget, labelled a heuristic; checks; where the difficulty is |
| §5 Cycles: what counting can and cannot do | 7–10 | a cycle as numbers (`m`-cycles, Hercher); size; size vs divisibility; small periods; the uniform trim as a short history (Rozier 1991 → Halbeisen–Hungerbühler 1997 → Brox 2000 → Simons–de Weger 2005); the `p = 7` staircase as a picture; sharpness in three bullets with every scope word; what is left |
| §6 The fair-coin hypothesis | 10–12 | letters and the model law; the hypothesis in words with both budget and admissibility clauses; where it is a theorem (`τ < 1`, `θ < 1/4`); what it would and would not give; the calibration in one paragraph |
| §7 What remains open | 12 | v4's Discussion, verbatim |
| §8 Credit and provenance | 12–13 | contemporary efforts and Rackl; the provenance paragraph, verbatim |
| **Main text total** | **≈ 12 pp (1–13)** | |
| App A Methodology, responsibility, and records | 13 | verbatim |
| App B The reduced system | 13–14 | Def B.1, Prop B.2, Thm B.3 with proofs |
| App C The exact laws | 14–17 | `N`, the isometry (1), Def C.1–Remark C.10, the undecided-rate paragraph |
| App D Cycles | 17–24 | setup, notation, Prop D.1–Lemma D.3, Thm D.4, the `m`-cycle dictionary, configurations (2), Thm D.5, Thm D.6 with its proof (3), the threshold, Remarks D.7–D.8, verification and record |
| App E The equidistribution hypothesis in full | 24–28 | the window law; Hyp E.1 and its equivalent form; budget and admissibility; the base case; what it implies; calibration with Lemma E.2 |
| App F Related work in detail | 28–29 | v4's related-work ¶1–¶2, verbatim |
| App G Verification index | 29–31 | every computational claim → check → script → record section; the list of statements proved in the record |
| App H Concordance and notation | 31–32 | v3 → v4 numbers; v3 sections → v4 places; renamed symbols |
| **Appendices total** | **≈ 19 pp (13–32)** | |
| References | 32–33 | verbatim |

## 3. The concordance (also printed as Appendix H)

v3's numbering and the content-locked v4's numbering are the same (the lock's Version note: "No statement is renumbered"), except Remark 4.8, new in v4. So one table serves both. The rule: §2 → B, §3 → C, §4 → D, §5 → E, same number.

| v3 / v4-lock | New | | v3 / v4-lock | New | |
|---|---|---|---|---|---|
| Def 2.1 | Def B.1 | reduced map | Prop 4.1 | Prop D.1 | elimination |
| Prop 2.2 | Prop B.2 | blocks | Cor 4.2 | Cor D.2 | size balance |
| Thm 2.3 | Thm B.3 | equivalence | Lemma 4.3 | Lemma D.3 | ceiling |
| Def 3.1 | Def C.1 | anchor | Thm 4.4 | Thm D.4 | periods 1–3 |
| Lemma 3.2 | Lemma C.2 | squaring | Thm 4.5 | Thm D.5 | uniform trim |
| Thm 3.3 | Thm C.3 | valuation law | Thm 4.6 | Thm D.6 | staircase |
| Lemma 3.4 | Lemma C.4 | absorption | Remark 4.7 | Remark D.7 | divergence |
| Thm 3.5 | Thm C.5 | depth closure | (v4-lock) Remark 4.8 | Remark D.8 | crash (new in v4) |
| Remark 3.6 | Remark C.6 | checks | Hyp 5.1 | Hyp E.1 | AEH |
| Thm 3.7 | Thm C.7 | increment | Lemma 5.2 | Lemma E.2 | routing |
| Thm 3.8 | Thm C.8 | trichotomy | eq. (1) | eq. (1) | isometry |
| Heuristic 3.9 | Heuristic C.9 | digit budget | (v4-lock) eqs. (2), (3) | eqs. (2), (3) | term, element |
| Remark 3.10 | Remark C.10 | checks | | | |

Sections: v3/v4-lock §1 → §1, §8, App F; §2 → §2–§3, App B; §3 → §4, App C; §4 → §5, App D; §5 → §6, App E; §6 → §7; App A → App A. Equation numbers are unchanged (global numbering kept; all three equations are in the appendices).

## 4. Symbol renames (U14, solved by renaming)

| Was | Now | Where | Meaning |
|---|---|---|---|
| `ε` | `ξ` | Thm C.5 | anchor displacement |
| `ε_t` | `χ_t` | Cor D.2, Lemma D.3 and proofs; §5 | block ratio |
| `T_j` | `μ_j` | proof of Thm D.5; proof of Thm D.6; Remark D.8 | partial sums of entry depths |
| `S` (= `K − n`) | `s_tot` | proof of Thm D.6, Thm D.6(iv) | total exit valuation |
| `T_N` | `H_N` | Hyp E.1, App E; §6 | block horizon |
| `Λ_N` | `E_N` | Hyp E.1, App E; §6 | exponent budget |
| `H` | `𝓗` (`\Ent`) | App E base case | binary entropy |

Kept, and said so in App D "Notation" and App H: `T` (the map), `Λ` (the linear form), `ε` (tolerance), `M_t` and `S_t` (the record's notation, P-25), `S_n` (exponent spent). Appendix H's table also records v3's `η → ζ` and `(r,1) → [r,1]` (made in the fix pass). The ledger row C-4.notation (the "Overloaded symbols" paragraph) is **replaced** by App D's shorter "Notation" paragraph and App H's rename table: its content (which symbol means what) is all there, but the collisions it listed no longer exist. A row-by-row checker should read C-4.notation against App H.

## 5. Ledger ID → new location

"Main" names the plain-words place; "Formal" the verbatim place. Every live row of Table A is in its formal place unchanged (save §4's renames and §1's ref changes); the main-text column says where a non-specialist meets it.

### Table A

| IDs | Formal (verbatim) | Main text |
|---|---|---|
| C-Abs.1–C-Abs.18 | Abstract (v4 words; C-Abs.7 adds "stated as a heuristic"; C-Abs.15 adds "(fair-coin)") | Abs.1 §3; Abs.2 §4 opening and "Where the difficulty is"; Abs.3 §4 "The valuation law"; Abs.4 §4 "The next depth"; Abs.5–6 §4 "How many digits one step needs"; Abs.7 §4 "The digit budget"; Abs.8 §5 "Size and divisibility", "Small periods"; Abs.9 §5 trim history; Abs.10–11 §5 "Sharpness" bullet 1 and §1 not-claimed; Abs.12 §5 bullet 2; Abs.13 §5 bullet 3; Abs.14 §5 history and "What is left"; Abs.15 §6 "The hypothesis"; Abs.16 §6 "What it would give"; Abs.17 §6 "Where it is already a theorem"; Abs.18 §6 "How it was tested" |
| C-Int.1 | — (intro rewritten) | §1 ¶1 |
| C-Int.2 | — | §1 ¶2 (the three purposes, with the parenthetical answer, scope words kept); §5 opening |
| C-Int.3 | Prop B.2 | §2 |
| C-Int.4 | Def B.1, Thm B.3 | §3 |
| C-Int.5–C-Int.10 | — | §1 "What is new" (i)–(vi), v4's contribution sentences with pointers changed |
| C-Int.11, C-Int.12, C-Int.13, C-Int.14 | — | §4 "Where the difficulty is" |
| C-Int.15 | Remark D.7 | §5 opening ("the one regime where finite data can beat unbounded depth") and "The staircase, as a picture" ("in a concrete sense, one object") |
| C-Int.16 | App E "The window law" | §6 opening and "Letters and the model law" |
| C-RW.1–C-RW.11, C-RW.13 | App F ¶1 | RW.13 also §5 "Size and divisibility" |
| C-RW.12 | App F ¶1 | §5 "Sharpness" bullet 2 |
| C-RW.14–C-RW.20 | App F ¶2 | §5 "The uniform trim: a short history" (14–19); §5 "Sharpness" (20) |
| C-RW.21 | — | §8 ¶2 (verbatim) |
| C-RW.22, C-RW.23 | — | §8 ¶3, the provenance paragraph (verbatim); RW.22 also §3 last paragraph |
| C-2.1 | Def B.1 | §3 |
| C-2.2(i), (ii), (iii) | Prop B.2 | §2 (i)–(ii), §3 (ii)–(iii) |
| C-2.3(a), (b), (c) | Thm B.3 | §3 "Nothing is lost" |
| C-3.N, C-3.eq1 | App C opening, eq. (1) | — |
| C-3.1 | Def C.1 and the parity paragraph | §4 "The valuation law" (the definition and `M(1) = 0`; the parity clause is formal only) |
| C-3.2 | Lemma C.2 | §1 (ii) ("one squaring lemma") |
| C-3.3(a), (b) | Thm C.3 | §4 "The valuation law" and its table |
| C-3.3(c) | proof of Thm C.3 | — |
| C-3.3(d) | Thm C.3 and proof | — |
| C-3.4 | Lemma C.4 | §4 "The factor of 3" |
| C-3.5(a), (b), (c) | Thm C.5 (`ε → ξ`) | §4 "The next depth" |
| C-3.5.TS | proof of Thm C.5 | — |
| C-3.6 | Remark C.6 | §4 "Checks"; App G row 1 |
| C-3.7, C-3.7.pf | Thm C.7 and proof | §4 "How many digits one step needs" |
| C-3.8 | Thm C.8 | §4 "How many digits one step needs" |
| C-3.8.rate | paragraph after Thm C.8 (outside the statement, N-18) | §4, after "never outputs a wrong value"; App G |
| C-3.9(a)–(e) | Heuristic C.9 | §4 "The digit budget (…; a heuristic, not a theorem)" |
| C-3.10 | Remark C.10 | §4 "Checks"; App G |
| C-3.post | — (moved) | §4 "Where the difficulty is" (v4 words) |
| C-4.setup | App D opening | §5 "A cycle as numbers" |
| C-4.notation | replaced: App D "Notation" + App H rename table (see §4 above) | — |
| C-4.1(a)–(d), C-4.1.BS | Prop D.1 and the paragraph after it | §5 "Size and divisibility" |
| C-4.2 | Cor D.2 (`ε_t → χ_t`) | §5 "Size" |
| C-4.3 | Lemma D.3 (`ε_t → χ_t`) | — |
| C-4.4, C-4.4.p1, C-4.4.p23 | Thm D.4 and outline | §5 "Small periods" (C-4.4) |
| C-4.dict(a)–(e) | App D "The dictionary with m-cycles" | §2 last paragraph (a); §5 "A cycle as numbers" (b)–(e) |
| C-4.cfg(a)–(d) | App D "Configurations" | §5 "Size", "Size and divisibility" ((a), and `γ`, `Λ` of (c)) |
| C-4.eq2 | eq. (2) | — |
| C-4.5(a)–(d), C-4.5.cr | Thm D.5, proof (`T_j → μ_j`), paragraph after | §5 trim history |
| C-4.6.φ, C-4.6.pf.a, C-4.6.eq3, C-4.6.constr, C-4.6.crashD, C-4.6.minimax, C-4.const, C-4.6.pf.iii | proof of Thm D.6 (`T → μ`, `S → s_tot`) | — |
| C-4.6(i)a, (i)b, (i)c, (i)d | Thm D.6(i) | §5 "Sharpness" bullet 1 |
| C-4.6(ii)a, (ii)b, (ii)c | Thm D.6(ii) | §5 "Sharpness" bullet 2 |
| C-4.6(iii)a | Thm D.6(iii) | §5 "Sharpness" bullet 2 |
| C-4.6(iii)b, (iii)c | Thm D.6(iii) | §5 bullet 3 (via C-4.thr.4) |
| C-4.6(iv) Δ (U27) | Thm D.6(iv) (`S − 6 → s_tot − 6`; the 84 and the constant restated, §7a) | §5 "The staircase, as a picture" (with `s_tot − 6 = 49` written out, `K = 149`) |
| C-4.6.close | Thm D.6 closing sentence; proof, last paragraph | §5 "What is left" |
| C-4.thr.1, C-4.thr.2 | App D "The threshold, explicitly" | §5 "Sharpness" bullet 2 (values, "no closed form… nothing below") |
| C-4.thr.3 | App D "The threshold, explicitly" | — |
| C-4.thr.4, C-4.thr.5, C-4.thr.6 | App D "The threshold, explicitly" | §5 "Sharpness" bullet 3 |
| C-4.thr.7 (cut) | **absent**, checked: the canonical-scale sentence is not in the new text | — |
| C-4.7 | Remark D.7 | §5 "The staircase, as a picture" |
| C-4.8(a)–(d) | Remark D.8 (`T → μ`) | — |
| C-4.ver(a)–(d) | App D "Verification and record" | §5 "What is left" (c), (d); App G (a) |
| C-5.null, C-5.depth, C-5.syrac, C-5.joint, C-5.W, C-5.pi, C-5.product, C-5.piledger | App E "The window law" | §6 "Letters and the model law" (syrac, piledger) |
| C-5.1 | Hyp E.1 (`T_N → H_N`, `Λ_N → E_N`) | §6 "The hypothesis" |
| C-5.eq, C-5.lim | App E, after Hyp E.1 | — |
| C-5.adm | App E "The budget and admissibility" | §6 "The hypothesis" (both clauses) |
| C-5.alt, C-5.cut, C-5.prot, C-5.cons, C-5.4mean, C-5.past, C-5.rates | App E "The budget and admissibility" | — |
| C-5.base, C-5.TV | App E "The unconditional base case" (`H → 𝓗`) | §6 "Where it is already a theorem" |
| C-5.thm | App E "The unconditional base case" | §6 "Where it is already a theorem" |
| C-5.clock, C-5.Korec | App E, after the base case | §6 "Where it is already a theorem" |
| C-5.ledger, C-5.dyadic, C-5.union, C-5.descent, C-5.block, C-5.supplies, C-5.exc | App E "What the hypothesis implies, and what it does not" | §6 "What it would give, and what it would not" (all but C-5.block); §1 not-claimed (descent, exc) |
| C-5.cal, C-5.2, C-5.ratio, C-5.limits, C-5.nocut | App E "Calibration" | §6 "How it was tested" (cal, 2, limits) |
| C-D.1, C-D.2, C-D.3 | §7 (verbatim) | §7 |

### Table B

| IDs | New location |
|---|---|
| P-1 | Title (verbatim) |
| P-2 | Title-page footnote (verbatim) |
| P-3 | Date line (verbatim) |
| P-4, P-5 | Version note (verbatim) |
| **P-6** | Version note — **changed by the brief**: "No statement is renumbered" is replaced by "v4 is also rewritten for a curious reader without training in mathematics… Its statements are therefore renumbered, and Appendix H maps v3's numbers to v4's. Outside work that cites this paper's statements by number, including the cycle ledger shared with Eric Merle, cites v3, which remains the pinned citation for that purpose." The version-history pointer is kept. |
| P-7, P-8, P-9, P-11 | Author's note (verbatim) |
| P-10 | superseded at the lock by A-1's settled wording; the Author's note is verbatim |
| P-12 | §1 ¶2 |
| P-13, P-14, P-15 | App F ¶1 (verbatim) |
| P-16 | App F ¶2 (verbatim); §5 trim history ("a rederivation by another route") |
| P-17, P-18 | §8 ¶2 (verbatim) |
| P-19–P-23 | §8 ¶3, the provenance paragraph (verbatim) |
| P-24 | Thm D.4; §5 "Small periods"; §1 not-claimed |
| P-25 | Prop D.1 (verbatim); App D "Notation"; App H |
| P-26 | paragraph after Thm D.5; §5 trim history |
| P-27 | App D "Verification and record" (verbatim) |
| P-28 | App E "The window law"; §6 "Letters and the model law" |
| P-29 | §7 (verbatim) |
| P-30–P-34 | Appendix A (verbatim) |
| P-35–P-40 | Bibliography (verbatim) |
| N-1 | Heuristic C.9; §4 "The digit budget"; §1 not-claimed |
| N-2 | Thm D.4; §5 "Small periods"; §1 not-claimed |
| N-3 | Thm D.5, App F ¶2; §5 trim history; §1 not-claimed |
| N-4 | Thm D.6(i) and proof; §5 bullet 1; §1 not-claimed |
| N-5 | App D "The threshold, explicitly"; §5 bullet 2; §1 not-claimed |
| N-6, N-7 | App D "The threshold, explicitly"; §5 bullet 3 |
| N-8 | Remark D.8 |
| N-9 | App D "Verification and record"; §5 "What is left"; §1 not-claimed |
| N-10 | App E "The window law" |
| N-11 | App E "The window law"; §6 "Letters and the model law"; §1 not-claimed |
| N-12 | App E "The budget and admissibility" |
| N-13 | App E "What the hypothesis implies"; §6; §1 not-claimed |
| N-14 | App E "What the hypothesis implies"; §6 |
| N-15 | App E "What the hypothesis implies"; §6; §1 not-claimed |
| N-16 | App E "Calibration"; §6 "How it was tested" |
| N-17 | App F ¶1 (verbatim) |
| N-18 | the undecided-rate paragraph stays after Thm C.8's proof; in §4 the rate follows the trichotomy as a separate sentence, under the model law with `D ≥ k + 2` |
| N-19 | Abstract; Thm D.6(i); §5 bullet 1 ("nothing is stated at `p = 1`"); §1 not-claimed |

Table C: A-1–A-7 settled at the lock and carried as is. PH-1–PH-8: all placeholders present and rendering as before; the `\recordcommit` comment's location text updated (§1).

## 6. Places where I was unsure a paraphrase kept its scope

Each is in the main text; the formal statement it paraphrases is unchanged. The checker should look at these first.

1. **§1 not-claimed, first bullet: "It does not settle the Collatz conjecture."** Not a ledger row. It is a disclaimer, not a claim, but it is new text.
2. **§5 "Sharpness" bullet 2: "Every odd number below the verified range `2^71` reaches 1 [Barina], so the elements of a nontrivial cycle all lie above it."** This is the inference Lemma D.3's proof already uses ("an element below `p/ln 2 ≤ X₀`, which reaches 1: impossible") from C-RW.12, but it is not a ledger row in this form.
3. **§5 trim history, the plain reading:** "a cycle with many rises needs `2^K` very close to `3^n`; but `κ_p` shrinks like `(log₂3)^{−p}`, so the requirement weakens exponentially as the number of blocks grows." A reading of Thm D.5's inequality and of C-Abs.9 ("constant degrades like `L^{−p}`"); no new content intended.
4. **§5 "Size and divisibility": "A cycle gives a size-passer; a size-passer need not give a cycle."** The second half rests on Thm D.6(iv)'s instances failing `q ∣ R_r`.
5. **§5 picture: "The first six blocks climb, their depths growing roughly geometrically."** The tuple's ratios are 1.29–1.75; "roughly" is meant loosely. `K = 149` and the last exit `49 = s_tot − 6` are computed (`n = 94`, `K = ⌈94 log₂3⌉`; γ = 6.7438 checks, as in the ledger's C-4.6(iv) row).
6. **§4 "The next depth": "an exact formula in the anchor displacement (the difference between the depth and the anchor) and `s`".** The displacement in Thm C.5 is `ξ = n − N(ω)` on `d = 2n` (resp. `n − N(3ω)`), a half-scale form of `d − M(ω)`; "the difference between the depth and the anchor" is loose.
7. **§4 "The anchor": "Every odd number has an inverse among them, and one can take logarithms."** Background on `Z₂`, not a ledger row.
8. **§4 analogy:** "Think of `d` as the reading of a binary counter and `M(ω)` as a fixed reference pattern: the length of the cascade is set by how many low-order bits of the counter match the pattern." Meant as mechanism only (it restates `v₂(d − M(ω))` as a count of matching low bits); the only analogy in the main text.
9. **§6 "Where it is already a theorem":** "the first blocks… are distributed exactly as the model says on the event that they have not divided out more factors of 2 than the start has binary digits (precisely, `S + 1 ≤ J`, with `S` the factors of 2 divided out)". In App E, `S` is the total exponent of the extended `(n+1)`-letter word (`S_{n+1}`), and the window has `2^J` integers; the plain words compress both.
10. **§6 "The hypothesis":** the admissibility clauses are paraphrased ("protected… consistent… the model's own mean spending, 4 factors of 2 per block, fits the horizon inside the budget: `4θ < τ`"); `protected` is quoted in full, `consistent` via `E_B[m + r] = 4`.
11. **§6 "Letters and the model law":** "the rate at which a factor of 3 is gained is 1/3, up to the cap" — App E: "exact up to that same cell, whose parity split the cap hides".
12. **Abstract:** "a digit-budget accounting, stated as a heuristic, indicates…" — "stated as a heuristic" added; it matches the row's grade and weakens nothing.
13. **§1 not-claimed, third bullet:** "The exclusion of cycles with one, two or three blocks, and the uniform trim, are not new… What is offered for them is new derivations." Combines N-2 ("the derivations, not the theorems") and N-3/P-16 ("a rederivation by another route") into one sentence; the credit list folds Rozier 1990 and 1991 into "Rozier".
14. **Version note (P-6):** the new sentence names "the cycle ledger shared with Eric Merle", as the brief asks. It is a provenance statement about outside work, new to the paper.
15. **§2:** "and it was also the author's starting point (Section 8)" — consistent with P-20 (the March 2023 note), but phrased loosely.

Nothing in the main text was found to strengthen a row on re-reading; two drafts that did were fixed before the commit: the §5 opening first said the size arguments "cannot achieve more" without scope (now "at every period `p ≥ 3`, and at every size threshold `X₀` for all periods `p ≥ p₁(X₀)`, the size conditions are met at the scale the classical bound allows", the proof's own closing sentence), and the "Sharpness" lead first said "at every period, and at every size threshold" (now "at every period `p ≥ 3`, and at every size threshold `X₀` once `p ≥ p₁(X₀)`").

## 7. What the author should read first

1. **§2 and §3 (pp. 4–6)** — the `x = 7` example and the states. This is your own layered view (draft000 §2: the map, extended valuation blocks, structural states), and the rest is built on it. If these two sections do not read right, nothing after them will.
2. **§1's "What this paper does not claim" (p. 4)** and the **Version note (p. 2)** — the scope box is new, and the Version note now says the statements are renumbered and v3 stays the pinned citation (including for the Merle ledger). Both are yours to approve.
3. **§5 (pp. 7–10)** — the cycles section is where most scope words live (`p ≥ 3`, `p ≥ p₁(X₀)`, "nothing at `p = 1`", "no bracket at `p ∈ {2,4}`", "not the inequality of Lemme 4", "none bears on whether cycles exist"). The staircase picture is the `p = 7` instance.
4. Then §4 and §6 in order. The appendices are v4's formal text, unchanged apart from the renames in §4 above.

## 7a. Revision round (after the check at `38ea5ee`, `briefs/paper1-v4-readable-check-findings.md`)

**The check's 14 fixes, applied** (one line each):
1. §5 "What is left": "Every statement about the staircase concerns…" (was "in this section", false beside Thm D.4 and Hercher).
2. §5 "What is left": "Parts (i)–(iii) were each checked by independently written code…" (was "Each part", which took in (iv)).
3. §5 trim history: "In this paper's notation, and up to an additive constant, the bound…" (C-4.5.cr's qualifier restored).
4. §1 not-claimed: credit split, "…one, two or three blocks is classical (Steiner; Rozier 1990; Simons–de Weger; Hercher), and so is the uniform trim (Rozier 1991; Simons–de Weger; finiteness at each period is Brox's)".
5. §4 "The next depth": the displacement is "half the difference between the depth and the anchor, taken 2-adically".
6. Version note: "the statements, with their proofs or the record sections that hold them, are in Appendices B–E". The Merle/v3 sentence is unchanged, awaiting the author.
7. §2 opening: "Long stretches of a Collatz orbit are forced."
8. §5 opening: "…or an orbit that falls into a cycle not containing 1."
9. App H: "The symbols below are renamed; no meaning changed."
10. App H: the rename row is now `S` (Theorem 4.6(iv)) → `s_tot` (Theorem D.6(iv) and its proof).
11. App G, the Theorem D.6(i) row: the 45 checks are attributed to `staircase_gamma_upper.py` alone, and the sweep, bracket, window counts and construction to the two `staircase_allp` scripts.
12. App G's record-only list: four items added — `cycles.md` Remark 12.6.1.7 (the integer form of the elimination identity), `cycles.md` §12.4 (the deep-entry clause of the dictionary), `aeh.md` §13.6 (the depth renewal law) and `aeh.md` §13.6.5 (the `Syrac` normalisation). The record's construction, wrongly listed earlier, had already been removed.
13. "Each result stated informally…" (§1); §2 now says "it is the mechanism of the author's hand-drawn note of March 2023".
14. X-1 and X-2 became U26 and U27, below.

**Readability.** §1 "What is new" is rewritten in plain words, each item led by what it does for the reader, with the technical name, the pointer and every scope word in the closing parenthesis. §4 drops the 2-adic preamble and the counter analogy. The anchor is now defined inside the valuation law, with one sentence of support: "The law describes a step; it does not shortcut one: computing `M(ω)` to the digits needed costs about as much as computing the valuation directly", cited to the record (`briefs/williams-letter-findings.md`, which states it). That sentence is not a ledger row. The parity clause of C-3.1 (`M(ω)` even iff `ω ≡ ±1 (8)`) is no longer restated in the main text; it lives only in Definition C.1.

**Locked-text corrections (content; ledger rows updated):**
- **U26.** In "The threshold, explicitly", `p₁ − log_L X₀ ∈ [2.784, 10.629]` becomes **`[2.783, 10.630]`**, rounded outward. The exact extremes are `2.7839895` (`j = 143`, `p₁ = 218`) and `10.6294771` (`j = 74`, `p₁ = 122`), recomputed here from those `p₁` values at 30 digits. The same change is made in ledger row C-4.thr.1, in `briefs/staircase-x0-threshold-findings.md` (two places) and in `briefs/x0-threshold-independent-check-findings.md`. No wiki page carries the range. `briefs/paper1-v4-fixpass-findings.md` U20 is left as it stands, as the record of that pass.
- **U27.** In Theorem D.6(iv), and in §5's picture, the 84 instances are now said plainly. They come from a seeded random search at `p = 6` (`experiments/uniform_trim.py`, `random.seed(41)`), and none of them falls below the period-3 trim's constant, now defined as `γ > 0.1157n − 2` (`cycles.md` Lemma 12.7.4): each clears it by at least `0.698`. Only the `p = 7` instance falls below it. Re-run this window: 84 passers, `n ∈ {20, 22, 27, 29, 34, 41, 46}`, minimum margin `0.6987`, none divisible. Ledger row C-4.6(iv) was updated (marked Δ) and App G's row too.

**Build:** 3× in the temp dir, 33 pp, 0 undefined references, 0 overfull boxes. Encoding scan clean. Content commit `03fdf7b`.

## 7b. Readability round 2 (branch `paper1-v4-readable-2`, base `c7c3c69`)

**The author's verdict:** "still too clunky to read; e.g. χ is mentioned without introduction". Presentation only; no locked claim changed.

**Main-text symbols.** §§1–8 now use only these: `x`, `T`, `m`, `s`, `a`, `ω`, `d`, `(ω, d)`, `F`, `p`, `n`, `K`, `q`, `γ`, `X₀`, `p₁(X₀)`. Each is introduced in words before it is used, and all are listed on the new "Symbols at a glance" page after §1. There is one exception: the provenance paragraph in §8 is kept verbatim, with its `x + 1 = 2^m 3^a ω`; its `(λ, k)` are introduced in the same sentence. Gone from the main text: `χ_t`, `σ`, `k`, `D`, `π_{k,D}`, `θ`, `τ`, `N`, `b`, `H_N`, `E_N`, `ε`, `X_N`, `J`, `S`, `M(ω)`, `ΔM`, `a₊`, `m₊`, `s₊`, `R_r`, `κ_p`, `λ₀`, `c_p`, `log₂3` as a symbol (now "1.585…, the base-2 logarithm of 3"), `x_exit`, `u`, `W`, `z`.

**Formula sentences removed: 53**, counted by section: §1 3, §2 3, §3 5, §4 13, §5 19, §6 9, §7 1. Each is now said in words, and its pointer is kept. Every formula removed was already in the appendix statement it points to, with one set of exceptions: `T`'s formula, the definitions of `v₂` and `v₃`, and the rising-step identity `T(x) + 1 = (3/2)(x + 1)`. These moved into Appendix B's opening paragraph; that paragraph is the only text added to Appendices B–E. Constants in the main text are now either exact numbers quoted as numbers (`0.054`, `0.698`, the `p₁` values) or approximations marked "about" with the exact statement named (`3.68`/`5.14` for Thm D.6(i); `2.71`/`4.21` for `λ₀`, `λ₀ + 1.5`).

**Paraphrases to check first** (main text only; the formal statements are unchanged):
- §5 "Sharpness", bullet 2: "the base-2 logarithm of its least element lies within about the base-2 logarithm of `p` of `γ`", for `γ − 1 ≤ log₂(x_min + 1) < γ + log₂ p` (Thm D.6(ii)).
- §5, bullet 1: "the factor in any trim of this shape that holds for every size-passer is smaller than 1.585… to the power `−p` times a quantity growing only like the logarithm of `p`", for `c_p < (5.140212 + log₂ p) L^{−p}`.
- §4: "finitely many binary digits of `ω` and of `d`, together with the low digits of the absorption" (Thm C.7's exact residues).
- §4 digit budget: "at most a number of decided steps proportional to its length" (`O(W/(k + 6))`).
- §6: the coding fact, now "any run of consecutive integers whose length is a power of 2 … on the event that they have divided out fewer factors of 2 than the exponent of that power".
- §6: "protected", now "above any level that grows more slowly than every fixed power of the starting size" (`log X_N = o(log N)`).

**New:**
- "Symbols at a glance": the main-text symbols with meaning and place, and the words used as names (block, anchor, configuration, size-passer, trim, letter).
- **Appendix I, Symbol index:** every symbol of the paper, with meaning and defining location. Overloaded letters are listed once per meaning: `n`, `q`, `r`, `k`, `X₀`, `β`, `A`, `S_t`, `e_t`, `σ` (also "5σ"), `ε`.

**Version note:** "Outside work that cites this paper's statements by number, including the cycle ledger shared with Eric Merle, cites v3, …" is now "For outside citations of this paper's statements by number, v3 remains the pinned citation." This is the author's decision.

**Pages (37):**
- front matter pp. 1–2;
- §1 pp. 2–4;
- Symbols at a glance p. 5;
- §§2–8 pp. 5–14;
- appendices A–I pp. 14–35 (I is pp. 33–35);
- references pp. 35–37.

Main text ≈ 13 pp.

**Build and commits:**
- **Build:** 3× in a temp dir, 0 undefined references, 0 overfull boxes. Encoding scan clean.
- **Content commit:** `35abcdb`.
- **This record:** the following commit.

## 7c. Readability round 3 (after the cold read, `briefs/paper1-v4-coldread-1.md`, 166 flags)

Branch `paper1-v4-readable-2`, on top of `6eb5946`. The author gave the go-ahead on 2026-10-20. Presentation only; no locked claim changed. The appendices only received moved text: the technical abstract (verbatim, as the opening "Technical summary") and §8's contemporary-work paragraph (verbatim, at the end of Appendix F). One sentence of the technical abstract was dropped: "The main text tells each idea in words; …". It was my own round-1 addition, not a claim.

**What changed, by the coordinator's items:**
1. **Abstract.** It is now in plain language, with no symbols. The technical abstract is verbatim in "Technical summary" at the start of the appendices; it also serves as the Zenodo description.
2. **Symbols at a glance.** It now sits after the Author's note and before §1, and now includes `λ`, `k`. Its claim is corrected: it lists every symbol used outside the appendices. The abstract and §1 now use no symbols. The "words used as names" paragraph is removed; each name is now defined where it is used.
3. **Running examples.**
   - **The orbit of 7** runs through §§2–5. §3 shows every transition: `(1,3)` exits at 13; `(7,1)` falls 40 → 5 with `s = 2`; `(1,2)` falls 16 → 1 with `s = 3`; `(1,1)` falls 4 → 1 with `s = 1`.
   - **§4** checks each law on it: the valuation table, the lifting example `(1,2)`, the factor of 3 at `(7,1)` (`21 + 3 = 24`), and the next depth.
   - **§5** uses two examples: the trivial cycle (`n = 1`, `K = 2`, `q = 1`, `γ = 2`, rotation number `= q`) and the `p = 7` staircase.
   - **§6** writes the example's letters, `(3,1)`, `(1,2)`, `(1,3)`, `(1,1)`, and gives the tally example (40 digits, horizon rate 1/10, budget rate 1/2).
4. **Gaps.** Each now has its one line of reason:
   - why a rising step halves once;
   - why the trade stops;
   - why the exit depends only on `(ω, d)`: one more than the last rising number is `2 · 3^{d−1} · ω`;
   - why exactly `d` numbers share a state;
   - "nothing is lost", as three facts;
   - why `s ≥ 3` on lifting kinds, and why `s` is fixed elsewhere (powers of 3 mod 8);
   - "exactly when `s` is even" (powers of 2 mod 3);
   - "`q` is at most each" (a positive multiple of `q` is `≥ q`);
   - "consequently … intrinsic" (the trim applied to the staircase);
   - the 1/3 rate (`1/4 + 1/16 + … = 1/3`);
   - the mean of 4 halvings per block;
   - why the averages are not controlled;
   - budget rate below 1 ⟺ horizon rate below 1/4.
5. **Jargon.** Each term is glossed at first use or removed from the main text. Long sentences are split into short ones and lists (§4's three outcomes, §5's history and sharpness, §6's "would not give" and the calibration).
6. **§8.** The contemporary-work paragraph is in Appendix F. A plain paragraph before the provenance paragraph glosses its three terms (skeleton rows, representative fibre, intra-block cascade). "Her open problem" is now "Williams's open problem". The provenance paragraph is otherwise verbatim.
7. **(d)** The staircase now reads "the exit valuations total 55; and so the halvings total `K = 94 + 55 = 149`". §5 says that a block halves `m + s` times, so `K = n + Σ s`. **(e)** §6 now has a paragraph "What is proved, and what is conjectured": the base case (budget rate below 1) is proved, assembled in the record; the rest is conjectured. §1's not-claimed bullet reads "a conjecture, apart from the range where it is proved".

**Cold-read items: 157 fixed, 1 partly fixed, 8 not fixed.**

| Items | Status | Note |
|---|---|---|
| 1–19 (abstract) | fixed | new plain abstract; the technical terms are in the Technical summary |
| 20 (version note: theorem labels before content) | not fixed | the version note must list v3 → v4 changes, and the labels are links; its symbols are removed |
| 21 (record sections) | fixed | "sections of the project record" |
| 22 (pinned citation) | not fixed | the author's own wording (round 2) |
| 23, 24, 25 (Author's note) | not fixed | verbatim, the author's voice; 24 is mitigated by Symbols at a glance directly after |
| 26–51 (§1) | fixed | §1 rewritten without symbols; terms glossed or moved to their section |
| 52–56 (symbols page) | fixed | moved before §1, completed, claim corrected, names paragraph removed |
| 57–64 (§2) | fixed | reasons and worked numbers added; one-division map named |
| 65–71 (§3) | fixed | reasons, transitions, three facts |
| 72–76, 78–93 (§4) | fixed | |
| 77 (no-shortcut sentence: no reason given) | not fixed | the record states it without proof (`briefs/williams-letter-findings.md`); a reason would add a claim |
| 94–131 (§5) | fixed | 113 (55 vs 149) resolved by saying what `K` counts |
| 132–155 (§6) | fixed | 143 resolved by "What is proved, and what is conjectured" |
| 156–159 (§7) | fixed | 158: the costumes metaphor is kept, now glossed by the staircase sentence |
| 160–162 (§8) | fixed | related work moved to App F |
| 163 (mechanism "comes from … and is classical") | not fixed | verbatim provenance paragraph; §2 now separates the two |
| 164 (skeleton rows, fibre, cascade, `λ`, `k`) | fixed | glossed in the paragraph before; `λ`, `k` in the symbols page |
| 165 ("Her open problem …") | partly | "Williams's open problem"; the rest of the sentence is the verbatim provenance paragraph |
| 166 (analytical superstructure) | not fixed | verbatim provenance paragraph |

**New paraphrases to check against the ledger:**
- the plain abstract, whole (C-Abs.1–18);
- §1 "What is new" (v), "reaches the optimum Rozier identified (the minimax value of his extremal profile)" (C-Int.9);
- §5: "a bound as strong as the three-block one would wrongly exclude this seven-block size-passer, and the requirement must weaken as the number of blocks grows" (C-4.6(iv)). The second clause is a reading of the example;
- §5 history: Brox, "only finitely many cycles can have any given number of local minima" (C-RW.15);
- §6: the base-case example, "among the odd numbers of any run of 1024 consecutive integers … each pattern of first blocks that uses fewer than ten halvings in all, counting the start's own block, occurs in exactly its fair-coin share" (C-5.base, `S + 1 ≤ J` with `J = 10`);
- §6 "would not give", bullet 1 (C-5.union) and bullet 4 (C-5.exc, non-iteration);
- §6: Inselmann's crossing, "for the range within which an orbit stays and for its average" (the trajectory envelope and first moment, C-5.Korec).

**Pages (41):**
- front matter pp. 1–2;
- Symbols at a glance pp. 2–3;
- §1 pp. 3–6;
- §§2–8 pp. 6–17 (main text ≈ 16 pp);
- Technical summary p. 17;
- Appendices A–I pp. 17–39;
- references pp. 39–41.

**Build:** 3× in a temp dir, 0 undefined references, 0 overfull boxes. Encoding scan clean. Content commit `c565330`.

## 7d. Readability round 4

Branch `paper1-v4-readable-2`, head `c9ef1bb` at the start of the round. The inputs were the round-3 scope check (`904dcc6:briefs/paper1-v4-readable-3-check-findings.md`) and cold read 2 (`briefs/paper1-v4-coldread-2.md`, 97 flags). Presentation only, apart from the scope fixes, which restore locked scope. The only appendix changes are the navigation fix in Appendix I and the paragraph that round 3 moved into Appendix F. Content commit `60522a7`.

**Scope check, §4 (11 scope changes, 1 unsupported sentence): all done.**

| Id | Done as |
|---|---|
| 1 (Ab10, I15) | "no cycles other than 1, 4, 2, 1" made of / with one, two or three blocks (abstract; §1 (v)) |
| 2 (Ab11) | "how many odd steps (multiplications by 3)" |
| 3 (Ab14) | "with their measure of closeness exceeding the classical bound's own exponent by at most a fixed amount" |
| 4 (Ab16) | "ruling out cycles of every length at once needs divisibility" |
| 5 (Ab17) | "the record's length, itself a fixed multiple of the start's number of binary digits" |
| 6 (Ab19) | "shows that the fair-coin conjecture holds outright … (the proof is assembled in the project record)" |
| 7 | = 1 |
| 8 (A30) | "The three outcomes were run along real orbits, 21,296 steps, with zero errors" |
| 9 (C22) | "the more multiplications by 3 a cycle has (the larger n)" |
| 10 (C30) | "at seven blocks the requirement must be weaker than at three. (That it must weaken exponentially … is part (i) below.)" |
| 11 (C50) | "The staircases pass every size condition, and every one tested fails the divisibility conditions." |
| 12 (A11, unsupported) | "The law describes a step; it is not offered as a faster way to compute one." The cost claim and the `briefs/` pointer are gone. |

**Navigation notes (4) and the optional one: all done.** The `p`-adic / `m`-cycle note is on the symbols page. The running example now "runs through Sections 2–4, and its blocks return in Section 6". Appendix I now says "before Section 1". The §8 gloss now says "elsewhere in this paper `cascade' means only the block's final burst of halvings". H25 now reads "for the proportion of its steps that are odd".

**Coordinator items 2–6:**
- **§4.** The section is rebuilt as:
  1. the eight-kind table;
  2. on six kinds `s` is the entry; on the two lifting kinds `s ≥ 3`, set by "a fixed binary pattern that belongs to ω";
  3. the ω = 1 table, d = 2, 4, 6, 8 → s = 3, 4, 3, 5, checked by hand: `3^d − 1` = 8, 80, 728, 6560 = 8·1, 16·5, 8·91, 32·205;
  4. "why the table holds";
  5. only then, the name "anchor", with the pointer to Definition C.1.

  "2-adic logarithm" and "infinite binary arithmetic" are gone from §4. "Anchor displacement" is replaced by "how `d` compares with the anchor (Theorem C.5)". The only remaining "2-adic logarithm" in the main text is in §7's third direction, glossed as "the digits of the anchors — in the usual terms, …". It keeps C-D.3's wording findable.
- **§5.**
  - The trim + Rhin step is now three numbered lines: (a) the trim, (b) Rhin's lower bound on how close the powers can be, (c) linear against logarithmic.
  - Simons and de Weger's `m`-cycle is now "a p-cycle in Simons and de Weger's sense (their `m-cycle', …)".
  - "One object" is now "in this one configuration, the cycle side and the ever-growing side of the problem meet".
  - The trim is named and pointed to at its first use in §1 and in the §5 opening.
- **§1.**
  - "eight kinds" now reads "Section 4 sorts the states into eight kinds by two simple remainders".
  - "three labels" is spelled out.
  - "the trim" is introduced as "that Section 5 calls the trim".
  - The one-line identity is marked "(stated in Section 5)".
- **Out-of-paper pointers.**
  - `aeh.md Lemma 13.2.4` → "Appendix E, 'The unconditional base case'; proof assembled in the project record, Appendix G".
  - `aeh.md Proposition 13.2.5` → "Appendix E, 'What the hypothesis implies'; proof assembled in the project record, Appendix G".
  - `briefs/williams-letter-findings.md` → removed with the cost claim.
- **§7.** "A single question wearing two costumes" is now "one difficulty, seen from two sides", and the staircase is "a single configuration that belongs to both sides". The divisibility pointer is now Proposition D.1, with Theorem D.6 for "size alone cannot decide" (cold-read 92).

**Cold read 2 (97 items): 73 fixed, 18 needed no fix, 6 not fixed.**

| Items | Status |
|---|---|
| 1–5, 10–21, 24, 28–34, 36–46, 48–50, 53–55, 57–59, 61–68, 70, 72–74, 76, 78–86, 88–93 | fixed |
| 9, 22, 23, 25, 26, 27, 35, 47, 51, 52, 56, 60, 69, 71, 75, 77, 87, 94 | no fix needed: the reader marked them READABLE or the arithmetic OK |
| 6, 7 (Author's note) | not fixed: verbatim, the author's voice |
| 8 (version chain) | not fixed: the version note must carry v3 → v4 |
| 95, 96, 97 (provenance paragraph) | not fixed: verbatim, apart from round 3's "Williams's" |

**Paraphrases to check:**
- §4: "s is set by a fixed binary pattern that belongs to ω, running on to the left without end" (C-3.3(a));
- §4: the next entry depth "by an exact formula in s and in how d compares with the anchor" (C-3.5);
- §5: (b) "γ can grow at most like a fixed multiple of the logarithm of n", from Rhin's display in Thm D.5;
- §5: "That multiplier currently depends on p" (C-4.thr.5);
- §5: "(These are samples …; the record computes p₁(X₀) at every power of 2 up to 2^200)" (C-4.ver(a));
- §6: "(1) and (2) … artifacts of including small starting values, which the sharper control set aside" (C-5.cal);
- §6: the 1024-integer reason, "each such class equally often" (C-5.base).

**Pages (42):**
- front matter and Symbols at a glance pp. 1–3;
- §1 pp. 3–6;
- §§2–8 pp. 6–18 (main text ≈ 17 pp);
- Technical summary p. 18;
- Appendices A–I pp. 18–41;
- references pp. 41–42.

**Build:** 3× in a temp dir, 0 undefined references, 0 overfull boxes. Encoding scan clean.

## 7e. Readability round 5 (option A)

Branch `paper1-v4-readable-2`, starting from `e0da786` (which adds cold read 3). The author chose option A on 2026-10-20. Presentation only. Content commit `ee20c3a`.

**Restructure.** §§4, 5 and 6 are now one page each, in four parts: what is claimed, why it matters, one worked example, and the full account. Everything else they carried moved, in its round-4 wording with the fixes below, into a plain-language "A guided account" at the start of Appendices C, D and E, before the formal statements ("The formal statements" in C and D; in E, the existing subsections from "The window law" on). The guided accounts carry exactly what §§4–6 carried in round 4, so every ledger location that round 4 put in §§4–6 is now in the matching guided account. §7 is now one paragraph. "How to read" describes the new shape. The Symbols page drops `q`, `γ`, `X₀`, `p₁(X₀)`, which no longer appear in the main text, and points to the appendices for them.

**Round-4 scope check (`98665e3`), all four fixes applied:**
1. §1: "that is not the same as saying that almost no orbits misbehave".
2. App E guided account: "a question about the digits of the anchors … — in the usual terms, digits of 2-adic logarithms of whole numbers … — and questions of that kind are older and broader than the Collatz problem". §7 attaches the phrase the same way.
3. App D guided account: Lemme 4's extra term is now "larger throughout this range than 2 to the power (n times the shrinking factor)".
4. App E guided account: the clause ", which the sharper control set aside" is dropped.

**Cold read 3's four inconsistencies:**
- **(a)** §1 (ii) now reads "the number of halvings, beyond the first, that end each block". §4 uses the same wording.
- **(b)** The `p = 7` staircase is v3's instance: it is in v3's `.tex` with `γ = 6.74`. Its `γ` lies outside part (i)'s bracket `[3.683012, 5.140212]`; part (i) covers `p ≥ 16` by proof and `3 ≤ p ≤ 15` in the same bracket. It is Theorem D.6(iv), from `uniform_trim.py`. §5 and the App D guided account now both say "v3's instance, … not a member of the family of part (i), whose closeness measure lies between about 3.68 and 5.14 — this one's is 6.74". Checked against v3 and Appendix D before writing.
- **(c)** §8 now reads "Section 4 answers it in part. It gives exact laws for where a trajectory leaving a row lands — the exit valuation and the entry position, and hence which row is entered. It gives no law for which skeleton is entered: on that question, F only restates Williams's Proposition 3.10." Only that sentence of the provenance paragraph changed.
- **(d)** The 62,937 sentence is left in place and marked `% PENDING-REVERIFY` in all three places it lives: App C's guided account, before Remark C.6, and before App G's table.

**The new main-text §§4–6, ledger-relevant paraphrases to check:**
- **§4.** Claimed: exact rules for `s` (eight kinds; six fixed at 1 or 2; lifting `s ≥ 3`, from the anchor's digits), for the factor of 3 (exactly when `s` is even), and for the next depth; and the window never errs (C-3.3, C-3.4, C-3.5, C-3.7, C-3.8). Why: the digit budget, "stated as a heuristic and not proved" (C-3.9, N-1); "the difficulty sits in one place" (C-Int.14).
- **§5.** The trim's history in one line; "with Rhin's theorem it leaves only finitely many candidates at each p" (C-4.5(c)); the rederivations (C-4.4, "no cycles other than 1, 4, 2, 1"); the staircase scope: "every choice of starting block, from 3 on (16 by proof, 3–15 by computer check; 2 and 4 examples without that range)", and the threshold clause without symbols (C-Abs.11–12, C-4.6). Why: divisibility, Halbeisen–Hungerbühler, "every one tested fails", "none bears on whether cycles exist" (C-4.6.close, C-4.ver(c)(d)).
- **§6.** The conjecture, with budget, horizon, admissibility and every finite length kept (C-Abs.15, C-5.1); "part of it is proved … (the unconditional base case; proof assembled in the project record, Appendix G)" (C-5.thm); "its consequences are proved on the condition that it holds" (C-Abs.16); "says nothing about where any single orbit ends up" (N-15).

**Pages (44):**
- front matter and Symbols at a glance pp. 1–3;
- §1 pp. 3–6;
- §§2–3 pp. 6–8;
- §4 p. 8;
- §5 p. 9;
- §6 pp. 9–10;
- §§7–8 pp. 10–11;
- **main text ≈ 9 pp of sections (pp. 3–11)**;
- Technical summary pp. 11–12;
- Appendices A–I pp. 12–43;
- references pp. 43–44.

**Build:** 3× in a temp dir, 0 undefined references, 0 overfull boxes. Encoding scan clean.

## 8. Record

**Commits** (branch `paper1-v4-readable`, base `46e7464`):
- `d421851` — content: the rewritten `.tex` and the rebuilt PDF;
- the commit carrying this file (structure).

Nothing was pushed. No wiki page, ledger file or version-history file was edited. The claims ledger `paper/collatz-reduced-v4-claims.md` was not changed; it still reads against the lock, and §5 above is the bridge.
