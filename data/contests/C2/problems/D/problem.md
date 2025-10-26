## C. Product of Three Numbers

Time limit: 2.00 s  
Memory limit: 256 MB

### Problem

You are given one integer number `n`.  
Find three **distinct integers** `a`, `b`, `c` such that `2 ≤ a, b, c` and `a · b · c = n`, or say that it is impossible to do so.

If there are several answers, you can print any.

You have to answer `t` independent test cases.

### Input

The first line of the input contains one integer `t` (`1 ≤ t ≤ 100`) — the number of test cases.  
Each of the next `t` lines contains one integer `n` (`2 ≤ n ≤ 10^9`).

### Output

For each test case, print the answer.

- Print `NO` if it is impossible to represent `n` as `a · b · c` for some distinct integers `a`, `b`, `c` such that `2 ≤ a, b, c`.
- Otherwise, print `YES` and any possible such representation.

### Example

**Input**
5
64
32
97
2
12345

**Output**

YES
2 4 8
NO
NO
NO
YES
3 5 823
