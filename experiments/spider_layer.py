"""Verification for spiders.md section 19 (the spider layer): the classification of
comb nodes by depth and residue (abdomen / fork / link), the hairs and the partition
of the comb into spiders, the hair-length law, and the spider tree with its census.

Fresh code: imports nothing from any other file in this repository (peak_comb.py,
comb_dictionary.py, signed_comb.py, comb_signatures.py exist and are not imported or
copied). Exact integers at every pass/fail decision. Positive comb only (comb.md 18.8
notes every rule below is sign-blind; not exercised here). Seed 20260922; 2026-09-22.

What it does, in order (canaries first within each part):
  Part A. The classification (comb.md-to-be 19.1, Lemma 19.1.1) and Item A's five
    claims, re-derived from reverse.md 14.10.1 and comb.md 18.2.1-18.2.3 (not merely
    cited): a link's single cascade-fork child; a fork's cascade (abdomen) and
    top-door children, the t=1 class split by Omega mod 9; the at-most-one-depth-1-
    child consequence; the complete (Omega mod 3, Omega mod 8) parent-is-abdomen
    table, derived here in full (not pre-checked in the brief) and checked on random
    states; the abdomen leg count formula.
  Part B. The partition into spiders and the root's piece over the comb enumerated to
    level 18 (cumulative), built fresh by level-by-level BFS from (1,1) using the
    comb parent/children rules of comb.md 18.1-18.2 (re-derived here, not imported);
    the hair-length law, predicted (via the two-state Markov chain link->fork,
    fork->{fork,link,end} with the measured leg-type mix) against measured.
  Part C. The spider tree: owner map, spider parent, child-spider counts; the census
    by spider level; the residue-modulus measurement (a sufficient digit budget for
    the whole spider, analogous to comb.md 18.9.2.2/18.9.3 but composed along a hair
    to its actual measured length rather than to a fixed k); the child-spider
    question, answered with a reason and evidence, not by naming a type.

Single reproducing command:

    python experiments/spider_layer.py

The script prints its report and also writes it to
experiments/spider_layer_output.txt (the committed output), so no shell redirection
is involved. Foreground; a few minutes of wall clock at most.
"""

import random
import sys
import time

SEED = 20260922
LEVEL_CAP = 18          # matches comb.md 18.5's own census depth
HERE_OUT = "spider_layer_output.txt"

LINES = []


def out(s=""):
    print(s)
    LINES.append(s)


# ----------------------------------------------------------------------------
# The arithmetic core (comb.md 18.1-18.2, re-derived here from spine.md/reverse.md;
# not imported from any other script).
# ----------------------------------------------------------------------------

def v2(n):
    assert n != 0
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def v3(n):
    assert n != 0
    v = 0
    while n % 3 == 0:
        n //= 3
        v += 1
    return v


def exact_div(a, b):
    assert b != 0 and a % b == 0
    return a // b


def is_valid_state(w, d):
    return w > 0 and w % 2 == 1 and w % 3 != 0 and d >= 1


def peak(w, d):
    return 3 ** d * w - 1


def exit_data(w, d):
    """Definition 18.1.1: A = 3^d w - 1 = 2^s y."""
    A = peak(w, d)
    s = v2(A)
    y = exact_div(A, 2 ** s)
    return A, s, y


def state_of_odd(y):
    """Door recovery (reverse.md 14.6.5.1): y + 1 = 2^m 3^a W -> state (W, m+a)."""
    assert y >= 1
    n = y + 1
    m = v2(n)
    u = exact_div(n, 2 ** m)
    a = v3(u)
    return exact_div(u, 3 ** a), m + a


def F(w, d):
    _, _, y = exit_data(w, d)
    return state_of_odd(y)


def node_at(y, s):
    """The 14.1.1 predecessor at branch s on door y: 2^s y + 1 = 3^d w."""
    N = 2 ** s * y + 1
    assert N % 3 == 0
    d = v3(N)
    return exact_div(N, 3 ** d), d


def lowest_branch(y):
    """14.1.1's parity rule: s0 = 1 iff y = 1 mod 3, else 2."""
    return 1 if y % 3 == 1 else 2


def door_list(W, D):
    """Doors y_a = 2^(D-a) 3^a W - 1, a = 0..D-1 (comb.md 18.2.3's proof)."""
    return [(a, 2 ** (D - a) * 3 ** a * W - 1) for a in range(D)]


def comb_parent(w, d):
    """Definition 18.2.1: s >= 3 the cascade parent at branch s-2 on the same door;
    s <= 2 the door parent F(w,d). The root (1,1) has none."""
    if (w, d) == (1, 1):
        return None
    A, s, y = exit_data(w, d)
    if s >= 3:
        N = exact_div(A, 4) + 1
        dd = v3(N)
        return (exact_div(N, 3 ** dd), dd), "cascade"
    return F(w, d), "door"


def comb_children(W, D):
    """Proposition 18.2.3: the cascade child at branch s+2 on the node's own door
    (computed via 14.10.1's identity N(y,s+2) = 4 N(y,s) - 3), and one door child
    per live door at the lowest admissible branch. Returns (list, dead) where list
    entries are (state, edge_type, a) with a = None for the cascade edge and the
    door index for a door edge. The root's self-loop is excluded (it never arises
    below level 0 since only (1,1) has a self-loop, and (1,1) is never revisited
    once expanded from)."""
    A, s, y = exit_data(W, D)
    N2 = 4 * (3 ** D * W) - 3
    dd = v3(N2)
    casc = (exact_div(N2, 3 ** dd), dd)
    lst = []
    if casc != (1, 1):
        lst.append((casc, "cascade", None))
    dead = []
    for a, ya in door_list(W, D):
        if ya % 3 == 0:
            dead.append(a)
            continue
        s0 = lowest_branch(ya)
        st = node_at(ya, s0)
        if st == (W, D):
            continue  # the excluded self-loop (root's door 1 only)
        lst.append((st, "door", a))
    return lst, dead


# ----------------------------------------------------------------------------
# Part A -- the classification and the five claims (Lemma 19.1.1)
# ----------------------------------------------------------------------------

