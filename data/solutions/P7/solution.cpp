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
