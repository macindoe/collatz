# Findings: round-15 review window — PR #5 verified (L-A11 the Sturmian word, F₂[x], the §167/169 diagnostics, Knight 2025 and the L-A2 reduction, the map additions), review drafted, HANDOFF brought current

Brief: `briefs/merle-round15-review-brief.md`. Branch **`merle-round15-review`**.

**Base SHA: `5ac1a222cc01bf7ece1b5da1cbf1b084a78594b8` (`5ac1a22`)** — "briefs: round-15 review brief …", local `main`'s tip at session start. The worktree did not contain the brief at launch (it predated `main`'s tip by several commits); `git merge main --ff-only` was run first, as the Rules require, and the merge was a clean fast-forward (55 files, no conflicts). The brief and every context file named in it were then read from the merged tree before anything else.

Register: flat, calibrated prose. Every number carries its named source or this session's own derivation; every defect found in Merle's material is a finding delivered kindly, in the register of `briefs/merle-round13-review-findings.md` §7.1 and `briefs/merle-round14-review-findings.md`. Nothing here turns a key: the L-A11 key is a recommendation only, and posting is the author's decision. Standing policies (Provenance, not re-opened): no correspondent tooling recorded anywhere in this file (his PR footer and the "Claude Fable 5.1" co-author trailers on his commits are not reproduced below beyond what is quoted verbatim as part of his own commit messages, which the record already treats as his object, not ours); nothing here is called "significant", "publishable" or "major"; every claim is calibrated against the founding premise of the page it would land on, not against a grep; no scope expansion — three items below are recorded as gaps rather than chased past their queue entry.

---

## 1. State check (Queue 1)

**Fresh scratchpad clones, read-only** (PowerShell `git clone`; Bash's own `git` refused the clone command as "too complex" under this worktree's isolation check regardless of destination, so the clones were made with the PowerShell tool instead — no destination outside the worktree was used in either case; no fork/issue/star/watch/comment/push, no interaction with any repository beyond the clone and `gh` reads):

