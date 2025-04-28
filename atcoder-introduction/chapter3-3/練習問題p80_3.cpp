#include <iostream>
using namespace std;

int main () {
    long X;
    cin >> X;
    long deposit = 100;
    long counter = 0;
    while(X > deposit){
        deposit += deposit / 100; // 丸目誤差でWA
        counter ++;
    }
    cout << counter << endl;
}