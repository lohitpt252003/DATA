
import math
import sys

def solve():
    try:
        # Read the integer n
        n_str = sys.stdin.readline()
        if not n_str: return
        n = int(n_str)

        divisors = set()
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                divisors.add(i)
                divisors.add(n // i)
        
        sorted_divisors = sorted(list(divisors))
        print(*sorted_divisors)

    except (IOError, ValueError):
        return

solve()
