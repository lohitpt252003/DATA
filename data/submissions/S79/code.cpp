#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    string s;
    cin >> n >> k >> s;

    int res = 0;
    int power = 1;

    for (int i = n - 1; i >= 0; i--) {  // right to left
        res = (res + (s[i] - '0') * power) % k;
        power = (power * 2) % k;
    }

    cout << res << "\n";
    return 0;
}
