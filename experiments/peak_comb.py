"""Independent verification for briefs/peak-comb-brief.md -- comb.md section 18,
the peak comb: the backward tree of reduced states re-rooted on peaks, with the
infinite fan over s on each door replaced by a chain of cascade edges.

Objects (all from the wiki's own definitions, re-implemented here):
  state (w,d): w odd, 3 does not divide w, d >= 1 (spine.md section 3.5).
  peak  A(w,d) = 3^d w - 1 = 2^s y, s = v2(A), y the exit (spine.md 9.1.1).
  F(w,d) via C = A + 2^s (spine.md 5.6); state(y) via door recovery
  (reverse.md 14.6.5.1); predecessors via doors x admissible s (14.1.1).
  comb parent: s >= 3 -> the state at branch s-2 on the same door (a cascade
  edge, reverse.md 14.10.1 read downward); s <= 2 -> state(y) = F(w,d) (a door
  edge). The root (1,1) has no parent (its own s=1 door child is itself).

Sections (letters as in the brief's Queue 2):
  canaries  (1,1) and its single child; door 5's three states and the raw
            orbit of 213; (7,3)'s three doors and the lowest child on each.
  (a) peak <-> state bijection; peak / non-peak alternation along a door's
      cascade against 14.1.1's admissible s.
  (b) the parent rule on a box: unique valid parent, the inverse (child) rule,
      the local chain lemma, the tree property against F-orbits, the root's
      single child, the degree formula against 14.1.1 and a brute-force
      forward scan.
  (c) the 4A cascade law and the 2A raw-maximum remark.
  (e) completeness against the raw map, brute force on a box of odd x.
  (f) the census by level, no size cutoff: a level-by-level pass to
      LEVELS_BFS (the cross-check) and a depth-first pass to LEVELS_DEEP
      (the census of record; the two must agree row for row), with
  (d) the two distances (r by iterating F, l = level) on every node,
  (g) ladder.md 15.6.2's forced chain in comb language, and
  (h) one exploratory table (run lengths against the 2^-j ledger),
      then the comparison with reverse.md 14.4's core-size counts.

Fresh code: imports nothing from any other file in this repository (in
particular not experiments/reverse_tree.py). Exact Python-integer arithmetic
at every pass/fail decision; the only floats are printed ratios. Canaries run
first. Single reproducing command:

    python experiments/peak_comb.py

No phases, no flags. Seed 20260915 for every randomized check. The census is
deterministic (no randomness); its wall-clock time is printed and is the only
machine-dependent line of the output.
"""

import random
import time
import heapq

SEED = 20260915
DATE = "2026-09-15"
LEVELS_BFS = 20        # level-by-level pass (whole levels in memory), the cross-check
LEVELS_DEEP = 27       # depth-first pass (constant memory), the census of record
R_SAMPLE = 2000        # direct r check: every node while a level has <= R_SAMPLE nodes,
                       # a deterministic hash sample of about R_SAMPLE per level above

CHECKS = 0
FAILS = 0
T0 = time.time()


def check(cond, msg):
    global CHECKS, FAILS
    CHECKS += 1
    if not cond:
        FAILS += 1
        print("  FAIL:", msg)


def running(label):
    print("  %s: %d checks so far, %d failures" % (label, CHECKS, FAILS))


# ---------------------------------------------------------------- primitives

def v2(n):
    return (n & -n).bit_length() - 1


def v3(n):
    v = 0
    while n % 3 == 0:
        n //= 3
        v += 1
    return v


def valid(w, d):
    return w >= 1 and w % 2 == 1 and w % 3 != 0 and d >= 1


def peak(w, d):
    return 3 ** d * w - 1


def exit_data(w, d):
    A = 3 ** d * w - 1
    s = v2(A)
    return A, s, A >> s


