"""Encoding integrity scan over the tracked tree.

Supports: HANDOFF.md "Known infrastructure quirks" (the PowerShell 5.1 UTF-8 hazard).

Three faults are detected, all of which have actually occurred in this repo and all
of which are invisible to `git diff --stat`:

1. **Double encoding.** PowerShell 5.1 `Get-Content` decodes UTF-8 as ANSI and
   `Set-Content -Encoding utf8` writes the result back as UTF-8. Every non-ASCII
   character is mangled. These pages are dense with em dashes and mathematical
   symbols, so the damage is total and silent, and it survives commits, rebases
   and merges. Observed 2026-07-26 in HANDOFF.md (125 sequences).

2. **ANSI/cp1252 output.** The inverse fault: a script's output redirected through
   a console that encodes as cp1252, leaving bytes that are not valid UTF-8 at all.
   Observed in experiments/merle_la6_check_output.txt (a 0x97 em-dash byte).

3. **Byte-order marks.** PowerShell `>` redirection prepends a UTF-8 BOM. Harmless
   to content but it makes review re-runs compare unequal ("identical modulo a
   BOM"), which costs time at exactly the moment verification is being checked.

Binary files (PDF, PNG) are skipped by extension, not by guesswork.

Run from anywhere; it resolves the repo root from its own location.
Exit status is 0 when clean, 1 when anything is found, so it can gate a commit.
"""

import os
import subprocess
import sys

BINARY_EXT = {'.pdf', '.png', '.jpg', '.jpeg', '.gif', '.zip', '.gz', '.ico', '.json'}

# Mojibake forms of characters this repo actually uses. Each key is what the
# character becomes after one spurious ANSI->UTF-8 round trip. Built from
# codepoints rather than written literally, so that this file never becomes a
# false positive for its own scan.
def _mojibake(ch):
    return ch.encode('utf-8').decode('cp1252', errors='replace')

WATCHED = ['—', '–', '≤', '≥', 'β', 'ε',
           '⌈', '⌊', '₀', '·', 'é', '→']

SIGNATURES = {}
for _ch in WATCHED:
    _m = _mojibake(_ch)
    if '�' not in _m:
        SIGNATURES[_m] = _ch


def repo_root():
    here = os.path.dirname(os.path.abspath(__file__))
    out = subprocess.run(['git', 'rev-parse', '--show-toplevel'],
                         cwd=here, capture_output=True, text=True)
    return out.stdout.strip() or os.path.dirname(here)


def main():
    # A finding's sample can contain characters the Windows default console
    # encoding cannot represent; without this the report crashes mid-print,
    # after the count header and before the file name and RESULT line --
    # which is exactly how a real finding went unread on 2026-08-03.
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    root = repo_root()
    os.chdir(root)
    files = [f for f in subprocess.run(['git', 'ls-files'], capture_output=True,
                                       text=True).stdout.split('\n') if f.strip()]

    not_utf8, with_bom, doubled = [], [], []

    for f in files:
        if os.path.splitext(f)[1].lower() in BINARY_EXT:
            continue
        try:
            raw = open(f, 'rb').read()
        except (OSError, IOError):
            continue
        if raw.startswith(b'\xef\xbb\xbf'):
            with_bom.append(f)
        try:
            text = raw.decode('utf-8')
        except UnicodeDecodeError as exc:
            not_utf8.append((f, exc.start, raw[exc.start:exc.start + 1]))
            continue
        hits = {}
        for sig, ch in SIGNATURES.items():
            n = text.count(sig)
            if n:
                hits[ch] = n
        if hits:
            doubled.append((f, hits))

    print('encoding scan: %d tracked files (binary extensions skipped)' % len(files))
    print()
    print('not valid UTF-8 (%d):' % len(not_utf8))
    for f, pos, byte in not_utf8:
        print('    %s  first bad byte %s at offset %d' % (f, byte.hex(), pos))
    print()
    print('UTF-8 BOM present (%d):' % len(with_bom))
    for f in with_bom:
        print('    %s' % f)
    print()
    print('double-encoding signatures (%d):' % len(doubled))
    for f, hits in doubled:
        print('    %s  %s' % (f, ', '.join('%r x%d' % (c, n) for c, n in hits.items())))
    print()

    clean = not (not_utf8 or with_bom or doubled)
    print('RESULT:', 'CLEAN' if clean else 'ISSUES FOUND')
    return 0 if clean else 1


if __name__ == '__main__':
    sys.exit(main())
