# Joint-note premise pre-check, half B — the external facts

Brief: `briefs/jointnote-premise-external-brief.md`. Branch
`jointnote-premise-external`, base **`d945556`** (the worktree was cut at the
session-start `2225b68`, which does not contain the brief; it was rebased onto
`d945556` before any work started, per the launch instruction).

**Facts only.** No contribution sentence is drafted here, no note prose is
written, no framing is recommended. Where Merle's statement and the source
differ, both are recorded and the difference is left standing. The sentence is
the author's — Merle asked him directly.

Half A (`briefs/jointnote-premise-ours-brief.md`) covers our own published
record and runs in parallel; nothing here duplicates it.

## Interaction record — none occurred

- **`ccchallenge.org`: read-only HTTP GET only.** No account was created, no
  login was attempted, nothing was added, claimed, edited, wishlisted or
  submitted. Every URL consulted is listed below and every one is a `GET` of a
  public page or public read fragment. The site's own `POST` endpoint
  (`/api/papers/{key}/wishlist`) was never called.
- **GitHub: read-only.** One unauthenticated `git clone` of the shared
  repository, plus read-only `gh api` reads of public endpoints. **No push, no
  fork, no issue, no pull request, no comment, no star, no watch, no follow, no
  release download**, against any repository, including the shared one.
- No contact with anyone.

## Timing of the checks

All external reads in this session were made on **2026-07-27 15:30–15:40 UTC**,
i.e. **2026-07-28, early morning, local (UTC+10)**. Dates below are given in the
local convention the rest of the record uses (2026-07-28) with the UTC instant
noted where it matters.

---

## Item 1 — `ccchallenge.org`, read directly (checked 2026-07-28)

### 1.1 Purpose and scope, in the site's own words

Tagline, on the front page under the site name:

> Formalising the Collatz literature, one paper at a time.

From `/story`:

> The goal of the Collatz Conjecture Challenge (ccchallenge for short) is to
> collaboratively formalise the research literature on the Collatz conjecture
> using proof assistants.

Scope, as `/story` puts it: the Collatz problem (the "3n + 1 problem"),
including its variants over the natural numbers, the negative integers and the
rationals with odd denominators; the literature base is drawn from J. C.
Lagarias's bibliographies (1963 onwards). Maintainers named on the page:
**Tristan Stérin (cosmo) and Olivier Rozier**.

From `/method`, the three stages, verbatim in part:

> Each paper goes through three stages: Formalisation. One or more contributors
> pick a paper and formalise its results in a proof assistant (Lean, Rocq,
> Isabelle, Agda, etc.).

Audit stage: reviewers assess whether "the formalisation faithfully captures the
paper's content and write an audit report recommending whether to accept or
reject it." Acceptance stage: "Accepted formalisations count toward the
project's formalisation goal. Rejected formalisations go back to stage 1 so that
their authors can address the problems." And the independence rule: "Auditors
must differ from the formalisation authors, unless the formalisation was done by
AI."

### 1.2 Entry count and status breakdown

| | His statement (at the time he looked) | The site, 2026-07-28 | Verdict |
|---|---|---|---|
| Entries | 371 | **371** — header reads "Literature (371 entries)" | **matches** |
| Formalised | one | **1** | **matches** |
| In progress | four | **4** ("Formalising: 4") | **matches** |
| Awaiting audit | five | **5** ("Ready: 5") | **matches** |

Goal-progress line as printed on the front page: **"1/363 papers formalised"**.
The stats fragment (`/htmx/stats`) gives the buckets as **"Not started: 353,
Formalising: 4, Ready: 5, Auditing: 0, Formalised: 1"** — which sums to the
**363** papers inside the formalisation goal. The two numbers are not in
tension: **371** is the size of the literature database, **363** the number of
those entries inside the goal (the remainder carry an exclusion reason and are
badged "Not in goal" — e.g. Andaloro 2000).

**No drift.** Every one of his four numbers is the site's current number. There
is nothing to record as drift.

The five status filter labels the browse controls offer, verbatim: *Not
formalised / Being formalised / Ready to be audited / Being audited /
Formalised*. So the site's own words for his "awaiting audit" is **"Ready to be
audited"**, and there is a separate, currently empty, "Being audited" bucket
(0).

The **five "Ready to be audited" entries**, in full (`/htmx/paper-list?status=waiting_to_be_audited`):

1. `Tao2022` — "Almost all orbits of the Collatz map attain almost bounded values", Terence Tao, 2022
2. **`Eliahou1993`** — "The $3x + 1$ problem: New Lower Bounds on Nontrivial Cycle Lengths", Shalom Eliahou, 1993
3. `BernsteinLagarias1996` — "The $3x+1$ Conjugacy Map", Daniel J. Bernstein and Jeffrey C. Lagarias, 1996
4. `RozierTerracol2025` — "Paradoxical behavior in Collatz sequences", Olivier Rozier and Claude Terracol, 2025
5. `EliahouVergerGaugry2025` — "The number system in rational base $3/2$ and the $3x+1$ problem", Shalom Eliahou and Jean-Louis Verger-Gaugry, 2025

