#include <iostream>
using namespace std;

int main(){
    long A, B;
    int K;
    cin >> A >> B >> K;

    for(long i=A; i<min(A+K, B + 1); i++){
        cout << i << endl;
    }
    
    for(long i=max(A + K, B - K + 1); i<B+1; i++){
            cout << i << endl;
    }
}