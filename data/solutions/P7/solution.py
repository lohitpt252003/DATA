
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
