n = int(input())
arr = map(int, input().split())
print("YES" if sum(arr) % 3 == 0 else "NO")