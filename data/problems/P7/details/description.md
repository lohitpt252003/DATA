You are given an array of integers `arr` of length `n` and an integer `k`.
Your task is to determine whether there exists a **non-empty subset** of `arr` such that the product of its elements is divisible by `k`.

Formally, check if there exists a subset `S` of indices such that:

$$
\left(\prod_{i \in S} arr[i]\right) \bmod k = 0
$$

If such a subset exists, print `YES`; otherwise, print `NO`.