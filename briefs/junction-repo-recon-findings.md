# Junction Theorem repository — recon and self-audit confirmation

Brief: `briefs/junction-repo-recon-brief.md`. Branch `junction-repo-recon`, base
`9d22dc8` (the worktree was cut at `b860fe8`, a strict ancestor that does not
contain the brief; the branch was taken from `main` at `9d22dc8`, which does).
Recon only: no proof of the Junction Theorem was checked and no grade is given.

## Outcome in one line

The repository described in his round-10 letter — the Junction Theorem work
carrying the `AUDIT_V9` self-audit — is **not present among his public GitHub
repositories**. Queue items 2, 3 (in part) and 4 (the diff) read that
repository and therefore could not be executed. What follows records the search
and its bounds, what the accessible sources do carry, and each described point
marked **NOT FOUND (repository inaccessible)** rather than confirmed or denied.

## Item 1 — locate

Handle `ericmerle3789`. Public repositories, enumerated 2026-07-26:

| Repository | HEAD (default branch `main`) | Last push |
|---|---|---|
| `collatz-conditional-cycles` | `c24633cc8999ec509782125d664b47396cb89593` | 2026-07-18T21:38:00Z (`gh-pages`); `main` last committed 2026-04-26 |
| `one-obstruction-three-faces-lean` | `5c9b66392a157ce63c34f765e18e05723d870ddf` | 2026-07-25T16:45:27Z |
| `paper-trading-dashboard` | not cloned (unrelated subject) | 2026-05-16T07:05:56Z |

`gh api users/ericmerle3789` reports `"public_repos": 3`. The repos-list
endpoint additionally returns a name `ericmerle3789/one-obstruction-three-faces`
whose direct fetch answers `404 Not Found`; it does not appear in
`gh search repos --owner=ericmerle3789` nor in the public event stream under his
ownership. Recorded flat, not chased — it is his own name for the shared repo,
not a Junction candidate.

Searches run, all read-only:

- `gh repo list ericmerle3789`; `gh api users/ericmerle3789/repos?per_page=100&type=all`
- `gh api users/ericmerle3789/orgs` → `[]` (no organizations)
- `gh search repos --owner=ericmerle3789` → the three repositories above
- `gh search repos "junction"`, `"junction collatz"`, `"junction theorem"`,
  `"collatz merle"` → no repository of his
- `gh search code "AUDIT_V9"` → 20 hits, none in any repository of his
- `gh search code "abs_sub_ge_of_not_convergent"` → one hit,
  `macindoe/one-obstruction-three-faces` `LEDGER.md`
- `gh search code "\"Junction Theorem\""`, `"jonction collatz"` → no hits
  (the phrase does occur in `one-obstruction-three-faces-lean`, so the code
  index is incomplete for that repository; absence there is not evidence)
- `gh api users/ericmerle3789/events/public?per_page=100` → activity in exactly
  three repositories: `ericmerle3789/collatz-conditional-cycles`,
  `ericmerle3789/one-obstruction-three-faces-lean`,
  `macindoe/one-obstruction-three-faces`; latest event 2026-07-25T16:45:30Z

`collatz-conditional-cycles` was cloned in full, all ten remote branches and
seven tags fetched. Across every ref in that repository there is **no file
matching `*AUDIT*`, no `STATUS.md`, and no file matching `*Legendre*`**.

**No repository named or describing itself as the Junction Theorem work exists
under his handle publicly. No commit carrying `AUDIT_V9` was found.**

Interaction record: no fork, issue, comment, star, watch, or any write of any
kind was made against any repository of his. All reads were unauthenticated
clones into the session scratchpad and read-only API calls.

### The nearest public repository, recorded as *not* the described one

