#!/usr/bin/env python3
"""merle_r18_check.py -- fresh verification of PR #8 (round 18),
github.com/macindoe/one-obstruction-three-faces, per
briefs/merle-round18-review-brief.md (Items A, B, C, E).

Supports: briefs/merle-round18-review-findings.md.

Reproduce (from the repository root, network required -- it clones the
shared repo read-only into a temporary directory and makes read-only `gh`
and HTTPS metadata calls):

    python experiments/merle_r18_check.py > experiments/merle_r18_check_output.txt

Rules honoured:
  - imports NOTHING from any Merle repository and nothing from any earlier
    check script of ours; Python stdlib only (decimal at two precisions,
    fractions, subprocess, json, urllib);
  - the shared LEDGER.md is read with `git show <sha>:LEDGER.md` from a
    fresh clone, at two PINNED SHAs: his `main` after the round-16/17
    merges (474125d) and the PR #8 head (031c454);
  - every number the collaboration block quotes that our record can
    reproduce is recomputed from its definition, exact integers wherever a
    decision can be an integer comparison;
  - read-only throughout: clone, `git show`, `gh pr view`, two metadata GETs
    (Crossref for Knight's citation, Zenodo for the v3 record). Nothing is
    posted, pushed or written outside a temporary directory.

What this script checks:
  PART 0 -- canaries: CF of log2(3) at two precisions (q_1..q_5 = 1,2,5,12,41);
            the four small real cycles' odd counts and seam gaps.
  PART 1 -- the pinned SHAs exist; PR #8's diff is +3/-0 in LEDGER.md; the
            L-A10 entry at 031c454 equals the entry at 474125d plus exactly
            one added line; that line quotes "The second key turns on L-A10."
            and that sentence occurs verbatim in our posted PR #4 review
            (APPROVED, macindoe).                                   (Item A.1)
  PART 2 -- per entry, at both SHAs: the opening status line, every
            `Key status` / `Status:` occurrence, first and last; the set of
            entries opening `DRAFT — one key`; the entries whose last
            `Key status` occurrence still reads one key / DRAFT; compared
            with our record's standing per entry.                   (Item A.2)
  PART 3 -- the block's numbers: the T1 direct floor and integral window,
            "<= 4.95e10", Hercher's 1.375e11 and its verification premise
            3*2^69 <= 2^71, the L-A9 margin, the L-A7 constants, the -17
            isolated peak, Knight's citation, the v3 record.         (Item B)
  PART 4 -- occurrence lists in our tracked files (this window's own files
            excluded so the output is stable): Gersonides with the year
            each occurrence gives; "PROTOCOL §13".                  (Items C, E)
"""

import json
import math
import os
import re
import subprocess
import sys
import tempfile
import urllib.request
from decimal import Decimal, getcontext
from fractions import Fraction

sys.stdout.reconfigure(encoding="utf-8", newline="\n")

REPO_URL = "https://github.com/macindoe/one-obstruction-three-faces.git"
REPO_SLUG = "macindoe/one-obstruction-three-faces"
MAIN_SHA = "474125de06e10d8fd32126eed4e6f5466cca9e36"   # his main after #6/#7 merges
R18_SHA = "031c454f54c5e531bebe7e532af051d7e2bf1b3b"    # PR #8 head
OUR_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CHECKS = 0
FAILURES = 0


def check(label, ok, detail=""):
    global CHECKS, FAILURES
    CHECKS += 1
    if not ok:
        FAILURES += 1
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {label}" + (f"   ({detail})" if detail else ""))
    return ok


def run(cmd, cwd=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True)
    if r.returncode != 0:
        raise RuntimeError(f"command failed: {cmd}\n{r.stderr.decode('utf-8', 'replace')}")
    return r.stdout.decode("utf-8")


def head(title):
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


# ---------------------------------------------------------------------------
# Number-theory helpers (written fresh)
# ---------------------------------------------------------------------------

def log2_3(prec):
    getcontext().prec = prec
    return Decimal(3).ln() / Decimal(2).ln()