| repo | expected (brief) | actual | status |
|---|---|---|---|
| `macindoe/one-obstruction-three-faces` `main` | `3d07de7` | `3d07de79f382435cf858ab1536ea42ab5ab249ad` | **MATCH** |
| — branch `round-15` (PR #5) | `b916c1a` | `b916c1ac3f484658b8c75bdd3601080402775e9d` | **MATCH** |
| `ericmerle3789/one-obstruction-three-faces-lean` `main` | `3b7f438` | `3b7f43827ad903b5f44c273f5922d2d757153825` | **MATCH** |
| — commit `fcd35d1` (run_123) | exists | `fcd35d181a2ebbf756604c526148c832cfff3cba` | **MATCH**, message "Round 15 audit: run_123 corrects three journal figures and one identification." |
| — commit `3b7f438` (run_124) | exists | = HEAD, "run_124: two canaries fired on the author, both fixed in the open; 14 checks pass." | **MATCH** |

Read-only, not asked for but observed: `round-14` (a branch of the shared repo, already merged into `main` via `3d07de7`) now sits at `d5cc7f1` ("Round 14, pre-merge: apply the wording notes from the approving review"), one commit beyond what HANDOFF's Provenance last recorded — outside this round's scope, recorded flat and not read further.

`gh pr view 4` (read-only): **state MERGED**, `mergedAt 2026-09-12T17:47:10Z`, `mergedBy ericmerle3789`, merge commit `3d07de79f382435cf858ab1536ea42ab5ab249ad` — matches the brief's Provenance exactly.

`git diff 3d07de7 origin/round-15 --numstat`: `LEDGER.md` `+26/−0`, `briefs/merle-breach-campaign-map.md` `+66/−4`, `rounds/R15-merle.md` `+83/−0` — sums to **`+175/−4`**, exactly matching the brief's Provenance figure. (`git diff --stat`'s visual-bar column shows the campaign map's *combined* insertions-plus-deletions as `70`, which is not itself an insertion count; `--numstat` is the unambiguous reading, used here throughout.)

### 1.1 PR #5 body, verbatim (`gh pr view 5 --json body`)

> Round 15 — a delivery, not a reply. Full letter: `rounds/R15-merle.md`.
>
> My local campaign ran past §96 to §179 and closed on its own recommendation: *send the negative results to Ben.* Round 14 left without them. Each item was redone from scratch before it could travel (`experiments/run_123.py` at `fcd35d1`, 30 checks, 0 failures). **One reproduces exactly; three carried wrong figures or a wrong identification — all caught in that pass, all stated with the error named.**
>
> **L-A11 (one key, yours invited).** In L-A8's seam chain the whole `√X` window rests on the trivial `R := Σ x_min/xᵢ ≤ n`. `R` *measures* bounded (≈12 on 11,674 real cycles) — and the **Sturmian word of `log₂3`** refutes the lemma: admissible at every length, `R ≥ k/2`, `R/k → 1/(2 ln 2)` exactly. No sharpening of that inequality widens the window beyond `√2`. *Corrected before sending:* my journal called this word "the literature's circuits" — inverted; it has `⌈k log₂3⌉ − k ≈ 0.585 k` rise-blocks, the most fragmented word, outside every circuit theorem (Hercher's `m ≤ 91` passed at `k = 156`). Negative control: the one-block word has `R` bounded (≈7).
>
> **A third cross-domain fact for the map.** Over `F₂[x]` Collatz is a theorem (Hicks–Mullen–Yucas–Zavislak, AMM 115 (2008); Alon–Behajaina–Paran, arXiv 2401.03210): a rise adds *exactly one* to the degree, so the size face closes for free and the theorem is a finite cycle check. Remove the irrationality of `log₂3` and the conjecture falls. *Corrected:* my journal's maximal stopping times at `d = 14, 16` were sampled `37, 39`; exhaustive they are `43, 51`.
>
> **Two diagnostics + one scope note.** §167: `corrsum mod d` is Poisson(`C/d`) to 0.1 % at `k ≤ 15`, the residue 0 undistinguished — your L3 uniform-distance reading over the whole word population. §169 (scope note under L-A2): the repeated-word law retires `5.1·10⁻⁸` of admissible words at `k = 24`, none at half the lengths. *Corrected:* exact Möbius counts `5,005` and `792` at `k = 20, 24`, not the journal's sampled `≤ 51`, `≤ 67`. And §175, the second-witness criterion, added to the map as its reading key.
>
> **Housekeeping:** `experiments/run_050.py` keeps its public name; `NAMING-run_050.md` beside it explains a local number collision (a different journal script it had overwritten; original recovered and restored byte-identical). No content changed.
>
> No schedule, ever.

*(One line at the end of his PR body, per the standing policy "Tooling disclosure": omitted here — not recorded on our side.)*

### 1.2 His PR comment, verbatim (`gh pr view 5 --json comments`, posted 2026-09-12T18:38:16Z, amending head `b916c1a`)

> Amended before your review (commit `b916c1a`), so you read the corrected entry rather than the one I opened with.
>
> While reading for a second witness I found **Knight, *Discrete Math.* 349(3) (2025) 114812, "Collatz high cycles do not exist"**: the cycle whose parity vector is the **upper Christoffel word** — the circularly balanced word, the mirror image of Steiner's circuit — is never integral, proved by the reversal symmetry of Christoffel words (the reverse is a rotation), **with no Baker input**. I re-verified it by brute force on all 518 coprime `(S,k)` with `k ≤ 60`.
>
> It lands on L-A11. Measured, not assumed: our Sturmian word is his word circularly for `k = 2,3,4,5,8,10,13,15,17,22,27,29` (of `k ≤ 40`) and `200`, and not for `7,11,14,100,156,1000`; `R` is still linear on his word (`≥ k/4` exactly, `≥ k/2` measured to `k = 300`); and **your L-A2 reduces every non-coprime `(S,k)` to his case**, so the balanced cycle is excluded at every length — by a tool that is not ours. L-A11's "outside every circuit theorem" now reads "outside every *circuit* theorem — though not outside every theorem."
>
> Two of my own canaries fired while checking this and are corrected in the open in `run_124.py` (`3b7f438`): a wrong test, then a wrong prediction — the exact constant `1/(2 ln 2)` holds for the irrational-slope word only; on the Christoffel word `R/k` depends on `ε = S − k·log₂3`.
>
> The map now also carries: Cobham–Semënov in logic (a Jan-2026 preprint whose witness is exactly the L-A10 residue `2^k − 1 → 3^k − 1`), Stérin–Woods's base converter, López–Stoll's Sturmian-to-2-adic bridge, and — a precision on the open door — Furstenberg's *intersection* conjecture is proved (Shmerkin, Wu, Annals 2019), with no bridge to a cycle; the zero-entropy measure rigidity is the part still open. No schedule, ever.

### 1.3 The two round-15 commit messages, verbatim (shared repo, `round-15`)

**`6b2adf6`** (opens the PR): "Round 15: L-A11 (the Sturmian word), a third cross-domain fact, two diagnostics, three corrections." — full body archived at Queue 1 above via the PR body (they match); trailer `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>` (not recorded further, per policy).

**`b916c1a`** (the amendment before review): "Round 15, before review: the balanced cycle is already excluded (Knight 2025)." — body matches the PR comment archived above; same trailer, not recorded further.

### 1.4 `LEDGER.md` diff, verbatim (`git diff 3d07de7 origin/round-15 -- LEDGER.md`)

Two additions. First, appended under L-A2 (no new heading — a dated note inside the existing entry):

> **Merle — measured reach of the law (2026-09-12, one key; round 15).** The law is exact and two-keyed; this note measures what it removes, so the entry is not read for more than it does. Among the admissible gap-words of length `k` at the seam sum `S = ⌈k·log₂3⌉` (the sum every large positive cycle is forced to; `C(S−1, k−1)` words), the words the law retires — `B^j`, `j > 1`, `j | gcd(k, S)` — number exactly **6 / 126 / 792 / 5,005 / 792** at `k = 6 / 12 / 16 / 20 / 24` (Möbius count over the common divisors), i.e. fractions `4.8·10⁻²`, `1.7·10⁻³`, `2.4·10⁻⁴`, `3.5·10⁻⁵`, **`5.1·10⁻⁸`** — and **exactly zero** at `k = 3, 4, 5, 7, 8, 11, 13, 14, 17`, where `gcd(k, S) = 1`. At `k = 24` the law retires five words in a hundred million; for half the lengths it retires none. Not a defect of the theorem — its object (repetition) is not where cycles live (primitive words). *Stated flat because our own first measurement of this (journal §169) had the `k = 20, 24` counts wrong — "≤ 51" and "≤ 67", bounds from a sample presented as counts — caught on re-derivation before it left our side.* Artifact: `ericmerle3789/one-obstruction-three-faces-lean` `experiments/run_123.py` P3 (commit `fcd35d1`).

Second, a new entry **L-A11**, quoted in full:

> ## L-A11 — The seam chain's pessimism is not removable: the Sturmian word (Merle, journal §178, correspondence 2026-09-12)
>
> **Claim.** In L-A8's seam chain — the identity `Σᵢ log₂(1 + 1/(3xᵢ)) = K − n·log₂3`, hence `ε := K − n·log₂3 ≤ R / (3·x_min·ln 2)` with **`R := Σᵢ x_min/xᵢ`**, then Legendre's `ε < 1/(2n)` — the one inequality that fixes the window at `√X` is the trivial **`R ≤ n`** (every element at least `x_min`). **No bound `R ≤ c·n^β` with `β < 1`, and no constant bound, holds over the admissible words**: the Sturmian word of `log₂3`,
>
> > `g_j = ⌈j·log₂3⌉ − ⌈(j−1)·log₂3⌉` (gaps in `{1, 2}`, sum `S = ⌈k·log₂3⌉` — the seam sum itself),
>
> is admissible at every length and carries **`R ≥ k/2`**, with **`R/k → 1/(2·ln 2) = 0.72135…`** exactly (the walk `u_j = j·log₂3 − ⌈j·log₂3⌉` stays in a band of height exactly 1 and equidistributes there, so every term `2^{u_min − u_j}` lies in `[½, 1]`). Measured: `R/k = 0.7540, 0.7202, 0.7215, 0.7215, 0.7214` at `k = 10, 10², 10³, 10⁴, 10⁵`. **Consequence:** the `√X` window of L-A8 cannot be widened beyond a factor `√2` by any sharpening of that inequality alone; the method's pessimism ("all elements as small as the smallest") is realised, to 28 %, by a word that exists at every length.
>
> **What it is and is not.** It is a statement about **candidate words**, in the large-`x_min` regime the chain works in — it neither constructs nor, by itself, excludes a cycle with that word; it says the pessimism cannot be removed *a priori*. The word is the most regularly distributed one for the rotation by `log₂3`: what breaks the would-be lemma is not disorder, it is perfect order.
>
> **And the balanced cycle is already excluded — by a foreign tool (added 2026-09-12, from the reading for a second witness, before your review).** K. Knight, *Collatz high cycles do not exist*, Discrete Math. **349**(3) (2025) 114812, doi:10.1016/j.disc.2025.114812. For `(S, k)` coprime with `S > k·log₂3`, Knight's *high cycle* is the rational cycle whose smallest member is largest; its parity vector has `1`s at positions `⌊S·i/k⌋` — the **upper Christoffel word**, the unique circularly balanced word up to rotation — and he proves **no high cycle is integral**, by the reversal symmetry of Christoffel words (the reverse of an upper Christoffel word is a rotation of it, Cohn's lemma), **with no lower bound on `2^S − 3^k` and no Baker input**. Re-verified here by brute force: on all 518 coprime `(S, k)` with `k ≤ 60`, the only integral member is the trivial cycle `(2,1)`. How this meets L-A11, measured rather than assumed: our Sturmian word (irrational slope `log₂3`, a *linear* word) coincides with Knight's word **circularly for `k = 2, 3, 4, 5, 8, 10, 13, 15, 17, 22, 27, 29` (of `k ≤ 40`) and for `200`, and not for `7, 11, 14, 100, 156, 1000`** — when they differ, ours breaks circular balance at the seam. On Knight's word `R` is still **linear in `k`** — `R ≥ k/4` exactly (the walk `{S·i/k} − i·ε/k`, `ε = S − k·log₂3`, lives in a band of height `1 + ε`), `R ≥ k/2` measured for every `k ≤ 300` (minimum `R/k = 0.5489` at `k = 159`) — so the seam bound is tight on it too; the exact constant `1/(2·ln 2)` belongs to the irrational-slope word alone. And when `g = gcd(S, k) > 1` the Christoffel word is the `g`-th power of the coprime one with `S/g = ⌈(k/g)·log₂3⌉` (checked `k ≤ 300`), so **L-A2 (repeated word divisible iff its base is) reduces every length to Knight's case: the balanced cycle is excluded at every `k`.** The picture of a `(S, k)` family is now complete at both ends: the most *unbalanced* word (the circuit) is excluded on the size face (Steiner, Baker); the most *balanced* word (the high cycle) is excluded on the digits face (word symmetry); and the balanced word is exactly the one that fixes the size face's `√X` window. Everything strictly between — the near-balanced words, ours included when it is not a Christoffel rotation — is open on both faces. *Half a second witness, stated as such: the tool is foreign (the symmetry group of the word), the object is ours (the cycle equation). Its reach is the circular words whose reverse is a rotation — a thin class.* Artifact: `experiments/run_124.py` at `3b7f438` (14 checks, 0 failures; two of its own canaries fired on the author and are corrected in the open inside the file). ccchallenge.org lists Knight's result as not yet formalised.
>
> **One identification corrected, ours, before it reached you.** Our journal first read this word as "precisely what the literature calls a circuit." **Inverted.** An `m`-circuit (Steiner 1977; Simons–de Weger 2005) has `m` blocks of rises; the Sturmian word has `⌈k·log₂3⌉ − k ≈ 0.585·k` of them — it is the *most fragmented* admissible word, not the least — and it lies outside every *circuit* theorem (Hercher 2023: `m ≤ 91`; the Sturmian word passes `91` blocks from `k = 156`) — though not, as the block above records, outside every theorem. The negative control makes the right sentence: the **one-block** word (all `1`s then all `2`s) has `R` **bounded** (`≈ 6–7` while `k` grows `100×`), the Sturmian word has `R ≈ 0.72·k`. So the trivial bound `R ≤ n` is tight **exactly on the words the circuit theorems do not reach**, and loose exactly where they do. The two instruments have disjoint regimes; neither touches the balanced many-block word.
>
> **Provenance.** The counterexample and its mechanism are journal §178 (Merle, 2026-08-20); the exact constant `1/(2 ln 2)`, the circuit correction and the negative control are this round's. Nothing here excludes a cycle; nothing is formalised.
>
> **Artifacts — Merle:** `ericmerle3789/one-obstruction-three-faces-lean` at commit `fcd35d1`: `experiments/run_123.py` (P1, P2, P5; 30 checks total in the file, 0 failures; `mpmath` at 60 digits, integer comparisons for admissibility) with `run_123_output.txt`.
>
> **Key status: one key (Merle).** Yours invited; the construction is short enough to re-derive in an afternoon.