`collatz-conditional-cycles`, HEAD `c24633c` ("Prepare JAR submission v1.1:
multi-agent audit fixes + Springer build", 2026-04-26), five commits on `main`,
companion to the paper *On the non-existence of non-trivial Collatz cycles: a
conditional formal proof in Lean 4 with documented structural obstructions*,
Zenodo DOI 10.5281/zenodo.19790406. It is his only other Collatz repository and
it is in the same family of work, but it is not the repository the letter
describes. The points that separate them, flatly:

- Its README is headed **"Collatz cycles: conditional non-existence in Lean 4"**
  and its Status section reads, verbatim and unchanged since the *first* commit
  `cc8c83e`: *"The paper proves a **conditional** theorem: there are no
  non-trivial Collatz cycles, *provided* three explicit hypotheses (one
  published, one computational, one project-derived) hold."* There is no
  unconditional claim in its history to have been corrected.
- It contains **no `axiom` declaration** in any `.lean` file. Simons–de Weger
  enters as a *structure parameter* — `ProductBoundThreshold` (`HYPOTHESES.md`:
  *"**ProductBoundThreshold** (formerly SimonsDeWegerBound)"*) — not as an axiom.
- It contains **no `sorry`**; `reproduce.sh` exits 4 on `sorryAx`.
- It **does** use `native_decide`, for the continued-fraction gap lemmas
  (`PROOF_CHAIN.md`: *"cf_gap_8..13 (6 native_decide arithmetic proofs)"*), and
  `expected_axioms.md` already names the compiler-trust axioms explicitly:
  *"**(N)** = `native_decide` axioms: `Lean.ofReduceBool`, `Lean.trustCompiler`"*.
- One number in the letter's description has a visible counterpart here:
  `HYPOTHESES.md` records *"SdW gives a LOWER bound on m (m ≥ 69)"*, and
  `paper/v2/06-obstruction-II-state-of-the-art.md` tabulates Simons–de Weger
  2005 as *"local-minima $m > 68$"*. The letter's "extra hypothesis for
  `k ≥ 69`" is the same ingredient. The "`k = 200`", "`k = 50000`" and
  "two asymptotic programs" markers have **no** counterpart in this repository;
  its own open-problem horizon is stated as `k < q_{14} ≈ 10,590,737`
  (`paper/v2/09-open-problems.md`).

## Item 2 — the self-audit, point by point

Every point below reads the Junction repository. That repository is not
publicly reachable, so no point is confirmed and no point is denied.

| Described point | Status |
|---|---|
| README claimed an **unconditional** proof of no cycles for all `k ≥ 3` | NOT FOUND (repository inaccessible) |
| Its technical document says two asymptotic programs, each with a named unclosed gap beyond `k = 200` | NOT FOUND (repository inaccessible) |
| The preprint states complete exclusion needs an extra hypothesis for `k ≥ 69` | NOT FOUND (repository inaccessible); the `m ≥ 69` ingredient is present in `collatz-conditional-cycles`, see above |
| README and STATUS rewritten to match the technical documents | NOT FOUND — no `STATUS.md` in any ref of any public repository of his |
| Scope banner added | NOT FOUND (repository inaccessible) |
| `native_decide` reliance flagged (compiler-trusted, not kernel-trusted) | NOT FOUND for the described repository; the equivalent flag is present in `collatz-conditional-cycles` `expected_axioms.md`, quoted above |
| Range beyond `k = 50000` marked **OPEN** | NOT FOUND (repository inaccessible) |
| Plain-words statement that the repository does **not** prove the Collatz conjecture | NOT FOUND for the described repository; `collatz-conditional-cycles` README carries the nearest sentence, *"It does not address the unconditional convergence-to-1 statement (the divergence half of the Collatz conjecture); only the no-non-trivial-cycle disjunct is treated."* |
| Audit record committed as `AUDIT_V9` | NOT FOUND — no such file or commit in any ref of any public repository of his, and no code-search hit under his ownership |
| *"The mathematics inside was sound; the shop window was ahead of the shop."* | not a repository artifact; nothing to check |

`AUDIT_V9` was not read, so its own summary of what it found is not recorded.

## Item 3 — the deficit lemma's provenance

The preprint is in neither shared nor accessible repository, and the Junction
repository is unreachable, so the §3 statement could not be read at source. What
the accessible committed artifacts carry, verbatim:

`ericmerle3789/one-obstruction-three-faces-lean` @ `5c9b663`,
`OneObstruction/DeficitLemma.lean`, header lines 5–10:

> CONTEXT. The L-A7 ledger entry rests on the margin inequality `margin(n) ≥ c_gen·n`,
> where `margin(n) = K − log₂ C(K−2, n−1)` and `K = ⌈n·log₂3⌉`. Its published-style proof
> (Merle, Junction Theorem preprint 2026, §3) goes through the binary-entropy bound
> `C(m,k) ≤ 2^{m·h(k/m)}`, with deficit constant `γ = 1 − h(1/log₂3)`; verified 2026-07-25
> that `γ·log₂3 = c_gen` exactly (REQ-MATH-037).

The dating in that header is **"preprint 2026"**; the brief's framing describes
it as a preprint from spring 2025. Recorded flat, not resolved — the letter
itself is the main session's source for the year and was not available here.

Same repository, `experiments/test_REQ-MATH-037_junction_gamma_is_cgen.py`,
lines 2–5, the §3 statement as he transcribes it:

> `# REQ-MATH-037 — ARES : le gamma du Junction Theorem (Merle 2026) EST le c_gen de Macindoe.`
> `# Junction: log2 d - log2 C >= (S-1)*gamma, gamma = 1 - h(1/log2 3)   [par unite de S]`
> `# L-A7   : margin(n) >= c_gen*n,            c_gen = L - L log2 L + (L-1) log2(L-1)  [par unite de n]`
> `# TEST : gamma * log2(3) == c_gen exactement ?  (S ~ n*log2 3)`

and its committed output `experiments/OUT_REQ-MATH-037.txt`:

> `  gamma = 1 - h(1/log2 3) = 0.05004447281`
> `  gamma * log2(3)         = 0.07931861277`
> `  c_gen (Ben)             = 0.07931861277`
> `  ecart |gamma*L - c_gen| = 0.0`
> `  => IDENTIQUES (meme constante, unites differentes : par S vs par n)`

**Definition of `γ`:** `γ = 1 − h(1/log₂3)`, `h` the binary entropy in bits,
`h(x) = −x log₂x − (1−x) log₂(1−x)`. Numerically `γ = 0.0500444728117`.

**Units:** the Junction form is stated *per unit of `S`*; the L-A7 form is
stated *per unit of `n`*; the conversion is the factor `log₂3`.

### Flag 6 of `briefs/merle-la7-close-check-findings.md` — settled: `S` is our `K`

That flag suspected, from the conversion comment `S ~ n·log₂3`, that the
preprint's `S` denotes our `K`. It settles from the committed sources alone,
without the preprint:

- The conversion factor is fixed by the identity he verifies. `γ` is the
  per-`S` constant and `c_gen` the per-`n` constant, and the identity that makes
  the two forms one statement is `γ·log₂3 = c_gen` — so `S/n → log₂3`. In our
  conventions `K/n → log₂3` and `S/n → log₂3 − 1 = 0.585`; only `S = K` gives
  the factor he uses.
- The alternative reading `S = K − n` would carry a per-`n` constant
  `γ·(log₂3 − 1) = 0.02928`, not `c_gen = 0.0793186`. His own committed output
  states the difference is exactly `0.0` under his reading.
- The two forms then coincide term for term with `log₂d = S = K` (i.e.
  `d = 2^K`): `S − log₂C ≥ (S−1)·γ` **is** `K − log₂C(K−2,n−1) ≥ (K−1)·γ`,
  which is `margin(n) ≥ (K−1)·γ`, and `(K−1)·γ ≈ n·log₂3·γ = n·c_gen`.

Numerical check run this session (`mpmath`, dps 40, `n = 2..2000`,
`K = ⌈n·log₂3⌉`): under `S = K` the inequality `margin(n) ≥ (S−1)γ` holds with
0 failures, minimum slack `2.8499` bits. The alternative `S = K − n` also holds
(0 failures, minimum slack `2.9500`) because it is the strictly weaker
statement — so the inequality does not discriminate, and the settlement above
rests on the *units*, not on the inequality. Recorded that way deliberately.

### The caveats he names — not verifiable

The brief asks which parts of the Junction proof use `native_decide`, where the
two `sorry`s sit in the asymptotic assembly, and whether Simons–de Weger
genuinely appears as an `axiom` declaration (with the declaration quoted). All
three read the Junction repository: **NOT VERIFIABLE from any accessible
source.** No `axiom` declaration of any kind, and no `sorry`, exists in
`collatz-conditional-cycles`; that is a statement about that repository only and
is not evidence either way about the described one.

## Item 4 — `LegendreApprox.lean`

**Home: not confirmed.** The file is not present in `collatz-conditional-cycles`
in any ref. Its stated provenance is his own commit message, quoted verbatim
from `one-obstruction-three-faces-lean` `da2c8db`:

> Reuses `LegendreApprox.abs_sub_ge_nat_div` from the Merle Junction repository
> (compiles unchanged in this toolchain, 0 errors) wrapping Mathlib's criterion

and the shared `LEDGER.md` (`macindoe/one-obstruction-three-faces` @ `826970e`):

> invoke Legendre's criterion (entry point `LegendreApprox.abs_sub_ge_of_not_convergent`,
> clean, already in the Merle Junction repository, wrapping Mathlib)

