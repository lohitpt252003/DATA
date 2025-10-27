#include<iostream>

using namespace std;

long long int find_sq_root(long long int n){

    int ans = -1;
    for(long long int k = 1; k <= 1e5; k++){
        if((k*k) <= n) {
            ans = k;
        }
        else break;
    }
    // cout << ans << endl;
    return ans;
}

int find_num_of_factors(long long int n){

    int sqroot = find_sq_root(n);

    int cnt = 0;
    for(int i = 1; i<=sqroot; i++){
        if(n%i == 0){
            if(i*i != n) cnt += 2;
            else cnt++;
        } 
    }

    // cout << cnt << endl;
    if(cnt > 2) return 0;
    else return 1;

}

int main(){
    long long int n;
    cin >> n;
   
    if(n == 1) cout << "not prime" << endl;
    else if(n == 0) cout << "Not prime" << endl;
    
    else{

        int Ans = find_num_of_factors(n);
        if(Ans) cout<<"PRIME"<< endl;
        else cout<<"NOT prime"<<endl;


    }
    
    return 0;
}