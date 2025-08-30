#include <stdio.h>

int mod(int n) {
if ( n > 0) return n;
else return -n;
}

int main() {
int a, b;
scanf("%d %d", &a, &b);
printf("%d", mod(a - b));

return 0;

}