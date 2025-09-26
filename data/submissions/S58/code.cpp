#include<iostream>
#include<vector>

using namespace std;

int main(){
    long long n,l,r;
    cin>>n;
    cin>>r;
    cin>>l;
    //1<l<r<n
    vector<long long>a(n+1);

    for(long long i=1; i<=n;i++){
        cin>>a[i];
    }

    long long Sum1=0;
    for(int i=1;i<=l;i++){
        Sum1=Sum1+a[i];
    }

    long long Sum2=0;
    for(int i=1+l;i<=r;i++){
        Sum2=Sum2+a[i];
    }

    long long Sum3=0;
    for(int i=1+r;i<=n;i++){
        Sum3=Sum3+a[i];
    }

    long long S1=Sum1%3;
    long long S2=Sum2%3;
    long long S3=Sum3%3;
    
    if(n<l || n<r || l>r){
        cout<<"Warning";
    }
    else if(S1==S2 && S1==S3){
        cout<<"Yes";
    }
    else if(S1!=S2 && S1!=S3 && S2!=S3){
        cout<<"No";
    }
    else{
        cout<<"defalt";
    }
    return 0;

}