#!/usr/bin/env python3
"""
Solver for Product of Three Numbers (CF 1294C style interface).

Reads `testcases/*.in` files sequentially. Each `.in` file must follow the
format described in the problem: first line t (number of test cases) followed
by t lines, each with one integer n. The runner is robust and will fallback to
token parsing if files are not strictly line-formatted.

For each `.in` the script writes a single `.out` file (same basename, extension
`.out`) and prints timing/memory diagnostics to stderr. The script does NOT
create any other files.
"""
import os
import sys
import time
import math


def find_three_factors(n: int):
    """Return a tuple (a,b,c) of distinct integers >1 with a*b*c == n, or None."""
    # find smallest factor a
    a = -1
    limit = int(math.isqrt(n))
    for i in range(2, limit + 1):
        if n % i == 0:
            a = i
            break
    if a == -1:
        return None
    n1 = n // a
    # find a factor b of n1 different from a
    b = -1
    limit2 = int(math.isqrt(n1))
    for j in range(a + 1, limit2 + 1):
        if n1 % j == 0:
            b = j
            break
    if b == -1:
        for j in range(2, limit2 + 1):
            if n1 % j == 0 and j != a:
                b = j
                break
    if b == -1:
        return None
    c = n1 // b
    if c <= 1 or c == a or c == b:
        return None
    return (a, b, c)


def process_file(path: str):
    txt = open(path, 'r', encoding='utf-8').read()
    if not txt.strip():
        out_path = os.path.splitext(path)[0] + '.out'
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write('\n')
        return

    # Prefer strict line-based t format: first line = t, then t lines follow
    lines = [ln.strip() for ln in txt.splitlines() if ln.strip()]
    ns = None
    if len(lines) >= 1 and lines[0].lstrip('-').isdigit():
        tval = int(lines[0])
        if len(lines) - 1 >= tval:
            try:
                ns = [int(lines[i]) for i in range(1, 1 + tval)]
            except ValueError:
                ns = None

    if ns is None:
        # fallback to whitespace-token parsing
        tokens = txt.strip().split()
        vals = [int(x) for x in tokens]
        if len(vals) >= 2 and vals[0] == len(vals) - 1:
            ns = vals[1:]
        else:
            ns = vals

    out_lines = []
    t0 = time.perf_counter()
    for n in ns:
        res = find_three_factors(n)
        if res is None:
            out_lines.append('NO')
        else:
            a, b, c = res
            out_lines.append('YES')
            out_lines.append(f"{a} {b} {c}")
    elapsed = time.perf_counter() - t0

    out_path = os.path.splitext(path)[0] + '.out'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out_lines) + '\n')

    import sys as _sys
    mem = _sys.getsizeof(ns) + sum(_sys.getsizeof(x) for x in out_lines)
    print(f"FILE: {os.path.basename(path)} TIME_SEC: {elapsed:.6f} EST_MEM_BYTES: {mem}", file=sys.stderr)


def main():
    base = os.path.dirname(__file__)
    tc_dir = os.path.join(base, 'testcases')
    if not os.path.isdir(tc_dir):
        print('No testcases directory found at', tc_dir, file=sys.stderr)
        return
    for name in sorted(os.listdir(tc_dir)):
        if not name.endswith('.in'):
            continue
        path = os.path.join(tc_dir, name)
        try:
            process_file(path)
        except Exception as e:
            print('Error processing', name, ':', e, file=sys.stderr)


if __name__ == '__main__':
    main()
