import sys
import math

def segmented_sieve(m, n):
    if n < 2:
        return []
    
    limit = int(math.sqrt(n)) + 1
    primes = []
    is_prime_small = [True] * limit
    if limit > 0:
        is_prime_small[0] = False
    if limit > 1:
        is_prime_small[1] = False

    for p in range(2, limit):
        if is_prime_small[p]:
            primes.append(p)
            for i in range(p * p, limit, p):
                is_prime_small[i] = False

    is_prime_segment = [True] * (n - m + 1)
    if m == 1 and len(is_prime_segment) > 0:
        is_prime_segment[0] = False

    for p in primes:
        start = max(p * p, ((m + p - 1) // p) * p)
        for i in range(start, n + 1, p):
            if i >= m and i - m < len(is_prime_segment):
                is_prime_segment[i - m] = False

    result = []
    for i in range(len(is_prime_segment)):
        if is_prime_segment[i]:
            result.append(m + i)
    
    return result

def main():
    try:
        num_test_cases = int(input())
        for i in range(num_test_cases):
            line = input()
            if line.strip() == "":
                line = input()
            m, n = map(int, line.split())
            
            primes = segmented_sieve(m, n)
            for p in primes:
                print(p)
            
            if i < num_test_cases - 1:
                print()

    except (IOError, ValueError):
        pass

if __name__ == "__main__":
    main()