Neither names a URL. No accessible artifact locates the file's home.

**Status in `one-obstruction-three-faces-lean` @ `5c9b663`:** the file entered at
`da2c8db` and is byte-identical since — blob `b55095a` at both `da2c8db` and
`HEAD`, and `git log --follow` shows `da2c8db` as its only commit. By read:
**0 `sorry`, 0 `native_decide`, 0 `axiom` declarations**; imports
`Mathlib.NumberTheory.DiophantineApproximation.Basic` and
`Mathlib.Data.Rat.Lemmas`. Three declarations, statements as recorded in
`briefs/merle-lean-r10-audit-findings.md` item 4, re-read and unchanged this
session. The standing pin from that audit also re-confirmed: no committed
`#print axioms` log contains any `LegendreApprox` entry, though
`T1Structure_axioms.txt`'s header names the file.

**Diff verdict: NOT PERFORMED — the counterpart is inaccessible.** There is no
copy of `LegendreApprox.lean` to diff against; the question "identical or not"
has no answer from public sources.

**Nearest public relative, recorded flat and not offered as the counterpart.**
`collatz-conditional-cycles` `ProjetCollatz/Phase61CFConvergents.lean` §4
contains the same mathematical step, specialized to `log₂3` rather than a
general `ξ`, with the same four-line proof script:

