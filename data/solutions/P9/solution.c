#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int main() {
    int n;
    while (scanf("%d", &n) != EOF) {
        int *divisors = (int *)malloc(sizeof(int) * 2000);
        int count = 0;
        for (int i = 1; i * i <= n; ++i) {
            if (n % i == 0) {
                divisors[count++] = i;
                if (i * i != n) {
                    divisors[count++] = n / i;
                }
            }
        }
        qsort(divisors, count, sizeof(int), compare);
        for (int i = 0; i < count; ++i) {
            printf("%d", divisors[i]);
            if (i < count - 1) {
                printf(" ");
            }
        }
        printf("\n");
        free(divisors);
    }
    return 0;
}