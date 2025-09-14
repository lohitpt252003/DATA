a = input()
b = input()

def addStrings(a: str, b: str) -> str:
    res = []
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    while i >= 0 or j >= 0 or carry:
        n1 = int(a[i]) if i >= 0 else 0
        n2 = int(b[j]) if j >= 0 else 0
        
        current_sum = n1 + n2 + carry
        carry = current_sum // 10
        res.append(str(current_sum % 10))
        
        i -= 1
        j -= 1
    return "".join(res[::-1])

print(addStrings(a, b))