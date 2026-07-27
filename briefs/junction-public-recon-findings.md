# The Junction stack, now public — completing the round-10 recon

Brief: `briefs/junction-public-recon-brief.md`. Branch `junction-public-recon`,
base **`e938040`** (the worktree was cut at the session-start `2225b68`, which
does not contain the brief; it was rebased onto `e938040` before any work
started, per the launch instruction).

This session completes `briefs/junction-repo-recon-findings.md`, every entry of
which was recorded NOT FOUND (repository inaccessible). Four repositories are
now public and were read at first hand.

**Recon only.** No proof is graded, no key is turned, no ledger or reply text is
written here.

## Interaction record — none occurred

All access was by **unauthenticated read-only `git clone`** into the session
scratchpad, plus read-only `gh api` calls against public endpoints. There was
**no fork, no issue, no pull request, no comment, no star, no watch, no follow,
no release download, no push, no write of any kind** against any repository of
his, and no contact with anyone. Nothing this session did appears in his
notifications or event stream.

**`Projet_Collatz` was not touched.** It stays private by his decision. It was
not requested, no invitation was sought or accepted, and no route to it was
attempted. It is named once below only because his own `docs/LINEAGE.md` names
it in a timeline we had to read for other reasons; its absence is not treated
as a gap anywhere in this record.

## Outcome in one line

The four repositories are public and readable, and **almost every described
point is now found** — but distributed across two of them rather than one, and
dated **March–April 2026**, before this correspondence, not after it. Two
described artifacts are not present anywhere in the four: a file named
`AUDIT_V9`, and a file named `STATUS.md`. One described remediation — the range
beyond `k = 50000` marked **OPEN** — is not present and its document still reads
**PROVED**. Everything else checks out, some of it verbatim.

---

## Item 1 — public status, HEADs, licences

Handle `ericmerle3789`, enumerated 2026-07-28. `gh api users/ericmerle3789`
reports `"public_repos": 7` (round 10 recorded 3). The four named in his letter
are all public, none archived at the GitHub-flag level, all default branch
`main`, all cloned successfully without authentication:

| Repository | HEAD | HEAD date | Commits on `main` | Branches | Tags | Licence file(s) |
|---|---|---|---|---|---|---|
| `Collatz-Junction-Theorem` | `a57d29e7c062e6c614ebca4dc0875f70065561a9` | 2026-04-22 19:20:46 +0200 | 232 | 3 (`main`, `proof-assembly-v1`, `syracuse-jepa-v2`) | 0 | `LICENSE` (MIT), `LICENSE-PAPER` (CC-BY 4.0) |
| `collatz-cycles-lean` | `1d771681fa1addf7429779cc5cddd48719dbdd8d` | 2026-04-22 19:21:16 +0200 | 7 | 1 | 0 | `LICENSE`, headed *"MIT License (code) / CC BY 4.0 (paper)"* |
| `collatz-nocycle-lean4` | `4ec239deeea642315fcb431ca0d22a09727911f3` | 2026-04-22 22:18:16 +0200 | 31 | 6 | 1 (`paper-v1-draft`) | `LICENSE` (MIT) |
| `collatz-audit-2026` | `eb237b39e17700f07d76ca53e6d18988cf7d5ba6` | 2026-07-26 21:25:49 +0200 | 9 | 1 | 0 | `LICENSE` (MIT) |

**His licence account checks out, in every particular.**

- MIT on code, CC-BY 4.0 on papers where he says so: `Collatz-Junction-Theorem`
  carries two files, `LICENSE` = MIT and `LICENSE-PAPER` = *"Creative Commons
  Attribution 4.0 International License (CC-BY 4.0) … This work (the
  mathematical preprint and associated documentation in the paper/ directory)"*.
  `collatz-cycles-lean` carries one file doing both jobs, MIT body with a
  closing line *"The paper (paper/) is licensed under Creative Commons
  Attribution 4.0 International (CC BY 4.0)."*
- **Which repository had no licence at all: `collatz-audit-2026`**, and the
  licence commit is dated **at the flip**. It is the repository's HEAD,
  `eb237b3`, 2026-07-26 21:25:49 +0200, message *"Add MIT licence before making
  the repository public."*, body: *"Without a licence, published code is 'all
  rights reserved' and cannot be legally reused or formalised by anyone — which
  defeats the reason for publishing it. MIT matches the other Collatz stacks
  (Junction, cycles-lean, nocycle-lean4)."* It is the only commit anywhere in
  the four repositories dated later than 2026-04-25.
- The other three licences long predate the flip and sit at or near each
  repository's first release: Junction `LICENSE` at `0295599` (2026-02-25,
  initial release) with `LICENSE-PAPER` added at `0613510` (2026-03-01);
  `collatz-cycles-lean` at `93c64ee` (2026-03-26, initial release);
  `collatz-nocycle-lean4` at `a55f119` (2026-02-22, first commit).

**"Last pushed 22 April" for `Collatz-Junction-Theorem`: correct.** GitHub
reports `pushed_at = 2026-04-22T17:20:48Z`; the HEAD commit is dated
2026-04-22 17:20:46 UTC. `collatz-cycles-lean` matches the same day
(`2026-04-22T17:21:17Z`); `collatz-nocycle-lean4` was last pushed
2026-04-25T12:05:11Z.

**One flat observation on dating the flip.** The public event stream returns a
`PublicEvent` for each of the four, but each carries a timestamp equal to that
repository's own `created_at` (2026-02-22, 2026-02-25, 2026-03-26, 2026-03-31),
not a July date. The event stream therefore does not date the flip either way.
What does date it is the `collatz-audit-2026` licence commit above, whose
message states the intent explicitly, and his letter. Recorded so nobody later
reads the February dates as contradicting him — they do not; they are creation
dates.

---

## Item 2 — the self-audit, read at first hand

### 2.1 `AUDIT_V9` — not present

**No file, directory, or commit named or containing `AUDIT_V9` exists in any
ref of any of the four repositories.** Searched: every branch of each (3 + 1 +
6 + 1 refs), by working-tree `find`, by `git log --all --diff-filter=A
--name-only`, and by `git log --all -S"AUDIT_V9"` (pickaxe over all history).
Zero hits.

