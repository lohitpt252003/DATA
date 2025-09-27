#include<iostream>
#include<vector>

using namespace std;
vector<long long>prefix;
// long long sum(const vector<long long> &a, long long l,long long r ){
//     long long s=0;
//     for (long long i = l; i <= r; i++) {
//         s += a[i];
//     }
//     return s;
// }
long long sum(int l,int r){
    return prefix[r]-prefix[l-1];
}
int main(){
    long long n;
    cin>>n;
    vector<long long>a(n+1);
    prefix.assign(n+1,0);

    for(long long i=1; i<=n;i++){
        cin>>a[i];
        prefix[i]=prefix[i-1]+a[i];
    }
    int t;
    for(int i=2;i<n;i++){
        for(int j=i+1;j<n;j++){
            int S1=sum(1,i)%3;
            int S2=sum(i+1,j)%3;
            int S3=sum(j+1,n)%3;
            if(S1==S2 && S2==S3 && S1==S3){
                t=1;
                break;
            }
            else if(S1!=S2 && S2!=S3 && S1!=S3){
                 t=1;
                 break;
            }
            else{
                t=0;
                break;
            }
        }
    }
    if(t){
        cout<<"YES";
    }
    else{
        cout<<"NO";
    }
    
    return 0;

}