> `theorem not_convergent_implies_far_approx`
> `    {q : ℚ} (h_not_conv : ∀ n, q ≠ (logb 2 3).convergent n) :`
> `    1 / (2 * (q.den : ℝ) ^ 2) ≤ |logb 2 3 - (q : ℝ)| := by`
> `  by_contra h_close`
> `  push_neg at h_close`
> `  obtain ⟨n, hn⟩ := exists_rat_eq_convergent h_close`
> `  exact h_not_conv n hn`

against `LegendreApprox.abs_sub_ge_of_not_convergent`, which generalizes `ξ`
and adds Parts B and C (`divInt_den_dvd_nat`, `abs_sub_ge_nat_div`). That file
also carries his own terminology caveat, verbatim: *"this contrapositive is NOT
the classical 'best approximation of the second kind' property of CF theory ...
The theorem below is merely the contrapositive of Mathlib's approximation bound
and makes no claim about comparison of `|q·ξ - p|` across different
denominators."* Its header states *"Zero `axiom` declaration ... Zero `sorry`.
No `native_decide`"*. This is a related file in a different repository; it is
not the described `LegendreApprox.lean` and no identity is claimed.

## Closing

His account of his own repository could not be checked, because the repository
it describes is not publicly reachable: three public repositories under his
handle, no organizations, no `AUDIT_V9` in any ref of any of them, no
`LegendreApprox.lean` outside the Lean repository that imports it, and a public
event stream showing activity in three repositories only. The described repo may
be private, may be under an account not linked from anything we can see, or may
not have been pushed. Nothing found contradicts his account; nothing found
confirms it. The one number in his description that has a visible counterpart —
the `m ≥ 69` Simons–de Weger ingredient — is present in his other public Collatz
repository, and that repository has been framed as conditional since its first
commit. The deficit lemma's provenance is recorded above at second hand, from
his own committed header and script, and the one open question our side had
about it — whether the preprint's `S` is our `K` — is settled affirmatively from
those artifacts alone. If confirming the self-audit matters to the reply, the
repository's location is the thing to ask for.
