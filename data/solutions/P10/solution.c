#include <stdio.h>
#include <string.h>

int main() {
    long long n, k;
    scanf("%lld %lld", &n, &k);
    char s[100001];
    scanf("%s", s);

    if (k == 0) {
        printf("-1\n");
        return 0;
    }

    long long res = 0;
    long long power = 1;
    for (int i = n - 1; i >= 0; i--) {
        if (s[i] == '1') {
            res = (res + power) % k;
        }
        power = (power * 2) % k;
    }

    printf("%lld\n", res);

    return 0;
}