# Solution for P11 - Euclidean Algorithm

The problem asks to find the greatest common divisor (GCD) of two integers. The most efficient way to do this is by using the Euclidean algorithm.

## The Euclidean Algorithm

The Euclidean algorithm is an efficient method for computing the greatest common divisor (GCD) of two integers, the largest number that divides them both without leaving a remainder.

The algorithm is based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number. This process is repeated until the two numbers become equal. This is the GCD.

A more efficient implementation of the algorithm uses the remainder of the division of the larger number by the smaller one. The process is as follows:

1.  Given two integers `a` and `b`, where `a > b >= 0`.
2.  If `b` is 0, the GCD is `a`.
3.  Otherwise, the GCD is the GCD of `b` and `a % b` (the remainder of `a` divided by `b`).

This can be implemented recursively or iteratively.

### Recursive Implementation (Python)

```python
def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)
```

### Iterative Implementation (Python)

```python
def gcd(a, b):
  while b:
    a, b = b, a % b
  return a
```
