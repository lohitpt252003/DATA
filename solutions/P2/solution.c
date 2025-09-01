#include <stdio.h>
#include <stdlib.h> // For abs

int main() {
    long long a, b;
    scanf("%lld %lld", &a, &b);
    printf("%lld\n", labs(a - b)); // labs for long long absolute value
    return 0;
}
