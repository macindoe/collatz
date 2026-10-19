# Findings: paper 1 v4 drafted from the checklist — source, PDF, version-history section, Zenodo description

**Task:** `briefs/paper1-v4-draft-brief.md`. Branch `paper1-v4-draft`, base **`85f42d3`** (the worktree was cut at `946e0d8` and fast-forwarded to `85f42d3` before any work). Drafted 2026-10-19. `main` was later merged in (`e4ad005`); nothing under `paper/` conflicted. The author's decisions D1–D15 were applied as given. D5 is applied in its revised form (2026-10-19): the provenance is dated from the author's evidence, and both AI phases are disclosed. Nothing outward: no upload, no Zenodo, no ccchallenge, no push, no email. The only network use was read-only GETs: the arXiv abstract page for 2607.01718, Lagarias's annotated bibliography I (arXiv math/0309224), the Rozier 1990 scan at `probleme-syracuse.fr`, and one Crossref bibliographic query (Świerczkowski). Downloads went to the session scratchpad. No wiki page was edited.

## 1. Deliverables

| File | What |
|---|---|
| `paper/collatz-reduced-v4.tex` | v4 source. Made by a byte copy of v3 (`cp`, checked with `cmp`), then edited with Edit only. Still ASCII. |
| `paper/collatz-reduced-v4.pdf` | Built in a scratch directory with `pdflatex` ×3, then copied in. **21 pages. 0 undefined references, 0 LaTeX warnings, 0 overfull boxes, 1 underfull box** (the Lagarias bibliography entry, badness 1067). |
| `paper/collatz-reduced-version-history.md` | New section `## v4 — [month] 2026`, marked DRAFT in an HTML comment. Month and DOI are placeholders. |
| `briefs/paper1-v4-zenodo-description.md` | The v4 Zenodo description, as HTML: the abstract first, then "Changes in v4", then the pointer. Not uploaded. |
| this file | Coverage table, markers, sweep, flags, and decisions left. |

## 2. Theorem 4.6 in v4: what is stated, and where the proof comes from

The statement has four parts:
- **(i)** Every `p ≥ 16`, with `3.683012 ≤ γ ≤ 5.140212`. The range `3 ≤ p ≤ 15` is a finite check and `p ∈ {2,4}` is by exhibition; both point to `cycles.md` §12.8.6.1 and §12.8.6.4. It ends with the consequence `c_p < (5.140212 + log₂p)(log₂3)^{−p}`.
- **(ii)** The sandwich `γ − 1 ≤ log₂(x_min+1) < γ + log₂p`, and from it the necessity at a threshold `X₀`.
- **(iii)** Sufficiency at every `X₀` for `p ≥ p₁(X₀)`, with `g ≤ γ ≤ g+1`, `λ₀ ≤ γ − κ_p n ≤ λ₀ + 1.5`, `κ_p n ≤ ρ₀ ≤ γ` and `Λ > 0.054·2^{−κ_p n}`.
- **(iv)** The v3 instances (`p = 7`; `84` at `p = 6`), which fail `q | R_r`.

v3's closing sentence follows the parts, unchanged, now attributed to HH p. 238. D15 holds: the theorem number is unchanged, and so is the sentence the joint note cites.

**The proof is printed in full** except for the finite checks.
- It **composes 12.8.6.1's availability with 12.8.7.2's construction under (H1′)**. The paper calls (H1′) "(H1)". The record's own 12.8.6 proof instead uses 12.8.6.2 under the stronger (H1), which forces a unit crash.
- That composition is not stated as such in the record. Every input is. The one new link is that 12.8.6.1's `n` satisfy (H1′): `Γ′ < 1.05(L^p)κ_p + L/(L−1) + η < 3.33 < Γ*`. I derived that link by hand and checked it numerically.
- A scratch script (`scratchpad/v4_sanity.py`, not committed) ran the composition exactly as printed. It used exact integer size tests at every rotation, at `p = 16..20` and at three `(X₀, p)` instances (`(10,10)`, `(10,12)`, `(100,14)`). All were size-passers, inside the printed brackets, with the sandwich holding.
- The Case-1 identity `L·A_{p−2} − (n+p−1−γ+η) = ((L^p−1)/(L−1))(γ − Γ′)` was checked numerically on 2,000 random `(p, n, γ, η)`, with maximum relative error `3·10⁻¹³`.
- The `p₁(X₀)` values are quoted from the record's computation (§12.8.7.4). So are the constants `0.0751874964`, `0.1169390665` and `5.1402114`, which I re-computed.

