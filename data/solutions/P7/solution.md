## Problem Description

You are given an array of integers `arr` of length `n` and an integer `k`.
Your task is to determine whether there exists a **non-empty subset** of `arr` such that the product of its elements is divisible by `k`.

## Simple Answer

The solution uses dynamic programming on the prime factors of `k` to check if a subset product divisible by `k` can be formed.

## Solution Approach

The solution uses dynamic programming. We keep track of the powers of prime factors of `k` that can be formed by the product of subsets of the array processed so far.

## Detailed Explanation

The problem asks if there exists a non-empty subset of an array `arr` whose product is divisible by `k`.

A number is divisible by `k` if its prime factorization contains all the prime factors of `k` with at least the same powers. Let the prime factorization of `k` be $k = p_1^{a_1} p_2^{a_2} \cdots p_m^{a_m}$.

We can use dynamic programming to solve this problem. Let `dp` be a set of tuples, where each tuple `(b_1, b_2, ..., b_m)` represents the powers of the prime factors `(p_1, p_2, ..., p_m)` of `k` that can be achieved by the product of some subset of the elements of `arr` processed so far. The powers are capped at the required powers `(a_1, a_2, ..., a_m)`.

The state of our DP will be `dp`, a set of tuples representing the achieved powers of the prime factors of `k`. Initially, `dp` contains a single tuple of all zeros, `(0, 0, ..., 0)`, representing the product of an empty set (which is 1).

We iterate through each number `x` in the input array `arr`. For each `x`, we calculate the powers of the prime factors of `k` that `x` contributes. Let these powers be `(c_1, c_2, ..., c_m)`.

Then, for each existing state `(b_1, b_2, ..., b_m)` in `dp`, we create a new state by adding the contributed powers from `x`:
`(min(b_1 + c_1, a_1), min(b_2 + c_2, a_2), ..., min(b_m + c_m, a_m))`
We add this new state to our `dp` set.

If at any point the tuple `(a_1, a_2, ..., a_m)` becomes part of our `dp` set, it means we have found a subset whose product is divisible by `k`, and we can terminate and print "YES".

If we process all the numbers in `arr` and the target tuple is not in `dp`, then no such subset exists, and we print "NO".

### Algorithm:

1.  Find the prime factorization of `k`: $k = p_1^{a_1} p_2^{a_2} \cdots p_m^{a_m}$. Store the primes `(p_1, ..., p_m)` and their target powers `(a_1, ..., a_m)`.
2.  Initialize a set `dp` with a single tuple `(0, 0, ..., 0)`.
3.  For each number `x` in `arr`:
    a. For each prime `p_i` in the factorization of `k`, calculate its power `c_i` in `x`.
    b. Create a new set `new_dp` from `dp`.
    c. For each tuple `(b_1, ..., b_m)` in `dp`:
        i. Create a new tuple `(min(b_1 + c_1, a_1), ..., min(b_m + c_m, a_m))`.
        ii. Add the new tuple to `new_dp`.
    d. Update `dp = new_dp`.
    e. If the tuple `(a_1, ..., a_m)` is in `dp`, print "YES" and terminate.
4.  If the loop finishes, print "NO".

The number of states in `dp` is at most the number of divisors of `k`, which can be large but is manageable for the given constraints in typical competitive programming scenarios.

### Python
```python
import math

def get_prime_factorization(n):
    factors = {}
    d = 2
    temp_n = n
    while d * d <= temp_n:
        if temp_n % d == 0:
            count = 0
            while temp_n % d == 0:
                count += 1
                temp_n //= d
            factors[d] = count
        d += 1
    if temp_n > 1:
        factors[temp_n] = 1
    return factors

def solve():
    try:
        while True:
            n, k = map(int, input().split())
            arr = list(map(int, input().split()))

            if k == 1:
                print("YES")
                continue

            k_factors = get_prime_factorization(k)
            
            primes = list(k_factors.keys())
            target_powers = tuple(k_factors.values())

            dp = {tuple([0] * len(primes))}

            for x in arr:
                g_powers = []
                for p in primes:
                    power_in_x = 0
                    temp_x = x
                    while temp_x > 0 and temp_x % p == 0:
                        power_in_x += 1
                        temp_x //= p
                    g_powers.append(power_in_x)
                
                new_dp = dp.copy()
                for powers_t in dp:
                    new_powers = []
                    for i in range(len(primes)):
                        new_powers.append(min(powers_t[i] + g_powers[i], target_powers[i]))
                    
                    new_dp.add(tuple(new_powers))
                dp = new_dp

                if target_powers in dp:
                    break
            
            if target_powers in dp:
                print("YES")
            else:
                print("NO")
    except (IOError, EOFError):
        pass

solve()
```
### C++
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <map>
#include <set>
#include <algorithm>

// Function to get prime factorization of a number
std::map<long long, int> get_prime_factorization(long long n) {
    std::map<long long, int> factors;
    for (long long i = 2; i * i <= n; ++i) {
        if (n % i == 0) {
            int count = 0;
            while (n % i == 0) {
                n /= i;
                count++;
            }
            factors[i] = count;
        }
    }
    if (n > 1) {
        factors[n] = 1;
    }
    return factors;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    long long n, k;
    while (std::cin >> n >> k) {
        std::vector<long long> arr(n);
        for (int i = 0; i < n; ++i) {
            std::cin >> arr[i];
        }

        if (k == 1) {
            std::cout << "YES\n";
            continue;
        }

        auto k_factors = get_prime_factorization(k);
        std::vector<long long> primes;
        std::vector<int> target_powers;
        for (auto const& [p, a] : k_factors) {
            primes.push_back(p);
            target_powers.push_back(a);
        }

        std::set<std::vector<int>> dp;
        dp.insert(std::vector<int>(primes.size(), 0));

        bool found = false;
        for (long long x : arr) {
            std::vector<int> g_powers;
            for (long long p : primes) {
                int power_in_x = 0;
                long long temp_x = x;
                while (temp_x > 0 && temp_x % p == 0) {
                    power_in_x++;
                    temp_x /= p;
                }
                g_powers.push_back(power_in_x);
            }

            std::set<std::vector<int>> new_dp = dp;
            for (const auto& powers_v : dp) {
                std::vector<int> new_powers;
                for (size_t i = 0; i < primes.size(); ++i) {
                    new_powers.push_back(std::min(powers_v[i] + g_powers[i], target_powers[i]));
                }
                new_dp.insert(new_powers);
            }
            dp = new_dp;

            if (dp.count(target_powers)) {
                found = true;
                break;
            }
        }

        if (found) {
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
// C solution is omitted due to complexity of implementing dynamic programming with hash maps and sets.
```