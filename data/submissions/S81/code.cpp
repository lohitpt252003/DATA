#include <iostream>
#include <string>
#include <vector>

int main() {
    long long n, k;
    std::cin >> n >> k;
    std::string s;
    std::cin >> s;

    if (k == 0) {
        std::cout << -1 << std::endl;
        return 0;
    }

    long long res = 0;
    long long power = 1;

    for (int i = n - 1; i >= 0; i--) {
        if (s[i] == '1') {
            res = (res + power) % k;
        }
        power = (power * 2) % k;
    }

    std::cout << res << std::endl;

    return 0;
}