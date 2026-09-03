# Brief: fresh-eyes assessment (2026-09-04) -- filing the scripts, the findings, and three calibration remarks

Delegation brief. Main session drives; the delegate produces. Read `README.md` (binding stopping rules), `AGENTS.md` (schema, proved-claim workflow, no change logs in tracked files), and the register norm in `HANDOFF.md` (flat, calibrated prose; heuristics labeled heuristics) before touching anything.

## 0. Discipline

- Work in the worktree named in your prompt, on its own branch. First command: `git rev-parse --short HEAD`, `git branch --show-current`, `git status`. The branch is cut from the tip of local `main`, which carries this brief; confirm the brief file is present. Report base SHA and branch name.
- Never edit tracked files with PowerShell `Get-Content`/`Set-Content` (HANDOFF quirk: double-encodes UTF-8). Use the Edit/Write tools. Run `python experiments/encoding_scan.py` over the tree before the final commit and report CLEAN.
- Committed script outputs must be produced by Python writing the file (or a Git Bash redirect), not PowerShell `>` (adds a BOM). LF line endings, UTF-8, no BOM.
- One commit per deliverable; separate commits for content and for structure; commit messages say what was checked and why. End every commit message with the trailer line `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`.
- Do not touch `sources/`, `paper/`, `publication.md`, or `aeh.md` (a parallel delegate owns the AEH verdict; see `briefs/tao-section5-read-brief.md`).
- Stopping rules apply: no proof attempt on AEH or on any Fourier bound, no cycle-exclusion attempt, no per-period cycle search. Record obstructions; do not force analogies. If a measured number differs from this brief, the fresh script is the authority: report the discrepancy, do not paper over it.
- Wait in the foreground for every script run. Do not stop until every commit below exists. Final report: branch, HEAD SHA, base SHA, list of commits, one summary line per script output, open items.

## 1. Context: what the assessment found

Fable 5.1 was asked for a fresh-eyes critical assessment of the whole approach on 2026-09-04. Findings, in the register of the record:

1. **Core laws re-verified with an independent anchor implementation.** The anchor `N(u) = -log u / log 9` computed by the 2-adic logarithm SERIES in exact rationals (each term `(u-1)^i/i` is a 2-adic integer of valuation `>= 3i - v2(i)`; partial sums have odd denominators; reduce mod `2^K`), not by the discrete-log tower every existing script uses. Checked: the global valuation law on the two lifting classes plus the mod-8 table off them (720 + 1998 states), the entry-depth law on all six classes (2718), the increment identity `dM = N((w+/w)^2) mod 2^24` (1360 steps), and an independently derived unrolled p-step identity (309 orbits, p <= 8). Zero failures.

2. **The digit budget is a delay line, not a fuel gauge.** Flipping one bit `j` of a 256-bit starting core (177 starts, 40 blocks, k = 8): bit `j` first changes the letter word at block ~ `j/4` (measured 2.2 at j=8, 4.4 at 16, 8.3 at 32, 16.4 at 64, 32.0 at 128; bits >= 200 never within 40 blocks, cumulative sigma at block 40 being ~161). Once read, a bit is never spent: flipping any of bits 1..8 changes the core mod 2^8 with probability 0.95-0.99 at every block 1..40, and changes the letter `s_16` with probability ~0.67, the value for two independent draws from the ledger (`1 - sum 2^{-2j} = 2/3`). The "regeneration" that stage4.md 11.8.7.7 says does not exist is the carry propagation of the multiply by `3^d`; what is not regenerated is local (residue-class) determinism, which is the classical statement (Terras cylinder count; Lagarias shift conjugacy -- citations pinned in publication.md). **One artifact to document precisely:** "core mod 2^k changed" fired for high `j` at blocks 1-3 in the raw run. This is a coordinate effect, not a locality violation: at a resonant step (stage3.md 11.8.6.2.1 case 3, `h(s) = d`, `a_+ = d + v3(w + beta)`) a high-bit flip can change `v3(w + beta)` and move one factor of 3 between `w` and `d`, leaving the underlying integer's low bits and the letters unchanged. The exit integer and the letters obey strict locality. Verify this in the filed script by tracking the exit `x_exit(t) mod 2^k` and `s_t` alongside the core.

