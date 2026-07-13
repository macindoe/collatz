"""
Stream anchor M(omega) bits as raw bytes to stdout, for piping into a strong
external PRNG battery (PractRand's RNG_test, or a file for TestU01 Alphabit/
Rabbit). Supports anchors.md S17.7's stopping-rule-permitted structure hunt on
one further, much stronger axis than the in-repo batteries.

Framing choice (option "b", the AEH-aligned one): the stream is a CONCATENATION
of many independent bulk anchors, each M(omega) to D bits, rather than one very
deep anchor. AEH is a bulk/ensemble claim, so a strong-battery pass on the
anchor *family* is the more relevant result; it also plays to the generator's
fast-per-anchor regime (one deep anchor is O(D^2)-capped). Random bulk omega are
used so no ordering correlation is induced; the low-order proven-structure bits
(bounded-reach digit-determinacy law, stage4 11.8.7.2) are dropped via --skip so
the battery sees the genuinely-open bulk, not a known deterministic prefix.

Modes (the last two are validation controls for the pipe itself):
  anchors  -- the concatenated M(omega) bulk stream (the actual test)
  urandom  -- os.urandom bytes: a true-random reference; PractRand MUST pass it
              (proves the pipe/format is right and the battery doesn't false-alarm)
  counter  -- an incrementing counter: blatantly structured; PractRand MUST fail
              it almost immediately (proves the setup can SEE structure)

Null model, as everywhere in S17.7: bits i.i.d. fair coin. PractRand is a far
stronger family of distinguishers than the NIST battery (S17.7.1); a clean pass
strengthens the pseudo-randomness calibration, a failure is a real find to
verify. As established in S17.7.4, M(omega) is computable hence NOT Martin-Lof
random -- this tests pseudo-randomness, at a scale the in-repo tests could not.

Usage:
  python anchor_bitstream.py --mode anchors --skip 64 --bits-per-anchor 8192 \
      | /path/to/RNG_test.exe stdin8 -tlmax 256MB
Fresh generator, validated 12/12 vs anchors.md S17.7 before streaming.
"""
import argparse
import multiprocessing as mp
import os
import random
import sys

# ---------------------------------------------------------------------
# Fresh M(omega) generator (2-adic-log series; imports nothing).
# ---------------------------------------------------------------------

def _v2(x):
    v = 0
    while x & 1 == 0:
        x >>= 1; v += 1
    return v


def _log1p(x, prec):
    mod = 1 << prec
    mask = mod - 1
    x &= mask
    if x == 0:
        return 0
    vx = _v2(x)
    acc = 0; xi = 1; i = 0
    while True:
        i += 1
        xi = (xi * x) & mask
        if i * vx >= prec:
            break
        e = _v2(i)
        t = ((xi >> e) * pow(i >> e, -1, mod)) & mask
        acc = (acc + t) & mask if (i & 1) else (acc - t) & mask
    return acc & mask


_L9 = {}

def _log9(prec):
    if prec not in _L9:
        _L9[prec] = _log1p(8, prec)
    return _L9[prec]


def anchor_int(omega, nbits, margin=192):
    prec = nbits + margin
    mask = (1 << prec) - 1
    x = ((omega * omega) - 1) & mask
    if x == 0:
        return 0
    Lw = _log1p(x, prec)
    L9 = _log9(prec)
    p = prec - 3
    pm = (1 << p) - 1
    N = (-((Lw >> 3) & pm) * pow((L9 >> 3) & pm, -1, 1 << p)) & pm
    return N & ((1 << nbits) - 1)


_REFERENCE = {
    1: "000000000000000000000000", 3: "111111111111111111111111",
    5: "101011110100001111101100", 7: "010010101101111111001101",
    11: "100110111000001010010011", 13: "110111011010100100010110",
    17: "001100100100010001101100", 31: "000101001100101110110001",
}

def _validate():
    for w, ref in _REFERENCE.items():
        n = anchor_int(w, 24)
        got = "".join(str((n >> i) & 1) for i in range(24))
        assert got == ref, f"gen mismatch omega={w}: {got} != {ref}"


# ---------------------------------------------------------------------
# Streams
# ---------------------------------------------------------------------

