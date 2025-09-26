## Problem Description

You are given an array of integers `arr` of length `n`.
You need to partition the array into exactly **three contiguous segments**.

Let:

* $s1 = \left(\text{sum of elements in the first segment}\right) \bmod 3$
* $s2 = \left(\text{sum of elements in the second segment}\right) \bmod 3$
* $s3 = \left(\text{sum of elements in the third segment}\right) \bmod 3$

Your task is to print:

* `YES` if either

  1. $s1 = s2 = s3$, or
  2. $s1, s2, s3$ are all **pairwise different** (no two are equal).
* Otherwise, print `NO`.

## Simple Answer

The solution checks if the total sum of the array is divisible by 3, which is a necessary and sufficient condition for a valid partition to exist.

## Solution Approach

The solution relies on a key mathematical observation about the sums of the segments modulo 3.

## Detailed Explanation

The problem requires us to determine if an array can be partitioned into three non-empty contiguous segments, such that the sums of elements in each segment, modulo 3, satisfy certain conditions. The conditions are that the three modulo values are either all equal or all pairwise different.

Let the three contiguous segments have sums `sum1`, `sum2`, and `sum3`. Let the modulo values be `s1 = sum1 % 3`, `s2 = sum2 % 3`, and `s3 = sum3 % 3`. The total sum of the array is `S = sum1 + sum2 + sum3`.

The sum of the modulo values, `(s1 + s2 + s3) % 3`, must be equal to the total sum modulo 3, `S % 3`.

Let's analyze the two valid conditions:
1.  `s1 = s2 = s3 = s`: In this case, `(s1 + s2 + s3) % 3 = (3 * s) % 3 = 0`.
2.  `{s1, s2, s3}` is a permutation of `{0, 1, 2}`: In this case, `(s1 + s2 + s3) % 3 = (0 + 1 + 2) % 3 = 3 % 3 = 0`.

In both valid cases, the sum of the modulo values is 0. This implies that a necessary condition for a valid partition to exist is that the total sum of the array must be divisible by 3.
`S % 3 = (s1 + s2 + s3) % 3 = 0`.

It turns out that this condition is not only necessary but also sufficient for an array of length `n >= 3`. The proof relies on the fact that if the total sum is divisible by 3, we have enough flexibility with two cut points to always find a valid partition. We can either find a prefix that sums to 0 mod 3, creating a `(0, s, -s)` partition which is always valid, or we can find two prefixes that create one of the other valid partitions.

Therefore, the solution simplifies to checking if the total sum of the array is divisible by 3.

### Algorithm:

1.  Calculate the sum of all elements in the array `arr`.
2.  If `sum(arr) % 3 == 0`, print "YES".
3.  Otherwise, print "NO".

This approach has a time complexity of O(n) to calculate the sum of the array, which is efficient enough for the given constraints.

### Python
```python
import sys

def solve():
    try:
        # Read the number of elements
        n_str = sys.stdin.readline()
        if not n_str: return
        n = int(n_str)
        
        # Read the array elements
        arr = list(map(int, sys.stdin.readline().split()))

        # Calculate the total sum of the array
        total_sum = sum(arr)

        if total_sum % 3 == 0:
            print("YES")
        else:
            print("NO")

    except (IOError, ValueError):
        return

solve()
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <numeric>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    int n;
    while (std::cin >> n) {
        std::vector<long long> arr(n);
        long long total_sum = 0;
        for (int i = 0; i < n; ++i) {
            std::cin >> arr[i];
            total_sum += arr[i];
        }

        if (total_sum % 3 == 0) {
            std::cout << "YES\n";
        } else {
            std::cout << "NO\n";
        }
    }
    return 0;
}
```

### C
```c
#include <stdio.h>

int main() {
    int n;
    while (scanf("%d", &n) != EOF) {
        long long total_sum = 0;
        for (int i = 0; i < n; ++i) {
            long long val;
            scanf("%lld", &val);
            total_sum += val;
        }

        if (total_sum % 3 == 0) {
            printf("YES\n");
        } else {
            printf("NO\n");
        }
    }
    return 0;
}
```