# Findings: propagate the shifted word into the paper (v3 round 5)

Branch `v3r5-shifted-word`, cut from `main` at `6b9716a`, worked in
`c:\Users\Ace\Documents\Collatz` directly. No worktree, no push, no merge, no
rebase, no branch switch.

**The brief's index analysis holds, and holds as an exact identity in the
paper's own `S` rather than only in law.** Both repairs are made; the declined
recommendation is not implemented and is answered below with its evidence.

---

## 1. Which word the paper's display is about, and how that was established

Round 4 corrected this line twice and both corrections were wrong, so the word
was re-derived from the definitions rather than from any prose about them.

**The definitions used, each read in the file.**

| where | what it says |
|---|---|
| `itinerary.md` `14.15.1.1` | `stratum(y) = (m(y), r(y))`, `m = v₂(y+1)`, `q = (y+1)/2^m`, `r = v₂(3^m q − 1)`, `G(y) = (3^m q − 1)/2^r` — total on all positive odd `y` |
| `itinerary.md` `14.15.1.2` | a length-`n` word at `y` is `stratum(y_i)`, `y_0 := y`, `y_(i+1) = G(y_i)`, `i = 0 … n−1`; `S(W) := Σ(m_i + r_i)` |
| `itinerary.md` `14.15.1.5` | the followers of `W` are exactly one residue class mod `2^(S+1)` — **the word beginning at the integer itself** |
| `aeh.md` `13.2.4` preamble | `y_(−1) = x`, `y_n = G^(n+1)(x)`, `ℓ_n = stratum(y_n)`, so `ℓ_0 = stratum(G(x))` |
| `aeh.md` `13.6.3`(i)(a) | one letter per `F`-block, letter `n` is `(m_+` of edge `n`, `s_(n+1))`, i.e. `stratum(y_n)` — the fixed one-index offset between letter time and state time |
| paper L253 | `ℓ_n = (m_(+,n), s_(n+1))` — the same letter, so the paper's `ℓ_0` is likewise `stratum(G(x))` |
| paper L254 | `S_n = Σ_(i<n)(m_i + s_i)`, **defined by what it counts**: the number of `2`'s divided out from `x` to `x_exit(n−1)` |

**The derivation.** One `G`-step out of `y` divides out exactly `m(y) + r(y)`
twos (`aeh.md` `13.2.3`: a letter occupies `m_n + r_n` steps of the one-division
map `T_1`). The extended word beginning at `x` is

```text
    stratum(x), stratum(G(x)), …, stratum(G^n(x))     — n + 1 letters,
  =  (start's own letter),  ℓ_0,  …,  ℓ_(n−1)
```

and its total exponent is therefore the number of `2`'s divided out taking `x`
through `n + 1` `G`-steps to `G^(n+1)(x) = x_exit(n)` — which is, by the paper's
own definition of `S`, **exactly `S_(n+1)`**. Not `S_(n+1)` in distribution:
`S_(n+1)` as a number, on every start.

Cross-check against `13.2.3`, which was not used to derive the above: it states
the gap between the budget count and the letter-word count as
`(m_n + s_n) − (m_0 + s_0)`. Under the reading derived here the budget count
`S_n` is the exponent of `stratum(G^i x)` for `i = 0 … n−1` and the letter count
is the same for `i = 1 … n`, so the gap is
`exp(stratum(G^n x)) − exp(stratum(x)) = (m_n + s_n) − (m_0 + s_0)`. It agrees
term for term, which fixes that the paper's `m_i + s_i` is the exponent of
`stratum(G^i(x))` and that `m_0 + s_0` is the start's own block.

So: **the paper displays the law of `ℓ_0 … ℓ_(n−1)`, which is the word one
`G`-step past the start; the cylinder theorem is a statement about the word
beginning at `x`; the word it must be applied to is the extended one of `n + 1`
letters, of exponent `S_(n+1)`.** The brief's analysis holds.

Independent corroboration already in the record, quoted from `aeh.md` L112's
Verified line rather than recalled: exact total variation of
`Law(ℓ_0, …, ℓ_(n−1))` against `B^(⊗n)` in rational arithmetic over *every* odd
start of `[2^b, 2^(b+1))` at `b = 12, 16, 20` (`n ≤ 5`) and `b = 24` (`n ≤ 3`),
18 cells — the `(n+1)`-letter tail `P_B(S_(n+1) ≥ b)` holds in all 18, the
`n`-letter tail `P_B(S_n ≥ b)` is exceeded in 15, by factors `4.45`, `8.56`,
`11.27` growing with `b`.

