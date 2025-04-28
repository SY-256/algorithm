#include <iostream>
using namespace std;

int main() {
    int A, B, C, D;
    cin >> A >> B >> C >> D;

    string ans = "Yes";

    while(A>0 || C>0){
        C -= B;
        if (C<=0) break;
        A -= D;
        if (A<=0) ans = "No";
    }
    cout << ans << endl;
}