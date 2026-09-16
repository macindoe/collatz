"""Independent verification for briefs/comb-dictionary-brief.md -- comb.md 18.7:
the comb path as the itinerary word (eta and lambda as word statistics), the
mean-degree identity, and the digit-transfer law across a door edge.

Objects (all from the wiki's own definitions, re-implemented here):
  state (w,d): w odd, 3 does not divide w, d >= 1 (spine.md section 3.5).
  peak  A(w,d) = 3^d w - 1 = 2^s y, s = v2(A), y the exit (comb.md 18.1.1).
  F(w,d) = state(y) via C = A + 2^s (spine.md 5.6; the dictionary of
  reverse.md 14.14.1.1), cross-checked against door recovery (14.6.5.1).
  doors of (W,D): y_a = 2^(D-a) 3^a W - 1, a = 0..D-1; live iff 3 does not
  divide y_a (14.1.1); the top door is a = 0 (14.8.4).
  node(y,s): the state at branch s on door y, 2^s y + 1 = 3^d w (14.1.1).
  comb parent (comb.md 18.2.1): s >= 3 -> node(y, s-2) (cascade edge);
  s <= 2 -> state(y) = F(w,d) (door edge). The root (1,1) has no parent.
  comb children (18.2.3): node(y, s+2) and, per live door y_a, node(y_a, s0)
  with s0 = 1 if y_a = 1 mod 3 else 2; the root's door child is excluded.
  exit map G(y) = (3^m q - 1)/2^r, m = v2(y+1), q = (y+1)/2^m,
  r = v2(3^m q - 1); stratum(y) = (m, r) (reverse.md 14.14.3.1, 14.14.4;
  itinerary.md 14.15.1.1).

Sections (letters as in the brief's Queue 2):
  canaries  (107,1)'s path and word; door 1's chain; two hand-checked door
            edges (parent doors 5 and 13) with their digit counts.
  (a) Item A on 3000 random states (w < 10^6, d <= 40): the comb path by the
      parent rule against the F-orbit's exit valuations and door indices,
      the cascade counts, eta and lambda by both routes, the letters of the
      exit's itinerary word (r_i = s_(i+1), m_i = D_(i+1) - a_i, last letter
      (1,1)), and lambda from the letters.
  (b) Item B on a level-by-level enumeration to level 20: per level the
      node count, mean D, dead-top-door fraction, mean degree, the ratio of
      consecutive counts (checked exactly equal to the mean degree), and the
      depth distribution against 2*3^-j; the counts against comb.md 18.5.
  (c) Item D: the top-door law on 5000 random (y, s0, j <= 6) -- agreement at
      j + d digits, sharpness at j + d - 1 (same d), the exact identity
      v3(y'_0 - y~'_0) = v3(y - y~) - d; the side-door law at every a < d on
      3000 random edges with d >= 2 -- v3(y'_a + 1) = a, the j - a + d count
      with its sharpness, the identity with d - a, the stratum of the child
      door (d - a, s0) and G(child door) = parent door, the designated door's
      loss of exactly one digit; the boundary cases (y = 1, j = 0, the dead
      top door, d not fixed by y mod 3^d); the identity at a general branch.

Fresh code: imports nothing from any other file in this repository. Exact
Python-integer arithmetic at every pass/fail decision; the only floats are
printed ratios. Canaries run first. Single reproducing command:

    python experiments/comb_dictionary.py

No phases, no flags. Seed 20260916 for every randomized check. The level
enumeration is deterministic; its wall-clock time is printed and is the only
machine-dependent line of the output.
"""

import random
import time

SEED = 20260916
DATE = "2026-09-16"
LEVELS = 20

CHECKS = 0
FAILS = 0
T0 = time.time()


def check(cond, msg=""):
    global CHECKS, FAILS
    CHECKS += 1
    if not cond:
        FAILS += 1
        if FAILS <= 30:
            print("  FAIL:", msg)
    return cond