---

## 2. Repair 1 — the paper's finite bound

`paper/collatz-reduced-v3.tex`, the base-case paragraph. Three numbers and one
explanation.

| | before | after |
|---|---|---|
| bound | `2^{J+2}/N + P_B(S_n \ge J)` | `2^{J+2}/N + P_B(S_{n+1} \ge J)` |
| identity | `P_B(S_n \ge J) = P(Bin(J-1,½) < 2n)` | `P_B(S_{n+1} \ge J) = P(Bin(J-1,½) < 2(n+1))` |
| trailing clause | "`S_n` is the waiting time for the `2n`-th head" | "`S_{n+1}` is the waiting time for the `2(n+1)`-th head" |

The identity is the same one at a shifted index: under `B`, `S_k` is a sum of
`2k` iid geometric(½) variables, so `P_B(S_k ≥ J) = P(Bin(J−1,½) < 2k)`; at
`k = n+1` this is `< 2(n+1)`.

**The explanation, which is the part that let the error stand.** The paragraph
previously invoked the coding fact for "the first `n` blocks of a start" and
then displayed a bound for a different word, with no sentence between them. It
now reads:

> That fact is about the word beginning at `x` itself, while `ℓ_0` is the letter
> of the block *after* the start's own; it is applied here to the *extended*
> `(n+1)`-letter word — the start's own letter followed by `ℓ_0, …, ℓ_(n−1)`, of
> total exponent exactly `S_(n+1)`, the divisions from `x` down to
> `x_exit(n)` — of whose law the one displayed is a marginal.

Nothing else in the paper moved. In particular the altitude bound at L302,
`log₂ x_exit(n−1) ≥ log₂ x − S_n`, is correct as printed and was **not**
changed: the paper's `S_n` is the budget count from `x`, so unlike `13.2.4`(c)'s
letter-word form it has no leading letter missing.

One typographic consequence, handled in its own commit: the repaired display is
wider than the one it replaced (`S_(n+1)` twice, `2(n+1)` for `2n`) and ran
`31.63531pt` past the text block as a single line — an overfull hbox the
previous build did not have. It is now a `gathered` pair of lines, and "the
identity on the right" reads "the second identity" to match.

---

## 3. Repair 2 — `13.2.4`(g)'s proof source

`aeh.md` `13.2.4`(g), the budget-versus-letter offset parenthetical. It bounds
`P(m_0 + s_0 > ρΛ_N)` — the start's **own** block exponent — and attributed the
one-letter law it uses to "(a) at `n = 1`". After round 4's repair (a) is about
`stratum(G(x))`, so at `n = 1` it supplies `ℓ_0`'s law, not the start's.

**The estimate is unchanged.** The printed composite bound
`2δ_N((1 − ρ)τ) + δ_N(τ) + ρΛ_N·2^(1 − ρΛ_N)` stands exactly as it was; only
the attribution moved. No numbered claim is strengthened, weakened or
renumbered.

**The replacement source, and why it covers the start's own letter.**
`itinerary.md` `14.15.1.3`(i), which is `14.15.1.5` at length one applied to
`x`'s *own* word: `stratum(x) = (m, r)` holds on exactly one odd residue class
mod `2^(m+r+1)`. Hence for `x` uniform on the odd integers of `[N, 2N)` each
cell carries probability `2^(−(m+r))` up to a boundary error `< 2/N` (one
residue class meets an interval of length `N` in `⌊N/2^(m+r+1)⌋` or
`⌈N/2^(m+r+1)⌉` integers). Summing the `(t−1)(t−2)/2` cells *below* `t` — a
finite sum, so no unbounded cell is ever priced —

```text
    P(m_0 + s_0 >= t)  <=  t·2^(1-t)  +  (t-1)(t-2)/N.
```

