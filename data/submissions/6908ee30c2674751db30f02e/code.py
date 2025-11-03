def count_divisors(n):
    if n == 0:
        return 0
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if n // i == i:
                count += 1
            else:
                count += 2
    return count

def main():
    n = int(input())
    results = []
    for _ in range(n):
        x = int(input())
        results.append(str(count_divisors(x)))
    print("\n".join(results))

if __name__ == "__main__":
    main()