def F(w, d):
    # spine.md 5.6: C = A + 2^s; omega_+ = C/(2^sigma 3^a_+), d_+ = sigma - s + a_+
    A = 3 ** d * w - 1
    s = v2(A)
    C = A + (1 << s)
    sig = v2(C)
    u = C >> sig
    a = v3(u)
    return (u // 3 ** a, sig - s + a)


def state_of_door(y):
    # reverse.md 14.6.5.1: y + 1 = 2^m 3^a Omega, D = m + a
    m = v2(y + 1)
    q = (y + 1) >> m
    a = v3(q)
    return (q // 3 ** a, m + a)


def peak_state(A):
    # claim (i)/(ii): an even A >= 2 with 3 | A+1 is the peak of exactly one state
    if A < 2 or A % 2 != 0 or (A + 1) % 3 != 0:
        return None
    d = v3(A + 1)
    return ((A + 1) // 3 ** d, d)


def doors(W, D):
    return [(a, 2 ** (D - a) * 3 ** a * W - 1) for a in range(D)]


def lowest(y):
    return 1 if y % 3 == 1 else 2


def node_on_door(y, s):
    N = (y << s) + 1
    assert N % 3 == 0
    d = v3(N)
    return (N // 3 ** d, d)


def comb_parent(w, d):
    if (w, d) == (1, 1):
        return None
    A, s, y = exit_data(w, d)
    if s >= 3:
        return ('C', node_on_door(y, s - 2))
    return ('D', state_of_door(y))


def comb_children(W, D):
    A, s, y = exit_data(W, D)
    kids = [('C', node_on_door(y, s + 2))]
    for a, ya in doors(W, D):
        if ya % 3 == 0:
            continue
        c = node_on_door(ya, lowest(ya))
        if c == (W, D):        # the root's own s=1 door child is the root: excluded
            continue
        kids.append(('D', c))
    return kids


def preds_14_1_1(W, D, smax):
    # reverse.md 14.1.1: doors x admissible s (s odd iff y = 1 mod 3)
    out = []
    for a, y in doors(W, D):
        if y % 3 == 0:
            continue
        s = lowest(y)
        while s <= smax:
            out.append((node_on_door(y, s), a, y, s))
            s += 2
    return out


def f_orbit_len(w, d, cap):
    # reduced distance: number of F-steps to (1,1); None if the cap is hit
    r = 0
    while (w, d) != (1, 1):
        w, d = F(w, d)
        r += 1
        if r > cap:
            return None
    return r


def col_steps(x, n):
    out = [x]
    for _ in range(n):
        x = x // 2 if x % 2 == 0 else 3 * x + 1
        out.append(x)
    return out


def reps(w, d):
    return [2 ** (d - a) * 3 ** a * w - 1 for a in range(d)]


# ------------------------------------------------------------------ canaries

print("peak_comb.py -- seed %d, %s" % (SEED, DATE))
print("--- Canaries ---")
random.seed(SEED)

# the root
A, s, y = exit_data(1, 1)
check((A, s, y) == (2, 1, 1), "root peak/exit")
check(F(1, 1) == (1, 1) and state_of_door(1) == (1, 1), "root fixed")
check(comb_parent(1, 1) is None, "root has no parent")
check(comb_children(1, 1) == [('C', (1, 2))], "root's single child (1,2): %r" % (comb_children(1, 1),))
check(comb_parent(1, 2) == ('C', (1, 1)), "(1,2)'s parent is the root by a cascade edge")
# door 1's own chain, branches 1,3,5,7,9
chain1 = [node_on_door(1, s) for s in (1, 3, 5, 7, 9)]
check(chain1 == [(1, 1), (1, 2), (11, 1), (43, 1), (19, 3)], "door-1 chain %r" % (chain1,))
for st in chain1[1:]:
    check(F(*st) == (1, 1), "door-1 node %r maps to the root" % (st,))

# door 5: (7,1), (1,4), (107,1) at s = 2, 4, 6 with peaks 20, 80, 320
d5 = [node_on_door(5, s) for s in (2, 4, 6)]
check(d5 == [(7, 1), (1, 4), (107, 1)], "door 5 nodes %r" % (d5,))
check([peak(*st) for st in d5] == [20, 80, 320], "door 5 peaks")
for st, ss in zip(d5, (2, 4, 6)):
    A, s, y = exit_data(*st)
    check((s, y) == (ss, 5), "door 5 node %r exit data" % (st,))
check(reps(107, 1) == [213], "entry of (107,1) is 213")
orb = col_steps(213, 8)
check(orb == [213, 640, 320, 160, 80, 40, 20, 10, 5], "raw orbit of 213: %r" % (orb,))
check(80 in orb and 20 in orb, "orbit of 213 passes the peaks 80 and 20")
check(reps(1, 4) == [15, 23, 35, 53] and reps(7, 1) == [13], "representatives of (1,4), (7,1)")
check(not any(v in orb for v in (15, 23, 35, 53, 13)), "orbit of 213 avoids the odd points of (1,4), (7,1)")
check(comb_parent(107, 1) == ('C', (1, 4)) and comb_parent(1, 4) == ('C', (7, 1)), "door 5 cascade parents")
check(comb_parent(7, 1) == ('D', (1, 2)) and F(7, 1) == (1, 2), "door 5 door parent (1,2)")

# (7,3): doors 55 (top), 83, 125; lowest children (37,1)@s=1, (37,2)@s=2, (167,1)@s=2
check([y for a, y in doors(7, 3)] == [55, 83, 125], "doors of (7,3)")
kids73 = comb_children(7, 3)
check(kids73[0] == ('C', (251, 1)) and peak(251, 1) == 4 * peak(7, 3), "cascade child of (7,3): %r" % (kids73[0],))
check(kids73[1:] == [('D', (37, 1)), ('D', (37, 2)), ('D', (167, 1))], "door children of (7,3): %r" % (kids73[1:],))
for st, ss, yy in (((37, 1), 1, 55), ((37, 2), 2, 83), ((167, 1), 2, 125)):
    A, s, y = exit_data(*st)
    check((s, y) == (ss, yy) and F(*st) == (7, 3), "(7,3) door child %r at s=%d on door %d" % (st, ss, yy))
running("canaries")

# ------------------------------------------------- (a) bijection, alternation

print("--- (a) peak <-> state bijection; peak / non-peak alternation on doors ---")
random.seed(SEED)
n_bij = 0
for _ in range(3000):
    w = random.randrange(1, 10 ** 6, 2)
    if w % 3 == 0:
        continue
    d = random.randrange(1, 41)
    A = peak(w, d)
    check(A % 2 == 0 and (A + 1) % 3 == 0, "peak parity/residue at %r" % ((w, d),))
    check(peak_state(A) == (w, d), "peak -> state at %r" % ((w, d),))
    check(v3(A + 1) == d and (A + 1) // 3 ** d == w, "claim (i) formulas at %r" % ((w, d),))
    n_bij += 1
n_even = 0
for _ in range(3000):
    A = random.randrange(2, 10 ** 12, 2)
    st = peak_state(A)
    if A % 3 == 2:
        check(st is not None and valid(*st) and peak(*st) == A, "even A = 2 mod 3 is a peak: %d" % A)
    else:
        check(st is None, "even A != 2 mod 3 is not a peak: %d" % A)
    n_even += 1
# alternation along a door's cascade: 2^j y is a peak iff 3 | 2^j y + 1 iff j admissible (14.1.1)
n_alt = 0
for _ in range(2000):
    y = random.randrange(1, 10 ** 7, 2)
    for j in range(1, 41):
        z = y << j
        is_peak = peak_state(z) is not None
        adm = (y % 3 == 1 and j % 2 == 1) or (y % 3 == 2 and j % 2 == 0)
        check(is_peak == adm, "alternation at y=%d j=%d" % (y, j))
        if adm:
            st = node_on_door(y, j)
            A, s, yy = exit_data(*st)
            check(A == z and s == j and yy == y, "peak 2^j y belongs to the branch-j node on door y (%d,%d)" % (y, j))
        n_alt += 1
running("(a): %d states, %d even integers, %d (door, branch) pairs" % (n_bij, n_even, n_alt))

# ------------------------------------------------------- (b) the parent rule

print("--- (b) the parent rule on the box w < 10^5, d <= 30 ---")
WBOX, DBOX = 10 ** 5, 30
n_box = 0
self_excl = 0
k_hist_box = {}
dr_hist_box = {}
box_s1 = box_s2 = 0
t_b = time.time()
for w in range(1, WBOX, 2):
    if w % 3 == 0:
        continue
    for d in range(1, DBOX + 1):
        n_box += 1
        A, s, y = exit_data(w, d)
        k = (s - 1) // 2
        k_hist_box[k] = k_hist_box.get(k, 0) + 1
        if s <= 2 and (w, d) != (1, 1):
            # forward door run: consecutive F-iterates with s <= 2, starting at this state
            if s == 1:
                box_s1 += 1
            else:
                box_s2 += 1
            nn = 1
            cur = F(w, d)
            while cur != (1, 1) and exit_data(*cur)[1] <= 2:
                nn += 1
                cur = F(*cur)
            dr_hist_box[nn] = dr_hist_box.get(nn, 0) + 1
        par = comb_parent(w, d)
        if (w, d) == (1, 1):
            check(par is None, "root parent")
            continue
        typ, p = par
        check(valid(*p), "parent valid at %r" % ((w, d),))
        if s >= 3:
            check(typ == 'C', "cascade edge at s>=3 %r" % ((w, d),))
            Ap, sp, yp = exit_data(*p)
            check(sp == s - 2 and yp == y, "cascade parent at branch s-2 on the same door %r" % ((w, d),))
        else:
            check(typ == 'D' and p == F(w, d) and p == state_of_door(y), "door parent = F = state(y) %r" % ((w, d),))
        # inverse: the node is among its parent's children, exactly once
        kids = comb_children(*p)
        check(sum(1 for t, c in kids if c == (w, d) and t == typ) == 1, "inverse child rule %r" % ((w, d),))
        # local chain lemma: k cascade steps reach the lowest sibling; then one door edge to F, or the root
        cur = (w, d)
        ok = True
        for i in range(k):
            pc = comb_parent(*cur)
            if pc is None or pc[0] != 'C':
                ok = False
                break
            cur = pc[1]
        low = node_on_door(y, s - 2 * k)
        check(ok and cur == low, "k=%d cascade steps reach the lowest sibling %r from %r" % (k, low, (w, d)))
        Al, sl, yl = exit_data(*low)
        check(sl <= 2 and yl == y, "lowest sibling has s<=2 on the same door %r" % ((w, d),))
        if low == (1, 1):
            check(y == 1 and F(w, d) == (1, 1), "root reached by cascade => F = root, door 1 %r" % ((w, d),))
        else:
            pl = comb_parent(*low)
            check(pl == ('D', F(w, d)), "door edge from the lowest sibling to F %r" % ((w, d),))
        if any(c == (w, d) for t, c in comb_children(w, d)):
            self_excl += 1
print("  box: %d states; self-child exclusion fired at %d states (expected: the root only) [%.1fs]"
      % (n_box, self_excl, time.time() - t_b))
check(self_excl == 0, "self-child exclusion fires only at the root (root skipped above)")
running("(b) local parent rule")

# tree property: parent chains reach the root iff F-orbits reach (1,1)
print("  tree property: F-orbit reachability, exhaustive on w < 2*10^4, d <= 30 (memoized)")
t_b = time.time()
memo = {(1, 1): 0}
unreached = []
CAP = 100000
for w in range(1, 2 * 10 ** 4, 2):
    if w % 3 == 0:
        continue
    for d in range(1, DBOX + 1):
        path = []
        cur = (w, d)
        n = 0
        while cur not in memo:
            path.append(cur)
            cur = F(*cur)
            n += 1
            if n > CAP:
                break
        if cur in memo:
            base = memo[cur]
            for i, st in enumerate(path):
                memo[st] = base + len(path) - i
        else:
            unreached.append((w, d))
check(len(unreached) == 0, "states not reaching (1,1) within the cap: %r" % (unreached[:5],))
n_sub = sum(1 for w in range(1, 2 * 10 ** 4, 2) if w % 3 for d in range(1, DBOX + 1))
print("  %d states, all reach (1,1); max r = %d; %d distinct states memoized [%.1fs]"
      % (n_sub, max(memo.values()), len(memo), time.time() - t_b))
running("(b) reachability")

print("  tree property: full parent chain vs F-orbit on 3000 random states of the box")
random.seed(SEED)
n_chain = 0
max_l = 0
while n_chain < 3000:
    w = random.randrange(1, WBOX, 2)
    if w % 3 == 0:
        continue
    d = random.randrange(1, DBOX + 1)
    # F-orbit
    orbit = [(w, d)]
    while orbit[-1] != (1, 1):
        orbit.append(F(*orbit[-1]))
        if len(orbit) > CAP:
            break
    check(orbit[-1] == (1, 1), "F-orbit reaches root %r" % ((w, d),))
    r = len(orbit) - 1
    # parent chain
    edges = []
    cur = (w, d)
    while cur != (1, 1):
        typ, p = comb_parent(*cur)
        edges.append((typ, p))
        cur = p
        if len(edges) > 10 * CAP:
            break
    check(cur == (1, 1), "parent chain reaches root %r" % ((w, d),))
    l = len(edges)
    max_l = max(max_l, l)
    door_targets = [p for t, p in edges if t == 'D']
    n_door = len(door_targets)
    n_casc = l - n_door
    # the door edges visit the F-orbit in order, up to the last state before (1,1)
    check(door_targets == orbit[1:-1], "door-edge targets = F-orbit minus the root %r" % ((w, d),))
    # corrected (ix): r = door edges + 1; cascade edges = l - r + 1 >= 1; last edge is (1,2)->(1,1)
    check(r == n_door + 1, "r = door edges + 1 at %r (r=%d, doors=%d)" % ((w, d), r, n_door))
    check(n_casc == l - r + 1 and n_casc >= 1, "cascade edges = l - r + 1 >= 1 at %r" % ((w, d),))
    check(edges[-1] == ('C', (1, 1)) and (edges[-2][1] if l >= 2 else (w, d)) == (1, 2),
          "every path enters the root by the edge (1,2)->(1,1) %r" % ((w, d),))
    check(l >= r and ((l == r) == (n_casc == 1)), "l >= r, equality iff exactly one cascade edge %r" % ((w, d),))
    n_chain += 1
print("  %d chains; max level %d; brief's (ix) as stated (r = door edges) held on 0 of them" % (n_chain, max_l))
running("(b) chains")

print("  degree formula: comb children = cascade child + live doors, against 14.1.1")
random.seed(SEED)
n_deg = 0
n_pred = 0
while n_deg < 2000:
    W = random.randrange(1, 10 ** 4, 2)
    if W % 3 == 0:
        continue
    D = random.randrange(1, 13)
    if (W, D) == (1, 1):
        continue
    kids = comb_children(W, D)
    live = [y for a, y in doors(W, D) if y % 3 != 0]
    top_dead = (2 ** D * W) % 3 == 1
    check(len(live) == D - (1 if top_dead else 0), "live doors = D or D-1 by 14.5.1 at %r" % ((W, D),))
    check(all(y % 3 != 0 for a, y in doors(W, D) if a >= 1), "side doors never dead at %r" % ((W, D),))
    check(len(kids) == 1 + len(live), "degree = 1 + live doors at %r" % ((W, D),))
    check(len(set(c for t, c in kids)) == len(kids), "children distinct at %r" % ((W, D),))
    for t, c in kids:
        check(comb_parent(*c) == (t, (W, D)), "child's parent is the node at %r" % ((W, D),))
    # door children = 14.1.1 predecessors with s <= 2; higher-s predecessors chain by cascade to them
    P = preds_14_1_1(W, D, 60)
    low_set = set(st for st, a, y, s in P if s <= 2)
    check(low_set == set(c for t, c in kids if t == 'D'), "door children = predecessors at s<=2 at %r" % ((W, D),))
    for st, a, y, s in P:
        check(F(*st) == (W, D), "14.1.1 predecessor maps forward at %r" % ((W, D),))
        cur = st
        for i in range((s - lowest(y)) // 2):
            pc = comb_parent(*cur)
            check(pc is not None and pc[0] == 'C', "cascade chain from branch s=%d on door %d" % (s, y))
            cur = pc[1]
        check(cur in low_set, "branch-%d predecessor chains down to a door child at %r" % (s, (W, D)))
        n_pred += 1
    n_deg += 1
print("  %d states, %d predecessors (s <= 60) placed on cascade chains above door children" % (n_deg, n_pred))
# brute-force forward scan: all F-preimages in a box vs the comb's prediction
scan = {}
for w in range(1, 3001, 2):
    if w % 3 == 0:
        continue
    for d in range(1, 13):
        scan.setdefault(F(w, d), set()).add((w, d))
for tgt in ((1, 1), (1, 2), (7, 1), (7, 3), (1, 4), (25, 2), (11, 4), (35, 2)):
    brute = scan.get(tgt, set())
    pred = set(st for st, a, y, s in preds_14_1_1(tgt[0], tgt[1], 60) if st[0] <= 3000 and st[1] <= 12)
    check(brute == pred, "forward scan = comb prediction at %r (%d vs %d)" % (tgt, len(brute), len(pred)))
running("(b) degree formula and forward scan")

# ------------------------------------------------- (c) 4A law, 2A raw maximum

print("--- (c) the 4A cascade law; the raw maximum 2A of a block ---")
random.seed(SEED)
n_c = 0
for _ in range(3000):
    w = random.randrange(1, 10 ** 5, 2)
    if w % 3 == 0:
        continue
    d = random.randrange(1, 21)
    A, s, y = exit_data(w, d)
    typ, c = comb_children(w, d)[0]
    Ac, sc, yc = exit_data(*c)
    check(typ == 'C' and Ac == 4 * A and sc == s + 2 and yc == y, "4A law at %r" % ((w, d),))
    check((Ac + 1) == 4 * (A + 1) - 3, "N(y,s+2) = 4N(y,s) - 3 at %r" % ((w, d),))
    # raw trajectory from every representative to the exit: maximum 2A, never a peak
    rs = reps(w, d)
    for a, x in enumerate(rs):
        n_steps = 2 * (d - a) + s      # odd steps and paired halvings inside the block, then the cascade
        tr = col_steps(x, n_steps)
        check(tr[-1] == y and max(tr) == 2 * A, "raw maximum 2A from representative %d of %r" % (x, (w, d)))
        check(tr[2 * (d - 1 - a) + 1] == 2 * A and tr[2 * (d - 1 - a) + 2] == A, "2A then A at the block's end %r" % ((w, d),))
        check(peak_state(2 * A) is None, "2A is never a peak %r" % ((w, d),))
        # the peaks the trajectory passes are exactly the branch-j nodes of door y at admissible j <= s
        passed = [z for z in tr if z % 2 == 0 and peak_state(z) is not None]
        expect = [y << j for j in range(s, 0, -1) if peak_state(y << j) is not None]
        check(passed == expect, "peaks passed = lower siblings' peaks %r" % ((w, d),))
        n_c += 1
print("  %d (representative, block) trajectories" % n_c)
running("(c)")

# -------------------------------------------- (e) completeness vs the raw map

print("--- (e) completeness against the raw map: odd x < 2*10^5 ---")
n_e = 0
n_z = 0
for x in range(1, 2 * 10 ** 5, 2):
    W, D = state_of_door(x)
    a0 = v3((x + 1) >> v2(x + 1))
    rs = reps(W, D)
    check(rs[a0] == x, "x is representative a=%d of its state %r" % (a0, (W, D)))
    A, s, y = exit_data(W, D)
    expect = []
    for b in range(a0, D):
        expect.append(rs[b])
        expect.append(2 * (rs[b + 1] if b + 1 < D else A))
    for j in range(s, -1, -1):
        expect.append(y << j)
    tr = col_steps(x, len(expect) - 1)
    check(tr == expect, "block trajectory bookkeeping at x=%d" % x)
    Ys = state_of_door(y)
    ay = v3((y + 1) >> v2(y + 1))
    for idx, z in enumerate(expect):
        actual = [(z - 1) // 3] if z % 6 == 4 else []          # odd predecessors under Col
        if z % 2 == 1:
            pred = []
        elif idx < 2 * (D - a0):                                 # z = 2 x_{b+1} or 2A inside the block
            b = a0 + idx // 2
            pred = [rs[b]]
        else:                                                    # z = 2^j y on the cascade, j = s .. 1
            j = s - (idx - 2 * (D - a0))
            if z % 3 == 2:
                pred = []                                        # a peak: no odd predecessor
                check(peak_state(z) == node_on_door(y, j), "cascade peak is the branch-j sibling at x=%d" % x)
            elif j >= 2:
                sib = node_on_door(y, j - 1)
                pred = [reps(*sib)[-1]]                          # last odd point of the branch-(j-1) node
            else:
                check(ay >= 1 and y % 3 == 2, "2y has an odd predecessor only for a side door y at x=%d" % x)
                pred = [reps(*Ys)[ay - 1]]                       # the previous door of state(y)
        check(actual == pred, "odd predecessors of %d on the trajectory of x=%d: %r vs %r" % (z, x, actual, pred))
        n_z += 1
    n_e += 1
print("  %d odd x, %d trajectory points, odd predecessors matched exactly" % (n_e, n_z))
running("(e)")

# ---------------------------------------------------------------- (f) census
#
# Two traversals of the same tree. The level-by-level pass keeps whole levels in
# memory and stops at LEVELS_BFS; the depth-first pass keeps only a stack and is
# the census of record to LEVELS_DEEP. Their per-level rows must agree on the
# levels both reach. Per-node checks -- (d) the two distances, (g) the forced
# chain, (h) the run tallies -- run in the depth-first pass on every node it
# visits (direct r on a deterministic hash sample per level).

XSMALL = 2 ** 13
DSTR_CAP = 9   # depth-distribution column lists d <= DSTR_CAP, then a tail count


def dstr(dhist):
    parts = ["%d:%d" % (dd, dhist[dd]) for dd in sorted(dhist) if dd <= DSTR_CAP]
    tail = sum(c for dd, c in dhist.items() if dd > DSTR_CAP)
    if tail:
        parts.append(">%d:%d" % (DSTR_CAP, tail))
    return " ".join(parts)


def census_bfs(levels):
    ws = [1]
    packs = [1]          # d | nd << 8   (nd = door edges on the path to the root)
    rows = []
    self_hits = 0
    for lev in range(levels + 1):
        n = len(ws)
        casc_in = door_in = 0
        dhist = {}
        maxpeak = 0
        new_ws = []
        new_packs = []
        for i in range(n):
            w = ws[i]
            p = packs[i]
            d = p & 255
            nd = p >> 8
            A = 3 ** d * w - 1
            s = v2(A)
            y = A >> s
            if A > maxpeak:
                maxpeak = A
            dhist[d] = dhist.get(d, 0) + 1
            if lev > 0:
                if s >= 3:
                    casc_in += 1
                else:
                    door_in += 1
            if lev < levels:
                N = (y << (s + 2)) + 1
                dc = v3(N)
                new_ws.append(N // 3 ** dc)
                new_packs.append(dc | (nd << 8))
                p3 = 1
                for a in range(d):
                    ya = (w << (d - a)) * p3 - 1
                    p3 *= 3
                    if ya % 3 == 0:
                        continue
                    s0 = 1 if ya % 3 == 1 else 2
                    N = (ya << s0) + 1
                    dk = v3(N)
                    wk = N // 3 ** dk
                    if dk == d and wk == w:
                        self_hits += 1
                        continue
                    new_ws.append(wk)
                    new_packs.append(dk | ((nd + 1) << 8))
        rows.append((lev, n, casc_in, door_in, dstr(dhist), maxpeak))
        ws, packs = new_ws, new_packs
    return rows, self_hits


def census_dfs(levels, sample_per_level):
    rows = [[lev, 0, 0, 0, {}, 0] for lev in range(levels + 1)]   # lev, nodes, casc_in, door_in, dhist, maxpeak
    small = {(1, 1): 0}
    k_hist = {}
    dr_hist = {}
    tal = {'s1': 0, 's2': 0, 'r_direct': 0, 'ix_holds': 0, 'g': 0, 'self': 0}
    # deterministic per-level sampling for the direct r check: a node is sampled when
    # a fixed multiplicative hash of (w,d) falls below the level's quota
    quota = []
    est = 1.0
    for lev in range(levels + 1):
        quota.append(1.0 if est <= sample_per_level else sample_per_level / est)
        est = max(est * 2.0, 2.0)
    MASK = (1 << 32) - 1
    stack = [(1, 1, 0, 0, 0)]     # w, d, lev, nd, dr
    while stack:
        w, d, lev, nd, dr = stack.pop()
        row = rows[lev]
        A = 3 ** d * w - 1
        s = v2(A)
        y = A >> s
        row[1] += 1
        if A > row[5]:
            row[5] = A
        dh = row[4]
        dh[d] = dh.get(d, 0) + 1
        if lev > 0:
            if s >= 3:
                row[2] += 1
            else:
                row[3] += 1
            k = (s - 1) // 2
            k_hist[k] = k_hist.get(k, 0) + 1
            if s <= 2:
                dr_hist[dr] = dr_hist.get(dr, 0) + 1
                if s == 1:
                    tal['s1'] += 1
                else:
                    tal['s2'] += 1
        if w <= XSMALL:
            small[(w, d)] = lev
        # (d) the two distances: r by iterating F, l = lev, on the hash sample
        h = ((w * 2654435761 + d * 40503) & MASK) / 4294967296.0
        if h < quota[lev]:
            r = f_orbit_len(w, d, 10 * lev + 100)
            check(r is not None, "F-orbit of census node %r reaches the root" % ((w, d),))
            if lev == 0:
                check(r == 0 and nd == 0, "root distances")
            else:
                check(r == nd + 1, "r = door edges + 1 at %r (r=%r, nd=%d, l=%d)" % ((w, d), r, nd, lev))
                check(lev - nd >= 1 and lev - nd == lev - r + 1, "cascade edges = l - r + 1 >= 1 at %r" % ((w, d),))
                check(lev >= r and ((lev == r) == (lev - nd == 1)), "l >= r, equality iff one cascade edge %r" % ((w, d),))
                if r == nd:
                    tal['ix_holds'] += 1
            tal['r_direct'] += 1
        # (g) 15.6.2's forced chain: depth-1 node, core = 1 mod 8, j = v2(core - 1)
        if d == 1 and w % 8 == 1 and w != 1:
            j = v2(w - 1)
            t = (j - 1) // 2
            cur = (w, 1)
            jj = j
            for step in range(t):
                Ac, sc, yc = exit_data(*cur)
                pc = comb_parent(*cur)
                check(sc == 1 and pc is not None and pc[0] == 'D', "forced door edge at s=1 from %r (j=%d)" % (cur, jj))
                check(yc % 3 == 1 and v2(yc + 1) == 1, "forced edge uses the parent's top door with m+=1 from %r" % (cur,))
                nxt = pc[1]
                check(nxt[1] == 1 and v2(nxt[0] - 1) == jj - 2, "lands on depth 1, core = 1 mod 2^%d exactly, from %r" % (jj - 2, cur))
                cur = nxt
                jj -= 2
            tal['g'] += 1
        # expansion
        if lev < levels:
            N = (y << (s + 2)) + 1
            dc = v3(N)
            stack.append((N // 3 ** dc, dc, lev + 1, nd, 0))
            p3 = 1
            for a in range(d):
                ya = (w << (d - a)) * p3 - 1
                p3 *= 3
                if ya % 3 == 0:
                    continue
                s0 = 1 if ya % 3 == 1 else 2
                N = (ya << s0) + 1
                dk = v3(N)
                wk = N // 3 ** dk
                if dk == d and wk == w:
                    tal['self'] += 1
                    continue
                stack.append((wk, dk, lev + 1, nd + 1, dr + 1))
    rows = [(r[0], r[1], r[2], r[3], dstr(r[4]), r[5]) for r in rows]
    return rows, small, k_hist, dr_hist, tal


print("--- (f) the census by peak level, no size cutoff ---")
t_census = time.time()
rows_bfs, self_bfs = census_bfs(LEVELS_BFS)
t_bfs = time.time() - t_census
t_census = time.time()
rows, census_small, k_hist, dr_hist, tal = census_dfs(LEVELS_DEEP, R_SAMPLE)
census_time = time.time() - t_census
check(rows[:LEVELS_BFS + 1] == rows_bfs, "level-by-level and depth-first passes agree on levels 0..%d" % LEVELS_BFS)
check(self_bfs == 1 and tal['self'] == 1, "the self-child exclusion fired exactly once per pass, at the root (%d, %d)" % (self_bfs, tal['self']))
check(rows[1][1] == 1, "level 1 has one node, the root's single child")
print("  level     nodes  cascade-in   door-in  depth distribution                                          largest peak")
for lev, n, ci, di, ds_, mp in rows:
    print("  %5d %9d %11d %9d  %-58s %d" % (lev, n, ci, di, ds_, mp))
total_nodes = sum(r[1] for r in rows)
print("  levels 0..%d: %d nodes; depth-first pass wall clock %.1fs (level-by-level pass to level %d: %.1fs, rows identical)"
      % (LEVELS_DEEP, total_nodes, census_time, LEVELS_BFS, t_bfs))
print("  (d) direct r on %d nodes (every node while a level has <= %d, a hash sample of about %d per level above): r = door edges + 1 throughout;"
      % (tal['r_direct'], R_SAMPLE, R_SAMPLE))
print("      the brief's (ix) as stated (r = door edges) held on %d of them" % tal['ix_holds'])
print("  (g) forced chain of 15.6.2 verified on every depth-1 census node with core = 1 mod 8: %d nodes" % tal['g'])
running("(f)/(d)/(g)")

# (h) the exploratory table
print("--- (h) exploratory: run lengths along comb paths against the 2^-j ledger ---")
tot_k = sum(k_hist.values())
tot_box = sum(k_hist_box.values())
print("  own cascade run k = floor((s-1)/2), each maximal cascade run once (its top node), all non-root census nodes (%d):" % tot_k)
print("     k       count   fraction   ledger (3/4)4^-k   box population (w<10^5, d<=30) fraction")
for k in range(0, 9):
    c = k_hist.get(k, 0)
    cb = k_hist_box.get(k, 0)
    print("    %2d %11d   %.5f      %.5f            %.5f" % (k, c, c / tot_k, 0.75 * 4.0 ** (-k), cb / tot_box))
tot_dr = sum(dr_hist.values())
tot_drb = sum(dr_hist_box.values())
print("  door run n = consecutive door edges from a door child upward, each maximal door run once (%d door children):" % tot_dr)
print("     n       count   fraction   ledger (1/4)(3/4)^(n-1)   box population (states with s<=2, forward run) fraction")
for nn in range(1, 13):
    c = dr_hist.get(nn, 0)
    cb = dr_hist_box.get(nn, 0)
    print("    %2d %11d   %.5f      %.5f                   %.5f" % (nn, c, c / tot_dr, 0.25 * 0.75 ** (nn - 1), cb / tot_drb))
door_s1, door_s2 = tal['s1'], tal['s2']
print("  door edges at s=1: %d (%.4f), at s=2: %d (%.4f); ledger 2/3 : 1/3 = 0.6667 : 0.3333; box population %.4f : %.4f"
      % (door_s1, door_s1 / (door_s1 + door_s2), door_s2, door_s2 / (door_s1 + door_s2),
         box_s1 / (box_s1 + box_s2), box_s2 / (box_s1 + box_s2)))
mean_dr = sum(nn * c for nn, c in dr_hist.items()) / tot_dr
mean_drb = sum(nn * c for nn, c in dr_hist_box.items()) / tot_drb
print("  mean door run: census %.3f, ledger 4.000, box %.3f; mean own cascade run: census %.4f, ledger 1/3 = 0.3333, box %.4f"
      % (mean_dr, mean_drb, sum(k * c for k, c in k_hist.items()) / tot_k, sum(k * c for k, c in k_hist_box.items()) / tot_box))
print("  reading: the census population carries one cascade child per node, so about half its nodes sit above their lowest sibling")
print("  and every door is counted once regardless of how often forward orbits use it; the uniform box is the ledger's own population.")
print("  Reported flat; nothing is proposed.")

# ------------------------------------ comparison with reverse.md 14.4's counts

print("--- (f) comparison with reverse.md 14.4's core-size counts ---")


def box_tree(X, early_break, scap=420):
    # the tree from (1,1) expanded in increasing core, predecessors kept when their core is <= X
    seen = {(1, 1)}
    pq = [(1, 1)]
    while pq:
        w, d = heapq.heappop(pq)
        for a, y in doors(w, d):
            if y % 3 == 0:
                continue
            s0 = lowest(y)
            s = s0
            while s <= scap:
                N = (y << s) + 1
                dd = v3(N)
                ww = N // 3 ** dd
                if early_break and ww > X and s > s0 + 6:
                    break
                if ww <= X and (ww, dd) not in seen:
                    seen.add((ww, dd))
                    heapq.heappush(pq, (ww, dd))
                s += 2
    return seen


for X, recorded, early_count in ((2 ** 10, 834, 833), (2 ** 13, 6280, 6261)):
    t_x = time.time()
    with_break = box_tree(X, True)
    full = box_tree(X, False)
    check(len(full) == recorded and len(with_break) == early_count, "14.4's count %d at w <= %d reproduced by the full scan to the branch cap (%d); the early-stop variant gives %d (%d)" % (recorded, X, len(full), early_count, len(with_break)))
    check(with_break <= full, "the early-break tree is a subset of the full box tree at w <= %d" % X)
    extra = sorted(full - with_break)
    print("  w <= %d: %d states by the full scan to the branch cap (14.4's count); %d with an early stop on the scan (first branch past s0+6 whose core exceeds X); %d states dropped by the stop: %s"
          % (X, len(full), len(with_break), len(extra), extra if len(extra) <= 3 else extra[:3] + ["..."]))
    for st in extra:
        A, s, y = exit_data(*st)
        img = F(*st)
        check(img in full and img[0] <= X, "missed state %r has its F-image %r in the box tree" % (st, img))
        check(any(yy == y for a, yy in doors(*img)) and node_on_door(y, s) == st,
              "missed state %r is a 14.1.1 predecessor of %r at branch s=%d" % (st, img, s))
    # every state of the box tree has a finite peak distance; those with l <= LEVELS_DEEP are in the census
    lvals = []
    for st in full:
        l = 0
        cur = st
        while cur != (1, 1):
            cur = comb_parent(*cur)[1]
            l += 1
        lvals.append(l)
        if l <= LEVELS_DEEP:
            check(census_small.get(st) == l, "box-tree state %r with l=%d is in the census at that level" % (st, l))
    n_in = sum(1 for l in lvals if l <= LEVELS_DEEP)
    print("  all %d states have finite l: max l = %d, mean %.2f; %d have l <= %d and all of them are census nodes at that level"
          % (len(full), max(lvals), sum(lvals) / len(lvals), n_in, LEVELS_DEEP))
    # census nodes with core <= X that are not in the box tree: their F-orbit leaves the box
    cens = [st for st in census_small if st[0] <= X]
    outside = [st for st in cens if st not in full]
    ex_shown = None
    for st in outside:
        cur = st
        left = False
        while cur != (1, 1):
            cur = F(*cur)
            if cur[0] > X:
                left = True
                if ex_shown is None:
                    ex_shown = (st, cur)
                break
        check(left, "census node %r outside the box tree has an F-iterate with core > %d" % (st, X))
    print("  census nodes with core <= %d: %d = %d in the box tree + %d whose F-orbit leaves the box (14.4 counts the box-connected tree only)"
          % (X, len(cens), len(cens) - len(outside), len(outside)))
    if ex_shown:
        print("    example: %r has F-image %r with core > %d, so 14.4's expansion never reaches it" % (ex_shown[0], ex_shown[1], X))
    print("  [%.1fs]" % (time.time() - t_x))
running("(f) comparison")

print()
print("TOTAL: checks=%d, failures=%d" % (CHECKS, FAILS))
print("census levels 0..%d: %d nodes, %d at the last level, depth-first wall clock %.1fs" % (LEVELS_DEEP, total_nodes, rows[-1][1], census_time))
print("time=%.1fs" % (time.time() - T0))
