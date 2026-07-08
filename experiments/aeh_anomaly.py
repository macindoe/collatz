# Anomaly resolution experiments (aeh.md 13.5): equilibration curve,
# deterministic routing check, long-horizon altitude bands.

# X1: equilibration curve for the (1 mod 8, d=1) anomaly.
# Uniform 100-bit starts, fixed 32 steps, NO early stopping, no per-orbit
# weighting. Tally P(omega = 25 mod 32 | class (1,1)) at step T.
import random
from collections import Counter
def v2(x): return (x & -x).bit_length() - 1
def step(w, d):
    A = 3**d * w - 1; s = v2(A); C = A + (1 << s)
    sig = v2(C); a = 0; u = C >> sig
    while u % 3 == 0: u //= 3; a += 1
    return s, u, sig - s + a
random.seed(83)
buckets = {1:0, 2:0, 4:0, 8:0, 16:0, 24:0, 32:0}
hits = Counter(); tot = Counter()
prof = Counter(); ptot = 0          # full mod-32 profile at T >= 16
NORB = 90000
for _ in range(NORB):
    w = random.getrandbits(100) | 1
    if w % 3 == 0: continue
    d = random.randrange(1, 8)
    for T in range(1, 33):
        s, w, d = step(w, d)
        if T in buckets and w % 8 == 1 and d == 1:
            tot[T] += 1; hits[T] += (w % 32 == 25)
        if T >= 16 and w % 8 == 1 and d == 1:
            prof[w % 32] += 1; ptot += 1
print("equilibration: P(omega=25 mod 32 | class (1,1)) by step T (null 0.25):")
for T in sorted(buckets):
    p = hits[T]/tot[T]; se = (p*(1-p)/tot[T])**0.5
    print(f"  T={T:2d}: {p:.4f} ± {se:.4f}   (n={tot[T]})")
print("\nfull mod-32 profile at T>=16 (each null 0.25):")
for r in (1, 9, 17, 25):
    print(f"  omega={r:2d} mod 32: {prof[r]/ptot:.4f}   (n={ptot})")

# X2: (a) verify the exact mod-32 -> next-class transition law from class (1,1);
# (b) fixed 150-step horizon from 140-bit starts (altitude stays >> 2^40),
#     pooled per-visit tallies at ALL steps: any altitude-dependent bias?
import random
from collections import Counter
def v2(x): return (x & -x).bit_length() - 1
def step(w, d):
    A = 3**d * w - 1; s = v2(A); C = A + (1 << s)
    sig = v2(C); a = 0; u = C >> sig
    while u % 3 == 0: u //= 3; a += 1
    return s, u, sig - s + a
random.seed(89)
# (a) exact transition check
trans = {}
for _ in range(40000):
    w = (random.getrandbits(60) << 5) | random.choice((1, 9, 17, 25))
    if w % 3 == 0 or w % 8 != 1: continue
    s, w1, d1 = step(w, 1)
    key = (w % 32, (w1 % 8, d1))
    trans[key] = trans.get(key, 0) + 1
by_res = {}
for (r, c), n in trans.items(): by_res.setdefault(r, []).append((c, n))
print("(a) from class (1,1): omega mod 32 -> next class (should be deterministic):")
for r in (1, 9, 17, 25):
    tt = sorted(by_res[r], key=lambda x: -x[1])
    total = sum(n for _, n in tt)
    print(f"  {r:2d} -> {tt[0][0]}  ({tt[0][1]}/{total}{'  DETERMINISTIC' if tt[0][1]==total else '  NOT deterministic: ' + str(tt[:3])})")
# (b) long-horizon pooled tallies
hits = Counter(); tot = Counter()
for _ in range(30000):
    w = random.getrandbits(140) | 1
    if w % 3 == 0: continue
    d = random.randrange(1, 8)
    for T in range(1, 151):
        s, w, d = step(w, d)
        if w % 8 == 1 and d == 1:
            band = T // 50   # 0: steps 1-49, 1: 50-99, 2: 100-150
            tot[band] += 1; hits[band] += (w % 32 == 25)
print("\n(b) P(omega=25 mod 32 | class (1,1)), pooled, fixed 150-step horizon:")
for band in (0, 1, 2):
    p = hits[band] / tot[band]; se = (p * (1 - p) / tot[band]) ** 0.5
    print(f"  steps {band*50}-{band*50+49}: {p:.4f} ± {se:.4f}  (n={tot[band]})")
