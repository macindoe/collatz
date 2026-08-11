# Findings: experiments-12862-repoint — the printed-string `12.8.6.2` repoint (2026-08-12)

Brief: `briefs/experiments-12862-repoint-brief.md`. Branch `experiments-12862-repoint`,
base `e8a0b65` (the briefs commit; the worktree was cut from `d09895c` and rebased
onto `e8a0b65` before any work began). Authority: `briefs/wiki-consolidation-3-audit-findings.md`
§6 and §9 items 1–3. Every site below was located by quoted string against the
current file, not by line number. `python experiments/encoding_scan.py`: **CLEAN**
(0 invalid, 0 BOM, 0 double-encoding), run after all edits and both regenerations,
before the commit. No file outside `experiments/` and this findings file was touched.
All edits via the Edit tool; both output files written by Git Bash redirection /
Python-side writes — no PowerShell `>` anywhere. Both regenerated outputs are
ASCII, CRLF, no BOM, matching their committed predecessors' convention.

## §1 The mapping (the double-citation subtlety)

`cycles.md` §12.8.6 was read in full before any edit. As the section now stands:

- **`12.8.6.2` now names** Theorem 12.8.6.2 (explicit construction; **no correction
  step**) — the greedy-saturation Construction B.
- **`12.8.6.3` now names** "superseded: the profile-plus-correction recipe", and it
  contains **both** old objects: *the profile* (the old `12.8.6.2` — pure geometric,
  partial-sum rounding) and *the correction* (the old `12.8.6.3` — the deterministic
  local search with a move budget). So every old "`12.8.6.2` + `12.8.6.3`" pair
  collapses to the **single number `12.8.6.3`**, with the object named in the sentence;
  a bare number-swap at sites 1–2 and 7 would have produced the nonsense the brief
  warned against, and none was made.
- Old citations of the *correction algorithm* as `12.8.6.3` still resolve (the
  correction lives at `12.8.6.3`); only old-`12.8.6.2` citations mis-resolved.
- `12.8.6` itself is **proved with scope** (its closing Scope paragraph), which is
  site 9's repair.

## §2 The nine sites, before → after (verbatim)

1. `experiments/p22_passer.py` (p=22 certificate 1 banner):
   `"(construction 12.8.6.2 + 13 correction moves of 12.8.6.3;"` →
   `"(superseded recipe of 12.8.6.3: pure-geometric profile + 13 correction moves;"`
2. `experiments/p22_passer.py` (certificate 2 banner):
   `"(construction 12.8.6.2 + 8 correction moves of 12.8.6.3;"` →
   `"(superseded recipe of 12.8.6.3: pure-geometric profile + 8 correction moves;"`
3. `experiments/prime_local_probe.py` (instance-record f-string):
   `"…the staircase recipe (12.8.6.2) always uses K = ceil(n log2 3)…"` →
   `"…the staircase recipe (12.8.6.3) always uses…"` (the referent is the whole
   recipe, which lives entire at `12.8.6.3`; the sentence already names the object).
4. `experiments/staircase_allp_construction.py` (Part 1b):
   `"   unit of exit valuation each climb block spends.  12.8.6.2's PURE"` →
   `"…12.8.6.3's PURE"` (continuation line "geometric profile omits it" names the object).
5. `experiments/staircase_allp_construction.py` (Part 2 header):
   `"PART 2.  Shortfall of the base construction 12.8.6.2 at the SAME n"` →
   `"PART 2.  Shortfall of 12.8.6.3's pure-geometric base profile at the SAME n"`
6. `experiments/staircase_allp_construction.py` (NC-B legend):
   `"     partialsum  : round the partial sums of the PURE geometric  [12.8.6.2]"` →
   `"…[12.8.6.3]"`