def cf_terms(x, n):
    """First n partial quotients of a positive Decimal x."""
    out = []
    for _ in range(n):
        a = int(x)
        out.append(a)
        frac = x - a
        if frac == 0:
            break
        x = 1 / frac
    return out


def convergents(terms):
    p0, q0, p1, q1 = 1, 0, terms[0], 1
    res = [(p1, q1)]
    for a in terms[1:]:
        p0, q0, p1, q1 = p1, q1, a * p1 + p0, a * q1 + q0
        res.append((p1, q1))
    return res


def odd_cycle(x0):
    """Odd elements of the 3x+1 orbit of an odd integer x0 until it returns,
    with the total halving count K (works for negative x0 too)."""
    odds, K, x = [], 0, x0
    while True:
        odds.append(x)
        y = 3 * x + 1
        while y % 2 == 0:
            y //= 2
            K += 1
        x = y
        if x == x0:
            return odds, K
        if len(odds) > 1000:
            raise RuntimeError("no return")


# ---------------------------------------------------------------------------
head("PART 0 -- canaries")
# ---------------------------------------------------------------------------
t150 = cf_terms(log2_3(150), 30)
t280 = cf_terms(log2_3(280), 30)
check("CF of log2(3): 30 partial quotients agree at 150 and 280 digits", t150 == t280)
conv = convergents(t150)
qs = [q for _, q in conv]
check("CF canary: q_1..q_5 = 1, 2, 5, 12, 41 (1-based, q_1 = 1)",
      qs[1:6] == [1, 2, 5, 12, 41] or qs[0:5] == [1, 1, 2, 5, 12],
      f"first denominators {qs[:7]}")
for x0, n_exp, K_exp in ((1, 1, 2), (-1, 1, 1), (-5, 2, 3), (-17, 7, 11)):
    odds, K = odd_cycle(x0)
    check(f"cycle of {x0}: {n_exp} odd element(s), K = {K_exp}",
          (len(odds), K) == (n_exp, K_exp), f"n={len(odds)}, K={K}, q=2^K-3^n={2**K - 3**len(odds)}")


# ---------------------------------------------------------------------------
head("PART 1 -- fresh clone, pinned SHAs, the L-A10 amendment (Item A.1)")
# ---------------------------------------------------------------------------
tmp = tempfile.mkdtemp(prefix="merle_r18_")
clone = os.path.join(tmp, "shared")
run(["git", "clone", "-q", REPO_URL, clone])
run(["git", "fetch", "-q", "origin", "refs/pull/8/head:pr8"], cwd=clone)
for sha, name in ((MAIN_SHA, "main after #6/#7"), (R18_SHA, "PR #8 head")):
    t = run(["git", "cat-file", "-t", sha], cwd=clone).strip()
    check(f"pinned SHA {sha[:7]} ({name}) exists as a commit", t == "commit")
pr8_head = run(["git", "rev-parse", "pr8"], cwd=clone).strip()
check("refs/pull/8/head is 031c454 (PR #8 unmoved)", pr8_head == R18_SHA, pr8_head[:7])
parent = run(["git", "rev-parse", R18_SHA + "^"], cwd=clone).strip()
check("PR #8 is one commit on 474125d", parent == MAIN_SHA, parent[:7])

numstat = run(["git", "diff", "--numstat", MAIN_SHA, R18_SHA], cwd=clone).split("\n")
numstat = [l.split("\t") for l in numstat if l.strip()]
print("  numstat 474125d..031c454:")
for a, d, f in numstat:
    print(f"    +{a} -{d}  {f}")
ns = {f: (int(a), int(d)) for a, d, f in numstat}
check("diff is +136/-0 over exactly three files",
      sum(a for a, _ in ns.values()) == 136 and sum(d for _, d in ns.values()) == 0 and len(ns) == 3)
check("LEDGER.md is +3/-0", ns.get("LEDGER.md") == (3, 0))

L_main = run(["git", "show", f"{MAIN_SHA}:LEDGER.md"], cwd=clone).split("\n")
L_r18 = run(["git", "show", f"{R18_SHA}:LEDGER.md"], cwd=clone).split("\n")


