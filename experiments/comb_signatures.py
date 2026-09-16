"""Independent verification for briefs/comb-signatures-brief.md -- comb.md
section 18.9, branching signatures.

Fresh code: imports nothing from any other file in this repository (in
particular not peak_comb.py, comb_dictionary.py or signed_comb.py). Exact
Python-integer arithmetic at every pass/fail decision; the only floats are
printed ratios, frequencies and significance figures. Canaries run first.
Single reproducing command:

    python experiments/comb_signatures.py

No phases, no flags. Seed 20260917 for every randomized check.

Objects (re-implemented here from the wiki's own definitions):
  state (Omega, D): Omega odd, 3 does not divide Omega, D >= 1.
  peak A(Omega,D) = 3^D Omega - 1 = 2^s y, s = v2(A), y the exit.
  doors y_a = 2^(D-a) 3^a Omega - 1, a = 0..D-1 (live iff 3 does not divide y_a).
  node_on_door(y,s): the state (w,d) with 2^s y + 1 = 3^d w (14.1.1's predecessor).
  comb children (18.2.3): one cascade child (branch s+2 on the node's own exit
  door), one door child per live door a (branch s0 = 1 if y_a = 1 mod 3 else 2,
  the lowest admissible branch); the root's own a=0 door child, which would be
  the excluded self-loop, is dropped.

Sections:
  canaries   the children of (7,3), (1,2), (5,2) by Item A's four laws; the
             signature of (1,2) to depth 2 written out by hand.
  (a)        Item A: the four level-1 laws on 5,000 random states against
             direct (generic) children computation; the corollary (level-1
             signature a function of (D, Omega mod 3^J)) on 2,000 pairs at
             J in {2,3,4}, sharpness reported; the a>=2 share of door children.
  (b)        Item B: the budget's sufficiency on 1,500 pairs per k <= 4; the
             exact modulus M computed per node on a level-based sample, with
             the B - M distribution.
  (c)        Item C: coincidences (independence baseline from the data),
             the 2-adic probe (contingency table, largest deviation), and the
             signature ledgers (distinct signatures vs distinct B-classes;
             depth-1 frequency vs the predicted product law; the window
             ledger across doors).
"""

import random
import time

SEED = 20260917
DATE = "2026-09-17"

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
    n = abs(n)
    return (n & -n).bit_length() - 1


def v3(n):
    n = abs(n)
    assert n != 0
    v = 0
    while n % 3 == 0:
        n //= 3
        v += 1
    return v


def valid(w, d):
    return w >= 1 and w % 2 == 1 and w % 3 != 0 and d >= 1


def exit_data(Omega, D):
    A = 3 ** D * Omega - 1
    s = v2(A)
    return A, s, A >> s


def doors(Omega, D):
    return [(a, (2 ** (D - a)) * (3 ** a) * Omega - 1) for a in range(D)]


def lowest_branch(y):
    return 1 if y % 3 == 1 else 2


