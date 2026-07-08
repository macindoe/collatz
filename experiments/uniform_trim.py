# Uniform trim lemma tests (cycles.md 12.8): staircase sharpness family,
# uniform-bound consistency, divisibility checks.

# Uniform trim lemma (cycles.md 12.8): tests.
# (1) Staircase sharpness: at p = 6, find configs passing ALL exact rotation
#     size tests (min_r R_r >= q) with gamma << 0.1157n - 2  (p=3 constant fails).
# (2) Confirm staircase size-passers all fail divisibility.
# (3) Confirm every size-passer respects the uniform bound n < 1.71(gamma+log2 p)L3^p.
import math, itertools, random
L3 = math.log2(3)

def R_rot(ms, ss):
    p = len(ms); R = 0; Spre = 0
    for t in range(p):
        R += 3**sum(ms[t+1:]) * (1 << Spre) * ((1 << ss[t]) - 1)
        Spre += ss[t] + ms[(t + 1) % p]
    return R
def minR(ms, ss):
    p = len(ms)
    return min(R_rot(ms[r:] + ms[:r], ss[r:] + ss[:r]) for r in range(p))
def allR(ms, ss):
    p = len(ms)
    return [R_rot(ms[r:] + ms[:r], ss[r:] + ss[:r]) for r in range(p)]

p = 6
passers = []
random.seed(41)
for n in range(20, 140):
    T3 = 3**n; K = T3.bit_length(); q = (1 << K) - T3; S = K - n
    if S < p: continue
    gamma = K - math.log2(q)
    # staircase candidates: m geometric-ish (ratio ~L3), s = 1 except one crash
    cands = set()
    for m0 in (1, 2, 3):
        for ratio in (1.45, 1.585, 1.7):
            m = [max(1, round(m0 * ratio**j)) for j in range(p - 1)]
            rest = n - sum(m)
            if rest < 1: continue
            m = m + [rest]
            for crash_pos in range(p):
                s = [1] * p; s[crash_pos] = S - (p - 1)
                if s[crash_pos] < 1: continue
                cands.add((tuple(m), tuple(s)))
    # a few random perturbations of each
    more = set()
    for ms, ss in cands:
        for _ in range(6):
            m = list(ms); i, j = random.randrange(p), random.randrange(p)
            if m[i] > 1: m[i] -= 1; m[j] += 1
            more.add((tuple(m), tuple(ss)))
    for ms, ss in cands | more:
        if sum(ms) != n or sum(ss) != S or min(ms) < 1: continue
        if minR(list(ms), list(ss)) >= q:
            Rs = allR(list(ms), list(ss))
            div_ok = all(R % q == 0 for R in Rs)
            passers.append((n, round(gamma, 2), round(0.1157*n - 2, 1), ms, ss, div_ok))

print(f"p={p}: staircase size-passers found: {len(passers)}")
for row in passers[:8]:
    n, g, p3const, ms, ss, div = row
    print(f"  n={n:3d} gamma={g:5.2f}  (p=3-constant would demand > {p3const})  m={ms} s={ss}  divisible={div}")
if passers:
    v = max(n / (1.71 * (g + math.log2(p)) * L3**p) for n, g, *_ in passers)
    print(f"uniform-bound ratio n / [1.71(gamma+log2 p)L3^p], max over passers: {v:.3f} (must be < 1)")
    print("any pass divisibility (would be a cycle!):", any(r[5] for r in passers))

# ---- focused staircase (correct shape) ----
# Correct staircase: m_j = round(c*L3^j) for j=0..p-2 (scaled to sum n-1),
# m_{p-1} = 1, s = 1 everywhere except s_{p-1} = S-(p-1). Seek size-passers
# with gamma < 0.1157n - 2 (violating the p=3-shaped constant at p=6).
import math, random
L3 = math.log2(3)
def R_rot(ms, ss):
    p = len(ms); R = 0; Spre = 0
    for t in range(p):
        R += 3**sum(ms[t+1:]) * (1 << Spre) * ((1 << ss[t]) - 1)
        Spre += ss[t] + ms[(t + 1) % p]
    return R
def allR(ms, ss):
    p = len(ms)
    return [R_rot(ms[r:] + ms[:r], ss[r:] + ss[:r]) for r in range(p)]

random.seed(43)
best = []
for p in (5, 6, 7):
    for n in range(40, 220):
        T3 = 3**n; K = T3.bit_length(); q = (1 << K) - T3; S = K - n
        if S < p: continue
        gamma = K - math.log2(q)
        thresh = 0.1157 * n - 2
        if gamma >= thresh: continue          # only interesting if p=3 constant would forbid
        geo = [L3**j for j in range(p - 1)]
        c = (n - 1) / sum(geo)
        base = [max(1, round(c * g)) for g in geo]
        base[-1] += (n - 1) - sum(base)       # fix rounding into biggest block
        if base[-1] < 1: continue
        for jitter in range(12):
            m = base[:]
            if jitter:
                i, j = random.randrange(p - 1), random.randrange(p - 1)
                if m[i] > 1: m[i] -= 1; m[j] += 1
            m = m + [1]
            if sum(m) != n or min(m) < 1: continue
            s = [1] * p; s[p - 1] = S - (p - 1)
            if s[p - 1] < 1: continue
            Rs = allR(m, s)
            if min(Rs) >= q:
                best.append((p, n, round(gamma, 2), round(thresh, 1), tuple(m),
                             all(R % q == 0 for R in Rs)))
                break
for row in best[:12]: print(" ", row)
if best:
    mx = max(b[1] / (1.71 * (b[2] + math.log2(b[0])) * L3**b[0]) for b in best)
    print(f"passers violating p=3 constant: {len(best)}; largest n: {max(b[1] for b in best)}")
    print(f"uniform-bound ratio (must be < 1): max {mx:.3f}")
    print("any divisible (= actual cycle!):", any(b[5] for b in best))
else:
    print("no violations found — p=3-shaped constant may survive; investigate")