def entries(lines):
    """Split the ledger into entries at '## ' headings; return ordered
    list of (id, start_index, end_index) with 0-based indices."""
    heads = [(i, l) for i, l in enumerate(lines) if l.startswith("## ")]
    out = []
    for j, (i, l) in enumerate(heads):
        m = re.match(r"## (L-?A?\d+)\b", l)
        eid = m.group(1) if m else l[3:20]
        end = heads[j + 1][0] if j + 1 < len(heads) else len(lines)
        out.append((eid, i, end))
    return out


E_main = entries(L_main)
E_r18 = entries(L_r18)
ids = [e for e, _, _ in E_main]
print(f"  entries at 474125d: {', '.join(ids)}")
check("same 15 entries, same order, at both SHAs",
      ids == [e for e, _, _ in E_r18] and len(ids) == 15)


def block(lines, E, eid):
    for e, a, b in E:
        if e == eid:
            return lines[a:b]
    raise KeyError(eid)


a10_main = block(L_main, E_main, "L-A10")
a10_r18 = block(L_r18, E_r18, "L-A10")
added = [l for l in a10_r18 if l not in a10_main]
check("L-A10 at 031c454 = L-A10 at 474125d plus exactly one line, nothing removed",
      len(a10_r18) == len(a10_main) + 1 and len(added) == 1
      and [l for l in a10_r18 if l != added[0]] == a10_main)
amend = added[0] if added else ""
print(f"  the added line: {amend}")
QUOTE = "The second key turns on L-A10."
check("the amendment line carries the quote verbatim and reads 'two keys'",
      QUOTE in amend and "two keys" in amend)
ks_idx = [i for i, l in enumerate(a10_r18) if l.startswith("**Key status")]
check("the amendment sits directly beneath L-A10's Key status line",
      len(ks_idx) == 1 and a10_r18[ks_idx[0] + 1] == amend)
for eid in ids:
    if eid == "L-A10":
        continue
    if block(L_main, E_main, eid) != block(L_r18, E_r18, eid):
        check(f"{eid} unchanged by PR #8", False)
check("every other entry byte-identical between the two SHAs",
      all(block(L_main, E_main, e) == block(L_r18, E_r18, e) for e in ids if e != "L-A10"))
pre_main = L_main[:E_main[0][1]]
pre_r18 = L_r18[:E_r18[0][1]]
pre_added = [l for l in pre_r18 if l not in pre_main]
check("the head gains exactly the reading note (plus one blank line)",
      len(pre_r18) == len(pre_main) + 2 and len([l for l in pre_added if l.strip()]) == 1
      and pre_added[0].startswith("**Reading note (Merle, 2026-10-02, round 18).**"))
reading_note = [l for l in pre_added if l.strip()][0] if pre_added else ""

reviews = json.loads(run(["gh", "pr", "view", "4", "--repo", REPO_SLUG, "--json", "reviews"]))["reviews"]
ours = [r for r in reviews if r["author"]["login"] == "macindoe" and r["state"] == "APPROVED"]
check("PR #4 carries exactly one APPROVED review by macindoe", len(ours) == 1,
      ours[0]["submittedAt"] if ours else "none")
check("that review contains 'The second key turns on L-A10.' verbatim",
      bool(ours) and QUOTE in ours[0]["body"])
check("the review's date matches the amendment's '2026-09-12'",
      bool(ours) and ours[0]["submittedAt"].startswith("2026-09-12") and "2026-09-12" in amend)


# ---------------------------------------------------------------------------
head("PART 2 -- status lines per entry (Item A.2)")
# ---------------------------------------------------------------------------

def first_status_line(blk):
    for l in blk[1:]:
        if l.strip():
            return l.strip()
    return ""


def occurrences(blk, pat):
    out = []
    for i, l in enumerate(blk):
        for m in re.finditer(pat, l):
            out.append((i, l[m.start():m.start() + 110].replace("\n", " ")))
    return out


KS = r"Key status"
ST = r"(?<![A-Za-z])Status:?\*?\*?:? |Status: "