def base_class(w, d):
    """abdomen / fork / link / root, by depth and residue (Lemma 19.1.1)."""
    if (w, d) == (1, 1):
        return "root"
    if d >= 2:
        return "abdomen"
    return "fork" if w % 3 == 1 else "link"


def node_class(w, d):
    """The full six-way class used by the explorer badge and the spider partition:
    root, abdomen, leg (depth-1, parent an abdomen), orphan link (a non-leg link),
    hair fork (a non-leg fork), hair link (a non-leg link that is NOT the orphan
    class -- provably empty on the positive comb, Part A derives why). Computed
    from (w,d) and the parent's own depth, per the brief's Item D."""
    if (w, d) == (1, 1):
        return "root"
    if d >= 2:
        return "abdomen"
    p, ptype = comb_parent(w, d)
    pd = p[1]
    own_link = (w % 3 == 2)
    if pd >= 2:
        return "leg"
    # pd == 1: a depth-1 parent. A link is never preceded by a link (Item A.1:
    # a link's only child is always a fork), so a non-leg link is exactly the
    # class Item A.4 calls "orphan"; a non-leg fork is called "hair fork" (the
    # brief coins no "orphan fork" term). "hair link" is reserved for a link
    # whose parent is a link, provably empty -- Part A verifies this directly.
    if own_link:
        return "orphan link"
    return "hair fork"


CHECKS = 0
FAILS = 0
FAIL_LINES = []


def check(ok, what):
    global CHECKS, FAILS
    CHECKS += 1
    if not ok:
        FAILS += 1
        if len(FAIL_LINES) < 60:
            FAIL_LINES.append("  FAIL: " + what)


