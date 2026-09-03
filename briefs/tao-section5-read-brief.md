# Brief: does Tao's proof deliver the letter statistics past the digit budget? (Section 5 read, 2026-09-04)

Delegation brief. Main session drives; the delegate produces. Read `README.md` (stopping rules), `AGENTS.md`, and the register norm in `HANDOFF.md` first. This is a literature read with a conditional edit, not a research task.

## 0. Discipline

- Work in the worktree named in your prompt, on its own branch cut from the tip of local `main` (which carries this brief). First command: `git rev-parse --short HEAD`, `git branch --show-current`. Report base SHA.
- Edit only with the Edit/Write tools; run `python experiments/encoding_scan.py` before the final commit. Commit messages end with `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`.
- Pages you may edit, and only if Section 4's condition is met: `publication.md` (the AEH verdict bullet), `aeh.md` 13.2 ("What has not been carried past it, as far as the literature check reached ...") and 13.3.3 if affected. No other page. A parallel delegate owns README.md, stage4.md, bridge.md, cycles.md, HANDOFF.md, experiments/ -- do not touch them.
- No proof attempts, no new theorems, no re-derivation of Tao. Quote; do not paraphrase where a quotation is possible. Every claim about Tao carries a page and an equation or proposition number.
- Wait in the foreground; do not stop until the findings commit exists.

## 1. The question

publication.md's AEH verdict says: "What no source checked contains: ... the distributional content -- the full 2^-j marginal at every j, the 1/3 rate, the depth law as a measure -- along horizons past the digit budget, which the classical cylinder count reaches only to theta < 1/4 block per bit." aeh.md 13.2 says the same in its own words. The fresh-eyes assessment of 2026-09-04 suspects this is carried by Tao's *proof* at logarithmic density even though his *theorem* (1.3) is about the minimum only: the descent is built from stages that each sit inside the Terras budget (Prop 1.9 gives near-iid `Geom(2)` valuations per stage), and the stages are glued by the stabilisation of first passage (Prop 1.11, eqs. 1.19-1.20), whose engine is Prop 1.14. If that is right, the letter statistics along the whole descent are near-Bernoulli for almost all `N` in logarithmic density, and the "unfound residue" shrinks to the natural-density form (Tao's Remark 1.16 names the ingredient natural density would need).

## 2. Inputs

- Tao, arXiv:1909.03562v7, saved PDF, read with the Read tool (`pages`, at most 20 per call):
  `C:\Users\Ace\.claude\projects\c--Users-Ace-Documents-Collatz\2a3d88a6-3bb7-431b-bf8e-78e0b4983e86\tool-results\webfetch-1788447970658-xmq7q0.pdf`
  Fallback: https://arxiv.org/abs/1909.03562 (WebFetch on the abs page works; the PDF via WebFetch does not decode).
- aeh.md 13.2.1 (the hypothesis), 13.2.3 (the clock), 13.2.4 (base case), 13.3.1-13.3.3, 13.6.5 (the Syrac attribution and the renewal-recoding dictionary: block letter `(m, r)` <-> exponent word `(1^{m-1}, 1+r)`).
- publication.md, the AEH bullet and the Inselmann bullet.

## 3. Questions, each answered with citations

- **Q1.** Where Prop 1.11 is derived from Props 1.9 and 1.14 (Section 5 per p.12; check Section 3 too), is Prop 1.9 applied at each scale stage to the *current* law (the first-passage law or the pushforward), giving `d_TV(a^{(n)}(N), Geom(2)^n) << 2^{-c n}` for the next `n` steps? Quote the lemma or display where this happens, and state what `n` is relative to `log` of the scale (i.e., is each stage inside the classical budget?).
- **Q2.** Does the argument yield, for almost all `N` in logarithmic density, that the *empirical* frequencies of every finite valuation pattern along the whole descent from `N` down to `f(N)` converge to their `Geom(2)` probabilities? If Tao states only per-stage TV bounds, write out the per-stage statement exactly, then do the bookkeeping: stages at scales `x^{alpha^k}`, per-stage errors (1.20)'s `log^{-c} x` plus Prop 1.9's `2^{-c1 n}`, the number of stages, and whether the union bound over stages vanishes. Say clearly whether the conclusion is (a) in Tao verbatim, (b) an immediate corollary of displayed statements, or (c) needs an argument Tao does not give.
- **Q3.** Map the answer onto aeh.md 13.2.1 clause by clause: (i) logarithmic vs natural density; (ii) Syracuse-step horizon vs block horizon (the conversion issue recorded at 13.3.2 and 13.2.3 -- do not resolve it, state whether it bites here); (iii) valuation words vs the `(m, r)` letter alphabet (the renewal recoding of 13.6.5); (iv) the budget-rate clause `tau`; (v) the two-sided depth marginal `pi_{k,D}`. For each: delivered / not delivered / delivered in a different time parametrisation.
- **Q4.** Remark 1.16: state exactly what "fine scale mixing of the entire random affine map" would add, and whether Inselmann 2024's `*`-density technique (as recorded in publication.md and aeh.md 13.3.2; re-read arXiv:2402.03276 only if the record is insufficient) already supplies the distributional statement at natural density, or only the envelope and first moment.
- **Q5.** Anything in Sections 3 or 5 that contradicts the reading in Section 1 above.

## 4. Deliverables

- `briefs/tao-section5-read-findings.md`: verdicts Q1-Q5 with quotations and page numbers; a "what changes in the record" section with the proposed wording for publication.md's bullet and aeh.md 13.2's paragraph (and 13.3.3 if affected), each as before/after text.
- **Apply the edits on the branch only if Q1 and Q2 both come out as (a) or (b) with quotations.** Otherwise leave the pages untouched and carry the proposed wording in the findings with the uncertainty stated. Conservative editing: no theorem, proof, or number on those pages moves except the sentences named. One commit per page.
- Report: branch, HEAD SHA, base SHA, commits, and the one-line verdict.