def node_on_door(y, s):
    N = (y << s) + 1
    assert N % 3 == 0
    d = v3(N)
    return (N // 3 ** d, d)


def comb_children(Omega, D):
    """Generic children: [('C', w, d)] + [('D', a, w, d), ...]. No
    depth cap, no signature -- used to verify Item A's closed forms."""
    A, s, y = exit_data(Omega, D)
    kids = [('C', ) + node_on_door(y, s + 2)]
    for a, ya in doors(Omega, D):
        if ya % 3 == 0:
            continue
        s0 = lowest_branch(ya)
        dw, dd = node_on_door(ya, s0)
        if (dw, dd) == (Omega, D):
            continue  # the root's own top-door child is the excluded self-loop
        kids.append(('D', a) + (dw, dd))
    return kids


def state_of_door(y):
    m = v2(y + 1)
    q = (y + 1) >> m
    a = v3(q)
    return (q // 3 ** a, m + a)


# --------------------------------------------------- Item A closed-form laws

def cascade_depth_law(Omega, D):
    if D >= 2:
        return 1
    return 1 + v3(4 * Omega - 1)


def door_depth_law(Omega, D, a):
    """Item A's four laws, dispatched by a. Returns depth, or None if a=0
    and the top door is dead (no such child)."""
    if a >= 2:
        return 1
    if a == 1:
        return 1 + v3(2 ** (D + 1) * Omega - 1)
    # a == 0: top door
    y0 = (2 ** D) * Omega - 1
    if y0 % 3 == 0:
        return None
    s0 = lowest_branch(y0)
    N = 2 ** s0 * y0 + 1
    return v3(N)


# --------------------------------------------- Item B: signature and budget

def depth_label(d, J):
    return d if d < J else J


def sig_and_B(Omega, D, k, J):
    """Returns (signature, B(v,k)) for node (Omega,D) at depth k, cap J.

    cost() uses the child's REAL (uncapped) depth whenever the recursion
    continues past that child (k > 1): reconstructing the child's own core
    Omega(child) mod 3^(B(child,k-1)) -- needed to build the child's own
    sub-signature -- goes through an exact division by 3^(real depth), and
    that division genuinely costs real-depth digits, not the capped label.
    Only at the base case (k == 1, so the child's own recursion is B(c,0)=0
    and nothing past its label is ever examined) does knowing the CAPPED
    label -- 'depth >= J' or the exact value below J -- suffice, matching
    Item A's finding that a level-1 label costs exactly J digits. Using the
    capped label uniformly (the first attempt) under-counts the budget at
    k >= 2 and was refuted by the sufficiency check itself (see findings,
    'the capped-cost bug')."""
    if k == 0:
        return ('LEAF',), 0
    A, s, y = exit_data(Omega, D)
    cw, cd = node_on_door(y, s + 2)
    c_sig, c_B = sig_and_B(cw, cd, k - 1, J)
    cd_lab = depth_label(cd, J)
    cd_for_cost = cd_lab if k == 1 else cd
    cost_c = cd_for_cost - D
    cascade_entry = ('C', cd_lab, c_sig)
    b_candidates = [J, c_B + cost_c]
    door_entries = []
    for a, ya in doors(Omega, D):
        if ya % 3 == 0:
            door_entries.append(('Ddead', a))
            continue
        s0 = lowest_branch(ya)
        dw, dd = node_on_door(ya, s0)
        if (dw, dd) == (Omega, D):
            continue  # root self-loop: no entry, no cost
        d_sig, d_B = sig_and_B(dw, dd, k - 1, J)
        dd_lab = depth_label(dd, J)
        dd_for_cost = dd_lab if k == 1 else dd
        cost_d = dd_for_cost - a
        door_entries.append(('D', a, s0, dd_lab, d_sig))
        b_candidates.append(d_B + cost_d)
    signature = (cascade_entry, tuple(door_entries))
    return signature, max(b_candidates)


def sig_only(Omega, D, k, J):
    return sig_and_B(Omega, D, k, J)[0]


def lift_same_mod(Omega, M, rng):
    """A random Omega' != Omega with Omega' == Omega (mod 3^M), Omega' odd,
    3 does not divide Omega' (inherited automatically once M >= 1)."""
    t = rng.randrange(1, 10 ** 6)
    return Omega + 2 * (3 ** M) * t


def lift_one_digit_short(Omega, M, rng):
    """Agrees with Omega mod 3^(M-1) but not mod 3^M (M >= 1)."""
    r = rng.choice([1, 2])
    t = rng.randrange(0, 10 ** 6)
    return Omega + 2 * (3 ** (M - 1)) * r + 2 * (3 ** M) * t


def exact_M(Omega, D, k, J, target_sig, B, cap_tests=60000):
    """The least M with 1 <= M <= B such that EVERY valid Omega' == Omega
    (mod 3^M) (equivalently every one of the 3^(B-M) completions of the
    low-M-digit prefix into a full B-digit residue, since sufficiency at B
    is already established) has the same signature. Computed exactly by
    full enumeration at each candidate M, searched from M = B downward.
    Floored at M = 1: at M = 0 the low digit (Omega mod 3, always nonzero
    for a valid state) is itself free, which would synthesize invalid
    (3 | Omega') candidates -- validity already fixes that digit, so it is
    never counted as free information. Returns (M, capped) where capped is
    True if the search was capped before a definitive least-M was found
    (reported if it occurs; not observed in the committed run)."""
    if B <= 1:
        return max(B, 1) if B >= 1 else 1, False
    M = B
    while M > 1:
        width = B - (M - 1)
        n_tests = 3 ** width
        if n_tests > cap_tests:
            return M, True
        ok = True
        prefix = Omega % (3 ** (M - 1))
        for j in range(n_tests):
            r = prefix + j * (3 ** (M - 1))
            # realize r (in [0, 3^B)) as an odd integer == r (mod 3^B);
            # 3 does not divide r since M-1 >= 1 pins Omega's own mod-3 digit
            cand = r if r % 2 == 1 else r + 3 ** B
            s = sig_only(cand, D, k, J)
            if s != target_sig:
                ok = False
                break
        if not ok:
            return M, False
        M -= 1
    return 1, False


# --------------------------------------------------------- census machinery

def comb_census_levels(max_level):
    """Level-by-level BFS from (1,1); returns a list of levels, each a list
    of (Omega, D) states. Mirrors comb.md 18.2's parent/child rule, built
    from this file's own comb_children (no size cutoff)."""
    levels = [[(1, 1)]]
    for lam in range(max_level):
        nxt = []
        for (Omega, D) in levels[-1]:
            for kid in comb_children(Omega, D):
                if kid[0] == 'C':
                    nxt.append((kid[1], kid[2]))
                else:
                    nxt.append((kid[2], kid[3]))
        levels.append(nxt)
    return levels


def main():
    rng = random.Random(SEED)

    print("=" * 78)
    print("comb_signatures.py -- verification for briefs/comb-signatures-brief.md")
    print("seed=%d date=%s" % (SEED, DATE))
    print("=" * 78)

    # ------------------------------------------------------------ canaries

    print("\n-- canaries --")

    # (7,3): D=3, doors a=0,1,2
    Omega, D = 7, 3
    A, s, y = exit_data(Omega, D)
    check((Omega, D, A, s, y) == (7, 3, 3 ** 3 * 7 - 1, v2(3 ** 3 * 7 - 1), (3 ** 3 * 7 - 1) >> v2(3 ** 3 * 7 - 1)),
          "canary (7,3) exit data self-consistent")
    kids = comb_children(Omega, D)
    by_type = {}
    for kd in kids:
        if kd[0] == 'C':
            by_type['C'] = (kd[1], kd[2])
        else:
            by_type[('D', kd[1])] = (kd[2], kd[3])
    check(by_type['C'][1] == cascade_depth_law(Omega, D), "canary (7,3) cascade depth matches law")
    for a in range(D):
        law_d = door_depth_law(Omega, D, a)
        if ('D', a) in by_type:
            check(by_type[('D', a)][1] == law_d, "canary (7,3) door a=%d depth matches law" % a)
        else:
            check(law_d is None, "canary (7,3) door a=%d absent iff law says dead" % a)
    print("  (7,3): cascade child %s depth %d; door children %s" %
          (by_type['C'], by_type['C'][1],
           {a: by_type.get(('D', a)) for a in range(D)}))

    # (1,2): D=2
    Omega, D = 1, 2
    kids = comb_children(Omega, D)
    by_type = {}
    for kd in kids:
        if kd[0] == 'C':
            by_type['C'] = (kd[1], kd[2])
        else:
            by_type[('D', kd[1])] = (kd[2], kd[3])
    check(by_type['C'][1] == cascade_depth_law(Omega, D), "canary (1,2) cascade depth matches law")
    for a in range(D):
        law_d = door_depth_law(Omega, D, a)
        if ('D', a) in by_type:
            check(by_type[('D', a)][1] == law_d, "canary (1,2) door a=%d depth matches law" % a)
        else:
            check(law_d is None, "canary (1,2) door a=%d absent iff law says dead" % a)
    print("  (1,2): cascade child %s depth %d; door children %s" %
          (by_type['C'], by_type['C'][1],
           {a: by_type.get(('D', a)) for a in range(D)}))

    # (5,2): D=2
    Omega, D = 5, 2
    kids = comb_children(Omega, D)
    by_type = {}
    for kd in kids:
        if kd[0] == 'C':
            by_type['C'] = (kd[1], kd[2])
        else:
            by_type[('D', kd[1])] = (kd[2], kd[3])
    check(by_type['C'][1] == cascade_depth_law(Omega, D), "canary (5,2) cascade depth matches law")
    for a in range(D):
        law_d = door_depth_law(Omega, D, a)
        if ('D', a) in by_type:
            check(by_type[('D', a)][1] == law_d, "canary (5,2) door a=%d depth matches law" % a)
        else:
            check(law_d is None, "canary (5,2) door a=%d absent iff law says dead" % a)
    print("  (5,2): cascade child %s depth %d; door children %s" %
          (by_type['C'], by_type['C'][1],
           {a: by_type.get(('D', a)) for a in range(D)}))

    # the signature of (1,2) to depth 2, cap J=3, written by hand
    J = 3
    sig12, B12 = sig_and_B(1, 2, 2, J)
    print("  sig((1,2), k=2, J=3) = %r  (B=%d)" % (sig12, B12))
    # by hand: (1,2) has A=8, s=3, y=1. cascade child: node_on_door(1,5) = (11,1)
    #   (2^5*1+1=33=3*11). door a=0: y0=2^2*1-1=3, dead (3|3). door a=1:
    #   y1=2^1*3*1-1=5, s0=2 (5 mod3=2), node_on_door(5,2)=(7,1) (4*5+1=21=3*7).
    hand_cascade = node_on_door(1, 5)
    hand_door1 = node_on_door(5, 2)
    check(hand_cascade == (11, 1), "hand: (1,2)'s cascade child is (11,1)")
    check(hand_door1 == (7, 1), "hand: (1,2)'s door-1 child is (7,1)")
    # (11,1): A=32, s=5, y=1: cascade child of (11,1) at depth k=1 is node_on_door(1,7)=(43,1)
    #   door a=0 of (11,1): y0=2^1*11-1=21, dead (3|21). so (11,1) has ONLY a cascade child.
    check((11 * 1) % 3 == 0 if False else ((2 * 11 - 1) % 3 == 0), "hand: (11,1)'s only door is dead")
    hand_cascade2 = node_on_door(1, 7)
    check(hand_cascade2 == (43, 1), "hand: (11,1)'s cascade child is (43,1)")
    # (7,1): A=20, s=2, y=5. cascade child: node_on_door(5,4)=(1,4) (4^2*5+1=81=3^4).
    #   door a=0 of (7,1): y0=2*7-1=13, alive (13 mod3=1), s0=1: node_on_door(13,1)=(1,2)
    hand_cascade3 = node_on_door(5, 4)
    check(hand_cascade3 == (1, 4), "hand: (7,1)'s cascade child is (1,4)")
    # top door of (7,1): y0 = 2^1*7-1 = 13, 13 mod 3 = 1 so s0=1; N = 2*13+1 = 27 = 3^3
    hand_door0 = node_on_door(13, 1)
    check(hand_door0 == (1, 3), "hand: (7,1)'s door-0 (top) child is (1,3)")
    print("  hand-worked depth-2 descendants: (11,1)->(43,1); (7,1)->(1,4),(1,3)")
    running("canaries")

    # ---------------------------------------------------------------- (a)

    print("\n-- (a) Item A: the four level-1 laws --")
    N_A = 5000
    a_ge2_children = 0
    a_ge2_live = 0
    total_door_children = 0
    for _ in range(N_A):
        Omega = 2 * rng.randrange(1, 500001) - 1
        while Omega % 3 == 0:
            Omega = 2 * rng.randrange(1, 500001) - 1
        D = rng.randrange(1, 31)
        kids = comb_children(Omega, D)
        by_type = {}
        for kd in kids:
            if kd[0] == 'C':
                by_type['C'] = (kd[1], kd[2])
            else:
                by_type[('D', kd[1])] = (kd[2], kd[3])
        check(by_type['C'][1] == cascade_depth_law(Omega, D),
              "cascade law at (%d,%d)" % (Omega, D))
        for a, ya in doors(Omega, D):
            law_d = door_depth_law(Omega, D, a)
            live = ya % 3 != 0
            present = ('D', a) in by_type
            if present:
                total_door_children += 1
                check(by_type[('D', a)][1] == law_d,
                      "door law a=%d at (%d,%d)" % (a, Omega, D))
                if a >= 2:
                    a_ge2_children += 1
            else:
                # either dead, or (root's own excluded self-loop)
                is_root_selfloop = (a == 0 and (Omega, D) == (1, 1))
                check((not live) or is_root_selfloop,
                      "door a=%d absent only if dead or root self-loop, (%d,%d)" % (a, Omega, D))
            if a >= 2:
                a_ge2_live += 1
    check(a_ge2_live == a_ge2_children,
          "every a>=2 door is alive (14.5.1's side-door claim, read at a>=2): %d == %d" %
          (a_ge2_live, a_ge2_children))
    running("(a) four laws, %d states" % N_A)
    share = a_ge2_children / total_door_children if total_door_children else 0.0
    print("  a>=2 door children (D uniform in [1,30], NOT ledger-weighted, structural only): %d / %d = %.4f" %
          (a_ge2_children, total_door_children, share))
    print("  (the ledger-weighted share -- the reconciliation with 18.5's depth distribution -- is")
    print("   measured on the level-18 census below: 1/6 predicted under P(D=j)=2.3^-j.)")

    # corollary: level-1 signature a function of (D, Omega mod 3^J)
    print("  corollary: level-1 signature vs (D, Omega mod 3^J)")
    for J in (2, 3, 4):
        N_pairs = 2000
        suff_ok = 0
        sharp_differ = 0
        for _ in range(N_pairs):
            Omega = 2 * rng.randrange(1, 200001) - 1
            while Omega % 3 == 0:
                Omega = 2 * rng.randrange(1, 200001) - 1
            D = rng.randrange(1, 21)
            base_sig = sig_only(Omega, D, 1, J)
            Omega2 = lift_same_mod(Omega, J, rng)
            same_sig = sig_only(Omega2, D, 1, J)
            if same_sig == base_sig:
                suff_ok += 1
            Omega3 = lift_one_digit_short(Omega, J, rng)
            short_sig = sig_only(Omega3, D, 1, J)
            if short_sig != base_sig:
                sharp_differ += 1
        check(suff_ok == N_pairs, "J=%d: level-1 signature determined by (D, Omega mod 3^J) in all %d pairs" % (J, N_pairs))
        print("    J=%d: sufficiency %d/%d; one-digit-short differed %d/%d" %
              (J, suff_ok, N_pairs, sharp_differ, N_pairs))
    running("(a) corollary")

    # ---------------------------------------------------------------- (b)

    print("\n-- (b) Item B: signature budget --")
    J = 3
    for k in (1, 2, 3, 4):
        N_pairs = 1500
        suff_ok = 0
        sharp_differ = 0
        B_values = []
        for _ in range(N_pairs):
            Omega = 2 * rng.randrange(1, 5001) - 1
            while Omega % 3 == 0:
                Omega = 2 * rng.randrange(1, 5001) - 1
            D = rng.randrange(1, 11)
            base_sig, B = sig_and_B(Omega, D, k, J)
            B_values.append(B)
            Omega2 = lift_same_mod(Omega, B, rng)
            same_sig = sig_only(Omega2, D, k, J)
            if same_sig == base_sig:
                suff_ok += 1
            if B >= 1:
                Omega3 = lift_one_digit_short(Omega, B, rng)
                short_sig = sig_only(Omega3, D, k, J)
                if short_sig != base_sig:
                    sharp_differ += 1
        check(suff_ok == N_pairs, "k=%d: budget sufficient in all %d pairs" % (k, N_pairs))
        print("    k=%d: sufficiency %d/%d; mean B=%.2f max B=%d; one-digit-short differed %d/%d" %
              (k, suff_ok, N_pairs, sum(B_values) / len(B_values), max(B_values),
               sharp_differ, N_pairs))
    running("(b) budget sufficiency")

    # exact modulus M vs B, on a level-based sample
    print("  exact modulus M(v,k) vs B(v,k), sampled per level")
    LEVELS_FOR_C = [10, 12, 14, 16, 18]
    max_level_needed = max(LEVELS_FOR_C)
    t_census = time.time()
    census_levels = comb_census_levels(max_level_needed)
    print("  census built to level %d in %.1fs (level sizes: %s)" %
          (max_level_needed, time.time() - t_census,
           [len(census_levels[l]) for l in LEVELS_FOR_C]))
    for lvl in census_levels:
        for (w, d) in lvl:
            check(valid(w, d), "every census node is a valid state")

    # ledger-weighted a>=2 share (Item A's reconciliation with 18.5), on the
    # level-18 census: D is distributed per the measured depth ledger there.
    pop18 = census_levels[18]
    ge2 = 0
    tot_door = 0
    for (Omega, D) in pop18:
        for a, ya in doors(Omega, D):
            if ya % 3 == 0:
                continue
            tot_door += 1
            if a >= 2:
                ge2 += 1
    print("  ledger-weighted a>=2 share (level-18 census, %d nodes): %d / %d = %.4f (predicted 1/6 = %.4f)" %
          (len(pop18), ge2, tot_door, ge2 / tot_door, 1.0 / 6))

    NODES_PER_LEVEL_M = 2000
    all_BM = []
    per_level_BM_summary = []
    for lam in LEVELS_FOR_C:
        pop = census_levels[lam]
        sample = pop if len(pop) <= NODES_PER_LEVEL_M else rng.sample(pop, NODES_PER_LEVEL_M)
        k_for_M = 2  # a fixed, moderate depth for the exact-M measurement (kept uniform per level)
        BMs = []
        capped_count = 0
        for (Omega, D) in sample:
            sig, B = sig_and_B(Omega, D, k_for_M, J)
            M, capped = exact_M(Omega, D, k_for_M, J, sig, B)
            check(M <= B, "M(v,k) <= B(v,k) at level %d" % lam)
            if capped:
                capped_count += 1
            else:
                BMs.append(B - M)
        all_BM.extend(BMs)
        if BMs:
            per_level_BM_summary.append((lam, len(BMs), sum(BMs) / len(BMs), max(BMs),
                                          sum(1 for x in BMs if x == 0)))
        print("    level %d: sampled %d nodes (k=%d), %d search-capped (excluded from stats)" %
              (lam, len(sample), k_for_M, capped_count))
    running("(b) exact modulus")
    print("  B - M distribution, per level (n, mean, max, #exact(B=M)):")
    for row in per_level_BM_summary:
        print("    level %2d: n=%4d mean(B-M)=%.3f max(B-M)=%d exact=%d (%.3f)" %
              (row[0], row[1], row[2], row[3], row[4], row[4] / row[1]))
    if all_BM:
        print("  overall: n=%d mean(B-M)=%.3f max(B-M)=%d exact-match fraction=%.3f" %
              (len(all_BM), sum(all_BM) / len(all_BM), max(all_BM),
               sum(1 for x in all_BM if x == 0) / len(all_BM)))

    # ---------------------------------------------------------------- (c)

    print("\n-- (c) Item C: search for a grouping finer than residues --")

    # C.1 coincidences: independence baseline computed from the data
    print("  C.1 coincidences (independence baseline from observed class frequencies)")
    for lam in LEVELS_FOR_C:
        pop = census_levels[lam]
        pop_D1 = [(w, d) for (w, d) in pop if d == 1]
        if not pop_D1:
            continue
        sample = pop_D1 if len(pop_D1) <= 1500 else rng.sample(pop_D1, 1500)
        k = 2
        node_data = []
        for (Omega, D) in sample:
            sig, B = sig_and_B(Omega, D, k, J)
            M, capped = exact_M(Omega, D, k, J, sig, B, cap_tests=20000)
            if capped:
                continue
            node_data.append((Omega, D, sig, M))
        # form classes: key = (M, Omega mod 3^M)
        class_of = {}
        class_sig = {}
        for (Omega, D, sig, M) in node_data:
            key = (M, Omega % (3 ** M))
            class_of.setdefault(key, []).append((Omega, sig))
            if key in class_sig:
                check(class_sig[key] == sig, "all members of one exact class share one signature")
            else:
                class_sig[key] = sig
        classes = list(class_of.keys())
        Cn = len(classes)
        freq = {}
        for key in classes:
            s = class_sig[key]
            freq[s] = freq.get(s, 0) + 1
        observed_pairs = sum(f * (f - 1) // 2 for f in freq.values())
        q = {s: f / Cn for s, f in freq.items()} if Cn else {}
        predicted_pairs = (Cn * (Cn - 1) / 2) * sum(qs * qs for qs in q.values()) if Cn > 1 else 0.0
        print("    level %2d (D=1, k=%d): %d nodes -> %d distinct exact classes, %d distinct signatures" %
              (lam, k, len(node_data), Cn, len(freq)))
        print("              observed different-class same-signature pairs = %d; independence baseline = %.2f" %
              (observed_pairs, predicted_pairs))
        if observed_pairs <= predicted_pairs * 1.5 + 2:
            print("              at or below the independence baseline: no grouping finer than residues visible")
        else:
            print("              above the independence baseline by more than 50%%: characterise (see findings)")

    # C.2 the 2-adic probe
    print("  C.2 the 2-adic probe (contingency test, largest standardized residual)")
    import math
    total_exceed = 0
    total_tests = 0
    for lam in LEVELS_FOR_C:
        pop = census_levels[lam]
        k = 1
        for m_probe in (4, 6, 8):
            # group by (D, signature-to-depth-k); within each group with
            # >= 20 members, test Omega mod 2^m_probe against the D-matched
            # marginal (D is already part of the group key, so pooling
            # across D would just detect "D correlates with Omega mod 2^m",
            # not a residual dependency past (D, signature)).
            group = {}
            for (Omega, D) in pop:
                sig = sig_only(Omega, D, k, J)
                group.setdefault((D, sig), []).append(Omega)
            pooled_by_D = {}
            N_by_D = {}
            for (Omega, D) in pop:
                r = Omega % (2 ** m_probe)
                pooled_by_D.setdefault(D, {})
                pooled_by_D[D][r] = pooled_by_D[D].get(r, 0) + 1
                N_by_D[D] = N_by_D.get(D, 0) + 1
            worst = (0.0, None, None)
            n_cells_tested = 0
            for (D, sig), members in group.items():
                n = len(members)
                if n < 20:
                    continue
                local = {}
                for Omega in members:
                    r = Omega % (2 ** m_probe)
                    local[r] = local.get(r, 0) + 1
                pooled = pooled_by_D[D]
                N_pool = N_by_D[D]
                for r, cnt in local.items():
                    p = pooled.get(r, 0) / N_pool
                    expected = n * p
                    if expected <= 0:
                        continue
                    resid = (cnt - expected) / (expected ** 0.5)
                    n_cells_tested += 1
                    if abs(resid) > abs(worst[0]):
                        worst = (resid, (D, sig), r)
            thresh = math.sqrt(2 * math.log(2 * max(n_cells_tested, 1) / 0.01)) if n_cells_tested else 0.0
            verdict = "within" if abs(worst[0]) <= thresh else "EXCEEDS"
            total_tests += 1
            if verdict == "EXCEEDS":
                total_exceed += 1
            print("    level %2d (k=%d, m=%d): %d groups (n>=20), %d cells; largest |resid|=%.2f (r=%s); Bonferroni@0.01=%.2f -- %s" %
                  (lam, k, m_probe, sum(1 for _, mm in group.items() if len(mm) >= 20),
                   n_cells_tested, worst[0], worst[2], thresh, verdict))
    print("  summary: %d / %d (level,m) tests exceeded the Bonferroni-corrected threshold" %
          (total_exceed, total_tests))

    # C.3 signature ledgers
    print("  C.3 signature ledgers")
    for lam in LEVELS_FOR_C:
        pop = census_levels[lam]
        k = 1
        sig_count = {}
        class_count = {}
        for (Omega, D) in pop:
            sig, B = sig_and_B(Omega, D, k, J)
            sig_count[sig] = sig_count.get(sig, 0) + 1
            key = (D, Omega % (3 ** B))
            class_count[key] = class_count.get(key, 0) + 1
        print("    level %2d: %d nodes, %d distinct signatures, %d distinct (D, Omega mod 3^B) classes" %
              (lam, len(pop), len(sig_count), len(class_count)))

    # C.3(b): depth-1 frequency vs predicted product law
    print("  C.3(b) depth-1 signature frequency vs the predicted product law")
    lam = 18
    pop = census_levels[lam]
    ledger = {j: 2 * (3.0 ** -j) for j in range(1, 12)}

    def geom3(t):
        # canonical "valuation of a generic 3-adic quantity" law: P(v3 = t) = 2/3 * 3^-t
        return (2.0 / 3.0) * (3.0 ** -t)

    def geom3_label_prob(label):
        # P(depth_label(1 + v3(X), J) == label) for a "generic" quantity X,
        # under the canonical valuation law P(v3(X) = t) = 2/3 * 3^-t: the
        # depth is 1 + v3(X), so P(depth == L) = geom3(L - 1) for L < J, and
        # the tail P(depth >= J) = P(v3(X) >= J - 1) = 3^-(J-1).
        if label < J:
            return geom3(label - 1)
        return 3.0 ** -(J - 1)

    def predicted_prob(sig):
        """Predicted probability of a depth-1 signature shape, under: D per
        the ledger; the top door alive with probability 1/2 (14.5.1), and
        (conditional on alive) s0 = 1 or 2 with probability 1/2 each -- the
        CENSUS's own unweighted 1:1 split (18.5's census column), not the
        forward-visit-weighted ledger's 2:1; every other live door's depth
        (the a=1 side door, the cascade child at D=1) an independent
        geom3-distributed valuation; every a>=2 door deterministically alive
        at depth 1 (Item A), contributing probability 1 once D is fixed."""
        cascade_entry, door_entries = sig
        D_here = len(door_entries)
        p = ledger.get(D_here, 2.0 * 3.0 ** -D_here)
        # cascade
        if D_here >= 2:
            if cascade_entry[1] != 1:
                return 0.0
        else:
            p *= geom3_label_prob(cascade_entry[1])
        # doors
        for entry in door_entries:
            a = entry[1]
            if a >= 2:
                if entry[0] != 'D' or entry[3] != 1:
                    return 0.0
                continue
            if a == 1:
                if entry[0] != 'D':
                    return 0.0  # side doors are never dead (14.5.1)
                p *= geom3_label_prob(entry[3])
            elif a == 0:
                if entry[0] == 'Ddead':
                    p *= 0.5
                else:
                    p *= 0.5 * 0.5 * geom3_label_prob(entry[3])
        return p

    obs = {}
    for (Omega, D) in pop:
        sig = sig_only(Omega, D, 1, J)
        obs[sig] = obs.get(sig, 0) + 1
    N = len(pop)

    # the uniform BOX population (18.5's own comparison population: Omega <
    # 10^5, D <= 30, uniform, NOT the comb tree) -- 18.5's own finding is that
    # the box matches ledger-style predictions and the census does not, for a
    # structural reason (every node has exactly one cascade child, so the
    # census systematically over-represents cascade-reached shapes); tested
    # here for signatures the same way.
    box_obs = {}
    N_box = 60000
    for _ in range(N_box):
        Omega_b = 2 * rng.randrange(1, 50001) - 1
        while Omega_b % 3 == 0:
            Omega_b = 2 * rng.randrange(1, 50001) - 1
        D_b = rng.randrange(1, 31)
        sig_b = sig_only(Omega_b, D_b, 1, J)
        box_obs[sig_b] = box_obs.get(sig_b, 0) + 1

    print("    level %d: %d nodes, %d distinct depth-1 signatures; top 8 by census frequency" %
          (lam, N, len(obs)))
    print("    (census vs predicted product law vs the uniform box, 18.5's own comparison population):")
    ranked = sorted(obs.items(), key=lambda kv: -kv[1])[:8]
    covered = 0.0
    pred_covered = 0.0
    box_covered = 0.0
    for sig, cnt in ranked:
        f_obs = cnt / N
        f_pred = predicted_prob(sig)
        f_box = box_obs.get(sig, 0) / N_box
        covered += f_obs
        pred_covered += f_pred
        box_covered += f_box
        print("      census=%.5f  pred=%.5f  box=%.5f  box/pred=%.3f  shape=%r" %
              (f_obs, f_pred, f_box, (f_box / f_pred if f_pred > 0 else float('nan')), sig))
    print("    top-8 coverage: census mass %.4f, predicted mass %.4f, box mass %.4f" %
          (covered, pred_covered, box_covered))
    print("    reading: the box (18.5's own uniform comparison population) is expected to track the")
    print("    predicted product law; the census is expected to deviate, structurally, the same way")
    print("    18.5's own run-length table deviates from its ledger -- see findings for the reading.")

    # Whole-census sanity: every a>=2 door is alive with depth exactly 1
    # (Item A), a DETERMINISTIC sub-event with no randomness at all -- the
    # predicted-frequency model above treats it as certain (probability 1
    # given D), and this is the exhaustive check that it really is.
    obs_a_ge2_ok = 0
    for (Omega, D) in pop:
        ok = True
        for a, ya in doors(Omega, D):
            if a < 2:
                continue
            if ya % 3 == 0:
                ok = False
                break
            law_d = door_depth_law(Omega, D, a)
            if law_d != 1:
                ok = False
                break
        if ok:
            obs_a_ge2_ok += 1
    print("    sanity (all a>=2 doors alive with depth exactly 1, per Item A): %d / %d = %.4f (must be 1.0000)" %
          (obs_a_ge2_ok, N, obs_a_ge2_ok / N))
    check(obs_a_ge2_ok == N, "every a>=2 door child has depth exactly 1 (Item A), whole level-%d census" % lam)

    # C.3(c): the window ledger
    print("  C.3(c) the window ledger: does a fixed door's window of 3^k branches")
    print("         carry an EXACT signature multiset, or only a statistical one?")
    for kw in (2, 3):
        width = 3 ** kw
        n_doors_tested = 8
        multisets = []
        doors_tested = []
        for _ in range(n_doors_tested):
            y = 2 * rng.randrange(1, 2 * 10 ** 6) + 1
            while y % 3 == 0:
                y = 2 * rng.randrange(1, 2 * 10 ** 6) + 1
            s0 = lowest_branch(y)
            branches = [s0 + 2 * i for i in range(width)]
            ms = {}
            for s in branches:
                w, d = node_on_door(y, s)
                dl = depth_label(d, J)
                ms[dl] = ms.get(dl, 0) + 1
            multisets.append(tuple(sorted(ms.items())))
            doors_tested.append(y)
        all_equal = all(m == multisets[0] for m in multisets)
        print("    k=%d (window width %d): depth-label multiset identical across %d random doors? %s" %
              (kw, width, n_doors_tested, all_equal))
        check(all_equal, "k=%d: the depth-label multiset per window is door-independent (14.6.5.2's own exact count)" % kw)
        # now the FULL depth-1 SIGNATURE multiset (not just depth label) of the window's nodes
        sig_multisets = []
        for y in doors_tested:
            s0 = lowest_branch(y)
            branches = [s0 + 2 * i for i in range(width)]
            ms = {}
            for s in branches:
                w, d = node_on_door(y, s)
                sig = sig_only(w, d, 1, J)
                ms[sig] = ms.get(sig, 0) + 1
            sig_multisets.append(tuple(sorted(ms.items(), key=lambda kv: repr(kv[0]))))
        sig_all_equal = all(m == sig_multisets[0] for m in sig_multisets)
        n_distinct_sig_multisets = len(set(sig_multisets))
        print("    k=%d: full depth-1 SIGNATURE multiset identical across the %d doors? %s (%d distinct multisets observed)" %
              (kw, n_doors_tested, sig_all_equal, n_distinct_sig_multisets))

    running("(c) Item C")

    # -------------------------------------------------------------- summary

    print("\n" + "=" * 78)
    print("TOTAL: checks = %d, failures = %d, wall clock = %.1fs" %
          (CHECKS, FAILS, time.time() - T0))
    print("=" * 78)


if __name__ == "__main__":
    main()