The **one Formalised** entry (`?status=audited`): `BohmSontacchi1978` — Corrado
Böhm and Giovanna Sontacchi, 1978, *"On the existence of cycles of given length
in integer sequences like $x_{n+1}= x_n/2$ if $x_n$ even, and $x_{n+1}= 3x_n +
1$ otherwise"*, badge **"Formalised"**.

The **four Being formalised**: `Knight2026` ("Collatz high cycles do not
exist", Kevin Knight, 2026), `Monks2006`, `KrasikovLagarias2003`, `Terras1976`.
(The `?status=formalising` filter returns five cards, the fifth being
`RozierTerracol2025`, which carries one formalisation in each state; the stats
bucket counts a paper at its highest-priority status, which is why the
"formalising" count is 4 and not 5.)

### 1.3 Eliahou 1993 — the fact his correction turns on: **CONFIRMED**

`Eliahou1993`, "The $3x + 1$ problem: New Lower Bounds on Nontrivial Cycle
Lengths", Shalom Eliahou, 1993. Status badge: **"Ready to be audited"**. Its
detail fragment shows **one formalisation**, proof assistant **`lean4`**, status
label **"Ready to be audited"**, with the AI disclosure **"AI-assisted:
aristotle"**; the entry also carries 2 reviews.

So the fact he cites is exactly as he states it: a formalisation of a
cycle-length paper exists and is awaiting audit. **His self-correction from "the
first machine-checked fragment of the cycle literature" to "a fragment" is
supported by the source.**

**One thing the source says that his statement does not** — recorded flat, not
as a correction to him, because it points the same way and further: the single
**accepted** formalisation in the whole register, `BohmSontacchi1978`, is also a
**cycle** paper — its title is literally *On the existence of cycles of given
length…* — and it is not merely awaiting audit but **Formalised** (audited and
accepted). And `Knight2026`, "Collatz high cycles do not exist", is currently
**Being formalised**. On the register as it stands, machine-checked work on the
cycle literature is not first, not sole, and not confined to the awaiting-audit
bucket.

### 1.4 Steiner, Simons–de Weger, Hercher — listed, none formalised

| Key | Title, as printed | Author(s) | Year | Status badge | Formalisations |
|---|---|---|---|---|---|
| `Steiner1978` | "A Theorem on the Syracuse Problem" | Ray P. Steiner | 1978 | ☆ Wishlist | **Formalisations (0)** — "No formalisations yet." (2 reviews) |
| `Steiner1981a` | "On the '$Qx+1$' Problem, $Q$ odd" | Ray P. Steiner | 1981 | ☆ Wishlist | 0 |
| `Steiner1981b` | "On the '$Qx+1$' Problem, $Q$ odd II" | Ray P. Steiner | 1981 | ☆ Wishlist | 0 |
| `SimonsWeger2005` | "Theoretical and computational bounds for $m$-cycles of the $3n+1$ problem" | John L. Simons and Benne M. M. de Weger | 2005 | ☆ Wishlist | **Formalisations (0)** — "No formalisations yet." (1 review) |
| `Hercher2023` | "There are no Collatz $m$-Cycles with $m \leq 91$" | Christian Hercher | 2023 | ☆ Wishlist | **Formalisations (0)** — "No formalisations yet." (1 review) |

**His statement — "Steiner, Simons-de Weger and Hercher are listed and none is
formalised" — is confirmed in every part.** One addition of detail: Steiner is
listed three times, and the one that matters for the cycle literature
(`Steiner1978`, the Syracuse-problem theorem) is dated **1978** on the register,
not 1977 as our own wiki and `NOTE.md` §1 cite it. That is a citation-year
difference between two records, recorded and not adjudicated here.

### 1.5 `Macindoe2026` — catalogued, formalisation slot empty: **CONFIRMED**

The entry exists. Recorded **verbatim** as the site serves it
(`/api/papers/Macindoe2026/bibtex`):

```bibtex
@misc{Macindoe2026,
  author    = {{Macindoe, Benjamin James}},
  title     = {{Reduced coordinates for the Collatz map: exact per-step laws, anchor dynamics, and the limits of counting arguments for cycles}},
  publisher = {{Zenodo}},
  year      = {{2026}},
  doi       = {{10.5281/zenodo.21273548}},
  url       = {{https://doi.org/10.5281/zenodo.21273548}},
  abstract  = {{We study the Collatz dynamics in a reduced coordinate system that compresses each deterministic valuation run into a single block, producing a self-map F on states (ω, d) — an odd core prime to 3 and a depth. The reduction is faithful: the Collatz conjecture is equivalent to every F-orbit reaching (1, 1), with nontrivial cycles in bijection. In these coordinates the local arithmetic admits exact laws. A single 2-adic quantity, the anchor M(ω) = −2 log ω/ log 9 ∈ Z2, governs the step: the exit valuation obeys the global law s = 2 + v2(d − M(ω)) whenever 3dω ≡ 1 (mod 8) and is constant on the remaining residue classes; the depth evolution closes exactly in terms of the anchor displacement together with a stated 3-adic absorption law; and the anchor increment along one step obeys an exact law modulo any power of 2, computable from graded residues of the state. A finite window of digits consequently decides each step in an error-free trichotomy, while a digit-budget argument shows no bounded window can decide infinite horizons — localizing the difficulty of the problem in the digit supply of the anchors. On the cycle side, a one-line elimination identity yields short rederivations of the classical exclusions for cycles of one, two, and three blocks. Our main new theorem is a sharp dichotomy for counting arguments: a trim uniform in the number of blocks p exists, giving effective finiteness at every period, but its constant necessarily degrades like (log2 3)−p — an explicit family of near-counterexamples (staircases: geometric climbs closed by a single crash, precisely divergent-orbit profiles bent into loops) shows size-counting cannot do better, so uniform cycle exclusion requires arithmetic (divisibility) input, not sharper counting. Finally we state the equidistribution hypothesis implicit in the classical heuristics as a precise conjecture about an exactly computable product law, prove its consequences conditionally, and report a calibration campaign whose four apparent anomalies all dissolved under controls — one of them via an exact routing lemma that a biased estimator had been reflecting.}},
  month     = {{jul}},
  version   = {{v1, github commit d77cb4b}},
}
```

Card as displayed (`/htmx/paper-card/Macindoe2026`): title and author as above,
year **2026**, link **DOI 10.5281/zenodo.21273548**, status badge **"☆ Wishlist
2026"**, **wishlist count 1**, formalisations **0**, reviews **0**.

Detail fragment (`/htmx/paper-detail/Macindoe2026`), verbatim:

> **Formalisations (0)** … "No formalisations yet." … "+ Add Formalisation"
> **Reviews (0)** … "No reviews yet." … "+ Add Review Link"

**The formalisation slot is empty, exactly as he says.** Recorded observations,
flat:

- The catalogued paper is **paper 1 at its v1 DOI** (`10.5281/zenodo.21273548`).
  The v2 DOI (`10.5281/zenodo.21421120`) and the mirror paper
  (`10.5281/zenodo.21303918`) are **not** separately catalogued under this key,
  and no other `Macindoe` entry was found.
- The BibTeX is a **Zenodo export**, `version = {{v1, github commit d77cb4b}}` —
  i.e. it is our own Zenodo metadata, taken over as-is.
- **Whose entry it appears to be: not visible.** The site's public fragments show
  no submitter attribution for any entry, so who added `Macindoe2026` cannot be
  established from a read-only look. Recorded as not determinable, not as
  unknown-to-us. One person has wishlisted it (count 1).

### 1.6 The submission process the site documents (fact only)

From `/contribute`: "Add a paper. Add papers to the database by entering their
BibTeX or filling in the metadata manually." To contribute a formalisation:
"Pick a paper and formalise its results in the proof assistant of your choice",
disclosing any AI tools and which models, after which "you can mark it as 'ready
to be audited'." Audits are written by someone other than the formalisation's
authors, unless the formalisation was essentially done by AI. Login is by
**"Continue with GitHub"** or **"Continue with Discord"**. Project resources
named on the page: `https://github.com/orgs/ccchallenge-org/repositories`,
`https://github.com/orgs/ccchallenge-org/discussions`, and a Discord invite.

**Whether we ever use any of this is the author's call and is not this session's
business.** Nothing was submitted, and no account exists.

### 1.7 URLs consulted (all `GET`, all public)

`https://ccchallenge.org/` · `/story` · `/method` · `/contribute` ·
`/htmx/stats` · `/htmx/stats-cards` · `/htmx/paper-list?status=audited` ·
`/htmx/paper-list?status=formalising` ·
`/htmx/paper-list?status=waiting_to_be_audited` · `/htmx/paper-list?q=Steiner` ·
`/htmx/paper-detail/Macindoe2026` · `/htmx/paper-detail/Eliahou1993` ·
`/htmx/paper-detail/Hercher2023` · `/htmx/paper-detail/Steiner1978` ·
`/htmx/paper-detail/SimonsWeger2005` · `/htmx/paper-card/Macindoe2026` ·
`/api/papers/Macindoe2026/bibtex`

The `/htmx/…` fragment routes are the site's own public read endpoints, read
from its open-source backend (`github.com/ccchallenge-org/ccchallenge`,
`backend/main.py`) so that the exact status vocabulary and the bucket arithmetic
could be quoted rather than inferred from the rendered page.

---

## Item 2 — Hercher's published numbers (checked 2026-07-28)

**Citation, as our own record already pins it** (`briefs/merle-la8-t1-check-findings.md`,
the Hercher adjudication — the authority for this item): C. Hercher, *There are
no Collatz-m-Cycles with m ≤ 91*, **Journal of Integer Sequences 26 (2023),
Article 23.3.5**; arXiv:2201.00406, v1 2 Jan 2022, v2 23 Jan 2022, **v3 4 Apr
2023**. Confirmed at the arXiv listing this session.

### 2.1 `m >= 92` — right figure, right symbol, and it is his

The abstract, verbatim (arXiv v3):

> The Collatz conjecture (or "Syracuse problem") considers recursively-defined
> sequences of positive integers where $n$ is succeeded by $\tfrac{n}{2}$, if
> $n$ is even, or $\tfrac{3n+1}{2}$, if $n$ is odd. The conjecture states that
> for all starting values $n$ the sequence eventually reaches the trivial cycle
> $1, 2, 1, 2, \ldots$ . We are interested in the existence of nontrivial
> cycles.
>
> Let $m$ be the number of local minima in such a nontrivial cycle. Simons and
> de Weger proved that $m \geq 76$. With newer bounds on the range of starting
> values for which the Collatz conjecture has been checked, one gets $m \geq
> 83$. In this paper, we prove $m \geq 92$.
>
> The last part of this paper considers what must be proven in order to raise
> the number of odd members a nontrivial cycle has to have to the next bound --
> that is, to at least $K\geq1.375\cdot 10^{11}$. We prove that it suffices to
> show that, for every integer smaller than or equal to $1536\cdot2^{60}=3\cdot
> 2^{69}$, the respective Collatz sequence enters the trivial cycle. This
> reduces the range of numbers to be checked by nearly $60\%$.

- **Is `m` his cycle-length parameter?** It is *a* cycle-length parameter of
  his, and it is his paper's headline one: **"Let $m$ be the number of local
  minima in such a nontrivial cycle."** It is **not** the same parameter as `K`,
  which he defines as the number of **odd members**. His paper carries both, and
  they are not interchangeable.
- **Is 92 the right figure and the right symbol?** **Yes.** Theorem 23 (the
  paper's main theorem) reads *"There are no Collatz m-cycles with m ≤ 91"*,
  equivalently `m ≥ 92`; the abstract states `m ≥ 92` in exactly those symbols.
  The chain he gives is Simons–de Weger `m ≥ 76` → `m ≥ 83` on newer verified
  ranges → **`m ≥ 92`** his.
- **Against our own record: consistent.** `cycles.md` 12.7.3 and
  `publication.md` both carry Hercher as the current `m`-cycle record at
  `m ≤ 91`, and `open-problems.md` notes it confirms our crossover threshold
  `p > 91` was correctly calibrated. Nothing of ours contradicts `m ≥ 92`.
- **One flat note on the pairing.** His letter writes the published record as
  "Hercher m >= 92, K > 1.375e11". Both numbers are Hercher's and both are
  correctly quoted, but they measure **different things** — `m` counts local
  minima, `K` counts odd members — and only `K` is on the same axis as the
  note's own exclusions (T1's length `n` = number of odd elements, `= p+1`, the
  same convention as `K`; `briefs/merle-la8-t1-check-findings.md` §(g)). Recorded
  as a fact about the two symbols, not as an error in his sentence.

### 2.2 `K > 1.375·10^11` — as our record has it, unchanged

Corollary 29, as our la8 record quotes it: *"If `X₀ ≥ 1536·2^60 = 3·2^69` then
every nontrivial cycle contains at least `K > 1.375·10^11` odd numbers."* The
underlying threshold is exactly `q₂₃ = 137528045312`, the printed `1.375·10^11`
being a rounded-down display (`137500000000`); the bound stands today because
Barina's verification reaches `2^71`. Nothing in this session's reading changes
any part of that adjudication.

### 2.3 The clause "on a strictly weaker verification hypothesis than ours" — **direction CONFIRMED, and it agrees with our record**

His sentence, verbatim: *"The note's exclusions are weaker than the published
record (Hercher m >= 92, K > 1.375e11, and on a strictly weaker verification
hypothesis than ours)."*

**Weaker for whom, and in which direction.** The clause sits inside the
parenthesis describing **the published record**, and "than ours" fixes the
comparison: it says **Hercher's** results are obtained on a verification
hypothesis strictly weaker than the one **our** exclusion instantiates. That is
the same direction our own adjudication records
(`briefs/merle-la8-t1-check-findings.md` §(g)): *"Hercher's `1.375·10^11` needs
only `X₀ ≥ 3·2^69` of verification — strictly less than the `2^71` this chain
instantiates."*

The three verification inputs, put in one unit so the direction cannot be read
two ways (`2^60` throughout; recomputed exactly this session):

| Result | Verification input `X₀` needed | In units of `2^60` |
|---|---|---|
| Hercher, Thm 23, `m ≥ 92` | `704·2^60` (his Definition 4: *"As of the date of writing this paper, we have X₀ = 704·2⁶⁰"*, citing Barina) | **704** |
| Hercher, Cor. 29, `K > 1.375·10^11` | `3·2^69 = 1536·2^60` | **1536** |
| The note's own exclusion (T1, `x_min ≥ 2^71`) | `2^71 = 2048·2^60` | **2048** |

`704 < 1536 < 2048`: **both** of Hercher's published numbers rest on strictly
less verified range than ours. So the clause is true of the whole parenthesis,
not only of the `K` half — which is more than our record had established (our
record settled only the `Cor. 29` comparison; the `m ≥ 92` half is added here).

**Ambiguity worth flagging for an abstract, since the brief asks the direction
to be unambiguous.** The proposition is unambiguous as written to a reader who
parses "weaker hypothesis" in the logician's sense (assumes less, therefore the
result is *stronger*). It is ambiguous to a reader who hears "weaker" as
"lesser" and attaches it to the note rather than to Hercher — the same reading
that would flip the sentence's point. Recording the fact, not a wording: **the
asymmetry runs in Hercher's favour on both axes** — hypothesis (he needs
`3·2^69` where the note instantiates `2^71`) *and* conclusion (`1.375·10^11`
against the note's `n ≤ 3.5032·10^10`, ratio `q₂₃/35031771147 = 3.9258`,
recomputed this session). This is the correction already applied at the round-10
co-edit review (`0cb155b` → `5481d2d` / pushed as `c966875`), where the
"not apples-to-apples" clause was fixed with its origin named.

