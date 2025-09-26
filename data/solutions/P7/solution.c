#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

#define MAX_PRIME_FACTORS 15
#define MAX_DP_STATES 150000

int dp[MAX_DP_STATES][MAX_PRIME_FACTORS];
int dp_size = 0;

typedef struct {
    long long prime;
    int power;
} PrimeFactor;

typedef struct {
    PrimeFactor factors[MAX_PRIME_FACTORS];
    int count;
} PrimeFactorization;

PrimeFactorization get_prime_factorization(long long n) {
    PrimeFactorization pf;
    pf.count = 0;
    long long temp_n = n;
    for (long long i = 2; i * i <= temp_n; ++i) {
        if (temp_n % i == 0) {
            int count = 0;
            while (temp_n % i == 0) {
                temp_n /= i;
                count++;
            }
            if (pf.count < MAX_PRIME_FACTORS) {
                pf.factors[pf.count].prime = i;
                pf.factors[pf.count].power = count;
                pf.count++;
            }
        }
    }
    if (temp_n > 1) {
        if (pf.count < MAX_PRIME_FACTORS) {
            pf.factors[pf.count].prime = temp_n;
            pf.factors[pf.count].power = 1;
            pf.count++;
        }
    }
    return pf;
}

int main() {
    long long n, k;
    while (scanf("%lld %lld", &n, &k) != EOF) {
        long long *arr = (long long *)malloc(sizeof(long long) * n);
        for (int i = 0; i < n; ++i) {
            scanf("%lld", &arr[i]);
        }

        if (k == 1) {
            printf("YES\n");
            free(arr);
            continue;
        }

        PrimeFactorization k_factors = get_prime_factorization(k);
        int num_primes = k_factors.count;

        dp_size = 1;
        for(int i=0; i<num_primes; ++i) dp[0][i] = 0;

        int found = 0;
        for (int i = 0; i < n; ++i) {
            long long x = arr[i];
            int g_powers[MAX_PRIME_FACTORS] = {0};
            for (int j = 0; j < num_primes; ++j) {
                long long p = k_factors.factors[j].prime;
                int power_in_x = 0;
                long long temp_x = x;
                while (temp_x > 0 && temp_x % p == 0) {
                    power_in_x++;
                    temp_x /= p;
                }
                g_powers[j] = power_in_x;
            }

            int current_dp_size = dp_size;
            for (int j = 0; j < current_dp_size; ++j) {
                int new_powers[MAX_PRIME_FACTORS];
                int is_target = 1;
                for (int l = 0; l < num_primes; ++l) {
                    new_powers[l] = dp[j][l] + g_powers[l];
                    if (new_powers[l] > k_factors.factors[l].power) {
                        new_powers[l] = k_factors.factors[l].power;
                    }
                    if (new_powers[l] < k_factors.factors[l].power) {
                        is_target = 0;
                    }
                }

                int exists = 0;
                for (int l = 0; l < dp_size; ++l) {
                    if (memcmp(dp[l], new_powers, sizeof(int) * num_primes) == 0) {
                        exists = 1;
                        break;
                    }
                }

                if (!exists) {
                    if (dp_size < MAX_DP_STATES) {
                        memcpy(dp[dp_size], new_powers, sizeof(int) * num_primes);
                        dp_size++;
                    }
                }
                if(is_target) {
                    found = 1;
                    break;
                }
            }
            if (found) {
                break;
            }
        }

        if (found) {
            printf("YES\n");
        } else {
            printf("NO\n");
        }

        free(arr);
    }
    return 0;
}
