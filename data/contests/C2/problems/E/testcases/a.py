tests = []

import random

# TLE CASES
t = []
for i in range(20000):
    t.append(random.randint(1, 10**18))

tests.append(t)

# RANDOM CASES
for _ in range(5):
    t = []
    n = random.randint(1, 20000)
    for i in range(n):
        t.append(random.randint(1, 10**18))
    tests.append(t)

for _ in range(len(tests)):
    with open(f"{_ + 1}.in", 'w') as f:
        t = tests[_]
        f.write(f"{len(t)}\n")
        for x in t:
            f.write(f"{x}\n")