At `t = ρΛ_N ≤ b` the first summand is the printed geometric term
`P_B(m + r ≥ t) = t·2^(1−t)` and the second is `< b²/N`, which sits inside
`δ_N(τ)`'s own window term `2^(Λ_N+2)/N`. So the bound the clause prints is
supplied by a source that is about the start's own letter, and every term is
still `e^(−Θ(b))`.

### The numerical check

Home: **`experiments/aeh_budget_clause.py`**, new section 6. Chosen over
`aeh_word_shift.py` because that file's subject is which word (a) is about,
while section 5 of `aeh_budget_clause.py` is already headed "the offset clause:
the law of the start's own block exponent" — this is the source for exactly
that law, so it belongs beside it. The check is exhaustive over every odd start
of `[N, 2N)`, so there is no seed; the module docstring's list of what is
checked gains item 6.

**(i) The single-class structure, and the boundary error.** Every realised
stratum cell is one residue class mod `2^(m+r+1)`, and every cell count is
within `1` of `N/2^(m+r+1)`:

```text
        N     cells   multi-class   count off by >1    max|p - 2^-(m+r)|      2/N          TV
    65536       121             0                 0            3.004e-05  3.052e-05   3.543e-04
   524288       172             0                 0            3.785e-06  3.815e-06   4.730e-05
  4194304       232             0                 0            4.619e-07  4.768e-07   7.078e-06
  1000003       190             0                 0            1.940e-06  2.000e-06   7.577e-05
```

The worst per-cell deviation tracks the predicted `2/N` at every scale — it is
the boundary error and nothing else — and the total variation against the
geometric weights falls `3.543×10⁻⁴ → 4.730×10⁻⁵ → 7.078×10⁻⁶` down the dyadic
scales. `1,000,003` is included so the estimate is not tested only on windows
where the modulus happens to divide the length.

**(ii) The tail the offset clause consumes.** `P(m_0 + s_0 ≥ t)` exactly,
against `t·2^(1−t)`, at `t = 2, 4, 6, 8, 10, 12, 14`:

- on the three dyadic windows the two agree **to the last printed digit at every
  `t`** (difference `0.000e+00` in all 21 cells) — as they must, since for
  `m + r + 1 ≤ b` the class tiles `[2^b, 2^(b+1))` a whole number of times;
- off them the boundary error becomes visible and stays inside the bound: at
  `N = 1,000,003` the differences are `2.000e-06`, `7.500e-07`, `1.750e-06`,
  `5.328e-06`, `1.398e-06`, `9.912e-07` at `t = 4 … 14`, against
  `(t−1)(t−2)/N` of `6.0e-06 … 1.56e-04`. `0` exceedances.

Full file run: `0` structural failures in all six sections
(`structural failures: tail identity 0, offset law 0, start letter 0`).

`aeh.md`'s Verified line for `13.2.4` was updated in place, still as one line,
with these numbers and with the note that the enumeration is complete so no
seed is carried.

### Any further instance of the mis-citation

**No second instance of the same defect.** Every reference to `13.2.4` in a
tracked page was read: `aeh.md` L2, L8, L30, L65, L67, L69, L84, L89, L94, L96,
L110, L114, L122, L124, L184; `index.md` L46; `open-problems.md` L86, L197,
L205, L207, L209; `stage1.md` L579, L620; `publication.md` L29; the paper at
L329, L374, L402, L437. `aeh.md` L105 — repaired here — was the only clause
deriving a statement about the start's own block from (a).

One adjacent observation, **reported and not fixed** because it is not the same
defect and is outside the brief's scope: `13.2.4`(c) says the subtracted
quantity is "the total exponent of exactly the `n + 1` letters (a) charges for"
and then transfers an event at cost `δ_N`. The identification is correct and
(a)'s printed tail term is the right one, but the transfer is licensed by the
chain *inside* (a)'s proof — `TV(Law(ℓ⁺), B^(⊗(n+1))) ≤ P_B(S_(n+1) ≥ J)` — and
not by (a)'s statement, which is a bound on the marginal. The estimate is sound
either way; the pointer would be sharper if it named the proof's chain. It is
also the clause `aeh_word_shift.py`'s C6 already exercises (`226` of `5,000`
failures without the start's own letter, `0` with it).

---

## 4. The declined recommendation, with its evidence

The reviewer recommends distinct notation for two exponent sums, on the ground
that the paper calls both `S_n`. **The author has declined this and it is not
implemented.** The evidence, in a form that answers the reviewer directly:

