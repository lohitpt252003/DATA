n, k = map(int, input().split())
s = input()

if k == 0:
    print(-1)
else:
    res = 0
    power = 1
    for c in reversed(s):
        if c == '1':
            res = (res + power) % k
        power = (power * 2) % k
    print(res)