def report(label):
    print("  %s: %d checks so far, %d failures" % (label, CHECKS, FAILS))


# ---------------------------------------------------------------- arithmetic

def v2(n):
    assert n != 0
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def v3(n):
    assert n != 0
    c = 0
    while n % 3 == 0:
        n //= 3
        c += 1
    return c


def valid(w, d):
    return w >= 1 and w % 2 == 1 and w % 3 != 0 and d >= 1


def peak(w, d):
    return 3 ** d * w - 1


def exit_data(w, d):
    """(s, y): exit valuation and exit of the state."""
    A = peak(w, d)
    s = v2(A)
    return s, A >> s


def state_of_door(y):
    """Door recovery, reverse.md 14.6.5.1: y + 1 = 2^m 3^a W, D = m + a."""
    assert y % 2 == 1 and y % 3 != 0
    m = v2(y + 1)
    q = (y + 1) >> m
    a = v3(q)
    W = q // 3 ** a
    return (W, m + a)


def F(w, d):
    """The reduced map via C = A + 2^s (spine.md 5.6 / reverse.md 14.14.1.1)."""
    A = peak(w, d)
    s = v2(A)
    C = A + (1 << s)
    sigma = v2(C)
    a = v3(C)
    w2 = C // (1 << sigma) // 3 ** a
    return (w2, sigma - s + a)


def doors(W, D):
    return [(1 << (D - a)) * 3 ** a * W - 1 for a in range(D)]