3. **The statistical half is a mixing question, and Tao already worked it.** The wiki frames the statistics half as "digit statistics of 2-adic logarithms, beyond current theory". As a statement about one anchor's digits that is right and a dead end. As a statement about orbits it is a mixing question about an explicit multiply-and-shift map, which is the road Tao took (arXiv:1909.03562, v7, read from the PDF): Prop 1.9 p.6 (valuations of `n` steps are within `2^{-c1 n}` of `Geom(2)^n` when `N mod 2^{n'}` is near-uniform, `n' >= (2+c0) n`); Prop 1.11 pp.8-9 (stabilisation of first passage, eqs. 1.19-1.20, TV error `log^{-c} x` between passage laws from scales `x^alpha` and `x^{alpha^2}`); Prop 1.14 p.11 (fine-scale mixing: `Syrac(Z/3^n)` is within `m^{-A}` of uniform on cosets of `3^m Z/3^n Z`, eqs. 1.26-1.27); Prop 1.17 p.12 (characteristic function of `Syrac(Z/3^n)` at `xi` not divisible by 3 is `<< n^{-A}`, uniform in `n`, `xi`); Remark 1.16 p.12 (natural density would need fine-scale mixing of the whole random affine map, not just the offset); Remark 1.4 p.3 (an absolute-constant bound for almost all `N` is likely as hard as the conjecture). Numbers from a fresh DP on `Z/3^j` under iid `Geom(2)` valuations: TV of the stationary law from uniform-on-units 0.346 / 0.371 / 0.389 at j = 3,4,5 (it is NOT uniform; Tao's printed `Syrac(Z/9)` = (0, 8, 16, 0, 11, 4, 0, 2, 22)/63 reproduced exactly); max |Fourier coefficient| depends only on `j - v3(xi)`: 0.577, 0.378, 0.252, 0.177, 0.129 for 1..5 fine digits; mean over unit frequencies 0.153, 0.085, 0.048 at j = 3,4,5. Along real 64-bit orbits at Syracuse steps 35..120 (past the ~32-step budget), the empirical law of `x_t mod 27` is at TV 0.0125 from the DP law and 0.358 from uniform (noise ~0.005); mod 81: 0.018 vs 0.385 (noise ~0.009). The README clause "empirically solid, theoretically untouched by anyone" contradicts publication.md. Whether Tao's *proof* delivers the letter statistics past the budget at logarithmic density is handed to the parallel Section 5 read; do not prejudge it in any page.

4. **The parked cycle condition is Tao's offset map evaluated mod `q`.** With `F_n(a) = sum_{m=1}^{n} 3^{n-m} 2^{-a_{[m,n]}}` (Tao eq. 1.5), the block-to-Syracuse dictionary block `(m_t, s_t)` -> valuations `(1, ..., 1, 1 + s_t)` (`m_t` entries; `|a| = K = n + sum s`, `n = sum m`), and `a` read from block 0 onward, the exact identity on EVERY profile (no closure; 3000 random profiles, entries 1..6, p <= 6, zero failures) is

   ```text
   2^{m_0} * R_0 = 2^K * F_n(a) + q,      q = 2^K - 3^n,
   ```

   derivation: `R_0 = u_0 q` with `u_0` the odd seed at block 0's entry `e_0 = 2^{m_0} u_0 - 1`, and Tao's cycle equation at `x = e_0` reads `e_0 q = 2^K F_n(a)`. Hence `q | R_0  <=>  2^K F_n(a) = 0 (mod q)` (2 is a unit mod `q`); agreement 3000/3000. The formula `x = 2^K F_n(a)/q` returns the known cycles from their valuation words: `x = 1` (a = (2)), `x = -5` (a = (1,2), q = -1), `x = -17` (a = (1,1,1,2,1,1,4), q = -139); the p = 7 staircase of 12.8.3 (m = (4,7,9,15,23,35,1), s = (1,1,1,1,1,1,49), n = 94, K = 149) fails both conditions. Reading: one object, two moduli -- mod `3^k` the same `F_n(Geom(2)^n)` is fine-scale equidistributed (Tao, proved); mod `q` the parked condition asks that it not concentrate at 0; 12.6.1.5's margin heuristic is the equidistribution-mod-`q` assumption written out. A naming, not a lever. Classical attribution to check: the linear cycle equation is usually credited to Boehm and Sontacchi (1978), Atti Accad. Naz. Lincei Rend. Cl. Sci. Fis. Mat. Nat. 64, 260-264, "On the existence of cycles of given length in integer sequences like x_{n+1} = x_n/2 if x_n even, and x_{n+1} = 3x_n + 1 otherwise". Verify this citation by web search before writing it; if it cannot be verified, cite Lagarias's 1985 survey (already pinned in publication.md) for the cycle equation and say the Boehm-Sontacchi attribution was not verified.

