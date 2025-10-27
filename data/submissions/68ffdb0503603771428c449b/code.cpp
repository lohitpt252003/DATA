#include<iostream>
#include<vector>

using namespace std;

bool CheckPrime(long long n){
    if(n<2)return false;
    if(n%2==0 && n!=2)return false;
    for(long long i=3;i*i<=n;i++){
        if(n%i==0){
            return false;
        }
    }
    return true;
}
int main(){
    
    long long n;
    cin>>n;
    // cout<<CheckPrime(n);
    if(CheckPrime(n)){
        cout<<"1";
    }
    else{
        cout<<"-1";
    }
    return 0;
}