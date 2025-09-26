
import sys

def solve():
    try:
        # Read the number of elements
        n_str = sys.stdin.readline()
        if not n_str: return
        n = int(n_str)
        
        # Read the array elements
        arr = list(map(int, sys.stdin.readline().split()))

        # Calculate the total sum of the array
        total_sum = sum(arr)

        # The condition for a valid partition to exist is that the total sum of the array is divisible by 3.
        # Let the sums of the three segments be s1, s2, s3.
        # The total sum S = s1 + s2 + s3.
        # The sum of the modulo values is (s1%3 + s2%3 + s3%3) % 3.
        # This must be equal to S % 3.
        # If the three modulo values are equal to s, then (3*s)%3 = 0.
        # If the three modulo values are a permutation of {0, 1, 2}, then (0+1+2)%3 = 0.
        # In both valid cases, the sum of the modulo values is 0.
        # Therefore, the total sum of the array must be divisible by 3.
        # It can be shown that this condition is also sufficient for n >= 3.
        if total_sum % 3 == 0:
            print("YES")
        else:
            print("NO")

    except (IOError, ValueError):
        return

# It's a single test case problem based on the provided format.
# If there were multiple test cases, a loop would be needed here.
solve()

