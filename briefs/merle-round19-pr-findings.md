# Findings: round 19 to Merle, prepared as a pull request: the joint note's dichotomy credit corrected and L-A12 offered, committed locally and not pushed

Brief: `briefs/merle-round19-pr-brief.md`.

**Wiki branch and base.** The branch is `merle-round19-pr`, with base `85f42d385bdb98b008b06cb92e7b4e1db4e1adaf`, the brief's own commit on `main`. The worktree was cut at `946e0d8`, and `git merge --ff-only 85f42d3` was a clean fast-forward. Nothing outward was done: no push, no PR, no comment and no email. This session used read-only `gh` (`pr list`, and `pr view` on our own PRs #1 and #2 for their body format), a fresh clone into the scratchpad, and `git ls-remote`.

**Shared-repo base.** The fresh clone of `github.com/macindoe/one-obstruction-three-faces` was taken on 2026-10-19. `origin/main` is **`474125de06e10d8fd32126eed4e6f5466cca9e36`**, the PR #7 merge, which matches HANDOFF. `origin/round-18` is at `031c454`, with PR #8 open; this round does not build on it. The local branch `round-19` starts from `474125d` and has three commits, head **`49b2f387cf63ec9da40c4264db0010ddf6b70c7b`**:

| # | commit | file | change |
|---|---|---|---|
| 1 | `6740c90` | `NOTE-v1.md` | `+13/−3`: the credit correction |
| 2 | `2e14315` | `LEDGER.md` | `+28/−0`: L-A12, a pure addition after L-A11 |
| 3 | `49b2f38` | `rounds/R19-macindoe.md` | new file, the letter |

These are the brief's deliverables:
- **The patch series:** `briefs/merle-round19-pr-patches/0001…0003-*.patch`, made with `git format-patch origin/main..round-19`. The series was checked by `git am` onto a fresh branch at `origin/main`, and the resulting tree is identical to `round-19`. The clone was set to `core.autocrlf=false` and re-checked out, so the blobs are LF exactly as committed upstream. Each file was checked for UTF-8 with no BOM and no CR.
- **The PR title and body:** `briefs/merle-round19-pr-body.md`, UTF-8 with no BOM. Its first line is the title. The body is everything after the `---` line.
- **The ledger entry number:** **L-A12**. The ledger on `main` runs L1–L4 and L-A1–L-A11. **There is no collision with PR #8's branch.** `git grep "L-A12\|R19" origin/round-18` returns nothing, and PR #8 adds no entry, only a reading note at the ledger head and one line under L-A10's `Key status`. `git merge-tree --write-tree origin/round-18 round-19` merges clean. The letter is numbered R19 because `rounds/` on `main` runs to R17 and PR #8 carries `R18-merle.md`.
- **The commit author:** `Ben Macindoe <macindoebenjamin@gmail.com>`, the public address used by our August commits in that repo. It is set in the clone's local config only.

## 1. Every changed line in the shared repo, with its source

### 1.1 `NOTE-v1.md` (commit 1)

