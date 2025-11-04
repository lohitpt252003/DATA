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


def generate(outdir: str, seed: int | None = None,
             cap: int = 100_000, min_n: int = 1, max_n: int = 100_000,
             val_lo: int = -1_000_000_000, val_hi: int = 1_000_000_000) -> None:
    rng = random.Random(seed)
    os.makedirs(outdir, exist_ok=True)

    # Case 1: random t, sum n <= cap
    t1 = rng.randint(1, 20)
    ns1 = gen_random_partition(rng, cap, t1, min_n, min(max_n, cap))
    cases1 = [gen_values(rng, n, val_lo, val_hi) for n in ns1]
    write_case_file(os.path.join(outdir, "1.in"), t1, ns1, cases1)

    # Case 2: similar to case 1, different sampling
    t2 = rng.randint(1, 20)
    ns2 = gen_random_partition(rng, cap, t2, min_n, min(max_n, cap))
    cases2 = [gen_values(rng, n, val_lo, val_hi) for n in ns2]
    write_case_file(os.path.join(outdir, "2.in"), t2, ns2, cases2)

    # Case 3: TLE-stressor: t=1, n=1e5
    n3 = min(max_n, 100_000)
    t3 = 1
    ns3 = [n3]
    cases3 = [gen_values(rng, n3, val_lo, val_hi)]
    write_case_file(os.path.join(outdir, "3.in"), t3, ns3, cases3)

    # Case 4: curated corners (explicit negatives and zero included)
    corners4: List[List[int]] = []
    ns4: List[int] = []
    # n=1 min (likely negative)
    ns4.append(1); corners4.append([val_lo])
    # n=1 max
    ns4.append(1); corners4.append([val_hi])
    # n=1 zero
    ns4.append(1); corners4.append([0])
    # n=2 duplicates (negative)
    ns4.append(2); corners4.append([val_lo, val_lo])
    # n=3 strictly increasing small (may be negative to near zero)
    inc3 = [val_lo, min(val_lo + 1, val_hi), min(val_lo + 2, val_hi)]
    ns4.append(len(inc3)); corners4.append(inc3)
    # n=3 all max
    ns4.append(3); corners4.append([val_hi] * 3)
    write_case_file(os.path.join(outdir, "4.in"), len(ns4), ns4, corners4)

    # Case 5: more edges (negatives/zeros patterns)
    corners5: List[List[int]] = []
    ns5: List[int] = []
    # alternating extremes
    alt_len = 10
    ns5.append(alt_len); corners5.append([val_lo if i % 2 == 0 else val_hi for i in range(alt_len)])
    # all equal mid
    mid = (val_lo + val_hi) // 2
    ns5.append(10); corners5.append([mid] * 10)
    # min/max pair
    ns5.append(2); corners5.append([val_lo, val_hi])
    # singletons
    ns5.append(1); corners5.append([val_lo])
    ns5.append(1); corners5.append([val_hi])
    # all zeros
    ns5.append(10); corners5.append([0] * 10)
    # strictly increasing negatives
    ns5.append(5); corners5.append([-5, -4, -3, -2, -1])
    write_case_file(os.path.join(outdir, "5.in"), len(ns5), ns5, corners5)

    print(f"Generated testcases in {outdir}: 1.in .. 5.in")


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    # Deterministic default seed for reproducibility; change to None for fresh draws
    generate(here, seed=42)
