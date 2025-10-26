#!/usr/bin/env python3
"""
Segmented-sieve runner for PRIME1 testcases.

Enhanced version:
- Writes output as *.out (e.g., 4.in -> 4.out)
- Prints execution time and peak memory usage per testcase
"""

import os
import math
import sys
import time
import tracemalloc


def simple_sieve(limit):
    """Return list of primes up to limit (inclusive) using simple sieve."""
    if limit < 2:
        return []
    mark = bytearray(b"\x01") * (limit + 1)
    mark[0:2] = b"\x00\x00"
    for i in range(2, int(math.isqrt(limit)) + 1):
        if mark[i]:
            step = i
            start = i * i
            mark[start:limit + 1:step] = b"\x00" * (((limit - start) // step) + 1)
    return [i for i in range(2, limit + 1) if mark[i]]


def segmented_sieve(m, n, base_primes):
    """Return list of primes in [m, n] using base_primes (primes up to sqrt(n))."""
    size = n - m + 1
    is_prime = bytearray(b"\x01") * size
    for p in base_primes:
        p2 = p * p
        if p2 > n:
            break
        start = p2 if p2 >= m else ((m + p - 1) // p) * p
        for j in range(start, n + 1, p):
            is_prime[j - m] = 0
    if m == 1:
        is_prime[0] = 0
    return [str(m + i) for i, v in enumerate(is_prime) if v]


def process_input_file(path):
    """Process one .in file and write .out file."""
    text = open(path, "r", encoding="utf-8").read().strip().split()
    if not text:
        open(path[:-3] + ".out", "w", encoding="utf-8").write("\n")
        return

    it = iter(text)
    try:
        t = int(next(it))
    except StopIteration:
        t = 0
    ranges = []
    max_n = 0
    for _ in range(t):
        m = int(next(it))
        n = int(next(it))
        ranges.append((m, n))
        max_n = max(max_n, n)

    # compute base primes up to sqrt(max_n)
    lim = int(math.isqrt(max_n)) + 1 if max_n >= 2 else 1
    base_primes = simple_sieve(lim)

    out_lines = []
    for idx, (m, n) in enumerate(ranges):
        primes = segmented_sieve(m, n, base_primes)
        if primes:
            out_lines.extend(primes)
        if idx != len(ranges) - 1:
            out_lines.append("")

    out_path = path[:-3] + ".out"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(out_lines) + "\n")


def main():
    base = os.path.dirname(__file__)
    tc_dir = os.path.join(base, "testcases")
    if not os.path.isdir(tc_dir):
        print("No testcases/ directory found in", base, file=sys.stderr)
        return

    names = sorted(os.listdir(tc_dir))
    for name in names:
        if not name.endswith(".in"):
            continue
        path = os.path.join(tc_dir, name)
        print(f"\nProcessing {name} ...", file=sys.stderr)

        start = time.time()
        tracemalloc.start()
        try:
            process_input_file(path)
        except Exception as e:
            print("Error processing", name, ":", e, file=sys.stderr)
            continue
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        elapsed = time.time() - start

        print(f"✔ {name} done in {elapsed:.3f}s | Peak memory: {peak/1024:.1f} KB", file=sys.stderr)


if __name__ == "__main__":
    main()
