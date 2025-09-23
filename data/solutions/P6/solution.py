t = int(input())  # read number of testcases
for _ in range(t):
    n = int(input())  # read the number
    if n % 2 == 0:
        print("EVEN")  # divisible by 2 → EVEN
    else:
        print("ODD")   # not divisible by 2 → ODD
