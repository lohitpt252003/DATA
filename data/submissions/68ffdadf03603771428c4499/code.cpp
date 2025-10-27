#include <bits/stdc++.h>

using namespace std;

void solve() {
    long long n;
    cin>>n;
    if(n<2) {
        cout<<"not prime";
        return;
    }

    for(int i=2;i<=pow(n,1.0/2);i++){
        if(n%i==0){
            cout<<"NOT PRIME";
            return ;
        }
    }
    cout<<"prime";

}

int main() {
    
    int t = 1;
    //cin >> t;
    
    while (t--) {
        solve();
    }
    
    return 0;
}