# Our record's standing per entry (HANDOFF.md item 1, "Ledger state"),
# reduced to the word that matters for the reading rule.
OUR_RECORD = {
    "L1": "corrected", "L2": "two keys", "L3": "two keys (corrected, accepted)",
    "L-A1": "two keys", "L4": "two keys (measured)", "L-A2": "two keys",
    "L-A3": "two keys", "L-A4": "two keys", "L-A5": "two keys",
    "L-A6": "two keys", "L-A7": "two keys", "L-A8": "two keys (incl. round-16 block, review 2026-09-26)",
    "L-A9": "two keys on the Dirichlet half (h1 accepted 2026-08-17)",
    "L-A10": "two keys (review 2026-09-12)", "L-A11": "two keys",
}

for label, L, E in (("474125d (main)", L_main, E_main), ("031c454 (PR #8)", L_r18, E_r18)):
    print(f"\n  --- at {label} ---")
    for eid, a, b in E:
        blk = L[a:b]
        fs = first_status_line(blk)
        ks = occurrences(blk, KS)
        print(f"  {eid}: opens: {fs[:90]}")
        if ks:
            print(f"      Key status x{len(ks)}; first (+{ks[0][0]}): {ks[0][1][:100]}")
            if len(ks) > 1:
                print(f"      last  (+{ks[-1][0]}): {ks[-1][1][:100]}")
        else:
            st = [o for o in occurrences(blk, r"Status: ") + occurrences(blk, r"\*\*Status") ]
            st.sort()
            if st:
                print(f"      no `Key status`; last `Status` (+{st[-1][0]}): {st[-1][1][:100]}")
            else:
                print("      no `Key status` and no `Status:` line")
        print(f"      our record: {OUR_RECORD[eid]}")

print()
opens_draft_one_key = [e for e, a, b in E_r18 if first_status_line(L_r18[a:b]).startswith("**DRAFT — one key")]
print(f"  entries opening `DRAFT — one key` at 031c454: {opens_draft_one_key}")
check("exactly the five he names open with `DRAFT — one key`",
      opens_draft_one_key == ["L-A4", "L-A6", "L-A7", "L-A8", "L-A9"])
opens_draft_coedit = [e for e, a, b in E_r18 if first_status_line(L_r18[a:b]).startswith("**DRAFT — for co-editing")]
print(f"  entries opening `DRAFT — for co-editing`: {opens_draft_coedit}")
check("four more open with a superseded `DRAFT — for co-editing` line (L-A1, L4, L-A2, L-A3)",
      opens_draft_coedit == ["L-A1", "L4", "L-A2", "L-A3"])
opens_seeded = [e for e, a, b in E_r18 if "Seeded at one key" in first_status_line(L_r18[a:b])]
check("L-A10 opens `Seeded at one key` (a one-key opener of a different wording)",
      opens_seeded == ["L-A10"])
no_ks = [e for e, a, b in E_r18 if not occurrences(L_r18[a:b], KS)]
print(f"  entries with no `Key status` line at all: {no_ks}")
check("eight entries carry no `Key status` line (their status sits in a `Status` sentence or a key-turn line)",
      no_ks == ["L1", "L2", "L3", "L-A1", "L4", "L-A2", "L-A3", "L-A4"])
la4 = block(L_r18, E_r18, "L-A4")
check("L-A4's two-key standing is carried by 'Status: **two keys**' inside its Macindoe key-turn paragraph",
      any(l.startswith("**Macindoe key turned (2026-07-24)") and "Status: **two keys**" in l for l in la4))

def last_ks_text(eid):
    blk = block(L_r18, E_r18, eid)
    ks = occurrences(blk, KS)
    i = ks[-1][0]
    line = blk[i]
    j = line.find("Key status", line.find("Key status") if line.count("Key status") == 1 else 0)
    # take the text from the LAST occurrence on that line
    j = line.rfind("Key status")
    return line[j:j + 240]

la8_last = last_ks_text("L-A8")
print(f"  L-A8 last `Key status`: {la8_last[:120]}")
check("L-A8's last `Key status` occurrence (the round-16 block) still reads 'one key (Merle)'",
      la8_last.startswith("Key status on this block: one key (Merle)"))
