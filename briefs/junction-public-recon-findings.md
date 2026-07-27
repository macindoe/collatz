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
