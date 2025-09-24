#include <stdio.h>

int main() {
    int t;  
    scanf("%d", &t);  // read number of testcases
    
    while (t--) {
        long long n;  
        scanf("%lld", &n);  // read the number
        
        if (n % 2 == 0) {
            printf("EVEN\n");  // n divisible by 2 → EVEN
        } else {
            printf("ODD\n");   // n not divisible by 2 → ODD
        }
    }
    return 0;
}