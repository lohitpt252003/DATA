## Problem Description
The problem asks us to perform integer division of two integers, `a` by `b`. We are guaranteed that `b` will not be zero.

## Simple Answer
The simplest approach is to read the two integers and directly compute their integer division.

## Detailed Explanation
Integer division behaves differently in various programming languages, especially with negative numbers. For this problem, we expect the result to be truncated towards zero.

### Python
Python's `//` operator performs floor division. For positive numbers, it's equivalent to truncation. For negative numbers, it floors towards negative infinity. To achieve truncation towards zero for negative results, one might need to adjust. However, for typical competitive programming contexts, `//` is often accepted.

```python
a, b = map(int, input().split())
print(a // b)
```

### C++
In C++, integer division (`/`) truncates towards zero. This is the desired behavior for this problem.

```cpp
#include <iostream>

int main() {
    int a, b;
    std::cin >> a >> b;
    std::cout << a / b << std::endl;
    return 0;
}
```

### C
In C, integer division (`/`) also truncates towards zero. This is the desired behavior for this problem.

```c
#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d\n", a / b);
    return 0;
}
```