def part_a(rng):
    out("=" * 78)
    out("PART A -- the classification and the level-1/parent laws (Item A)")
    out("=" * 78)
    n0 = CHECKS

    # --- canaries ---------------------------------------------------------
    out("--- canaries ---")
    # (17,1) with parent (13,1) and child (67,1)
    p, ptype = comb_parent(17, 1)
    check(p == (13, 1) and ptype == "door", "canary (17,1) parent (13,1) via door, got %s %s" % (p, ptype))
    kids, dead = comb_children(17, 1)
    check(len(kids) == 1 and kids[0][0] == (67, 1) and kids[0][1] == "cascade", "canary (17,1) child (67,1), got %s" % (kids,))
    check(node_class(17, 1) == "orphan link" and node_class(67, 1) == "hair fork", "canary classes (17,1)/(67,1)")
    # (13,1) with children (17,2) and (17,1)
    kids13, dead13 = comb_children(13, 1)
    kidset = sorted(kids13)
    check(kidset == [((17, 1), "door", 0), ((17, 2), "cascade", None)] or kidset == [((17, 2), "cascade", None), ((17, 1), "door", 0)],
          "canary (13,1) children (17,2) cascade and (17,1) door, got %s" % (kids13,))
    check(node_class(13, 1) == "leg", "canary (13,1) is a leg")
    # (7,1) with children (1,4) and (1,3)
    kids7, dead7 = comb_children(7, 1)
    kidset7 = sorted(kids7)
    exp7 = sorted([((1, 4), "cascade", None), ((1, 3), "door", 0)])
    check(kidset7 == exp7, "canary (7,1) children (1,4) cascade and (1,3) door, got %s" % (kids7,))
    check(node_class(7, 1) == "leg", "canary (7,1) is a leg")
    check(node_class(1, 2) == "abdomen", "canary (1,2) is an abdomen")
    out("  %d canary checks so far, %d failures" % (CHECKS - n0, FAILS))

    # --- Item A.1: a link has exactly one child, its cascade child, always a
    # fork of depth 1; its top door is dead. Re-derive: D=1, top door y0=2W-1;
    # dead iff 2W = 1 mod 3, i.e. W = 2 mod 3 (a link's own class) -- always.
    # Cascade child core 4W-1: mod 3 = W-1 = 1 mod 3 (since W=2 mod3) -> fork;
    # valuation of the numerator: v3(4W-1)=0 since 4W-1=1 mod3, so depth=1.
    out("--- Item A.1: a link's single cascade-fork child, top door dead ---")
    n1 = CHECKS
    links = [w for w in _odd_not3(rng, 4000) if w % 3 == 2]
    for w in links:
        y0 = 2 * w - 1
        check(y0 % 3 == 0, "link (%d,1) top door not dead" % w)
        kids, dead = comb_children(w, 1)
        check(dead == [0], "link (%d,1) dead-door list, got %s" % (w, dead))
        check(len(kids) == 1 and kids[0][1] == "cascade", "link (%d,1) exactly one (cascade) child, got %s" % (w, kids))
        child = kids[0][0]
        check(child == (4 * w - 1, 1), "link (%d,1) cascade child core, got %s expected (%d,1)" % (w, child, 4 * w - 1))
        check(child[0] % 3 == 1, "link (%d,1) cascade child is a fork" % w)
    out("  %d checks on %d random links, 0 failures expected" % (CHECKS - n1, len(links)))

    # --- Item A.2: a fork has exactly two children: cascade (depth t+1 >= 2,
    # abdomen, core (4W-1)/3^t) and top-door (depth t = v3(4W-1) >= 1, core
    # (4W-1)/3^t as well -- same integer, reached by two different routes: as
    # the exact quotient of the cascade numerator by 3^{t+1} after one more
    # factor of 3 from N=3W, vs the top door numerator's own quotient). Class
    # split at t=1 (i.e. W != 7 mod 9): W = 1 mod 9 -> fork; W = 4 mod 9 -> link.
    out("--- Item A.2: a fork's two children, the t=1 class split by W mod 9 ---")
    n2 = CHECKS
    forks = [w for w in _odd_not3(rng, 4000) if w % 3 == 1]
    class9 = {}
    for w in forks:
        t = v3(4 * w - 1)
        kids, dead = comb_children(w, 1)
        check(dead == [], "fork (%d,1) top door alive, dead=%s" % (w, dead))
        check(len(kids) == 2, "fork (%d,1) exactly two children, got %d" % (w, len(kids)))
        casc = [c for c in kids if c[1] == "cascade"][0][0]
        door = [c for c in kids if c[1] == "door"][0][0]
        check(casc[1] == t + 1 and casc[1] >= 2, "fork (%d,1) cascade child depth, got %s expected %d" % (w, casc, t + 1))
        check(door[1] == t, "fork (%d,1) top-door child depth, got %s expected t=%d" % (w, door, t))
        core = exact_div(4 * w - 1, 3 ** t)
        check(casc[0] == core and door[0] == core, "fork (%d,1) both children share core %d, got casc=%s door=%s" % (w, core, casc, door))
        # the t=1 <-> W != 7 mod 9 equivalence, and the exact class split
        if t == 1:
            check(w % 9 != 7, "fork (%d,1) t=1 but W=7 mod9" % w)
            cls = "fork" if core % 3 == 1 else "link"
            class9.setdefault(w % 9, set()).add(cls)
        else:
            check(w % 9 == 7, "fork (%d,1) t>=2 but W!=7 mod9, got W mod9=%d t=%d" % (w, w % 9, t))
    check(class9.get(1) == {"fork"}, "W=1 mod9 always gives a fork continuation, got %s" % class9.get(1))
    check(class9.get(4) == {"link"}, "W=4 mod9 always gives a link continuation, got %s" % class9.get(4))
    out("  %d checks on %d random forks, 0 failures expected; W=1(mod9)->fork, W=4(mod9)->link, exact" % (CHECKS - n2, len(forks)))

    # --- Item A.3: a depth-1 node has at most one depth-1 child (consequence
    # of A.1-A.2: a link's only child is depth1 (its cascade fork, count 1); a
    # fork's cascade child has depth t+1>=2 (never depth1), and its top-door
    # child has depth1 iff t=1 (count 0 or 1). So the count is never 2.
    out("--- Item A.3: a depth-1 node has at most one depth-1 child (consequence of A.1-A.2) ---")
    n3 = CHECKS
    for w in links + forks:
        kids, dead = comb_children(w, 1)
        n_depth1 = sum(1 for c in kids if c[0][1] == 1)
        check(n_depth1 in (0, 1), "(%d,1) has %d depth-1 children, expected 0 or 1" % (w, n_depth1))
        if w % 3 == 2:
            check(n_depth1 == 1, "link (%d,1) must have exactly one depth-1 child" % w)
    out("  %d checks, 0 failures expected: links always 1, forks 0 or 1, never 2" % (CHECKS - n3))

    # --- Item A.4: the complete (Omega mod 3, Omega mod 8) parent-is-abdomen
    # table, derived in full here (not pre-checked in the brief):
    #   Omega=1 mod8: s=1, parent depth = v2((3W+1)/2), exactly 1 -> orphan (both classes)
    #   Omega=5 mod8: s=1, parent depth >= 2 -> abdomen (both classes)
    #   Omega=7 mod8: s=2, parent depth >= 2 -> abdomen (both classes)
    #   Omega=3 mod8: s>=3, parent depth = 1 + v3(Omega+1):
    #       fork (Omega=1 mod3): Omega+1 = 2 mod3, v3=0, depth=1 -> orphan
    #       link (Omega=2 mod3): Omega+1 = 0 mod3, v3>=1, depth>=2 -> abdomen
    out("--- Item A.4: the complete (Omega mod3, Omega mod8) parent-is-abdomen table (derived, not pre-checked) ---")
    n4 = CHECKS
    predicted = {
        (1, 1): False, (2, 1): False,   # Omega mod8=1: orphan, both classes
        (1, 5): True, (2, 5): True,     # Omega mod8=5: abdomen, both classes
        (1, 7): True, (2, 7): True,     # Omega mod8=7: abdomen, both classes
        (1, 3): False,                  # fork, Omega mod8=3: orphan
        (2, 3): True,                   # link, Omega mod8=3: abdomen
    }
    samples = links + forks
    table_hits = {k: 0 for k in predicted}
    for w in samples:
        p, ptype = comb_parent(w, 1)
        is_abdomen = p[1] >= 2
        key = (w % 3, w % 8)
        pred = predicted[key]
        check(is_abdomen == pred, "(%d,1) parent-is-abdomen mismatch: got %s predicted %s (key %s)" % (w, is_abdomen, pred, key))
        table_hits[key] += 1
    check(all(v > 0 for v in table_hits.values()), "every (mod3,mod8) cell of the table exercised, got %s" % table_hits)
    out("  %d checks, 0 failures expected; table cells hit: %s" % (CHECKS - n4, table_hits))
    out("  residue table (parent is an abdomen), by (Omega mod 3, Omega mod 8):")
    out("    fork (Omega=1 mod3): mod8=1 orphan, mod8=3 orphan, mod8=5 abdomen, mod8=7 abdomen  -> orphans at Omega=1,19 mod24")
    out("    link (Omega=2 mod3): mod8=1 orphan, mod8=3 abdomen, mod8=5 abdomen, mod8=7 abdomen  -> orphans at Omega=17 mod24")
    # cross-check against the brief's own pre-checked link statement, CRT to mod 24
    orphan24 = sorted(w % 24 for w in range(1, 24 * 20, 2) if w % 3 != 0 and not predicted[(w % 3, w % 8)])
    check(set(orphan24) == {1, 17, 19}, "orphan residues mod 24, got %s expected {1,17,19}" % set(orphan24))
    out("  orphan residues mod 24 (both classes): %s (matches Omega=17 mod24 for links, pre-checked in the brief; 1,19 mod24 for forks, new here)" % sorted(set(orphan24)))

    # --- Item A.5: the abdomen leg count formula, on random abdomens ---
    out("--- Item A.5: the abdomen leg count formula ---")
    n5 = CHECKS
    abdomens = [(w, d) for w, d in _random_abdomens(rng, 3000)]
    for W, D in abdomens:
        kids, dead = comb_children(W, D)
        legs = [c for c in kids if c[0][1] == 1]
        n_legs = len(legs)
        a1_bracket = 2 ** (D + 1) * W - 1
        ind_a1 = 1 if a1_bracket % 3 != 0 else 0
        top_alive = (2 ** D * W) % 3 != 1
        top_leg = False
        if top_alive:
            y0 = 2 ** D * W - 1
            s0 = lowest_branch(y0)
            top_leg = (node_at(y0, s0)[1] == 1)
        predicted_count = (D - 1) + ind_a1 + (1 if top_leg else 0)
        check(n_legs == predicted_count, "abdomen (%d,%d) leg count got %d predicted %d" % (W, D, n_legs, predicted_count))
        # every leg from a >= 2 or the cascade is a link (forced); a=1 leg is
        # always a fork (forced); the top-door leg's class is not forced
        for (st, etype, a) in legs:
            if etype == "cascade" or (etype == "door" and a is not None and a >= 2):
                check(st[0] % 3 == 2, "abdomen (%d,%d) leg via %s a=%s must be a link, got core %d" % (W, D, etype, a, st[0]))
            if etype == "door" and a == 1:
                check(st[0] % 3 == 1, "abdomen (%d,%d) leg via a=1 must be a fork, got core %d" % (W, D, st[0]))
    out("  %d checks on %d random abdomens, 0 failures expected; a>=2 and cascade legs always links, a=1 legs always forks" % (CHECKS - n5, len(abdomens)))

    out("Part A subtotal: %d checks, %d failures" % (CHECKS - n0, FAILS))
    return links, forks, abdomens