The audit series it belongs to is public and stops at **V8**.
`Collatz-Junction-Theorem/audits/` holds `AUDIT_V1_CERTIFICATION.md`,
`AUDIT_V2_CERTIFICATION.md`, `AUDIT_V3_CERTIFICATION.md`,
`AUDIT_V4_MATHEMATIQUE.md` (all added at `9afe0c1`, 2026-02-27) and
`AUDIT_V8_RESULTS.md` (added at `6a7df1a`, 2026-03-07, commit message *"audit:
V8 Red Team + corrections + repo cleanup"*). No V5, V6, V7 or V9 anywhere.

`AUDIT_V8_RESULTS.md` is worth recording because its verdict is the same shape
as the one he described, three months earlier. Header and verdict, verbatim:

> `**Date** : 2026-03-07`
> `**Auditeur** : Claude Opus 4.6 (Red Team adversarial)`
> `**Objectif** : Audit le plus strict possible — essayer de « casser » le papier.`
>
> `LE SQUELETTE STRUCTURAL TIENT.`
> `LE RÉSULTAT CONDITIONNEL (GRH) A DES BRÈCHES.`
> `L'ABSTRACT SURAFFIRME.`
>
> `**Classification** :`
> `- Résultat inconditionnel (Junction Theorem) : **SOLIDE** ✅`
> `- Résultat conditionnel (Blocking + GRH) : **FISSURÉ** ⚠️`
> `- Présentation (abstract, comptages) : **INCORRECTE** ❌`

*"L'abstract suraffirme"* — the presentation overclaims while the structural
skeleton holds — is his own sentence *"the mathematics inside was sound; the
shop window was ahead of the shop"* in another language. **This is recorded as
a resemblance, not as an identification.** `AUDIT_V9` is not here, and this file
is not it.

### 2.2 `STATUS.md` — not present; the role is filled by a differently named file

**No `STATUS.md` in any ref of any of the four repositories** (same sweep as
above). The document that does the job he describes — the status page rewritten
to match the technical documents — is **`collatz-cycles-lean/VERIFICATION.md`**,
rewritten in the same commit as the README (`1a56828`). Its two tables, verbatim
and in full:

> `## What is proved`
>
> `| N₀(d) = 0 for k = 3..15 | **PROVED** (Lean, 0 sorry) | lean/verified/, lake build |`
> `| Steiner's equation | **PROVED** (Lean) | lean/skeleton/JunctionTheorem.lean, steiner_equation |`
> `| Nonsurjectivity k ≥ 18 | **PROVED** (Lean) | lean/skeleton/, crystal_nonsurjectivity |`
> `| No cycle k ≤ 91 | **PROVED** (external) | Hercher (2025), J. Integer Seq. |`
> `| Spectral gap ρ_p < 1 | **PROVED** (Wielandt) | scripts/spectral_analysis.py |`
>
> `## What is NOT proved`
>
> `| N₀(d) = 0 for k > 15 | **OPEN** | Lean verified stops at k=15 |`
> `| Range Exclusion k=3..10000 | **INVALID** | lean/range-exclusion/ uses wrong corrsum formula |`
> `| Baker argument k ≥ 10001 | **INVALID** | Applies to wrong function |`
> `| N₀(d) = 0 for all k | **OPEN** | Gap between nonsurjectivity and N₀=0 |`

That is an unusually clean status page: it marks its own headline module
**INVALID** by name and its own asymptotic argument **INVALID**, and leaves the
general claim **OPEN**.

### 2.3 The README overclaim, and the rewrite — both found, in `collatz-cycles-lean`

The overclaim is **not** in `Collatz-Junction-Theorem`. That repository's README
has said *"Conditional on GRH"* since its first substantive version and says
*"Theorem (Conditional on GRH + Conjecture 7.4)"* today; its earliest README
(`0295599`, 2026-02-25) is headed *"Entropic Barriers and Nonsurjectivity"* and
already frames the residual question as a hypothesis. There is no unconditional
no-cycles headline in its history to have been corrected. (One overclaim *was*
corrected there, a different one: the row `Im_int ×2-closed` moved from status
`Unconditional` to `**Open conjecture**`, and the README now records that
exhaustive computation for `k = 7..20` shows the claim is *"in fact **false as
stated**"*. Commits `01a5e1c` *"fix: correct logical errors and overclaims in
preprint"* and `7eaa373` *"docs: rewrite README to match current repo state"*,
both 2026-03-07, the day after AUDIT V8.)

The overclaim he describes is in **`collatz-cycles-lean`**, and it is exactly as
he described it. Its first README (`93c64ee`, 2026-03-26) says, verbatim:

> `## Result`
>
> `For every k ≥ 1, the accelerated Collatz map T(n) = (3n+1)/2^{v₂(3n+1)} admits no nontrivial positive cycle of length k.`
>
> `## Proof architecture`
>
> `| k = 3..10000 | Range Exclusion verified by Lean native_decide | lean/range-exclusion/ |`
> `| k ≥ 10001 | Baker–Wüstholz (1993) lower bound on linear forms in logarithms | Section 5 |`
>
> `The sole external dependency beyond the Lean kernel is the Baker–Wüstholz theorem, a published result.`

That is an unconditional no-cycles claim for all `k`, resting on a Lean module
and one published theorem.

**The rewrite is commit `1a56828`** (2026-03-26, seven hours after the initial
release), message verbatim:

> `CRITICAL: Fix corrsum formula, reduce claim to what is actually proved`
>
> `The corrsum formula in the article (eq.3) used tail sums instead of`
> `cumulative positions. The correct Steiner formula is:`
> `  corrsum = Σ 3^{k-1-i} · 2^{P_i}  with P_i = g_1+...+g_i, P_0=0`
>
> `This matches lean/verified/ (corrSumList) and lean/skeleton/ (steiner_equation).`
> `The lean/range-exclusion/ module uses a DIFFERENT formula (gap values via`
> `enumMonotone) — this is now documented with a WARNING.`
>
> `Claim reduced to what is actually proved:`
> `  - N₀(d)=0 for k=3..15: Lean verified, correct formula, 0 sorry`
> `  - Nonsurjectivity for k≥18: Lean skeleton`
> `  - No cycle k≤91: Hercher (2025)`
> `  - The gap N₀(d)=0 for k>91: OPEN (honestly stated)`

and the README's `## Result` section after it, verbatim:

> `N₀(d(k)) = 0 (no composition achieves corrsum ≡ 0 mod d) is established:`
> `- For k = 3..15 by Lean 4 certified computation (0 sorry, 0 axiom)`
> `- For k ≤ 91 by Hercher (2025), independently`
> `- For k ≥ 18, nonsurjectivity C(S−1,k−1) < d is proved (Lean skeleton)`

**Verdict on the rewrite: it does what he says it does.** The unconditional
headline is gone; what replaces it is a three-line statement each clause of
which is supported by a named artifact in the same repository. The scope banner
was added later (`1d77168`, 2026-04-22), and it goes further than described — it
tells readers by name not to cite the broken module:

> `⚠️ Repository archived 2026-04-22 — historical reference only.`
> `## ⚠️ Known formula error — do NOT cite the lean/range-exclusion/ module`
> `- ❌ Do NOT copy, cite, or re-use any theorem from lean/range-exclusion/.`
> `- ❌ Do NOT treat the range-exclusion/ results as valid Collatz cycle non-existence proofs.`

### 2.4 Does the current README match what the technical documents support?

For `collatz-cycles-lean`'s README and `VERIFICATION.md`: **yes**, and they are
mutually consistent. Both name the same four supported claims and the same
invalid module.

**One finding, delivered flat.** The rewrite of 2026-03-26 touched
`README.md`, `VERIFICATION.md`, `docs/AUDIT_CORRSUM.md`,
`lean/range-exclusion/WARNING.md` and the paper. It did **not** touch
`docs/PROOF_ASSEMBLY.md`, which was added in the same day's earlier commit
`8fdfb20` and **has never been modified since**. At HEAD, that document still
carries the withdrawn claim in its own headline:

> `## $N_0(d(k)) = 0$ for all $k \geq 3$, $k \neq 4$`
>
> `**Status:** **COMPLETE.** Path A (Range Exclusion + Baker–LMN) proves $N_0(d(k)) = 0$ unconditionally for all $k \geq 3$, $k \neq 4$.`

and, in §10.6, the table and sentence:

> `| $k = 6, \ldots, 10000$ | **PROVED** | Range Exclusion (Lean native_decide, 9995/9995 pass) |`
> `| $k = 10001, \ldots, 50000$ | **PROVED** | Range Exclusion (Python exact arithmetic, 39995/39995 pass) |`
> `| $k > 50000$ | **PROVED** | Baker–LMN: range $< d$ (condition A), $d \nmid (3^k-1)$ (condition B) |`
>
> `**No gap remains. The proof is unconditional for all $k \geq 3$.**`

Every line of that is about **Range Exclusion** — the module his own README,
`VERIFICATION.md`, `WARNING.md` and `AUDIT_CORRSUM.md` all mark as computing the
wrong function. So the repository at HEAD contains, side by side, a status page
marking the Baker argument INVALID and a proof-assembly document declaring the
same argument complete and unconditional. A reader who opens `docs/` before
`VERIFICATION.md` meets the withdrawn claim first. This is a one-file loose end
from an otherwise thorough retraction, and it is the same *kind* of thing his
self-audit was about — recorded here so the reply can mention it if the author
wants to, not as a charge.

### 2.5 The described "two asymptotic programs, each with a named unclosed gap beyond `k = 200`" — confirmed verbatim

Same document, `collatz-cycles-lean/docs/PROOF_ASSEMBLY.md` §2, verbatim:

> `## 2. Proof Architecture`
>
> `Two independent proof paths establish $N_0(d(k)) = 0$ for all $k \geq 3$.`
>
> `| Path | Method | Finite range | Asymptotic regime | Gap |`
> `| **A — Range Exclusion** | corrSum confined to narrow interval; $d$ too large to divide any value | $k = 3, \ldots, 200$ (PROVED) | $k > 200$: exponential convergence $\text{range}/d = O(3^{-0.415k})$ | Effective Diophantine constants |`
> `| **B — FCQ/Junction** | Prime-by-prime spectral contraction: $\rho_p < 1$ for all $p \geq 5$ | $k = 3, \ldots, 200$ (PROVED) | $k > 200$: $k_{\min}(p) = O(\log p)$ | Multiplicative order control for factors of $d(k)$ |`

Two programs, finite range to `k = 200` each, and a named gap each beyond it —
exactly as described, in the document he said says something weaker than the
README did. That the *same file* later declares Path A's gap closed (§6.1
*"the asymptotic gap has been **closed unconditionally**"*) is the tension
recorded in 2.4.

