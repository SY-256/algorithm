#include <iostream>
using namespace std;

int main(){
    long long N;
    int  K;

    cin >> N >> K;

    for(int i=1; i<=K; i++){
        if( N % 200 == 0){
            N = N / 200; 
        }else{
            N = stoll(to_string(N)+to_string(200));
        }
    }
    cout << N << endl;
}