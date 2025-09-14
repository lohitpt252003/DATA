#include <iostream>
#include <string>
#include <algorithm> // For std::reverse

std::string addStrings(std::string num1, std::string num2) {
    std::string res = "";
    int i = num1.length() - 1, j = num2.length() - 1, carry = 0;
    while (i >= 0 || j >= 0 || carry) {
        int n1 = (i >= 0) ? num1[i--] - '0' : 0;
        int n2 = (j >= 0) ? num2[j--] - '0' : 0;
        int sum = n1 + n2 + carry;
        res += std::to_string(sum % 10);
        carry = sum / 10;
    }
    std::reverse(res.begin(), res.end());
    return res;
}

int main() {
    std::string num1, num2;
    std::cin >> num1 >> num2;
    std::cout << addStrings(num1, num2) << std::endl;
    return 0;
}