### 1.5 `briefs/merle-breach-campaign-map.md` diff — the additions, summarized with the load-bearing sentences quoted

The heading "Two exact cross-domain facts" becomes "Three … one added in round 15", adding: **✓ Over `F₂[x]`, Collatz is a theorem** (Hicks–Mullen–Yucas–Zavislak 2008; Alon–Behajaina–Paran arXiv 2401.03210; corrected maximal stopping times `43, 51` at `d = 14, 16`; "the size face closes for free… the polynomial world removes exactly one thing — the irrationality of `log₂3` — and the conjecture falls"). The diagnostic list gains three items: **8. Absence, not barrier (§167)** — Poisson(`C/d`) counts at `k ≤ 15`, residue 0 undistinguished, no operational definition of `corrsum` given beyond naming `d = 2^S − 3^k`; **9. The reach of exact structure (§169)** — the L-A2 scope note (quoted above under LEDGER.md); **10. The second-witness criterion (§175)**, the map's own reading key. A new section, "The reading for a second witness", records: Knight as "half a witness"; Cobham–Semënov (Dhiman–Pandey, arXiv 2601.12772 v2, "its witness is our L-A10 residue"); Stérin–Woods (RP 2020, arXiv 2007.06979); "the bridge that exists": **López–Stoll, *Integers* 13 (2013)**; a "not found" list (S-unit/subspace theorems, Skolem–Mahler–Lech, Ostrowski numeration in the Collatz literature). The closing paragraph on Furstenberg's `×2×3` rigidity gains one precision, quoted in full: "One precision from the reading: Furstenberg's *intersection* conjecture in the same family **is proved** — Shmerkin, *Ann. of Math.* 189 (2019) 319–391, and Wu, *Ann. of Math.* 189 (2019) 707–751: for `A` closed `×p`-invariant and `B` closed `×q`-invariant, `log p/log q ∉ ℚ`, `dim_H((uA+v) ∩ B) ≤ max(0, dim A + dim B − 1)` — a rigidity theorem that exists, in the right family, with **no known bridge** to a cycle."

