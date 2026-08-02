# Brief: the exceptional tail under the two-sided space (v3 round 3, Wave 5a)

**Branch.** `v3r3-review-round3`, at `fa07929`. Work directly in `c:\Users\Ace\Documents\Collatz` on that branch. **Do not create a worktree.**

**This is a proof task, read-only.** Produce a derivation and drop-in text; change no tracked file. A separate delegate applies the round's remaining fixes after you, and will land your text.

## The gap

Round 3 moved the ambient probability space from the one-sided Bernoulli measure `B` to the two-sided `B̂` (`aeh.md` §13.2, the `π_{k,D}` paragraph). **Lemma `13.6.3`(iv) — `P_B(a ≥ j) ≤ 2·(0.93)^j` — was not re-derived.** It still reads "Under `B`" at `aeh.md` L178, and its proof conditions on "the `i` letters nearest `y_n`" and prepends letters, which is a construction of a *finite* past.

This is not cosmetic. The bound is a live dependency of the round's new material:

- **Lemma `13.2.4`(e)** (`aeh.md` L101) chooses `W ≥ D` with `2L(0.93)^W < ε'/8` and cites `13.6.3`(iii)–(iv) to make the `L`-block of capped windows an explicit function of finitely many consecutive letters. The base-case lemma the round marked **PROVED** rests on it.
- **Theorem `13.6.4`**'s (⇒) direction uses the same `2L(0.93)^W` exceptional mass.

The round's own §13.2 text asserts a relocation — that with an infinite past the reconstruction is exact almost surely, so `π_{k,D}` carries no exceptional-set caveat and the estimate "survives only where it belongs, in the finite-past bound of `13.6.4`." **Check that relocation is correct**, and then establish the bound where it is now used.

Delegate A flagged this as its open question 3 and believed it needed only a one-paragraph check. The apply delegate did not do it. The verify delegate calls it a proof dependency of the new lemma. Nobody has done the work.

## The question, precisely

The uses above are all **finite-past** statements: the `L`-block is reconstructed from a bounded letter window, and the exceptional event is that the reconstruction fails. So what is needed is a bound of the form `P_B̂(a ≥ W) ≤ 2·(0.93)^W`, with `a` the absorption of a point drawn from the *two-sided* stationary law, and the reconstruction using only `W` letters of past.

Settle:

1. Does `13.6.3`(iv)'s existing argument transfer verbatim to `B̂`, need modification, or fail?
2. Is the constant `0.93` still correct under `B̂`, or does it move?
3. Is the relocation sentence at §13.2 accurate — is the reconstruction genuinely exact almost surely under an infinite past, and does `π_{k,D}` genuinely carry no exceptional-set caveat?
4. Are `13.2.4`(e) and `13.6.4`(⇒) correct as written once (1)–(3) are settled, or does either need amending?

**One thing to consider before writing a long proof.** `13.6.5` computes the exact law of `a` under the two-sided space — `P(a=0) = 2/3`, `P(a=1) = 19/63`, `P(a ≥ 2) = 2/63` — via `ν_j`, the exact pushforward of `B^{⊗j}` under the offset formula. Those values are far below what `2·(0.93)^j` gives. If the exact law is available at every `j` by the same finite computation, the honest move may be to replace the estimate with a statement citing the exact law, or to derive a sharper geometric bound from it, rather than to port an argument that was always a crude over-estimate. Decide which is right; state your reasoning either way.

## Read first

- `aeh.md` §13.2 (the `π_{k,D}` and `B̂` paragraphs), Lemma `13.2.4` including part (e), §13.6.3(iii)–(v), Theorem `13.6.4` and its proof, Proposition `13.6.5`.
- `itinerary.md` `14.15.3.3` (the `3`-adic past-limit) and `reverse.md` `14.14.8.2`–`14.14.8.3` (the offset recursion and the synchronization corollary the proof uses).
- `briefs/v3r3-aeh-object-findings.md` §3.5 (the two-sided space, as designed) and its open question 3.
- `briefs/v3r3-verify-findings.md` — its verdict on this item and on the `13.6.4`(⇐) parenthetical, which a separate fix delegate will complete.

## Verification

`AGENTS.md`: anything marked proved needs an independent numerical check with a fresh implementation, recorded as one current line in the owning page. Your result is either a proof or a correction to one, so it qualifies.

Write scratch code to the scratchpad — **not** the repository:
`C:\Users\Ace\AppData\Local\Temp\claude\c--Users-Ace-Documents-Collatz\7ee86884-4e62-4eca-b73c-3d997568403a\scratchpad`

Check at minimum: the tail probabilities `P(a ≥ j)` computed directly against your bound at several `j`; and, if you claim the finite-past reconstruction succeeds off an event of the stated mass, the measured failure rate of that reconstruction at several past-window sizes. `experiments/aeh_symbolic.py` already contains a two-sided reconstruction check — read it, and write something that does not import it.

## Deliverable

Write **only** `briefs/v3r3-tailbound-findings.md`:

1. the verdict on (1)–(4), each stated plainly;
2. the derivation, in full;
3. **exact drop-in Markdown** for `13.6.3`(iv), plus any consequential amendment to `13.2`'s relocation sentence, `13.2.4`(e), or `13.6.4`'s proof — ready for the fix delegate to land;
4. the verification record in the form the page's other verification lines use;
5. what you could not settle, named plainly.

**If the bound fails or the constant moves**, say so immediately and prominently: the base-case lemma is currently marked PROVED on the strength of it, and the author needs to know before the branch is merged.

## Constraints

- **Read-only on every tracked file.** The one file you may write in the repository is your findings file.
- No `git` write operations of any kind: no commit, no branch, no checkout, no push, no merge.
- Write files with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes this repo's `≤`, `—`, `ε`.
- Do not renumber any monolith anchor.
- Every number and section reference verified against the file, not recalled. Note that this round rewrote much of §13.2 and §13.6; read the current text, not a findings file's quotation of it.
- Do not attempt to prove AEH. This is a bound on an exceptional event under an explicit product measure, and nothing more.