def stream_anchors(out, D, skip, seed, total_bytes):
    """Concatenate M(omega) for random bulk omega: bits [skip, D) of each,
    packed little-endian, until total_bytes emitted (or forever if 0)."""
    assert (D - skip) % 8 == 0, "(bits-per-anchor - skip) must be a multiple of 8"
    nb = (D - skip) // 8
    keepmask = (1 << (D - skip)) - 1
    rng = random.Random(seed)
    written = 0
    while total_bytes == 0 or written < total_bytes:
        w = rng.randrange(1 << 40, 1 << 64) | 1
        if w % 3 == 0:
            continue
        val = (anchor_int(w, D) >> skip) & keepmask
        try:
            out.write(val.to_bytes(nb, "little"))
        except BrokenPipeError:
            return
        written += nb


def _anchor_worker(task):
    """Top-level (picklable) worker: (omega, D, skip, nb, keepmask) -> bytes.
    Order is preserved by Pool.imap, so the stream is deterministic in the
    omega sequence regardless of which core computes which anchor."""
    omega, D, skip, nb, keepmask = task
    return ((anchor_int(omega, D) >> skip) & keepmask).to_bytes(nb, "little")


def stream_anchors_parallel(out, D, skip, seed, total_bytes, jobs):
    """Same concatenated stream as stream_anchors, but anchors are computed
    across `jobs` processes; Pool.imap keeps output order = omega order, so the
    byte stream is identical (and reproducible) for a given seed and job count-
    independent because order is preserved."""
    assert (D - skip) % 8 == 0
    nb = (D - skip) // 8
    keepmask = (1 << (D - skip)) - 1
    rng = random.Random(seed)

    def tasks():
        while True:
            w = rng.randrange(1 << 40, 1 << 64) | 1
            if w % 3:
                yield (w, D, skip, nb, keepmask)

    written = 0
    with mp.Pool(jobs) as pool:
        try:
            for chunk in pool.imap(_anchor_worker, tasks(), chunksize=4):
                out.write(chunk)
                written += len(chunk)
                if total_bytes and written >= total_bytes:
                    break
        except BrokenPipeError:
            pass
        finally:
            pool.terminate()


def stream_urandom(out, total_bytes):
    written = 0
    chunk = 1 << 16
    while total_bytes == 0 or written < total_bytes:
        n = chunk if total_bytes == 0 else min(chunk, total_bytes - written)
        try:
            out.write(os.urandom(n))
        except BrokenPipeError:
            return
        written += n


def stream_counter(out, total_bytes):
    written = 0
    c = 0
    while total_bytes == 0 or written < total_bytes:
        try:
            out.write((c & 0xFFFFFFFFFFFFFFFF).to_bytes(8, "little"))
        except BrokenPipeError:
            return
        c += 1
        written += 8


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["anchors", "urandom", "counter"], default="anchors")
    ap.add_argument("--bits-per-anchor", type=int, default=8192)
    ap.add_argument("--skip", type=int, default=64, help="drop low-order proven-structure bits")
    ap.add_argument("--seed", type=int, default=20260713)
    ap.add_argument("--total-mb", type=float, default=0.0, help="0 = stream until pipe closes")
    ap.add_argument("--jobs", type=int, default=1, help="parallel processes for anchor generation")
    ap.add_argument("--no-validate", action="store_true")
    args = ap.parse_args()

    if not args.no_validate:
        _validate()
        print(f"[anchor_bitstream] generator 12/12 OK; mode={args.mode} "
              f"D={args.bits_per_anchor} skip={args.skip} seed={args.seed}", file=sys.stderr)

    total = int(args.total_mb * (1 << 20))
    out = sys.stdout.buffer
    if args.mode == "anchors":
        if args.jobs > 1:
            stream_anchors_parallel(out, args.bits_per_anchor, args.skip, args.seed, total, args.jobs)
        else:
            stream_anchors(out, args.bits_per_anchor, args.skip, args.seed, total)
    elif args.mode == "urandom":
        stream_urandom(out, total)
    else:
        stream_counter(out, total)


if __name__ == "__main__":
    main()
