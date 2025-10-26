## LCM Challenge (235A)

Time limit: 1.00 s  
Memory limit: 256 MB

### Problem

Given an integer n, find the maximum possible value of LCM(a, b, c) among all triples of integers a, b, c such that 1 ≤ a, b, c ≤ n.

### Input

The input contains a single integer n (1 ≤ n ≤ 10^9).

### Output

Print one integer — the maximum possible LCM(a, b, c).

### Sample

Input:

```
9
```

Output:

```
504
```

### Notes

Optimal solution uses math observations
The result may become very large, 32-bit integer won't be enough. So using 64-bit integers is recommended.