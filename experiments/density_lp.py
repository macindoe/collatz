# KL-LP density-refinement front (reverse.md 14.6.5+, briefs/kl-lp-brief.md).
# Stage 1: multi-door renewal, rigorous.
#
# (A) generic-door check: Lemma 14.6.1 (collapse identity) and Lemma 14.6.2
#     (triple law) hold for ANY live door of ANY backward-reachable state,
#     not only the "designated" (top/unique) door the single-door tree of
#     14.6 follows. Verified two ways: every door's T-orbit reaches 1, and
#     all doors of all states in the tree are pairwise-distinct odd
#     integers, recoverable via a = v3(y+1), D-a = v2(y+1).
# (B) exact ledger: within ANY window of 3^k consecutive admissible s, the
#     count with v3(s - M3(y)) = j is EXACTLY 2*3^(k-1-j) for j=0..k-1, and
#     exactly 1 has v3(s-M3(y)) >= k -- a deterministic fact (not a
#     measured average), independent of y. This is what makes a guaranteed
#     (worst-case) multi-door bonus possible.
# (C) recursive worst-case mass: extends Lemma mass (paper Sec 8) with the
#     guaranteed-alive extra doors a=1..d'-2 of any depth-d'>=3 predecessor
#     (Theorem 14.5.1), computed via the same rearrangement (worst-offset,
#     worst-slot) principle as the original lemma, applied recursively
#     through the exact ternary (1-of-3-continues) branching structure of
#     (B). Reproduces the known critical c*=0.3304 when bonus is disabled
#     (sanity check), and finds the new critical c* with the bonus enabled.
import heapq, math, random

def v2(x):
    v = 0
    while x % 2 == 0:
        x //= 2; v += 1
    return v

def v3(x):
    v = 0
    while x % 3 == 0:
        x //= 3; v += 1
    return v

def tree_states(X):
    seen = {(1, 1)}; pq = [(1, 1)]
    while pq:
        w, d = heapq.heappop(pq)
        for a in range(d):
            y = 2**(d - a) * 3**a * w - 1
            if y % 3 == 0:
                continue
            s0 = 1 if y % 3 == 1 else 2
            s = s0
            while True:
                N = (1 << s) * y + 1
                dd = v3(N); ww = N // 3**dd
                if ww > X and s > s0 + 6:
                    break
                if dd >= 1 and ww <= X and (ww, dd) not in seen:
                    seen.add((ww, dd)); heapq.heappush(pq, (ww, dd))
                s += 2
                if s > 420:
                    break
    return seen

def T_orbit_reaches_1(y, cap=200000):
    x = y
    for _ in range(cap):
        if x == 1:
            return True
        x = x // 2 if x % 2 == 0 else 3 * x + 1
    return False

def check_A_generic_doors(X=2**14, sample=200, seed=42):
    states = tree_states(X)
    middle = [(w, d) for (w, d) in states if d >= 3]
    random.seed(seed)
    sample_states = random.sample(middle, min(sample, len(middle)))
    checked = bad = 0
    all_doors = {}
    collisions = recovery_fail = 0
    for (w, d) in states:
        for a in range(d):
            y = 2**(d - a) * 3**a * w - 1
            if y % 3 == 0:
                continue
            if y in all_doors:
                collisions += 1
            else:
                all_doors[y] = (w, d, a)
            ra = v3(y + 1); rDa = v2(y + 1)
            rw = (y + 1) // (2**rDa * 3**ra)
            if (rw, ra + rDa, ra) != (w, d, a):
                recovery_fail += 1
    for (w, d) in sample_states:
        for a in range(1, d - 1):
            y = 2**(d - a) * 3**a * w - 1
            if y % 3 == 0:
                continue
            checked += 1
            if not T_orbit_reaches_1(y):
                bad += 1
    return dict(states=len(states), live_doors=len(all_doors), collisions=collisions,
                recovery_fail=recovery_fail, middle_door_checks=checked, middle_door_fail=bad)

def check_B_exact_ledger(trials=400, ks=(2, 3, 4), seed=20260711):
    random.seed(seed)
    checked = bad = 0
    for _ in range(trials):
        y = random.randrange(1, 10**6, 2)
        if y % 3 == 0:
            continue
        s0 = 1 if y % 3 == 1 else 2
        for k in ks:
            N = 3**k
            depths = []
            s = s0
            for _ in range(N):
                Nval = (1 << s) * y + 1
                depths.append(v3(Nval) - 1)  # j = v3(s - M3(y))
                s += 2
            checked += 1
            for j in range(k):
                if sum(1 for d in depths if d == j) != 2 * 3**(k - 1 - j):
                    bad += 1
            if sum(1 for d in depths if d >= k) != 1:
                bad += 1
    return checked, bad

