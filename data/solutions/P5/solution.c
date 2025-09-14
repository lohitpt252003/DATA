#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Function to reverse a string
void reverse(char* str) {
    int len = strlen(str);
    int i, j;
    char temp;
    for (i = 0, j = len - 1; i < j; i++, j--) {
        temp = str[i];
        str[i] = str[j];
        str[j] = temp;
    }
}

int main() {
    char a[100005], b[100005];
    scanf("%s", a);
    scanf("%s", b);

    char result[100006]; // Max length + 1 for carry + null terminator
    int i = strlen(a) - 1;
    int j = strlen(b) - 1;
    int k = 0; // index for result
    int carry = 0;

    while (i >= 0 || j >= 0 || carry) {
        int n1 = (i >= 0) ? (a[i] - '0') : 0;
        int n2 = (j >= 0) ? (b[j] - '0') : 0;

        int sum = n1 + n2 + carry;
        result[k++] = (sum % 10) + '0';
        carry = sum / 10;

        i--;
        j--;
    }
    result[k] = '\0'; // Null-terminate the string

    reverse(result);
    printf("%s\n", result);

    return 0;
}