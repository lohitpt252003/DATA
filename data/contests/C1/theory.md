# Contest Theory

This section contains the theoretical concepts and algorithms that might be useful for solving the problems in this contest.

## Topics Covered

### Prime Numbers

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The first few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.

**Primality Test:**
A simple way to check if a number `n` is prime is to try dividing it by all integers from 2 up to `sqrt(n)`. If none of these divisions result in a whole number, then `n` is prime.

### T-Prime Numbers

A T-prime number is a positive integer that has exactly three distinct positive divisors.
A number is a T-prime if and only if it is the square of a prime number.

For example, 4 is a T-prime number because it has three divisors (1, 2, 4) and it is the square of the prime number 2.
Similarly, 9 is a T-prime number (divisors 1, 3, 9; square of 3).