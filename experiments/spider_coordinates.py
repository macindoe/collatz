"""Verification for spiders.md 19.5 (the coordinates of a spider): the legs as the
doors of (Omega, D+1) (19.5.1), the hair descent map desc (19.5.2), the member formula
and the lens identity with the admissible-word residue claim (19.5.3), the raw-Collatz
dictionary of a spider (19.5.4), and the two searches for a walk-free identifier
(19.5.5).

Fresh code: imports nothing from any other file in this repository (spider_layer.py,
spider_explorer_check.py, peak_comb.py, comb_signatures.py exist and are neither
imported nor copied). Exact Python integers at every pass/fail decision; numpy is used
only for the E.1 measurement tables, on int64 arrays whose magnitudes are asserted
below 2^62 before use. Positive comb only (every rule is sign-blind, comb.md 18.8; not
exercised here). Seed 20260926; 2026-09-26.

What it does, in order (canaries first):
  Part 0. Canaries: (1,2) with t = 0 and legs (11,1), (7,1); (5,2) with t = 1, legs
    (59,1), (13,1), the door-1 child (13,2) and top-door child (13,1) sharing the core
    13; the orphan link (17,1) descending by desc to 13 and owned by (5,2); the lens at
    17 giving 160 = 2^5 * 5; the b >= 3 fixed hair on (1,4).
  Part A. Item A (19.5.1) on random abdomens (D = 2..14) and exhaustively on every
    abdomen of the level-18 census; the D = 1 instance of claim 1 on random depth-1
    nodes. Children are computed by the comb's children rule (comb.md 18.2.3) from
    first principles; the claims are computed from the door formula of (Omega, D+1);
    every child is also sent back through the parent rule (18.2.1).
  Part B. Item B (19.5.2): desc against the comb parent on random depth-1 nodes and on
    every depth-1 node of the census; the raw form on the same nodes; the owner by
    desc-iteration against the owner by comb-parent ascent (Theorem 19.2.2).
  Part C. Item C (19.5.3): the recursion, the member formula and both lens identities
    at every member of every census spider (every hair walked to its true end by
    ground-truth arithmetic, past the census boundary) and on random spiders; the
    admissible-word residue claim as a sufficiency check (random lifts) and an exact
    full-coset measurement of the least modulus.
  Part D. Item D (19.5.4): the raw translation at every member walked in Part C.
  Part E. Item E (19.5.5): E.1 the affine-lens and comb-quantity constancy tables with
    a shuffled baseline; E.2 the exact residue modulus of the hair position, and the
    construction showing the owner's D and Omega mod 3 are not determined by any
    bounded residue at any position.

Single reproducing command (writes experiments/spider_coordinates_output.txt itself,
no shell redirection):

    python experiments/spider_coordinates.py
"""

import os
import random
import sys
import time

import numpy as np

SEED = 20260926
HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(HERE, "spider_coordinates_output.txt")
_out_lines = []


def out(s=""):
    print(s)
    _out_lines.append(s)


CHECKS = [0]
FAILS = [0]
FAIL_EXAMPLES = []


def check(ok, what):
    CHECKS[0] += 1
    if not ok:
        FAILS[0] += 1
        if len(FAIL_EXAMPLES) < 30:
            FAIL_EXAMPLES.append(what)


# ----------------------------------------------------------------------------
# Arithmetic core (re-derived from spine.md 3.2-3.7 / 5.6, reverse.md 14.1.1,
# comb.md 18.1-18.2; written fresh here).
# ----------------------------------------------------------------------------

def v2(n):
    assert n != 0
    return (n & -n).bit_length() - 1


def v3(n):
    assert n != 0
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return k


def free23(n):
    """The 2,3-free part of a nonzero integer, sign kept."""
    assert n != 0
    sgn = -1 if n < 0 else 1
    m = abs(n)
    m //= (m & -m)
    while m % 3 == 0:
        m //= 3
    return sgn * m


def valid(w, d):
    return d >= 1 and w >= 1 and w % 2 == 1 and w % 3 != 0


