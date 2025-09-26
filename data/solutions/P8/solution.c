#include <stdio.h>

int main() {
    int n;
    while (scanf("%d", &n) != EOF) {
        long long total_sum = 0;
        for (int i = 0; i < n; ++i) {
            long long val;
            scanf("%lld", &val);
            total_sum += val;
        }

        if (total_sum % 3 == 0) {
            printf("YES\n");
        } else {
            printf("NO\n");
        }
    }
    return 0;
}