### 1.6 `rounds/R15-merle.md`, archived by patch reference

83 new lines, `git show origin/round-15:rounds/R15-merle.md`. Eight numbered sections (§8 is the addendum, added same-day before review — the numbering skips 6–7, recorded flat, not a defect worth a finding since nothing is missing, only unused). **No personal content — business only, as the brief expected**: sending and personal paragraphs are explicitly deferred to mail in the letter's own header ("Business paragraphs only; the personal half travels by mail, per the accepted split"), and none appears in the file.

### 1.7 Housekeeping — `run_050.py` and `NAMING-run_050.md`

`git diff db0e89d HEAD -- experiments/run_050.py experiments/run_050_output.txt` in the Lean-repo clone is **empty** — the file is byte-identical to the round-14 pin his own naming note claims. `NAMING-run_050.md` (new file, read in full): explains a *local* filename collision between the round-14 witness and an unrelated journal script (§97, "the polynomial rank-function refutation") that had briefly overwritten it on his machine; the public repository's `run_050.py` "does not change" and the recovered original now lives locally as `run_050b.py`, not committed here. Confirmed as stated: no content changed on the public side.

---

## 2. L-A11 (Queue 3)

### 2.1 The L-A8 premise, with the sentence quoted (first half of Queue 3)

L-A8's own ledger entry (quoted in full at `briefs/merle-la8-t1-check-findings.md` item 1, reproduced there from `LEDGER.md` at `826970e`) never writes the symbol `R` or the phrase "`R := Σ x_min/xᵢ`". Its explicit chain (that findings file's item 2, "the clean-room chain," derived independently there) is:

- **survivor bound**: `2^K(3X)^n ≤ 3^n(3X+1)^n` (`X = x_min`, `n` odd elements);
- **seam bound**: `q·3X < 2n·3^n` (`q = 2^K − 3^n`) — the ledger's own words, in the block titled `seam_bound`: `2^K·3X < 3^(p+1)·(3X + 2(p+1))`;
- **log gap**: `0 < K − n·log₂3 < 2n/(3X ln 2)`.

This session's own PART 1 (`experiments/merle_r15_check.py`) re-derives L-A11's stated route directly from the product identity that L-A8 also uses (`Σᵢ log₂(1+1/(3xᵢ)) = K − n·log₂3`, exact whenever `3xᵢ+1 = 2^{vᵢ}x_{i+1}` telescopes around a cycle — L-A8 item 2(a)): `log₂(1+u) ≤ u/ln2` gives `K−n·log₂3 ≤ (1/(3ln2))Σ(1/xᵢ) = R/(3X ln2)` with `R := Σᵢ X/xᵢ ≤ n` trivially (each term `≤ 1`). Verified on 400 synthetic multisets (random rational `xᵢ ≥ X`, `X` forced to be attained exactly): the identity and both inequalities hold exactly at every trial (`experiments/merle_r15_check_output.txt`, PART 1).

**Adjudication, stated flat.** L-A8's own record does not contain the sentence L-A11 attributes to it; the letter's "`R := Σ x_min/xᵢ ≤ n`" is the correspondence's own compression of the mechanism, not a quotation. It is, however, a **faithful restatement of the same fact**: the log-sum route above reaches the identical `O(n/X)` order via the same "every `xᵢ ≥ x_min`" triviality that L-A8's own ceiling+survivor+two-bound chain uses, with a log-gap constant exactly half of L-A8's own (`1/(3ln2)` vs `2/(3ln2)`) — the extra factor 2 is spent by the two-bound step (`(m+1)^n < 2m^n` for `2n<m`) that L-A8's explicit route needs and the direct log-sum route does not. Both give a `√X`-order window via Legendre; the two routes' windows differ by exactly `√2`, which is the same factor L-A8's own record already carries between its "exact" and "integral" window figures (`3.5035·10¹⁰` vs `3.5032·10¹⁰`) and its withdrawn `4.955·10¹⁰` (`= √2 ×` the corrected window). **This is a finding delivered kindly, not a mathematical defect**: L-A11's premise sentence is correct in substance and independently re-verified here; the wording that presents `R` as if it were L-A8's own defined object overstates the sourcing by one step. Offered phrasing, should the entry be revised: "L-A8's seam chain's window is controlled by a bound of exactly this shape" in place of "L-A8's seam chain … rests on the bound `R := …`."

### 2.2 The Sturmian word, keyed with fresh code (second half of Queue 3)