la9_last = last_ks_text("L-A9")
print(f"  L-A9 last `Key status`: {la9_last[:120]}")
la9 = block(L_r18, E_r18, "L-A9")
ks_i = [i for i, l in enumerate(la9) if l.startswith("**Key status")][-1]
check("L-A9's last `Key status` line says the entry stays DRAFT until h1 is accepted, with no condition-met stamp",
      "stays **DRAFT** until offer h1 is accepted" in la9[ks_i] and "Condition met" not in la9[ks_i])
acc_i = [i for i, l in enumerate(la9) if l.startswith("**Merle — round-12 offers h1–h5 accepted (2026-08-17).**")]
check("...while h1's acceptance (2026-08-17) sits ABOVE that line, not after it",
      len(acc_i) == 1 and acc_i[0] < ks_i)
check("...and that acceptance names the second key: 'this round-13 pull request's review turns it'",
      "this round-13 pull request's review turns it" in la9[acc_i[0]])
la10_last = last_ks_text("L-A10")
check("L-A10's `Key status` line itself still reads 'one key (Merle)'; the 'two keys' is the italic amendment beneath it",
      la10_last.startswith("Key status: one key (Merle)"))
for eid, stamp in (("L-A5", "(Condition met, 2026-07-24"), ("L-A7", "Key status (2026-07-26): two keys")):
    blk = block(L_r18, E_r18, eid)
    check(f"{eid}: its last `Key status` statement records two keys ({stamp[:28]}...)",
          any(stamp in l for l in blk))
check("the reading note names the rule 'last `Key status` line'",
      "its **last** `Key status` line" in reading_note)


# ---------------------------------------------------------------------------
head("PART 3 -- the block's numbers (Item B)")
# ---------------------------------------------------------------------------
X = 2 ** 71
floors = []
for prec in (150, 280):
    getcontext().prec = prec
    ln2 = Decimal(2).ln()
    w_direct = (Decimal(3) * X * ln2 / 2).sqrt()
    w_chain = (Decimal(3) * X * ln2 / 4).sqrt()
    floors.append((int(w_direct), int(w_chain)))