def node(y, s):
    """The state at branch s on door y (14.1.1); None if s is not admissible."""
    N = (1 << s) * y + 1
    if N % 3 != 0:
        return None
    d = v3(N)
    return (N // 3 ** d, d)


def lowest_branch(y):
    return 1 if y % 3 == 1 else 2


def comb_parent(w, d):
    """(kind, parent, door index a): kind 'C' or 'D'; None at the root."""
    if (w, d) == (1, 1):
        return None
    s, y = exit_data(w, d)
    if s >= 3:
        return ("C", node(y, s - 2), None)
    return ("D", state_of_door(y), v3(y + 1))


def comb_children(W, D):
    """[(child, kind)]: the cascade child, then one door child per live door."""
    s, y = exit_data(W, D)
    out = [(node(y, s + 2), "C")]
    for ya in doors(W, D):
        if ya % 3 == 0:
            continue
        child = node(ya, lowest_branch(ya))
        if child == (W, D):
            continue          # the root's door child would be itself
        out.append((child, "D"))
    return out


def stratum(y):
    m = v2(y + 1)
    q = (y + 1) >> m
    r = v2(3 ** m * q - 1)
    return (m, r)


def G(y):
    m, r = stratum(y)
    q = (y + 1) >> m
    return (3 ** m * q - 1) >> r


def top_dead(W, D):
    return ((1 << D) * W) % 3 == 1


# ---------------------------------------------------------------- Item A helpers

def comb_path(w, d, cap=100000):
    """Edges from (w,d) to the root: list of 'C' or ('D', a); the nodes visited."""
    edges = []
    nodes = [(w, d)]
    cur = (w, d)
    while cur != (1, 1):
        p = comb_parent(*cur)
        assert p is not None
        kind, par, a = p
        edges.append("C" if kind == "C" else ("D", a))
        cur = par
        nodes.append(cur)
        if len(edges) > cap:
            return None, None
    return edges, nodes


def orbit_data(w, d, cap=100000):
    """The F-orbit to (1,1): per step (s_i, y_i, a_i, D_(i+1)); eta."""
    steps = []
    cur = (w, d)
    while cur != (1, 1):
        s, y = exit_data(*cur)
        nxt = F(*cur)
        steps.append((s, y, v3(y + 1), nxt[1]))
        cur = nxt
        if len(steps) > cap:
            return None
    return steps


def predicted_edges(steps):
    eta = len(steps)
    out = []
    for i, (s, y, a, D1) in enumerate(steps):
        out.extend(["C"] * ((s - 1) // 2))
        if i < eta - 1:
            out.append(("D", a))
    return out


def item_a_checks(w, d, tag):
    steps = orbit_data(w, d)
    if not check(steps is not None, "%s: orbit did not reach (1,1)" % tag):
        return
    eta = len(steps)
    edges, nodes = comb_path(w, d)
    if not check(edges is not None, "%s: path did not reach the root" % tag):
        return
    lam = len(edges)
    # (a) the edge sequence
    pred = predicted_edges(steps)
    check(edges == pred, "%s: edge sequence %s != predicted %s" % (tag, edges, pred))
    # door edges = eta - 1; lambda formula; cascade edges = lambda - eta + 1 >= 1
    ndoor = sum(1 for e in edges if e != "C")
    check(ndoor == eta - 1, "%s: door edges %d != eta - 1 = %d" % (tag, ndoor, eta - 1))
    lam_formula = sum((s - 1) // 2 for (s, y, a, D1) in steps) + eta - 1
    check(lam == lam_formula, "%s: lambda %d != formula %d" % (tag, lam, lam_formula))
    check(lam - eta + 1 >= 1, "%s: cascade edges < 1" % tag)
    # the last step: exit 1, odd s >= 3, no door edge
    s_last, y_last = steps[-1][0], steps[-1][1]
    check(y_last == 1 and s_last % 2 == 1 and s_last >= 3,
          "%s: last step not on door 1 at odd branch >= 3" % tag)
    # every door edge enters the parent through the door y_i of index a_i
    di = 0
    for i, (s, y, a, D1) in enumerate(steps[:-1]):
        di += (s - 1) // 2
        entered = nodes[di + 1]
        check(entered == F(*nodes[di]) and doors(*entered)[a] == y,
              "%s: door edge %d enters wrong node/door" % (tag, i))
        di += 1
    # (b) letters of the exit's itinerary word
    ys = [st[1] for st in steps]
    for i in range(eta - 1):
        check(G(ys[i]) == ys[i + 1], "%s: G(y_%d) != y_%d" % (tag, i, i + 1))
    check(G(ys[-1]) == 1 and ys[-1] == 1, "%s: last door not 1" % tag)
    letters = [stratum(y) for y in ys]
    s_seq = [st[0] for st in steps] + [1]        # s_eta = s(1,1) = 1
    for i in range(eta):
        m, r = letters[i]
        check(r == s_seq[i + 1], "%s: r_%d = %d != s_%d = %d" % (tag, i, r, i + 1, s_seq[i + 1]))
        check(m == steps[i][3] - steps[i][2], "%s: m_%d != D_(i+1) - a_i" % (tag, i))
    check(letters[-1] == (1, 1), "%s: last letter %s != (1,1)" % (tag, letters[-1]))
    # every door of v has r = s_0
    for yd in doors(w, d):
        if yd % 3 == 0:
            continue
        check(stratum(yd)[1] == steps[0][0], "%s: door %d of v has r != s_0" % (tag, yd))
    lam_word = (steps[0][0] - 1) // 2 + sum((r - 1) // 2 for (m, r) in letters) + eta - 1
    check(lam == lam_word, "%s: lambda %d != word formula %d" % (tag, lam, lam_word))
    return eta, lam


# ---------------------------------------------------------------- canaries

def canaries():
    print("--- Canaries ---")
    # F against door recovery on a few states
    for (w, d) in [(107, 1), (1, 2), (7, 3), (19, 3), (43, 1), (5, 7)]:
        s, y = exit_data(w, d)
        check(F(w, d) == state_of_door(y), "F != state(exit) at %s" % ((w, d),))
    # (107,1): path, distances, word
    edges, nodes = comb_path(107, 1)
    check(nodes == [(107, 1), (1, 4), (7, 1), (1, 2), (1, 1)], "(107,1) path nodes %s" % nodes)
    check(edges == ["C", "C", ("D", 1), "C"], "(107,1) edges %s" % edges)
    res = item_a_checks(107, 1, "(107,1)")
    check(res == (2, 4), "(107,1) (eta, lambda) = %s" % (res,))
    steps = orbit_data(107, 1)
    check([st[0] for st in steps] == [6, 3] and [st[1] for st in steps] == [5, 1],
          "(107,1) s, y sequence")
    check([stratum(st[1]) for st in steps] == [(1, 3), (1, 1)], "(107,1) word")
    # door 1's chain
    chain = [node(1, s) for s in (1, 3, 5, 7, 9)]
    check(chain == [(1, 1), (1, 2), (11, 1), (43, 1), (19, 3)], "door 1 chain %s" % chain)
    check(comb_children(1, 1) == [((1, 2), "C")], "root's children %s" % comb_children(1, 1))
    check(comb_parent(1, 1) is None, "root has a parent")
    # hand-checked door edge, parent door 5: s0 = 2, 21 = 3*7, child (7,1), top door 13
    check(lowest_branch(5) == 2 and node(5, 2) == (7, 1), "door 5 lowest child")
    check(doors(7, 1) == [13], "doors of (7,1)")
    check(node(59, 2) == (79, 1) and doors(79, 1)[0] == 157 and 157 % 9 == 13 % 9,
          "y~ = 59 = 5 mod 27 agrees mod 9 at the top door")
    check(node(23, 2) == (31, 1) and doors(31, 1)[0] == 61 and 61 % 9 != 13 % 9,
          "y~ = 23 = 5 mod 9, not mod 27, disagrees mod 9 at the top door")
    check(v3(157 - 13) == v3(59 - 5) - 1 and v3(61 - 13) == v3(23 - 5) - 1,
          "door 5: identity v3(diff of top doors) = v3(diff of doors) - d")
    # hand-checked door edge, parent door 13: s0 = 1, 27 = 3^3, child (1,3), doors 7, 11, 17
    check(lowest_branch(13) == 1 and node(13, 1) == (1, 3), "door 13 lowest child")
    check(doors(1, 3) == [7, 11, 17], "doors of (1,3)")
    check([v3(y + 1) for y in (7, 11, 17)] == [0, 1, 2], "v3(y'_a + 1) = a on (1,3)")
    check([stratum(y) for y in (7, 11, 17)] == [(3, 1), (2, 1), (1, 1)],
          "strata of (1,3)'s doors are (d - a, s0)")
    check([G(y) for y in (7, 11, 17)] == [13, 13, 13], "G of (1,3)'s doors is 13")
    check(node(175, 1) == (13, 3) and doors(13, 3) == [103, 155, 233], "y~ = 175 child")
    check(node(67, 1) == (5, 3) and doors(5, 3) == [39, 59, 89], "y~ = 67 child")
    check(103 % 3 == 7 % 3, "top door agrees mod 3 at 81 digits (j=1, d=3)")
    check(39 % 3 != 7 % 3 and 39 % 3 == 0, "top door disagrees mod 3 at 27 digits; 39 is dead")
    check(233 % 27 == 17 % 27, "side door a=2 agrees mod 27 at 3^4 (j=3, d=3, a=2)")
    check(89 % 27 != 17 % 27, "side door a=2 disagrees mod 27 at 3^3")
    check(v3(233 - 17) == v3(175 - 13) - (3 - 2) and v3(89 - 17) == v3(67 - 13) - 1,
          "door 13: identity at a = 2")
    check(v3(103 - 7) == v3(175 - 13) - 3 and v3(39 - 7) == v3(67 - 13) - 3,
          "door 13: identity at a = 0")
    # y = 1: the self-loop
    check(node(1, 1) == (1, 1) and doors(1, 1) == [1] and (4 * 1 - 1) // 3 == 1, "y = 1 self-loop")
    # 14.14.7's worked instance as a sanity check of G
    check(stratum(7) == (3, 1) and G(7) == 13, "G(7) = 13")
    report("canaries")


# ---------------------------------------------------------------- (a) Item A

def section_a(rng):
    print("--- (a) Item A: the comb path is the word, 3000 random states (w < 10^6, d <= 40) ---")
    n = 0
    max_eta = max_lam = 0
    while n < 3000:
        w = rng.randrange(1, 10 ** 6, 2)
        if w % 3 == 0:
            continue
        d = rng.randint(1, 40)
        res = item_a_checks(w, d, "(%d,%d)" % (w, d))
        if res is not None:
            max_eta = max(max_eta, res[0])
            max_lam = max(max_lam, res[1])
        n += 1
    print("  3000 states; largest eta %d, largest lambda %d" % (max_eta, max_lam))
    report("(a)")


# ---------------------------------------------------------------- (b) Item B

CENSUS_18_5 = [1, 1, 2, 3, 10, 17, 30, 61, 124, 239, 478, 961, 1978, 3823, 7748,
               15597, 30844, 61947, 124068, 247507, 495986]


def section_b():
    print("--- (b) Item B: level-by-level enumeration to level %d; the mean degree ---" % LEVELS)
    t = time.time()
    level = [(1, 1)]
    rows = []
    for lam in range(LEVELS + 1):
        n = len(level)
        sumD = 0
        dead = 0
        sumdeg = 0
        dist = {}
        nxt = []
        seen = set()
        for (W, D) in level:
            sumD += D
            dist[D] = dist.get(D, 0) + 1
            ch = comb_children(W, D)
            deg = len(ch)
            sumdeg += deg
            if (W, D) == (1, 1):
                check(deg == 1, "root degree %d" % deg)
                isdead = 0
            else:
                isdead = 1 if top_dead(W, D) else 0
                check(deg == 1 + D - isdead, "degree formula at %s" % ((W, D),))
            dead += isdead
            for (c, kind) in ch:
                check(c is not None and valid(*c), "invalid child of %s" % ((W, D),))
                p = comb_parent(*c)
                check(p is not None and p[1] == (W, D) and p[0] == kind,
                      "child %s of %s has parent %s" % (c, (W, D), p))
                check(c not in seen, "duplicate child %s" % (c,))
                seen.add(c)
                nxt.append(c)
        rows.append((lam, n, sumD, dead, sumdeg, dist))
        if lam < LEVELS:
            check(sumdeg == len(nxt), "sum of degrees %d != next level count %d" % (sumdeg, len(nxt)))
        if lam >= 1:
            check(sumdeg == n + sumD - dead, "mean-degree identity at level %d" % lam)
        check(lam >= len(CENSUS_18_5) or n == CENSUS_18_5[lam],
              "level %d count %d != comb.md 18.5's %d" % (lam, n, CENSUS_18_5[lam]))
        level = nxt
    elapsed = time.time() - t
    print("  level     nodes   mean D  dead-top  door-ch  mean deg  next/this   P(D=1..6) against 2/3^j")
    ledger = ["%.4f" % (2 / 3 ** j) for j in range(1, 7)]
    print("  ledger                                                     " + " ".join(ledger))
    for (lam, n, sumD, dead, sumdeg, dist) in rows:
        ratio = "%.4f" % (rows[lam + 1][1] / n) if lam + 1 < len(rows) else "   -  "
        frac = " ".join("%.4f" % (dist.get(j, 0) / n) for j in range(1, 7))
        print("  %5d %9d  %7.4f  %8.4f  %7.4f  %8.4f  %s   %s"
              % (lam, n, sumD / n, dead / n, sumD / n - dead / n, sumdeg / n, ratio, frac))
    total = sum(r[1] for r in rows)
    print("  %d nodes over levels 0..%d [%.1fs]" % (total, LEVELS, elapsed))
    report("(b)")


# ---------------------------------------------------------------- (c) Item D

def random_live_door(rng, bits=60):
    while True:
        y = rng.getrandbits(bits) | 1
        if y % 3 != 0:
            return y


def door_edge(y, s=None):
    """(s, d, w, doors of the child) for the door edge at the lowest branch (or at s)."""
    if s is None:
        s = lowest_branch(y)
    child = node(y, s)
    assert child is not None
    w, d = child
    return s, d, w, doors(w, d)


def section_c(rng):
    print("--- (c) Item D: the digit-transfer law across a door edge ---")
    # top door: 5000 random (y, s0, j <= 6)
    n = 0
    agree = sharp = sharp_filtered = dead = 0
    while n < 5000:
        y = random_live_door(rng)
        s0, d, w, ds = door_edge(y)
        j = rng.randint(1, 6)
        # agreement at j + d digits: y~ = y + 2 t 3^(j+d)
        t = rng.randint(1, 1000)
        yt = y + 2 * t * 3 ** (j + d)
        st, dt, wt, dst = door_edge(yt)
        check(st == s0 and dt == d, "top: agreement mod 3^(j+d) did not fix (s0, d)")
        check(dst[0] % 3 ** j == ds[0] % 3 ** j, "top: y'_0 differs mod 3^j under agreement")
        check(v3(dst[0] - ds[0]) == v3(yt - y) - d, "top: identity failed (agreement case)")
        agree += 1
        # sharpness at j + d - 1 digits, same d: y~ = y + 2 t 3^(j+d-1), 3 does not divide t
        t = rng.randint(1, 1000)
        while t % 3 == 0:
            t = rng.randint(1, 1000)
        yt = y + 2 * t * 3 ** (j + d - 1)
        st, dt, wt, dst = door_edge(yt)
        check(st == s0, "top: s0 changed under agreement mod 3")
        if dt != d:
            check(j == 1 and dt > d, "top: d changed with j >= 2")
            sharp_filtered += 1
        else:
            check(dst[0] % 3 ** j != ds[0] % 3 ** j, "top: y'_0 agrees mod 3^j at one digit short")
            check(v3(dst[0] - ds[0]) == v3(yt - y) - d == j - 1, "top: identity failed (sharp case)")
            sharp += 1
        # the dead top door: its status is a function of y mod 3^(d+1)
        if ds[0] % 3 == 0:
            dead += 1
            check(top_dead(w, d), "dead top door not detected by 14.5.1's criterion")
        # d not fixed by y mod 3^d: construct a lift with d~ >= d + 1
        t = 1
        while (w + 2 ** (s0 + 1) * t) % 3 != 0:
            t += 1
        yt = y + 2 * t * 3 ** d
        check(door_edge(yt)[1] >= d + 1, "d fixed by y mod 3^d after all")
        # designated door (14.6.1): loss exactly one digit
        a_star = 0 if d == 1 else d - 1
        t = rng.randint(1, 1000)
        while t % 3 == 0:
            t = rng.randint(1, 1000)
        for (extra, want_equal) in ((1, True), (0, False)):
            yt = y + 2 * t * 3 ** (j + extra)
            st, dt, wt, dst = door_edge(yt)
            if dt != d:
                continue   # same-d hypothesis fails (only possible at j + extra = d)
            eq = dst[a_star] % 3 ** j == ds[a_star] % 3 ** j
            check(eq == want_equal, "designated door: loss is not exactly one digit")
        n += 1
    print("  5000 edges: %d agreements at j+d digits, %d sharp disagreements at j+d-1 (same d),"
          % (agree, sharp))
    print("  %d sharpness draws filtered (j = 1, the lift changed d), %d child top doors dead"
          % (sharp_filtered, dead))
    report("(c) top door")
    # side doors: 3000 random edges with d >= 2, every a < d
    n = 0
    pairs = 0
    dmax = 0
    while n < 3000:
        y = random_live_door(rng)
        s0, d, w, ds = door_edge(y)
        if d < 2:
            continue
        dmax = max(dmax, d)
        for a in range(d):
            ya = ds[a]
            check(v3(ya + 1) == a, "v3(y'_a + 1) != a")
            check(stratum(ya) == (d - a, s0), "stratum of child door != (d - a, s0)")
            check(G(ya) == y, "G(child door) != parent door")
            for j in range(a + 1, a + 6):
                k = j - a + d
                t = rng.randint(1, 1000)
                yt = y + 2 * t * 3 ** k
                st, dt, wt, dst = door_edge(yt)
                check(st == s0 and dt == d, "side: agreement mod 3^(j-a+d) did not fix (s0, d)")
                check(dst[a] % 3 ** j == ya % 3 ** j, "side: y'_a differs mod 3^j under agreement")
                check(v3(dst[a] - ya) == v3(yt - y) - (d - a), "side: identity failed (agreement)")
                t = rng.randint(1, 1000)
                while t % 3 == 0:
                    t = rng.randint(1, 1000)
                yt = y + 2 * t * 3 ** (k - 1)
                st, dt, wt, dst = door_edge(yt)
                if dt != d:
                    check(j - a == 1, "side: d changed with j - a >= 2")
                    continue
                check(dst[a] % 3 ** j != ya % 3 ** j, "side: y'_a agrees mod 3^j one digit short")
                check(v3(dst[a] - ya) == v3(yt - y) - (d - a) == j - 1, "side: identity failed (sharp)")
                pairs += 1
            # j <= a: the residue is -1 mod 3^j whatever the parent door
            for j in range(0, a + 1):
                check((ya + 1) % 3 ** j == 0, "y'_a != -1 mod 3^j for j <= a")
            yo = random_live_door(rng)
            so, do, wo, dso = door_edge(yo)
            if do > a:
                check((dso[a] - ya) % 3 ** a == 0, "two unrelated door-a residues differ mod 3^a")
        n += 1
    print("  3000 edges with d >= 2 (largest d %d), every a < d, j = a+1..a+5: %d sharp pairs"
          % (dmax, pairs))
    report("(c) side doors")
    # the identity at a general branch s (the same door, higher on the chain)
    n = 0
    while n < 2000:
        y = random_live_door(rng)
        s = lowest_branch(y) + 2 * rng.randint(0, 14)
        s_, d, w, ds = door_edge(y, s)
        a = rng.randint(0, d - 1)
        k = rng.randint(0, 5)
        t = rng.randint(1, 1000)
        while t % 3 == 0:
            t = rng.randint(1, 1000)
        yt = y + 2 * t * 3 ** (d + k)
        st, dt, wt, dst = door_edge(yt, s)
        if dt != d:
            check(k == 0, "branch s: d changed with k >= 1")
            continue
        check(v3(dst[a] - ds[a]) == v3(yt - y) - (d - a) == k + a, "branch s: identity failed")
        n += 1
    print("  2000 edges at branches s <= 30: the identity with d(y,s) in place of d")
    # boundary: j = 0 -- every residue mod 1 agrees, and agreement at 3^(0+d) = 3^d
    # digits does not fix d: doors 5 and 11 agree mod 3 with d = 1 and d = 2
    check(doors(*node(5, 2))[0] % 1 == doors(*node(23, 2))[0] % 1, "j = 0 vacuous")
    check(door_edge(5)[1] == 1 and door_edge(11)[1] == 2 and (11 - 5) % 3 == 0,
          "j = 0 boundary: 5 and 11 agree mod 3^d = 3 but d differs")
    report("(c)")


# ---------------------------------------------------------------- main

def main():
    print("comb_dictionary.py -- seed %d, %s" % (SEED, DATE))
    rng = random.Random(SEED)
    canaries()
    section_a(rng)
    section_b()
    section_c(rng)
    print()
    print("TOTAL: checks=%d, failures=%d" % (CHECKS, FAILS))
    print("time=%.1fs" % (time.time() - T0))


if __name__ == "__main__":
    main()