### 2.4 Is Hercher formalised anywhere we can see? **No.**

- `ccchallenge.org`, 2026-07-28: `Hercher2023` is listed, badge **☆ Wishlist**,
  **Formalisations (0)**, "No formalisations yet." (item 1.4).
- In Merle's own public stack: `collatz-conditional-cycles` uses **Simons–de
  Weger**'s `m ≥ 69` as a structure parameter, not Hercher
  (`briefs/junction-repo-recon-findings.md`); the round-11 public recon
  (`briefs/junction-public-recon-findings.md`) records Simons–de Weger as a
  genuine `axiom` declaration in `collatz-cycles-lean`. **No Hercher
  formalisation is recorded in any of his repositories.**
- Nothing of ours formalises Hercher.

So the whole `m`-cycle record chain — Steiner, Simons–de Weger, Hercher — is
unformalised as far as any public register or repository we can read shows.

### 2.5 Nothing needed computing beyond three integer comparisons

The only arithmetic in this item is `704·2^60 < 1536·2^60 = 3·2^69 < 2^71 =
2048·2^60` and the ratio `137528045312 / 35031771147 = 3.9258…`, both checked
exactly in-session. **No script is committed for this item** — there is nothing
a script would carry that the table above does not, and the substantive
computations behind these figures already have committed scripts
(`experiments/merle_la8_t1_check.py`).

