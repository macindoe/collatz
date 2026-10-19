# Findings: paper 1 v4 fix pass — U1–U19 tightened, the author's decisions applied, the ledger re-cut

**Task:** `briefs/paper1-v4-fixpass-brief.md`. Branch `paper1-v4-fixpass`, base **`870d34b`** (the worktree was cut at `8370638` and fast-forwarded to `870d34b`, the brief's commit on `main`, before any work). Done 2026-10-19.

**Rules kept.** Prose was weakened to match the theorems; no theorem was strengthened and no theorem's mathematics changed. Where support was missing it was added: a proof printed from the record, a record pointer, a script name, or a bibliography entry. No statement was renumbered: the theorem-environment sequence of the rebuilt PDF is identical to the old one (`pdftotext`, compared). The Author's note is unchanged in its text; A-1 is proposed in a comment only. No wiki page was edited. Files were written with Edit/Write only. The only outward actions were read-only reference lookups (web search; the zbMATH API; the IMPAN page; the Rackl thesis PDF).

**Deliverables:**
- `paper/collatz-reduced-v4.tex` and `paper/collatz-reduced-v4.pdf` (22 pp; 0 undefined references);
- `paper/collatz-reduced-v4-claims.md`, re-cut;
- this file.

## 1. The U table

`Lnn` is a line of the fixed `.tex` (603 lines, commit `01641d5`).

| U | v4 location | Old text (short) | New text | Source |
|---|---|---|---|---|
| U1 | Abstract L48; Intro L83; Discussion L556 | "exact laws, all governed by one 2-adic quantity"; "every quantity above obeys an exact law in the anchor displacement"; "one 2-adic logarithm governs the step" | "governed — apart from a 3-adic absorption term, which obeys its own exact law — by one 2-adic quantity"; "every quantity above other than the absorption `a₊` obeys an exact law in `d − M(ω)`, and `a₊` obeys its own exact 3-adic law (Lemma 3.4)"; "…governs the step, apart from the 3-adic absorption, which has its own exact law" | Lemma 3.4; Thm 3.7's own carve-out |
| U2 | Contribution (v), L81 | "with every element above any size threshold `X₀`" | "with every element at least any size threshold `X₀`" | Thm 4.6(iii): `x_min ≥ X₀` |
| U3 | Intro L83; Heuristic 3.9 L205 | "an elementary accounting argument shows each decision consumes digits irreversibly" | "a digit-budget accounting, stated as a heuristic (Heuristic 3.9), indicates that each decision consumes digits irreversibly"; and inside the Heuristic: "Theorem 3.7 shows that these residues suffice; that they are also needed is part of the heuristic." | Thm 3.7 (sufficiency only) |
| U4 | Related work L86 | "the law recorded here implies his conclusion, its level-one form already forcing some class to frequency at least 2/9" | "The stationary 3-adic law of Section 5 (Tao's Syrac) is far from the near-uniformity he rules out: at level one it puts mass 2/3 on the residue 2 mod 3, which three of his six classes share, so a sequence with those frequencies has some class at frequency at least 2/9 > 1/6 + 0.0215. That his counting bound follows from the law is not claimed." | `briefs/v3r2-thomas-check-findings.md` (`Syrac(Z/3Z) = (0, 1/3, 2/3)`); Tao's printed `Syrac(Z/9Z)`. The implication claim was withdrawn because Thomas's bound is a power saving `N^{0.9999}` over orbits reaching 1, which a density-one law does not deliver. |
| U5 | Thm 3.8 statement L195; new paragraph L202 | "under the law `π_{k,D}` … the undecided rate is `≈ 2^{−(k+1)}`" (inside the theorem) | Clause removed from the statement. After the proof: "By the proof, the window is undecided exactly when `s₊ ≥ k+2`. Under `π_{k,D}` with `D ≥ k+2`, whose `s`-marginal is `P(s = j) = 2^{−j}` for `j < D`, that event has probability `Σ_{j≥k+2} 2^{−j} = 2^{−(k+1)}` exactly", with the record's measurements (`0.0275` vs `0.03125` at `k = 4`; `0.0019` vs `0.00195` at `k = 8`). | Thm 3.8's proof (undecided ⟺ `v₂(d₊ − M(ω₊)) ≥ k` ⟺ `s₊ ≥ k + 2`); §5's `s`-marginal; `stage4.md` Remark "undecided rate" |
| U6 | Thm 4.6 closing sentence L294; Discussion L556 | "requires the divisibility system — equivalently, rigidity of the closed anchor walk `Σ ΔM_t = 0`"; "for cycles, whether closed anchor walks are rigid (Theorem 4.6)"; "(the only route past Theorem 4.6)" | "requires the divisibility conditions `q ∣ R_r` of Proposition 4.1, not size alone"; "for cycles, whether the divisibility conditions `q ∣ R_r` can be met, which size alone cannot decide (Theorem 4.6)"; the anchor walk kept only as an example of arithmetic input ("a cycle's anchors return and its increments satisfy `Σ_t ΔM_t = 0`") | The equivalence is asserted in the record too (`cycles.md` Remark 12.8.4), not proved; only the necessary direction is trivial (`spine.md` 9.8.4, anchor form) |
| U7 | Remark 4.8 L342 | "At the scale of Theorem 4.6(iii) a unit block is excluded." | "…a unit block is excluded wherever the inequality below holds." | Remark 4.8's own displayed condition |
| U8 | §5 L542 | "by Heuristic 3.9 it cannot be reached by finite-window computation" | "by Heuristic 3.9, it is not expected to be reachable by finite-window computation" | Heuristic 3.9's grade |
| U9 | Heuristic 3.9; "The threshold, explicitly"; Remark 4.8; "Verification and record"; "Calibration"; Appendix A | No script named for: the orbit mean `σ ≈ 4.0`; Lemma 4.3's `p ≤ 5` inspection; the `p ∈ {2,4}` exhibitions; `p₁` at `5·2^{60}` and the two ranges; Remark 4.8's table; the campaign. App A: "every computational claim cites a runnable script" | `σ ≈ 4.0`: the unscripted measurement replaced by the model mean ("`σ = s + m₊` has mean 4 under the model law of Section 5 … the heuristic does not depend on the constant"); `p ≤ 5`: the inspection printed (U13); `p ∈ {2,4}`: `experiments/staircase_allp.py`, §12.8.6.4; `p₁`: `experiments/staircase_x0_threshold.py` computes the values at `2^j`, `5·2^{60}`, `2^{71}`, and the ranges follow by monotonicity of `p₁` in `X₀`; Remark 4.8: the table is in that script's output; campaign: `experiments/aeh_calibration.py`, `experiments/aeh_anomaly.py`. App A: "every computational claim is backed by a runnable script, named here or at the record section cited" | `cycles.md` §12.8.6.4, §12.8.7.4–5; `experiments/staircase_x0_threshold_output.txt` (lines 80–125, 296–316); `aeh.md` §13.4–13.5; `stage4.md` §11.8.7.7 (names no script for `E[σ] ≈ 4.0`) |
| U10 | Discussion L556 | "Three directions have defined success criteria" | "Three directions are open" | — (no criteria are stated in v4 or chosen by the author) |
| U11 | Related work L90; bibliography L599 | Rackl cited by name only | `\cite{rackl}`; entry: D. Rackl, *Cycles in the Collatz sequence: an approach using 2-adic arithmetic*, Bachelor's thesis, University of Klagenfurt, Department of Mathematics, 22 September 2021, with the PDF's URL | the thesis's title page, read 2026-10-19 (`benjamin-hackl.at/downloads/theses/2021-bachelor-rackl.pdf`; advisor B. Hackl) |
| U12 | Abstract L48; Version note L54; Intro L77, L81; Related work L88; Thm 4.6 proof (iv) L332 | "slack between two absolute constants at every period (…, `p ∈ {2,4}` by exhibition)"; "at every period" | "at every period `p ≥ 3` (`p ≥ 16` by proof, `3 ≤ p ≤ 15` by finite check; at `p ∈ {2,4}` size-passing configurations are exhibited, with no bracket claimed)"; elsewhere "at every period `p ≥ 3`" | Thm 4.6(i). The theorem's own part label "Every period." was left as it is: the part lists exactly what it covers. `p = 1` stays unaddressed, now recorded as N-19. |
| U13 | §3 L126, L136; Cor 4.2 proof L236; Lemma 4.3 proof L244; after Thm 4.5 L278; Thm 4.6 proof L298 | No proof or pointer for: Cor 4.2 ("obtained in four lines"); Lemma 4.3; Thm 4.5's third display; `N` an isomorphism; `M(ω)` even iff `ω ≡ ±1 (8)`; `φ` a decreasing involution | Cor 4.2: the four lines printed (step identity multiplied around the cycle; `log(1+ε) < ε`; `ε_t < 1/x_t`). Lemma 4.3: proof printed, including the `p ≤ 5` inspection (`3 → 5 → 1`, `7 → 11 → 17 → 13 → 5 → 1`). Thm 4.5: pointer "its derivation … is `cycles.md` Corollary 12.8.2". `N`: "the inverse of `t ↦ 9^{−t}`, a continuous homomorphism, injective by the isometry and onto because its image is compact and dense". Parity: `ω² ≡ 1` or `9 (mod 16)`, and `9² ≡ 1 (mod 16)`. `φ`: `2^{−x} + 2^{−φ(x)} = 1` is symmetric. | `cycles.md` Corollary 12.1.2, Lemma 12.6.2, Corollary 12.6.3, Corollary 12.8.2 (the printed proofs follow the record's) |
| U14 | new paragraph L218; Lemma 5.2 L549; §5 L481 | Collisions: Lemma 5.2's `(1,1)` (a class) against the state `(1,1)`; `η` in §4 and §5; `Λ`/`Λ_N`; `T`/`T_N`/`T_j`; three `ε`; `M_t`/`M(ω)` | An "Overloaded symbols" paragraph at the head of §4 (`T`, `Λ`, `ε`, `S`, `M_t`); Lemma 5.2's classes written `[r,1]` ("the class `ω ≡ r (mod 8)`, `d = 1`, not a state"); §5's slack `η` renamed `ζ` | — (notation only; no symbol's meaning changed) |
| U15 | "Calibration" L546 | four violations listed in three clauses | "(1) an `s=3` marginal excess and (2) pair correlations, both artifacts of small starting values; (3) digit biases …; and (4) a `5σ` digit bias …" | `aeh.md` §13.4–13.5 |
| U16 | §5 L446 | "…does not follow there and can fail by any amount." | adds: "a single letter of size `cT_N` at the exhausting block, with the `o(T_N)` blocks after it tallied at `†`, leaves every fixed pattern frequency at its `B`-value and moves the mean from 4 to `4 + c` (`aeh.md` §13.2)" | `aeh.md` §13.2 (the record's own example) |
| U17 | after Lemma 5.2, L552 | "one residue of the unique class with a self-loop channel" | "one residue of the class `[1,1]`, whose residue 1 returns to it deterministically (a self-loop channel)" | Lemma 5.2. The record (`aeh.md` §13.5) also asserts uniqueness without proof; the word was dropped rather than proved. |
| U18 | Abstract L48; Contribution (v) L81; Related work L88 | "The family realizes Rozier's 1991 extremal" (after both statements); "an explicit family realizing Rozier's extremal profile … at every period" | "At that threshold scale the family realizes the minimax value of Rozier's 1991 extremal under every rotation's exact size condition"; (v) and Related work: the realization attached to the threshold statement only | "The threshold, explicitly" (C-4.thr.6); `briefs/paper1-v4-draft-findings.md` §5 |
| U19 | Abstract L48 | "the block letters of uniformly sampled large starts carry, at every finite block length, …" | "…large starts, tallied within an exponent budget proportional to the start's bit length and for every admissible pair of budget and horizon rates, carry, …" | Hyp 5.1. v4 has no other in-words statement of the hypothesis; the rewrite must keep both clauses in any it adds. |

## 2. The author's decisions (2026-10-19)

- **A-4, kept.** Appendix A's "the AI collaborators carried out the mathematical development" stands for both phases. There was no `% AUTHOR:` flag on it in the source, so nothing was removed.
- **A-5, cut.** The canonical-scale sentence at the end of "The threshold, explicitly" is gone. Its ledger row C-4.thr.7 stays, marked "cut", so the rewrite does not restore it.
- **A-6, left out.** None of the gcd rotation-invariance, the Tao p. 2 / Prop 1.11 refinement, or the Knight clause is in the source. Confirmed by search.
- **A-2 (the brief's numbering), done.** The line-61 `% AUTHOR:` comment ("next sentence is accurate as written") is deleted. The ledger had called this item A-3; its A-2, the note's header comment at L58–59, stays until A-1 is settled.
- **A-1, proposed, not applied.** The current sentence stays. The proposal sits beside it as a `% AUTHOR-PROPOSED:` comment (L68–72):

  > That simplification is what enables the paper's main contributions: exact laws for every single step; a proof that the limit Rozier and Simons–de Weger found on what size-counting can achieve against cycles is essentially the true one; and an exact hypothesis pointing the remaining question toward more fundamental ``fair-coin'' mathematics.

  "Essentially" is there on purpose. Theorem 4.6 proves that the exponential rate is the true one, and that the prefactor `p c_p` cannot go below `0.054` at the threshold scale. Whether the `log₂ p` can be removed is left open (C-4.thr.5). "The true one" alone would claim the constants as well.

## 3. Sós and Świerczkowski, checked at source

| Entry | As printed | Source | Verdict |
|---|---|---|---|
| `sos` | V. T. Sós, *On the distribution mod 1 of the sequence nα*, Ann. Univ. Sci. Budapest. Eötvös Sect. Math. 1 (1958), 127–134 | zbMATH Open API record **0094.02903**: same title, *Annales Universitatis Scientiarum Budapestinensis de Rolando Eötvös Nominatae, Sectio Mathematica* 1 (1958), 127–134 | **held** |
| `swierczkowski` | S. Świerczkowski, *On successive settings of an arc on the circumference of a circle*, Fund. Math. 46 (1958), 187–189; DOI 10.4064/fm-46-2-187-189 | the publisher's page (IMPAN, Fundamenta Mathematicae 46(2)): same title, 46 (1958), 187–189, the same DOI. MacTutor's publication list gives 1959; the publisher's 1958 is followed. | **held** |

No change to either entry.

## 4. The re-cut ledger

`paper/collatz-reduced-v4-claims.md` now reads against `01641d5`. Unchanged rows keep their IDs, and their `Lnn` references were moved to the fixed file. Changed rows carry `Δ` and name their U-item or author item. New rows carry `+`.

**Counts** (primary grade, counted from the file):
- **Table A:** 191 rows, 190 live; C-4.thr.7 is cut. 37 rows are `Δ`; C-4.notation is new.
  - proved here 90 (was 85);
  - cited 29;
  - def 19 (was 18);
  - interpretation 13;
  - proved in record 11 (was 13);
  - measured 11 (was 12);
  - rederived 7;
  - heuristic 6;
  - conjectured 3;
  - open 1;
  - **asserted 0 (was 3 primary, 8 in all).**
- **Grade moves:**
  - asserted → proved here: C-RW.11, C-3.8.rate, C-4.6.φ;
  - measured → proved here: C-3.9(b), now the model mean;
  - proved in record → proved here: C-4.2, C-4.3;
  - the asserted components of C-3.N, C-3.1, C-4.6.close, C-5.past and C-5.ratio are discharged.
- **Table B:** 40 prose claims. P-39 (`rackl`) and P-40 (`sos`/`swierczkowski` checked) are new; P-5, P-18 and P-33 changed.
- **Not-claimed items:** 19. N-17 (Thomas's bound), N-18 (the rate is outside Thm 3.8) and N-19 (`p = 1`; no bracket at `p ∈ {2,4}`) are new.
- **Table C:** 7 author items. A-3 to A-7 are settled; A-1 is proposed; A-2 follows A-1. There are 8 placeholders, unchanged except for their line numbers: PH-6 is now L348 and PH-7 is L561.

## 5. Left for the author

1. **A-1.** Approve, edit or reject the proposed wording. On approval, replace the sentence at L73 and delete the comments at L58–59 and L62–72 (A-2).
2. **Notation.** U14 was fixed by a paragraph and two local renames, not by a global renaming. The readability rewrite may rename freely (it renumbers anyway). The ledger's C-4.notation row lists every collision.
3. **The `σ` measurement.** v4 no longer quotes `E[σ] ≈ 4.0` along orbits, because the record names no script for it. If the author wants the empirical figure back, a script must first be added to `experiments/` and named in `stage4.md` §11.8.7.7.
4. **Record-side asserted sentences.** These are the sources the paper's loose sentences came from: `cycles.md` Remark 12.8.4 ("equivalently, in anchor coordinates, the rigidity of closed anchor walks") and `aeh.md` §13.5 ("`(1,1)` is the unique class with a deterministic self-loop channel"). Wiki pages were out of scope for this pass. Both are worth a status pass.
5. **Placeholders PH-1 to PH-8:** unchanged.

## 6. Record

**Commits:**
- `01641d5`, content: the `.tex` and the rebuilt PDF;
- the next commit, structure: the re-cut ledger and this file.

**Build:** `pdflatex` ×3 in the session scratchpad (`…/scratchpad/build`). Output: 22 pages, no undefined references or citations, no multiply defined labels, 0 overfull boxes. The PDF was copied into `paper/`. The theorem-environment sequence on `pdftotext` is identical to the pre-pass PDF.

**Encoding:** `python experiments/encoding_scan.py` was run before each commit: clean, 0 / 0 / 0.