### 2.6 The preprint's `k ≥ 69` clause — confirmed verbatim

`Collatz-Junction-Theorem/paper/preprint_en.tex`, Remark
`rem:junction-scope`, verbatim:

> `Complete cycle exclusion for $k \geq 69$ requires`
> `the additional Hypothesis~\textup{(H)}---namely that`
> `residue~$0$ is among those omitted by~$\Ev_d$.`

and, immediately before it, the honest scope sentence:

> `Obstruction~(b) is \emph{structural}: it proves that`
> `$\Ev_d$ omits at least one residue modulo~$d$, but does`
> `not identify \emph{which} residue is omitted`
> `\ldots In particular, nonsurjectivity alone does not exclude`
> `cycles.`

### 2.7 The repository checked as we check any artifact

By read, at HEAD, in the two Junction-family repositories:

| | `Collatz-Junction-Theorem` | `collatz-cycles-lean` |
|---|---|---|
| `sorry` (real, non-comment) | **0** | **0** |
| `axiom` declarations | **2** | **4** |
| `native_decide` occurrences | 1062 across 11 files | 1144 across 13 files |

Every string `sorry` in either repository is inside a docstring or a comment,
including several stale ones (`JunctionTheorem.lean` line 670 still says
`→ AsymptoticBound (2 sorry's)` in a table whose own header two lines earlier
says `0 sorry remaining`).

**The two `axiom` declarations in `Collatz-Junction-Theorem`**, both in
`lean/skeleton/`, quoted:

> `/-- **Simons–de Weger theorem** (2005). No positive cycle with k < 68.`
> `Accepted as axiom (published Acta Arithmetica 117, independently verified). -/`
> `axiom simons_de_weger :`
> `    ∀ k : ℕ, k ≥ 1 → k < 68 →`
> `    ¬ ∃ (n₀ S : ℕ) (A : Fin k → ℕ),`
> `      n₀ > 0 ∧ crystalModule S k > 0 ∧`
> `      (n₀ : ℤ) * crystalModule S k = ↑(corrSum k A)`

> `axiom small_gap_crystal_bound (k S : ℕ) (hk : k ≥ 666) … :`
> `    Nat.choose (S - 1) (k - 1) < (Collatz.FiniteCases.crystalModule S k).toNat`

whose docstring states its own reason: *"**Why axiom**: The CF lower bound
`|ξ - p_n/q_n| > 1/(q_n·(q_{n+1}+q_n))` is standard number theory (Hardy &
Wright §10.8) but not yet formalized in Mathlib."*

So **Simons–de Weger does genuinely appear as an `axiom` declaration**, as he
said — this was the question round 10 recorded as NOT VERIFIABLE. The second
axiom is the continued-fraction bound, which the README also names
(*"Axiom 2: continued fraction lower bound for convergents of log₂3 (Hardy &
Wright §10.8)"*).

`collatz-cycles-lean` carries the same two (identical files) **plus two more**
in the module marked invalid, of which one is worth naming because it assumes
its own conclusion for the whole asymptotic range:

