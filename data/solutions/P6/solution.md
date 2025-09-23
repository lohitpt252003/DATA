## Problem Description

The task is to determine whether a given number is odd or even for multiple test cases.
If the number is divisible by 2, it is EVEN; otherwise, it is ODD.

## Simple Answer

Check the remainder when dividing the number by 2:

* If remainder is 0 → EVEN
* Otherwise → ODD

## Detailed Explanation

### Approach

1. **Input Acquisition:**

   * First read the integer $t$, the number of test cases.
   * For each test case, read an integer $n$.

2. **Computation:**

   * Use the modulo operation (`n % 2`).
   * If the remainder is 0, print "EVEN"; otherwise, print "ODD".

3. **Output Presentation:**

   * For each test case, print the result on a new line.

### Constraints and Data Types

* $1 \leq t \leq 10^5$
* $0 \leq n \leq 10^{18}$

Since $n$ can be very large, we must use 64-bit integers (`long long` in C/C++). Python naturally supports big integers, so no special care is required.

### Language-Specific Implementations

#### Python (`solution.py`)

```python
t = int(input())  # number of testcases
for _ in range(t):
    n = int(input())  # read number
    if n % 2 == 0:
        print("EVEN")  # divisible by 2
    else:
        print("ODD")   # not divisible by 2
```

#### C++ (`solution.cpp`)

```cpp
#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;  // read number of testcases
    while (t--) {
        long long n;
        cin >> n;  // read number
        if (n % 2 == 0) cout << "EVEN" << endl;
        else cout << "ODD" << endl;
    }
    return 0;
}
```

#### C (`solution.c`)

```c
#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);  // number of testcases
    while (t--) {
        long long n;
        scanf("%lld", &n);  // read number
        if (n % 2 == 0) printf("EVEN\n");
        else printf("ODD\n");
    }
    return 0;
}
```
