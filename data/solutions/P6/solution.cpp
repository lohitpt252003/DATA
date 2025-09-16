#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

// Function to check if num1 is smaller than num2 (for positive numbers)
bool isSmaller(std::string num1, std::string num2) {
    int n1 = num1.length(), n2 = num2.length();
    if (n1 < n2) return true;
    if (n1 > n2) return false;
    for (int i = 0; i < n1; i++) {
        if (num1[i] < num2[i]) return true;
        else if (num1[i] > num2[i]) return false;
    }
    return false;
}

// Function to subtract two positive numbers represented as strings
// Assumes num1 >= num2
std::string subtractPositive(std::string num1, std::string num2) {
    std::string str = "";
    int n1 = num1.length(), n2 = num2.length();
    std::reverse(num1.begin(), num1.end());
    std::reverse(num2.begin(), num2.end());

    int carry = 0;
    for (int i = 0; i < n2; i++) {
        int sub = ((num1[i] - '0') - (num2[i] - '0') - carry);
        if (sub < 0) {
            sub = sub + 10;
            carry = 1;
        } else {
            carry = 0;
        }
        str.push_back(sub + '0');
    }

    for (int i = n2; i < n1; i++) {
        int sub = ((num1[i] - '0') - carry);
        if (sub < 0) {
            sub = sub + 10;
            carry = 1;
        } else {
            carry = 0;
        }
        str.push_back(sub + '0');
    }

    std::reverse(str.begin(), str.end());

    // Remove leading zeros
    size_t first_digit = str.find_first_not_of('0');
    if (std::string::npos == first_digit) {
        return "0";
    }
    return str.substr(first_digit);
}

// Function to subtract two large numbers represented as strings
std::string subtract(std::string num1, std::string num2) {
    std::string result;
    bool negative = false;

    // Remove leading zeros
    size_t first_digit_num1 = num1.find_first_not_of('0');
    if (std::string::npos == first_digit_num1) num1 = "0";
    else num1 = num1.substr(first_digit_num1);

    size_t first_digit_num2 = num2.find_first_not_of('0');
    if (std::string::npos == first_digit_num2) num2 = "0";
    else num2 = num2.substr(first_digit_num2);

    if (num1 == num2) return "0";

    // Determine the sign of the result
    if (isSmaller(num1, num2)) {
        std::swap(num1, num2);
        negative = true;
    }

    result = subtractPositive(num1, num2);

    if (negative) result = "-" + result;
    return result;
}

int main() {
    std::string a_str, b_str;
    std::cin >> a_str >> b_str;
    std::cout << subtract(a_str, b_str) << std::endl;
    return 0;
}