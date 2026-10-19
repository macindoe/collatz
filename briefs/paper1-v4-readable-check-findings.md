# Findings: claim-by-claim check of the readable rewrite of paper 1 v4

**Task:** `briefs/paper1-v4-readable-check-brief.md`. Branch `paper1-v4-readable-check`, cut from `paper1-v4-readable` at **`c1d4b57`** (the brief's commit; the rewrite is `d421851`, its record `82da95c`). Baseline: tag `paper1-v4-content-lock` (`paper/collatz-reduced-v4-claims.md` and `paper/collatz-reduced-v4.tex` at the tag). Done 2026-10-19. The `.tex` was not edited; nothing went outward.

**Verdict in one paragraph.** The appendices are the locked formal text: a token-level diff finds only the declared renames, cross-reference rewording, new labels and headings, the declared replacement of "Overloaded symbols", and the declared move of C-3.post into §4. No ledger row is missing. 241 of the 249 rows checked keep their scope. 8 change scope, and all 8 changes are in main-text paraphrases or in the new notation and version-note text, never in a formal statement. The serious one is §5 "What is left": "Every statement in this section … none bears on whether cycles exist". The same section states Theorem D.4 and Hercher's exclusion, so the sentence is false where it stands. There are seven more unsupported or over-wide sentences, and there are small errors in Appendices G and H. Every worked example was recomputed and holds: **57 checks, 0 failures; 7 negative controls, all rejected.** The concordance is correct in all 25 number rows. One rename row is wrong (`s_tot` is not new in v4). Build: 33 pp, 0 undefined references.

---

## 1. Item 1 — mechanical diff of Appendices B–E against the locked §§2–5

**Method.** I tokenised the locked `.tex` lines 81–540 (§2 to the end of §5) and the new lines 248–724 (App B to the end of App E) into LaTeX control words, alphanumeric runs and single symbols. I then ran `difflib.SequenceMatcher` on the token streams (22,158 tokens old, 22,101 new), and classified every non-equal opcode by hand. The diff script is in the session scratchpad and is not a deliverable. The same tool was run on every block the writer calls verbatim.

**Result: 127 hunks, every one of them a declared change.**

| Class | Hunks | What |
|---|---|---|
| Section titles, labels, "This appendix states formally what Section X tells in words", `\subsection*` headings | 1–8, 18, 26, 95–97, 99, 108, 118, 121, 126–127 | `def:anchor` and `rem:verify2` added; §5's `\paragraph{Calibration.}` becomes `\subsection*{Calibration}`; four new `\subsection*` in App E |
| `Section~\ref{sec:…}` → `Appendix~\ref{app:…}`, "this section" → "this appendix", "cited in Related work" → "cited in Appendix F" | 14–17, 36–38, 98, 124, 125 | cross-references only |
| C-3.post removed from the formal text (end of §3) | 19–25 | the paragraph "Heuristic 3.9 is the paper's organizing negative observation … we know of no residual content outside those two" now closes main §4 "Where the difficulty is", word for word |
| "Overloaded symbols" → "Notation" | 27–35 | declared replacement (C-4.notation, see §2) |
| renames `ε→ξ` (Thm C.5), `ε_t→χ_t` (Cor D.2, Lemma D.3), `T_j→μ_j` (proofs of D.5, D.6, Remark D.8), `S→s_tot` (D.6(iv) and proof), `Λ_N→E_N`, `T_N→H_N`, `H→𝓗` | 9–13, 39–94, 100–107, 109–117, 119–120, 122–123 | every occurrence; no other token changed |

No other difference. Nothing was reworded inside a statement, proof, remark, constant or record pointer, and the order is unchanged.

**The other blocks called verbatim** (same tool): title, footnote and date line (0 hunks); Author's note (0); Appendix A (0); §7 against the lock's Discussion (0); §8 ¶2–¶3 against the lock's related-work ¶3–¶4 (0); Appendix F against related-work ¶1–¶2 (10 hunks, all `Section`→`Appendix` references); bibliography (0). The abstract differs by exactly the five declared insertions: the two plain opening sentences, "We study … compresses" → "We compress each such", ", stated as a heuristic,", "(`fair-coin')", and the closing layout sentence. The Version note differs by exactly the P-6 replacement. In §1, "What is new" (i)–(vi) is the lock's Contributions paragraph word for word, apart from pointer additions (Appendix/Theorem/Lemma refs).

**Build (item 6).** `pdflatex` ×3 in the session scratchpad: **33 pages, 0 undefined references or citations, 0 multiply defined labels, 0 overfull boxes**. Its `pdftotext` (blank lines ignored) is identical to that of the committed `paper/collatz-reduced-v4.pdf`.

---

## 2. Item 2 — every live Table A row, every P row, every N row

I placed each row myself: the formal place comes from the diff above, and the main-text place from reading §§1–8 sentence by sentence. The writer's table (`briefs/paper1-v4-readable-findings.md` §5) agrees with mine wherever it gives a place. It marks no scope change; I find 8, all in its "main text" column or in text new to v4.

**Counts (249 rows: 190 live Table A + 40 P + 19 N):**

