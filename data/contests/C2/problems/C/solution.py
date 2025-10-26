#!/usr/bin/env python3
"""
Solution runner for CF 235A (LCM Challenge).

This script scans the `testcases/` directory for `*.in` files and processes them
one-by-one (sequentially). For each input file it computes the optimal answer
and writes a corresponding `.out` file. It also prints timing and a rough
memory estimate to stderr per input file.

The solver itself uses the O(1) math formula per n (constant time), so this
script is fast even for large inputs. It is deliberately sequential: it will
finish processing one `.in` before starting the next.
"""
import os
import sys
import time
import math


def max_lcm(n: int) -> int:
    if n <= 2:
        return n
    if n == 3:
        return 6
    # If n is odd, n*(n-1)*(n-2) is coprime triple and maximal
    if n % 2 == 1:
        return n * (n - 1) * (n - 2)
    # n is even
    # If n is divisible by 3, then (n-1)*(n-2)*(n-3) might be larger
    if n % 3 != 0:
        return n * (n - 1) * (n - 3)
    else:
        return (n - 1) * (n - 2) * (n - 3)


def process_file(path: str):
    data = open(path, 'r', encoding='utf-8').read().strip().split()
    if not data:
        # write empty out
        out_path = os.path.splitext(path)[0] + '.out'
        open(out_path, 'w', encoding='utf-8').write('\n')
        return

    # Interpret file: if first token equals count of remaining, treat as t
    tokens = [int(x) for x in data]
    if len(tokens) >= 2 and tokens[0] == len(tokens) - 1:
        ns = tokens[1:]
    else:
        # treat every token as an independent n (covers single-number files too)
        ns = tokens

    t0 = time.perf_counter()
    answers = [str(max_lcm(n)) for n in ns]
    elapsed = time.perf_counter() - t0

    out_path = os.path.splitext(path)[0] + '.out'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(answers) + '\n')

    # rough memory estimate
    import sys as _sys
    mem = _sys.getsizeof(ns) + sum(_sys.getsizeof(a) for a in answers)
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