> `axiom baker_lmn (k : Nat) (hk : k ≥ 10001) : checkRE k = true`
> `axiom simons_de_weger (k : Nat) (hk : 1 ≤ k) (hlt : k < 68) : …`

**The described caveats, resolved.** His round-10 description of the deficit
lemma's home was *"`native_decide`, two `sorry`s in the asymptotic assembly,
Simons–de Weger as an axiom"*.
`native_decide` — confirmed and then some (648 cases for `k ∈ [18, 665]` per the
README, `FiniteCases*.lean`).
Simons–de Weger as an axiom — confirmed, quoted above.
The two `sorry`s in the asymptotic assembly — **they were there and are not
now**: commit `97de5ec` (2026-03-07) is *"feat: Lean4 k≤665 computationally
verified + AsymptoticBound (2 sorry's remaining)"* and `c2bedb6` the same day is
*"feat: skeleton 0 sorry — asymptotic bound via Legendre + CF axiom"*. They were
discharged by introducing `small_gap_crystal_bound`, i.e. converted from
`sorry` to axiom rather than proved. Recorded flat: his description is accurate
about a state the repository was in, and the current state substitutes an
explicit axiom for the two holes.

**What the claims say vs what the artifacts support**, in one line each:
`lean/verified/` (280 theorems, Lean 4.15, no Mathlib) claims 0 `sorry`,
0 `axiom` — holds by read.
`lean/skeleton/` claims *"~38 theorems, **0 sorry**, 2 axioms (published
external results)"* — holds by read, with the note that
`small_gap_crystal_bound` is not a published external result but an
unformalized-in-Mathlib standard fact, which the README's own axiom list does
say (*"Hardy & Wright §10.8"*).
Neither claim was built: **read, not built** — there is no Lean toolchain in
this session, and no `#print axioms` log is committed in either repository.

### 2.8 Resolution of every round-10 NOT FOUND entry

| Described point (round 10) | Round-10 verdict | Now | Where |
|---|---|---|---|
| README claimed an **unconditional** proof of no cycles for all `k` | NOT FOUND (inaccessible) | **CONFIRMED**, verbatim | `collatz-cycles-lean` README at `93c64ee` (2026-03-26) |
| Technical document says two asymptotic programs, each with a named unclosed gap beyond `k = 200` | NOT FOUND | **CONFIRMED**, verbatim | `collatz-cycles-lean/docs/PROOF_ASSEMBLY.md` §2 |
| Preprint states complete exclusion needs an extra hypothesis for `k ≥ 69` | NOT FOUND | **CONFIRMED**, verbatim | `Collatz-Junction-Theorem/paper/preprint_en.tex`, `rem:junction-scope` |
| README rewritten to match the technical documents | NOT FOUND | **CONFIRMED** | `collatz-cycles-lean` `1a56828` (2026-03-26) |
| STATUS rewritten | NOT FOUND — no `STATUS.md` | **CONFIRMED in substance, NOT in name**: no `STATUS.md` exists in any ref of any of the four; the rewritten status page is `collatz-cycles-lean/VERIFICATION.md`, rewritten in the same commit | — |
| Scope banner added | NOT FOUND | **CONFIRMED, and stronger than described** | `collatz-cycles-lean` and `Collatz-Junction-Theorem` READMEs, `1d77168` / `a57d29e` (2026-04-22) |
| `native_decide` reliance flagged (compiler-trusted, not kernel-trusted) | NOT FOUND for the described repo | **PARTIAL**: the explicit `Lean.ofReduceBool` / `Lean.trustCompiler` flag exists in `collatz-nocycle-lean4` (`expected_axioms.md`, `docs/BIBLE/LIMITATIONS.md`, `RISK_REGISTER.md` R-05/R-10). In the two repositories where the 648-case `native_decide` block actually lives there is **no such flag** — the nearest is one cell of the Junction archive banner, which is about the *active* repo and is forward-looking (*"will be added in Phase Legendre"*) | — |
| Range beyond `k = 50000` marked **OPEN** | NOT FOUND | **NOT FOUND — and the document says the opposite.** `PROOF_ASSEMBLY.md` §10.6 marks `k > 50000` **PROVED**, at HEAD. `k = 50000` occurs nowhere else in any of the four in this sense | — |
| Plain-words statement that the repository does **not** prove the Collatz conjecture | NOT FOUND for the described repo | **CONFIRMED in `collatz-nocycle-lean4` only** — README §*"What This Does NOT Prove"*: *"This does **NOT** prove the full Collatz conjecture … This proves **ONLY** the anti-cycle part, conditional on 3 published hypotheses"*, plus `paper/sections/05-hypotheses.tex` §*"What the formal theorem does not prove."* **NOT present** in `Collatz-Junction-Theorem`, `collatz-cycles-lean`, or `collatz-audit-2026` | — |
| Audit record committed as `AUDIT_V9` | NOT FOUND | **NOT FOUND.** No such file or commit in any ref of any of the four; the public audit series stops at V8 (2026-03-07) | — |
| *"The mathematics inside was sound; the shop window was ahead of the shop."* | not a repository artifact | still not a repository artifact; the nearest committed text is AUDIT V8's *"le squelette structural tient … l'abstract suraffirme"* | — |

