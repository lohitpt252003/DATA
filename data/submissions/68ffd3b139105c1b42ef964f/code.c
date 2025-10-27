#include <stdio.h>
#include <math.h>
#include <stdbool.h>

bool is_prime(long long n) {
    if (n < 2) return false;
    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    long long n;
    scanf("%lld", &n);
    if (is_prime(n))
        printf("prime\n");
    else
        printf("not prime\n");
    return 0;
}