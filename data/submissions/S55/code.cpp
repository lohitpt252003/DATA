#include <bits/stdc++.h>

using namespace std;

void solve() {
    int n;
    cin>>n;
    vector<int>arr(n);
    int s1=0;
    int s2=0;
    int s3=0;
    for (int i=0;i<n;i++){
        cin>>arr[i];
        if(i>1)
        s3=s3+arr[i];
    }
    s1=arr[0];
    s2=arr[1];
    if((s1==s2)&& (s2==s3)){
        cout<<"YES";
        return;
    }
    if( (s1!=s2) && (s2!=s3) && (s3!=s1) ){
        cout<<"YES";
    }
    else{
        cout<<"NO";
    }

}

int main() {
    
    int t = 1;
    //cin >> t;
    
    while (t--) {
        solve();
    }
    
    return 0;
}