---

## Item 3 — the shared repository and `NOTE.md` (fresh clone, 2026-07-28)

Method: unauthenticated `git clone https://github.com/macindoe/one-obstruction-three-faces.git`
into the session scratchpad. Nothing was pushed, branched on the remote, or
otherwise written.

### 3.1 Current HEAD: **`c966875` — unmoved**

```
c96687544fd387fd8bcff1df2c04056a2be99f3a
macindoe <begemite0.o@gmail.com>
Sun Jul 26 19:21:46 2026 +1000
Round-10 co-edits: L-A7 closed out at two keys with our margin proof offered as
the second proof at the true c_gen; L-A8 Macindoe key turned on the mathematics,
kernel claims deferred
```

This is **exactly the SHA our record expects** (HANDOFF item 1, "Round-10
co-edit: PUSHED, 2026-07-26 … shared HEAD now `c966875`"). **The repository has
not moved since our own round-10 push.** No new commits, by him or anyone; the
commit immediately below ours is still his `826970e` of 2026-07-25.

So the material fact the brief asks about is a negative one, and it is clean:
**nothing of his has landed in the shared repository since round 10**, and his
round-11 letter's proposals about `NOTE.md` are proposals only — he has not
acted on them in the file. Working tree at HEAD: `LEDGER.md`, `NOTE.md`,
`PROTOCOL.md`, `README.md`, and nothing else.

### 3.2 `NOTE.md` against the "19 July skeleton" he remembers

**The file is still the skeleton, and it still says so in its own first line.**
Header, verbatim at HEAD:

> **ARCHITECTURE DRAFT — for co-editing (Merle, 2026-07-19). Prose not started;
> this is the load-bearing skeleton, seeded the way this repository seeds
> everything: edit directly, strike freely. Every numbered claim enters via
> LEDGER.md first (all entries below have their keys turned).**

Working title, verbatim: *One obstruction, three faces: the Collatz cycle
problem between size, digits, and the local–global seam.*

**Section structure at HEAD — eight numbered sections plus an appendix list,
unchanged since the skeleton commit:**

| § | Heading, verbatim | What it carries | Ledger entries cited |
|---|---|---|---|
| 0 | The porch (elementary front door) | Gersonides 1342/43; the spent `\|q\| = 1` stock; the four real loops; the crank-proof detector | [L-A3] |
| 1 | The problem and the two shores | the cycle half; the `×3−1` mirror; the anchor correspondence with its folklore provenance (Steiner 1977, Crandall 1978, Eliahou 1993, Halbeisen–Hungerbühler 1997, Simons 2005, Simons–de Weger 2005, Lagarias's bibliographies) | — |
| 2 | Face I — size (the archimedean shadow) | the δ8 impossibility (Merle side) and the scissors; the staircase family (Macindoe side), contiguous `p ∈ {2,…,23}` | [L1] |
| 3 | Face II — digits (the 2-adic body) | reduced coordinates and the anchor walk; the transport recurrence; the repeated-word gcd law | [L-A1], [L-A2] |
| 4 | Face III — the seam (local–global) | no Hasse gap; the local obstruction at 7; the realization-height theorem | [L3], [L-A4] |
| 5 | The quantitative complements | the Benford side-asymmetry; the AEH class skeleton and its measured spectrum | [L-A3], [L4] |
| 6 | What remains, stated exactly | the residual hypothesis | [L-A4], [L-A3 cadeau B] |
| 7 | Method (the actual novelty for many readers) | two stacks never merged; the two-key rule; the ledger as spine | [L1], [L-A3] |
| — | Appendices (candidates) | A. the Lean artifact and its axiom profile; B. the shared test vectors; C. the two gateways | — |

**§6, verbatim and in full, as it stands at HEAD:**

> ## 6. What remains, stated exactly
>
> The residual hypothesis, now stated exactly: the **equidistribution of `R_r
> mod q`** along the aperiodic forced family (the *arithmetic* distribution of
> the seam residues across profiles — to be kept terminologically distinct from
> the ergodic/statistical equidistribution of AEH orbits, `aeh.md 13.6.7`; note
> that `R_r mod ℓ` is in fact non-uniform at every prime yet unconfined,
> structural bias strongest at `7 = 2³−1`, consistent with the prime-local
> probe's *no-coset-confinement* verdict; the structured refuge is closed by
> descent [L-A4]); strictly weaker than `ProductBoundThreshold`; honestly placed
> on the ×2×3 gap. The capacity–demand margin is positive and grows linearly —
> `≈ 0.27·n` in the odd-step stratum, `≈ 0.08·n` in general [L-A3 cadeau B;
> REQ-MATH-014] — so the no-conspiracy cycle-count decays like `2^(−margin)`,
> making that one equidistribution the exact remaining gap. No promise past the
> calculations.

**The abstract-or-opening: there is no abstract.** `NOTE.md` has no abstract
section and no position paragraph. The opening is **§0, "The porch (elementary
front door)"** — the Gersonides front door — reached immediately after the
header and the working title. Its text at HEAD:

> Gersonides, 1342/43, *De numeris harmonicis*, written for the composer
> Philippe de Vitry: the only pairs of harmonic numbers differing by one are
> (1,2), (2,3), (3,4), (8,9) — a mod-8 remainder argument and a two-line
> factoring. Fourteenth-century, referee-proof, and the reader meets it before
> Baker. Consequence stated immediately: the "free locks" `|q| = 1` are a
> **spent finite stock** (three tickets, dealt one north / two south), and the
> four real loops of the map — `{+1}` and `{−1, −5, −17}` — are the stock's
> biography [L-A3]. The crank-proof detector falls out as a corollary: any
> parity/speed argument forbidding loops forbids the four that exist.

Recorded against his three round-11 proposals, as facts about the file and
nothing more:

- *(i) make the counting dichotomy the load-bearing result and the three faces
  its instances* — the file does not currently name a counting dichotomy at all.
  The word "dichotomy" **does not occur in `NOTE.md`**. Its nearest present
  content is §2's pairing of the δ8 impossibility with the staircase sharpness
  as "One wall, one analytic face and one constructive face", and §6's
  capacity–demand margin. The three faces are currently coordinate,
  not instances of a stated result.
- *(ii) state the position once, early, in the abstract* — **there is no
  abstract to state it in.** The nearest thing to a position statement in the
  file is §6's closing "No promise past the calculations", which is at the end,
  not early.
- *(iii) treat the genre as mapping-and-instruments rather than announcing a
  result* — the file already leans that way: §7 is titled "Method (the actual
  novelty for many readers)", and the shared `README.md` describes the whole
  thing as "A joint technical-comparison note between two independent Collatz
  research programs" whose status line reads "note not started".