1. **The paper defines exactly one exponent sum.** It is L254,
   `S_n = Σ_(i<n)(m_i + s_i)`, defined by what it counts — the `2`'s divided out
   from `x` to `x_exit(n−1)`. Every subsequent use is that sum: the budget
   clause `S_n < Λ_N` (L258, L311), the altitude bound (L302), and the base-case
   display (L363–L367). There is no second sum in the section for a second
   symbol to disambiguate from.

2. **The paper never forms the other sum.** Its only use of `r_i` is L273 —
   "writing `w_i = (m_i, r_i)` for the components of the `i`-th letter of `w`,
   `B[w] = Π_i 2^(−(m_i + r_i))`" — the components of a *generic* letter inside
   the Bernoulli weight of a word, not a running total along an orbit. The
   exponent mean the section does discuss is written `E_B[m+r]` (L318, L324,
   L386) and `T_N^(−1)Σ_(n<T_N)(m_n + r_n)` (L336), never as an `S`.

3. **The single existing `S` makes the corrected display come out right, and
   exactly.** As derived in §1, the extended word covering `ℓ_0 … ℓ_(n−1)` is
   the strata of `x, G(x), …, G^n(x)` — letters `0 … n`, `n + 1` of them — and
   its total exponent is the divisions from `x` to `x_exit(n)`, which is the
   paper's `S_(n+1)` on the nose. A second symbol would have to be introduced
   only to be immediately identified with `S_(n+1)`.

   A further point in the same direction: the coding fact is stated at L348
   with a generic `S`, "the itinerary's total exponent", and the good event as
   `S + 1 ≤ J`. On the word the fact is applied to — the one beginning at `x` —
   that generic `S` and the indexed `S_(n+1)` are the same number, so the
   paragraph's two `S`'s already agree. Splitting the symbol would break that
   agreement rather than clarify it.

4. **The distinction is one the wiki needs and the paper does not.** `aeh.md`
   `13.2.3` carries both counts and says so in terms: "`S_n = Σ_(i<n)(m_i + s_i)`
   counts the divisions from `x` down to `x_exit(n−1)` and is the one the budget
   clause uses, while the letter word's own total exponent `Σ_(i<n)(m_i + r_i)`
   — the `S` of `14.15.1.5`, of the base case and of `13.2.4` — is the one the
   cylinder count is stated in." The wiki needs both because its base case and
   its budget clause are stated in different ones; the paper states both in the
   budget count, so the collision the recommendation guards against does not
   occur there. Importing the distinction immediately before a pruning round
   would add a symbol the paper never needs.

**One qualification, offered rather than concealed.** The paper does carry a
second `S` — but not the one the reviewer names, and not in this section:
L184, in the cycle elimination identity, has `S_t = Σ_(j<t) σ_j` with
`σ_j = s_j + m_(j+1)`, a cycle's own total exponent, cyclically indexed,
defined at its point of use, in Section~4 and with a different index letter.
It is not an orbit exponent sum, it never appears beside `S_n`, and v3's own
change note already records that this proposition defines `σ_j` at its point of
use. Reported here for completeness; **not changed** (renaming it would be
outside this brief, and it is not the collision described).

---

## 5. The pin

Commits, in the order the brief prescribes:

```text
  2ccbb34  13.2.4(g): the start's own block gets a source that covers it   (record)
  1663d30  paper: the finite bound is about the extended (n+1)-letter word (paper)
  e62cd12  Appendix A record pin: 03207fe -> 1663d30                       (pin, its own commit)
  4aa19a0  paper: set the corrected display on two lines, and rebuild      (typography + built PDF)
```

`1663d30` is the commit containing **both** repairs: the record repair in its
parent's tree, the paper repair in its own.

**Verified with `git show`, never the working tree**, positively and negatively,
by fixed-string count:

```text
  ---------------------------------- 1663d30   e62cd12   03207fe (old pin)
  paper: P_B(S_{n+1} \ge J)                 2         2         0
  paper: P_B(S_n \ge J)                     0         0         2
  paper: Bin(...) < 2(n+1)                  1         1         0
  paper: "extended} word of $n+1$ letters"  1         1         0
  aeh:   new (g) source at the start        1         1         0
  aeh:   "through (a) at `n = 1`"           0         0         1
  Appendix A pin text            \texttt{03207fe}  \texttt{1663d30}  \texttt{132cb4d}
```