| line (new file) | change | source |
|---|---|---|
| 17 | "The dichotomy is Macindoe's, published in [1]." → "The dichotomy is stated in [1], but it is not Macindoe's as a whole: its upper half is classical, its lower half was anticipated in part, and the credit for each is given under each half below." The label sentence after it is unchanged. | Brief item 1. `briefs/ceiling-novelty-refresh-findings.md` §0, §5.2. `briefs/ceiling-ccchallenge-sweep-findings.md` §0, §6. |
| 19 | One sentence inserted into **Upper half**: Rozier [5] (Théorème p. 8; Lemme 4 p. 11, same exponent `(log₂3 − 1)/((log₂3)^p − 1)`), made explicit by Simons–de Weger [6] (Lemma 7, Lemma 14, Theorem 3(d)), their `m` = [1]'s `p` exactly, finiteness for each `m` also Brox [7]; [1]'s Thm 4.5 "a rederivation by another route (rotation numerators and a max-plus recursion)". | Rozier: CS §0, §3, §3.1 (held, read from the page images). SdW: NR §3, §4.1 (held). Brox: NR §3, **cited, not held** (403; SdW p. 54 and Lagarias II). `m = p`: NR §4.3 and `cycles.md` 12.4, re-checked in `briefs/cycles-12-4-recheck-findings.md` (47,498 checks). The "another route" wording is NR §4.1 and §5.1. |
| 21 | Two sentences appended to **Lower half**: Rozier [5, p. 11] observes, by a minimax over positive real run-length tuples, that his bound is optimal given his per-minimum inequalities; SdW [6, p. 69] expected the exponential dependence on `m` unavoidable; HH [8] proved the analogue in the cycle-length parameter (Lemma 5, p. 230). "What is [1]'s is the realization in integers, in the block parameter: configurations meeting every rotation's exact size condition at bounded slack `γ`, at every period." | CS §0, §3.2 (Rozier p. 11). NR §3 and §4.2 (SdW p. 69; HH Lemma 5 p. 230 and §4.4 p. 236). CS §3.2 gives the residue ("integer, all-rotations, bounded-slack"). The brief's item 1 wording is followed. |
| 29 (new paragraph) | "The sentence is [1]'s; its moral is older." HH [8, p. 238], "*cannot* be successful" and "would hence involve number theoretical arguments", reducing what remains to the divisibility condition at every rotation; SdW [6, p. 69] expected the same in `m`; "[1]'s theorem carries the moral into the block parameter `p` (= `m`)." | NR §3, HH row (p. 238, quoted as held). NR §4.2 item 2. The brief's item 1 says the obstruction "stands as a statement but must carry the HH 1997 / SdW 2005 credit". The quotation itself (line 27) is untouched. |
| 65–71 | References [5] Rozier 1991, [6] SdW 2005 (DOI 10.4064/aa117-1-3), [7] Brox 2000, [8] HH 1997 (DOI 10.4064/aa-78-3-227-239). | NR §3 for SdW, HH and Brox, with titles and DOIs as recorded there. CS §3 for Rozier. Brox's DOI is not given, because it was not verified. |

Not changed: the 12.8.7 threshold result is **not** put into the note. PROTOCOL §5 keeps one-key claims out of the note's text, and the brief asks for a credit-only edit.

### 1.2 `LEDGER.md` (commit 2): L-A12, every line new