**The one thing this table cannot resolve is timing, and it should be said
plainly.** Every confirmed remediation above is dated **March or April 2026**.
The only commit anywhere in the four repositories after 2026-04-25 is the
`collatz-audit-2026` licence. So the remediations he described are real,
findable, and in several places verbatim — but they are not visible as work
done in response to this correspondence, because no such commits exist in the
public repositories. Two readings fit equally well and neither is adjudicated
here: the audit he described may be the **April 2026 adversarial audit** whose
apparatus is fully committed in `collatz-nocycle-lean4/docs/BIBLE/`
(`signoffs/G0`–`G3`, `redteam/2026-04-22-*`, `RISK_REGISTER.md`,
`LIMITATIONS.md`, `postmortems/2026-04-22-G3.11-procedural-debt.md`, and
`docs/LINEAGE.md`'s *"the April 2026 adversarial audit … Signal #1 of the
2026-04-21 audit"*), which he then recounted to us; or `AUDIT_V9` may live
somewhere we have not looked and are not going to. **Absence of an `AUDIT_V9`
in the four public repositories is not evidence that it does not exist**, and
the round-10 posture — absence of a public copy is not evidence against his
account — carries over unchanged to this one file.

---

## Item 3 — `LegendreApprox.lean`: the diff, performed

Round 10 recorded **NOT PERFORMED** because no counterpart existed to diff
against. Both counterparts now exist and are public.

**Three copies, two blobs.**

| Copy | Path | git blob | SHA-256 of file | Entered at | Unchanged since |
|---|---|---|---|---|---|
| Junction | `Collatz-Junction-Theorem` `lean/skeleton/LegendreApprox.lean` | `a4fae1f9606cbb2ec4cc2a6da7e6e786881c7adf` | `6beec7b45105854cc27c1cf1380b5156b6af34563426fe812f4818de0230bdda` | `09f481b`, **2026-02-26** (as `lean/LegendreApprox.lean`; moved to `lean/skeleton/` at `9afe0c1`, 2026-02-27) | byte-identical from `09f481b` to HEAD |
| cycles-lean | `collatz-cycles-lean` `lean/skeleton/LegendreApprox.lean` | `a4fae1f9606cbb2ec4cc2a6da7e6e786881c7adf` | same as above | `93c64ee`, 2026-03-26 (initial release) | byte-identical since |
| T1 chain | `one-obstruction-three-faces-lean` `OneObstruction/LegendreApprox.lean` | `b55095ac13eeafdf759d7d28b997a175e56e6392` | `a1d7e0abd5fb6089e17569efa78f771111a0d871f8b2e69d47c330eac9d43c1e` | `da2c8db`, 2026-07-25 | byte-identical at `da2c8db`, `5c9b663` **and at current HEAD `c991430`** |

**Upstream by commit date: the Junction copy**, by five months
(2026-02-26 vs 2026-07-25). The two Junction-family copies are byte-identical to
each other; the T1-chain copy is the one that differs. His commit message at
`da2c8db` — *"Reuses `LegendreApprox.abs_sub_ge_nat_div` from the Merle Junction
repository (compiles unchanged in this toolchain, 0 errors)"* — is accurate as
to origin. **Home: CONFIRMED**, the clause round 10 could only record as
unconfirmed.

**Verdict: NOT byte-identical, and the difference is immaterial.** Same length
(3,175 bytes each), and the whole diff is a two-line reordering:

```
16,17d15
< open Real
<
18a17,18
>
> open Real
```

i.e. the Junction copy has `open Real` **before** `namespace LegendreApprox`;
the T1-chain copy has it **inside** the namespace. Nothing else differs — not
one character of any statement, hypothesis, binder, docstring or tactic. The
three declarations are identical in both:

- `theorem abs_sub_ge_of_not_convergent (ξ : ℝ) (q : ℚ) (hnc : ∀ n, q ≠ ξ.convergent n) : 1 / (2 * (q.den : ℝ) ^ 2) ≤ |ξ - ↑q|`
- `lemma divInt_den_dvd_nat (S k : ℕ) (_hk : 0 < k) : (Rat.divInt (↑S) (↑k)).den ∣ k`
- `theorem abs_sub_ge_nat_div (ξ : ℝ) (S k : ℕ) (hk : 0 < k) (hnc : ∀ n, Rat.divInt (↑S) (↑k) ≠ ξ.convergent n) : 1 / (2 * (k : ℝ) ^ 2) ≤ |ξ - (S : ℝ) / k|`

which are exactly the statements `briefs/merle-lean-r10-audit-findings.md`
item 4 recorded and re-verified. `open Real` at file scope versus inside a
`namespace` puts the same names in scope for the same declarations; **there is
no divergence for the reply to carry, and nothing in the T1 chain's kernel
claims turns on it.**

**Drift check on the Junction side: none.** Blob `a4fae1f` from 2026-02-26 to
HEAD, in both Junction-family repositories. (Incidentally confirmed on his Lean
side too — blob `b55095a` at `da2c8db`, `5c9b663` and current HEAD `c991430`.
The sibling session `merle-r11-ceiling-audit` owns that question; this is
recorded only so the two records agree, and any reconciliation is the main
session's.)

**Junction copy's own counts, by read: 0 `sorry`, 0 `native_decide`, 0 `axiom`
declarations.** Imports: `Mathlib.NumberTheory.DiophantineApproximation.Basic`
and `Mathlib.Data.Rat.Lemmas` — identical to the T1-chain copy.

**Build context: it differs, and the difference does not bear on T1.**

| | Junction (`lean/`) | T1 chain (`one-obstruction-three-faces-lean`) |
|---|---|---|
| toolchain | `leanprover/lean4:v4.29.0-rc2` | `leanprover/lean4:v4.27.0` |
| Mathlib pin | `mathlib4 @ v4.29.0-rc2` | `mathlib @ v4.27.0` |
| lakefile | `lakefile.lean`, package `collatz_junction`, `autoImplicit := false`, `srcDir := "skeleton"` | `lakefile.toml`, package `otf-lean-merle`, no `leanOptions` |

The T1 chain compiles **its own copy** under its own v4.27.0 pin — it does not
import the Junction project — so the Junction repository's newer toolchain has
no bearing on T1's kernel claims. What the Junction context does add is one flat
data point our record did not have: the same three declarations are stated
against two different Mathlib pins five months apart, and his `da2c8db` claim
that the file *"compiles unchanged in this toolchain"* is consistent with the
file being pin-insensitive at this level (it uses only
`Real.exists_rat_eq_convergent`, `Rat.den_dvd` and elementary order lemmas).
**Read, not built** — no toolchain in this session; the standing pin from the
round-10 audit is unchanged, that no committed `#print axioms` log contains any
`LegendreApprox` entry although `T1Structure_axioms.txt`'s header names the file.

---

## Item 4 — the deficit lemma at first hand; flag 6 settled on the definition

Source: `Collatz-Junction-Theorem/paper/preprint_en.tex` @ `a57d29e`,
§3 *"Entropic deficit and nonsurjectivity"* (`\label{sec:entropy}`). The
`DeficitLemma.lean` header's pointer — *"(Merle, Junction Theorem preprint 2026,
§3)"* — resolves exactly: §3 is the section, and it contains the statement the
header describes.

Script: `experiments/junction_public_recon_deficit_check.py` with its committed
output; 465 checks, 0 failures.

### 4.1 The deficit lemma is there, and states what the header says

Notation, verbatim (`\label{not:main}`):

> `$k \geq 1$ denotes the \emph{length} of a cycle (number of odd steps);`
> `$S = S(k) = \lceil k \log_2 3 \rceil$ is the \emph{Syracuse height};`
> `$d = d(k) = 2^S - 3^k$ is the \emph{crystal module};`
> `$C = C(k) = \binom{S-1}{k-1}$ is the number of admissible compositions;`
> `$h(p) = -p\log_2 p - (1-p)\log_2(1-p)$ is the \emph{binary Shannon entropy}`

Definition 3.1 (`\label{def:deficit}`, `eq:gamma`), verbatim:

> `The \emph{entropic deficit} is the real number`
> `  \gamma \;=\; 1 - h\!\left(\frac{1}{\log_2 3}\right),`
> `where $h$ is the binary Shannon entropy.`

The lemma itself, Proposition *"Linear deficit"*
(`\label{prop:linear-deficit}`, `eq:deficit`), verbatim:

> `For every $k \geq 1$ with $d(k) > 0$:`
> `  \log_2 d - \log_2 C \;\geq\; (S-1) \cdot \gamma - \varepsilon(k),`
> `where $\varepsilon(k) = O(\log k)$ is a logarithmic error arising from`
> `the Diophantine approximation of $\log_2 3$.`

So: `γ = 1 − h(1/log₂3)` exactly as the header says, stated **per unit of `S`**,
with the binary-entropy bound as its engine
(Lemma `lem:binomial-entropy`: `log₂ binom(S−1,k−1) ≤ (S−1)·h(α)`,
`α = (k−1)/(S−1)`, cited to Cover–Thomas Thm 11.1.3). **Confirmed.**

### 4.2 Flag 6 — `S` **is** our `K`. Confirmed, and now on the definition

Round 10 settled this from the committed artifacts alone, on the units argument
(`γ·log₂3 = c_gen` exactly, versus `γ·(log₂3 − 1) = 0.02928`), and recorded the
inequality as non-discriminating. The preprint settles it more directly: **`S`
is defined**, not inferred:

`S = S(k) = ⌈k log₂ 3⌉`, with `k` the number of odd steps.

Our `K = ⌈n log₂ 3⌉` with `n` the number of odd steps. Same formula, same
argument, different letter. The naming clash with our own `S = K − n` is real
and is his letter's `S`, not ours.

Checked in the script (§A), by exact integer arithmetic rather than floating
point (`S = (3**k).bit_length()`): `S(k) = ⌈k·log₂3⌉` for every `k = 1..400`,
0 mismatches, and `S(3) = 5`, `S(5) = 8`, `S(100) = 159` reproduce the
preprint's own printed values exactly. The round-10 units argument is also
re-run and stands (§B): `γ·log₂3 − c_gen = 5.8·10⁻⁶²` at 60 digits, while the
alternative reading gives `γ·(log₂3 − 1) = 0.029274…`, not `c_gen`.

**Flag 6: CONFIRMED at first hand. No correction to the round-10 settlement.**

### 4.3 Two differences from our L-A7 form, recorded flat

Both are visible only now that the preprint can be read; neither was knowable
from the committed scripts.

**(a) The preprint's statement carries an error term; ours does not.** His
committed transcription in
`one-obstruction-three-faces-lean/experiments/test_REQ-MATH-037_junction_gamma_is_cgen.py`
reads `# Junction: log2 d - log2 C >= (S-1)*gamma`, dropping the `− ε(k)`. The
drop is harmless for the identity that script tests (`γ·log₂3 = c_gen`, a
statement about constants) but it is not harmless as a reading of the
proposition. Read literally without `ε(k)`, the printed inequality **fails**:
over the sampled `k`, 8 negative-slack instances, minimum slack `−4.4848` at
`k = 306` (a convergent denominator of `log₂3`), and `−2.4506` at `k = 200`
(script §C). Those are exactly the cases `ε(k)` exists to absorb — the failures
sit at convergents, where `log₂ d` falls furthest below `S`. So the error term
is load-bearing, and the difference between his form and ours is precisely
`S − log₂ d`, which is unbounded along convergents.

Our own margin uses `K` where he uses `log₂ d`, so it has no error term at all:
`margin(n) = K − log₂ binom(K−2, n−1) ≥ c_gen·n` for all `n ≥ 1`, with a uniform
surplus `1 + log₂(log₂3) = 1.66444871` (Theorem A,
`briefs/margin-inequality-proof-findings.md`). Script §E re-checks it at
`n ∈ {1, 2, 5, 18, 100, 1000, 16266, 190537}`; minimum sampled slack `1.9207` at
`n = 1`.

**(b) The binomial index differs by one.** The preprint counts
`C = binom(S−1, k−1)`; our L-A7 word count is `binom(K−2, n−1)`. His is the
larger, by `log₂((S−1)/(S−k))` — `1.3479` bits at `k = 18`, rising to `1.4375`
at `k = 2000` and to `log₂(log₂3 / (log₂3 − 1)) ≈ 1.43803` in the limit
(script §D). Recorded because the two forms are otherwise term-for-term the
same statement, and a future joint note should not let the two `C`s be read as
one.

### 4.4 Is the preprint's version proved, conditional, or exhibited?

**Exhibited on a finite range and asymptotic beyond it, with the constant left
inexplicit.** The proposition's own proof, verbatim in its load-bearing parts:

> `For $\theta > 0$ (i.e.\ $d > 0$), we have`
> `$\log_2(1 - 2^{-\theta}) > -1/(\theta \ln 2)$, but the`
> `precise bound depends on the Diophantine approximation`
> `of~$\log_2 3$.`
>
> `By continued fraction theory, if~$k$ is not a convergent`
> `of~$\log_2 3$, then $\theta \geq c/k$ for some`
> `constant~$c > 0$ …`
>
> `We verify numerically for every $k \in [18, 500]$`
> `that $C(k) < d(k)$ … For $k > 500$, the asymptotic argument works because`
> `$\log_2 C \leq (S-1)(1 - \gamma + O(1/k))$ while`
> `$\log_2 d \geq S - O(\log k)$ (by Diophantine approximation)`

The constant `c` is never made explicit, `ε(k)` is never bounded, and no
effective threshold is produced; the finite range `k ∈ [18, 500]` is verified by
computation and the rest is an asymptotic argument in `O`-notation. The theorem
it feeds (`thm:nonsurj`, `C(k) < d(k)` for `k ≥ 18`) is *stated* as proved, and
its proof is *"it suffices to verify that `(S−1)γ > ε(k)` for `k ≥ 18`"* —
which is the same unquantified comparison.

This is **not a criticism of the preprint**, which is a preprint and says what
it is doing; it is the fact our record needs, because the L-A7 ledger entry
rests on the margin inequality and the question of what the preprint supplies
was open. **What the preprint supplies is the idea and the constant; what it
does not supply is an effective inequality.** Our Theorem A supplies the latter
for the `K`-form, elementary and citing nothing, and his rational-binomial
`marginTarget` route supplies it at `1/13` in Lean. All three are on record; no
comparison of merit is drawn here and none is needed.

---

## Item 5 — the other three repositories, light recon

### 5.1 What each claims, in its own status words

**`collatz-nocycle-lean4`** — the active repository of the four, per its own
`docs/LINEAGE.md`. README `## Result`, verbatim:

> `Under three published hypotheses (Baker, Barina, Continued Fractions),`
> `no non-trivial cycle exists in the Collatz iteration.`
> `Formally verified in **Lean 4** with **zero sorry** statements and **zero axioms**.`

Main theorem, verbatim:

> `theorem no_nontrivial_cycle_phase59`
> `    (baker : BakerSeparation) (barina : BarinaVerification)`
> `    (cf : DerivedLargeKBound)`
> `    (n k : ℕ) (hcyc : IsOddCycle n k) : False`

Shape: 93 tracked files at HEAD, 36 `.lean` under `ProjetCollatz/`, self-reported
393 theorems, Lean/Mathlib v4.27.0. **By read: 0 `axiom` declarations, 0 real
`sorry`, `native_decide` in 10 files (self-reported 182 occurrences).** The
three hypotheses are Lean `structure`s taken as explicit parameters, not axioms
— the README says so and the code bears it out. `expected_axioms.md` lists
`propext, Classical.choice, Quot.sound` for the central theorem and names
`Lean.ofReduceBool` / `Lean.trustCompiler` as the `native_decide` axioms on the
`cf_gap_*` lemmas, currently isolated from the central chain. Formalised vs
asserted, cleanly separated: the two-case split (`k ≤ 1322` via Baker + product
bound; `k > 1322` via `DerivedLargeKBound`) is formalised; `DerivedLargeKBound`
itself is the asserted content, and the repository says so and names the plan to
discharge it (*"Phase Legendre"*). It carries the plain-words disclaimer quoted
in 2.8, a `verify.sh`, a `reproduce.sh`, two `probes/` files including a
dedicated `sorryAx` probe, and an audit apparatus under `docs/BIBLE/`
(RISK_REGISTER, LIMITATIONS, four gate sign-offs, four red-team reports, a
procedural-debt postmortem, environment snapshots and a SHA-256 integrity log).
This is the most carefully instrumented of the four by a wide margin.

**`collatz-cycles-lean`** — covered in item 2. Status words at HEAD: the archive
banner, the reduced README `## Result` (three clauses), and `VERIFICATION.md`'s
proved/not-proved tables. Shape: 47 tracked files (25 `.lean`), three Lean trees
(`verified/` Lean 4.15 no Mathlib, `skeleton/` Lean 4.29.0-rc2 + Mathlib,
`range-exclusion/` Lean 4.28, marked invalid), plus `paper/` (md/tex/pdf).
**4 `axiom` declarations, 0 real `sorry`, `native_decide` across 13 files.**

**`collatz-audit-2026`** — a meta-repository, not a formalisation. What it
audits, in its own words:

> `Ce dépôt centralise les résultats d'un audit mathématique rigoureux`
> `de trois dépôts de recherche sur la conjecture de Collatz:`
> `- Collatz-Junction-Theorem`
> `- collatz-cycles-lean`
> `- collatz-nocycle-lean4`

i.e. it cross-references the other three, dated March 2026. Shape: 22 tracked
files — three audit documents (`SYNTHESE_MARS2026.md`, `COMPLEMENT_RECHERCHE.md`,
`PISTES_CROISEES.md`), eight Lean files (scaffolding), three Python scripts, two
results files, two CI workflows. Its Lean is explicitly scaffolding and **does
carry real `sorry`s** — `lean/BakerSeparationProof.lean:79` and `:122`,
`lean/ContinuedFractionBridge.lean:35` and `:41` (the latter two commented
*"Legendre 1798, ~150 lignes a formaliser"*) — with `lean/FinalAssembly.lean`
stating the arithmetic openly: *"Si les 2 sorry sont combles: 0 sorry + 1 axiome
= PREUVE COMPLETE"*. Its own new result is modest and stated as such: `k = 16`
and `k = 17` proved without external dependency.

**One flat hygiene note on `collatz-audit-2026`.** Its README's summary table
reads:

> `| Cycles de longueur 18+ | **Impossibles** | Théorème de Jonction (Merle) |`

The Junction Theorem does not give impossibility for `k ≥ 18`; it gives
non-surjectivity, and his own preprint says so in the same breath
(*"nonsurjectivity alone does not exclude cycles"*, `rem:junction-scope`, quoted
in 2.6). The row is a plain-language summary in a section headed *"vulgarisé,
sans jargon"*, under an archive banner, in the repository that had no licence
until the flip — so it is a small thing in a small place. Recorded because the
brief asks for what is there, and because it is the one place in the four where
a headline is still stronger than the document behind it besides
`PROOF_ASSEMBLY.md`.

### 5.2 Overlap with our own record, stated flat

This is prior-art hygiene for a possible joint note. No priority is asserted, no
credit is adjudicated, and no comparative adjective is used.

**(i) Periods 1–3 / small-`k` cycle exclusion.** We close periods 1, 2, 3 in
reduced coordinates in-house (cycles.md 12.2.3, 12.5.3, 12.7.5), matching Steiner
and Simons–de Weger. His counterpart is `collatz-cycles-lean/lean/verified/`:
`N₀(d(k)) = 0` for `k = 3..15` by Lean-certified computation, 280 theorems,
0 `sorry`, 0 `axiom`, Lean 4.15 without Mathlib (first committed 2026-02/03).
The objects differ — his `k` is the number of odd steps in Steiner's
formulation, our `p` is the number of *blocks* of the reduced map — so the two
ranges are not directly comparable and no generality claim is made either way.
What is comparable and worth having on record: **both sides have an
independently checkable small-range exclusion, his by Lean computation over
compositions, ours by reduced-coordinate classification.** Dates: his
2026-02-26/2026-03-26 (public), ours in this repository's git log.

**(ii) The uniform trim / "`2^K` close to `3^n`" geometry.** Our Theorem 12.8.1
derives, from the rotation size conditions `q ≤ R_r`, a bound
`γ + log₂p > 0.585·n/(1.585^p − 1)` uniform in `p`, with `q = 2^K − 3^n`. His
counterpart is **Range Exclusion** (`collatz-cycles-lean/docs/PROOF_ASSEMBLY.md`
§3): `corrSum` over monotone compositions is confined to
`[3^k − 1, 3^k + 3^r − 2]`, an interval of width `3^r − 1`, and the question is
whether `d = 2^S − 3^k` can divide anything in it. **Both are "a hypothetical
cycle forces `2^S` close to `3^k`, and the closeness is the whole content."**
They are the same geometry in different coordinates. Two flat notes:

- His §3.1 *"Forced Flatness Theorem"* (for `k ≥ 5`, the first
  `L = 2k − S ≈ 0.415k` parts of any admissible composition are forced equal)
  has **no counterpart in our record**; it is a statement about monotone
  compositions of `S` into `k` parts and our block/exit coordinates do not have
  it.
- His decay `range/d = O(k^{4.125} · 3^{−0.415k})` and our trim's degradation
  `1.585^(−p)` are **different quantities and must not be read as the same
  number**: `3^{0.415} = 1.5777…` is `3^(2 − log₂3)`, while our `1.585` is
  `log₂3 = 1.58496…`, and his exponent counts odd steps `k` where ours counts
  blocks `p`. The numerical proximity is a coincidence of two different
  constants.

**(iii) The `1.585^(−p)` degradation and the staircase (cycles.md 12.8.3).**
**No counterpart in any of the four.** There is no family of size-passing
near-counterexamples anywhere in his repositories, and no statement that
counting arguments cannot do substantially better. The word *escalier*
("staircase") does occur, in
`Collatz-Junction-Theorem/research_log/phase10l_choc_des_cristaux.md`, for a
different object entirely — the rigid lattice path traced by the monomials
`2^a 3^b` in `ℤ²` — and it is not our staircase. Recorded so the word cannot
later be mistaken for a shared object.

**(iv) Convergent denominators of `log₂3` as the location of the hard cases.**
This one is a genuine antecedent on his side, months before L-A8/T1, and it is
worth pinning. `collatz-cycles-lean/docs/PROOF_ASSEMBLY.md` §10.5, dated
17 March 2026 in the document header and committed 2026-03-26, verbatim:

> `**Consequence:** The "dangerous" $k$ values (where $\{k\alpha\}$ is smallest)`
> `are confined to convergent denominators $q_n$ of the continued fraction of`
> `$\alpha$. No other $k$ can approach 0 more closely. This regularizes the`
> `problem: we only need to check that the Baker bound holds at convergent`
> `denominators.`

with §10.2 giving the CF of `log₂3` to 10,000 terms (citing Jackson–Matthews
2002, OEIS A028507), §10.4 tabulating the irrationality measures
(Rhin 1987 `8.616`, Salikhov 2007 `5.125`, Wu–Wang 2014 `5.1163` — for `log 3`,
the same list the L-A7 re-sourcing adjudicated), and §10.5 citing Sós 1958's
three-distance theorem, verified for `α = log₂3`, `N = 3..200`. **This is the
same observation as L-A8/T1's frame-prediction point** (thresholds live on the
convergent grid) and as the tightening our round-10 L-A8 check contributed (that
an in-window `n` is a priori a *multiple* of a convergent denominator, cycles.md
12.8.6.1's neighbourhood). It predates the correspondence on his side by four
months. Recorded as prior art of his own, for citation in a joint note; nothing
in our record is displaced by it, and our record already credits the
convergent-grid framing to the L-A8 entry, which is his.

### 5.3 Anything that would change a claim of ours if true

**Nothing found does.** Every claim of ours that touches this material —
periods 1–3, the uniform trim and its degradation, the staircase, the
margin/deficit inequality at `c_gen`, the L-A7 constants, the L-A8 convergent
window and Hercher's threshold — was checked against what these repositories
say, and none is contradicted. Two flat consistency notes:

- `collatz-cycles-lean/VERIFICATION.md` records *"No cycle k ≤ 91 — **PROVED**
  (external) — Hercher (2025), J. Integer Seq."* That is the same Hercher our
  L-A8 check adjudicated (there via Cor. 29's `K > 1.375·10^11`), and the `91`
  is the crossover target cycles.md 12.8.5 already names. Consistent; nothing
  to change.
- His `k ≥ 69` Hypothesis (H) clause (2.6) is the `m ≥ 69` Simons–de Weger
  ingredient round 10 identified in `collatz-conditional-cycles`. Same
  ingredient, now readable in its own preprint. Consistent; nothing to change.

The only items with any reply-side weight are the two internal tensions on his
side recorded flat above — `docs/PROOF_ASSEMBLY.md` at 2.4 and the
`collatz-audit-2026` summary row at 5.1 — and both are his to do as he sees fit
with, if the author chooses to mention them at all.

---

## Closing

His account of his own work checks out on almost every particular that can be
checked, and several of them check out word for word: a README that claimed an
unconditional no-cycles result for all `k`, rewritten in a commit whose own
message says *"reduce claim to what is actually proved"*; a technical document
naming two asymptotic programs each with an unclosed gap beyond `k = 200`; a
preprint that states in its own text that complete exclusion for `k ≥ 69` needs
an additional hypothesis; scope banners that go further than he described;
Simons–de Weger as a genuine `axiom` declaration; and a status page that marks
its own headline module INVALID by name.

Three things did not check out, and they are recorded without adjudication of
motive.

1. **`AUDIT_V9` is not in any of the four repositories**, in any ref, at any
   point in their history. The public audit series stops at V8 (2026-03-07),
   whose verdict — *"le squelette structural tient … l'abstract suraffirme"* —
   is the same shape as the one he described, three months earlier. The
   round-10 posture applies unchanged: absence here is not evidence that the
   record does not exist. `Projet_Collatz` is private by his decision and was
   not looked at.
2. **`STATUS.md` does not exist**; the status document that was rewritten is
   `VERIFICATION.md`, and it was rewritten well.
3. **The range beyond `k = 50000` is not marked OPEN.** The document that
   discusses it, `docs/PROOF_ASSEMBLY.md`, marks it **PROVED** and closes with
   *"No gap remains. The proof is unconditional for all `k ≥ 3`."* — about the
   very module the rest of the repository marks invalid. That document was not
   touched by the rewrite and has not been modified since the day it was added.

And one thing about the whole picture that belongs in the record because it will
otherwise be inferred silently: **every confirmed remediation is dated March or
April 2026**, and no commit anywhere in the four repositories is later than
2026-04-25 except the licence added at the flip. So the work he described is
there, and it is older than the description. Whether the audit he recounted is
the April 2026 adversarial audit — whose gate sign-offs, red-team reports, risk
register and postmortem are all committed in `collatz-nocycle-lean4/docs/BIBLE/`
— or a separate later record we have not seen, is not settled by anything
public, and this session does not settle it.

Two answers our record was waiting on are now closed at first hand. **The
preprint's `S` is our `K`** — by definition, not by inference
(`S = ⌈k log₂3⌉`), so flag 6 of `briefs/merle-la7-close-check-findings.md` is
confirmed with no correction. And **`LegendreApprox.lean`'s home is confirmed**,
the Junction copy is upstream by five months, and the diff against the T1-chain
copy comes back as a two-line reordering of `open Real` with no mathematical
content — so the one clause the round-10 reply flagged as bearing on what T1
rests on is now answered, and it is a clean answer.

Access record, restated: read-only clones and read-only public API calls only.
**No fork, no issue, no pull request, no comment, no star, no watch, no follow,
no push, no write of any kind, and no contact with anyone.** `Projet_Collatz`
untouched, unrequested, unreached.
