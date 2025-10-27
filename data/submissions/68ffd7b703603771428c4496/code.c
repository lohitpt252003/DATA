#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    if (n < 2) {
        printf("not prime\n");
        return 0;
    }
    int is_prime = 1;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            is_prime = 0;
            break;
        }
    }
    if (is_prime) {
        printf("prime\n");
    } else {
        printf("not prime\n");
    }
    return 0;
}