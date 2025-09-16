#include <stdio.h>

int main() {
    // Declare two variables of type long long int to hold large numbers.
    long long int a, b;
    
    // Read two space-separated long long integers from the input.
    scanf("%lld %lld", &a, &b);
    
    // Print their sum.
    printf("%lld\n", a + b);
    
    return 0;
}