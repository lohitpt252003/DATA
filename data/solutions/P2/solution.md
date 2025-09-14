# Problem 2: Subtract - Solution Explanation

## Problem Description

The problem asks us to find the absolute difference between two integers, `a` and `b`.

**Note on Problem Statement Discrepancy:**

The provided problem statement for "Subtract" has some inconsistencies:
- The "Output" section incorrectly states to print the "sum of a and b".
- The "Example 1" and "Example 2" show outputs (`2` and `4`) that correspond to addition, not subtraction.
- The "Explanation" correctly describes subtraction (e.g., `1 - 1 = 0`).

Based on the problem title "Subtract" and the explicit mention of "absolute difference" in the description, the solutions below are implemented to calculate the absolute difference, disregarding the incorrect examples and output description.

## Simple Answer

Read the two numbers, calculate their difference, and then take the absolute value of that difference. Output the result.

## Detailed Explanation

### Concept of Absolute Difference

The absolute difference between two numbers, `a` and `b`, is the non-negative difference between them. It can be formally defined as $|a - b|$. This means if $a - b$ is positive, the result is $a - b$. If $a - b$ is negative, the result is $-(a - b)$, which is equivalent to $b - a$. Essentially, it's the distance between `a` and `b` on the number line, which is always a positive value.

### Approach

1.  **Input Acquisition:** Read the two integers, `a` and `b`, from standard input.

2.  **Difference Calculation:** Compute the difference between `a` and `b` (i.e., `a - b`).

3.  **Absolute Value:** Apply the absolute value function to the calculated difference. This ensures the result is always non-negative.

4.  **Output Presentation:** Print the final absolute difference to standard output.

### Constraints and Data Types

Similar to Problem 1, $a$ and $b$ can range from $-10^9$ to $10^9$. Their difference $a - b$ can range from $-2$ times $10^9$ to $2$ 	times $10^9$. Therefore, `long long` in C/C++ and Python's arbitrary-precision integers are necessary to prevent overflow before taking the absolute value.

### Language-Specific Implementations

#### Python (`solution.py`)

Python's `abs()` function directly computes the absolute value. The solution reads `a` and `b`, calculates `a - b`, and then applies `abs()` before printing.

```python
a, b = map(int, input().split())
print(abs(a - b))
```

#### C++ (`solution.cpp`)

In C++, `std::abs()` from the `<cmath>` header is used for `long long` types. The solution reads `a` and `b` using `std::cin`, computes `std::abs(a - b)`, and prints the result using `std::cout`.

```cpp
#include <iostream>
#include <cmath> // For std::abs

int main() {
    long long a, b;
    std::cin >> a >> b;
    std::cout << std::abs(a - b) << std::endl;
    return 0;
}
```

#### C (`solution.c`)

In C, `labs()` from the `<stdlib.h>` header is specifically designed for `long long` absolute values. The solution reads `a` and `b` using `scanf` and `%lld`, computes `labs(a - b)`, and prints the result using `printf` and `%lld`.

```c
#include <stdio.h>
#include <stdlib.h> // For labs

int main() {
    long long a, b;
    scanf("%lld %lld", &a, &b);
    printf("%lld\n", labs(a - b));
    return 0;
}
```
