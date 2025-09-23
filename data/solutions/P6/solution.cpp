#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;  // read number of testcases
    
    while (t--) {
        long long n;
        cin >> n;  // read the number
        
        if (n % 2 == 0) {
            cout << "EVEN" << endl;  // n divisible by 2 → EVEN
        } else {
            cout << "ODD" << endl;   // n not divisible by 2 → ODD
        }
    }
    return 0;
}
