#include <bits/stdc++.h>

using namespace std;

#define ll long long

 bool prime(int n){
    if(n<=1) return false;
    for(int i=2; i*i<=n; i++){
        //if(n<=1) return false;
        if(n%i==0) return false;
    }
    return true;
    }

int main() {
    long long int n;
    cin>>n;
    prime(n);
    // bool prime(int n){
    // if(n<=1) return false;
    // for(int i=2; i*i<=n; i++){
    //     //if(n<=1) return false;
    //     if(n%i==0) return false;
    // }
    // return true;
    // }
    
    if(prime) cout<<"Prime";
    else cout<<"Not prime";
    return 0;
}