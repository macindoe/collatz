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
