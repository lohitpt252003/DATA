import sys, math

def simple_sieve(limit):
    if limit < 2:
        return []
    mark = bytearray(b"\x01") * (limit + 1)
    mark[0:2] = b"\x00\x00"
    for i in range(2, int(math.isqrt(limit)) + 1):
        if mark[i]:
            start = i * i
            step = i
            mark[start:limit+1:step] = b"\x00" * (((limit - start)//step) + 1)
    return [i for i in range(2, limit + 1) if mark[i]]

def segmented(m, n, base):
    size = n - m + 1
    is_prime = bytearray(b"\x01") * size
    for p in base:
        p2 = p * p
        if p2 > n:
            break
        start = p2 if p2 >= m else ((m + p - 1)//p)*p
        for j in range(start, n + 1, p):
            is_prime[j - m] = 0
    if m == 1:
        is_prime[0] = 0
    return [str(m + i) for i, v in enumerate(is_prime) if v]

data = sys.stdin.read().strip().split()
it = iter(data)
t = int(next(it, 0))
pairs = [(int(next(it)), int(next(it))) for _ in range(t)]
maxn = max((b for _, b in pairs), default=1)
base = simple_sieve(int(math.isqrt(maxn)) + 1 if maxn >= 2 else 1)
out = []
for i, (m, n) in enumerate(pairs):
    out.extend(segmented(m, n, base))
    if i != t - 1:
        out.append("")
print("\n".join(out))