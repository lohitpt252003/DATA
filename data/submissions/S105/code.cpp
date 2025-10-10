#include<iostream>
using namespace std;

int fun(int A,  int B){
    if(A==0){
        return B;
    }
    else if(B==0 || A==B){
        return A;
    }
    else if(A>B){
        return fun(B,  A-B);
    }
    else if(A<B){
        return fun(A,  B-A);
    }
    
}
int main(){
    int A,B;
    cin>>A>>B;
    int result= fun(A,  B);
    cout<<result;
    return 0;
}