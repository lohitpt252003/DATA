# Problem 1: Add - Solution Explanation

## Problem Description

The problem asks us to read two integers, `a` and `b`, and print their sum.

## Simple Answer

The solution is straightforward: read the two numbers and output their sum. This directly implements the definition of addition.

## Detailed Explanation

### Approach

To solve this problem, we need to perform a basic arithmetic operation: addition. The process can be broken down into three logical steps:

1.  **Input Acquisition:** The first step is to obtain the two integers, `a` and `b`, from the user or the testing environment. These are typically provided via standard input.

2.  **Computation:** Once `a` and `b` are available, their sum is calculated. This is a fundamental operation supported directly by all programming languages.

3.  **Output Presentation:** Finally, the computed sum must be displayed to the user or recorded for verification. This is typically done by writing to standard output.

### Constraints and Data Types

The problem specifies that `a` and `b` can range from -10^9 to 10^9. The sum `a + b` could therefore range from -2 * 10^9 to 2 * 10^9. Standard 32-bit integer types (like `int` in C/C++ on many systems) might overflow for this range. Therefore, it is crucial to use data types that can accommodate values up to 2 * 10^9. `long long` in C/C++ and Python's arbitrary-precision integers are suitable choices.

### Language-Specific Implementations

#### Python (`solution.py`)

Python's integers handle arbitrary precision automatically, so overflow is not a concern. The `input().split()` method reads the line, and `map(int, ...)` converts the parts to integers. The `print()` function then outputs the sum.

```python
a, b = map(int, input().split())
print(a + b)
```

#### C++ (`solution.cpp`)

In C++, `long long` is used for `a` and `b` to prevent overflow. `std::cin` and `std::cout` are used for input/output. The `std::endl` flushes the output buffer and adds a newline.

```cpp
#include <iostream>

int main() {
    long long a, b;
    std::cin >> a >> b;
    std::cout << a + b << std::endl;
    return 0;
}
```

#### C (`solution.c`)

In C, `long long` is also used for `a` and `b`. `scanf` with the `%lld` format specifier reads the input, and `printf` with `%lld` prints the sum, followed by a newline character `\n`.

```c
#include <stdio.h>

int main() {
    long long a, b;
    scanf("%lld %lld", &a, &b);
    printf("%lld\n", a + b);
    return 0;
}
```