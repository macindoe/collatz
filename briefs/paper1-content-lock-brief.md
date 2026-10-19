# Brief: lock paper 1's content before the readability rewrite — a claims ledger of the v4 draft — for a delegated session

**Why.** The author decided (2026-10-19) that before v4 is minted, the paper is rewritten to be human-readable: for a **curious non-specialist reader** (the author's own background — electrical engineering and music, not mathematics), **one document**, with the main text carrying the ideas in layers and **the majority of the mathematics in appendices** "where the real nerds (and AI) can dig and dispute". The rewrite may move and re-explain; it may not strengthen, weaken, add or drop a claim. This window produces the baseline the rewrite will be checked against.

**Read first:** `README.md`, `AGENTS.md`, `paper/collatz-reduced-v4.tex` (all), `briefs/paper1-v4-draft-findings.md`, `briefs/paper1-v4-items-findings.md`.

## Items

1. **Claims ledger** `paper/collatz-reduced-v4-claims.md`: one row per mathematical claim in v4 — every Definition, Lemma, Proposition, Theorem, Corollary, Remark with mathematical content, and every quantitative sentence in the abstract, introduction, related work and status paragraphs. Columns: ID (stable, e.g. `C-4.6(ii)`), the LaTeX label, the exact statement (verbatim or a faithful compression that preserves every quantifier, constant and scope word), its grade (proved here / proved in the record with a pointer / cited / conjectured / measured), where its proof lives, its credit (whose result; our rederivation or ours), and its verification line.
2. **Prose claims that are not theorems** (provenance, method disclosure, credit chain, what is not claimed) as a second table — these must survive the rewrite too.
3. **Open author items** carried as rows marked AUTHOR (the Author's note line 65; the Appendix A sentence "the AI collaborators carried out the mathematical development", which now spans the ChatGPT phase; any `% AUTHOR:` marker), and the `% PIN-AT-BUILD` / `% DOI:` placeholders.
4. **A proposed layer map** for the rewrite (a suggestion, not the rewrite): which claims belong in the main text's layers — the map; blocks (the 2-for-3 trade); states `(ω, d)` and `F`; the exact laws; cycles and the limit of counting; the equidistribution conjecture — and which move to appendices, with one sentence each on what the non-specialist reader needs in the main text.
5. Tag nothing; the main session tags the lock commit after review.

## Rules and deliverables

Do not edit the `.tex`. Nothing outward; if a command is denied, stop and report. Edit/Write only; encoding scan before the last commit; foreground until committed. Branch `paper1-content-lock` from current `main` (`git merge --ff-only main` first if behind; record the base SHA). Deliverables: the claims ledger, `briefs/paper1-content-lock-findings.md` (counts, anything in v4 that could not be stated as a claim cleanly, the layer-map proposal, open author items).
