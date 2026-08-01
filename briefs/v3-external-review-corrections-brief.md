# Brief: fold the external-review corrections into v3 (no v4)

**Branch:** `v3-external-review-corrections`, cut from `e1c7d5f` (session-start HEAD; verify with `git rev-parse HEAD` before you start and say so in your findings).
**Record:** `briefs/v3-external-review-corrections-findings.md`.
**Push:** nothing. Do not push. Do not merge. Hand the branch back.

## Context

`paper/collatz-reduced-v3.tex` carries a reserved Zenodo DOI (`10.5281/zenodo.21730505`) but is **not yet published**. An external reviewer (ChatGPT, reviewing the tex + PDF against the live wiki) filed a report. The main session has already adjudicated every item against the repo; the verdicts below are settled and are **not** yours to relitigate. Your job is to produce the edits, verify them, and record what you did.

Two of the reviewer's findings are real and are *ours*: the paper is stale against the wiki, not wrong against reality. The rest are small defects or labelling fixes. One proposed restructure was **declined** by the author.

Read first, in order: `AGENTS.md` (binding), `README.md` stopping rules, `paper/collatz-reduced-v3.tex` entire, `aeh.md` §13.2 and §13.6 (especially 13.6.3(v), 13.6.4, the (q1)/(q2) bullets, and Proposition 13.6.5), `stage4.md` §11.8.7.6–7, `cycles.md` §12.8.2 and §12.8.6.

## Hard scope limits

- **Edit exactly one tracked file: `paper/collatz-reduced-v3.tex`** (and rebuild `paper/collatz-reduced-v3.pdf`).
- **Do not touch any wiki page.** `aeh.md`, `stage4.md` and `cycles.md` are already correct — the paper is what drifted. If you believe a wiki page is wrong, record it in the findings and change nothing.
- **Do not touch `sources/`, `experiments/`, `viz/`, `README.md`, `index.md`, `publication.md`, `TOUR.md`, `HANDOFF.md`.**
- **No mathematical content changes** beyond items 1 and 2 below. Do not "improve" a proof while doing this work. Separate commits for content vs. structure, per `AGENTS.md`.
- Every claim you import from a wiki page must be **quoted to the number** from that page, not paraphrased from this brief. If a number here disagrees with the page, the page wins and you record the discrepancy.

## The edits

### Content (their own commits)

**1. §5's π_k depth clause is stale. CONFIRMED against `aeh.md` (q2) and Prop 13.6.5.**

Line ~229 says the depth component "receives not Haar measure but the stationary law of the exact window chain. Let π_k denote this product law." `aeh.md` 13.6.5 proves that chain's stationary law is **not** the exact bulk depth marginal: chain `P(a≥2)=4/63`, `P(d=2)=19/63` against exact `2/63`, `20/63`, and fixed-horizon orbit data rejects the chain law (`P(d=2)` off by `0.018`, `≈14` pooled standard errors).

Replace the depth clause so π_k's depth component is the **exact convolution/renewal law of `13.6.3`(v), with marginal `13.6.5`**, and keep the window chain in one clause as what it is — a `~1%`-accurate model, which is the resolution at which §13.4 recorded it.

**Scope discipline — this is the load-bearing instruction.** Do **not** rebuild AEH or its consequences. `aeh.md` line 116 states that the ω-residue/s-word component of π_k is exact and unqualified; the `P(s=j)=2^{-j}` ledger, the exact `1/3` 3-gain rate (which comes from Lemma `lem:absorption`, not from the chain), and the drift are all untouched. Only the depth clause of the *definition* moves. If your edit grows past a few sentences plus a pointer, you have overshot — stop and record why.

Check whether the abstract's "exactly computable product law" and the §1 sentence about `π_k` need any adjustment. Likely they do not (the law *is* exactly computable — more exactly so now). Say what you concluded.

**2. `thm:onestep` (Thm 3.8) claims exact `d_+` from data that does not determine it. CONFIRMED; counterexample verified by the main session.**