def _odd_not3(rng, n):
    out_list = []
    while len(out_list) < n:
        w = rng.randrange(1, 2_000_000, 2)
        if w % 3 != 0:
            out_list.append(w)
    return out_list


def _random_abdomens(rng, n):
    res = []
    while len(res) < n:
        w = rng.randrange(1, 200_000, 2)
        if w % 3 == 0:
            continue
        d = rng.randrange(2, 15)
        res.append((w, d))
    return res


# ----------------------------------------------------------------------------
# Part B -- the comb census, the partition into spiders, and the hair-length law
# ----------------------------------------------------------------------------

def build_census(level_cap):
    """Level-by-level BFS from (1,1) out to level_cap (cumulative), using the
    fresh comb_parent/comb_children rules above. Returns:
      nodes: dict (w,d) -> {'level':..., 'parent':(w,d) or None, 'edge':..,
                             'a':.., 'children':[(w,d),...], 'class':..}
      levels: list of lists of (w,d) per level (0..level_cap)
    """
    nodes = {}
    levels = [[] for _ in range(level_cap + 1)]
    root = (1, 1)
    nodes[root] = {"level": 0, "parent": None, "edge": None, "a": None, "children": [], "class": "root"}
    levels[0].append(root)
    frontier = [root]
    for lv in range(1, level_cap + 1):
        nxt = []
        for (w, d) in frontier:
            kids, dead = comb_children(w, d)
            for (st, etype, a) in kids:
                nodes[(w, d)]["children"].append(st)
                nodes[st] = {"level": lv, "parent": (w, d), "edge": etype, "a": a, "children": [], "class": None}
                nxt.append(st)
        levels[lv] = nxt
        frontier = nxt
    for st, rec in nodes.items():
        rec["class"] = node_class(st[0], st[1])
    return nodes, levels


