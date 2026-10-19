# Brief: check the readable rewrite of paper 1 v4 against the content lock, claim by claim — for a delegated session

**Why.** `paper/collatz-reduced-v4.tex` was rewritten for a curious non-specialist reader (branch `paper1-v4-readable`, commits `d421851`, `82da95c`), presentation only, against the lock at tag `paper1-v4-content-lock` (`paper/collatz-reduced-v4-claims.md`). You did not write it. Your job is to find every place the rewrite changed content.

**Read:** `AGENTS.md`; the claims ledger at the tag; `paper/collatz-reduced-v4.tex` at the tag and at the branch head; `briefs/paper1-v4-readable-findings.md` (the writer's own placement table and its 15 self-flagged paraphrases — check them, but do not rely on its placement table: build your own).

## Items

1. **Appendices B–E vs the locked §§2–5:** confirm by mechanical diff that the moved formal text differs only by the declared renames (ε→ξ, ε_t→χ_t, T_j→μ_j, S→s_tot, T_N→H_N, Λ_N→E_N, H→script H), cross-reference rewording and new labels/headings. Any other difference is a finding.
2. **Every live Table A row, every P row and every N row:** locate it in the new text yourself; verdict *present, same scope* / *present, scope changed* (quote both) / *missing*.
3. **The main text (§§1–8):** read every sentence that states a mathematical fact, a credit or a provenance claim. Each must be backed by a ledger row and must not exceed it (scope words, quantifiers, constants, grade — "proved" vs "heuristic" vs "measured" vs "conjectured"). New sentences with no row (e.g. "It does not settle the Collatz conjecture"; "every odd number below 2^71 reaches 1, so …"; "a size-passer need not give a cycle") get a verdict: supported by which row / unsupported.
4. **Recompute the worked examples** (x = 7 block and states; the state (1,2) cascade; the p = 7 staircase picture's numbers, including K = 149 and exit valuation 49; the eight-class table) in fresh code.
5. **The concordance (Appendix H):** spot-check every row against both PDFs (`pdftotext`).
6. Build the PDF yourself; 0 undefined references.

## Rules and deliverables

Do not edit the `.tex` — findings only. Nothing outward; if a command is denied, stop and report. Edit/Write only; encoding scan before committing; foreground until committed. Work on branch `paper1-v4-readable-check` cut from `paper1-v4-readable` (record the SHA). Deliverables: `experiments/paper1_v4_readable_examples_check.py` + output (one command), `briefs/paper1-v4-readable-check-findings.md` (per-row verdict table, every scope change quoted, unsupported sentences, the diff verdict, example checks, and a list of exact fixes proposed).
