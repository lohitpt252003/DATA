import argparse
import os
import random
from typing import List


def write_case_file(path: str, t: int, ns: List[int], cases: List[List[int]]):
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"{t}\n")
        for n, arr in zip(ns, cases):
            f.write(f"{n}\n")
            if n:
                f.write(" ".join(map(str, arr)) + "\n")


def gen_random_partition(rng: random.Random, cap: int, t: int, min_n: int, max_n: int) -> List[int]:
    # Produce ns with sum <= cap, each in [min_n, max_n]
    budget = cap
    ns: List[int] = []
    for i in range(t):
        remain = t - i - 1
        # Leave at least min_n for each remaining test
        max_here = min(max_n, max(min_n, budget - remain * min_n))
        n_i = rng.randint(min_n, max_here)
        ns.append(n_i)
        budget -= n_i
    return ns


def gen_values(rng: random.Random, n: int, lo: int, hi: int) -> List[int]:
    return [rng.randint(lo, hi) for _ in range(n)]


def main():
    p = argparse.ArgumentParser(description="Generate 5 CP test files with constraints.")
    p.add_argument("outdir", help="Directory to write 1.in .. 5.in (e.g., data/contests/Cx/problems/A/testcases)")
    p.add_argument("--seed", type=int, default=None, help="RNG seed for reproducibility")
    p.add_argument("--cap", type=int, default=100_000, help="Sum of n cap for cases 1 and 2")
    p.add_argument("--min-n", dest="min_n", type=int, default=1, help="Minimum n per test")
    p.add_argument("--max-n", dest="max_n", type=int, default=100_000, help="Maximum n per test")
    p.add_argument("--val-lo", type=int, default=1, help="Minimum value for generated integers")
    p.add_argument("--val-hi", type=int, default=1_000_000_000, help="Maximum value for generated integers")
    args = p.parse_args()

    rng = random.Random(args.seed)
    os.makedirs(args.outdir, exist_ok=True)

    # Case 1: random t, sum n <= cap
    t1 = rng.randint(1, 20)
    ns1 = gen_random_partition(rng, args.cap, t1, args.min_n, min(args.max_n, args.cap))
    cases1 = [gen_values(rng, n, args.val_lo, args.val_hi) for n in ns1]
    write_case_file(os.path.join(args.outdir, "1.in"), t1, ns1, cases1)

    # Case 2: similar to case 1, different seed path
    t2 = rng.randint(1, 20)
    ns2 = gen_random_partition(rng, args.cap, t2, args.min_n, min(args.max_n, args.cap))
    cases2 = [gen_values(rng, n, args.val_lo, args.val_hi) for n in ns2]
    write_case_file(os.path.join(args.outdir, "2.in"), t2, ns2, cases2)

    # Case 3: TLE-stressor: t=1, n=max_n (default 1e5)
    n3 = min(args.max_n, 100_000)
    t3 = 1
    ns3 = [n3]
    cases3 = [gen_values(rng, n3, args.val_lo, args.val_hi)]
    write_case_file(os.path.join(args.outdir, "3.in"), t3, ns3, cases3)

    # Case 4: corner cases pack
    corners4: List[List[int]] = []
    ns4: List[int] = []
    # n=1 min
    ns4.append(1); corners4.append([args.val_lo])
    # n=1 max
    ns4.append(1); corners4.append([args.val_hi])
    # n=2 duplicates
    ns4.append(2); corners4.append([args.val_lo, args.val_lo])
    # n=3 strictly increasing small
    inc3 = [args.val_lo, min(args.val_lo + 1, args.val_hi), min(args.val_lo + 2, args.val_hi)]
    ns4.append(len(inc3)); corners4.append(inc3)
    # n=3 all max
    ns4.append(3); corners4.append([args.val_hi] * 3)
    write_case_file(os.path.join(args.outdir, "4.in"), len(ns4), ns4, corners4)

    # Case 5: more edge patterns
    corners5: List[List[int]] = []
    ns5: List[int] = []
    # alternating extremes
    alt_len = 10
    ns5.append(alt_len); corners5.append([args.val_lo if i % 2 == 0 else args.val_hi for i in range(alt_len)])
    # all equal mid
    mid = (args.val_lo + args.val_hi) // 2
    ns5.append(10); corners5.append([mid] * 10)
    # min/max pair
    ns5.append(2); corners5.append([args.val_lo, args.val_hi])
    # singletons
    ns5.append(1); corners5.append([args.val_lo])
    ns5.append(1); corners5.append([args.val_hi])
    write_case_file(os.path.join(args.outdir, "5.in"), len(ns5), ns5, corners5)

    print(f"Generated testcases in {args.outdir} -> 1.in .. 5.in")


if __name__ == "__main__":
    main()

