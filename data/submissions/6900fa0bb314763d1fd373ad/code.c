#include <stdio.h>

// Define the maximum value of x
#define MAX_X 1000000

// Array to store the count of divisors for each number.
// We use 'static' so it's initialized to all zeros by default.
static int divisor_counts[MAX_X + 1];

// Function to pre-compute the divisor counts for all numbers up to MAX_X
void precompute_divisors() {
    // Loop through all possible divisors 'i'
    for (int i = 1; i <= MAX_X; i++) {
        // Loop through all multiples 'j' of 'i'
        // For each multiple 'j', 'i' is a divisor, so we increment its count.
        for (int j = i; j <= MAX_X; j += i) {
            divisor_counts[j]++;
        }
    }
}

int main() {
    // Run the pre-computation once at the start.
    precompute_divisors();

    int n; // Number of integers
    scanf("%d", &n);

    // Loop n times to process each query
    for (int i = 0; i < n; i++) {
        int x; // The integer for the current query
        scanf("%d", &x);

        // Print the pre-computed answer from our array.
        // This is an O(1) lookup.
        printf("%d\n", divisor_counts[x]);
    }

    return 0;
}