check("direct and chain floors agree at 150 and 280 digits", floors[0] == floors[1])
fd, fc = floors[0]
check("T1 direct floor = 49547666543", fd == 49547666543, str(fd))
check("chain floor = 35035491004", fc == 35035491004, str(fc))
# integral window: largest n with 2000 n^2 <= 2079 X (693/1000 < ln 2)
n_int = math.isqrt(2079 * X // 2000)
while 2000 * (n_int + 1) ** 2 <= 2079 * X:
    n_int += 1
while 2000 * n_int ** 2 > 2079 * X:
    n_int -= 1
check("integral (kernel-canary) window = 49542405870", n_int == 49542405870, str(n_int))
check("693/1000 < ln 2 exactly (so the integral window sits inside the exact one)",
      Fraction(693, 1000) < Fraction(str(Decimal(2).ln())) and n_int <= fd)
check("'length <= 4.95e10' is a true under-statement: 49500000000 <= integral window <= exact floor",
      49500000000 <= n_int <= fd)
check("4.95e10 is the 3-significant-figure rounding of both windows",
      round(fd / 1e10, 2) == 4.95 and round(n_int / 1e10, 2) == 4.95)
la8 = block(L_r18, E_r18, "L-A8")
check("'length' in T1 is n, the number of odd elements (L-A8's round-16 block: 'a cycle of the odd map with `n` elements')",
      any("for a cycle of the odd map with `n` elements all `≥ X`" in l for l in la8))
q_by_index = {i: q for i, q in enumerate(qs)}
# locate q21, q22, q23 by value as the standing record numbers them
qa = [q for q in qs if q > 6.5 * 10 ** 9][:3]
check("the next three convergent denominators past 6.5e9: 6586818670, 65470613321, 137528045312",
      qa == [6586818670, 65470613321, 137528045312], str(qa))
below = [q for q in qs if 1 <= q <= fd]
check("22 convergents lie below the direct floor (q_0 = q_1 = 1 counted as two, the record's count)",
      len(below) == 22 and below[-1] == 6586818670, f"{len(below)} convergents, {len(set(below))} distinct denominators")
check("Hercher's 1.375e11 is q_23 = 137528045312 rounded to 4 s.f.",
      round(137528045312 / 1e11, 3) == 1.375)
check("the T1 window is weaker than Hercher's bound: 49547666543 < 1.375e11", fd < 137500000000)
check("Hercher's sufficiency premise (verification to 3*2^69) is met by Barina's 2^71",
      3 * 2 ** 69 <= 2 ** 71 and 1536 * 2 ** 60 == 3 * 2 ** 69)

# L-A9: c* = ln(3 X0 - K_H)/ln(K_H) - 1 with K_H = 1.375e11 (the entry's chain
# m <= (k^(c+1)+k)/3 closing at k = K_H), margin to Dirichlet's floor c >= 1
margins = []
for prec in (60, 120):
    getcontext().prec = prec
    KH = Decimal(137500000000)
    cstar = (Decimal(3 * X) - KH).ln() / KH.ln() - 1
    margins.append(1 - cstar)
check("L-A9 c* stable at 60 and 120 digits", abs(margins[0] - margins[1]) < Decimal("1e-40"))
c_star = 1 - margins[0]
print(f"  c* = {float(c_star):.6f}, margin 1 - c* = {float(margins[0]):.6f}")
check("L-A9: c* = 0.9617 and the margin 1 - c* = 0.0383 (= 2 - mu*)",
      round(float(c_star), 4) == 0.9617 and round(float(margins[0]), 4) == 0.0383)
check("'about 0.04' is the 1-significant-figure rounding of 0.0383",
      round(float(margins[0]), 2) == 0.04)

# L-A7: the kernel's rational 1/13 vs the exact constant c_gen
getcontext().prec = 60
b = log2_3(60)
lg = lambda v: v.ln() / Decimal(2).ln()
c_gen = b - b * lg(b) + (b - 1) * lg(b - 1)
print(f"  c_gen = {float(c_gen):.7f}; 1/13 = {1/13:.7f}")
check("L-A7: c_gen = 0.0793186... (the exact constant, ours)", str(c_gen)[:9] == "0.0793186")
check("L-A7: the kernel's 1/13 is a weaker (smaller) constant than c_gen", Decimal(1) / 13 < c_gen)

# L-A5: -17 realises an isolated C = 1 peak -- on the negative shore
odds, K = odd_cycle(-17)
q = 2 ** K - 3 ** len(odds)
check("the -17 cycle: n = 7, K = 11, q = 2^11 - 3^7 = -139 (negative shore)", (len(odds), K, q) == (7, 11, -139))
check("139 is prime and gcd(139, 3^3 - 2^3) = gcd(139, 19) = 1 (shared content 1)",
      all(139 % d for d in range(2, 12)) and math.gcd(139, 3 ** 3 - 2 ** 3) == 1)
check("the -17 cycle is primitive (7 distinct odd elements in one period)", len(set(odds)) == 7)

# Knight's citation, at the publisher-deposited metadata (Crossref)
def get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "merle_r18_check (read-only)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))

kn = get_json("https://api.crossref.org/works/10.1016/j.disc.2025.114812")["message"]
print(f"  Crossref 10.1016/j.disc.2025.114812: {kn['title'][0]!r}, {kn['container-title'][0]}, "
      f"vol {kn.get('volume')}, issue {kn.get('issue')}, art. {kn.get('article-number')}, "
      f"issued {kn['issued']['date-parts'][0]}, DOI registered {kn['created']['date-time'][:10]}")
check("Knight: Discrete Math. 349(3), article 114812, issued 2026-03",
      (kn.get("volume"), kn.get("issue"), kn.get("article-number"), kn["issued"]["date-parts"][0][:2])
      == ("349", "3", "114812", [2026, 3]))
check("Knight: the DOI's '2025' is its registration year (online 2025), not the volume year",
      kn["created"]["date-time"].startswith("2025"))
block_text = run(["git", "show", f"{R18_SHA}:briefs/merle-site-collaboration-block.md"], cwd=clone)
check("the block's 'Discrete Math. 349 (2026), 114812' matches the volume year (issue not given)",
      "*Discrete Math.* 349 (2026), 114812" in block_text)
check("the shared ledger's L-A11 cites '349(3) (2025)' -- the online year, a correction for the ledger",
      any("**349**(3) (2025) 114812" in l for l in block(L_r18, E_r18, "L-A11")))

# the v3 record: still the latest; title; concept DOI
z = get_json("https://zenodo.org/api/records/21730505")
zv = get_json("https://zenodo.org/api/records/21730505/versions?size=20")
versions = sorted((h["metadata"]["publication_date"], h["doi"]) for h in zv["hits"]["hits"])
print(f"  Zenodo versions: {versions}")
check("v3 (10.5281/zenodo.21730505) is the latest released version",
      versions[-1][1] == "10.5281/zenodo.21730505" and z["metadata"].get("version") == "v3")
check("concept DOI is 10.5281/zenodo.21273547", z.get("conceptdoi") == "10.5281/zenodo.21273547")
title = z["metadata"]["title"]
print(f"  v3 title: {title}")
check("the block's '*Reduced coordinates for the Collatz map*' is v3's main title exactly (subtitle omitted)",
      title.split(":")[0] == "Reduced coordinates for the Collatz map"
      and "*Reduced coordinates for the Collatz map*" in block_text)


# ---------------------------------------------------------------------------
head("PART 4 -- occurrences in our tracked files (Items C, E)")
# ---------------------------------------------------------------------------
files = run(["git", "ls-files"], cwd=OUR_ROOT).split("\n")
EXCL = ("briefs/merle-round18-", "experiments/merle_r18_check")
ger, prot = [], []
for f in files:
    if not f or f.startswith("sources/") or f.startswith(EXCL):
        continue
    if f.lower().endswith((".pdf", ".png", ".jpg", ".json")):
        continue
    try:
        with open(os.path.join(OUR_ROOT, f), encoding="utf-8") as fh:
            text = fh.read()
    except (UnicodeDecodeError, OSError):
        continue
    for i, l in enumerate(text.split("\n"), 1):
        for m in re.finditer(r"Gersonid\w*|Levi ben Gers\w*", l):
            win = l[max(0, m.start() - 40):m.end() + 70]
            yrs = re.findall(r"\b13[0-9]{2}(?:/[0-9]{2})?\b", win)
            ger.append((f, i, ",".join(yrs) if yrs else "-"))
        for m in re.finditer(r"PROTOCOL(?:\.md)? ?§ ?13", l):
            prot.append((f, i))
ger = sorted(set(ger))
by_year = {}
for f, i, y in ger:
    by_year.setdefault(y, []).append(f"{f}:{i}")
for y in sorted(by_year):
    print(f"  Gersonides with year {y}: {len(by_year[y])}")
    if y != "-":
        for loc in by_year[y]:
            print(f"      {loc}")
check("our tracked files give the year both ways ('1342/43' and '1343')",
      "1342/43" in by_year and "1343" in by_year)
print(f"  'PROTOCOL §13' occurrences (excluding this window's files): {len(prot)}")
for f, i in prot:
    print(f"      {f}:{i}")
check("'PROTOCOL §13' occurs only in briefs/ (session records), no wiki page",
      all(f.startswith("briefs/") for f, _ in prot))
proto = run(["git", "show", f"{MAIN_SHA}:PROTOCOL.md"], cwd=clone)
secs = re.findall(r"^## (\d+)\.", proto, re.M)
check("PROTOCOL.md at 474125d has sections 1-7 and no section 13", secs == [str(k) for k in range(1, 8)],
      ",".join(secs))

print()
print("=" * 78)
print(f"TOTAL: {CHECKS} checks, {FAILURES} failures")
print("=" * 78)
sys.exit(1 if FAILURES else 0)