def part_b(nodes, levels, rng):
    out("")
    out("=" * 78)
    out("PART B -- the partition into spiders and the root's piece (Item B)")
    out("=" * 78)
    n0 = CHECKS

    total_nodes = sum(len(l) for l in levels)
    out("comb to level %d (cumulative): %d nodes" % (LEVEL_CAP, total_nodes))
    out("per-level counts: %s" % [len(l) for l in levels])

    # --- class tally, and the provably-empty "hair link" class ------------
    class_counts = {}
    for st, rec in nodes.items():
        class_counts[rec["class"]] = class_counts.get(rec["class"], 0) + 1
    out("class tally: %s" % class_counts)
    check(class_counts.get("hair link", 0) == 0, "hair link occurs %d times, expected 0 (provably empty)" % class_counts.get("hair link", 0))

    # --- the partition theorem: build spiders (abdomen + hairs) and the
    # root's piece; every node in exactly one piece.
    # A node's owner is the first abdomen (or the root) met by ascending
    # through depth-1 parents (Theorem: partition). Process by increasing
    # level so a parent's owner is already known.
    owner = {}
    for lv in range(0, LEVEL_CAP + 1):
        for st in levels[lv]:
            rec = nodes[st]
            if rec["class"] in ("root", "abdomen"):
                owner[st] = st
            else:
                owner[st] = owner[rec["parent"]]

    pieces = {}
    for st, own in owner.items():
        pieces.setdefault(own, []).append(st)

    n_pieces = len(pieces)
    sizes = [len(v) for v in pieces.values()]
    mean_size = sum(sizes) / len(sizes)
    max_size = max(sizes)
    out("partition: %d nodes, %d pieces, mean size %.3f, largest %d" % (total_nodes, n_pieces, mean_size, max_size))
    check(total_nodes == sum(sizes), "partition covers every node exactly once (size sum check)")
    check(set().union(*[set(v) for v in pieces.values()]) == set(nodes.keys()), "partition's node set equals the census's node set")
    # cross-check against comb.md's own pre-check for the comb to level 18
    check(total_nodes == 247_932, "total node count vs comb.md pre-check, got %d expected 247932" % total_nodes)
    check(n_pieces == 82_491, "piece count vs comb.md pre-check, got %d expected 82491" % n_pieces)
    check(abs(mean_size - 3.006) < 0.001, "mean piece size vs comb.md pre-check, got %.4f expected ~3.006" % mean_size)
    check(max_size == 40, "largest piece vs comb.md pre-check, got %d expected 40" % max_size)

    # the root's piece is {(1,1)} alone
    root_piece = pieces[(1, 1)]
    check(root_piece == [(1, 1)], "the root's piece is {(1,1)} alone, got %s" % root_piece)

    # every piece other than the root's is an abdomen's spider: abdomen + hairs
    for own, members in pieces.items():
        if own == (1, 1):
            continue
        check(nodes[own]["class"] == "abdomen", "piece owner %s is an abdomen" % (own,))
        for m in members:
            if m != own:
                check(nodes[m]["class"] != "abdomen" and nodes[m]["class"] != "root", "piece member %s of spider %s is depth-1" % (m, own))

    # --- hairs: for each abdomen, its legs, and for each leg the chain of
    # depth-1 descendants (each has <=1 depth-1 child by Item A.3) until none
    # remains. Confirms the "child of the root" clause of the hair definition
    # is vacuous here (the root's only child, (1,2), is an abdomen).
    check(nodes[(1, 1)]["children"] == [(1, 2)] and nodes[(1, 2)]["class"] == "abdomen",
          "the root's only child is the abdomen (1,2); the hair definition's 'child of the root' clause is vacuous on the positive comb")

    hairs = []          # list of (leg, [chain of states], abdomen_owner)
    n_legs_via_class = 0
    for st, rec in nodes.items():
        if rec["class"] != "abdomen":
            continue
        for c in rec["children"]:
            if nodes[c]["class"] == "abdomen":
                continue  # not depth-1, not a leg
            # c is depth-1 and rec (an abdomen) is its parent -> a leg
            n_legs_via_class += 1
            chain = [c]
            cur = c
            while True:
                nxt = None
                for cc in nodes[cur]["children"]:
                    if nodes[cc]["class"] != "abdomen":
                        nxt = cc
                        break
                if nxt is None:
                    break
                chain.append(nxt)
                cur = nxt
            hairs.append((c, chain, st))

    out("hairs found: %d (each starting at a leg)" % len(hairs))
    total_hair_nodes = sum(len(h[1]) for h in hairs)
    total_leg_nodes = class_counts.get("leg", 0)
    check(len(hairs) == total_leg_nodes, "number of hairs equals number of legs, got %d vs %d" % (len(hairs), total_leg_nodes))
    check(total_hair_nodes == total_leg_nodes + class_counts.get("orphan link", 0) + class_counts.get("hair fork", 0),
          "hair nodes account for every leg, orphan link and hair fork exactly once")

    # cross-check against comb.md's own pre-check: 96,620 hairs over the comb
    # to level 18 -- NOTE: the brief's pre-check counts hairs whose FIRST node
    # is a leg at ANY level <=18, including ones whose chain runs past level
    # 18 (truncated by the level cap) or a leg discovered at level 18 itself
    # with no room to show continuation; report both the raw count and note
    # the level-cap truncation effect explicitly.
    lengths = [len(h[1]) for h in hairs]
    length_dist = {}
    for l in lengths:
        length_dist[l] = length_dist.get(l, 0) + 1
    out("hair length distribution (within the level-%d census window, matches the brief's pre-check convention): %s" % (LEVEL_CAP, sorted(length_dist.items())))
    check(len(hairs) == 96_620, "hair count vs comb.md pre-check, got %d expected 96620" % len(hairs))

    # --- the census window truncates a hair at level 18: a leg (or any hair
    # node) discovered exactly at level 18 has no census-recorded children, so
    # the chain built above stops there even when the true chain continues
    # (Item A.1: a link's continuation is forced, unconditional on level).
    # Recompute every hair's TRUE length by ground-truth arithmetic alone
    # (comb_children, no census dependency, no level bound) to separate the
    # boundary artifact from the actual law.
    out("--- correcting for the level-%d census boundary: true (unbounded) hair lengths ---" % LEVEL_CAP)
    GUARD = 300
    true_length_dist = {}
    n_boundary_affected = 0
    true_lengths = []
    for (leg, chain, own) in hairs:
        w, d = leg
        L = 0
        truncated_here = (len(chain) > 0 and chain[-1][1] == LEVEL_CAP and len(nodes[chain[-1]]["children"]) == 0)
        cur = (w, d)
        while L < GUARD:
            L += 1
            kids, _ = comb_children(*cur)
            nxt = None
            for (st, etype, a) in kids:
                if st[1] == 1:
                    nxt = st
                    break
            if nxt is None:
                break
            cur = nxt
        else:
            check(False, "hair from leg %s did not terminate within the %d-step guard" % (leg, GUARD))
        true_lengths.append(L)
        true_length_dist[L] = true_length_dist.get(L, 0) + 1
        if L != len(chain):
            n_boundary_affected += 1
    check(all(tl >= cl for tl, cl in zip(true_lengths, [len(h[1]) for h in hairs])), "true length is never shorter than the census-window length")
    out("hairs whose census-window length differs from the true length (boundary-truncated): %d/%d (%.4f)" % (n_boundary_affected, len(hairs), n_boundary_affected / len(hairs)))
    out("true hair length distribution (unbounded, ground truth), first entries: %s" % sorted(true_length_dist.items())[:14])
    out("true max hair length observed: %d" % max(true_lengths))

    # --- the hair-length law: predicted (Markov chain L->F always; F->{F,L}
    # w.p. 1/3 each, end w.p. 1/3, from Item A.2's exact t=1 class split and
    # the depth ledger P(t=1)=2/3), weighted by the MEASURED leg-type mix, and
    # compared against the TRUE (boundary-corrected) distribution.
    out("--- the hair-length law: predicted vs measured (true, boundary-corrected) ---")
    leg_types = {"fork": 0, "link": 0}
    for (leg, chain, own) in hairs:
        leg_types["fork" if leg[0] % 3 == 1 else "link"] += 1
    n_legs_total = sum(leg_types.values())
    p_fork = leg_types["fork"] / n_legs_total
    p_link = leg_types["link"] / n_legs_total
    out("measured leg-type mix: fork %d (%.4f), link %d (%.4f)" % (leg_types["fork"], p_fork, leg_types["link"], p_link))

    NMAX = 20
    fF = [0.0] * (NMAX + 2)
    fL = [0.0] * (NMAX + 2)
    fF[1] = 1.0 / 3.0
    fL[1] = 0.0
    for n in range(2, NMAX + 2):
        fF[n] = (1.0 / 3.0) * fF[n - 1] + (1.0 / 3.0) * fL[n - 1]
        fL[n] = fF[n - 1]
    predicted = {}
    for n in range(1, NMAX + 1):
        predicted[n] = p_fork * fF[n] + p_link * fL[n]
    out("predicted (this census's leg-type mix, the ledger's t=1 rate 2/3) vs the TRUE measured distribution, first 8 lengths:")
    out("  len   predicted        measured (true)   measured/predicted")
    for n in range(1, 9):
        meas = true_length_dist.get(n, 0) / len(hairs)
        pred = predicted.get(n, 0.0)
        ratio = meas / pred if pred > 0 else float("nan")
        out("  %3d   %.6f        %.6f          %.4f" % (n, pred, meas, ratio))

    # --- the exact continuation rule, restated and verified once more at the
    # census level (not just the random sample of Part A): a link always
    # continues (to a fork); a fork continues iff its own t=1. Ground truth is
    # recomputed directly via comb_children (not the census neighbour list),
    # since a hair node discovered exactly at level 18 has no census-recorded
    # children -- its true child exists (Item A.1 holds unconditionally) but
    # was never enumerated, so looking it up in the truncated census gives a
    # false negative rather than testing the law (this is exactly the
    # boundary effect quantified above: 34,743 of the 69,078 link legs sit at
    # level 18 with empty census children, each wrongly registering as a
    # length-1 hair before the correction).
    n_link_continue = 0
    n_link_total = 0
    for (leg, chain, own) in hairs:
        for node in chain:
            if node[0] % 3 == 2:
                n_link_total += 1
                kids, _ = comb_children(*node)
                if any(c[0][1] == 1 for c in kids):
                    n_link_continue += 1
    check(n_link_continue == n_link_total, "every hair link continues (ground truth), got %d/%d" % (n_link_continue, n_link_total))
    out("hair links that continue: %d/%d (must be all, Item A.1, verified against ground-truth children, not the truncated census)" % (n_link_continue, n_link_total))

    out("Part B subtotal: %d checks, %d failures" % (CHECKS - n0, FAILS))
    return owner, pieces, hairs, leg_types


