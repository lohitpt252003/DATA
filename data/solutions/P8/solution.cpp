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