`(263,1)` and `(2375,1)` agree on `ω mod 64`, `d mod 16`, `(s,σ)=(2,3)` and `a_+ mod 2`, but have `a_+ = 2, 4` and `d_+ = 3, 5`. Both sit in the third branch of `lem:absorption` (`d = h(s) = 1`, `s` even), where `a_+ = d + v_3(ω + (2^s−1)3^{−d})` — a **3-adic** function of ω that no 2-adic window sees at any `k`. `aeh.md` (q1) says this outright: *"a_{+,n+1} is not a function of any depth-k window at visit n, at any k."* **Re-verify the counterexample yourself with exact integer arithmetic before editing** (report both states' `A, s, C, σ, a_+, d_+`).

The repair is in the paper only. `stage4.md` §11.8.7.6 defines the depth-`k` window as those two residues **together with the stratum labels `(s, σ, a_+)`** — exact labels — and Theorem `11.8.7.6.1`'s proof says `d_+` "is exact from the labels". The paper compressed `a_+` into `a_+ mod 2^k` when merging `11.8.7.3.1`'s data list into `thm:deltaM`.

Therefore:
- **`thm:deltaM` (Thm 3.7) stands unchanged.** `a_+ mod 2^k` genuinely does suffice for `ΔM mod 2^k`, via `ω_+ mod 2^{k+2}`. Do not weaken it.
- **`thm:onestep` gains the labels**: state the depth-`k` window as the residues of `thm:deltaM` *together with the stratum labels `(s, σ, a_+)`*, matching `stage4.md` §11.8.7.6 verbatim in structure. Its proof already says `d_+` is "exact from the stratum data" — make the statement match the proof.
- **Judgement call, yours, recorded:** `thm:deltaM`'s trailing clause "and the stratum data `(s,σ)` are determined by the same residues" is defensible but sits awkwardly beside `a_+` now being a label. Either keep it with a qualifier making clear it does **not** extend to `a_+`, or follow `stage4.md` and make all three labels. Pick one, justify it in the findings, do not do both.
- **Abstract:** qualify "A finite window of digits consequently decides each step" so it is true — the deciding data is a finite residue window **plus the step's stratum labels**. Do **not** adopt the reviewer's "countable shell-indexed chart, not a fixed finite-state window" framing: it overreaches, and the trichotomy's zero-error verification (21,296 real steps) was run with those labels. One clause, minimal.

**3. `thm:vlaw`'s Baker bound is false at `d=1`.** `s ≤ C(ω)(\log d)^2` has RHS `0` at `d=1`; `ω=3, d=1` is lifting with `s=3`. Use `C(ω)(1+\log d)^2`. Confirm the `d=1` instance numerically.

**4. `def:reduced` must require `ω > 0`.** As written `(−1,1)` qualifies: `A=−4`, `s=2`, `C=0`, `v_2(0)` is not finite, `F` undefined. Add the positivity condition. Check nothing downstream silently assumed it.

**5. `thm:uniform`'s `n_0(p)` is called explicit but never defined.** The defining equation is at `cycles.md` §12.8.2 (Corollary 12.8.2, "the unique solution (in `n`) of …"). Import it **verbatim in content**, with the Rhin pin as that corollary states it. Do not restate the corollary's surrounding claims.

**6. `hyp:aeh`'s limit is underspecified.** It currently mixes time averages along one orbit, natural density of starts, a bulk cutoff `X`, and fixed-horizon calibration. `aeh.md` Theorem 13.6.4 has the precise framework: orbit by orbit, bulk frequency over visits with `x_exit > X`, **limit orbit length → ∞ then X → ∞**, no measure on starting values invoked. State the limit order explicitly and handle the reviewer's real sub-point (for a fixed orbit the qualifying visit set need not grow — `aeh.md` 13.6.6's bottom-regime paragraph is why the bulk cut exists). Keep it to the hypothesis statement; do not import 13.6.4's equivalence theorem.

### Labelling and register (their own commits)

**7. `prop:budget` → retitle to a heuristic.** Retitle the environment "Digit-budget heuristic" (or equivalent). The *consumption identity* is proved and stays proved — `stage4.md` 11.8.7.7 is explicit that only the unbounded-horizon conclusion is the organizing heuristic, and `prop:budget`'s own text already says so. Also soften the trailing "and nothing else" in the paragraph after `rem:verify1`'s successor (line ~169). Do not delete the proposition or its content.

**8. The v3 correction paragraph must say the proof is not reproduced here.** Author's decision: **Theorem `thm:staircase` and its hedge stay exactly as they are, and §4 is not restructured.** The 2026-08-01 correction paragraph currently asserts "The two halves compose to a proof for every period `p ≥ 16`" and supplies a URL. Add one explicit clause stating the proof is established in the project record and **is not reproduced in this paper**. The scope sentence already present (unconditional `p ≥ 16`; finite check `3 ≤ p ≤ 15`; `p ∈ {2,4}` by direct exhibition; `γ` between `3.683012` and `5.140212`) is correct — verify it against `cycles.md` §12.8.6 and leave it alone if it matches. One clause. Nothing else in §4 moves.

**9. `thm:smallp`'s "Full details and the searches accompany the paper" → concrete pointers.** Name the wiki sections (`cycles.md` 12.2.3, 12.5.3, 12.7.5, and the trim lemmas at 12.6/12.7.4 — **verify these numbers resolve** before printing them) and the script filenames from `experiments/`. The theorem already says the derivations, not the theorems, are the contribution, and the proof is already labelled "Proof outline" — no overclaim exists, so do not relabel the theorem.

**10. Script filenames + one commit pin.** Author's decision: **filenames and a commit pin, not seeds.** In `rem:verify1`, the trichotomy verification remark, and `thm:smallp`'s outline, name the actual `experiments/` scripts that produced each quoted figure. **Verify each file exists and that the script genuinely supports the figure quoted** — do not print a filename you have not opened. Pin one commit SHA covering the whole record (use the branch's base `e1c7d5f` unless you find a reason not to, and say which). This makes Appendix A's "every computational claim cites a runnable script" true as written; do not weaken Appendix A.

**11. `M_t` collides with the anchor `M(ω)`.** In `prop:elim`, `M_t = Σ_{j>t} m_j`. **Check `cycles.md` first**: if the record uses `M_t` for this object, a silent rename desyncs the paper from the record. Either rename in the paper *and* add a one-line note tying it to the record's name, or keep `M_t` and add a disambiguating parenthetical. Pick the option that keeps paper and record legible together; justify it.

**12. Bibliography metadata.** Fill in what the repo already knows: split the grouped Yu I–III entry into properly citable form, complete the Rhin/Wu entry. The `llmcollatz` entry (arXiv:2603.11066) lacks authors in our record too — **do not invent them**. If you cannot resolve them offline, leave the entry as is and flag it in the findings as an author-side lookup.

### Build (its own commit)

**13. The source does not compile. CONFIRMED by the main session.**

`pdflatex -interaction=nonstopmode -halt-on-error` fails: `! Missing $ inserted. l.30`, **fatal, no PDF produced**. Cause is line 26's `\date{... \;\cdot\; DOI: ...}` — both `\;` and `\cdot` are math-mode-only, and `\maketitle` at line 30 is where it detonates. The committed PDF exists only because the build ran without `-halt-on-error` and TeX's recovery inserted the `$`.

- Fix the date line (`\(\cdot\)`, `\textperiodcentered`, or equivalent — your call, keep the rendered result identical).
- Add `\hypersetup{pdftitle={...}, pdfauthor={...}}`. Verify the metadata is actually blank before and populated after (`pdfinfo` or equivalent); report both.
- **Acceptance gate: `pdflatex -halt-on-error` must exit 0 on a clean run, twice (for refs).** Build in a sandbox temp dir — the mount locks aux files — and copy only the PDF artifact back in.
- Confirm the rebuilt PDF has no clipping, no overfull-box regressions vs. the committed one, and that the DOI link still resolves as written.

## Verification and hygiene

- **Re-verify items 2, 3 and 4 numerically yourself**, with fresh exact-integer code, before you edit. Quote the outputs in the findings. Do not take this brief's arithmetic on trust.
- **Every wiki number you print in the paper must be read from the page**, with the section number quoted.
- **Run `experiments/encoding_scan.py` over the tracked tree before your last commit.** Never edit a tracked file with PowerShell `Get-Content`/`Set-Content` — it double-encodes the `≤ — ε` characters these files are full of. Use the file-editing tools.
- Keep the paper's existing register: the Version note is a published-document convention, not a change log, and `AGENTS.md`'s no-change-logs rule applies to the wiki pages you are not touching. **v3 is unpublished, so rewrite the v3 entry of the Version note to cover these corrections — do not open a v4 entry** and do not append a dated narrative.

## What to report

`briefs/v3-external-review-corrections-findings.md`, structured item by item (1–13), each with: what you verified, the exact command/output where numerical, what you changed, and the file/line. Plus:

- The base SHA you actually cut from.
- **Anything you found that this brief got wrong.** The main session's adjudication is settled on the *verdicts*, not on the details; if a wiki number here is misquoted or an edit turns out to be unsafe, that is the most valuable thing you can report. Record obstructions; do not force an edit to fit the brief.
- Anything you deliberately did **not** do, and why.
- Whether the paper is, in your reading, now internally consistent with `aeh.md` §13.6 and `stage4.md` §11.8.7.6 — and any *remaining* drift you noticed but were out of scope to fix.
