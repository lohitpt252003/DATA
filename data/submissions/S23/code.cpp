#include <iostream>
#include <string>
#include <algorithm> // For std::reverse

std::string addStrings(std::string a, std::string b) {
    std::string res = "";
    int i = a.length() - 1, j = b.length() - 1, carry = 0;
    while (i >= 0 || j >= 0 || carry) {
        int n1 = (i >= 0) ? a[i--] - '0' : 0;
        int n2 = (j >= 0) ? b[j--] - '0' : 0;
        int sum = n1 + n2 + carry;
        res += std::to_string(sum % 10);
        carry = sum / 10;
    }
    std::reverse(res.begin(), res.end());
    return res;
}

int main() {
    std::string a, b;
    std::cin >> a >> b;
    std::cout << addStrings(a, b) << std::endl;
    return 0;
}