5. **No lever, no sidestep.** Front statuses are unchanged everywhere. Further coordinate changes are not recommended.

Scratch scripts (session scratchpad, uncommitted; copy them, do not link to them):

```text
C:\Users\Ace\AppData\Local\Temp\claude\c--Users-Ace-Documents-Collatz\2a3d88a6-3bb7-431b-bf8e-78e0b4983e86\scratchpad\fresh_spotcheck.py
C:\Users\Ace\AppData\Local\Temp\claude\c--Users-Ace-Documents-Collatz\2a3d88a6-3bb7-431b-bf8e-78e0b4983e86\scratchpad\avalanche.py
C:\Users\Ace\AppData\Local\Temp\claude\c--Users-Ace-Documents-Collatz\2a3d88a6-3bb7-431b-bf8e-78e0b4983e86\scratchpad\fourier3.py
C:\Users\Ace\AppData\Local\Temp\claude\c--Users-Ace-Documents-Collatz\2a3d88a6-3bb7-431b-bf8e-78e0b4983e86\scratchpad\cycle_offset.py
C:\Users\Ace\AppData\Local\Temp\claude\c--Users-Ace-Documents-Collatz\2a3d88a6-3bb7-431b-bf8e-78e0b4983e86\scratchpad\offset_identity.py
```

Tao's PDF (arXiv 1909.03562v7), readable with the Read tool's `pages` parameter:

```text
C:\Users\Ace\.claude\projects\c--Users-Ace-Documents-Collatz\2a3d88a6-3bb7-431b-bf8e-78e0b4983e86\tool-results\webfetch-1788447970658-xmq7q0.pdf
```

## 2. Deliverable 1: four scripts into `experiments/`

Names and the page each supports (state it in the header comment, per AGENTS.md):

- `experiments/law_spotcheck_logseries.py` -- supports spine.md 9.8, stage1-synthesis.md 11.8.4.1, stage3.md 11.8.6.3, stage2.md 11.8.5.6, cycles.md 12.6.1 (unrolled identity). Merge `fresh_spotcheck.py`. Add a calibration line: the series anchor must reproduce the published `N(17) = 38, N(25) = 245, N(33) = 236 (mod 2^8)` (stage1-synthesis.md, remark after 11.8.3.6.6); print the match.
- `experiments/digit_budget_avalanche.py` -- supports stage4.md 11.8.7.7 (calibration paragraph you will add). Merge `avalanche.py` and add: tracking of `x_exit(t) mod 2^k` and of `s_t`; three separate change matrices (core, exit, letter); the locality check that exit and letter changes vanish for `j >= sum_{i<t} sigma_i + k + c` with the smallest `c` that works reported per `t`; a diagnosis printout of the resonant-step artifact (count how many of the high-`j` core changes coincide with a change in `a_+` at a resonant step); the theoretical decorrelation value `2/3` printed next to the measured letter-change probability at t = 16.
- `experiments/syrac_residue_fourier.py` -- supports the new cycles.md Remark 12.6.1.7 and aeh.md 13.6.5 (Tao attribution; read-only, do not edit aeh.md). Merge `fourier3.py`; print the `j - v3(xi)` dependence as a table; keep the real-orbit part.
- `experiments/cycle_offset_identity.py` -- supports cycles.md Remark 12.6.1.7. Merge `cycle_offset.py` and `offset_identity.py`: the exact identity on random profiles, the divisibility biconditional, the three known cycles, the p = 7 staircase, plus (optional, only if a few lines) a consistency check with 12.6.1.4's repetition factor on one repeated profile.

