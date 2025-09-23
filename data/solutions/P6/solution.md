# Solution for Max of Three

## Problem Description

The problem asks us to find the largest of three given integers. We can solve this by reading the three integers and using a series of conditional statements (if-else) or by using the built-in `max` function in many programming languages.

## Logic

1. Read the three integers, let's call them `a`, `b`, and `c`.
2. Compare `a` with `b` and `c`. If `a` is greater than or equal to both `b` and `c`, then `a` is the largest.
3. If not, compare `b` with `a` and `c`. If `b` is greater than or equal to both `a` and `c`, then `b` is the largest.
4. Otherwise, `c` must be the largest.

A simpler approach is to use the `max` function, which is available in most languages. For example, in Python, you can simply do `max(a, b, c)`.

## Simple Answer

Read the three integers and use the `max` function to find the largest one. Then print the result.

## Detailed Explanation

The `max` function is a built-in function in many programming languages that returns the largest of the input values. In this problem, we can use it to find the largest of the three integers. The function takes the three integers as arguments and returns the largest one. We then print the result to the standard output.

## Code

### Python

```python
a, b, c = map(int, input().split())
print(max(a, b, c))
```

### C

```c
#include <stdio.h>

int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    if (a >= b && a >= c) {
        printf("%d\n", a);
    } else if (b >= a && b >= c) {
        printf("%d\n", b);
    } else {
        printf("%d\n", c);
    }
    return 0;
}
```

### C++

```cpp
#include <iostream>
#include <algorithm>

int main() {
    int a, b, c;
    std::cin >> a >> b >> c;
    std::cout << std::max({a, b, c}) << std::endl;
    return 0;
}
```