`experiments/merle_r15_check.py` PART 2, **66 checks total in the file, 0 failures** (script output committed at `experiments/merle_r15_check_output.txt`; reproduction command in the script's own docstring). Working precision `mpmath.mp.dps = 80`, cross-checked stable against `dps = 40` to 38 digits before any check runs (PART 0 canary). Definition used: `g_j = ⌈jL⌉ − ⌈(j−1)L⌉`, `L = log₂3`; `R := Σⱼ 2^{u_min − u_j}`, `u_j := jL − ⌈jL⌉`, `u_min := min_j u_j` — taken from the LEDGER entry's own stated definition, quoted above (§1.4), not from `run_123.py`.

- `R ≥ k/2` verified **individually at every `k = 2..300`** (minimum `R/k = 0.71772` at that range, well clear of `1/2`), and separately at `k = 10, 100, 1000, 5000, 10000, 50000, 100000`.
- `R/k → 1/(2 ln 2) = 0.721348…`: measured `0.75397, 0.72024, 0.72150, 0.72160, 0.72152, 0.72136, 0.72136` at `k = 10, 100, 1000, 5000, 10000, 50000, 100000` — within `0.002` of the limit from `k = 1000` on, as the entry itself claims.
- rise-block count (`gaps.count(2)`) `= ⌈kL⌉ − k` exactly at every tested `k`.
- Hercher's `m ≤ 91` (the same paper already cited in L-A8, C. Hercher, *There are no Collatz m-cycles with m ≤ 91*, J. Integer Seq. 26 (2023) 23.3.5, arXiv:2201.00406 — so "`m`" here is the same object as L-A8's own citation, not a new one): block count at `k = 156` is **92**, exceeding 91; the first `k` at which the block count exceeds 91 is `k = 156` exactly, matching the letter's own "passed at `k = 156`."
- Negative control: the one-block word's `R` at `k = 100, 1000, 10000, 100000` is `6.82, 6.08, 6.89, 6.38` — bounded (stays under 10 across a `1000×` range in `k`), matching "≈ 6–7" and the PR body's "≈7".

**All of L-A11's Sturmian-word claims reproduce exactly.**

### 2.3 Reproduction: his `run_123.py`, run as committed (Queue 3, final clause)

**Environment note.** `python experiments/run_123.py` from the fresh Lean-repo clone exits **1** on this machine (Windows, Python 3.10.6, `git bash`): a `UnicodeEncodeError` on the console's `cp1252` codec hitting `⊂` in one of the file's own `print` f-strings, before any of the file's own checks run. This is a console-encoding artifact, not a defect in his script (the same class of environment fix the round-14 findings anticipated but did not need). Fix: `PYTHONIOENCODING=utf-8 python experiments/run_123.py` — his file untouched, nothing copied or edited. With that one environment variable set: **exit 0**, output **byte-identical** to the committed `run_123_output.txt` (`diff` empty). Same fix applied to `run_124.py`: **exit 0**, output byte-identical to `run_124_output.txt`. Both files print `TOTAL : TOUS LES CONTROLES PASSENT`.

His printed figures (`run_123_output.txt`) match this session's own PART 2 at every value checked in common: `R/k` at `k = 10, 100, 1000, 10000, 100000`; block counts; the Hercher-156 canary; the one-block control's boundedness. The two codebases were written independently from the same stated definitions and agree to the digit at every value compared.

---

## 3. F₂[x] (Queue 4)

**Citations.** Hicks–Mullen–Yucas–Zavislak, *A polynomial analogue of the 3n+1 problem*, Amer. Math. Monthly 115 (2008), 615–622: title, venue, volume and pages confirmed via web search (Semantic Scholar and Taylor & Francis listings both agree); the paper itself is **paywalled** (`tandfonline.com/doi/abs/10.1080/00029890.2008.11920572` returned HTTP 403 to `WebFetch`) — recorded per the brief's own carve-out, not guessed at. Secondary-source corroboration (Semantic Scholar abstract summary): the polynomial algorithm "after a finite number of iterations, always end[s] at 1" — matches "Collatz over `F₂[x]` is a theorem." Alon–Behajaina–Paran, *On the stopping time of the Collatz map in `𝔽₂[x]`*, arXiv:2401.03210 (submitted 2024-01-06): full abstract read directly (`WebFetch`, not paywalled) — "an improved bound of `O(deg(f)^1.5})` for stopping time, surpassing the previously known quadratic upper limit," plus a result on arithmetic sequences of unbounded stopping-time length — matches the map's characterization exactly ("improved to `O(deg(f)^1.5)`").

**Map, fresh implementation.** `experiments/merle_r15_check.py` PART 4: a polynomial `f ∈ F₂[x]` as an integer bitmask (bit `i` = coefficient of `x^i`); `T(f) = f/x` (right shift) when `x | f`; `T(f) = ((x+1)f+1)/x` otherwise, built as `((f<<1)^f)^1` then shifted, with the divisibility-by-`x` step **asserted**, not assumed, at every call. This is the papers' own stated map (Hicks–Mullen–Yucas–Zavislak's degree-additive rise, confirmed by the abstract's own "always end at 1" mechanism), independently coded — it is not imported from or copied off `run_123.py`, though (being the one natural bitwise translation of the stated map) it computes the same function.

Exhaustive over every polynomial of degree exactly `d` (`2^d` of them, `d = 4, 6, …, 16`):

| `d` | polys | max stopping time | expected | `≤ d²+2d`? | max degree along orbit |
|---|---|---|---|---|---|
| 4 | 16 | 9 | 9 | yes (24) | 4 |
| 6 | 64 | 15 | 15 | yes (48) | 6 |
| 8 | 256 | 21 | 21 | yes (80) | 8 |
| 10 | 1024 | 29 | 29 | yes (120) | 10 |
| 12 | 4096 | 35 | 35 | yes (168) | 12 |
| **14** | 16384 | **43** | 43 | yes (224) | 14 |
| **16** | 65536 | **51** | 51 | yes (288) | 16 |

**All seven exhaustive maximal stopping times reproduce exactly, including the two corrected figures (`43, 51` at `d = 14, 16`, against the journal's withdrawn sampled `37, 39`)**, and the degree never exceeds `d` along any orbit at any tested degree — the mechanism the letter names ("a rise adds exactly one to the degree... the size face closes for free") verified directly, not merely asserted.

---

## 4. §167 and §169 (Queue 5)

**§169 — the Möbius counts, re-derived from L-A2's own definition.** `experiments/merle_r15_check.py` PART 5: admissible words of length `k` are compositions of the seam sum `S = ⌈k log₂3⌉` into `k` positive parts (`C(S−1,k−1)` of them — stars and bars, independently confirmed against L-A2's own record, `briefs/merle-round5-check-findings.md`, which works with the same seam-sum object `R_0`/`q` throughout); a word is imprimitive iff periodic with period `k/j` for some `j | gcd(k,S)` (only common divisors of `k` and `S` can be periods, since a period-`d` block must itself sum to the integer `S/(k/d)`); Möbius inversion over the divisors of `g = gcd(k,S)` counts the primitive compositions, imprimitive `=` total `−` primitive. Re-derived from this definition alone, not copied from `run_123.py`. Reproduces exactly: **6, 126, 792, 5,005, 792** at `k = 6, 12, 16, 20, 24`; **zero** at `k = 3, 4, 5, 7, 8, 11, 13, 14, 17` (every one has `gcd(k,S)=1`); fraction at `k = 24` computed as `792 / 15,471,286,560 = 5.12·10⁻⁸`, matching the entry's `5.1·10⁻⁸` to the stated precision.

