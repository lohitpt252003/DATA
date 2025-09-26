You are given an array of integers `arr` of length `n`.
You need to partition the array into exactly **three contiguous segments**.

Let:

* $s1 = \left(\text{sum of elements in the first segment}\right) \bmod 3$
* $s2 = \left(\text{sum of elements in the second segment}\right) \bmod 3$
* $s3 = \left(\text{sum of elements in the third segment}\right) \bmod 3$

Your task is to print:

* `YES` if either

  1. $s1 = s2 = s3$, or
  2. $s1, s2, s3$ are all **pairwise different** (no two are equal).
* Otherwise, print `NO`.