7. `experiments/staircase_allp_diophantine.py` (Part 3 header):
   `"  Recipe of 12.8.6.2 + 12.8.6.3, reimplemented independently; candidate"` →
   `"  Superseded profile-plus-correction recipe of 12.8.6.3, reimplemented independently; candidate"`
   (the name is cycles.md's own descriptor for `12.8.6.3`, covering both old objects).
8. `experiments/merle_pincer_check.py` (item-2c report f-string; liveness confirmed
   by the main session's trace of `print(item2c_correction_runs())`):
   `"…per run, crash_depth=1, base construction 12.8.6.2."` →
   `"…per run, crash_depth=1, base construction = 12.8.6.3's pure-geometric base profile."`
   The same string's opening `"Correction runs (algorithm 12.8.6.3 via Section 1's
   instrumented copy)"` was left unchanged: the correction algorithm lives at
   `12.8.6.3`, so that half resolves correctly as written.
9. `experiments/staircase_allp_diophantine.py:5–6` (docstring, comment-only):
   `"# Supports: …, and the sole / # remaining gap of the floor-grade result at cycles.md 12.8.6."` →
   `"# Supports: …, and the / # availability theorem (12.8.6.1) of the proved result at cycles.md 12.8.6."`

**One consequential comment edit beyond the nine** (recorded, not silent):
the Part-2 banner comment in `staircase_allp_construction.py` read "…Wherever the
printed text of this Part cites 12.8.6.2, the object meant is that pure-geometric
profile, i.e. 12.8.6.3.  The printed strings are left as they stand so the
committed output stays byte-exact." Those two sentences described the
pre-decision state and become false in this very commit (the strings are
repointed and the output regenerated), so they were dropped; the banner's first
sentence (naming the object and `12.8.6.3`) stands. Also verified still-resolving
and untouched: the printed `"12.8.6.3's move count"` line (Part 2 close) — the
move count belongs to the correction algorithm, which is at `12.8.6.3`.

## §3 Output regeneration 1: `staircase_allp_construction_output.txt`

Full rerun, `python experiments/staircase_allp_construction.py` (Git Bash `>`
into the committed path). **Wall clock 404.0 s** (committed predecessor: 407.6 s);
**total failed checks: 0**. Diff against the committed predecessor — exactly:

- lines 73 / 92 / 242: the three repointed strings (sites 4, 5, 6);
- lines 359–360 (Part 4, p = 31 and 32): the final wall-clock column only
  (32.0→31.7 s, 95.4→95.9 s), every other field byte-identical;
- line 366: `wall clock: 407.6 s` → `404.0 s`.

Nothing else moved: every check count, every table row, every 0-failures line
byte-identical. No STOP condition arose.

## §4 Output regeneration 2: `staircase_allp_diophantine_part3.out`

**Ground fact the regeneration had to respect:** the committed `_part3.out` is a
*hand-assembled record*, not raw script output — its own line 10 says "Assembled
from the slices listed in staircase_allp_diophantine_note.txt", and the script
provably cannot print its lines 10–15 (the assembly paragraph), the dash-redacted
p=22 row, the literal `P36ROW` placeholder at line 35, or the closing paragraphs
(lines 37–45) — none of those strings occur in `part3()`. So "regenerate per its
documented invocation" here means: re-run the note's documented segment-3 slices,
verify the rows, and re-assemble on the committed predecessor's bytes.

All documented slices were re-run at their documented budgets (`part3(pmin, pmax,
40, budget)` via module import; `mp.dps = 800` is module-level, so precision is
identical to `main()`'s). p = 36 was **not** run — the note records it as
"started, NOT completed — recorded as not run", and that is the committed state.
Measured slice wall-clocks (quiet-machine values):

- p = 18..21 @ 240 s/pass: 90.2 s (solo rerun; an earlier pass gave 94.9–98.0 s)
- p = 22 @ 30 s/pass: 32.0–33.7 s
- p = 24..28 @ 240 s/pass: 550.5 s (single invocation, the note's exact slicing;
  a split rerun 24..26 / 27..28 gave 332.3 s + 221.4 s and identical rows)
- p = 29..32 @ 60 s/pass: 364.3–366.0 s
- p = 33..34 @ 60 s/pass: 354.9–375.7 s
- p = 35 @ 60 s/pass: 1020.4–1025.6 s (committed row's own sec: 1039.4)

Total ≈ 41 minutes per full pass over the slices.

**Row verification: every period p ∈ {18,…,21, 24,…,35} reproduced its committed
row byte-identically in every field except the wall-clock `sec` column —
including all six budget-capped rows (29–35: same n, gamma, moves, cap flag).**
The committed p=22 row is hand-redacted (dashes in n/gamma/moves/sec); the fresh
run at the documented 30 s budget produced the full row `n=63069  2.508  15.067
3.379  1  9  PASS  False  yes` — and its `gam/log2p = 3.379` equals the one
numeric field the committed redacted row retains. No STOP condition arose.

**Assembly of the replacement file** (Python-side write, CRLF, ASCII): the
committed predecessor's bytes, with exactly (a) line 4 replaced by site 7's
repointed string as actually printed by the fresh runs, and (b) the nine
`cap=no` rows (18–21, 24–28) spliced from single-writer fresh runs, changing
their `sec` cells only. Kept byte-identical as committed: the hand prose, the
table header, the hand-redacted p=22 row, the six budget-capped rows 29–35
(their fresh reproductions are recorded above; their committed `sec` values are
the July record and were not spliced), the `P36ROW` placeholder, and the closing
paragraphs. The final diff against the predecessor is therefore: line 4 + nine
`sec` cells. `P36ROW` is noted as a defect of the *committed predecessor* (a
placeholder the July assembly never resolved); it was left as committed — not
this brief's to repair.

## §5 Sites with no committed output (render checks)

- Sites 1–2: `python experiments/p22_passer.py` run in full — both repointed
  banners printed, and the run **PASSes** end-to-end (p=7 anchor gamma 6.7438
  MATCH; both p=22 certificates 22/22 rotations, gammas 11.1861 / 14.7462,
  divisibility fails as expected).
- Site 3: `prime_local_probe.py` is long-running; per the audit's "visual check
  only", the edited print statement (its exact source lines) was executed in a
  harness with representative values — renders as "…the staircase recipe
  (12.8.6.3) always uses K = ceil(n log2 3)…".
- Site 8: `item2c_correction_runs(deadline_s=2.0)` called live — the repointed
  header rendered verbatim. (At that deliberately trivial 2 s budget all three
  runs report NOT resolved; the function's own docstring records that the
  resolved/not-resolved outcome at a given wall-clock budget is machine-speed
  dependent. This was a render check, not a measurement; no output is committed
  for this script.)
- Site 9 is comment-only; `python -m py_compile` passed on all five edited scripts.

## §6 Incident record: the duplicated Part-3 run

The first Part-3 slice driver, launched in the background, was interrupted with
a session stop and silently resumed later, running concurrently with the
foreground re-runs of the same slices and writing the same scratch filenames.
Because `part3` is deterministic, the two writers produced identical bytes in
every field except `sec`, and the fixed-width row format kept the raced files
well-formed; both writers' complete logs agree. For the committed assembly no
raced file was used: rows 18–21 come from a solo rerun on a quiet machine, and
rows 24–28 from the driver's own solo `24..28` invocation (the note's exact
slicing). The concurrent pair also served as an unplanned cross-check: two
independent full passes over p = 18..35 reproduced every committed row mod `sec`.

## §7 Verdicts

- `python experiments/encoding_scan.py`: **CLEAN** (run before the commit, after
  all edits, both regenerations, and this file).
- Diff rule: satisfied for both outputs; **nothing moved beyond the repointed
  strings and wall-clock cells; no STOP was triggered.**
- The audit's §9 item 2 discrepancy (`_note.txt` vs `_part3.out`) is confirmed
  from the tree: the stale string printed into `staircase_allp_diophantine_part3.out:4`;
  `_note.txt` contains no citation and was not touched.
