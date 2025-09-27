//1<=N<=10^10, print all deviders in incresing order
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    long long N;
    cin>>N;
    vector<long long> chosenDiv;

    for(long long i=1;i*i<=N;i++){
        if(N%i==0){
            cout<<i<<" ";
            if(i!=N/i){
                chosenDiv.push_back(N/i);
            }
        }
    }
    reverse(chosenDiv.begin(),chosenDiv.end());
    for(long long x=0;x<chosenDiv.size();x++){
        cout<<chosenDiv[x]<<" ";
        
    } 
    return 0;
}