#!/usr/bin/env python3
"""
Solver for "GCD of Pairwise LCMs".

This script processes `testcases/*.in` files one-by-one and writes corresponding
`.out` files. For each input file it reads either a single test (n and array)
or a leading t followed by t test cases (the solver handles both modes).

Implementation notes:
- Uses smallest-prime-factor sieve up to max(ai) (<= 200000) to factorize numbers fast.
- For each prime p we keep a list of exponents across numbers where p appears.
- After processing all numbers, for each prime we compute zeros = n - len(list).
  if zeros >= 2 => exponent contribution is 0; if zeros == 1 => exponent = min(list);
  else exponent = second smallest in list. Multiply primes^exponent into the answer.

Prints per-file TIME_SEC and EST_MEM_BYTES to stderr.
"""
import os
import sys
import math
import time
from collections import defaultdict


def build_spf(limit):
    spf = list(range(limit + 1))
    for i in range(2, int(math.isqrt(limit)) + 1):
        if spf[i] == i:
            step = i
            start = i * i
            for j in range(start, limit + 1, step):
                if spf[j] == j:
                    spf[j] = i
    return spf


def factorize(x, spf):
    res = {}
    while x > 1:
        p = spf[x]
        cnt = 0
        while x % p == 0:
            x //= p
            cnt += 1
        res[p] = cnt
    return res


def process_single_test(n, arr, spf):
    maxa = max(arr) if arr else 0
    prime_exps = defaultdict(list)
    for x in arr:
        if x == 1:
            continue
        fac = factorize(x, spf)
        for p, e in fac.items():
            prime_exps[p].append(e)

    ans = 1
    for p, exps in prime_exps.items():
        k = len(exps)
        zeros = n - k
        exps.sort()
        if zeros >= 2:
            continue
        elif zeros == 1:
            exp = exps[0]
        else:
            # zeros == 0
            if len(exps) >= 2:
                exp = exps[1]
            else:
                exp = 0
        if exp > 0:
            ans *= pow(p, exp)
    return ans


def process_file(path):
    txt = open(path, 'r', encoding='utf-8').read().strip().split()
    if not txt:
        out_path = os.path.splitext(path)[0] + '.out'
        open(out_path, 'w', encoding='utf-8').write('\n')
        return
    it = iter(txt)
    vals = [int(x) for x in txt]
    # decide format: if first token t equals number of following tests? Not safe here.
    # We'll attempt to parse common single-test (n then n numbers). If mismatch, try t-format.
    out_lines = []
    ptr = 0
    start_time = time.perf_counter()
    # precompute spf up to maximum ai found in file (safe upper bound 200000)
    max_a = 0
    # attempt to find max ai by scanning tokens: tokens include n and ai; difficult to know positions without parsing.
    # Simpler: parse assuming single test or multiple tests: if first token is total count of tests t and remaining tokens match expected sizes,
    # otherwise treat as single test consisting of n followed by n numbers.
    tokens = vals
    # Try t-format
    ok = False
    if len(tokens) >= 1:
        t = tokens[0]
        idx = 1
        ok_t = True
        max_a_candidate = 0
        for _ in range(t):
            if idx >= len(tokens):
                ok_t = False
                break
            n = tokens[idx]; idx += 1
            if idx + n - 1 >= len(tokens):
                ok_t = False
                break
            for j in range(n):
                max_a_candidate = max(max_a_candidate, tokens[idx+j])
            idx += n
        if ok_t and idx == len(tokens):
            ok = True
            max_a = max_a_candidate
            spf = build_spf(max(2, max_a))
            idx = 1
            for _ in range(t):
                n = tokens[idx]; idx += 1
                arr = tokens[idx:idx+n]; idx += n
                res = process_single_test(n, arr, spf)
                out_lines.append(str(res))
    if not ok:
        # Treat as single test: first token n followed by n numbers
        n = tokens[0]
        arr = tokens[1:1+n]
        max_a = max(arr) if arr else 0
        spf = build_spf(max(2, max_a))
        res = process_single_test(n, arr, spf)
        out_lines.append(str(res))
    elapsed = time.perf_counter() - start_time
    out_path = os.path.splitext(path)[0] + '.out'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out_lines) + '\n')
    import sys as _sys
    mem = _sys.getsizeof(out_lines) + sum(_sys.getsizeof(x) for x in out_lines)
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
