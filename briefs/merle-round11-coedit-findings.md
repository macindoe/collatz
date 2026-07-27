# Findings: round-11 co-edit prep (merle-round11-coedit)

Delegated session, 2026-07-28. Brief: `briefs/merle-round11-coedit-brief.md`
(commit `9fdaa0f`). Branch `merle-round11-coedit`, **base commit `9fdaa0f`** —
the worktree was cut at the session-start HEAD `2225b68`, which contains
neither the brief nor any round-11 finding, so it was moved onto current `main`
(`9fdaa0f`) before any work began, exactly as the launch instruction and the
brief's Rules require.

**SHARED REPO NOT PUSHED. Nothing left this machine.** No push to the shared
repo, no push to our own remote, no interaction of any kind with either of his
repositories. The shared repo received exactly one **local** commit on a local
branch of a fresh scratchpad clone; the patch archived under
`briefs/merle-round11-coedit-patches/` is the portable form. **Handbacks:
none.** No reply paragraphs (parallel session `merle-round11-reply`), no
wiki-page edits, everything outside this repo read-only except the scratchpad
clones. Register: flat; corrections offered, never argued; nothing anywhere
comments on his self-corrections.

---

## 0. PRE-PUSH CONDITION — read this first

**Every artifact pin this commit carries lives in a commit that exists only on
our local `main`. Public wiki `main` is behind, and none of the pins resolves
today.**

Checked by `ls-remote` against `https://github.com/macindoe/collatz.git`,
2026-07-28 09:37 AUSEST (2026-07-27 23:37 UTC): public `main` =
**`2225b6849a659bd74c6d03aff05823f8130c0c9d`** (`2225b68`) — which is, not
coincidentally, the stale commit this session's worktree was cut from. All of
round 11 is unpushed.

The complete pin list, each checked individually against the public remote:

| pin | record it serves | files at that commit | on public `main` (`2225b68`)? |
|---|---|---|---|
| `dc8fde6` | L-A8 kernel key-turn block | `experiments/merle_r11_ceiling_audit.py` + `merle_r11_ceiling_audit_output.txt` | **NO** |
| `38ccc49` | L-A8 hygiene verification record | `experiments/merle_r11_hygiene_check.py` + `merle_r11_hygiene_check_output.txt` | **NO** |
| `dc8fde6` | the one-sidedness sharpening | (as above) | **NO** |
| `38ccc49` | the theorem hand-back | (as above) | **NO** |

Two distinct commits, four citations. Both are verified ancestors of local
`main` (`9fdaa0f`) and both contain exactly the named script plus its committed
output; neither is an ancestor of `2225b68`.

**Stated plainly: the author must push wiki `main` before or with the
shared-repo push, or the pins will not resolve.** The earliest commit on `main`
containing both pin targets is **`185c622`** (the hygiene-check merge); current
`main` is `9fdaa0f`, which is the natural choice and also carries this round's
briefs. This is a condition, not a handback — the shared-repo push is gated on
the author anyway and the fix is his routine main push. **The same check caught
a real problem at round 9 and again at round 10**, both times with the pins
dangling for exactly this reason.

No pin is carried for the L-A3 (B) date-stamp: that edit adds no claim and no
artifact, and the block's existing `52e8c5c` pin is untouched.

---

## 1. Shared-repo state verified, at the start and at the end

| # | when | method | result |
|---|---|---|---|
| 1 | **2026-07-28 09:35 AUSEST** (2026-07-27 23:35 UTC) | `git ls-remote` on `github.com/macindoe/one-obstruction-three-faces` | `c96687544fd387fd8bcff1df2c04056a2be99f3a` at both `HEAD` and `refs/heads/main` — **unmoved** |
| 1b | same minute | fresh unauthenticated clone into the scratchpad | HEAD `c966875`, tree `bcae6b6` — the round-10 tree exactly, confirming the record |
| 2 | **2026-07-28 09:48 AUSEST** (2026-07-27 23:48 UTC) | `git ls-remote`, immediately before finishing | `c96687544fd387fd8bcff1df2c04056a2be99f3a` — **still unmoved** |

The public wiki remote was re-checked in the same command at the same minute
and is still at `2225b68`, so the pre-push condition of §0 stands as written.

Nothing of his has landed since our own round-10 push. No stop condition
triggered; no re-seating was needed. The L-A8 and L-A3 entry texts at `c966875`
were read in full before editing and match the verbatim quotes carried in
`briefs/merle-la8-t1-check-findings.md` and
`briefs/jointnote-premise-external-findings.md` §4.3.

---

## 2. The prepared commit

- **Clone:** fresh, unauthenticated, `scratchpad/r11/shared`. Identity set
  repo-local to `macindoe <begemite0.o@gmail.com>`, the established co-edit
  author (`e53630f` / `641a530` / `c966875` precedent).
- **Line endings, handled up front.** This machine has `core.autocrlf=true`
  globally, so the checkout arrived CRLF against an LF blob. `core.autocrlf`
  and `core.eol` were set repo-local to `false`/`lf` and all four files
  re-checked-out **before any edit**, so the working tree matched the blob
  byte-for-byte (verified: 0 CR bytes, tree `bcae6b6`). Every count below is
  therefore a real content count and not a line-ending artefact.
