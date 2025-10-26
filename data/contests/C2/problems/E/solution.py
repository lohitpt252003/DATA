#!/usr/bin/env python3
"""
Solver for Maximum Pair GCD problem.

This script looks for `*.in` files under `testcases/`, processes them sequentially
(one file at a time), writes corresponding `*.out` files, and prints timing and
a rough memory estimate per file to stderr.
"""
import os
import sys
import time


def max_pair_gcd(n: int) -> int:
    return n // 2


def process_file(path: str):
    content = open(path, 'r', encoding='utf-8').read().strip().split()
    if not content:
        out_path = os.path.splitext(path)[0] + '.out'
        open(out_path, 'w', encoding='utf-8').write('\n')
        return
    nums = [int(x) for x in content]
    # if first token equals count of following, treat as t
    if len(nums) >= 2 and nums[0] == len(nums) - 1:
        ns = nums[1:]
    else:
        ns = nums

    t0 = time.perf_counter()
    answers = [str(max_pair_gcd(n)) for n in ns]
    elapsed = time.perf_counter() - t0

    out_path = os.path.splitext(path)[0] + '.out'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(answers) + '\n')

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