### 3.3 Is a 19 July skeleton what is actually there? **Yes structurally, no textually — and the date is off by one on his own header**

Commit history of `NOTE.md`, complete:

| Commit | Date (author TZ) | Author | What it did |
|---|---|---|---|
| `63c396d` | 2026-07-17 10:47 +1000 | macindoe | seeded the note **stub** with README/protocol/ledger |
| `f496abe` | **2026-07-18 23:48 +0200** | Eric MERLE | **seeded the architecture skeleton** (the file this record calls "the skeleton") |
| `61d2cf3` | 2026-07-23 09:16 +0200 | Eric MERLE | §4 realization-height reference made renumber-proof; pin invited on co-edit |
| `430c00c` | 2026-07-24 09:06 +1000 | macindoe | §4: pinned the realization-height reference (`itinerary.md` 14.15.5(b), Cor. 14.15.5.4) |
| `d2407b9` | 2026-07-24 09:07 +1000 | macindoe | §4: "positive integer" → "positive **odd** integer" |
| `b8842bb` | **2026-07-24 12:40 +0200** | Eric MERLE | **§4 and §6 reframed** to the no-Hasse-gap / local-obstruction and equidistribution framing |
| `6b9f2b1` | **2026-07-24 17:29 +0200** | Eric MERLE | **§6** arithmetic-vs-AEH-equidistribution disambiguation |

