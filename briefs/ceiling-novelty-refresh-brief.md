# Brief: novelty refresh for the counting ceiling — is the uniform trim + staircase sharpness (paper 1 Theorems 4.5/4.6; cycles.md 12.8, 12.8.6) already in the literature? — for a delegated session

**Why now.** `publication.md` rates the uniform trim + staircase sharpness the program's "best candidate for a genuinely new result", on a novelty snapshot dated 2026-08-03. Snapshots of this kind have gone stale before (Inselmann 2024 subsumed an AEH consequence and was caught only at round 2). The joint note with Merle (`NOTE-v1.md` in the shared repo; the full second version not yet drafted) takes Theorem 4.6's closing sentence as *the* obstruction it locates, so the claim of novelty carries a paper that does not yet exist. This window tests it before anyone builds on it. The author asked for it (2026-10-18).

**Context required before starting (in order):** `README.md` (binding stopping rules), `AGENTS.md`, `publication.md` (the 2026-08-03 snapshot — read the 12.8 line, the 12.6.2 ceiling-lemma line, and what was searched), `cycles.md` 12.8 and 12.8.6 (the result as it now stands — stronger than published: a `γ` demand not growing with `p`, achieved `γ` bracketed by absolute constants), `paper/collatz-reduced-v3.tex` §4 (Theorems 4.5, 4.6, `thm:staircase`, and the related-work paragraph as published), `briefs/tao-section5-read-findings.md` (the Tao-subsumption check, verdict negative), `briefs/jointnote-premise-external-findings.md` (Hercher's clauses; what the joint note leans on), `TOUR.md` (the terms-against-the-literature dictionary — search under the literature's names, not ours).

## The claim under test (state it in the literature's terms before searching)

Two parts, assessed separately:
1. **Upper half (Theorem 4.5):** a trim uniform in the number of blocks `p` exists and, with an effective irrationality measure of `log₂3`, gives effective finiteness of cycles at every period: `n ≤ n₀(p) = O(p·(log₂3)^p)`.
2. **Lower half / sharpness (Theorem 4.6, `thm:staircase`, 12.8.6):** no trim uniform in `p` extends the small-period constants — there are explicit configurations (the staircase family) satisfying every rotation's exact size condition `q ≤ R_r` with slack `γ = K − log₂ q` bounded, so size-counting exclusion is capped; uniform exclusion needs divisibility input. Proved in the wiki at every period (unconditional for `p ≥ 16`, finite check `3 ≤ p ≤ 15`, exhibition at `p ∈ {2,4}`).

The *idea* "size/counting arguments alone cannot exclude all cycles" is folklore and is not the claim; a match must be a statement that pins the cap (exponential-in-`p`, or equivalent in the source's parameters — number of local minima `m`, of odd steps, of "circuits") and/or exhibits configurations meeting all the size inequalities. Record near-misses with exactly what they lack.

## Where to look (minimum)

- **The cycle-bound line, read for remarks on the limits of their own method:** Steiner 1977; Belaga–Mignotte (1998, and later); Simons 2005, Simons–de Weger 2005; Hercher 2023 and its June-2026 corrigendum; Eliahou 1993; Halbeisen–Hungerbühler 1997; Brox 2000; Knight 2026 (*Discrete Math.* 349(3), 114812). In each, any sentence about why the method cannot be pushed to all `m` / all lengths — quote it, with page.
- **Surveys and annotated bibliographies:** Lagarias (1985; the annotated bibliographies 1963–1999 and 2000–2009; *The Ultimate Challenge*, 2010), Chamberland's survey, Wirsching 1998 (LNM 1681).
- **2024–2026:** arXiv math.NT / math.DS / math.GM, Google Scholar, zbMATH: Collatz/3x+1 cycles, "m-cycles", "linear forms in logarithms" + cycle, "counting argument" / "size argument" / "barrier" / "limitation" + Collatz cycle; Tao's blog posts and comments on cycles; ccchallenge.org's register of cycle papers. Follow citations forward from Simons–de Weger and Hercher.
- **Neighbouring frames that could contain it under another name:** generalized `ax+b` maps and their cycles (e.g. `3x+k`, Lagarias's `3x+k` cycle papers), Böhm–Sontacchi, Crandall 1978, Matthews's generalized-map work, the negative-integer / `3x−1` cycles as a barrier argument.

## Rules

- **A label is not a match.** A paper using the word "barrier" or "limitation" matches only if its statement implies one of the two parts; write out the implication or the gap.
- Record every source as **read at source** (held: URL/DOI, page, date) or **relied on via citation** (who cites it, saying what). Paywalled and unheld items are listed as such; do not characterize their content beyond what a held source says about them.
- Calibrate: verdict per part — *subsumed*, *partially anticipated* (name what's anticipated and what isn't), *not found in this search*. "Not found" is the strongest verdict a search can give; do not write "new".
- No computation is required; if a candidate source states a construction, a short check that it meets the size conditions is welcome, in fresh code under `experiments/`, with one documented command reproducing its committed output.
- Nothing outward: no email, no posting, no push. If a command is denied, stop and hand it back.
- Edit with the Edit/Write tools only; run `python experiments/encoding_scan.py` before the last commit and record the RESULT line. Work in the foreground; do not stop until the commits exist.
- Do not edit `publication.md`, `cycles.md`, the papers or the joint note. Proposed changes go in the findings, for the main session.

## Deliverables

Branch `ceiling-novelty-refresh`, cut from current `main` (**first** `git merge --ff-only main` if your worktree started behind — this brief is committed on `main`; record the base SHA). `briefs/ceiling-novelty-refresh-findings.md`:
1. The claim restated in the literature's terms (and the dictionary used).
2. The search log: queries, databases, dates, hit counts read.
3. The source table: source → held/cited → relevant statement (quoted, with page) → relation to part 1 / part 2 → verdict.
4. Verdict per part, and the closest prior statement found for each, with exactly what it lacks.
5. For the main session: proposed wording for `publication.md`'s 12.8 line (current state, one dated verification line, no change-log prose); whether paper 1's related-work paragraph or the joint note would need a citation added; anything the author must decide.