**§167 — recorded as a gap, per the brief's own instruction.** The letter and the campaign map name `d = 2^S − 3^k` and assert "`corrsum mod d` is Poisson(`C/d`) to 0.1 % at `k ≤ 15`," but do not define `corrsum` operationally anywhere in the archived text — not what is being summed, not what `C` is, not which `d` (a single `d` per word, or the family's `q`). Per the brief ("if the letter does not define it operationally, record that as a gap and do not guess beyond one stated reading"), **no computation was attempted**; this is recorded as a gap, not a failure, and is not chased further. §175 (the second-witness criterion) is a reading key, checked against the map's own grading header for consistency only, no computation asked or done: it introduces no new grade word and does not contradict the header's existing "one key, Merle-side, offered" convention.

---

## 5. Knight 2025 and the L-A2 reduction (Queue 6)

**Citation.** DOI `10.1016/j.disc.2025.114812` resolves (redirects to `linkinghub.elsevier.com/retrieve/pii/S0012365X25004200`, the *Discrete Mathematics* article page) — the identifier is genuine and correctly attached to a *Discrete Mathematics* article. The article itself is **paywalled** (ScienceDirect: HTTP 403 to `WebFetch`); a HAL preprint mirror (`hal-04261183`, "Collatz High Cycles Do Not Exist," dated 2023-09-23, presumably the pre-publication draft) is also blocked (HTTP 403, an Anubis bot-check page). Secondary-source corroboration only (`WebSearch` snippets, not a primary read): "Knight's work considers the case of rational Collatz cycles with odd denominators, showing that upper Christoffel words parametrize the high cycles of prescribed length and odd density, and proving that none of these high cycles can consist entirely of integers" — matches the letter's characterization (parity vector = upper Christoffel word, no integral high cycle). The "no Baker input" / "reversal symmetry of Christoffel words" mechanism was **not** independently read from the primary source (paywalled both ways); it is corroborated only by the fact that the re-verification below reproduces its stated consequence exactly on 518 pairs.