- **Branch:** `round11-coedit`, from `c966875`.
- **Commit:** **`2f724d159e2f5c080fae4c9e26810d8622581e8c`** (`2f724d1`),
  **tree `5c0ccbfa10561bc1292031c3b22073ab48319f5f`** (`5c0ccbf`).
  **`LEDGER.md` only, 44 insertions / 1 deletion.**
- **Patch:** `briefs/merle-round11-coedit-patches/0001-Round-11-co-edits-the-Macindoe-kernel-key-turned-on-.patch`
  — verified by `git am` onto a **separate, pristine** clone checked out at
  `c966875` (tree `bcae6b6` confirmed before applying). It applies clean, and
  the resulting tree is **`5c0ccbf`** — **tree-identical** to the prepared
  commit. The applied `LEDGER.md` was additionally compared byte-for-byte
  against the prepared clone's: 114,762 bytes both sides, **identical**. The
  applied commit's SHA is `b6aaa67` rather than `2f724d1` because `git am`
  restamps the committer date — the round-10 record notes the same thing, and
  **the tree is the object that matters**.
- **Encoding:** the edited `LEDGER.md` is valid UTF-8, no BOM, 0 CR bytes,
  ends with a newline, and carries **no** double-encoding signature (114,762
  bytes / 111,941 characters). All edits were made with the Edit tool;
  PowerShell `Get-Content`/`Set-Content` was not used on any file this session.
  `experiments/encoding_scan.py` run over the tracked tree before the final
  commit — result in §7.

### 2.1 The diff stat, with the one deletion justified

```
 LEDGER.md | 45 ++++++++++++++++++++++++++++++++++++++++++++-
 1 file changed, 44 insertions(+), 1 deletion(-)
```

`git diff --stat --ignore-all-space` reports the same 44 / 1, so no part of the
count is whitespace.

**The single "deletion" is a pure-append modification of one line, and that
line is our own.** It is line 93, the closing sentence of the **Macindoe**
block `On (B): definition pinned, replication, and the asymptote (Macindoe,
2026-07-24)` in L-A3 — the date-stamp of item 7. Verified mechanically: the
pre-edit line is an **exact prefix** of the post-edit line (954 characters
grow to 1,318; `new.startswith(old)` is `True`), so nothing whatsoever was
removed, and the appended tail is the parenthetical quoted in §3.7.

Everything else in the commit is pure insertion at the end of the file. **No
prose of his is touched anywhere**, and no line of his is modified, reordered,
or reflowed. Unlike round 10, no final-newline deletion arises: `c966875`'s
`LEDGER.md` already ends with a newline, because our own round-10 commit
supplied it.

### 2.2 Diff summary by entry

| entry | change | lines |
|---|---|---|
| L-A3 (B) | date-stamp appended to our own Key-status sentence | 1 modified |
| L-A8 | ten new blocks appended after the round-10 `ceiling_upper` mismatch paragraph | 44 added (blocks + their separating blanks) |

---

## 3. The prepared blocks, verbatim

### 3.1 L-A8 — the ceiling pinned, in his own proposed wording

