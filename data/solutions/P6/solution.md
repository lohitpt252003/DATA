## Problem Description

## Simple Answer

## Detailed Explanation

### Input/Output Format

### Constraints and Data Types

### Python

### C++

### C

## Problem Description

## Simple Answer

The approach is to simulate manual subtraction, digit by digit, from right to left, handling borrowing. This is necessary because standard integer types cannot hold numbers as large as $10^{1e5}$.

## Detailed Explanation

To subtract two very large numbers, we simulate manual subtraction, digit by digit, from right to left, handling borrowing. This approach is necessary because standard integer types in most programming languages cannot hold numbers as large as $10^{1e5}$. Therefore, the numbers are typically processed as sequences of digits (e.g., strings or arrays of integers).

### Input/Output Format
The input consists of two lines, each containing a non-negative integer ($a$ and $b$). The output should be a single line containing their difference ($a - b$). Since the numbers can be very large, they are typically read and printed as strings.

### Constraints and Data Types
The problem specifies that $a$ and $b$ are less than $10^{1e5}$. This means they can have up to $10^5$ digits. Standard integer types (like `int` or `long long` in C/C++) cannot store such large numbers, as they typically handle up to about 18-19 digits. Therefore, the numbers must be handled as strings or arrays of digits. Python's arbitrary-precision integers can handle these numbers directly, but the problem often implies implementing the subtraction logic manually.

### Python
Python's arbitrary-precision integers simplify this problem significantly, as `int` can handle numbers of any size. The solution simply involves converting the input strings to integers and performing the subtraction directly.

```python
def solve():
    a = int(input())
    b = int(input())
    print(a - b)

solve()
```

### C++
In C++, we can use `std::string` to represent the numbers. The core idea is to implement subtraction similar to how it's done manually. We need to handle signs, compare magnitudes, and then perform digit-by-digit subtraction with borrowing. The `std::reverse` from `<algorithm>` is useful for processing digits from right to left.

```cpp
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
```

### C
In C, we use character arrays (`char[]`) to store the numbers. String manipulation functions like `strlen` and manual iteration are necessary. We need to handle memory allocation and deallocation carefully using `malloc` and `free`. The core logic involves comparing magnitudes, handling signs, and performing digit-by-digit subtraction with borrowing.

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

// Function to check if num1 is smaller than num2 (for positive numbers)
bool isSmaller(char* num1, char* num2) {
    int n1 = strlen(num1), n2 = strlen(num2);
    if (n1 < n2) return true;
    if (n1 > n2) return false;
    for (int i = 0; i < n1; i++) {
        if (num1[i] < num2[i]) return true;
        else if (num1[i] > num2[i]) return false;
    }
    return false;
}

// Function to reverse a string
void strrev(char *str) {
    int len = strlen(str);
    int i = 0, j = len - 1;
    char temp;
    while (i < j) {
        temp = str[i];
        str[i] = str[j];
        str[j] = temp;
        i++;
        j--;
    }
}

// Function to subtract two positive numbers represented as strings
// Assumes num1 >= num2
char* subtractPositive(char* num1, char* num2) {
    char* str = (char*)malloc(sizeof(char) * (strlen(num1) + 2)); // +1 for null terminator, +1 for potential sign
    int k = 0;
    int n1 = strlen(num1), n2 = strlen(num2);
    
    // Reverse both strings
    char* rev_num1 = strdup(num1);
    char* rev_num2 = strdup(num2);
    strrev(rev_num1);
    strrev(rev_num2);

    int carry = 0;
    for (int i = 0; i < n2; i++) {
        int sub = ((rev_num1[i] - '0') - (rev_num2[i] - '0') - carry);
        if (sub < 0) {
            sub = sub + 10;
            carry = 1;
        } else {
            carry = 0;
        }
        str[k++] = sub + '0';
    }

    for (int i = n2; i < n1; i++) {
        int sub = ((rev_num1[i] - '0') - carry);
        if (sub < 0) {
            sub = sub + 10;
            carry = 1;
        } else {
            carry = 0;
        }
        str[k++] = sub + '0';
    }
    str[k] = '\0';

    strrev(str);

    // Remove leading zeros
    int i = 0;
    while (i < k - 1 && str[i] == '0') {
        i++;
    }
    char* result = strdup(str + i);
    free(str);
    free(rev_num1);
    free(rev_num2);
    return result;
}

// Placeholder for large number subtraction in C
// This is a simplified placeholder. Full implementation requires careful handling of signs and magnitudes.
char* subtract(char* num1_orig, char* num2_orig) {
    char* num1 = strdup(num1_orig);
    char* num2 = strdup(num2_orig);
    char* result_str;
    bool negative = false;

    // Remove leading zeros
    int i = 0;
    while (num1[i] == '0' && num1[i+1] != '\0') i++;
    char* temp_num1 = strdup(num1 + i);
    free(num1);
    num1 = temp_num1;

    i = 0;
    while (num2[i] == '0' && num2[i+1] != '\0') i++;
    char* temp_num2 = strdup(num2 + i);
    free(num2);
    num2 = temp_num2;

    if (strcmp(num1, num2) == 0) {
        free(num1);
        free(num2);
        return strdup("0");
    }

    // Determine the sign of the result
    if (isSmaller(num1, num2)) {
        char* temp = num1;
        num1 = num2;
        num2 = temp;
        negative = true;
    }

    result_str = subtractPositive(num1, num2);

    if (negative) {
        char* temp_result = (char*)malloc(strlen(result_str) + 2);
        sprintf(temp_result, "-%s", result_str);
        free(result_str);
        result_str = temp_result;
    }
    free(num1);
    free(num2);
    return result_str;
}

int main() {
    char a_str[1000], b_str[1000]; // Increased buffer size for large numbers
    scanf("%s %s", a_str, b_str);
    char* result = subtract(a_str, b_str);
    printf("%s\n", result);
    free(result);
    return 0;
}
```
