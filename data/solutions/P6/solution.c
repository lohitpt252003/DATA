#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

// Function to check if num1 is smaller than num2 (for positive numbers)
bool isSmaller(char* num1, char* num2) {
    int n1 = strlen(num1), n2 = strlen(num2);
    if (n1 < n2) return true;
    if (n1 > n2) return false;
    for (int i = 0; i < n1; i++) {
        if (num1[i] < num2[i]) return true;
        else if (num1[i] > num2[i]) return false;
    }
    return false;
}

// Function to subtract two positive numbers represented as strings
// Assumes num1 >= num2
char* subtractPositive(char* num1, char* num2) {
    char* str = (char*)malloc(sizeof(char) * (strlen(num1) + 2)); // +1 for null terminator, +1 for potential sign
    int k = 0;
    int n1 = strlen(num1), n2 = strlen(num2);
    
    // Reverse both strings
    char* rev_num1 = strdup(num1);
    char* rev_num2 = strdup(num2);
    strrev(rev_num1);
    strrev(rev_num2);

    int carry = 0;
    for (int i = 0; i < n2; i++) {
        int sub = ((rev_num1[i] - '0') - (rev_num2[i] - '0') - carry);
        if (sub < 0) {
            sub = sub + 10;
            carry = 1;
        } else {
            carry = 0;
        }
        str[k++] = sub + '0';
    }

    for (int i = n2; i < n1; i++) {
        int sub = ((rev_num1[i] - '0') - carry);
        if (sub < 0) {
            sub = sub + 10;
            carry = 1;
        } else {
            carry = 0;
        }
        str[k++] = sub + '0';
    }
    str[k] = '\0';

    strrev(str);

    // Remove leading zeros
    int i = 0;
    while (i < k - 1 && str[i] == '0') {
        i++;
    }
    char* result = strdup(str + i);
    free(str);
    free(rev_num1);
    free(rev_num2);
    return result;
}

// Placeholder for large number subtraction in C
// This is a simplified placeholder. Full implementation requires careful handling of signs and magnitudes.
char* subtract(char* num1_orig, char* num2_orig) {
    char* num1 = strdup(num1_orig);
    char* num2 = strdup(num2_orig);
    char* result_str;
    bool negative = false;

    // Remove leading zeros
    int i = 0;
    while (num1[i] == '0' && num1[i+1] != '\0') i++;
    char* temp_num1 = strdup(num1 + i);
    free(num1);
    num1 = temp_num1;

    i = 0;
    while (num2[i] == '0' && num2[i+1] != '\0') i++;
    char* temp_num2 = strdup(num2 + i);
    free(num2);
    num2 = temp_num2;

    if (strcmp(num1, num2) == 0) {
        free(num1);
        free(num2);
        return strdup("0");
    }

    // Determine the sign of the result
    if (isSmaller(num1, num2)) {
        char* temp = num1;
        num1 = num2;
        num2 = temp;
        negative = true;
    }

    result_str = subtractPositive(num1, num2);

    if (negative) {
        char* temp_result = (char*)malloc(strlen(result_str) + 2);
        sprintf(temp_result, "-%s", result_str);
        free(result_str);
        result_str = temp_result;
    }
    free(num1);
    free(num2);
    return result_str;
}

int main() {
    char a_str[1000], b_str[1000]; // Increased buffer size for large numbers
    scanf("%s %s", a_str, b_str);
    char* result = subtract(a_str, b_str);
    printf("%s\n", result);
    free(result);
    return 0;
}