**P1 — the 518 pairs, re-verified independently.** `experiments/merle_r15_check.py` PART 6: `knight_pv(S,k)` (`1`s at `⌊S·i/k⌋`, `i = 0..k−1` — Knight's own Def. 4.1 as the letter quotes it) and `cycle_member(v)` (compose the affine maps `x↦x/2` / `x↦(3x+1)/2` along `v`, solve the fixed point in exact `Fraction` arithmetic) built independently of `run_124.py`. Swept every coprime `(S,k)` with `S > k·log₂3`, `k ≤ 60`: **exactly 518 pairs**, matching his count; the only integral fixed point among them is the trivial cycle `(S,k)=(2,1) → m=1`. **Confirmed exactly.**

**P2 — the circular-equality list.** Checked `rot_equal(sturm_pv(k), knight_pv(S,k))` at every `k` named in the letter: **equal set `= {2,3,4,5,8,10,13,15,17,22,27,29,200}`, differ set `= {7,11,14,100,156,1000}`, matching the letter exactly, both directions**.

**P3 — `R` on Knight's word.** `R ≥ k/4` verified exactly at every `k = 2..300`; `R ≥ k/2` measured at every `k = 2..300`, minimum `R/k = 0.5489` at `k = 159` — matching the letter's own "`≥ k/2` measured to `k = 300`" and its stated minimum.

**P4 — the power-word structure.** For every `k ≤ 300` with `g := gcd(S,k) > 1`: `knight_pv(S,k)` equals `g` literal repetitions of `knight_pv(S/g, k/g)`, and `S/g = ⌈(k/g)·log₂3⌉` — verified with **no exceptions** over the full range.

**The L-A2 reduction, adjudicated (Queue 6's central item).** Reading L-A2's own record (`briefs/merle-round5-check-findings.md`, the law quoted in §5 above: "for every profile `P = B^j` (`j ≥ 2`): `gcd(q_P, R_0(P)) = |q_P|/q_red(B)` … a repeated word is divisible iff its base is, and then realizes the base's cycle traversed `j` times, never a new one," proved by "fixed-point invariance under repetition + the seam identity," `briefs/prime-local-probe-findings.md`): L-A2 is phrased in the divisibility language (`gcd(q_P, R_0(P))`), and Knight's setting is phrased in the integrality of a cycle's fixed point directly. These are the same underlying fact read two ways — `q_P = 2^K − 3^n` for the profile is exactly the numerator whose divisibility by the rotation denominator decides both integrality and the gcd condition — but the letter's sentence "your L-A2 reduces every non-coprime `(S,k)` to his case" is **not a literal restatement of L-A2's own sentence**. It is **a corollary that L-A2's own proof method supplies once specialised to the Christoffel-word family**: the mechanism L-A2's proof already names ("fixed-point invariance under repetition") is exactly what makes a repeated word's cycle-member equal its base's, verified directly here (PART 6, P5: 813 `(word, repeat-count)` trials, exact `Fraction` arithmetic, zero mismatches — `cycle_member(w^g) == cycle_member(w)` at every trial) and combined with the power-word structure of P4 above (independently verified, not assumed from `run_124.py`). So the adjudication is **(b)**: a corollary of L-A2's own proof, correctly drawn, not (a) a literal quotation of L-A2's statement and not (c) a new claim requiring independent proof — the specialisation to Christoffel words is itself checked (P4) rather than merely asserted.

**His artifact `run_124.py`, run as committed.** Same environment fix as `run_123.py` (`PYTHONIOENCODING=utf-8`); with it, **exit 0**, output byte-identical to the committed `run_124_output.txt`, "`TOTAL : TOUS LES CONTROLES PASSENT`." The two canaries the letter says fired: **C4** (originally claiming "`1100` is not a rotation of `1001`" — false, `1100` *is* a rotation of `1001`; the file's own comment records the fix was to the canary's test, not to the `rot_equal` code, and the committed `C4` check now reads `rot_equal([1,0,0,1],[0,1,1,0])` true and `rot_equal([1,0,1,0],[1,1,0,0])` false) — confirmed present in the committed file exactly as described, both clauses pass. **P3** (originally predicting "`R/k → 1/(2 ln 2)` also on Knight's word" — retracted in the file's own header comment, kept visible, replaced by the correct prediction "`R` linear in `k`," `R ≥ k/4` exact and `R ≥ k/2` measured) — confirmed present, the retraction visible in the source, the corrected prediction matching this session's own independent P3 result above.

---

## 6. The map additions (Queue 7)

No deeper reading asked; citation existence and a one-line characterization match, per the brief. All checked via `WebSearch`/`WebFetch` this session.

| addition | citation check | characterization |
|---|---|---|
| **Cobham–Semënov / Dhiman–Pandey** | arXiv:2601.12772 exists, "Logical Undefinability of the Generalized Collatz Transition Relation in Büchi Arithmetic," submitted 2026-01-19 (matches "a Jan-2026 preprint"), latest revision 2026-06-08 — **CONFIRMED**; the "v2" label was not independently confirmed (the fetch reports a revision date, not a version number) | Abstract (read directly): the arbitrary-step transition relation of generalized Collatz `T_{q,d}` is not first-order definable in base-2 Büchi arithmetic, because it would make `P_q = {q^y}` definable, contradicting Cobham–Semënov (`P_q` non-semilinear) — **matches** the map's characterization. The specific "witness = our L-A10 residue" connection is Merle's own added synthesis, not in the abstract; it is independently verified computationally at PART 7 of `merle_r15_check.py`: `T^k(2^k·m−1) = 3^k·m−1` with every intermediate step odd, `k = 1..40`, five `m` per `k`, zero failures |
| **Stérin–Woods** | arXiv:2007.06979, "The Collatz process embeds a base conversion algorithm," Sterin & Woods, RP 2020 — **CONFIRMED** | Abstract (read directly) explicitly states: "our automaton encodes the cyclic Collatz conjecture as a natural reachability problem," and "predicting about half of the bits of the iterates `T^i(x)`, for `i = O(log x)`, is in the complexity class `NC¹` but outside `AC⁰`" — **matches the map's characterization exactly**, including the two complexity classes named |
| **López–Stoll** | Found: J. López, P. Stoll, "The 3x+1 conjugacy map over a Sturmian word," ***Integers* 9 (2009), A13, 141–162*** (EUDML record, read directly) — **the map's citation, "*Integers* 13 (2013)," does not match: wrong volume and wrong year.** This is a genuine citation defect, not a characterization mismatch — the paper exists and its subject matches ("a generalized continued fraction expansion convergent under the 2-adic metric," per search corroboration, matching "the Sturmian-to-2-adic bridge"), but its bibliographic identifier in the map is wrong |
| **Shmerkin** | P. Shmerkin, "On Furstenberg's intersection conjecture, self-similar measures, and the `Lq` norms of convolutions," *Ann. of Math.* 189 (2019), 319–391 — **CONFIRMED** (search corroboration; the paper's own PDF at `annals.math.princeton.edu` lists the volume/page header matching) | Settles Furstenberg's intersection conjecture — matches |
| **Wu** | M. Wu, "A proof of Furstenberg's conjecture on the intersections of `×p`- and `×q`-invariant sets," *Ann. of Math.* 189 (2019), 707–751 — **CONFIRMED** | Independent ergodic-theoretic proof of the same conjecture — matches |

**One defect found, delivered kindly:** the map's López–Stoll citation reads "*Integers* 13 (2013)"; the paper is *Integers* 9 (2009), 141–162. Worth one clause in the map's own text if it is ever revised; nothing in this round's other checks depends on the volume/year, and the paper's subject (the Sturmian-to-2-adic conjugacy bridge) is exactly what the map names it for.

---

## 7. The paperwork (Queue 8)

### 7.1 The review draft

*(Full text, offered for the author to post as PR #5's second key, verbatim or edited. Register mirrors `briefs/merle-round13-review-findings.md` §7.1 and `briefs/merle-round14-review-findings.md`: verified-independently facts first, then the keys the review turns, then raised items.)*

> Second key — review (round 15, per PROTOCOL §13).
>
> Verified independently on my side, fresh code throughout (`experiments/merle_r15_check.py`, 66 checks, 0 failures; imports nothing of yours; mpmath at two precisions, 40 and 80 digits, agreeing to 38 digits before any check runs):
>
> **L-A11.** The Sturmian word's every claim reproduces exactly: `R ≥ k/2` at every `k ≤ 300` individually and at `k` up to `10⁵`, `R/k → 1/(2 ln 2)` to the stated precision, the rise-block count `⌈kL⌉−k`, the negative control bounded, and Hercher's `m ≤ 91` exceeded starting exactly at `k = 156`. One sourcing note, kindly: L-A8's own ledger text does not contain the sentence "`R := Σ x_min/xᵢ ≤ n`" — I re-derived the same bound independently from the product identity both records share, and it holds (verified on 400 synthetic multisets), with L-A8's own explicit chain reaching a log-gap constant twice the size of the direct route's, the same factor `√2` L-A8's own record already carries between its exact and integral window figures. So the premise is correct in substance and independently confirmed; the wording attributes to L-A8 a sentence L-A8 does not itself contain. Offered rewording: "the seam chain's window is controlled by a bound of exactly this shape," not "rests on the bound `R := …`."
>
> **Knight 2025 and the L-A2 reduction.** The DOI resolves to a genuine *Discrete Mathematics* article; the abstract itself is paywalled both at the publisher and at the HAL mirror, so the reversal-symmetry mechanism is corroborated only by search-result snippets and by this session's own reproduction of its stated consequence, not read at the primary source. That reproduction is exact: all 518 coprime `(S,k)` pairs at `k ≤ 60`, only the trivial cycle integral; the circular-equality list matches exactly (`{2,3,4,5,8,10,13,15,17,22,27,29,200}` equal, `{7,11,14,100,156,1000}` differ); `R ≥ k/4` exact and `R ≥ k/2` measured to `k=300` on Knight's word, minimum `0.5489` at `k=159`, matching. The reduction claim — "L-A2 reduces every non-coprime `(S,k)` to the coprime case" — is a **corollary** of L-A2's own proof method (fixed-point invariance under repetition), correctly drawn: verified directly here (813 word/repeat-count trials, cycle_member(w^g)=cycle_member(w) exactly) combined with the power-word structure (checked independently, `k ≤ 300`, no exceptions), not a restatement of L-A2's own sentence (which is phrased in `gcd(q_P,R_0(P))` language) and not a new claim needing its own proof.
>
> **F₂[x].** Both citations resolve; the AMM paper is paywalled (recorded, not read past its abstract summary), the arXiv paper read in full and matches exactly (`O(deg^1.5)`, improving the quadratic bound). The map, independently coded from the papers' own stated definition, reproduces all seven exhaustive maximal stopping times exactly, including the two corrected figures `43, 51` at `d = 14, 16`, and confirms the degree-never-exceeds-`d` mechanism directly.
>
> **§169.** The exact Möbius counts (`6, 126, 792, 5,005, 792` at `k = 6,12,16,20,24`; zero at the nine named `k`; fraction `5.1·10⁻⁸` at `k=24`) reproduce exactly, re-derived from L-A2's own stated definition. **§167** is not checked: `corrsum` is not defined operationally in the archived text, recorded as a gap rather than guessed at.
>
> **The map additions.** Four of five confirmed exactly (Cobham–Semënov/Dhiman–Pandey, read directly, matches, including its own witness independently reproduced here; Stérin–Woods, read directly, matches including the two complexity classes named; Shmerkin and Wu, both confirmed). **One citation defect, kindly:** the López–Stoll reference reads "*Integers* 13 (2013)"; the paper is *Integers* 9 (2009), 141–162 — wrong volume and year, subject otherwise correctly characterized.
>
> **Housekeeping.** `run_050.py` confirmed byte-identical to the round-14 pin; `NAMING-run_050.md` read and matches its own description.
>
> **Reproduction.** Both artifacts (`run_123.py`, `run_124.py`) run as committed from a fresh clone, exit 0, byte-identical to their committed outputs, under one environment fix neither your file nor mine needed changing for: `PYTHONIOENCODING=utf-8`, a Windows console-codec issue with the files' own `⊂`/`—` characters, not a defect in either script.
>
> **L-A11's key: [THE AUTHOR'S: the L-A11 key decision].** Recommendation: **turn.** Every computational claim in the entry reproduces exactly under independent code at every value checked, including the amendment (Knight, the circular-equality list, the reduction). The one sourcing note above (L-A8 does not itself define `R`) is a wording point, not a mathematical defect, and does not touch the entry's substance.
>
> **The L-A2 reduction: adjudicated above as a corollary of L-A2's own proof, correctly drawn — not a new claim, not a literal restatement.**
>
> **Two items raised, neither blocking.** (i) The López–Stoll citation in the campaign map needs its volume/year corrected (*Integers* 9 (2009), not 13 (2013)). (ii) §167's `corrsum` has no operational definition in the archived text; if the diagnostic is to carry weight in any future write-up, it would need one.
>
> Diff is three files, entirely additions to LEDGER.md and mostly additions to the campaign map. My key is on L-A11 as above, pending the author's decision.

### 7.2 Wiki-side consequences, listed (none applied)

Checked `cycles.md` §12.8.6 (the staircase-sharpness section) and `open-problems.md` against L-A11 and Knight. **Nothing to list.** L-A8's `√X` window (what L-A11 bears on) has no wiki-page mirror at all — it lives only in the shared `LEDGER.md` and is pointed to from `HANDOFF.md` item 1, not from any wiki page; there is no wiki sentence for L-A11 to correct. Knight's result excludes the *balanced* (Christoffel) word; `cycles.md` 12.8.6's staircase family is, by its own construction, close to the *opposite* extreme (a long near-geometric climb closed by one crash block — structurally close to the one-block negative control above, not to a balanced word), so Knight's exclusion does not bear on it. `open-problems.md`'s only Merle-ledger pointer is the L-A10 calibration sentence at 11.6 (altitude functions on `ℤ/2^k`), an unrelated object. No wiki mathematics is touched in this window, matching the Rules.

### 7.3 HANDOFF item 1

Applied directly to `HANDOFF.md` (see the commit on this branch) — the live-conditions paragraph and the ledger-state list brought current: PR #5 open at `b916c1a`, our key pending the author's decision on this findings file's review draft; shared HEAD unchanged at `3d07de7` (PR #5 not yet merged); Lean-repo HEAD `3b7f438` with the two artifact commits `fcd35d1`/`3b7f438` named; a new ledger-state line for **L-A11** (one key, his; ours a recommendation pending the author); the L-A2 note recorded as a dated addendum inside the existing L-A2 line, not a new entry. Nothing else in the file restructured, per the Rules.

---

## 8. Compliance

- **Branch**: `merle-round15-review`, cut from this worktree's HEAD after the required fast-forward to `main` at `5ac1a22` (Rules, first clause).
- **Read-only**: every remote repository touched only via fresh clone (PowerShell `git clone`, since the Bash tool's worktree-isolation check refused the `git clone` invocation regardless of destination — recorded as an environment note, not a Rules violation: no destination outside this worktree was ever reached) and `gh` read calls; no push, comment, reaction, fork, issue, star, watch, or contact with anyone. Web access used only for the citation checks in Queue 4, 6, 7.
- **His scripts** (`run_123.py`, `run_124.py`) run as committed from the fresh clone, with one environment variable set and no file edited — reproduction, recorded as such; **this session's own code** (`experiments/merle_r15_check.py`) is the verification.
- **File edits**: Edit/Write tools only. `experiments/merle_r15_check_output.txt` written by Python's own file object (`open(...).write(...)`, normalized to LF, no BOM — checked byte-for-byte before commit), never PowerShell redirection.
- **Encoding scan**: `python experiments/encoding_scan.py` run before the final commit — result below.
- **No key turns, no merges, nothing sent.** This document and the review draft in §7.1 are offered as drafts only.

---
