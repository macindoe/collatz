"""
Generate the data feeding viz/anchor_digit_visualizer.html.

Brief: briefs/anchor-digit-search-brief.md. Scope: anchors.md S17.9,
first-tier visualizations (recurrence plot, chaos-game representation)
for a handful of representative omega, including at least one from the
"bottom" (small omega, known-structured per aeh.md S13.1's bulk/bottom
split, applied here to the historically-flagged small omega of
archive/appendix-a.md A.4.6) and several from the bulk, so the known
bottom/bulk distinction is visually confirmed before looking for
anything new.

This script computes M(omega) bit strings for a fixed representative
set and writes them into the HTML as inline hex-encoded data (avoiding
a runtime fetch, since the page is opened from the filesystem) -- the
canvases themselves (recurrence plot, chaos game) are computed and drawn
client-side in JS, so window width / mode selection stays interactive
without recomputing the anchor. See viz/anchor_digit_visualizer.html.

Fresh generator implementation, third independent copy in this brief's
code (see anchor_digit_structure.py and anchor_compressibility.py for
the other two, and the shared derivation) -- re-validated against the
same anchors.md S17.7 reference table before use.
"""
import string

def v2(x):
    if x == 0:
        return None
    v = 0
    while x % 2 == 0:
        x //= 2
        v += 1
    return v


def log2adic(x, M):
    mask = (1 << M) - 1
    x &= mask
    if x == 0:
        return 0
    vx = v2(x)
    total = 0
    xi = 1
    i = 0
    while True:
        i += 1
        xi = (xi * x) & mask
        if i * vx >= M:
            break
        e = v2(i) if i % 2 == 0 else 0
        j = i >> e
        term = ((xi >> e) * pow(j, -1, 1 << M)) & mask
        total = (total + term if i % 2 == 1 else total - term) & mask
    return total & mask


_log9_cache = {}


def compute_M_omega(omega, target_bits, margin=160):
    M = target_bits + 3 + margin
    mask = (1 << M) - 1
    y = (omega * omega) & mask
    x = (y - 1) & mask
    if x == 0:
        return 0
    Ly = log2adic(x, M)
    if M not in _log9_cache:
        _log9_cache[M] = log2adic(8, M)
    L9 = _log9_cache[M]
    prec = M - 3
    pmask = (1 << prec) - 1
    u9 = (L9 >> 3) & pmask
    inv_u9 = pow(u9, -1, 1 << prec)
    Ly_shift = (Ly >> 3) & pmask
    N = (-(Ly_shift * inv_u9)) & pmask
    return N & ((1 << target_bits) - 1)


def bits_lsb_first(n, k):
    return [(n >> i) & 1 for i in range(k)]


def validate_against_reference():
    reference = {
        1: "000000000000000000000000", 3: "111111111111111111111111",
        5: "101011110100001111101100", 7: "010010101101111111001101",
        11: "100110111000001010010011", 13: "110111011010100100010110",
        17: "001100100100010001101100", 19: "110000011010111111001110",
        23: "011001111111100000001110", 29: "111011010111011110110011",
        31: "000101001100101110110001", 37: "101101110100011110111111",
    }
    for omega, ref in reference.items():
        got = "".join(str(b) for b in bits_lsb_first(compute_M_omega(omega, 24), 24))
        assert got == ref, f"omega={omega}: got {got}, expected {ref}"
    return True


def bits_to_hex(bits):
    n = len(bits)
    pad = (-n) % 4
    padded = bits + [0] * pad
    out = []
    for i in range(0, len(padded), 4):
        nibble = padded[i] | (padded[i + 1] << 1) | (padded[i + 2] << 2) | (padded[i + 3] << 3)
        out.append("0123456789abcdef"[nibble])
    return "".join(out)


REPRESENTATIVES = [
    # (omega, label, group)
    (1, "omega=1 (fixed point, M=0 exactly)", "bottom"),
    (3, "omega=3 (M=-1 exactly, 3^2=9 is the log's own base)", "bottom"),
    (25, "omega=25 (A.4.6 'regular' tower)", "bottom"),
    (49, "omega=49 (A.4.6 'regular' tower)", "bottom"),
    (17, "omega=17 (A.4.6 'irregular' tower)", "bottom"),
    (41, "omega=41 (A.4.6 'irregular' tower)", "bottom"),
    (1234567891, "omega=1234567891 (bulk)", "bulk"),
    (9876543211, "omega=9876543211 (bulk)", "bulk"),
    (2**50 + 87, "omega=2^50+87 (bulk)", "bulk"),
    (1152921504606847169, "omega=2^60+193 (bulk, 3|w+ excluded, using nearby coprime)", "bulk"),
]


def main():
    print("Validating generator against anchors.md S17.7 worked example...")
    validate_against_reference()
    print("  OK.\n")

    BITS = 8192
    data = []
    for omega, label, group in REPRESENTATIVES:
        assert omega % 2 == 1, f"omega={omega} must be odd"
        # omega=3 is deliberately included as a known algebraic degeneracy
        # (M(3)=-1 exactly, since 3^2=9 is the log's own base); every other
        # representative is required coprime to 3 (see sample_omegas's
        # docstring rationale in anchor_digit_structure.py).
        assert omega == 3 or omega % 3 != 0, f"omega={omega} must be coprime to 3"
        bits = bits_lsb_first(compute_M_omega(omega, BITS), BITS)
        hexstr = bits_to_hex(bits)
        data.append(dict(omega=omega, label=label, group=group, bits=BITS, hex=hexstr))
        print(f"  omega={omega:22d}  group={group:6s}  {BITS} bits computed  ({label})")

    template_path = "viz/_anchor_digit_visualizer_template.html"
    out_path = "viz/anchor_digit_visualizer.html"
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    import json
    data_json = json.dumps(data)
    out = template.replace("/*__ANCHOR_DATA__*/", data_json)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"\nWrote {out_path} ({len(out)} bytes).")


if __name__ == "__main__":
    main()