> **The ceiling is pinned — both halves at the kernel (Merle's proposed wording, 2026-07-27; entered by Macindoe at his request, 2026-07-28).** After the round-10 audit he left this entry untouched rather than restate his own claim, and proposed the wording instead; it is written here as he proposed it.
>
> > `ceiling_pinned` : a positive cycle with `p+1` odd elements, all `≥ X`, with `2(p+1) < 3X`, satisfies `3^(p+1) < 2^K ∧ 2^K < 2·3^(p+1)` — so `K = ⌈(p+1)·log₂3⌉` is forced, in pure integers, with no logarithm in the statement.
>
> The **lower half** `3^(p+1) < 2^K` was found missing in the Macindoe round-10 audit — `ceiling_upper` proves only the upper bound, and the lower half travelled downstream as the unproved hypothesis `hceil` — and it was **proved afterwards**, as `ceiling_lower` (stack `6c084c5`, 2026-07-26). Both facts are recorded because both are part of the entry's history; neither is stated as anything more than what happened. `ceiling_lower` is unconditional — no `hpX`, no `2⁷¹`, no window, no real-number hypothesis of any kind, the statement and proof entirely in ℕ, its only inputs `cycle_prod_identity` and Mathlib's `Finset` product lemmas — and `hceil` is **removed** from the four downstream signatures rather than merely discharged at their call sites. The two-sided sentence this entry has carried since stack `41fa4f8` is therefore now a single kernel theorem rather than half a theorem plus an elementary hypothesis, and the statement/prose mismatch recorded in the paragraph above is closed at the statement level.

### 3.2 L-A8 — the kernel key turned, scoped, read-not-built

> **Macindoe kernel key turned on L-A8 (2026-07-28) — scoped in the ContentDescent language, and read-not-built in the same breath.** Round 10 turned our key on the mathematics of every link and deferred *every* kernel claim to a statement-match audit; that deferral is now discharged. The kernel key turns on five things and no more — the **statement match** (fifteen declarations of `T1Structure.lean` at `c991430` read and matched against this entry's blocks, with `ceiling_lower` and `ceiling_pinned` recorded verbatim and all four downstream signatures recorded before and after), the **dependency structure** (the `hceil` removal, below), the **committed axiom logs** (below), the **truth of every statement as instantiated** (`experiments/merle_r11_ceiling_audit.py`, **190 exact checks, 0 failures**, in fresh code that imports nothing from either Merle repository and nothing from our own round-10 scripts; every decision that can be exact-integer is exact-integer, and where a logarithm is unavoidable the work is done in `Decimal` at two precisions, 120 and 200 significant digits, with agreement asserted for every reported quantity), and **our own derivation of the repair**, written before reading his proof term line by line and agreeing exactly — and it turns **read-not-built**: there is no Lean toolchain our side, none was installed, nothing was compiled, so the kernel-3 / `[propext]`-only / `convPairs_length`-no-axioms / 0-`sorry` / 0-`native_decide` claims rest on his committed logs and his four-way-hardened protocol rather than on a build of ours. Artifact: `macindoe/collatz` `experiments/merle_r11_ceiling_audit.py` with committed output (commit `dc8fde6`, on `main`).
>
> **The dependency structure — the `hceil` removal is verified, not taken.** This is the part of the claim most easily reported in good faith and still wrong, so it is the part that was checked hardest, against every mechanism by which a hypothesis can vanish from a printed signature and still be threaded. `hceil` is gone from all four downstream signatures (`ratio_bound_at_barina`, `log_gap_at_barina`, `log_gap_gen`, `quotient_is_convergent_gen`); it is **not renamed** and not weakened — the binder lists shrink by exactly one and change in no other respect; it is **not a structure or class field** — none is declared; and it is **not hoisted**, because `T1Structure.lean` declares no `variable`, `include`, `omit`, `section`, `structure`, `class`, `instance`, `attribute` or `local` anywhere in its 482 lines, the only structural keywords in the file being its opening `namespace` and closing `end`. It is genuinely re-derived internally, by `have hceil := ceiling_lower p _ K x v hstep hK (by positivity) hmin` at two located call sites (inside `ratio_bound_at_barina` and inside `log_gap_gen`), and inherited transitively by the other two, each of which simply passes one fewer argument to its predecessor. Nothing rode along with the repair: the window constants, `2000`/`2079`, `4000·(p+1)² ≤ 2079·X`, the `2⁷¹` numerals and every conclusion are character-identical between `5c9b663` and `c991430`. Positivity of `∏x` is **proved in-file**, in two lines, from `0 < X ≤ xᵢ` and `Finset.prod_pos` — not assumed. His sentence "derived internally now, so it cannot travel as an assumption again" is accurate as committed.
>
> **The committed axiom logs, and the 13 → 15 reconciliation.** `T1Structure_axioms.txt` at `c991430` carries fifteen entries, in exactly the order of the fifteen `#print axioms` lines at the end of the file, one-to-one, nothing extra and nothing missing: `discharge_all` → `[propext]` only, `convPairs_length` → "does not depend on any axioms", the remaining thirteen each exactly `[propext, Classical.choice, Quot.sound]`. The reconciliation against the round-10 log is **exact, and it is 13 + 2**: the diff adds precisely `ceiling_lower` and `ceiling_pinned`, and **no entry is removed, renamed, reordered or re-axiomatised** — the thirteen pre-existing entries are byte-identical. `DeficitLemma_axioms.txt` is now **10 of 10**, `key_shifted` and `key15` carrying their own probes, so the round-10 gap there is closed directly and not merely transitively. **`sorryAx` is absent** from the entire tree but for two prose lines inside the RETRACTED block. The RETRACTED record for `da2c8db` is present as a standalone block, marked "PERMANENT RECORD, DO NOT REMOVE", stating what was claimed, why it was false, the real obstruction, the fix, and the four-way hardening; nothing at HEAD depends on the retracted result, and the non-`gen` `quotient_is_convergent` exists nowhere in the tree. The `DeficitLemma.lean` SCOPE header is corrected in place and now matches the file it heads. There is **no drift** in `ContentDescent.lean`, `ContentSeparation.lean`, `TransportRecurrence.lean` or `LegendreApprox.lean`, and the graph `5c9b663 → 6c084c5 → c991430` is linear.
>
> **The mathematics of the repair, re-derived independently.** Multiply the `n` step relations `3xᵢ + 1 = 2^{vᵢ}·x_{i+1}`; the shifted product is the same product, giving `∏(3xᵢ+1) = 2^K·∏xᵢ`. For positive integers `3x < 3x+1` factor by factor, and a product of `n` strict inequalities between positive terms is strict, so `3ⁿ·∏xᵢ = ∏(3xᵢ) < ∏(3xᵢ+1) = 2^K·∏xᵢ`; cancel `∏xᵢ > 0` and `3ⁿ < 2^K`. Every step is an identity or inequality between positive integers — no logarithm, no real number, no continued fraction, no size threshold — which is exactly why the theorem is unconditional and why discharging `hceil` downstream imports nothing. `n = p+1` throughout, the same `n` as the rest of this entry and as `cycles.md` 12.1.1; no index shift. Positivity is load-bearing rather than decorative: the three negative cycles are out of scope at the ℕ typing, and they are also exactly the cases where the conclusion is false (`3 > 2`, `9 > 8`, `2187 > 2048`). The canaries confirm the pin from the other side too: at 320 synthetic scales, `K₀ = bitlength(3ⁿ)` satisfies both halves and is the **unique** admissible `K`, with `K₀ − 1` failing the lower bound and `K₀ + 1` the upper at every one.
>
> **What sits outside this kernel key, stated as narrowly as the audit warrants.** Three things, and they are named rather than left to inference. (i) The **two continued-fraction glue facts** — that `convPairs` is exactly the list of convergent denominators in the window, and the classical bound `θ_j > 1/(q_j + q_{j+1})` — remain unformalized. Both are independently confirmed our side, at round 10 and again at round 11, but *confirmed is not kernel-proved*, and this entry's own honest-scope sentence already says so. (ii) **`LegendreApprox.lean` carries no `#print axioms` probe and no axiom-log entry at all.** Its "0 sorry, 0 axioms, 0 native_decide" is consistent by read and was re-verified this round; it is not traceable to a log. (The round-10 observation that the log header named a file with no entries is resolved at `c991430` by deleting the header rather than by adding the entries — a legitimate resolution, and see offers (a) and (c).) (iii) **Nothing here supports a claim that T1's chain is machine-checked end to end, and this key does not carry one.** The key belongs on the statements, the dependency structure, the logs and the mathematics — which is precisely what the ContentDescent key carries and precisely what is checked above.

### 3.3 L-A8 — the hygiene verification record

> **Macindoe verification record — the round-11 hygiene pass (2026-07-28).** Independent verification with fresh code (`experiments/merle_r11_hygiene_check.py`, **115 checks, 0 failures**), importing nothing from either Merle repository and nothing from any earlier check of ours; fixed-point big-integer logarithms built in-house at two working precisions with agreement asserted between them. **Everything reconciled and nothing failed.** The three previously scriptless outputs now have generator scripts, and all five relevant scripts — 043, 055, 056 and the repaired 052, 053 — were **run here** and reproduce their committed outputs byte-identically (in two of the five the only difference is one em-dash rendered by this machine's console codepage, an artefact of our redirect and not of the file). Every number was independently recomputed: `C₀ = −14.9487` under `c_gen` and `−14.9535` under `1/13`; the per-scale crossings `1596`/`1655` and the cumulative `1661`/`1722`; the exact window `35035491004` and the integral window `35031771147` with the loss `0.010617 %` — the same number round 10 carried as `0.011 %`, at two roundings and not a change; the 22 in-window convergents, the same 22 under either window; `5.1713×` tightest with the exact test `5.4433×`; `δ = 4.073367·10⁻²²`; and the best-approximation property exhaustively over all 190,536 values of `n < q₁₃ = 190537`. Two things worth stating plainly. **`5.17× at j = 21` is CORRECT** — the discharge margin recomputed at every one of the 22 convergents is tightest at `j = 21`, `q = 6586818670`, and the exact test is tightest at the same `j`. We queried that index; the query was ours and it was wrong, and the label is not stale. And the **`053` monotonicity argument is exhibited, not taken**: writing the test as `P_d(j) := [θ_j ≤ q_j·d]`, the right-hand side is increasing in `d`, so a smaller `δ` can only push the first admissible `j` later — valid, and needing no hypothesis about how `θ_j` or `q_j` behave. What it yields is `≥ 22`, not `= 22`; the equality is a separate computation, `θ₂₂/(q₂₂·δ_old) = 0.499018 < 1`, clearing the older and stricter test by a margin of only `2.0039×`. Had the slip been a factor 3 rather than a factor 2 the answer would have moved. **He ran that check** — his red team, named as such in the commit message — and it is correct. So "no result changed; only the reasoning became correct" holds, with that precision: the reasoning supplies the inequality and the computation supplies the equality. His claim (v) is confirmed on our side as well: no altered `θ_j`/`δ` figure is cited in the shared `LEDGER.md`, `NOTE.md` or `PROTOCOL.md`, or in any of our correspondence records. Artifact: `macindoe/collatz` `experiments/merle_r11_hygiene_check.py` with committed output (commit `38ccc49`, on `main`).

### 3.4 L-A8 — the one-sidedness sharpening, offered as a gift

> **A sharpening the repair buys, offered as a gift rather than a correction — and the sentence it tightens is ours, not his (2026-07-28).** Because `ceiling_lower` makes the positivity of the log gap a **theorem** rather than a threaded hypothesis, a positive cycle is confined to convergents lying *above* `log₂3`. Combined with the Legendre step's `n = t·q_m`, `K = t·p_m`, the gap is `K − n·log₂3 = −t·(q_m·log₂3 − p_m)`, so only the convergents on the upper side can host a north-shore configuration. Signed, and computed here from a continued fraction built from scratch at two precisions: `p₂₂/q₂₂ − log₂3 = −1.016341·10⁻²²` (below) and `p₂₃/q₂₃ − log₂3 = +9.427058·10⁻²⁴` (above). So the first scale admissible on the **north shore** is `q₂₃ = 137,528,045,312` — exactly Hercher's underlying threshold. **Nothing in the Lean chain depends on this**, since the closure runs on the window and `q₂₂` is already outside it, and it is not a discrepancy with anything he has written: his blocks state no two-sided figure. What it tightens is our own round-10 record, whose §(f) sentence gives the first admissible scale as `q₂₂ = 65470613321` — the answer to the *two-sided* test — without naming the shore. And it makes his own frame-prediction point land harder than he claimed it: the threshold that the frame predicts is not merely on the convergent grid, it is the first convergent the one-sided test admits, and it is Hercher's. Artifact as above (commit `dc8fde6`, on `main`).

### 3.5 L-A8 — the theorem hand-back

> **A theorem to hand back — the third face made exact (2026-07-28).** Verified on all four real cycles, both shores, agreeing to 45 digits in every case:
>
> > **Identity.** For a cycle of the odd map with `n` odd elements and `K = Σᵢ v₂(3xᵢ ± 1)`, the summed per-step drift equals the log-seam gap **exactly**: `Σᵢ log₂(1 + 1/(3xᵢ)) = K − n·log₂3` on the north shore, and `Σᵢ log₂(1 − 1/(3yᵢ)) = K − n·log₂3` on the south (`yᵢ = |xᵢ|`).
>
> Three lines: each step gives `3 + 1/xᵢ = 2^{vᵢ}·x_{i+1}/xᵢ`; multiplying around the cycle the `x`'s telescope and `Σ vᵢ = K`, so `∏(3 + 1/xᵢ) = 2^K`; subtract `n·log₂3`. Its right-hand side is `log₂(2^K/3ⁿ)` — precisely the quantity this chain's seam bound controls. So **"a third face of the same wall" is right, and stronger than he states it**: the per-step drift does not merely bound the seam gap, it sums to it exactly. Two corrections inside the same offer, both flat and neither touching the reading. First, "summed around a cycle that is exactly `n·δ`" is **not an identity** but a sharp upper bound: `D` is strictly decreasing, so for a cycle with all elements `≥ x_min`, `Σᵢ D(xᵢ) ≤ n·D(x_min)`, with equality **only** when every element sits at the minimum — which no cycle achieves (on `−17`: `Σ D = 0.188` against `n·D(x_min) = 0.396`). At `x_min = 2⁷¹` the two sides agree to 44 decimal places, which is presumably why it reads as exact. Second, what **is** exact is the constant identification:
>
> > `D(x_min) = δ·(1 + 1/(27·x_min²))`, where `δ = 2/(3·x_min·ln2)` is T1's own constant.
>
> Read the direction off the factor: `1 + 1/(27·x_min²) > 1`, so **`δ` sits strictly *below* the true per-step north–south drift at the minimum element**, by that relative `1/(27·x_min²)` — `6.643·10⁻⁴⁵` at `2⁷¹`. That is the honest statement of what `δ` is, and it is a reframing worth one sentence: the factor 2 in `δ` arrives in this entry's own derivation from a **crude step**, the two-bound `(m+1)ⁿ < 2mⁿ`, and in the drift reading it arrives from a **symmetry** — north and south contributing one unit each. Two mechanisms landing on the same 2; no number moves, but the constant becomes structure rather than slack. Finally, `x* = 7/3` is exact and unique (`D(x) = log₂(4/3) ⟺ 3(3x+1) = 4(3x−1) ⟺ 3x = 7`, one linear equation, one root), but the identity `log₂(4/3) = 2 − log₂3` that carries it is a tautology; the corollary with integer teeth is ours and he can have it: since `D` is strictly decreasing and `7/3` lies strictly between `1` and `3`, **`x = 1` is the only odd positive integer at which the sign information exceeds the drift** (`D(1) = 1` exactly, against `2 − log₂3 = 0.415`; `D(3) = log₂(5/4) = 0.322` is already below, and it falls from there). The `±1` matters more than the drift at exactly one odd integer, and that integer is the trivial cycle. Artifact as above (commit `38ccc49`, on `main`).

### 3.6 L-A8 — the seven offers, and the key-status line

> Offers, inside the entry per the co-edit style — all minor, all hygiene, acceptance is Merle's call:
>
> - *(offer a — the axiom-log headers.)* Both logs lost their header lines with the repair, and `T1Structure_axioms.txt` also lost the three compiler-warning lines it carried at `5c9b663`, so both are now curated lists rather than raw probe output. The cost is specific: the four-way verification claim ("0 `error:`, 0 stack overflow/abort, 0 `sorryAx`, 0 `native_decide`") no longer appears **in** an artifact, only in the letter and the commit messages. A one-line header on each log saying what it is and how it was produced would carry it, and keeping the raw output — warnings included — is what makes a log evidence of a run rather than a list.
> - *(offer b — two unprobed lemmas.)* `mul_pow_succ_le` and `pow_succ_lt_two_mul_pow` are the last two declarations in either file that the hardened protocol's fourth check does not reach directly. Both are transitively covered by their consumers' probes, so nothing mathematical hangs on it; two `#print axioms` lines would close it.
> - *(offer c — `LegendreApprox`.)* A probe and a log entry for its two theorems. This is the one file in the chain with no axiom-log line at all, and it is named as outside our key above for exactly that reason; two lines would move it inside.
> - *(offer d — whose slack the `1.700 bits` is.)* The `DeficitLemma.lean` SCOPE header's "minimum slack `1.700` bits at `n = 12`" still carries no clause saying which quantity that is the slack of. It is the **route-implied** bound's slack over `n/13`, which is the right quantity for the proof — not the true margin's, whose minimum is at `n = 1`. Offered at round 10 and simply still open; repeated here because the header was otherwise revised.
> - *(offer e — two `q₂₁` in the Lean comments.)* The subscript sweep reached the Python artifacts and the pin, and not the Lean source comments. `T1Structure.lean` at `c991430` carries **two different `q₂₁`** 245 lines apart: line 188, in the `seam_bound` docstring, has the shifted `q₂₁ = 6.547·10¹⁰` (and `q₂₂ = 1.375·10¹¹`), where the true labels on the pinned convention are `q₂₂ = 65470613321` and `q₂₃ = 137528045312`; line 433, in the discharge docstring, has the correct `q₂₁ = 6586818670`. In the same `seam_bound` docstring, line 186's `‖n·log₂3‖ ≤ n/(3X·ln2)` is the **pre-REQ-054 `δ`**, missing the factor 2 — everything downstream in the file uses the corrected constant, so this is one comment line. (At the lowest grade and recorded rather than pressed: the file header's "Legendre window `4.955e10`" is the withdrawn figure, defensible as a record of what REQ-052 computed at the time, though it reads as a current fact.) None of this touches a theorem statement, a proof, or any number entering the discharge.
> - *(offer f — Cor. 29's condition, recorded as promised.)* `X₀ ≥ 3·2⁶⁹`, named in his letter as the clause to add, has not landed: it appears nowhere in the Lean repository, the only `Cor. 29` mentions being the old REQ-001/004 headers without the condition. Recorded as promised-not-yet-landed and with no complaint — its natural home is ledger prose, and this ledger had not moved when the check was run.
> - *(offer g — and this one is different in kind, so it is marked as such.)* The same repair that cleaned `OUT_REQ-MATH-052.txt` **deleted its `(d-bis)` Ostrowski section** — the table carrying "median lowest denominator 15601, against 1 for controls" and the expansion `14936 = 22·665 + 306`. This entry's own seed block above cites exactly those two figures for the grid half. The committed `test_REQ-MATH-052` script does not produce that section (confirmed by running it here: its output is now byte-identical to the cleaned file), so the section came from an uncommitted script — the same two-runs-stitched-together pattern he identified himself in OUT-053, in the other file. **No figure is disputed and nothing about the grid half is called into question**; the claim may well be exactly right. The observation is only that a sentence already in this shared ledger now has no committed artifact behind it, and the remedy is the one he himself performed for 043, 055 and 056 three weeks into the same habit: commit the script that produced the table. Offered in that spirit and no other. (A smaller adjacent note so a `False` is never misread: the committed 052 script's own coarse grid test prints `tous ancres sur la grille ? False`, because its `near_grid` helper tries single-denominator anchoring only; the deleted `(d-bis)` table, which used the full Ostrowski expansion, is the stronger test and the one the ledger sentence rests on. No contradiction in substance.)
>
> **Kernel key status (2026-07-28): two keys on the kernel claims as well, scoped exactly as above.** The Macindoe key now turns on the statement match, the dependency structure (`hceil` verified gone, not taken), the committed axiom logs with their exact 13 → 15 reconciliation, the truth of every statement as instantiated (190 exact checks, 0 failures), and our own derivation of the repair — **read-not-built**, with the two continued-fraction glue facts and `LegendreApprox.lean`'s absent axiom-log entry explicitly outside it, and with no claim of end-to-end machine checking made or implied. The mathematics of every link carries its own two keys from round 10, unchanged. The model→certainty question is untouched: T1 removes one degree of freedom and excludes nothing by itself, exactly as the honest-scope paragraphs already say.

### 3.7 L-A3 (B) — the date-stamp appended to our own line

The Macindoe block's closing sentence is unchanged up to its final period, then
gains:

> *(Condition met, 2026-07-25: the asymptote constants are accepted in Merle's round-9 letter, point by point with the rest of that round's offers. **(B)'s quantification carries two keys** from that date. Date-stamped by Macindoe 2026-07-28; bookkeeping only — no claim, constant, artifact or attribution in this block changes, and this is our own line, not his.)*

---

## 4. Judgment calls

1. **The "K pinned" wording is his proposal, adopted — recorded here so the
   history is unambiguous.** The brief quotes his letter: *"My proposal, and it
   is only a proposal: the entry says the ceiling is pinned, cites
   `ceiling_pinned`, and notes that the lower half was found missing in your
   round-10 audit and proved afterwards. Your key on the kernel side belongs
   wherever you judge it belongs."* The block in §3.1 is written to that
   specification, element for element: it says the ceiling is pinned, it cites
   `ceiling_pinned` (and `ceiling_lower`, per the brief), and it names the
   round-10 finding and the round-11 repair **factually and without moral** —
   "Both facts are recorded because both are part of the entry's history;
   neither is stated as anything more than what happened." He deliberately left
   `LEDGER.md` untouched rather than restate his own claim after we caught it,
   and asked that the wording be settled together; **this is his wording,
   adopted, and typed in by us at his request** — the attribution line in the
   block says exactly that. His last sentence ("your key belongs wherever you
   judge it belongs") is honoured by keeping our key in its own separate block
   (§3.2) rather than folding it into his.
2. **His status header untouched.** L-A8's `DRAFT — one key (Merle: Lean kernel
   + scripts); Macindoe key invited.` stays exactly as he wrote it; our key
   state lives in the appended Key-status paragraph — the L-A4/L-A6/L-A7
   precedent. Header updates are his edit to make.
3. **The L-A3 date-stamp is an edit to our own paragraph**, executed as a pure
   append (nothing deleted), producing the commit's one modified line. The same
   reading as round 9's judgment call 2 and round 10's judgment call 2.
4. **Every record pins its own artifact**, per the round-10 consistency call
   (judgment call 6 there). Four citations across two commits; the pin list and
   its resolve check are §0.
5. **The one-sidedness figures were verified before use, because they are
   brief-only.** `−1.016·10⁻²²` and `+9.427·10⁻²⁴` appear in
   `briefs/merle-round11-coedit-brief.md` and in **no findings file** — the
   ceiling-audit findings establish the *shores* (`q₂₂` below, `q₂₃` above) but
   print no signed figure. Rather than carry an unsourced number into the
   shared ledger, they were recomputed here from a continued fraction built
   from scratch, at working precisions 200 and 300 digits, with the two
   precisions agreeing to every printed digit: `p₂₂/q₂₂ − log₂3 =
   −1.016341·10⁻²²`, `p₂₃/q₂₃ − log₂3 = +9.427058·10⁻²⁴`. The convergent list
   reproduced matches `briefs/merle-r11-hygiene-check-findings.md` §2.0 exactly
   (`q₁₃ = 190537`, `q₂₁ = 6586818670`, `q₂₂ = 65470613321`,
   `q₂₃ = 137528045312`), and the sign alternation is the expected one (even
   `j` below `log₂3`, odd `j` above). The ledger carries the six-digit forms.
6. **The drift/`δ` direction, checked character by character before writing.**
   The formula is `D(x_min) = δ·(1 + 1/(27·x_min²))`. Since
   `1 + 1/(27·x_min²) > 1`, it says `D(x_min) > δ` — **`δ` sits strictly BELOW
   the true per-step drift at the minimum element.** That is the direction
   written into the ledger, and the block states it twice: once as the formula
   and once in words ("`δ` sits strictly *below* the true per-step north–south
   drift at the minimum element"), with the relative size `1/(27·x_min²)` =
   `6.643·10⁻⁴⁵` at `2⁷¹`. Checked against
   `briefs/merle-r11-hygiene-check-findings.md`, which has it right in three
   places — §8.1 ("`D` is *above* it, by a relative `1/(27x²)`"), §8.2
   (`Σᵢ D(xᵢ) ≤ n·D(X) = n·δ·(1 + 1/(27X²))`, and `D(x_min)/δ = 1 + 6.64·10⁻⁴⁵`)
   and §8.4 (`D(X) = δ·(1 + 1/(27X²))`). The brief flags that this was written
   backwards once this round in a findings summary and corrected at merge; the
   version written here is the corrected one.
7. **Stack SHAs, not shared-repo SHAs.** Where a block points at one of his
   commits it names the **Lean stack** SHA (`5c9b663`, `6c084c5`, `c991430`,
   `41fa4f8`, `da2c8db`), never a shared-repo SHA — a ledger reader can resolve
   the former from the entry itself. The one exception is by construction: our
   own artifact pins name commits on `macindoe/collatz` `main`, in the shape
   the existing records use.
8. **The `1.700 bits` offer is a DeficitLemma/L-A7 item carried in L-A8's offer
   list**, because it arrives from the round-11 ceiling audit (which covers
   both files) and because the header was otherwise revised this round. It is
   labelled as the `DeficitLemma.lean` SCOPE header's clause so nobody reads it
   as an L-A8 figure, and it is named as already offered at round 10 and still
   open — not as a new finding.
9. **Nothing about the Junction repositories is in this commit.** It is reply
   material, as at round 10, and the sibling session
   `merle-round11-reply` owns it.
10. **Nothing about the joint note is in this commit** — neither its
    contribution sentence (the author's own, Merle having asked him directly)
    nor any of the premise pre-check's findings.
11. **The register on offer (g).** It is marked as different in kind, exactly
    as the brief asks, because it is the one item where a sentence *already in
    the shared ledger* lost its artifact. It is written flat, states twice that
    no figure is disputed, and frames the remedy as the same good habit he
    himself practised on 043/055/056 — not as a lapse. No moral anywhere.

---

## 5. What was deliberately NOT done

**No ledger entry was created for his δ8 impossibility, and that was a
deliberate abstention.** `briefs/jointnote-premise-external-findings.md` §4.2
records that Face I's Merle half — the δ8 impossibility, which Face I rests on
— has **no ledger entry at all**: `LEDGER.md` at `c966875` contains zero
occurrences of "Product", "Product-Bound", "δ8", "delta8" or "scissors", though
the claim lives in the shared `README.md`'s scope sentence and in `NOTE.md` §2
and §6, and though the note header's own rule is that every numbered claim
enters via `LEDGER.md` first. **That entry is his to seed, not ours**, and the
observation is reply material. This session read the finding, confirmed the
absence in the clone, and wrote nothing. No entry, no stub, no placeholder, no
cross-reference.

Two adjacent facts from the same findings file were likewise left alone as
reply material and not written into the ledger: that L1 — the entry `NOTE.md`
§2 actually cites — carries the status word `corrected` rather than `two keys`,
and that `L-A5`…`L-A8` are cited nowhere in `NOTE.md`, L-A8 included. The one
item from that file that *is* actioned here is the L-A3 (B) bookkeeping gap
(§3.7), because that is our own line and its fix is ours to make.

---

## 6. Flags

1. **Pre-push condition (§0):** both artifact pins — `dc8fde6` and `38ccc49`,
   four citations — fail to resolve on public wiki `main`, which is at
   `2225b68` at this session's `ls-remote`. **The author's wiki-main push to
   `185c622` or later (`9fdaa0f` current) must accompany or precede the
   shared-repo push**, or all four dangle. Caught at rounds 9 and 10 for the
   same reason.
2. **Patch line endings, minor, and the same note as round 10.** The archived
   patch is generated with LF and is checked out with CRLF on this machine
   (`core.autocrlf=true` globally). `git am` strips trailing CRs by default
   (`am.keepCr` unset), so it applies cleanly either way; the authoritative
   apply path is a fresh clone with `core.autocrlf` set `false`, which is how
   the verification in §2 was performed.
3. **The commit SHA restamps on re-apply.** `2f724d1` is this session's clone;
   applying the patch fresh gives `b6aaa67`. **The tree `5c0ccbf` is the object
   to check**, and it is identical either way. If the push is made by applying
   the patch rather than by pushing this branch, the SHA to cite afterwards is
   the one that lands — the round-10 precedent (`5481d2d` prepared, `c966875`
   pushed).
4. **No handbacks, and no stop condition triggered.** The shared HEAD was
   `c966875` at both checks. No discrepancy of digits, SHAs, statements or
   citations was found between the prepared blocks and the round's five
   findings files. Where the brief and a findings file could have diverged, the
   findings file was taken as the authority — see judgment calls 5 and 6, which
   are the two places that mattered this round.

---

## 7. Encoding

`experiments/encoding_scan.py` run over the tracked tree before the final
commit of this branch — result recorded in the commit message of the last
commit. Independently, the edited shared-repo `LEDGER.md` was checked
byte-level: valid UTF-8, no BOM, 0 CR bytes, terminating newline present, and
**no** double-encoding signature for any of the characters these files use
(`—`, `≤`, `≥`, `ε`, `β`, `δ`, `·`, `×`, `⌈`, `∏`). All edits made with the
Edit tool; PowerShell `Get-Content`/`Set-Content` was not used on any file this
session, tracked or untracked.

---

## 8. What the main session does next

1. **Review**: verify the patch applies clean and tree-identical on a pristine
   `c966875` (tree `5c0ccbf`), confirm the 44/1 counts and that the single
   deletion is the pure-append L-A3 line, and re-check the shared HEAD unmoved.
2. **Merge** this branch (this session does not merge).
3. **Author pushes wiki `main`** (≥ `185c622`, i.e. `9fdaa0f` or later,
   including whatever this branch adds) so both artifact pins resolve publicly.
4. On the author's go-ahead, and only then: push from the scratchpad clone
   (`scratchpad/r11/shared`, branch `round11-coedit` → `main`, fast-forward
   over `c966875`), or `git am` the archived patch onto a fresh clone if the
   scratchpad has been cleaned. If the shared repo has moved past `c966875` by
   then, re-seat first (the round-8 precedent).
5. The round-11 reply is a **parallel session** with its own brief; this
   session makes no claim on it, and the δ8 ledger observation of §5 belongs
   there.