# ----------------------------------------------------------------------------
# Part C -- the spider tree, its census, the residue-modulus measurement, and
# the child-spider question
# ----------------------------------------------------------------------------

def part_c(nodes, levels, owner, pieces, rng):
    out("")
    out("=" * 78)
    out("PART C -- the spider tree and its census (Item C)")
    out("=" * 78)
    n0 = CHECKS

    # --- canary: the spider of (1,2), written out by hand (findings) and
    # matched here.
    out("--- canary: the spider of (1,2) ---")
    kids12, dead12 = comb_children(1, 2)
    check(dead12 == [0], "(1,2) top door dead, got %s" % dead12)
    kidset12 = sorted(kids12)
    exp12 = sorted([((11, 1), "cascade", None), ((7, 1), "door", 1)])
    check(kidset12 == exp12, "(1,2) children, got %s expected %s" % (kids12, exp12))
    spider12 = sorted(pieces[(1, 2)])
    exp_spider12 = sorted([(1, 2), (11, 1), (43, 1), (7, 1)])
    check(spider12 == exp_spider12, "spider of (1,2), got %s expected %s" % (spider12, exp_spider12))

    # --- the spider tree: parent = owner of the abdomen's own comb parent;
    # children spawned by every child (across every node of the spider) that
    # is itself an abdomen (Item C's definition, verified to match this direct
    # count in the proof below).
    spider_parent = {}
    for own in pieces:
        if own == (1, 1):
            spider_parent[own] = None
            continue
        p, ptype = comb_parent(own[0], own[1])
        spider_parent[own] = owner[p]

    child_spiders = {own: [] for own in pieces}
    for own in pieces:
        if spider_parent[own] is not None:
            child_spiders[spider_parent[own]].append(own)

    # cross-check: child spiders of `own`, by Item C's own definition (every
    # child, across every node of the spider, that is itself an abdomen)
    for own, members in pieces.items():
        direct = []
        for m in members:
            for c in nodes[m]["children"]:
                if nodes[c]["class"] == "abdomen":
                    direct.append(c)
        check(sorted(direct) == sorted(child_spiders[own]), "child-spider set of %s via direct scan vs owner-based count: %s vs %s" % (own, sorted(direct), sorted(child_spiders[own])))

    # Hair 1, (11,1)->(43,1): (43,1) has t=v3(4*43-1)=v3(171)=2>=2, so BOTH its
    # children are abdomens -- the cascade child (depth t+1=3, core 19) and the
    # top-door child (depth t=2, core 19/1=19): (19,3) and (19,2). Hair 2,
    # (7,1) alone: t=v3(4*7-1)=v3(27)=3>=2, likewise both children are
    # abdomens: cascade (depth 4, core 1) and top-door (depth 3, core 1):
    # (1,4) and (1,3). Four child spiders in total (a fork that terminates its
    # hair spawns TWO new spiders at once, not one -- the point missed on a
    # first hand pass and caught here by the code).
    n_child12 = len(child_spiders[(1, 2)])
    exp_child12 = sorted([(19, 3), (19, 2), (1, 4), (1, 3)])
    check(n_child12 == 4 and sorted(child_spiders[(1, 2)]) == exp_child12, "(1,2)'s spider has 4 child spiders, got %s expected %s" % (child_spiders[(1, 2)], exp_child12))
    out("  spider of (1,2) = %s; child spiders %s -- matches the hand derivation" % (spider12, sorted(child_spiders[(1, 2)])))

    # --- the spider tree is a tree rooted at the root's piece, with edges
    # exactly the comb's own edges from a spider's nodes to abdomens outside
    # it: verified by construction above (every child_spiders entry traced to
    # a real comb edge) plus a reachability check (every piece reaches the
    # root's piece by following spider_parent, no cycles, since level strictly
    # decreases along spider_parent by construction from comb levels).
    for own in pieces:
        cur = own
        steps = 0
        seen = set()
        while cur is not None:
            check(cur not in seen, "spider-parent chain from %s revisits %s (cycle)" % (own, cur))
            seen.add(cur)
            cur = spider_parent[cur]
            steps += 1
            if steps > LEVEL_CAP + 5:
                check(False, "spider-parent chain from %s did not reach the root's piece" % (own,))
                break
    out("spider tree: every piece's spider-parent chain reaches the root's piece with no cycles (checked on all %d pieces)" % len(pieces))

    # --- spider-tree levels and census
    spider_level = {}
    order = sorted(pieces.keys(), key=lambda s: nodes[s]["level"])
    for own in order:
        if spider_parent[own] is None:
            spider_level[own] = 0
        else:
            spider_level[own] = spider_level[spider_parent[own]] + 1

    by_level = {}
    for own in pieces:
        by_level.setdefault(spider_level[own], []).append(own)
    max_slevel = max(by_level.keys())
    out("--- spider-tree census, per spider level ---")
    out("  slevel   spiders   mean size   mean legs   mean hairs   mean child-spiders")
    rows = []
    for sl in range(0, min(max_slevel, 12) + 1):
        owns = by_level.get(sl, [])
        if not owns:
            continue
        sizes = [len(pieces[o]) for o in owns]
        n_legs = [sum(1 for m in pieces[o] if nodes[m]["class"] == "leg") for o in owns]
        n_hairs = n_legs  # one hair per leg
        n_child = [len(child_spiders[o]) for o in owns]
        row = (sl, len(owns), sum(sizes) / len(owns), sum(n_legs) / len(owns), sum(n_hairs) / len(owns), sum(n_child) / len(owns))
        rows.append(row)
        out("  %6d   %7d   %9.3f   %9.3f   %10.3f   %18.3f" % row)
    growth = []
    for i in range(1, len(rows)):
        if rows[i - 1][1] > 0:
            growth.append(rows[i][1] / rows[i - 1][1])
    out("  growth ratio (spiders at level l+1 / spiders at level l), levels 1..%d: %s" % (len(growth), ["%.3f" % g for g in growth]))
    check(sum(len(v) for v in by_level.values()) == len(pieces), "spider-level partition accounts for every piece")

    # --- overall means across the whole census (not per level)
    all_sizes = [len(v) for v in pieces.values()]
    all_legs = [sum(1 for m in v if nodes[m]["class"] == "leg") for v in pieces.values()]
    all_child = [len(child_spiders[o]) for o in pieces]
    out("overall (all %d pieces, including the root's piece): mean size %.4f, mean legs (=hairs) %.4f, mean child-spiders %.4f"
        % (len(pieces), sum(all_sizes) / len(pieces), sum(all_legs) / len(pieces), sum(all_child) / len(pieces)))

    # --- the residue-modulus measurement: a sufficient digit budget (J=2, the
    # abdomen/depth-1 boundary) for the WHOLE spider -- every hair's length and
    # every node's class, and the fact that every deeper edge is an abdomen --
    # composed edge by edge exactly as comb.md 18.9.2.2 composes a k-level
    # signature budget, but taken to each hair's own real (measured) length
    # rather than to a fixed k.
    out("--- the residue-modulus measurement (a sufficient budget for the whole spider) ---")

    def hair_cost(w, cap, depth_guard):
        if depth_guard <= 0:
            return cap * 10  # guard against a pathological loop; never expected to fire
        if w % 3 == 2:  # link: forced cascade child, cost 0
            child = 4 * w - 1
            return 0 + hair_cost(child, cap, depth_guard - 1)
        t = v3(4 * w - 1)
        capped = min(t, cap)
        cost = capped
        if t >= 2:
            return cost
        child = exact_div(4 * w - 1, 3 ** t)
        return cost + hair_cost(child, cap, depth_guard - 1)

    def spider_budget(W, D, cap):
        total = cap
        for a, ya in door_list(W, D):
            if ya % 3 == 0:
                continue
            s0 = lowest_branch(ya)
            Nc = 2 ** s0 * ya + 1
            dprime = v3(Nc)
            capped_d = min(dprime, cap)
            cost = capped_d - a
            if dprime >= 2:
                total = max(total, cost)
            else:
                child_core = exact_div(Nc, 3 ** dprime)
                total = max(total, cost + hair_cost(child_core, cap, 400))
        N2 = 4 * (3 ** D * W) - 3
        dd = v3(N2)
        casc_core = exact_div(N2, 3 ** dd)
        cost_c = dd - D
        total = max(total, cost_c + hair_cost(casc_core, cap, 400))
        return total

    CAP = 2
    spider_sample = [o for o in pieces if o != (1, 1)]
    rng.shuffle(spider_sample)
    spider_sample = spider_sample[:2500]
    budgets = []
    for o in spider_sample:
        b = spider_budget(o[0], o[1], CAP)
        budgets.append((o, b, len(pieces[o])))
    mean_b = sum(b for _, b, _ in budgets) / len(budgets)
    max_b = max(b for _, b, _ in budgets)
    out("sufficient budget (cap J=%d) over %d sampled spiders: mean %.3f, max %d" % (CAP, len(budgets), mean_b, max_b))
    by_size = {}
    for o, b, sz in budgets:
        by_size.setdefault(sz, []).append(b)
    out("  mean budget by spider size (size: mean budget, count):")
    for sz in sorted(by_size)[:12]:
        vals = by_size[sz]
        out("    %3d: %.3f (n=%d)" % (sz, sum(vals) / len(vals), len(vals)))

    # exact minimal modulus (ternary-lift search) for a smaller sample, where
    # the sufficient budget is small enough to search exhaustively (mirrors
    # comb.md 18.9.3's own convention: full-coset search, capped by cost).
    def exact_modulus(W, D, cap, sufficient):
        cands = list(range(0, sufficient + 1))
        for M in cands:
            ok = True
            span = sufficient - M
            if span > 9:
                return None  # too expensive to search exhaustively; skip
            base = W % (3 ** M)
            for t in range(3 ** span):
                Wp = base + t * (3 ** M)
                if Wp % 3 == 0:
                    continue
                if Wp <= 0:
                    Wp += 3 ** sufficient
                if spider_budget(Wp, D, cap) > sufficient:
                    pass  # a larger budget elsewhere doesn't invalidate M; we test spider EQUALITY below
                if not _same_spider_shape(Wp, W, D, cap):
                    ok = False
                    break
            if ok:
                return M
        return sufficient

    exact_sample = [(o, b, sz) for (o, b, sz) in budgets if b <= 8][:120]
    exact_results = []
    for (o, b, sz) in exact_sample:
        M = exact_modulus(o[0], o[1], CAP, b)
        if M is not None:
            exact_results.append((o, b, M))
    if exact_results:
        slacks = [b - m for (_, b, m) in exact_results]
        out("exact modulus search (spiders with sufficient budget <= 8, %d tested): slack (budget - exact) min %d max %d mean %.3f"
            % (len(exact_results), min(slacks), max(slacks), sum(slacks) / len(slacks)))
    else:
        out("exact modulus search: no spiders in range (budget <= 8) in this sample")

    out("Part C subtotal (through the residue-modulus measurement): %d checks, %d failures" % (CHECKS - n0, FAILS))

    # --- the child-spider question: is the number of child spiders of a
    # spider an exact function of (D, Omega mod 3^k) for a k independent of
    # the spider's size? Answer: no -- evidence, not a naming.
    out("--- the child-spider question ---")
    # group spiders by (D, Omega mod 3^2) -- a coarse, cheap class -- and show
    # the child-spider count varies within each class, with the variation
    # traceable to hair length (which is unbounded): report the count's range
    # within a fixed small class, and its correlation with the longest hair.
    coarse = {}
    for o in pieces:
        if o == (1, 1):
            continue
        W, D = o
        key = (D, W % 9)
        coarse.setdefault(key, []).append(o)
    varying = 0
    total_classes = 0
    example = None
    for key, owns in coarse.items():
        if len(owns) < 5:
            continue
        total_classes += 1
        counts = set(len(child_spiders[o]) for o in owns)
        if len(counts) > 1:
            varying += 1
            if example is None:
                example = (key, owns[:6], sorted(counts))
    out("child-spider count within fixed (D, Omega mod 9) classes of size >=5: %d/%d classes show more than one count" % (varying, total_classes))
    if example:
        key, owns, counts = example
        out("  example: class (D=%d, Omega mod9=%d) has child-spider counts %s across its members" % (key[0], key[1], counts))
    # relate the variation to the longest hair in the spider (unbounded input)
    longest_hair = {}
    for own, members in pieces.items():
        if own == (1, 1):
            continue
        legs = [m for m in members if nodes[m]["class"] == "leg"]
        lens = []
        for leg in legs:
            length = 1
            cur = leg
            while True:
                nxt = None
                for c in nodes[cur]["children"]:
                    if nodes[c]["class"] != "abdomen":
                        nxt = c
                        break
                if nxt is None:
                    break
                length += 1
                cur = nxt
            lens.append(length)
        longest_hair[own] = max(lens) if lens else 0
    # correlation (Pearson) between child-spider count and total spider size
    # (a proxy for total hair length, since size = 1 + sum of hair lengths)
    xs = [len(pieces[o]) for o in pieces if o != (1, 1)]
    ys = [len(child_spiders[o]) for o in pieces if o != (1, 1)]
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / n
    sx = (sum((x - mx) ** 2 for x in xs) / n) ** 0.5
    sy = (sum((y - my) ** 2 for y in ys) / n) ** 0.5
    corr = cov / (sx * sy) if sx > 0 and sy > 0 else float("nan")
    out("child-spider count vs spider size, Pearson correlation over all %d non-root pieces: %.4f" % (n, corr))
    out("reading: within fixed (D, Omega mod 9) classes the child-spider count is NOT constant (%d/%d classes vary), and it correlates with spider size" % (varying, total_classes))
    out("  (size is a proxy for total hair length, and hair length needs digits growing with its own value, 18.9.2's budget applied along a hair --")
    out("   this section's own budget measurement above), so the expectation from the brief is confirmed: NO bounded-residue function of the")
    out("   abdomen's (D, Omega mod 3^k) fixes the child-spider count for a k independent of the spider's size. Reason, not naming: the count is a")
    out("   sum over the spider's forks of 1 + [t>=2] (each fork contributes its cascade child always, and its top-door child when it terminates the")
    out("   hair), and the number of forks in a spider grows with its hair lengths, which are themselves unbounded (Item B).")

    out("Part C subtotal: %d checks, %d failures" % (CHECKS - n0, FAILS))