**Remark 4.8 (new)** is the crash-depth-1 obstruction, with its proof.
- It is stated in an exact form: `(L−1)κ_p n ≥ λ₀ + 1.5 + (L−1)L^{p−1}/(L^{p−1}−1) + log₂p`.
- That constant is at most the record's `λ + 2.09`, so the record's tabulated range (`X₀ = 2^{20}` through `2^{200}`) carries over.
- Remark 4.8 takes the number after Remark 4.7, so nothing is renumbered.

**D3, the ordinary-scale sentence: included, in structural form only** (drafter's judgment, flagged). The paragraph "The threshold, explicitly" ends: "Configurations at the canonical scale … have `κ_p n` bounded, so at a large threshold they test only the elementary bound `Λ < p/X₀` and not Lemma 7". It does **not** repeat the record's existence claim that the canonical-scale family carries the threshold. I judged that claim to rest on six runs rather than on a stated proof. The author may cut the sentence.

## 3. Coverage of the checklist (`briefs/paper1-v4-items-findings.md`)

**Counts: 92 rows — done 68, changed 10, deferred 14.** "Changed" means applied, with wording or placement different from the checklist's proposal (reason given). "Deferred" means left for the author or the main session.

| Item | Rows | Done | Changed | Deferred |
|---|---|---|---|---|
| 1 | 27 | 17 | 8 | 2 |
| 2 | 16 | 10 | 1 | 5 |
| 3 | 16 | 14 | 0 | 2 |
| 4 | 24 | 23 | 1 | 0 |
| 5 | 3 | 3 | 0 | 0 |
| 6 | 6 | 1 | 0 | 5 |

### Item 1

| Row | v4 location | Status |
|---|---|---|
| 1.1 | Abstract, cycle sentences | **changed.** Per D4 there is no "main new theorem". Both scopes are stated: all-`p` with its scope words, and `X₀` for `p ≥ p₁(X₀)`. The credit chain follows D4. |
| 1.2 | Abstract, and the paragraph after Prop 4.1 | **changed.** The abstract also names Böhm–Sontacchi; the checklist had proposed leaving the abstract unchanged. |
| 1.3 | Author's note | **deferred** (D6; `% AUTHOR:` marker). |
| 1.4 | Author's note | done. The author's decision: the sentence is accurate as written, and its `% AUTHOR:` comment says so. |
| 1.5 | Intro ¶1 | done. The scope reads "at every period, and at every size threshold `X₀` for all periods `p ≥ p₁(X₀)`". |
| 1.6 | Intro ¶2 | done (Steiner; Rozier 1990; LaDue; Williams). |
| 1.7 | Related work, provenance ¶ | **changed.** The Williams correspondences (her Prop 3.3, Thm 3.6, Prop 3.10 ↔ Prop 2.2(iii), (i), (ii)) are placed in provenance, not after Prop 2.2's proof. The checklist left placement to the author. |
| 1.8 | Contributions (i) | **changed.** The `[[F]]` clause sits in the provenance paragraph rather than in (i), as the one sentence D5 asks for. |
| 1.9 | Contributions (v) | **changed.** It reads "a proof of that trim's sharpness", without "the main new theorem", following D4. |
| 1.10 | Intro ¶3 | done (unchanged). |
| 1.11 | Related work | done. `rozier90` is in the cycle-literature list, and the trim paragraph is new. |
| 1.12 | Related work, trim ¶ and the Merle sentence | **changed.** The optional Knight clause is omitted (D7 does not list Knight). `[[X0]]` is resolved. |
| 1.13 | Provenance ¶ | **changed**, per D5 as revised. Only the mechanism is dated to the March 2023 note, and it is cited as classical. The coordinate `x + 1 = 2^m 3^a ω` is dated to the author's hand work of December 2025. It was named and formalized as `(ω, d)` with ChatGPT (from December 2025) and Claude (from March 2026). Williams is cited as independent and posted earlier. No priority or influence is claimed. The text is in §5. |
| 1.14 | Provenance ¶ | done (clause deleted, no replacement). |
| 1.15 | Paragraph after Prop 4.1 | done for (a): Böhm–Sontacchi via Lagarias I item 26, and Tao (1.5). (b), the gcd rotation-invariance, is **not** added. It is optional, and it would be a new claim needing proof in the paper. |
| 1.16 | Thm 4.4 cite list; new paragraph "The dictionary with m-cycles" | done. `m = p` is stated with its proof, the Hercher transfer to `p ≤ 91` is given, and no deep-entry claim is made (`[[12.4]]` §4). |
| 1.17 | Thm 4.5 header and the paragraph after its proof | done (D1). |
| 1.18 | Thm 4.6 closing sentence | done (D15). |
| 1.19 | "Sharpness evidence and assessment" | done (removed, D2). |
| 1.20 | "Verification and record" ¶ | **changed.** The Status paragraph is replaced by a verification paragraph. The framing sentence moves to the abstract, related work and "The threshold, explicitly". The pin is `\recordcommit` (PIN-AT-BUILD). The v2 pointer is dropped. |
| 1.21 | Remark 4.7 | done (unchanged). |
| 1.22 | Version note | done (D11). |
| 1.23 | Date line | done. Version DOI placeholder plus concept DOI. |
| 1.24 | Thm 3.3 and its proof | done (D14). |
| 1.25 | §5 | done (D9): "one-division-map time"; plus a clause at the intro's definition of `T` that it is Tao's `Syr`. |
| 1.26 | §5 non-iteration sentence | **deferred.** This is the optional Tao p. 2 / Prop 1.11 refinement. v3's sentence is not wrong, and I did not hold Tao. |
| 1.27 | Appendix A | done (PIN-AT-BUILD). |

### Item 2

| Row | Status |
|---|---|
| 2.1 | done: the new Version note has no drafting-time language. |
| 2.2 | done: nothing is needed in v4. The v3 notes field stays on v3. |
| 2.3 | done: the v2 pointer is gone from the body. |
| 2.4 | done: the result is stated with its proof. |
| 2.5–2.9 | done (carried forward; the assessment paragraph is removed). |
| 2.10 | done: scope restated in the Version note and the VH entry. |
| 2.11 | **deferred**: HANDOFF citation guidance, main session. |
| 2.12 | **deferred**: collatz-lab.org pin (D12). |
| 2.13 | **deferred**: the joint note (D15 keeps its citation valid). |
| 2.14 | **deferred**: `publication.md`, owned by the alignment window. See §5. |
| 2.15 | **deferred**: ccchallenge (D12). |
| 2.16 | **changed**: applied through the Zenodo description (abstract first, as HTML). VH's preface line "Each version's Zenodo release description carries the same text" is left as is. |

### Item 3

| Row | Status |
|---|---|
| 3.1 | done: Thm 4.6(i), with its proof. |
| 3.2 | done: after Prop 4.1. |
| 3.3 | done: the dictionary paragraph. |
| 3.4 | done: Thm 3.3. |
| 3.5 | done: intro and §5. |
| 3.6 | **deferred** (optional, as 1.26). |
| 3.7–3.14 | done (left, as the checklist says). |
| 3.15 | **deferred** (optional, as 1.15b). |
| 3.16 | done: Thm 4.6(ii)–(iii), the paragraph "The threshold, explicitly", and Remark 4.8. |

### Item 4 (bibliography)

| Row | Status |
|---|---|
| 4.1 `rozier91` | done; the title is as CS read it from the scan. |
| 4.2 `rozier90` | **changed.** I read the title and pages on the scan (2 pages, fetched 2026-10-19). The title is "Démonstration de l'absence de cycles d'une certaine forme pour le problème de Syracuse", correctly spelled, unlike the copies in Lagarias and ccchallenge. **Pages 9–10**: the article is signed on p. 10. Lagarias I and ccchallenge give 9–12. The volume number "1" is taken from Lagarias, since the scan says only "N°3 mai 1990". |
| 4.3 `brox`, 4.4 `hh` | done. |
| 4.5 `williams` | done. Re-checked 2026-10-19 on the arXiv abs page: still v1 only, no journal-ref. |
| 4.6 `ladue` | done, cited with no lemma locator, since the journal's numbering was not checked. |
| 4.7 Knight | done: not cited, per D7's list. |
| 4.8 `bohm` | done. **The statement was checked at a reliable secondary source: Lagarias, annotated bibliography I (arXiv math/0309224), item 26.** It gives the rational cycle element as `x = Σ_{k=0}^{m−1} 3^{m−k−1}2^{v_k}/(2^n − 3^m)`, which is Prop 4.1's equation. Bibliographic data and series "(8)" are from Lagarias plus the record's `cycles.md` 12.6.1.7, which cites Zbl 0417.10008 and an EuDML check of 2026-09-04. The primary (Lincei archive) was not read. |
| 4.9 Steiner 1981 | done: not cited. |
| 4.10–4.21 | done. Applied: the `sdw` DOI; `steiner` "and Computing" and Congr. Numer. 20 (from Lagarias, secondary); the `hercher` corrigendum; `barina` no. 7; `terras` DOI; `merle` at the version DOI 19790406 with the concept DOI beside it (D10); `bl` Corollaire 2 in Thm 3.3; `tao` (1.5). |
| 4.22–4.24 | done (no change; concept DOI used; "one week" uses CS's v1 date of 2026-07-09, not re-checked). |
| new `sos`, `swierczkowski` | Added for the three-distance theorem used in Thm 4.6(iii). Świerczkowski was checked on Crossref (DOI 10.4064/fm-46-2-187-189). **Sós 1958 is entered from standard bibliographic knowledge and was not checked at source.** |

### Items 5 and 6

- **Item 5:** all three placeholders are resolved. `[[12.4]]` gives `m = p` and the dictionary paragraph. `[[F]]` gives "in part", in one sentence. `[[X0]]` gives Thm 4.6(ii)–(iii) and Remark 4.8.
- **Item 6:**
  - 6.1 done (the Zenodo description file).
  - 6.2–6.6 **deferred** (ccchallenge, README, collatz-lab.org, `publication.md`, HANDOFF: the author's or the main session's).

## 4. Markers in the v4 source

**`% AUTHOR:`**, three comment blocks, all in the Author's note; the text itself is v3's, unchanged:
- **L58:** header. The note is in the author's voice and the rewording is his.
- **L61:** "We cleaned my idea up into the states (ω,d)…". Accurate as written (the author's decision, 2026-10-19). No change needed.
- **L65:** "That simplification is what enables… a uniform trim that caps what size-counting can achieve…". **Wrong in its second item**: the trim is Rozier and SdW, obtained without these coordinates. Row 1.3's option is quoted.

**`% PIN-AT-BUILD`**, five:
- **L29:** `\recordcommit`, the record commit. It is used in the Verification paragraph and in Appendix A, and renders as a bold "[record commit, pinned at release]".
- **L36:** the month on the date line.
- **L53:** the month in the Version note.
- **L330:** the Verification and record paragraph (the pin is via `\recordcommit`).
- **L540:** Appendix A; the commit must be reachable on the public repository.

**`% DOI:`**, two:
- **L26:** `\vfourdoi`, which renders as a bold "[v4 version DOI]" on the title page and in the Version note.
- **L52:** the Version note.

The two visible placeholders, **[v4 version DOI]** and **[record commit, pinned at release]**, are deliberate. The PDF in `paper/` is a draft and must be rebuilt after both are filled.

## 5. Sentence-level sweep: the abstract, related work and Version note against the findings

**Abstract** (verbatim in `briefs/paper1-v4-zenodo-description.md`):
- "the states appear independently as the skeleton rows of Williams (2026)": CS §5. ✓
- "a one-line elimination identity (the Böhm–Sontacchi cycle equation in block form)": row 1.15; Lagarias I item 26. ✓
- "rederivations … of the classical trim … (Rozier 1991; Simons–de Weger 2005)": NR §4.1, CS §3.1. The trim is called classical, not new. ✓
- "We prove that this exponential loss is intrinsic to size arguments": the residue not found in NR §4.2 or CS §3.2. Proved in Thm 4.6. The word "new" is not used. ✓
- "slack between two absolute constants at every period (`p ≥ 16` by proof, `3 ≤ p ≤ 15` by finite check, `p ∈ {2,4}` by exhibition)": 12.8.6 scope words, as D2 requires. ✓
- "with every cycle element at least a threshold `X₀`, at every period `p ≥ p₁(X₀)`, with slack exceeding the trim's own exponent by at most an absolute constant": 12.8.7.4, `γ − κ_p n ≤ λ₀ + 1.5`. ✓
- "realizes Rozier's 1991 extremal, which Simons–de Weger expected in 2005": D4's framing. The body says what is realized: "the minimax value … not the inequality of his Lemme 4". Of 12.8.7's list of things v4 must not say, Lemme 4 is respected. ✓
  - **Flag:** for the all-`p` family of (i) the realization is weak. There `κ_p n ≈ 0.59`, so `κ_p n ≤ ρ₀ ≤ κ_p n + 4.6` holds trivially. It has content at the threshold scale, Thm 4.6(iii).
- "the analogue in the cycle-length parameter, and the conclusion that uniform cycle exclusion needs divisibility input, are Halbeisen–Hungerbühler's (1997)": NR §4.2 item 2; D4. ✓
- **Not said, per 12.8.7's list:**
  - that the trim is new;
  - that Lemme 4 is attained;
  - that SdW's "at best a constant" is settled ("The threshold, explicitly" says it is open);
  - that the unit-block staircase works at the threshold scale (Remark 4.8 says the opposite);
  - anything about exclusion (the Verification paragraph's last sentence).
  ✓

**Related work and provenance:**
- The trim paragraph attributes Lemme 4, Brox, and SdW Lemmas 7, 14 and Thm 3, and calls our proof a rederivation. ✓
- "Theorem 4.6 realizes Rozier's extremal … the sharpness Simons and de Weger expected." ✓ (as above).
- The Merle/Chang sentence ends "neither contains the anchor machinery or the exact per-step laws". Literally true; "the counting-limit dichotomy" is removed. ✓
- Provenance, verbatim from the source with TeX simplified: "The mechanism underneath the reduced coordinates — each rising step trades a factor of 2 for a factor of 3 — comes from the author's hand-drawn note of March 2023, and is classical (Steiner; see also Rozier and LaDue). The reduced coordinate itself, the factorization x + 1 = 2^m 3^a ω with its odd core ω, was worked out by the author by hand in December 2025, and was named and formalized as the state (ω,d) in AI-assisted work: with ChatGPT (OpenAI) from December 2025, and with Claude (Anthropic) from March 2026. The same states, with their representative fibre and intra-block cascade, appear independently as the skeleton rows (λ,k) of Williams, posted earlier, …" Neither priority nor influence is claimed. ✓ (D5 as revised; CS §6).
- Title-page footnote and Appendix A: both AI phases are named, and no conversation is quoted or linked. ✓
- "any overlap … not in the coordinate system" is deleted (D5). ✓
- "Section 3 answers it in part: … exact laws for where a trajectory leaving a row lands … but none for which skeleton is entered, where F restates her Proposition 3.10." This is the Williams calibration verbatim in substance. "In part" is kept. Neither the sweep's superseded "answers (1)" nor "answers" alone is used. ✓

**Version note:**
- "attributes the uniform trim … presents it as a rederivation" ✓.
- "states the sharpness … with its proof, in place of the assessment and status report of v3" ✓.
- "No statement is renumbered" ✓ (checked on the PDF: Prop 2.2, Thm 2.3, Thm 3.3, Lemma 3.4, Thm 3.5, Thms 3.7–3.8, Heuristic 3.9, Prop 4.1, Cor 4.2, Lemma 4.3, Thms 4.4–4.6, Remark 4.7, Hyp 5.1 and Lemma 5.2 are as in v3; Remark 4.8 is new).
- There is no drafting-time self-description. ✓

**Elsewhere in the body:** a grep for `\bnew\b` returns only the Author's note ("completely new to me"), the provenance sentence ("not new as objects") and §5 ("is not new here"). "dichotomy", "invention", "assessment" (except the Version note's "in place of the assessment") and the old pins `6285485` and `9d9d1ec` are all absent.

## 6. Flags for the main session (no wiki page was edited)

1. **The 12.8.7 constant.** The derivation supports `2^{−(λ+1.5)} = 0.0540518…`, with `λ = 2.7095122450` as printed by `experiments/staircase_x0_threshold.py`. `cycles.md` 12.8.7 and `briefs/staircase-x0-threshold-findings.md` now state `0.054` (commit `6642ceb`, the only wiki edit of this window, with the derivation in its message). These files outside this window still print `0.0541` and are not edited:
   - `publication.md` L39;
   - `briefs/ceiling-wiki-alignment-findings.md`;
   - `briefs/merle-round19-pr-findings.md`;
   - the round-19 patches `0002` (LEDGER L-A12) and `0003` (the R19 letter). These are prepared for an outward PR and need the same correction before posting.
2. **Rozier 1990 pages:** 9–10 on the scan, against 9–12 in Lagarias and ccchallenge (row 4.2).
3. **TOUR.md L22** (paper 1 "names the one-division map in words only") is now accurate for v4 §5's fixed sentence. It was inaccurate for v3 (checklist §7 item 3).
4. **The composed proof** (12.8.6.1 + 12.8.7.2 under (H1′)) is printed in the paper but is not itself a record statement. If the record should carry it, it is one sentence in 12.8.6's Scope or 12.8.7.2.

## 7. The author's remaining decisions

1. **The Author's note.** Reword the sentence marked at L65 (the uniform-trim item). L61 stands as written. Then delete the `% AUTHOR:` comments.
2. **Appendix A's wording.** It says "the AI collaborators carried out the mathematical development". That covers both phases. Narrow it if the ChatGPT phase should read as exploratory only.
3. **At minting:**
   - fill `\vfourdoi` and the two months;
   - fill `\recordcommit` with a commit reachable on the public repository (push `main` first);
   - rebuild the PDF;
   - finalize the VH v4 section (month, DOI, remove its DRAFT comment) and the Zenodo description's `[month]`.
4. **D3's ordinary-scale sentence:** keep as written (structural, at the end of "The threshold, explicitly") or cut.
5. **Optional items left out:**
   - the gcd rotation-invariance (rows 1.15b, 3.15);
   - the Tao p. 2 / Prop 1.11 refinement (rows 1.26, 3.6);
   - the Knight clause (row 1.12; D7 omitted it).
6. **Sós 1958:** confirm the bibliographic entry at source before release.
7. **Length.** 15 → 21 pages, mostly from Theorem 4.6's proof. If shorter is preferred, the construction's well-definedness and climb steps could point to `cycles.md` §12.8.6.2 and §12.8.7.2. D2 allows condensing with pointers.
8. **D12 and listings after minting** (unchanged): the ccchallenge request, the collatz-lab.org pin, README L3, `publication.md`, and HANDOFF's citation guidance.

## 8. Record

- **Commits on the branch:**
  - `c055b6b`: v4 source and PDF.
  - `8a9211c`: the VH v4 section and the Zenodo description.
  - `1109f1e`: this file.
  - `e4ad005`: merge of `main`.
  - `6642ceb`: the 12.8.7 constant (`cycles.md`, `briefs/staircase-x0-threshold-findings.md`).
  - `d9b9058`: provenance, the method disclosure, the L61 comment, VH brought into line, PDF rebuilt.
  - The commit carrying this file's current state.
- **Build:** `pdflatex -interaction=nonstopmode -halt-on-error collatz-reduced-v4.tex`, three runs in `scratchpad/build/`. The source there was checked byte-identical (`cmp`) to the committed one before the PDF was copied in.
- **Encoding:** `python experiments/encoding_scan.py` returned CLEAN before the first commit and again before this one.