Three facts, stated flatly:

1. **Structurally it is the skeleton.** `git diff f496abe HEAD -- NOTE.md` is
   **2 insertions, 2 deletions, in one file** — exactly one line of §4 and one
   line of §6 rewritten. Every other line of the file, including the header, the
   working title, all eight section headings and the text of §0, §1, §2, §3, §5
   and §7, is byte-identical to the skeleton commit.
2. **Textually it is not the 19 July text.** The two rewritten lines are the
   two most load-bearing in the file — §4 (Face III, the seam) and §6 (what
   remains) — and both were rewritten **by him on 2026-07-24**, absorbing our
   two one-line pins in the process. The §4 line went from "solvable over ℝ,
   over ℤ₂, over ℤ₃ at every rotation and over ℤ at none … **no finite place
   alone will do it**" to the no-Hasse-gap / local-obstruction-at-7 statement;
   the §6 line went from a single sentence ("The residual hypothesis
   (anchor-walk rigidity beyond the spent stock), its relation to
   `ProductBoundThreshold` (strictly weaker), and its honest placement on the
   ×2×3 gap. No promise past the calculations.") to the paragraph quoted in §3.2
   above. This matches our own record exactly (HANDOFF item 1: "**§4 and §6
   rewritten by him 2026-07-24**").
3. **The date.** The skeleton commit is timestamped **2026-07-18 23:48:48
   +0200** — 18 July in his own timezone, by eleven minutes. The line *inside*
   the file says "(Merle, 2026-07-19)", and that line is his and is unchanged.
   So "the NOTE.md skeleton from 19 July" is his file's own self-description, is
   off by one day against its own commit timestamp, and in any case does not
   describe the current §4 and §6. **A misremembered date in a letter is not a
   finding of substance; it is recorded here only so that the note's shape is
   discussed against the file that exists.**

---

## Item 4 — the three faces, as `NOTE.md` presents them, and their status today

Sources: `NOTE.md` and `LEDGER.md` at shared HEAD `c966875`, plus our own wiki.
Half A checks the *independence* of the three; this item records only their
*status*. Nothing here is a recommendation.

### 4.1 The three faces and what each rests on

**Face I — size (the archimedean shadow), `NOTE.md` §2.** Two halves, one
per side.

| Half | What it is | Ledger entry | Wiki / artifact home | Status as the ledger states it |
|---|---|---|---|---|
| the δ8 impossibility + the scissors (Merle side) | why no uniform Product-Bound refinement closes the window; required exponent below Dirichlet's floor, `k_min ~ X₀^{1/2}` vs `k_max ≤ X₀^{1/3}` | **none** | — | **no ledger entry exists** (see 4.3) |
| the staircase family (Macindoe side) | the sharpness that makes the same wall constructive; contiguous verified range `p ∈ {2,…,23}` | **[L1]** as §2 cites it; the `p = 7` instance is **[L2]** | `cycles.md` §12.8.3 (staircase), §12.8.6 (the `p = 22` resolved obstruction) | **L1: `corrected` (both directions), and productive — closed 2026-07-17** — not a "two keys" entry, and not phrased as one. **L2: `two keys` (2026-07-16)** |

**Face II — digits (the 2-adic body), `NOTE.md` §3.**

| Component | Ledger entry | Wiki / artifact home | Status as the ledger states it |
|---|---|---|---|
| the transport recurrence; the collapse of the `p` divisibility conditions to one | **[L-A1]** | `itinerary.md` Lemma 14.15.9.2 (fixed-point form); his `TransportRecurrence.lean` | **both keys** on the mathematics, **plus the Lean key**: "With Macindoe's independent-code + fixed-point key, the mathematics of L-A1 now carries **both keys**, neither derived from the other." Kernel-3, 0 `sorry`, non-vacuity canary proved in Lean |
| the repeated-word gcd law | **[L-A2]** | `experiments/prime_local_probe.py`, `experiments/merle_round5_check.py`; his `REQ-MATH-012` at `ec4f229` | **two keys** (2026-07-19) |

**Face III — the seam (local–global), `NOTE.md` §4.**

| Component | Ledger entry | Wiki / artifact home | Status as the ledger states it |
|---|---|---|---|
| the closure equation, the no-Hasse-gap reading and the local obstruction at 7 | **[L3]** | `experiments/merle_pincer_check.py` (item 3); `experiments/merle_round8_check.py` part (b); his `REQ-MATH-017` | **two keys** (2026-07-17), with the 2026-07-24 correction **accepted into the two-key record** ("Correction **accepted into the two-key record**") |
| descent: no new cycle in structured families | **[L-A4]** | `cycles.md` Remark 12.6.1.4 | **two keys**, plus the **Lean key on the structured half** (`ContentDescent.lean`, kernel-3) with our statement-match recorded read-not-built |
| the realization-height theorem | **none — it is ours, cited directly** | `itinerary.md` §14.15.5(b), **Corollary 14.15.5.4**; wrong-sign clause §14.15.5(c) | not a ledger entry; a wiki citation inside the face |

### 4.2 Which faces are at two keys today, and which are not

**At two keys today:**

- **Face II, both components** — L-A1 (two keys + Lean) and L-A2 (two keys).
  This face is fully two-keyed, with a kernel key on top.
- **Face III, both ledger components** — L3 (two keys, correction absorbed) and
  L-A4 (two keys + kernel key on the structured half). Its third component, the
  realization-height theorem, is ours and carries no key because it is not a
  ledger claim.
- **Face I's Macindoe half** — via L2 (two keys) for the `p = 7` instance; L1,
  the entry §2 actually cites, is a **`corrected`** entry, not a two-key one.

**Not at two keys today:**

- **Face I's Merle half — the δ8 impossibility.** It has **no ledger entry at
  all**. `LEDGER.md` at `c966875` contains **zero** occurrences of "Product",
  "Product-Bound", "δ8", "delta8" or "scissors". The claim exists in the shared
  `README.md`'s scope sentence ("the δ8 impossibility and the staircase
  sharpness as one obstruction") and in `NOTE.md` §2 and §6
  (`ProductBoundThreshold`), and nowhere in the ledger. Under the note's own
  stated rule — the header line "**Every numbered claim enters via LEDGER.md
  first (all entries below have their keys turned)**" — this is the one
  component of the three faces that has not entered.
- **Face I's cited entry L1 is not a two-key entry.** Its status word is
  `corrected` (both directions), closed 2026-07-17; it refuted a claim on each
  side and yielded the contiguous verified range. It is a strong entry, but a
  reader checking "all entries below have their keys turned" against L1 will
  find a different status word.

### 4.3 Two further status facts, recorded flat

- **`L-A3` (B) is still conditional in the file.** §5 and §6 both lean on L-A3,
  and §6 quotes the capacity–demand margin `≈ 0.27·n` / `≈ 0.08·n` from
  "[L-A3 cadeau B; REQ-MATH-014]". The ledger's own last word on (B) at HEAD
  reads: "Status of (B): our key is turned on the `n ~ 10³` replication, and the
  asymptote is offered — **(B)'s quantification carries two keys once Merle's
  acceptance of the asymptote lands.**" Our own record (HANDOFF item 1) has his
  round-9 letter accepting the (B) constants, but **that acceptance has not been
  written into the ledger entry**, so the shared file still shows the condition
  open. Recorded as a bookkeeping gap between our record and the shared file,
  not as a disagreement.
- **The note's newest and strongest material is not in `NOTE.md` at all.**
  `L-A5`, `L-A6`, `L-A7` and `L-A8` all postdate the skeleton and none is cited
  anywhere in the file. In particular **`L-A8` — T1, the no-hair theorem, the
  kernel-checked cycle exclusion that any "machine-checked fragment of the cycle
  literature" clause would be about — appears in `LEDGER.md` at "two keys,
  scoped exactly as above" and appears in `NOTE.md` nowhere.** Its kernel claims
  became keyable only at the round-11 Lean re-audit
  (`briefs/merle-r11-ceiling-audit-findings.md`), and no ledger text has been
  written for that yet.
