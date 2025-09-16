#include <iostream>

int main() {
    // It's good practice to speed up C++ I/O.
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    // Declare two long long variables.
    long long a, b;
    
    // Read the two numbers from standard input.
    std::cin >> a >> b;
    
    // Print the sum to standard output followed by a newline.
    std::cout << a + b << std::endl;
    
    return 0;
}