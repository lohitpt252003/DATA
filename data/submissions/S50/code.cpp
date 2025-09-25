#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t); // Read number of test cases

    while (t--) {
        long long n;
        scanf("%lld", &n); // Read long long integer

        if (n % 2 == 0) {
            printf("EVEN\n");
        } else {
            printf("ODD\n");
        }
    }

    return 0;
}