Each script: self-contained (no imports from other repo scripts), deterministic seed, exact integer arithmetic at every pass/fail decision, prints what it verifies and the date, and a committed `experiments/<name>_output.txt` produced from the repo root. Re-run each twice and confirm byte-identical output.

## 3. Deliverable 2: `briefs/fresh-eyes-assessment-findings.md`

The record of the assessment, flat register. Sections: purpose and scope; what was checked (with the script names and their summary lines); the five findings above, each with its numbers; what is NOT claimed (no lever, no sidestep, every front status unchanged, AEH verdict untouched pending `briefs/tao-section5-read-brief.md`); the Tao statements as read, with page numbers; the terminology question the author raised (recorded as pending, not decided). No change-log prose, no session narration.

## 4. Deliverable 3: three calibration remarks and two housekeeping edits

Content edits are conservative: never alter a theorem statement or a proof while adding a remark. One commit per page.

- **stage4.md 11.8.7.7**: append a paragraph headed `**Calibration (delay-line reading; 2026-09-04).**` carrying finding 2: what the consumption identity says about unread digits, the measured first-effect blocks, the never-spent statistic, the carry-propagation reading of regeneration, the resonant-step coordinate artifact, the classical pointer (Terras cylinder count; Lagarias shift conjugacy, citations in publication.md), and the script pointer with the standard verification line (what, range, date). Keep "organizing heuristic, not a formalized theorem" intact.
- **bridge.md 16.2**: one pointer sentence to the calibration at 11.8.7.7 (one-fact-one-page; no restatement).
- **cycles.md**: new `**Remark 12.6.1.7 (the rotation numerator is Tao's n-Syracuse offset; one object, two moduli).**` placed after 12.6.1.6, carrying finding 4 in full: dictionary, exact identity with its two-line derivation, the biconditional, the known-cycle recoveries, the staircase failure, the two-moduli reading with Tao's Prop 1.14/1.17 cited by number and page, the link to 12.6.1.5's margin heuristic, the classical attribution (verified or explicitly unverified), and a `*Calibration.*` paragraph: a naming, not a lever; nothing excluded; front stays parked (12.8.5). Standard `*Verified*` line pointing at `cycle_offset_identity.py` and `syrac_residue_fourier.py`.
- **README.md**: in the paragraph "Where the difficulty actually lives", replace the clause `the "fair-coin" behavior of 2-adic logarithm digits, empirically solid, theoretically untouched by anyone` with calibrated wording consistent with publication.md's AEH verdict (Tao 2019 at logarithmic density and Inselmann 2024 at natural density carry the descent consequence; what remains is the distributional content at natural density past the digit budget, with the logarithmic-density question under review). Keep the rest of the paragraph.
- **HANDOFF.md**: add open work item 4, one paragraph: the assessment exists (pointer to the findings brief and the four scripts), the Section 5 read is pending on its own branch, and the author has raised the terminology-alignment question (decision pending; the main session's recommendation will be recorded when the author decides).
- **index.md**: no edit unless a page's "Current state" paragraph would otherwise be wrong; prefer none.

## 5. Verification before you report

Re-run all four scripts from the branch; committed outputs byte-identical; `python experiments/encoding_scan.py` CLEAN; `git log --oneline main..HEAD` listed in the report.
