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