| block | source |
|---|---|
| Title and seeding line ("one key (ours), yours invited") | Brief item 2. L-A10 is the format precedent for seeding. |
| Notation and dictionary (`m = p`, `K_SdW = n`, `a_i = R_r/q`, `x_r = 2^{m_r}R_r/q − 1`, (S) and (X)) | `cycles.md` 12.8.7, "The threshold, as posed". `briefs/staircase-x0-threshold-findings.md` §1.1–1.2. |
| Claim 1 (sandwich; `γ > max(ε_p n, log₂(X₀+1)) − log₂ p`; maximum not sum) | `cycles.md` Prop 12.8.7.1. X0 findings §2 item 1, §3. |
| Claim 2 (deep crash; `γ ≤ max(log₂(X₀+1), 2.71) + 2`; `2.7095 ≤ γ − ε_p n ≤ 4.2096`; scale `ε_p n ≥ log₂(X₀+1) − 2.21`; `Λ ≥ 0.0541·2^{−ε_p n}`) | Thm 12.8.7.2 and 12.8.7.4. X0 findings §5.1, §7.2, §9. `λ = 2.7095122` and `λ + 1.5 = 4.2095122` are rounded outward. |
| Claim 3 (`p₁` table: 10, 22, 98, 110, 309; `[2.92, 10.42]`) | 12.8.7, after the proof. X0 findings §5.3. |
| Claim 4 (unit-block bound; threshold `(L−1)ε_p n > 4.80 + log₂ p`, i.e. `λ + 2.09`; from `X₀ = 2^20`) | Prop 12.8.7.1(iii), Remark 12.8.7.5. X0 findings §6. |
| Grade (size-only; `q ∣ R_r` never evaluated; no exclusion; not formalised; three-distance theorem cited, checked `k ≤ 13`) | 12.8.7 current state and proof. X0 findings §2 closing paragraph, §11. |
| Relation to Rozier and SdW (minimax value attained, not Lemme 4's inequality; `m c_m ≥ 0.0541`; "given `m` and `K`" decided within `(−log₂ p, 2.7096]`) | Remark 12.8.7.6. X0 findings §7.1, §7.2. The SdW p. 69 sentence is quoted as held in NR §3 and X0 findings §1.3. |
| Left open (the `log₂ p` gap; no uniform `p₁`; nothing below `p₁`; no necessary threshold) | X0 findings §7.2, §11. 12.8.7 after the proof. |
| Regime (proof for all `X₀ ≥ 1`, `p ≥ p₁`; exact check at 6 `X₀`, 95 points, `p ≤ 32`, `n ≤ 4,412,888`; measured `[2.7532, 3.8267]`; second regime: 30,000 random configurations and the stronger condition `X₀ q ≤ R_r`; sandwich ends approached to `10⁻⁶` and `0.0014` bits) | X0 findings §3, §4.4, §8 parts C and F. The regime column itself is PROTOCOL.md §3. |
| Artifacts: `macindoe/collatz` at `85f42d3`, `experiments/staircase_x0_threshold.py` and its output, 188 checks, 0 failures, re-run byte-identical | X0 findings §8. **Re-run this session** with the documented command (3 min 10 s): `CHECKS: 188 FAILURES: 0`, identical to the committed output modulo line endings. |
| Key status: one key (Macindoe) | Brief item 2. |

### 1.3 `rounds/R19-macindoe.md` (commit 3): every line new

The register follows `rounds/R12-macindoe.md`: numbered sections, business only, no personal paragraph and no tooling.

| section | content | source |
|---|---|---|
| header | One round per PR, second key = approving review (R11 §13); based on `474125d`; no line PR #8 touches; personal half by mail. | HANDOFF item 1, standing conventions. The trial merge in §0. |
| §1 | The error is ours: we held the pen on NOTE-v1 (PR #2), and [1]'s abstract calls the dichotomy its "main new theorem". The two literature checks of 2026-10-18 give sources and pages. Rozier's Théorème is quoted in French (p. 8). Lemme 4 (p. 11). SdW Lemma 7 (p. 58), Lemma 14 (p. 61), Thm 3(d) (pp. 55–56), `15.107…`. Brox is marked not held. `m = p`, with our own 12.4 error self-reported. Rozier's p. 11 remark is quoted in French. SdW p. 69 is quoted. HH Lemma 5 (p. 230), §4.4 (p. 236) and p. 238 are quoted. Then what is [1]'s, the obstruction paragraph, the patch, and the grep result. "Our side found the error, not you." | NR §3, §4.1–4.3. CS §0, §3, §3.1–3.2. `cycles.md` 12.4. `paper/collatz-reduced-v3.tex` L38 (abstract). The shared repo's `git log` on `NOTE-v1.md` (both commits ours, `96ccadf`, `93c6ac4`; `git blame` lines 15–30 all `96ccadf`). |
| §2 | L-A12 in prose. What it settles of SdW p. 69, and what it leaves open. Its relation to Rozier. Its placement beside L-A8 and L-A9 is left to him. | As in §1.2. |
| §3 | Paper 1 v4 is announced and not minted, with no DOI, and carries the same credit chain (Thm 4.5 header attribution; "main new theorem" dropped; sharpness with proof and credit; threshold form included). The theorem numbers the note cites are kept. [1] stays v3 until minting, and the reference update comes as its own round. | `briefs/paper1-v4-draft-brief.md` D1, D2, D3, D4, D15. `briefs/paper1-v4-items-findings.md` rows 1.1, 1.17, 1.18. |
| §4 | Where everything lives, at `85f42d3`. | The files exist at `85f42d3`: checked by the fast-forward stat. |

## 2. What the main session must check before pushing

1. **The wiki pin `85f42d3` is not public yet.** `git ls-remote origin main` on `macindoe/collatz` returns `946e0d8` (2026-10-19). `85f42d3`, which holds `cycles.md` §12.8.7, the script and the findings files, is unreachable on GitHub. L-A12's artifact link and the letter's §4 cite it. **Push the wiki's `main`, or at least a commit containing `85f42d3`, before pushing `round-19`,** and then confirm that `https://github.com/macindoe/collatz/blob/85f42d3/cycles.md` resolves. To pin a later commit instead, edit the two occurrences: `LEDGER.md` L-A12 "Artifacts" and `R19-macindoe.md` §4.
2. **The shared repo's `main` has not moved.** The base is `474125d`. If Merle merges PR #8 first, `round-19` still applies: `merge-tree` against `round-18` is clean. Rebase onto the new `main` and re-run `git am` or `merge-tree`.
3. **No line of NOTE-v1 has moved upstream** since `93c6ac4`.
4. **The commit trailers.** The three local commits carry **no** `Co-Authored-By` trailer. That follows our own last commits in this repo (the August ones carry none) and the instruction never to mention tooling there. The delegation message asked for the trailer on commit messages. If the main session wants it on the shared-repo commits, amend before pushing. The wiki commit on this branch carries it.
5. **The PR body carries no "Generated with" footer**, for the same reason. Neither does our PR #1 or #2. Add it only if the author wants it.
6. **Encoding.** `experiments/encoding_scan.py` was run on the wiki branch before the final commit, and its result is in the commit message. The three shared-repo files are UTF-8 with no BOM and no CR, and so is the body file.
7. **Applying the patches.** This machine checks out with `core.autocrlf=true`, so the working-copy patch files may be CRLF. Apply them from the committed blobs, which are LF: for example, `git show <wiki-commit>:briefs/merle-round19-pr-patches/0001-….patch > /tmp/0001.patch`, and so on. Run `git am` in a clone set to `core.autocrlf=false`, then check that the tree equals `round-19` at `49b2f38`. The clone `scratchpad/r19-shared` already holds `round-19` and can be pushed from directly if the main session uses this session's scratchpad.
8. **Upstream state of PR #8.** The letter says only that PR #8 is open and untouched by this round. It does not mention our approving review of 2026-10-17. If PR #8 is merged by push time, the header sentence "touches no line that PR #8 touches" stays true.

## 3. For the author to decide

1. **The NOTE-v1 wording.**
   - The credit sentence now reads "stated in [1], but … not Macindoe's as a whole". A shorter alternative is "The dichotomy is stated in [1]; credit for each half is given below."
   - Whether the note should also name Rozier's remark among the obstruction's antecedents. It is not added: the sweep judged that the remark "points at" divisibility without naming it (CS §3.2 item 4).
2. **Whether to send L-A12 now or hold it.** It is a strengthening, not a correction. The brief asks for it in this round.
3. **The theorem numbers in v4.** The letter's §3 says "the theorem numbers the note cites are kept". D1 fixes Thm 4.5 and D15 relies on Thm 4.6 staying valid. If the v4 draft renumbers Theorem 4.6, that sentence must change before sending.
4. **The mail.** The personal paragraph and the reply mail with the author's own note attached are the author's (the brief, "Why").
5. **NOTE.md and README** are left untouched. NOTE.md §1 already lists HH 1997 and SdW 2005 in its provenance line. NOTE.md §2's "The staircase family (Macindoe side)" is a side label for who brings the item, not a priority claim, and the integer construction is ours. If the author prefers, Rozier 1991 could be added to NOTE.md §1's list in a later round.
6. **Brox 2000** is cited but was not read at source (the publisher returned 403). The note and letter cite it only for "finiteness for each `m`", as SdW p. 54 characterizes it, and the letter says it was not held.

## 4. Record

- One numerical re-run: `python experiments/staircase_x0_threshold.py`, 188 checks, 0 failures, identical to the committed output modulo line endings (2026-10-19). No new computation was needed. Everything else is a reading of findings already merged.
- Scratch, not committed: the clone `scratchpad/r19-shared` (branch `round-19` at `49b2f38`), the three commit-message files, and the re-run output.
