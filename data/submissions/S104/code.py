a = input()
b = input() 

a = '0' + a
b = '0' + b

n_a = len(a)
n_b = len(b)

if n_a >= n_b :
    for i in range(1, n_a - n_b + 1):
        b = '0' + b

if n_b >= n_a :
    for i in range(1, n_b - n_a + 1):
        a = '0' + a
        

l = len(a)
ans = ""
borrow = 0

for i in range(0, l):

    num = int(a[l-1 - i]) + int(b[l-1 - i]) + borrow
    ans = str(num % 10) + ans
    borrow = int(num / 10)


ans = ans.lstrip("0")
if not ans: ans = '0'


print(ans)