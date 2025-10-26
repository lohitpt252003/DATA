## GCD of Pairwise LCMs

Time limit: 3.00 s  
Memory limit: 256 MB

### Problem

Given a sequence a of length n, define the multiset T = { lcm(ai, aj) | i < j } (LCMs of all unordered pairs). Compute gcd(T) — the greatest common divisor of all numbers in T.

### Input

The first line contains integer n (2 ≤ n ≤ 100000). The second line contains n integers a1..an (1 ≤ ai ≤ 200000).

### Output

Print one integer: `gcd({lcm({ai, aj}) | i < j})`

### Example

Input:

```
4
10 24 40 80
```

Output:

```
40
```
