def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

try:
    a, b = map(int, input().split())
    print(gcd(a, b))
except (ValueError, IndexError):
    pass