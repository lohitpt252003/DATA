# Problem 2: Subtract - Solution Explanation

## Problem Description

The problem asks us to find the absolute difference between two integers, `a` and `b`.



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

Similar to Problem 1, `a` and `b` are less than $10^{17}$. Their difference `a - b` could therefore be up to approximately $2$ 	times $10^{17}$. Standard 64-bit integer types (like `long long` in C/C++) are necessary to prevent overflow before taking the absolute value. Python's arbitrary-precision integers are also suitable choices.

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
