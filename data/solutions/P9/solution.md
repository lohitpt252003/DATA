## Problem Description

You are given a positive integer `n`.
Your task is to print all the **divisors** of `n` in **ascending order**.

## Simple Answer

The solution finds all divisors by iterating up to the square root of the given number `n`.

## Solution Approach

The solution iterates up to the square root of `n`, finding pairs of divisors.

## Detailed Explanation

The problem asks us to find all divisors of a given positive integer `n` and print them in ascending order.

A naive approach would be to iterate from 1 to `n` and check for divisibility at each step. However, with `n` up to 10^9, this would be too slow (O(n) complexity).

A more efficient approach is to iterate from 1 up to the square root of `n`. The key observation is that divisors come in pairs. If `i` is a divisor of `n`, then `n/i` is also a divisor.

### Algorithm:

1.  Read the integer `n`.
2.  Create a set to store the divisors to avoid duplicates. A set is used because if `n` is a perfect square, say `n = i*i`, then `i` and `n/i` are the same, and we should only include it once.
3.  Iterate with a loop variable `i` from 1 up to `floor(sqrt(n))`.
4.  In each iteration, check if `i` divides `n` evenly (`n % i == 0`).
    *   If it does, add both `i` and `n/i` to the set of divisors.
5.  After the loop finishes, the set will contain all the divisors of `n`.
6.  Convert the set to a list and sort it in ascending order.
7.  Print the elements of the sorted list, separated by spaces.

This approach has a time complexity of O(sqrt(n)), which is efficient enough for the given constraints. For `n = 10^9`, `sqrt(n)` is approximately 31622, which is well within typical time limits.

### Python
```python
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
```