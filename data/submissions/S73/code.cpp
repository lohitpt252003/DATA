#include<iostream>
#include <vector>
using namespace std;
int main(){
    vector<int>v;
    int t;
    cin>>t;
    int x;
    for(int i=0;i<t;i++){
      cin>>x;
      v.push_back(x);
    }
    for(int j=0;j<t;j++){
        if(v[j]%2==0) cout<<"EVEN"<<endl;
      else cout<<"ODD"<<endl;
}
    
}