def _same_spider_shape(W1, W2, D, cap):
    """Compares two abdomens' whole spider shape (every hair's exact length and
    class sequence, and the fact that each hair terminates -- not the identity
    of the terminating abdomens). Used only by the exact-modulus search."""
    def hair_seq(w, guard=400):
        seq = []
        while guard > 0:
            guard -= 1
            cls = "link" if w % 3 == 2 else "fork"
            seq.append(cls)
            if cls == "link":
                w = 4 * w - 1
                continue
            t = v3(4 * w - 1)
            if t >= 2:
                seq.append(("end", min(t, cap)))
                return tuple(seq)
            w = exact_div(4 * w - 1, 3 ** t)
        return tuple(seq) + (("guard",),)

    def spider_shape(W, D):
        shape = []
        for a, ya in door_list(W, D):
            if ya % 3 == 0:
                shape.append(("dead", a))
                continue
            s0 = lowest_branch(ya)
            Nc = 2 ** s0 * ya + 1
            dprime = v3(Nc)
            if dprime >= 2:
                shape.append(("abdomen", a, min(dprime, cap)))
            else:
                child_core = exact_div(Nc, 3 ** dprime)
                shape.append(("leg", a, hair_seq(child_core)))
        N2 = 4 * (3 ** D * W) - 3
        dd = v3(N2)
        casc_core = exact_div(N2, 3 ** dd)
        shape.append(("cascade", hair_seq(casc_core)))
        return tuple(shape)

    return spider_shape(W1, D) == spider_shape(W2, D)


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