def state_of_odd(y):
    """Door recovery (reverse.md 14.6.5.1): y + 1 = 2^m 3^a Omega -> ((Omega, m+a), a)."""
    assert y % 2 == 1 and y >= 1
    m = v2(y + 1)
    r = (y + 1) >> m
    a = v3(r)
    return (r // 3 ** a, m + a), a


def door(w, d, a):
    """The door y_a(w, d) = 2^(d-a) 3^a w - 1, 0 <= a < d."""
    return (1 << (d - a)) * 3 ** a * w - 1


def node_from_numerator(N):
    d = v3(N)
    return (N // 3 ** d, d)


def exit_data(w, d):
    A = 3 ** d * w - 1
    s = v2(A)
    return A, s, A >> s


def F(w, d):
    return state_of_odd(exit_data(w, d)[2])[0]


def comb_parent(w, d):
    """comb.md Definition 18.2.1."""
    if (w, d) == (1, 1):
        return None
    A, s, y = exit_data(w, d)
    if s >= 3:
        return node_from_numerator((1 << (s - 2)) * y + 1)
    return state_of_odd(y)[0]


def comb_children(W, D):
    """comb.md Proposition 18.2.3, labelled: ('cascade', None, node) and
    ('door', a, node) for each live door a; the root's self-child excluded."""
    A, s, y = exit_data(W, D)
    kids = [("cascade", None, node_from_numerator((1 << (s + 2)) * y + 1))]
    for a in range(D):
        ya = door(W, D, a)
        if ya % 3 == 0:
            continue
        s0 = 1 if ya % 3 == 1 else 2
        c = node_from_numerator((1 << s0) * ya + 1)
        if c == (W, D):
            continue
        kids.append(("door", a, c))
    return kids


def owner_by_ascent(w, d):
    """Theorem 19.2.2: ascend through comb parents while depth 1."""
    if d >= 2 or (w, d) == (1, 1):
        return (w, d)
    v = (w, d)
    while True:
        p = comb_parent(*v)
        if p[1] >= 2:
            return p
        v = p


# ----------------------------------------------------------------------------
# The objects of 19.5
# ----------------------------------------------------------------------------

CONT24 = (1, 17, 19)


def t_of(W, D):
    return v3((1 << (D + 1)) * W - 1)


def predicted_legs(W, D):
    """Item A.3: legs as (core, b, kind); kind 'low' (core = y_b(W, D+1)) or 'top'
    (core = y_0(W, D+1)/3, only when t = 1)."""
    t = t_of(W, D)
    legs = [(door(W, D + 1, b), b, "low") for b in range(1, D)]
    if t == 0:
        legs.append((door(W, D + 1, 0), 0, "low"))
    elif t == 1:
        legs.append((door(W, D + 1, 0) // 3, 0, "top"))
    return legs


def desc(x):
    """Item B: the hair descent map on a depth-1 core x with x mod 24 in {1,17,19}."""
    if x % 8 == 1:
        return (3 * x + 1) // 4
    if x % 8 == 3:
        return (x + 1) // 4
    raise ValueError("desc undefined")


def step_up(x):
    """The unique depth-1 child of the depth-1 node (x, 1), by formula:
    (next core, eps) or None at the end of a hair."""
    if x % 3 == 2:
        return 4 * x - 1, 0
    q = 4 * x - 1
    if v3(q) == 1:
        return q // 3, 1
    return None


def c_of_word(word):
    """c_w by the recursion c_{w eps} = 4 c_w + 3^{f(w)}, c_empty = 0."""
    c, f = 0, 0
    for e in word:
        c = 4 * c + 3 ** f
        f += e
    return c


def c_by_sum(word):
    k = len(word)
    total, f = 0, 0
    for i in range(1, k + 1):
        total += 4 ** (k - i) * 3 ** f
        f += word[i - 1]
    return total


def lens_value(x, word, kind):
    """3^f x + c_w + 4^k (lower), or 3^(f+1) x + 3 c_w + 4^k (top)."""
    k, f, c = len(word), sum(word), c_of_word(word)
    if kind == "low":
        return 3 ** f * x + c + 4 ** k
    return 3 ** (f + 1) * x + 3 * c + 4 ** k


def raw_Q(n):
    """The raw descent on a depth-1 odd integer n (n = 1 mod 4)."""
    if n % 8 == 1:
        return (3 * n + 1) // 4
    if n % 8 == 5:
        return (n - 1) // 4
    raise ValueError("raw_Q undefined")


def is_depth1_odd(n):
    return n % 4 == 1 and ((n + 1) // 2) % 3 != 0


def T_odd(n):
    m = 3 * n + 1
    return m >> v2(m)


# ----------------------------------------------------------------------------
# random helpers
# ----------------------------------------------------------------------------

def rand_core(rng, hi):
    while True:
        w = rng.randrange(5, hi, 2)
        if w % 3:
            return w


# ----------------------------------------------------------------------------
# Part 0 -- canaries
# ----------------------------------------------------------------------------

def part0():
    out("=" * 78)
    out("PART 0 -- canaries")
    out("=" * 78)
    # (1,2): t = 0, legs (11,1), (7,1)
    check(t_of(1, 2) == 0, "canary t(1,2)")
    legs = sorted(c for c, b, k in predicted_legs(1, 2))
    check(legs == [7, 11], "canary legs of (1,2)")
    kids = {c for _, _, c in comb_children(1, 2)}
    check({(7, 1), (11, 1)} <= kids, "canary (1,2) children contain the legs")
    check(door(1, 3, 1) == 11 and door(1, 3, 0) == 7, "canary doors of (1,3)")
    # (5,2): t = 1, legs (59,1), (13,1); door-1 child (13,2), top-door child (13,1)
    check(t_of(5, 2) == 1, "canary t(5,2)")
    legs = sorted((c, k) for c, b, k in predicted_legs(5, 2))
    check(legs == [(13, "top"), (59, "low")], "canary legs of (5,2)")
    kd = {(lab, a): c for lab, a, c in comb_children(5, 2)}
    check(kd[("door", 1)] == (13, 2) and kd[("door", 0)] == (13, 1), "canary shared core 13")
    check(kd[("cascade", None)] == (59, 1), "canary cascade leg 59")
    # the orphan link (17,1): 17 = 17 mod 24, desc(17) = 13, owner (5,2)
    check(17 % 24 == 17 and desc(17) == 13, "canary desc(17) = 13")
    check(comb_parent(17, 1) == (13, 1), "canary parent of (17,1)")
    check(owner_by_ascent(17, 1) == (5, 2), "canary owner of (17,1)")
    # the lens at 17: top leg 13, word (1,), k = 1, f = 1, c = 1: 9*17 + 3 + 4 = 160
    check(step_up(13) == (17, 1), "canary step 13 -> 17 is a fork step")
    L = lens_value(17, (1,), "top")
    check(L == 160 and L == 2 ** 5 * 5, "canary lens 160 = 2^5 * 5")
    check(free23(L) == 5 and v2(L) == 2 * 1 + 2 + 1, "canary lens reads Omega = 5, D = 2")
    check(state_of_odd(L - 1) == ((5, 5), 0), "canary state(159) = (5, 5), door 0")
    # b >= 3 fixed hair: (1,4), b = 3 leg 107 -> 427 -> 569 -> 2275 (end)
    x, hair, word = 107, [107], []
    while True:
        st = step_up(x)
        if st is None:
            break
        x, e = st
        hair.append(x)
        word.append(e)
    check(door(1, 5, 3) == 107 and hair == [107, 427, 569, 2275] and word == [0, 1, 0],
          "canary fixed hair of the b = 3 leg of (1,4)")
    out(f"  {CHECKS[0]} canary checks, {FAILS[0]} failures")
    out("  (1,2): t = 0, legs (11,1) = y_1(1,3), (7,1) = y_0(1,3)")
    out("  (5,2): t = 1, legs (59,1) = y_1(5,3), (13,1) = y_0(5,3)/3; children (13,2), (13,1)")
    out("  (17,1): desc(17) = 13, owner (5,2); lens at 17 = 9*17 + 3 + 4 = 160 = 2^5 * 5")
    out("  (1,4): b = 3 leg 107, hair 107 -> 427 -> 569 -> 2275, word 010, then end")


# ----------------------------------------------------------------------------
# Census to level 18 (built fresh)
# ----------------------------------------------------------------------------

def build_census(level_cap):
    level = {(1, 1): 0}
    parent = {(1, 1): None}
    children = {}
    frontier = [(1, 1)]
    counts = [1]
    for lev in range(1, level_cap + 1):
        nxt = []
        for v in frontier:
            ks = []
            for _, _, c in comb_children(*v):
                if c in level:
                    raise AssertionError("census: node reached twice")
                level[c] = lev
                parent[c] = v
                nxt.append(c)
                ks.append(c)
            children[v] = ks
        for v in nxt:
            children[v] = []
        frontier = nxt
        counts.append(len(nxt))
    return level, parent, children, counts


# ----------------------------------------------------------------------------
# Part A -- the legs are the doors of (Omega, D+1)
# ----------------------------------------------------------------------------

def check_item_A(W, D):
    """All claims of Item A at one abdomen (or claim 1 at D = 1)."""
    kids = comb_children(W, D)
    by = {}
    for lab, a, c in kids:
        by[(lab, a)] = c
    t = t_of(W, D)
    # claim 1: lower children numerators 3 * y_b(W, D+1), b = 0..D-1;
    # b = D-1 is the cascade child; b = 0..D-2 are the doors a = b+1
    ok = True
    for b in range(D):
        key = ("door", b + 1) if b <= D - 2 else ("cascade", None)
        c = by.get(key)
        if c is None:
            ok = False
            break
        num = 3 ** c[1] * c[0]
        if num != 3 * door(W, D + 1, b):
            ok = False
        if comb_parent(*c) != (W, D):
            ok = False
    check(ok, f"A.1 lower children at {(W, D)}")
    if D == 1:
        return
    # claim 2: top door alive iff t >= 1; branch 1; numerator y_0(W, D+1); shared core
    y0 = door(W, D, 0)
    alive = y0 % 3 != 0
    check(alive == (t >= 1), f"A.2 top alive iff t>=1 at {(W, D)}")
    if alive:
        check(y0 % 3 == 1, f"A.2 top door = 1 mod 3 at {(W, D)}")
        ct = by[("door", 0)]
        check(3 ** ct[1] * ct[0] == 2 * y0 + 1 == door(W, D + 1, 0), f"A.2 top numerator at {(W, D)}")
        c1 = by[("door", 1)]
        check(ct[0] == c1[0] and ct[1] == t and c1[1] == t + 1, f"A.2 shared core at {(W, D)}")
        check(comb_parent(*ct) == (W, D), f"A.2 top child's parent at {(W, D)}")
    else:
        check(("door", 0) not in by, f"A.2 dead top door has no child at {(W, D)}")
    # claim 3: legs
    actual = sorted(c[0] for _, _, c in kids if c[1] == 1)
    pred = predicted_legs(W, D)
    check(actual == sorted(p[0] for p in pred), f"A.3 leg set at {(W, D)}")
    check(len(actual) == D - 1 + (1 if t <= 1 else 0), f"A.3 leg count at {(W, D)}")
    # 19.1.6's count, as written there
    cnt1916 = (D - 1) + (1 if ((1 << (D + 1)) * W - 1) % 3 != 0 else 0) + \
        (1 if (alive and by[("door", 0)][1] == 1) else 0)
    check(cnt1916 == len(actual), f"A.3 agrees with 19.1.6 at {(W, D)}")
    for core, b, kind in pred:
        if kind == "low":
            check(core % 3 == (2 if b >= 1 else 1), f"A.3 class of lower leg b={b} at {(W, D)}")
            check(state_of_odd(core) == ((W, D + 1), b), f"A.3 state(x0) = (W, D+1) at {(W, D)}")
        else:
            check(3 * core + 1 == (1 << (D + 1)) * W, f"A.3 top leg identity at {(W, D)}")


def partA(rng, census_abdomens):
    out()
    out("=" * 78)
    out("PART A -- Item A: the legs are the doors of (Omega, D+1)  [19.5.1]")
    out("=" * 78)
    c0 = CHECKS[0]
    n = 0
    tdist = {}
    for _ in range(3000):
        D = rng.randint(2, 14)
        W = rand_core(rng, 10 ** 6)
        t = t_of(W, D)
        tdist[min(t, 2)] = tdist.get(min(t, 2), 0) + 1
        check_item_A(W, D)
        n += 1
    out(f"  random abdomens (Omega < 10^6, 2 <= D <= 14): {n}; t = 0 / 1 / >=2: "
        f"{tdist.get(0, 0)} / {tdist.get(1, 0)} / {tdist.get(2, 0)}")
    # D = 1 instance of claim 1
    for _ in range(2000):
        W = rand_core(rng, 10 ** 9)
        check_item_A(W, 1)
    out("  claim 1 at D = 1 (cascade child numerator 3(4 Omega - 1)): 2000 random depth-1 nodes")
    for (W, D) in census_abdomens:
        check_item_A(W, D)
    out(f"  every abdomen of the level-18 census: {len(census_abdomens)}")
    out(f"  Part A: {CHECKS[0] - c0} checks, failures so far {FAILS[0]}")


# ----------------------------------------------------------------------------
# Part B -- the hair descent map
# ----------------------------------------------------------------------------

def check_item_B(x):
    p = comb_parent(x, 1)
    cont = x % 24 in CONT24
    check((p[1] == 1) == cont, f"B continuation test at x={x}")
    if cont:
        check(p == (desc(x), 1), f"B desc = parent at x={x}")
    n = 2 * x - 1
    check(n % 4 == 1 and ((n + 1) // 2) % 3 != 0, f"B raw representative at x={x}")
    check((n % 48 in (1, 33, 37)) == cont, f"B raw continuation set at x={x}")
    if cont:
        if n % 16 == 1:
            n2 = (3 * n + 1) // 4
            check(v2(3 * n + 1) == 2, f"B two halvings at n={n}")
        elif n % 16 == 5:
            n2 = (n - 1) // 4
            check(T_odd(n) == T_odd(n2) and 4 * n2 + 1 == n, f"B sibling at n={n}")
        else:
            n2 = None
        check(n2 == 2 * desc(x) - 1, f"B raw form at x={x}")
    # raw Q (the n mod 8 form, 19.5.4) agrees with desc on continuation
    q = raw_Q(n)
    if cont:
        check(q == 2 * desc(x) - 1, f"B raw Q = raw desc at x={x}")
    check(is_depth1_odd(q) == cont, f"B raw Q stays depth 1 iff continuation at x={x}")


def owner_by_desc(x):
    j = 0
    while x % 24 in CONT24:
        if x == 1:
            return None, None
        x = desc(x)
        j += 1
    return comb_parent(x, 1), j


def partB(rng, census_d1):
    out()
    out("=" * 78)
    out("PART B -- Item B: the hair descent map desc and its raw form  [19.5.2]")
    out("=" * 78)
    c0 = CHECKS[0]
    check(desc(1) == 1, "B root fixed point desc(1) = 1")
    cells = {}
    for _ in range(15000):
        x = rand_core(rng, 10 ** 9)
        cells[x % 24] = cells.get(x % 24, 0) + 1
        check_item_B(x)
        o, j = owner_by_desc(x)
        check(o == owner_by_ascent(x, 1), f"B owner at x={x}")
    out(f"  random depth-1 nodes (x < 10^9): 15000, all 8 cells mod 24 hit: {sorted(cells) == [1, 5, 7, 11, 13, 17, 19, 23]}")
    pos_hist = {}
    for x in census_d1:
        check_item_B(x)
        o, j = owner_by_desc(x)
        check(o == owner_by_ascent(x, 1), f"B owner (census) at x={x}")
        pos_hist[j] = pos_hist.get(j, 0) + 1
    out(f"  every depth-1 node of the census: {len(census_d1)}")
    out(f"  hair position (desc steps to the leg) over the census: "
        f"{sorted(pos_hist.items())[:12]} ... max {max(pos_hist)}")
    out(f"  Part B: {CHECKS[0] - c0} checks, failures so far {FAILS[0]}")


# ----------------------------------------------------------------------------
# Part C / D -- member formula, lens identity, raw dictionary
# ----------------------------------------------------------------------------

STATS = {"members": 0, "hairs": 0, "maxlen": 0, "raw_moves": 0}


def walk_spider(W, D, census_members=None):
    """Walk every hair of the spider of (W, D) to its true end; check Items C and D at
    every member. Returns list of (x, b, kind, word) for every depth-1 member."""
    members = []
    t = t_of(W, D)
    run = [door(W, D, a) for a in range(D)]
    # Item D: the abdomen as the rising run
    for a in range(D - 1):
        check((3 * run[a] + 1) // 2 == run[a + 1] and v2(3 * run[a] + 1) == 1,
              f"D run step at {(W, D)} a={a}")
    A, s, y = exit_data(W, D)
    check(3 * run[D - 1] + 1 == 2 * A and v2(3 * run[D - 1] + 1) == s + 1,
          f"D run exit at {(W, D)}")
    # no one-halving predecessor of y_0
    check((2 * run[0] - 1) % 3 != 0, f"D run is maximal at {(W, D)}")
    for core, b, kind in predicted_legs(W, D):
        x0 = core
        # raw leg values
        n0 = 2 * x0 - 1
        if kind == "low":
            check(n0 == 4 * run[b] + 1 == 2 * door(W, D + 1, b) - 1, f"D raw lower leg {(W, D, b)}")
            check(T_odd(n0) == T_odd(run[b]), f"D lower leg is the sibling of y_b {(W, D, b)}")
        else:
            check(3 * n0 + 1 == 4 * run[0] and n0 == (4 * run[0] - 1) // 3, f"D raw top leg {(W, D)}")
        # the raw descent from the leg lands on y_b(W, D)
        q = raw_Q(n0)
        check(not is_depth1_odd(q) and q == run[b], f"D raw descent lands on y_b {(W, D, b)}")
        check(state_of_odd(q) == ((W, D), b), f"D terminal reads (W, D, b) {(W, D, b)}")
        # walk the hair up
        x, word, k = x0, [], 0
        hair_len = 0
        while True:
            hair_len += 1
            members.append((x, b, kind, tuple(word)))
            STATS["members"] += 1
            f = sum(word)
            c = c_of_word(word)
            check(c == c_by_sum(word), "C c_w recursion = sum")
            num = 4 ** k * x0 - c
            check(num % 3 ** f == 0 and num // 3 ** f == x, f"C member formula {(W, D, b, tuple(word))}")
            check(3 ** f * x + c == 4 ** k * x0, "C member identity")
            L = lens_value(x, word, kind)
            if kind == "low":
                check(L == 4 ** k * (x0 + 1) == (1 << (2 * k + D + 1 - b)) * 3 ** b * W,
                      f"C lens (lower) {(W, D, b, tuple(word))}")
                check(v3(L) == b and v2(L) == 2 * k + D + 1 - b and free23(L) == W,
                      "C lens valuations (lower)")
                check(state_of_odd(L - 1) == ((W, D + 1 + 2 * k), b), "C lens - 1 is door b of (W, D+1+2k)")
            else:
                check(L == 4 ** k * (3 * x0 + 1) == (1 << (2 * k + D + 1)) * W,
                      f"C lens (top) {(W, D, tuple(word))}")
                check(v3(L) == 0 and v2(L) == 2 * k + D + 1 and free23(L) == W, "C lens valuations (top)")
                check(state_of_odd(L - 1) == ((W, D + 1 + 2 * k), 0), "C lens - 1 is door 0 of (W, D+1+2k)")
            # descent returns to the leg in k steps, reversing the word
            z, jj = x, 0
            while z % 24 in CONT24 and z != x0:
                z = desc(z)
                jj += 1
            check(z == x0 and jj == k and x0 % 24 not in CONT24, "C desc returns to the leg in k steps")
            # raw member value is depth 1 and never 2 mod 3
            n = 2 * x - 1
            check(is_depth1_odd(n) and n % 3 != 2, "D raw member is depth 1, not 2 mod 3")
            # ground-truth depth-1 child vs formula step
            gt = [c2 for _, _, c2 in comb_children(x, 1) if c2[1] == 1]
            st = step_up(x)
            check(len(gt) <= 1, "C at most one depth-1 child")
            if st is None:
                check(gt == [] and x % 9 == 7, f"C hair end at x={x}")
                check(n % 9 == 4, "D raw hair end iff n = 4 mod 9")
                break
            x_next, e = st
            check(gt == [(x_next, 1)], f"C step formula = comb child at x={x}")
            n_next = 2 * x_next - 1
            if e == 0:
                check(n % 3 == 0 and n_next == 4 * n + 1 and T_odd(n_next) == T_odd(n), "D raw link move")
            else:
                check(n % 3 == 1 and n_next == (4 * n - 1) // 3 and 3 * n_next + 1 == 4 * n
                      and n % 9 != 4, "D raw fork move")
            check(raw_Q(n_next) == n, "D raw descent inverts the move")
            STATS["raw_moves"] += 1
            x = x_next
            word.append(e)
            k += 1
        STATS["hairs"] += 1
        STATS["maxlen"] = max(STATS["maxlen"], hair_len)
        if census_members is not None:
            tkey = "top" if kind == "top" else ("b>=3" if b >= 3 else f"b={b}")
            tab = census_members.setdefault(tkey, {})
            tab[hair_len] = tab.get(hair_len, 0) + 1
        # the forced hairs of the deep lower legs (19.5.3, corollary)
        if kind == "low" and b >= 3:
            check(tuple(word) == (0, 1, 0), f"C b>=3 hair is 010 at {(W, D, b)}")
            STATS["b3"] = STATS.get("b3", 0) + 1
        if kind == "low" and b == 2:
            u = (1 << (D - 1)) * W
            # word 0101 forced; the fifth node is a link iff 2^(D-1) W = 2 (mod 3)
            if u % 3 == 2:
                okb2 = tuple(word[:5]) == (0, 1, 0, 1, 0)
            else:
                okb2 = tuple(word[:4]) == (0, 1, 0, 1) and (len(word) == 4 or word[4] == 1)
            check(okb2, f"C b=2 hair prefix at {(W, D)}")
            STATS["b2"] = STATS.get("b2", 0) + 1
        if kind == "low" and b == 1:
            u = (1 << D) * W
            check(word[0] == 0 and ((len(word) == 1) == (u % 3 == 1)), f"C b=1 hair end at {(W, D)}")
            STATS["b1"] = STATS.get("b1", 0) + 1
    return members


def word_prefix_exponent(b, kind, f):
    """The derived sufficient 3-adic exponent on Omega for 'w is an admissible prefix'."""
    if kind == "top":
        return f + 2
    return max(0, f + 1 - b)


def hair_word_from(x0, maxlen):
    """Word of the hair from x0, truncated at maxlen steps; plus ended flag."""
    x, word = x0, []
    while len(word) < maxlen:
        st = step_up(x)
        if st is None:
            return tuple(word), True
        x, e = st
        word.append(e)
    return tuple(word), (step_up(x) is None)


def leg_of(W, D, b, kind):
    for core, bb, kk in predicted_legs(W, D):
        if bb == b and kk == kind:
            return core
    return None


def partC(rng, census_abdomens):
    out()
    out("=" * 78)
    out("PART C -- Item C: member formula and lens identity  [19.5.3]; PART D -- raw dictionary [19.5.4]")
    out("=" * 78)
    c0 = CHECKS[0]
    t0 = time.time()
    len_by_type = {}
    for (W, D) in census_abdomens:
        walk_spider(W, D, len_by_type)
    out(f"  every census abdomen, every leg (inside or past the level-18 boundary) walked to the true end of "
        f"its hair: {len(census_abdomens)} spiders, {STATS['hairs']} hairs, {STATS['members']} depth-1 members, "
        f"longest hair {STATS['maxlen']} nodes ({time.time() - t0:.1f}s)")
    out("  true hair length (nodes) by leg type over the census abdomens -- shares of lengths 1..6:")
    allc = {}
    for key in ("b=0", "b=1", "b=2", "b>=3", "top"):
        tab = len_by_type.get(key, {})
        n = sum(tab.values())
        for L_, c_ in tab.items():
            allc[L_] = allc.get(L_, 0) + c_
        out(f"    {key:5s} legs {n:6d}: " + ", ".join(f"{L_}: {tab.get(L_, 0) / n:.4f}" for L_ in range(1, 7)))
    n = sum(allc.values())
    out(f"    all   legs {n:6d}: " + ", ".join(f"{L_}: {allc.get(L_, 0) / n:.5f}" for L_ in range(1, 9)))
    # 19.2's two-state chain, started from a link and from a fork (exact rationals)
    from fractions import Fraction as Fr
    fF, fL = {1: Fr(1, 3)}, {1: Fr(0)}
    for L_ in range(2, 9):
        fF[L_] = Fr(1, 3) * fF[L_ - 1] + Fr(1, 3) * fL[L_ - 1]
        fL[L_] = fF[L_ - 1]
    out("    19.2 chain from a link: " + ", ".join(f"{L_}: {float(fL[L_]):.4f}" for L_ in range(1, 7)))
    out("    19.2 chain from a fork: " + ", ".join(f"{L_}: {float(fF[L_]):.4f}" for L_ in range(1, 7)))
    m0, h0 = STATS["members"], STATS["hairs"]
    for _ in range(2000):
        D = rng.randint(2, 14)
        W = rand_core(rng, 10 ** 6)
        walk_spider(W, D)
    out(f"  random spiders (Omega < 10^6, 2 <= D <= 14): 2000 spiders, {STATS['hairs'] - h0} hairs, "
        f"{STATS['members'] - m0} depth-1 members; longest hair overall {STATS['maxlen']} nodes")
    out(f"  raw moves checked (4n+1 / (4n-1)/3, inverted by the raw descent): {STATS['raw_moves']}")
    out(f"  forced hairs of the deep lower legs: b >= 3 hair = 010 exactly at {STATS.get('b3', 0)} legs; "
        f"b = 2 prefix 0101 (fifth node's class by 2^(D-1) Omega mod 3) at {STATS.get('b2', 0)} legs; "
        f"b = 1 hair ends at its second node iff 2^D Omega = 1 (mod 3) at {STATS.get('b1', 0)} legs")
    out(f"  Parts C-D walk: {CHECKS[0] - c0} checks, failures so far {FAILS[0]}")

    # --- admissible-word residue claim: sufficiency by random lifts --------------
    c1 = CHECKS[0]
    lifts = 0
    for _ in range(3000):
        D = rng.randint(2, 10)
        W = rand_core(rng, 10 ** 6)
        for core, b, kind in predicted_legs(W, D):
            word, ended = hair_word_from(core, 40)
            for k in range(len(word) + 1):
                w = word[:k]
                e = word_prefix_exponent(b, kind, sum(w))
                full = (k == len(word) and ended)
                if full:
                    e = e + 1          # the end condition reads one more digit
                for _ in range(2):
                    # lift W by a multiple of 3^e keeping it odd and prime to 3
                    u = rng.randrange(1, 10 ** 6)
                    W2 = W + 3 ** e * 2 * u
                    while W2 % 3 == 0:
                        W2 += 3 ** e * 2
                    check(valid(W2, D) and (W2 - W) % 3 ** e == 0, "C lift is a valid core in the class")
                    if kind == "top" and t_of(W2, D) != 1:
                        check(False, f"C lift lost the top leg {(W, D, e)}")
                        continue
                    x02 = leg_of(W2, D, b, kind)
                    if x02 is None:
                        check(False, f"C lift lost leg {(W, D, b, kind)}")
                        continue
                    w2, ended2 = hair_word_from(x02, k if not full else len(word) + 1)
                    if full:
                        check(w2 == word and ended2, f"C full hair shape preserved {(W, D, b, kind, word)}")
                    else:
                        check(w2[:k] == w and len(w2) >= k, f"C prefix preserved {(W, D, b, kind, w)}")
                    lifts += 1
    out(f"  admissible-word residue claim, sufficiency by random lifts: {lifts} lifts "
        f"({CHECKS[0] - c1} checks)")

    # --- exact least modulus by full-coset enumeration --------------------------
    E = 7
    exact_tab = {}
    smaller_examples = []
    forced_examples = []

    def fn_of_mod(universe, S, e):
        """Is membership in S a function of r mod 3^e on the universe?"""
        m = 3 ** e
        ins = {r % m for r in universe if r in S}
        outs = {r % m for r in universe if r not in S}
        return not (ins & outs)

    for D in range(2, 7):
        for (b, kind) in [(bb, "low") for bb in range(0, D)] + [(0, "top")]:
            words = {}
            universe = []
            for r in range(3 ** E):
                if r % 3 == 0:
                    continue
                W = r if r % 2 == 1 else r + 3 ** E
                t = t_of(W, D)
                if kind == "low" and b == 0 and t != 0:
                    continue
                if kind == "top" and t != 1:
                    continue
                universe.append(r)
                x0 = leg_of(W, D, b, kind)
                word, ended = hair_word_from(x0, 14)
                for k in range(1, len(word) + 1):
                    w = word[:k]
                    if word_prefix_exponent(b, kind, sum(w)) <= E - 1:
                        words.setdefault(w, set()).add(r)
            for w, S in words.items():
                pred = word_prefix_exponent(b, kind, sum(w))
                check(fn_of_mod(universe, S, pred), f"C prefix set is a function of Omega mod 3^pred {(D, b, kind, w)}")
                if len(S) == len(universe):
                    tag = "forced"
                    if len(forced_examples) < 40:
                        forced_examples.append((D, b, kind, ''.join(map(str, w)), pred))
                elif pred >= 1 and not fn_of_mod(universe, S, pred - 1):
                    tag = "exact"
                else:
                    tag = "smaller"
                    if len(smaller_examples) < 6:
                        smaller_examples.append((D, b, kind, ''.join(map(str, w)), pred))
                exact_tab[tag] = exact_tab.get(tag, 0) + 1
    out(f"  admissible-word least modulus, full-coset over Omega mod 3^{E} (D = 2..6, every leg type, every "
        f"word prefix with derived exponent <= {E - 1}): {dict(sorted(exact_tab.items()))}")
    out("    ('exact' = the derived exponent is the least; 'forced' = the prefix holds at every Omega of that "
        "leg type; 'smaller' = a smaller modulus already suffices)")
    if smaller_examples:
        out(f"    first 'smaller' cases (D, b, kind, word, derived exponent): {smaller_examples}")
    fb = {}
    for (D_, b_, k_, w_, p_) in forced_examples:
        fb.setdefault((b_, k_), set()).add((w_, p_))
    out("    forced cases by leg (b, kind): " + "; ".join(
        f"{key}: {sorted(v)}" for key, v in sorted(fb.items())))
    out(f"  Part C total: {CHECKS[0] - c0} checks, failures so far {FAILS[0]}")


# ----------------------------------------------------------------------------
# Part E -- the search for a walk-free identifier
# ----------------------------------------------------------------------------

def free23_arr(V):
    V = V.copy()
    zero = V == 0
    sign = np.sign(V)
    a = np.abs(V)
    a[zero] = 1
    a = a // (a & -a)
    idx = np.nonzero(a % 3 == 0)[0]
    while idx.size:
        a[idx] //= 3
        idx = idx[a[idx] % 3 == 0]
    res = sign * a
    res[zero] = 0
    return res


def canon(al, be):
    """(alpha, beta) with the common power of 2 and of 3 divided out: two pairs with
    the same canonical form give the same 2,3-free part at every x."""
    for p in (2, 3):
        while al % p == 0 and be % p == 0:
            al //= p
            be //= p
    return (al, be)


def group_const(vals, starts, sizes):
    mins = np.minimum.reduceat(vals, starts)
    maxs = np.maximum.reduceat(vals, starts)
    return mins == maxs


def partE(rng, level, parent, children, census_abdomens):
    out()
    out("=" * 78)
    out("PART E -- Item E: the search for a walk-free identifier  [19.5.5]")
    out("=" * 78)
    # ---------------- build window spiders ----------------
    owner = {}
    for v in sorted(level, key=lambda z: level[z]):
        if v == (1, 1):
            owner[v] = v
        elif v[1] >= 2:
            owner[v] = v
        else:
            p = parent[v]
            owner[v] = p if p[1] >= 2 else owner[p]
    spiders = {}
    for v, o in owner.items():
        if o == (1, 1):
            continue
        spiders.setdefault(o, []).append(v)
    # true-complete spiders: every hair's window length equals its true length
    complete = {}
    hairs = []          # list of node lists (window)
    link_pairs = []
    fork_pairs = []
    # abdomens at level 18 have none of their legs inside the window (size-1 window
    # pieces); they are left out of every spider table below
    in_window = [ab for ab in census_abdomens if level[ab] <= 17]
    for ab in in_window:
        ok_all = True
        for c in children[ab]:
            if c[1] != 1:
                continue
            h = [c]
            while True:
                d1 = [z for z in children[h[-1]] if z[1] == 1]
                if not d1:
                    break
                h.append(d1[0])
            if step_up(h[-1][0]) is not None:
                ok_all = False
            hairs.append(h)
            for i in range(len(h) - 1):
                if h[i][0] % 3 == 2:
                    link_pairs.append((h[i], h[i + 1]))
                else:
                    fork_pairs.append((h[i], h[i + 1]))
        complete[ab] = ok_all
    sp_list = in_window
    sizes_ok = all(len(spiders[ab]) >= 2 for ab in sp_list)
    check(sizes_ok, "E every window spider with abdomen at level <= 17 has size >= 2")
    check(all(len(spiders[ab]) == 1 for ab in census_abdomens if level[ab] == 18),
          "E abdomens at level 18 are alone in the window")
    n_complete = sum(1 for ab in sp_list if complete[ab])
    out(f"  window spiders with abdomen at level <= 17: {len(sp_list)} (every one of size >= 2: {sizes_ok}; "
        f"the {len(census_abdomens) - len(sp_list)} abdomens at level 18 are alone in the window and left out); "
        f"complete within the window (every hair ends inside it): {n_complete}")
    out(f"  window hairs: {len(hairs)} ({sum(1 for h in hairs if len(h) >= 2)} with >= 2 nodes); "
        f"link pairs: {len(link_pairs)}; fork pairs: {len(fork_pairs)}")

    # flatten groups: spider members, abdomen first
    sp_members = []
    sp_starts = []
    for ab in sp_list:
        sp_starts.append(len(sp_members))
        sp_members.append(ab)
        sp_members.extend(sorted(z for z in spiders[ab] if z != ab))
    sp_starts = np.array(sp_starts, dtype=np.int64)
    sp_sizes = np.diff(np.append(sp_starts, len(sp_members)))
    comp_mask = np.array([complete[ab] for ab in sp_list])
    hl = [h for h in hairs if len(h) >= 2]
    h_members = [z for h in hl for z in h]
    h_starts = np.cumsum([0] + [len(h) for h in hl[:-1]]).astype(np.int64)
    lp_members = [z for pr in link_pairs for z in pr]
    lp_starts = np.arange(0, len(lp_members), 2, dtype=np.int64)
    fp_members = [z for pr in fork_pairs for z in pr]
    fp_starts = np.arange(0, len(fp_members), 2, dtype=np.int64)

    # shuffled baseline: the same members, permuted, same group sizes
    perm_sp = list(sp_members)
    rng.shuffle(perm_sp)
    perm_h = list(h_members)
    rng.shuffle(perm_h)
    perm_lp = list(lp_members)
    rng.shuffle(perm_lp)

    def cores(lst):
        arr = np.array([z[0] for z in lst], dtype=np.int64)
        return arr

    C_sp, C_h, C_lp, C_fp = cores(sp_members), cores(h_members), cores(lp_members), cores(fp_members)
    P_sp, P_h, P_lp = cores(perm_sp), cores(perm_h), cores(perm_lp)
    maxcore = int(max(C_sp.max(), C_h.max()))
    check(27 * maxcore + 27 < 2 ** 62, "E int64 headroom")
    out(f"  largest core in the window: {maxcore} (27*max + 27 < 2^62: {27 * maxcore + 27 < 2 ** 62})")

    # ---------------- E.1 affine lenses ----------------
    alphas = [1, 2, 3, 4, 6, 8, 9, 12, 16, 27]
    betas = list(range(-27, 28))
    rows = []
    zero_hits = {}
    for al in alphas:
        for be in betas:
            if be == 0 and False:
                pass
            res = {}
            for name, C, st in (("sp", C_sp, sp_starts), ("h", C_h, h_starts),
                                ("lp", C_lp, lp_starts), ("fp", C_fp, fp_starts),
                                ("sp0", P_sp, sp_starts), ("h0", P_h, h_starts), ("lp0", P_lp, lp_starts)):
                V = al * C + be
                nz = int((V == 0).sum())
                if nz:
                    zero_hits[(al, be)] = zero_hits.get((al, be), 0) + nz
                g = free23_arr(V)
                const = group_const(g, st, None)
                res[name] = int(const.sum())
                if name == "sp":
                    res["sp_c"] = int((const & comp_mask).sum())
                    if const.any():
                        vals = g[st[const]]
                        res["sp_distinct"] = len(set(vals.tolist()))
                        res["sp_ex"] = [sp_list[i] for i in np.nonzero(const)[0][:3].tolist()]
                if name == "h" and const.any():
                    res["h_idx"] = np.nonzero(const)[0].tolist()
            rows.append((al, be, res))
    nsp, nh, nlp, nfp = len(sp_starts), len(h_starts), len(lp_starts), len(fp_starts)
    out()
    out("  E.1 affine lenses g(x) = 2,3-free part of (alpha x + beta) on the core, "
        f"alpha in {alphas}, beta in [-27, 27] ({len(rows)} pairs; none skipped: alpha x + beta = 0 occurs "
        f"only at core 1 with beta = -alpha, counted with the sentinel value 0 -- {len(zero_hits)} pairs, "
        f"{sum(zero_hits.values())} zero values)")
    out(f"  groups: spiders {nsp} (complete {int(comp_mask.sum())}), hairs(>=2 nodes) {nh}, link pairs {nlp}, "
        f"fork pairs {nfp}")
    out("  columns: spiders constant [of them complete] (distinct constant values) | shuffled baseline | "
        "hairs | baseline | link pairs | baseline | fork pairs")
    agg = {"sp": 0, "h": 0, "lp": 0, "fp": 0, "sp0": 0, "h0": 0, "lp0": 0}
    for al, be, r in rows:
        for kk in agg:
            agg[kk] = max(agg[kk], r[kk])
    shown = 0
    seen_canon = set()
    n_canon = len({canon(al, be) for al, be, _ in rows})
    out(f"  ({n_canon} distinct canonical pairs after dividing out common powers of 2 and 3; one row each, "
        "largest counts first)")
    for al, be, r in sorted(rows, key=lambda t: (-(t[2]["sp"] + t[2]["h"] + t[2]["lp"] + t[2]["fp"]), t[0], t[1])):
        if r["sp"] + r["h"] + r["lp"] + r["fp"] == 0:
            continue
        if canon(al, be) in seen_canon:
            continue
        seen_canon.add(canon(al, be))
        if shown >= 25:
            break
        shown += 1
        out(f"    ({al:2d},{be:4d}): sp {r['sp']:6d} [{r['sp_c']:5d}] ({r.get('sp_distinct', 0):5d}) | {r['sp0']:3d} | "
            f"h {r['h']:6d} | {r['h0']:3d} | lp {r['lp']:6d} | {r['lp0']:3d} | fp {r['fp']:6d}")
    nonzero_sp = [(al, be) for al, be, r in rows if r["sp"] > 0]
    out(f"  pairs constant on at least one spider: {len(nonzero_sp)}; max spiders constant for any pair: "
        f"{agg['sp']} of {nsp}; max shuffled-baseline spiders: {agg['sp0']}")
    ex_seen = set()
    for al, be, r in rows:
        for ab in r.get("sp_ex", []):
            if ab in ex_seen or len(ex_seen) >= 8:
                continue
            ex_seen.add(ab)
            mem = [ab] + sorted(z for z in spiders[ab] if z != ab)
            out(f"    example constant spider for ({al},{be}): members {mem[:6]}{' ...' if len(mem) > 6 else ''}, "
                f"level {level[ab]}, value {free23(al * ab[0] + be) if al * ab[0] + be else 0}")
    out(f"  max hairs constant: {agg['h']} of {nh}; max link pairs: {agg['lp']} of {nlp}; "
        f"max fork pairs: {agg['fp']} of {nfp}")
    out(f"  shuffled-baseline maxima over all pairs: spiders {agg['sp0']}, hairs {agg['h0']}, link pairs {agg['lp0']}")
    oth = {kk: max(r[kk] for al, be, r in rows if canon(al, be) not in (canon(1, -1), canon(3, -1)))
           for kk in ("sp", "h", "lp", "fp")}
    out(f"  maxima over the pairs not equivalent to (1,-1) or (3,-1): spiders {oth['sp']}, hairs {oth['h']}, "
        f"link pairs {oth['lp']}, fork pairs {oth['fp']}")
    # the two exact invariants, derived: free(3x-1) under link steps, free(x-1) under fork steps
    d = {(al, be): r for al, be, r in rows}
    check(d[(3, -1)]["lp"] == nlp, "E.1 free(3x-1) constant on every link pair (control)")
    check(d[(1, -1)]["fp"] == nfp, "E.1 free(x-1) constant on every fork pair (derived)")
    out(f"  control: g_(3,-1) = exit y on depth-1 nodes, constant on {d[(3, -1)]['lp']}/{nlp} link pairs; "
        f"derived: g_(1,-1) constant on {d[(1, -1)]['fp']}/{nfp} fork pairs")

    # per-hair constancy explained: all-link-step hairs and all-fork-step hairs
    def hair_kind(h):
        ks = set(0 if h[i][0] % 3 == 2 else 1 for i in range(len(h) - 1))
        return ks
    n_all_fork = sum(1 for h in hl if hair_kind(h) == {1})
    n_all_link = sum(1 for h in hl if hair_kind(h) == {0})
    out(f"  window hairs (>= 2 nodes) whose steps are all fork steps: {n_all_fork}; all link steps: {n_all_link}")
    out(f"    g_(1,-1) constant on {d[(1, -1)]['h']} hairs; g_(3,-1) constant on {d[(3, -1)]['h']} hairs")
    for (al, be), kind_ in (((1, -1), {1}), ((3, -1), {0})):
        extra = [hl[i] for i in d[(al, be)].get("h_idx", []) if hair_kind(hl[i]) != kind_]
        for h in extra[:4]:
            out(f"    g_({al},{be}) constant on a hair outside its step type: cores {[z[0] for z in h]}, "
                f"values {[free23(al * z[0] + be) for z in h]}")
    # every other pair: hairs it is constant on, and whether they are all small-core
    worst = sorted(((r["h"], al, be) for al, be, r in rows
                    if canon(al, be) not in (canon(1, -1), canon(3, -1))), reverse=True)[:3]
    out(f"    largest hair counts among pairs not equivalent to (1,-1) or (3,-1): {worst}")

    # ---------------- E.1 comb quantities ----------------
    def q_exit(v):
        return exit_data(*v)[2]

    def q_peak(v):
        return exit_data(*v)[0]

    def q_top(v):
        return door(v[0], v[1], 0)

    def q_F(v):
        f = F(*v)
        return 3 ** f[1] * f[0]

    def q_F2(v):
        f = F(*F(*v))
        return 3 ** f[1] * f[0]

    def peak_odd(v):
        A = exit_data(*v)[0]
        return A >> v2(A)

    out()
    out("  E.1 comb quantities (all members; hairs >= 2 nodes; link pairs; fork pairs; shuffled baseline on spiders):")
    quants = [("exit y", q_exit), ("peak A", q_peak), ("odd part of A", peak_odd), ("top door y0", q_top),
              ("F(v)", q_F), ("F^2(v)", q_F2)]
    for nm, fn in quants:
        def const_count(members, starts):
            vals = [fn(z) for z in members]
            cnt = 0
            bounds = list(starts) + [len(members)]
            for i in range(len(starts)):
                seg = vals[bounds[i]:bounds[i + 1]]
                if all(s == seg[0] for s in seg):
                    cnt += 1
            return cnt
        spc = const_count(sp_members, list(sp_starts))
        # complete spiders only
        vals = [fn(z) for z in sp_members]
        bounds = list(sp_starts) + [len(sp_members)]
        spcc = sum(1 for i in range(len(sp_starts)) if comp_mask[i] and
                   all(s == vals[bounds[i]] for s in vals[bounds[i]:bounds[i + 1]]))
        hc = const_count(h_members, list(h_starts))
        lc = const_count(lp_members, list(lp_starts))
        fc = const_count(fp_members, list(fp_starts))
        bc = const_count(perm_sp, list(sp_starts))
        out(f"    {nm:14s}: spiders {spc:6d} [complete {spcc:5d}] | hairs {hc:6d} | link pairs {lc:6d}/{nlp} | "
            f"fork pairs {fc:6d}/{nfp} | baseline {bc}")
        if nm == "exit y":
            check(lc == nlp, "E.1 exit y constant on every link pair (control)")
            exit_sp = spc
            exit_spc = spcc
        if nm in ("F(v)", "F^2(v)"):
            ex = [sp_list[i] for i in range(len(sp_starts)) if comp_mask[i] and
                  all(s == vals[bounds[i]] for s in vals[bounds[i]:bounds[i + 1]])]
            if ex:
                out(f"      complete spiders with {nm} constant: abdomens {ex[:6]}, "
                    f"common value = 3^d w of {[F(*F(*e)) if nm == 'F^2(v)' else F(*e) for e in ex[:6]]}")

    # derive the exit-constant spiders: abdomen + cascade leg + its fork child only
    expl = 0
    for i, ab in enumerate(sp_list):
        seg = sp_members[sp_starts[i]:(sp_starts[i + 1] if i + 1 < len(sp_starts) else len(sp_members))]
        ys = {q_exit(z) for z in seg}
        if len(ys) == 1:
            # every depth-1 member must be on the abdomen's own door: the cascade leg and its link-step child
            ok = all(z == ab or q_exit(z) == q_exit(ab) for z in seg)
            casc = node_from_numerator(4 * exit_data(*ab)[0] + 1)
            chain = {casc, (4 * casc[0] - 1, 1)}
            if ok and set(seg) - {ab} <= chain:
                expl += 1
    out(f"    exit-constant spiders explained as {{abdomen, cascade leg, its link-step child}} (a cascade chain "
        f"cut by the window): {expl} of {exit_sp}; complete ones: {exit_spc}")
    check(expl == exit_sp, "E.1 every exit-constant spider is a window-cut cascade chain")

    # ---------------- E.1 (ii): g(x) = Omega_owner, by position ----------------
    out()
    out("  E.1 (ii): which affine lenses return the owner's core Omega at a depth-1 member, by position")
    d1 = [(z, owner[z]) for z in level if z[1] == 1 and z != (1, 1)]
    posinfo = {}
    for z, ab in d1:
        W, D = ab
        # position (b, kind, word) by descent
        x, word = z[0], []
        while x % 24 in CONT24:
            px = desc(x)
            word.append(0 if px % 3 == 2 else 1)
            x = px
        word = tuple(reversed(word))
        leg = x
        if state_of_odd(leg)[0] == (W, D + 1):
            b, kind = state_of_odd(leg)[1], "low"
        else:
            check(3 * leg + 1 == (1 << (D + 1)) * W, "E top leg identity")
            b, kind = 0, "top"
        posinfo[z] = (b, kind, word)
    X = np.array([z[0] for z, _ in d1], dtype=np.int64)
    OM = np.array([ab[0] for _, ab in d1], dtype=np.int64)
    hits_tab = []
    for al in alphas:
        for be in betas:
            g = free23_arr(al * X + be)
            hit = g == OM
            nh_ = int(hit.sum())
            if nh_:
                classes = {}
                for i in np.nonzero(hit)[0].tolist():
                    b, kind, word = posinfo[d1[i][0]]
                    key = (kind, len(word), word, "b>=1" if (kind == "low" and b >= 1) else ("b=0" if kind == "low" else "top"))
                    classes[key] = classes.get(key, 0) + 1
                hits_tab.append((nh_, al, be, classes))
    hits_tab.sort(key=lambda t: -t[0])
    # predicted lens coefficients for k <= 2
    pos_count = {}
    for z, (b, kind, word) in posinfo.items():
        key = (kind, word, "b>=1" if (kind == "low" and b >= 1) else ("b=0" if kind == "low" else "top"))
        pos_count[key] = pos_count.get(key, 0) + 1
    seen_c2 = set()
    shown2 = 0
    for nh_, al, be, classes in hits_tab:
        if canon(al, be) in seen_c2:
            continue
        seen_c2.add(canon(al, be))
        shown2 += 1
        if shown2 > 16:
            break
        top = sorted(classes.items(), key=lambda t: -t[1])[:2]
        desc_ = "; ".join(f"{k[3]} w={''.join(map(str, k[2])) or 'empty'}: {v}/{pos_count[(k[0], k[2], k[3])]}"
                          for k, v in top)
        out(f"    ({al:2d},{be:4d}): {nh_:6d} members -- {desc_}")
    out(f"  pairs with any hit: {len(hits_tab)} ({len({canon(al, be) for _, al, be, _ in hits_tab})} canonical)")
    # hits outside the lens positions: count and largest core involved
    lens_canon = {("b>=1", ()): (1, 1), ("b=0", ()): (1, 1), ("top", ()): (3, 1), ("b>=1", (0,)): (1, 5),
                  ("b=0", (1,)): (3, 5), ("top", (0,)): (3, 7), ("top", (1,)): (9, 7), ("b>=1", (0, 1)): (1, 7),
                  ("b=0", (1, 0)): (3, 23), ("b=0", (1, 1)): (9, 23)}
    off = 0
    off_max = 0
    for nh_, al, be, classes in hits_tab:
        off_pair = 0
        for key, v in classes.items():
            cls_key = (key[3], key[2])
            if lens_canon.get(cls_key) != canon(al, be):
                off += v
                off_pair += v
        off_max = max(off_max, off_pair)
    out(f"  member hits at a position whose lens is not that pair (chance coincidences): {off}, at most "
        f"{off_max} for any one pair (against {sum(h[0] for h in hits_tab)} hits in all, over {len(d1)} "
        f"depth-1 members x {len(rows)} pairs)")
    # the lens predictions, checked exactly: lens(k <= 2) coefficient pairs give Omega at every member there
    lens_pred = {("b>=1", ()): (1, 1), ("b=0", ()): (1, 1), ("top", ()): (3, 1),
                 ("b>=1", (0,)): (1, 5), ("b=0", (1,)): (3, 5), ("top", (0,)): (3, 7), ("top", (1,)): (9, 7),
                 ("b>=1", (0, 1)): (3, 21), ("b=0", (1, 0)): (3, 23), ("b=0", (1, 1)): (9, 23)}
    for (cls, word), ab_ in lens_pred.items():
        if ab_ is None:
            continue
        al, be = ab_
        idx = [i for i, (z, _) in enumerate(d1)
               if posinfo[z][2] == word and
               ("b>=1" if (posinfo[z][1] == "low" and posinfo[z][0] >= 1) else
                ("b=0" if posinfo[z][1] == "low" else "top")) == cls]
        if not idx:
            continue
        ok = all(free23(al * d1[i][0][0] + be) == d1[i][1][0] for i in idx)
        check(ok, f"E.1(ii) lens coefficients {ab_} at {cls} w={word}")
        out(f"    lens at {cls:4s} w={''.join(map(str, word)) or 'empty':5s}: (alpha, beta) = {ab_} returns Omega "
            f"at {len(idx)}/{len(idx)} members")
    # whole-spider: one pair returning Omega at every depth-1 member of a spider
    order = sorted(range(len(d1)), key=lambda i: d1[i][1])
    Xo, OMo = X[order], OM[order]
    own_o = [d1[i][1] for i in order]
    ow_starts = np.array([i for i in range(len(own_o)) if i == 0 or own_o[i] != own_o[i - 1]], dtype=np.int64)
    ow_complete = np.array([complete.get(own_o[i], False) for i in ow_starts.tolist()])
    best_whole, best_whole_w, best_pair = 0, 0, None
    for al in alphas:
        for be in betas:
            hit = (free23_arr(al * Xo + be) == OMo).astype(np.int64)
            allhit = np.minimum.reduceat(hit, ow_starts) == 1
            best_whole_w = max(best_whole_w, int(allhit.sum()))
            nc = int((allhit & ow_complete).sum())
            if nc > best_whole:
                best_whole, best_pair = nc, (al, be)
    out(f"  (window spiders whose window depth-1 members are all legs -- hairs cut at the window edge -- "
        f"give up to {best_whole_w} for the pair (1,1); restricted to complete spiders:)")
    out(f"  complete spiders on which one pair returns Omega at every depth-1 member: max over pairs "
        f"{best_whole} of {n_complete}{'' if best_pair is None else ' (pair ' + str(best_pair) + ')'}")

    # ---------------- E.2 residue determinacy of the position ----------------
    out()
    out("  E.2 the hair position j (desc steps to the leg): exact least modulus by full-coset search")

    def pos_trunc(r, jmax):
        for i in range(jmax + 1):
            if r % 24 not in CONT24:
                return i
            r = desc(r)
        return jmax + 1

    census_pos = {}
    for z, ab in d1:
        x, j = z[0], 0
        while x % 24 in CONT24:
            x = desc(x)
            j += 1
        census_pos[z[0]] = j
    JMAX = 7
    for j in range(0, JMAX + 1):
        A_s = 2 * j + 3
        Ms = (1 << A_s) * 3
        res = [r for r in range(Ms) if r % 2 == 1 and r % 3 != 0]
        ind = {r: (pos_trunc(r, j) == j) for r in res}
        # consistency with the census (sufficiency)
        okc = all(ind[x % Ms] == (p == j) for x, p in census_pos.items())
        check(okc, f"E.2 sufficiency on the census at j={j}")
        # random large lifts
        for _ in range(300):
            r = rng.choice(res)
            x = r + Ms * rng.randrange(1, 10 ** 12)
            check((pos_trunc(x, j) == j) == ind[r], f"E.2 lift at j={j}")
        sufficient = []
        for b in (0, 1):
            for a in range(0, A_s + 1):
                M = (1 << a) * 3 ** b
                cls = {}
                ok = True
                for r in res:
                    kk = r % M
                    if cls.setdefault(kk, ind[r]) != ind[r]:
                        ok = False
                        break
                if ok:
                    sufficient.append((M, a, b))
        least = min(sufficient)
        minimal = sorted(set((a, b) for M, a, b in sufficient
                             if not any((a2 <= a and b2 <= b and (a2, b2) != (a, b)) for _, a2, b2 in sufficient)))
        # census-restricted least modulus (a lower bound; data-limited)
        cl = None
        for M in sorted((1 << a) * 3 ** b for a in range(0, A_s + 1) for b in range(0, 2)):
            cls = {}
            ok = True
            for x, p in census_pos.items():
                kk = x % M
                v = (p == j)
                if cls.setdefault(kk, v) != v:
                    ok = False
                    break
            if ok:
                cl = M
                break
        npos = sum(1 for p in census_pos.values() if p == j)
        out(f"    j = {j}: sufficient 2^{A_s}*3 = {Ms}; exact least modulus {least[0]} = 2^{least[1]}*3^{least[2]}; "
            f"minimal (a,b): {minimal}; census nodes at j: {npos}; census-consistent least modulus: {cl}")
        check(least[1] == A_s and least[2] == 1, f"E.2 exact modulus = 2^(2j+3)*3 at j={j}")

    # ---------------- E.2 owner's D and Omega mod 3 not determined ----------------
    out()
    out("  E.2 owner's D and Omega mod 3 at fixed position: two members congruent mod 2^a 3^c at the same "
        "position j with owners of different D and different Omega mod 3 (construction of 19.5.5, checked "
        "by ground truth)")
    built = 0
    for j in range(0, 7):
        # find an abdomen (W1, D1) whose b = 1 leg's hair reaches position j
        for a in range(3, 25, 3):
            for c3 in range(1, 7):
                D1 = a + 2 * j + 2
                W1, x0, word = None, None, None
                cand = 1
                while True:
                    cand += 2
                    if cand % 3 == 0:
                        continue
                    x0c = door(cand, D1 + 1, 1)
                    wd, _ = hair_word_from(x0c, j)
                    if len(wd) >= j:
                        W1, x0, word = cand, x0c, wd[:j]
                        break
                f = sum(word)
                D2 = D1 + 1
                mod3 = 3 ** (c3 + f + 3)
                # W2 = 2^(D1-D2) W1 mod 3^(c3+f+3), odd
                inv2 = pow(2, -1, mod3)
                W2 = (inv2 * W1) % mod3
                if W2 % 2 == 0:
                    W2 += mod3
                x02 = door(W2, D2 + 1, 1)
                wd2, _ = hair_word_from(x02, j)
                # members at position j
                def member(x0_, w_):
                    x_ = x0_
                    for e_ in w_:
                        x_ = (4 * x_ - 1) // (3 if e_ else 1)
                    return x_
                m1 = member(x0, word)
                if wd2[:j] != word:
                    check(False, f"E.2 construction word mismatch j={j}")
                    continue
                m2 = member(x02, word)
                o1, j1 = owner_by_desc(m1)
                o2, j2 = owner_by_desc(m2)
                M = (1 << a) * 3 ** c3
                ok = (m1 - m2) % M == 0 and j1 == j2 == j and o1 == (W1, D1) and o2 == (W2, D2) \
                    and o1[1] != o2[1] and o1[0] % 3 != o2[0] % 3 \
                    and o1 == owner_by_ascent(m1, 1) and o2 == owner_by_ascent(m2, 1)
                check(ok, f"E.2 construction at j={j}, a={a}, c={c3}")
                built += 1
    out(f"    constructions: {built} (j = 0..6, a = 3..24 step 3, c = 1..6), each verified by descent and "
        "by comb-parent ascent")


# ----------------------------------------------------------------------------

def main():
    t_start = time.time()
    rng = random.Random(SEED)
    out(f"spider_coordinates.py -- seed {SEED}, 2026-09-26")
    out("Fresh code; imports nothing from any other script in this repository; positive comb only.")
    out()
    part0()
    t0 = time.time()
    level, parent, children, counts = build_census(18)
    out()
    out(f"census to level 18 built fresh from (1,1): {len(level)} nodes, per level {counts} "
        f"({time.time() - t0:.1f}s)")
    check(len(level) == 247932, "census size 247,932")
    abdomens = sorted(v for v in level if v[1] >= 2)
    d1 = sorted(v[0] for v in level if v[1] == 1 and v != (1, 1))
    out(f"abdomens {len(abdomens)}, depth-1 nodes {len(d1)}")
    partA(rng, abdomens)
    partB(rng, d1)
    partC(rng, abdomens)
    partE(rng, level, parent, children, abdomens)
    out()
    out("=" * 78)
    out(f"TOTAL: {CHECKS[0]} checks, {FAILS[0]} failures; wall clock {time.time() - t_start:.1f}s")
    if FAIL_EXAMPLES:
        out("first failures:")
        for s in FAIL_EXAMPLES:
            out("  " + s)
    with open(OUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(_out_lines) + "\n")
    return 0 if FAILS[0] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