Positive: at `1663d30` both repairs are present. Negative: at `1663d30` neither
defect remains. Negative control: at the **old** pin `03207fe` both defects are
present and the extended-word explanation is absent, so the pin move is not
vacuous.

The pin stays at `1663d30` after the typography commit. `git diff 1663d30 HEAD
-- aeh.md itinerary.md experiments/ open-problems.md` is **empty**: nothing
under the record has changed since the pinned commit, so what the pin claims —
that every wiki section and script the paper names is cited at that commit — is
unaffected by a paper-only follow-up. This matches the repo's existing
convention: the previous pin `03207fe` was likewise a record-only commit
(`aeh.md`, `experiments/aeh_word_shift.py`, `open-problems.md`), with the paper
changed afterwards in the pin commit `c964d7d`.

---

## 6. The build

Three `pdflatex -halt-on-error -interaction=nonstopmode` passes on the final
source.

| | |
|---|---|
| passes | 3, all exit `0`; `Rerun to get` count `0` after the third |
| overfull boxes | **0** |
| underfull boxes | **1** — `badness 1067`, `.tex` lines 496–497, in the bibliography (`\bibitem{lagarias}` / `\bibitem{yu}`) |
| undefined references / citations | **0** |
| pages | **18** (`435,524` bytes) |

**Baseline comparison, so the box report means something.** The pre-round source
(`6b9716a`) was built in the scratchpad under the same three passes: `17` pages,
`0` overfull, the *same* one underfull box (there at lines 489–490, the same
two bibliography items shifted by the lines added here). So the only box in the
artifact is the pre-existing one, and the overfull box that the repaired display
first introduced (`31.63531pt`) is gone.

The extra page is a real consequence of the repair, and is reported rather than
smoothed: the four added lines of explanation plus the display's second line
carry the last reference, `[18]`, onto a page of its own. The added prose was
tightened once for exactly this reason (it recovered reference `[17]`); a
further cut would have had to drop the gloss tying `S_(n+1)` to
`x_exit(n)`, which is the sentence's load-bearing clause, so it was kept.
Reverting the display to one line would restore 17 pages at the cost of text
running ~11 mm into the margin; the clean box was preferred.

**Confirmed from the built PDF's text** (`pdftotext`), not from the source:

```text
  ... it is applied here to the extended (n + 1)-letter word -- the start's own
  letter followed by 0, . . . , n-1, of total exponent exactly Sn+1, the
  divisions from x down to xexit(n) -- of whose law the one displayed is a
  marginal.
  ...  2J+2 N + PB(Sn+1 >= J),
       PB(Sn+1 >= J) = P( Bin(J - 1, 1/2 ) < 2(n + 1) ),
  the second identity because Sn+1 is the waiting time for the 2(n + 1)-th head
  in a fair coin sequence.
```

(`ℓ` and `≥` drop out of `pdftotext`'s output; the glyphs are present in the
PDF.) Appendix A in the artifact reads "cited at commit 1663d30".

---

## 7. Found and not fixed

1. **`13.2.4`(c) leans on (a)'s proof rather than (a)'s statement** — §3 above.
   Sound as it stands; a sharper pointer would name the proof's chain.
2. **`S_t` at paper L184** — a second `S` in the cycles section, locally
   defined, different index letter, not an orbit exponent sum. §4 above.
3. **The paper's `m_i` inside `S_n` is not separately defined.** `S_n` is
   defined by what it counts, which is unambiguous and is what §1's derivation
   uses; but the summand `m_i + s_i` is only pinned down through that
   description, and reading it component-wise requires the one-index offset of
   `13.6.3`(i)(a) — `m_i` is `m_(+,i−1)`. This is a face of the indexing
   standardization left open at `open-problems.md` `11.12`, which the brief
   forbids attempting. Not touched.
4. **The extra page.** §6 above.

Not done, per the brief: no pruning, no anchor renumbered, no indexing
standardization attempted, nothing claimed about the deferred prefix result,
nothing changed in `13.3.2`, no numbered theorem's claim moved.