| Verdict | Rows |
|---|---|
| present, same scope | **241** |
| present, scope changed | **8**: C-3.5(a), C-4.notation, C-4.5.cr, C-4.ver(a), C-4.ver(d), P-6, N-2, N-3 |
| missing | **0** |

C-4.thr.7 (cut) is confirmed absent: there is no "canonical scale" sentence outside Remark D.8's pointer to the record's construction, which is locked text.

### 2.1 Table A

"Formal" is the place where the locked words stand unchanged, up to the renames. "Main" is where the plain-words text restates the row; "—" means the row is only in the formal text.

| Row(s) | Formal | Main | Verdict |
|---|---|---|---|
| C-Abs.1 | Abstract | §1 (i); §3 "Nothing is lost" | same |
| C-Abs.2 | Abstract | §4 opening ¶ ("All of them except the absorption are governed by one number … its anchor; the absorption obeys its own exact law") | same |
| C-Abs.3 | Abstract | §4 "The valuation law" | same |
| C-Abs.4 | Abstract | §4 "The next depth" | same (see C-3.5(a) for the gloss) |
| C-Abs.5, C-Abs.6 | Abstract | §4 "How many digits one step needs" | same |
| C-Abs.7 | Abstract (+ "stated as a heuristic") | §4 "The digit budget (…; a heuristic, not a theorem)" | same (insertion matches the grade) |
| C-Abs.8 | Abstract | §5 "Size and divisibility", "Small periods" | same |
| C-Abs.9 | Abstract | §5 "The uniform trim: a short history" | same |
| C-Abs.10, C-Abs.11 | Abstract | §5 "Sharpness" bullet 1; §1 not-claimed bullet 4 | same |
| C-Abs.12 | Abstract | §5 "Sharpness" bullet 2 | same |
| C-Abs.13 | Abstract | §5 "Sharpness" bullet 3 | same |
| C-Abs.14 | Abstract | §5 trim history (HH 1997); "What is left" | same |
| C-Abs.15 | Abstract (+ "(`fair-coin')") | §6 "The hypothesis" | same |
| C-Abs.16 | Abstract | §6 "What it would give" | same |
| C-Abs.17 | Abstract | §6 "Where it is already a theorem" | same |
| C-Abs.18 | Abstract | §6 "How it was tested" | same |
| C-Int.1 | — (intro rewritten) | §1 ¶1 (definition of `T`, Tao's `Syr`, the conjecture) | same |
| C-Int.2 | — | §1 ¶2 (lock words); §5 opening | same |
| C-Int.3 | Prop B.2 | §2 (general statement + "classical observation (Steiner; …)") | same |
| C-Int.4 | Def B.1, Thm B.3 | §3 ¶1–3 | same |
| C-Int.5–C-Int.10 | — | §1 "What is new" (i)–(vi), the lock's words | same |
| C-Int.11, C-Int.12, C-Int.13, C-Int.14 | — | §4 "Where the difficulty is" (lock words; "a digit-budget accounting" → "the digit-budget accounting") | same |
| C-Int.15 | Remark D.7 | §5 opening; §5 "The staircase, as a picture" (last sentence) | same |
| C-Int.16 | App E "The window law" | §6 opening; §6 "Letters and the model law" (last sentence) | same |
| C-RW.1–C-RW.11, C-RW.13 | App F ¶1 | RW.13 also §5 "Size and divisibility" | same |
| C-RW.12 | App F ¶1 | §5 "Sharpness" bullet 2 (with an inference, see §3 S4) | same |
| C-RW.14–C-RW.19 | App F ¶2 | §5 trim history | same |
| C-RW.20 | App F ¶2 | §5 "Sharpness" | same |
| C-RW.21 | — | §8 ¶2 (verbatim) | same |
| C-RW.22 | — | §8 ¶3 (verbatim); §3 last ¶ | same |
| C-RW.23 | — | §8 ¶3 (verbatim; "Section~\ref{sec:anchor}" now resolves to main §4, which states the laws in words) | same |
| C-2.1 | Def B.1 | §3 | same |
| C-2.2(i), (ii), (iii) | Prop B.2 | §2 (i)–(ii); §3 (ii)–(iii) | same |
| C-2.3(a), (b), (c) | Thm B.3 | §3 "Nothing is lost" | same |
| C-3.N, C-3.eq1 | App C opening, eq. (1) | §4 "The anchor" (background) | same |
| C-3.1 | Def C.1 + parity paragraph | §4 "The anchor" | same |
| C-3.2 | Lemma C.2 | §1 (ii) | same |
| C-3.3(a), (b) | Thm C.3 | §4 "The valuation law" + table (recomputed, §4) | same |
| C-3.3(c), C-3.3(d) | Thm C.3 and proof | — | same |
| C-3.4 | Lemma C.4 | §4 "The factor of 3" | same |
| **C-3.5(a)** | Thm C.5 (`ε→ξ`) | §4 "The next depth" | **scope changed** (gloss), see 2.4 |
| C-3.5(b), (c), C-3.5.TS | Thm C.5 and proof | §4 "The next depth" ((c)); — | same |
| C-3.6 | Remark C.6 | §4 "Checks"; App G row 1 | same |
| C-3.7, C-3.7.pf | Thm C.7 and proof | §4 "How many digits" | same |
| C-3.8 | Thm C.8 | §4 "How many digits" | same |
| C-3.8.rate | ¶ after Thm C.8's proof | §4, a separate sentence after the window's guarantee | same (N-18 kept: the formal statement does not carry it) |
| C-3.9(a)–(e) | Heuristic C.9 | §4 "The digit budget" | same ("the heuristic does not depend on the constant" is omitted in §4; still in C.9) |
| C-3.10 | Remark C.10 | §4 "Checks"; App G | same |
| C-3.post | — (moved) | §4 "Where the difficulty is", verbatim | same |
| C-4.setup | App D opening | §5 "A cycle as numbers" | same |
| **C-4.notation** | replaced: App D "Notation" + App H rename table | — | **scope changed**, see 2.4 |
| C-4.1(a)–(d), C-4.1.BS | Prop D.1 + ¶ after | §5 "Size and divisibility" | same |
| C-4.2 | Cor D.2 (`ε_t→χ_t`) | §5 "Size" | same |
| C-4.3 | Lemma D.3 (`ε_t→χ_t`) | — | same |
| C-4.4, C-4.4.p1, C-4.4.p23 | Thm D.4 + outline | §5 "Small periods" (C-4.4 verbatim) | same |
| C-4.dict(a)–(e) | App D "The dictionary with m-cycles" | §2 last ¶ (a); §5 "A cycle as numbers" (b)–(e) | same |
| C-4.cfg(a)–(d), C-4.eq2 | App D "Configurations", eq. (2) | §5 "Size" (`γ`, (c)); "Size and divisibility" ((a)) | same |
| C-4.5(a)–(d) | Thm D.5 (`T_j→μ_j` in proof) | §5 trim history | same |
| **C-4.5.cr** | ¶ after Thm D.5 | §5 trim history | **scope changed** (main-text echo), see 2.4 |
| C-4.6.φ, C-4.6.pf.a, C-4.6.eq3, C-4.6.constr, C-4.6.crashD, C-4.6.minimax, C-4.const, C-4.6.pf.iii | proof of Thm D.6 | — | same |
| C-4.6(i)a–(i)d | Thm D.6(i) | §5 "Sharpness" bullet 1 | same |
| C-4.6(ii)a–(ii)c, C-4.6(iii)a | Thm D.6(ii)–(iii) | §5 "Sharpness" bullet 2 | same |
| C-4.6(iii)b, (iii)c | Thm D.6(iii) | §5 bullet 3 (via C-4.thr.4) | same |
| C-4.6(iv) | Thm D.6(iv) (`S→s_tot`) | §5 "The staircase, as a picture" (`K = 149`, last exit `49` written out) | same (numbers recomputed, §4; a pre-existing ambiguity in "84 further instances", §5 X-2) |
| C-4.6.close | Thm D.6 closing sentence; proof, last ¶ | §5 opening; §5 "What is left" | same |
| C-4.thr.1, C-4.thr.2 | App D "The threshold, explicitly" | §5 bullet 2 (values recomputed, §4; the range is not quoted) | same |
| C-4.thr.3 | same | — | same |
| C-4.thr.4, C-4.thr.5, C-4.thr.6 | same | §5 bullet 3 | same |
| C-4.7 | Remark D.7 | §5 "The staircase, as a picture" | same |
| C-4.8(a)–(d) | Remark D.8 (`T→μ`) | — | same |
| **C-4.ver(a)** | App D "Verification and record" | §5 "What is left"; App G | **scope changed** (main-text echo and App G), see 2.4 |
| C-4.ver(b) | same | — | same |
| C-4.ver(c) | same | §5 "What is left" | same |
| **C-4.ver(d)** | same | §5 "What is left"; §1 not-claimed bullet 4 | **scope changed** (§5 echo), see 2.4 |
| C-5.null, C-5.depth, C-5.joint, C-5.W, C-5.pi, C-5.product | App E "The window law" | §6 "Letters and the model law" (pi) | same |
| C-5.syrac, C-5.piledger | App E "The window law" | §6 "Letters and the model law" | same |
| C-5.1 | Hyp E.1 (`T_N→H_N`, `Λ_N→E_N`) | §6 "The hypothesis" | same |
| C-5.eq, C-5.lim | App E after Hyp E.1 | — | same |
| C-5.adm | App E "The budget and admissibility" | §6 "The hypothesis" (both clauses) | same |
| C-5.alt, C-5.cut, C-5.prot, C-5.cons, C-5.4mean, C-5.past, C-5.rates | same | — (C-5.cons's `E_B[m+r] = 4` in §6) | same |
| C-5.base, C-5.TV (`H→𝓗`), C-5.thm | App E "The unconditional base case" | §6 "Where it is already a theorem" | same |
| C-5.clock, C-5.Korec | App E after the base case | §6 "Where it is already a theorem" | same |
| C-5.ledger, C-5.dyadic, C-5.union, C-5.descent, C-5.supplies, C-5.exc | App E "What the hypothesis implies" | §6 "What it would give"; §1 not-claimed (descent, exc) | same |
| C-5.block | same | — | same |
| C-5.cal, C-5.2, C-5.limits | App E "Calibration" | §6 "How it was tested" | same |
| C-5.ratio, C-5.nocut | App E "Calibration" | — | same |
| C-D.1, C-D.2, C-D.3 | §7 (verbatim) | §7 | same |

### 2.2 Table B — P rows

| Row(s) | Place | Verdict |
|---|---|---|
| P-1, P-2, P-3 | title, footnote, date line (verbatim) | same |
| P-4, P-5 | Version note (verbatim) | same |
| **P-6** | Version note | **scope changed** (by the brief), see 2.4 |
| P-7, P-8, P-9, P-11 | Author's note (verbatim) | same |
| P-10 | superseded at the lock by A-1; the Author's note carries A-1's settled words, verbatim | same (as locked) |
| P-12 | §1 ¶2 | same |
| P-13, P-14, P-15 | App F ¶1 (verbatim) | same |
| P-16 | App F ¶2 (verbatim); §5 trim history | same |
| P-17, P-18 | §8 ¶2 (verbatim) | same |
| P-19–P-23 | §8 ¶3 (verbatim); P-20 also §2 "the author's starting point" (see §3 S9) | same |
| P-24 | Thm D.4; §5 "Small periods" | same |
| P-25 | Prop D.1 (verbatim); App D "Notation"; App H | same |
| P-26 | ¶ after Thm D.5; §5 trim history | same |
| P-27 | App D "Verification and record" (verbatim) | same |
| P-28 | App E "The window law"; §6 | same |
| P-29 | §7 | same |
| P-30–P-34 | Appendix A (verbatim) | same |
| P-35–P-40 | bibliography (verbatim) | same |

### 2.3 Table B — N rows

| Row(s) | Place | Verdict |
|---|---|---|
| N-1 | Heuristic C.9; §4 "The digit budget"; §1 not-claimed bullet 2 | same |
| **N-2**, **N-3** | Thm D.4, Thm D.5 and App F (formal, same); §1 not-claimed bullet 3 | **scope changed** (§1 merges the two credit lists), see 2.4 |
| N-4 | Thm D.6(i) and proof; §5 bullet 1; §1 bullet 4 | same |
| N-5 | App D "The threshold"; §5 bullet 2; §1 bullet 4 | same |
| N-6, N-7 | App D "The threshold"; §5 bullet 3 | same |
| N-8 | Remark D.8 | same |
| N-9 | App D "Verification and record"; §5 "What is left" ((iii) untested: same; "nothing bears": see C-4.ver(d)) | same |
| N-10 | App E "The window law" | same |
| N-11 | App E; §6 "Letters"; §1 bullet 5 | same |
| N-12 | App E "The budget and admissibility" | same |
| N-13, N-14, N-15 | App E "What the hypothesis implies"; §6; §1 bullet 5 | same |
| N-16 | App E "Calibration"; §6 "How it was tested" | same |
| N-17 | App F ¶1 (verbatim) | same |
| N-18 | ¶ after Thm C.8; §4 (separate sentence) | same |
| N-19 | Abstract; Thm D.6(i); §5 bullet 1; §1 bullet 4 | same |

### 2.4 The eight scope changes, quoted

1. **C-3.5(a)** (writer's flag 6). The row says the displacement is `ξ = n − N(ω)` on `d = 2n`, resp. `n − N(3ω)`. §4 "The next depth" says: "an exact formula in the anchor displacement (*the difference between the depth and the anchor*) and `s`". The fresh check computes `2ξ ≡ d − M(ω) (mod 2^64)` on 10,000 lifting states, both components, with 0 failures. So `ξ` is **half** that difference. A control without the factor ½ is rejected. **Fix:** "… in the anchor displacement (half the difference between the depth and the anchor, taken $2$-adically) and $s$".
2. **C-4.notation.** The row is the "Overloaded symbols" list. Its replacement, App H, says "Symbols that carried two meanings in v3, or would have in v4, are renamed here; no meaning changed." That is wider than the truth. In v4 these symbols still carry two meanings: `β` (`1 + η` in the proof of Thm D.6; `2(2 − log₂3)` in App E), `q` (`2^K − 3^n`; the exponent in the proof of Thm C.7), `n` (`d = 2n` in Thm C.5; `Σ m_t`), `N` (the map `N(u)`; the sampling scale), `A` (`3^dω − 1`; arcs `A`, `A_t`; the recursion `A_r`), `k` (depth; convergent index), and `ε` (tolerance; "the record's `ε_p`" in "Configurations"). None of these was in the old list either, so no reader is misled about a renamed symbol. The sentence claims completeness all the same. **Fix:** "The symbols below are renamed; no meaning changed." The content of C-4.notation (which letter means what for `T`, `Λ`, `ε`, `M_t`, `S_t`, `S_n` and the renamed ones) is all present.
3. **C-4.5.cr.** The row says Thm D.5 is Rozier's Lemme 4 and SdW's Lemma 7 "in rotation coordinates, **up to an additive constant**". §5 trim history says: "In this paper's notation the bound — the *uniform trim* — reads (Theorem D.5): …". That drops the qualifier. The qualifier matters, because C-4.thr.6 / N-7 rest on Rozier's additive term `2^p`. **Fix:** "In this paper's notation, and up to an additive constant, the bound --- the \emph{uniform trim} --- reads (Theorem~\ref{thm:uniform}):".
4. **C-4.ver(a).** The row says "Parts (i)–(iii) were … each checked by independently written code with exact integer arithmetic at every size decision". §5 "What is left" says: "*Each part* was checked by independently written code with exact integer arithmetic at every size decision". In context "each part" includes part (iv), named one sentence earlier. Part (iv) is a computation of the record by `uniform_trim.py`, a seeded candidate search (Thm D.6's proof: "(iv) is a computation of the record"), and the row does not extend the "independently written code" description to it. **Fix:** "Parts (i)--(iii) were each checked by independently written code …". App G's row for Thm D.6(i) also blurs the attribution. It reads "45 checks, 0 failures; the sweep, the bracket, the window counts, and the construction …", but in the row the 45 checks are `staircase_gamma_upper.py`'s alone. **Fix:** "\texttt{staircase\_gamma\_upper.py}: $45$ checks, $0$ failures; \texttt{staircase\_allp\_construction.py} and \texttt{staircase\_allp\_diophantine.py}: the sweep, the bracket, …".
5. **C-4.ver(d)** (the serious one). In the formal text: "Every statement *here* concerns the reach of size arguments, and none bears on whether cycles exist" ("here" = the staircase theorem's verification paragraph). §5 "What is left" says: "Every statement *in this section* concerns the reach of size arguments, and none bears on whether cycles exist." But §5 also states "$F$ has no nontrivial cycles of $1$, $2$ or $3$ blocks" (Thm D.4) and Hercher's exclusion of `p ≤ 91`. Both bear directly on whether cycles exist, so the sentence is false where it stands. §1 bullet 4 has it right ("Every statement about the staircase …"). **Fix:** "Every statement about the staircase concerns the reach of size arguments, and none bears on whether cycles exist."
6. **P-6** (changed by the brief, as declared). Locked: "No statement is renumbered … (Remark 4.8 is new and takes the next number.)" New: "v4 is also rewritten for a curious reader … the statements, *with every proof*, are in Appendices B–E. Its statements are therefore renumbered, and Appendix H maps v3's numbers to v4's. Outside work that cites this paper's statements by number, including the cycle ledger shared with Eric Merle, cites v3, which remains the pinned citation for that purpose." The renumbering and the concordance are true (§5). "With every proof" is not, see §3 S7. The Merle sentence is new provenance. It is backed by the record (`briefs/merle-round18-review-findings.md`: "DOI v3 pinned"; `briefs/paper1-v4-fixpass-brief.md`: "v3 stays the pinned citation for Merle's work") but by no ledger row, so it is the author's to approve. The fact that Remark D.8 is new moved to App H ("— → Remark D.8, crash (new)"). **Fix:** "the statements, with their proofs or the record sections that hold them, are in Appendices~\ref{app:reduced}--\ref{app:aeh}."
7. **N-2 and N-3** (writer's flag 13). Locked: N-2, periods 1–3 classical (Steiner; Rozier **1990**; SdW; Hercher). N-3, the trim is **Rozier's [1991] and SdW's**, finiteness Brox's. §1 bullet 3: "The exclusion of cycles with one, two or three blocks, and the uniform trim, are not new: they are classical (Steiner; Rozier; Simons--de~Weger; Hercher; finiteness at each period is Brox's)." The merged list credits the trim to Steiner and Hercher too and drops the years. **Fix:** "The exclusion of cycles with one, two or three blocks is classical (Steiner; Rozier 1990; Simons--de~Weger; Hercher), and so is the uniform trim (Rozier 1991; Simons--de~Weger; finiteness at each period is Brox's). What is offered for them is new derivations."

---

## 3. Item 3 — main-text sentences with no row, or exceeding one

I read every sentence of §§1–8 that states a mathematical fact, a credit or a provenance claim. Apart from the scope changes in §2.4 above, these sentences have no ledger row of their own or say more than the row behind them.

| # | Sentence (place) | Verdict | Fix |
|---|---|---|---|
| S1 | "It does not settle the Collatz conjecture." (§1 not-claimed, writer's flag 1) | supported: a disclaimer, consistent with C-4.ver(d) and C-D.2; no row claims otherwise | none |
| S2 | "**Most** steps of a Collatz orbit are forced." (§2 opening) | **unsupported** quantifier. A block of entry depth `m` is `m` steps of `T`, of which `m − 1` are forced rises. Under the paper's own model law `E[m − 1]/E[m] = 1/2`, so "most" has no backing. The abstract says "much", and §1 (2) "long stretches" | "Long stretches of a Collatz orbit are forced." |
| S3 | "A counterexample to the conjecture would be either an orbit that grows forever or **a cycle that never reaches 1**." (§5 opening) | no row; elementary but imprecise. A bounded non-convergent orbit *enters* a cycle; it need not be one | "… either an orbit that grows forever or an orbit that falls into a cycle not containing $1$." |
| S4 | "Every odd number below the verified range $2^{71}$ reaches $1$ [Barina], so the elements of a nontrivial cycle all lie above it" (§5 bullet 2, flag 2) | supported: C-RW.12, plus the inference Lemma D.3's proof already makes | none |
| S5 | "A cycle gives a size-passer; a size-passer need not give a cycle." (§5, flag 4) | supported: C-4.1(c) (a cycle meets `q ≤ R_r`), C-4.6(iv) and C-4.ver(c) (size-passers failing `q ∣ R_r`); the `p = 7` instance recomputed, `q` divides 0 of 7 `R_r` | none |
| S6 | Trim plain reading: "the requirement weakens exponentially as the number of blocks grows" (flag 3) | supported: C-Abs.9, Thm D.5 | none (but see 2.4 item 3 for the sentence before it) |
| S7 | "the statements, **with every proof**, are in Appendices B–E" (Version note) | **unsupported**: App G itself lists statements proved in the record and not printed; Thm D.4 is an outline; C-4.5(d), C-5.thm, C-5.eq, C-5.dyadic are record-proved | as in 2.4 item 6 |
| S8 | Merle/v3 sentence (Version note, flag 14) | not a ledger row; supported by the record (see 2.4 item 6); author approval | none beyond approval |
| S9 | "and it was also the author's starting point (Section 8)" (§2, flag 15) | supported by P-20 (the mechanism is the March 2023 note) and P-30 (that note is the origin) | optional: "and it is the mechanism of the author's hand-drawn note of March 2023 (Section~\ref{sec:credit})" |
| S10 | "Every odd number has an inverse among them, and one can take logarithms." (§4, flag 7) | background on `Z₂`, true; consistent with C-3.N | none |
| S11 | binary-counter analogy (§4, flag 8) | a restatement of `v₂(d − M(ω))` as matching low bits; true for `d ≠ M(ω)`, which holds on valid lifting states | none |
| S12 | "(precisely, $S + 1 \le J$, with $S$ the factors of $2$ divided out)" … "not divided out more factors of 2 than the start has binary digits" (§6, flag 9) | same scope as the formal gloss in App E ("the event that the itinerary has not outspent the start's supply of binary digits"); `S` = `S_{n+1}` = divisions from `x` to `x_exit(n)` | none |
| S13 | admissibility paraphrase, "$4\theta < \tau$" (§6, flag 10) | supported: C-5.adm with C-5.cons (`E_B[m + r] = 4`, recomputed) | none |
| S14 | "the rate at which a factor of 3 is gained is 1/3, up to the cap" (§6, flag 11) | supported: C-5.piledger (1/3 recomputed) | none |
| S15 | "stated as a heuristic" (abstract, flag 12) | supported: C-Abs.7's grade | none |
| S16 | "roughly geometrically" (§5 picture, flag 5) | supported: C-4.7. The ratios are 1.750, 1.286, 1.667, 1.533, 1.522 (recomputed) | none |
| S17 | "Every informal statement in the main text names its formal statement in an appendix" (§1 "How to read") | slightly wide: S2, S3 and S4 name none. A navigation claim, not mathematics | "Each result stated informally in the main text names its formal statement …" |
| S18 | App H: "— & $s_{\mathrm{tot}}$ (… new in v4)" | **wrong**: v3 has `S` in Thm 4.6(iv), "$s = (1,\dots,1,\,S-6)$" (v3 `.tex` line 222) | row: "$S$ (Theorem 4.6(iv)) & $\stot$ (Theorem~\ref{thm:staircase}(iv) and its proof) & $K - n$" |
| S19 | App G "Statements proved in the record and not printed here" | incomplete as a list: it omits C-5.depth (`aeh.md` §13.6), the integer form of C-4.1.BS (`cycles.md` Remark 12.6.1.7), C-4.dict(e) (`cycles.md` §12.4) and C-5.syrac's normalisation (`aeh.md` §13.6.5) | add those four items, or head the list "Among the statements proved in the record …" |

App G's other rows match their ledger verification lines (C-3.6, C-3.7, C-3.10, C-3.8.rate, C-4.3, C-4.4, C-4.ver(a), C-4.6(i)c, C-4.thr.1, C-4.8(d), C-4.6(iv), C-5.cal), apart from the Thm D.6(i) attribution (2.4 item 4).

Everything else in §§1–8 restates a row in the row's words or with its scope words kept. I checked in particular: every quantifier in §5 "Sharpness" (`p ≥ 16`, `3 ≤ p ≤ 15` by finite check, `p ∈ {2,4}` with no bracket, nothing at `p = 1`, `p ≥ p₁(X₀)`, "no closed form … nothing below", "that value, not the inequality of his Lemme 4", "below 0.054", "left open"); the grades in §6 ("conjecture", "theorem for … `τ < 1`", "(record …)", "by Heuristic C.9 … not expected"); and the credits in §5's trim history, §6 (Terras, Tao, Korec, Inselmann) and §8.

---

## 4. Item 4 — worked examples recomputed (fresh code)

`experiments/paper1_v4_readable_examples_check.py`, written from the paper's text with nothing imported from the repository. Exact integers and Fractions; `mpmath` at 400 digits for real constants and `p₁`. One command, deterministic, about 2 s:

    python experiments/paper1_v4_readable_examples_check.py

It writes `experiments/paper1_v4_readable_examples_check_output.txt` and exits 0. **57 checks, 0 failures; 7 negative controls, all rejected.**

- **`x = 7` (§2):** the four table rows (binary of `x` and `x + 1`, the factorisations `2³`, `2²·3`, `2·3²`, `2·7`); `T`-orbit 7, 11, 17, 13; `3·17 + 1 = 52 = 110100₂`, `v₂ = 2`; `m = 3`, `u = 1`, `26 = 2·13`, `s = 1`, exit 13; one-division map 7, 11, 17, 26, 13; `T(x)+1 = (3/2)(x+1)` for every `x ≡ 3 (4)` below 200,001; "ends in exactly `m` ones" for every odd `x` below 200,001; Prop B.2(i)–(ii) for every odd `x` below 100,001.
- **States (§3):** `R⁻¹(1,3) = {7, 11, 17}` and `R⁻¹(1,1) = {1}` below 200,001; the chain `(1,3) → (7,1) → (1,2) → (1,1)` with block entries 7, 13, 5, 1, both from the `T`-orbit and from Definition B.1's formulas; `F(1,1) = (1,1)`; `R(T^m x) = F(R(x))` below 50,001.
- **The state (1,2) cascade (§4):** `s = 3`; `3·5 + 1 = 16` halves 4 times, to 1.
- **The eight-class table (§4):** every `(ω mod 8, d mod 2)` cell for `ω < 3001` (`3 ∤ ω`), `d ≤ 40`; the lifting condition; `s = 2 + v₂(d − M(ω))` on all 10,000 lifting states (anchor computed mod `2^64` by lifting `9^t ≡ ω^{−2}`); `M(1) = 0`; `M(ω)` even iff `ω ≡ ±1 (8)`; the undecided-rate arithmetic `2^{−(k+1)}` = 0.03125, 0.001953.
- **The `p = 7` staircase (§5):** `n = 94`; `K = ⌈94 log₂3⌉ = 149` (exact: `2^148 < 3^94 < 2^149`); last exit `s_tot − 6 = 49`; `γ = 6.7437584` (printed 6.74); all seven `q ≤ R_r` (min `R_r/q = 1.42`); `q` divides none of the seven `R_r`; period-3 constant `0.1157·94 − 2 = 8.8758` (printed 8.9); the D.6(ii) sandwich (`log₂(x_min + 1) = 7.030`); the D.5 trim (`9.551 > 2.279`).
- **Constants (§5 Sharpness):** `Γ* = 3.683012101` (≥ 3.683012), `φ(0.0415) = 5.140211486` (≤ 5.140212), `λ₀ = 2.709512245`, `2^{−(λ₀+1.5)} = 0.0540518`.
- **`p₁(X₀)` (§5 bullet 2):** recomputed from the definition in the proof of Thm D.6(iii) (convergents of `log₂3`, `Δ = φ(g) − φ(g+1)`, `N*`, the least `p` with `(L^p − 1)/(2(L − 1)) ≥ max(N*, 3p + 40)`). The results are 10 at `X₀ = 1` and 16, 22 at `2^8` and `2^12`, 36 at `2^20`, 98 at `5·2^60`, 110 at `2^71` and 309 at `2^200`: all match.
- **§6:** `E_B[m + r] = 4`; `Σ_{j even} 2^{−j} = 1/3`; a `τ` with `4θ < τ < 1` exists iff `θ < 1/4`.
- **Controls rejected:** a wrong table cell; a wrong state chain; last exit 48; a flat profile `(1,…,1,88)` (fails the size tests); `p₁(2^20) = 35`; `K = 150`; `ξ = d − M(ω)` without the ½.

---

## 5. Item 5 — the concordance (Appendix H)

I checked every row against `pdftotext` of `paper/collatz-reduced-v3.pdf` and of my build (identical to the committed `paper/collatz-reduced-v4.pdf`), by statement number and title.

- **Statement rows, 23 of 23 correct:** Def 2.1→B.1, Prop 2.2→B.2, Thm 2.3→B.3, Def 3.1→C.1, Lemma 3.2→C.2, Thm 3.3→C.3, Lemma 3.4→C.4, Thm 3.5→C.5, Remark 3.6→C.6, Thm 3.7→C.7, Thm 3.8→C.8, Heur 3.9→C.9, Remark 3.10→C.10, Prop 4.1→D.1, Cor 4.2→D.2, Lemma 4.3→D.3, Thm 4.4→D.4, Thm 4.5→D.5, Thm 4.6→D.6, Remark 4.7→D.7, — → D.8 (v3 has no Remark 4.8; the lock's 4.8 is D.8), Hyp 5.1→E.1, Lemma 5.2→E.2. Titles match in each case. The lock's numbering equals v3's apart from 4.8.
- **Equation rows, 2 of 2 correct:** v3 has one equation, `eq:isometry` (1) → (1); eqs. (2) and (3) are new in v4.
- **Section map:** correct (v3 §1 Introduction with Related work, §2 reduced system, §3 anchor dynamics, §4 cycles, §5 hypothesis, §6 Discussion, App A).
- **Rename table:** 8 of 9 rows match v3's source (`ε` Thm 3.5; `ε_t` Cor 4.2 and Lemma 4.3; `T_j` proof of Thm 4.5; `T_N`, `Λ_N` Hyp 5.1; `H` and `η` §5; `(r,1)` Lemma 5.2). **The `s_tot` row is wrong** (S18): v3 had `S` in Thm 4.6(iv).
- The lead sentence, "a v3 number becomes a v4 number by a change of the leading section number to a letter", holds for every statement row. The rename paragraph's "Symbols that carried two meanings … are renamed" over-reaches (2.4 item 2).

**Verdict:** the concordance is correct; one rename row and one sentence need the fixes above.

---

## 6. Observations on locked text (outside the rewrite; for the author, not fixes to the rewrite)

- **X-1.** App D "The threshold, explicitly": "over $X_0 = 2^j$, $j \le 200$, $p_1 - \log_{\LL} X_0 \in [2.784, 10.629]$". The exact extremes are **2.7839895** (`j = 143`) and **10.6294771** (`j = 74`). Both endpoints are rounded to nearest, so both extremes lie just outside the printed closed interval. Outward rounding gives `[2.783, 10.630]`. The independent check of 12.8.7 quoted `[2.7840, 10.6295]` (4 decimals, also nearest). This range is not quoted in the main text.
- **X-2.** Thm D.6(iv), carried into §5's picture: "… where the period-3 constant would demand $\gamma > 8.9$, and $84$ further instances occur at $p = 6$ alone". The 84 are the size-passers of a seeded random search (`experiments/uniform_trim.py`, `random.seed(41)`; re-run: 84). **None of them beats the period-3 constant**: `γ − (0.1157n − 2) ≥ +0.698` at every one (`n ∈ {20, 22, 27, 29, 34, 41, 46}`). The script's second search finds exactly one configuration that does, the `p = 7` instance. Placed right after "would demand γ > 8.9", "further instances" reads as further instances beating it. The "period-3 constant" `0.1157n − 2` is also not defined anywhere in the paper. A possible wording: "… and a search at $p = 6$ found $84$ further staircase size-passers (none of them below that constant); all of them fail the divisibility conditions."

---

## 7. Exact fixes proposed (none applied)

1. §5 "What is left": "Every statement in this section concerns" → "Every statement about the staircase concerns". *(C-4.ver(d); the one false sentence)*
2. §5 "What is left": "Each part was checked by independently written code" → "Parts (i)--(iii) were each checked by independently written code". *(C-4.ver(a))*
3. §5 trim history: "In this paper's notation the bound --- the \emph{uniform trim} --- reads" → "In this paper's notation, and up to an additive constant, the bound --- the \emph{uniform trim} --- reads". *(C-4.5.cr)*
4. §1 not-claimed bullet 3 → "The exclusion of cycles with one, two or three blocks is classical (Steiner; Rozier 1990; Simons--de~Weger; Hercher), and so is the uniform trim (Rozier 1991; Simons--de~Weger; finiteness at each period is Brox's). What is offered for them is new derivations." *(N-2, N-3)*
5. §4 "The next depth": "(the difference between the depth and the anchor)" → "(half the difference between the depth and the anchor, taken $2$-adically)". *(C-3.5(a))*
6. Version note: "the statements, with every proof, are in" → "the statements, with their proofs or the record sections that hold them, are in". *(P-6, S7)*
7. §2 opening: "Most steps of a Collatz orbit are forced." → "Long stretches of a Collatz orbit are forced." *(S2)*
8. §5 opening: "or a cycle that never reaches $1$" → "or an orbit that falls into a cycle not containing $1$". *(S3)*
9. App H: "Symbols that carried two meanings in v3, or would have in v4, are renamed here; no meaning changed." → "The symbols below are renamed; no meaning changed." *(C-4.notation)*
10. App H rename table: "--- & $\stot$ (proof of Theorem~\ref{thm:staircase}, new in v4)" → "$S$ (Theorem 4.6(iv)) & $\stot$ (Theorem~\ref{thm:staircase}(iv) and its proof)". *(S18)*
11. App G, row Theorem D.6(i): attribute "$45$ checks, $0$ failures" to \texttt{staircase\_gamma\_upper.py} alone, and the sweep, bracket, window counts and construction to the two \texttt{staircase\_allp} scripts. *(C-4.ver(a))*
12. App G "Statements proved in the record and not printed here": add the depth renewal law (\texttt{aeh.md} \S13.6), the integer form of the elimination identity (\texttt{cycles.md} Remark~12.6.1.7), the deep-entry clause of the dictionary (\texttt{cycles.md} \S12.4) and the normalisation of $\mathrm{Syrac}$ (\texttt{aeh.md} \S13.6.5). *(S19)*
13. Optional: §1 "How to read": "Every informal statement" → "Each result stated informally" (S17). §2: "the author's starting point" → "the mechanism of the author's hand-drawn note of March 2023" (S9).
14. For the author (locked text, §6): X-1 (outward-round the `p₁` range) and X-2 (say what the 84 are).

The author still has to approve the three items the writer flagged as his: §1's not-claimed box, the Version note (including the Merle/v3 sentence), and §§2–3.

---

## 8. Record

- Branch `paper1-v4-readable-check`, cut at `c1d4b57`.
- Deliverables: `experiments/paper1_v4_readable_examples_check.py` with its output, and this file.
- The `.tex` and PDF are untouched. No wiki page or ledger was edited. Nothing was pushed.