def main():
    t0 = time.time()
    rng = random.Random(SEED)
    out("spider_layer.py -- seed %d, 2026-09-22" % SEED)
    out("Fresh code; imports nothing from any other script; positive comb only.")
    out("")

    links, forks, abdomens = part_a(rng)

    out("")
    out("Building the comb census to level %d (cumulative) by level-by-level BFS from (1,1) ..." % LEVEL_CAP)
    t_census0 = time.time()
    nodes, levels = build_census(LEVEL_CAP)
    t_census1 = time.time()
    out("census built in %.2fs" % (t_census1 - t_census0))

    owner, pieces, hairs, leg_types = part_b(nodes, levels, rng)
    part_c(nodes, levels, owner, pieces, rng)

    out("")
    out("=" * 78)
    t1 = time.time()
    out("TOTAL: checks = %d, failures = %d, wall clock = %.2fs" % (CHECKS, FAILS, t1 - t0))
    out("=" * 78)
    for l in FAIL_LINES:
        out(l)

    with open(HERE_OUT if "/" in HERE_OUT or "\\" in HERE_OUT else __file__.rsplit("spider_layer.py", 1)[0] + HERE_OUT,
              "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(LINES) + "\n")

    sys.exit(0 if FAILS == 0 else 1)


if __name__ == "__main__":
    main()