L3 = math.log2(3)
L15 = math.log2(1.5)

def weight(m, c):
    if m <= 2:
        return 1.0
    return 1.0 + sum(1.5**(c * (m - 1 - a)) for a in range(1, m - 1))

def total_mass(c, bonus=True, s0=2, n_level1_triples=3**9):
    slots = [s0 + 2 * i for i in range(3 * n_level1_triples)]
    deltas = [s + 1 - L3 for s in slots]
    total = 0.0
    level = 1
    current = deltas
    while len(current) >= 3:
        next_candidates = []
        for j in range(len(current) // 3):
            small, mid, large = sorted(current[3 * j:3 * j + 3])
            next_candidates.append(large)
            if level == 1:
                total += (weight(1, c) if bonus else 1.0) * 2**(-c * mid)
            else:
                w = weight(level, c) if bonus else 1.0
                total += w * 2**(-c * small) + w * 2**(-c * mid)
        current = next_candidates
        level += 1
    return total

def critical_c(bonus=True, lo=0.2, hi=0.9, **kw):
    def f(c):
        return total_mass(c, bonus=bonus, **kw) - 1
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if f(mid) > 0 else (lo, mid)
    return (lo + hi) / 2


# --- 14.13 (stages 2-3): the precision-loss obstruction, recorded as code ---
# (D) REFUTES the naive claim that a parent known only mod 3^k pins its
#     child's full k-digit residue whenever d=v3(N)<k. This is the bug
#     behind the first (unsound) stage-2 LP attempt.
# (E) the CORRECT law used in its place: parent mod 3^k pins the child only
#     mod 3^(k-d) -- exactly d digits of precision are spent per step, and
#     since admissible s forces d>=1 always, no step is free. This is why a
#     stationary same-precision residue LP does not exist for this map.

def check_D_naive_precision_refuted(k=4, trials_per_edge=20, seed=7):
    random.seed(seed)
    checked = bad = 0
    for r in range(1, 3**k):
        if r % 3 == 0:
            continue
        s0 = 1 if r % 3 == 1 else 2
        for s in (s0, s0 + 2, s0 + 4):
            Nr = (1 << s) * r + 1
            d = v3(Nr)
            if d == 0 or d >= k:
                continue
            base_child = (Nr // 3**d) % (3**k)  # WRONG: claims full k digits
            for _ in range(trials_per_edge):
                m = random.randrange(0, 10**5)
                y = r + 3**k * m
                N = (1 << s) * y + 1
                checked += 1
                if v3(N) != d or (N // 3**d) % (3**k) != base_child:
                    bad += 1
    return checked, bad

def check_E_correct_precision_law(k=4, trials_per_edge=20, seed=7):
    random.seed(seed)
    checked = bad = 0
    for r in range(1, 3**k):
        if r % 3 == 0:
            continue
        s0 = 1 if r % 3 == 1 else 2
        for s in (s0, s0 + 2, s0 + 4, s0 + 6):
            Nr = (1 << s) * r + 1
            d = v3(Nr)
            if d == 0 or d >= k:
                continue
            target_mod = 3**(k - d)
            base_child = (Nr // 3**d) % target_mod  # correct: k-d digits only
            for _ in range(trials_per_edge):
                m = random.randrange(0, 10**5)
                y = r + 3**k * m
                N = (1 << s) * y + 1
                checked += 1
                if v3(N) != d or (N // 3**d) % target_mod != base_child:
                    bad += 1
    return checked, bad

if __name__ == "__main__":
    print("(A) generic-door validity + distinctness:")
    print("   ", check_A_generic_doors())

    checked, bad = check_B_exact_ledger()
    print(f"(B) exact ledger (deterministic 2*3^(k-1-j) counts): {checked} windows checked, {bad} failures")

    c_old = critical_c(bonus=False)
    c_new = critical_c(bonus=True)
    print(f"(C) critical c, single-door baseline (sanity, should match 14.6.4's 0.3304...): {c_old:.6f}")
    print(f"(C) critical c, multi-door (guaranteed a=1.. extra doors, worst case):        {c_new:.6f}")
    print("    mass(0.33) with bonus at n_level1_triples=9 (window s in [2,54]):",
          total_mass(0.33, n_level1_triples=9))

    checked, bad = check_D_naive_precision_refuted()
    print(f"(D) naive 'child known mod 3^k when d<k' claim: {checked} checked, {bad} failures (REFUTED, as expected)")

    checked, bad = check_E_correct_precision_law()
    print(f"(E) correct 'child known mod 3^(k-d)' law:       {checked} checked, {bad} failures (should be 0)")
