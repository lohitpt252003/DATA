n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 1
for i in arr: ans = (ans * i) % k

print("YES" if ans == 0 else "NO")