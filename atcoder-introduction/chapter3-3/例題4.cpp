#include <iostream>
using namespace std;

int main() {
    int K, A, B;
    cin >> K >> A >> B;

    // フラグ
    bool exist = false;

    for (int i = A; i <= B; i++) {
        if (i % K == 0) {
            exist = true;
        }
    }
    if (exist) {
        cout << "OK" << endl;
    }
    else {
        cout << "NG" << endl;
    }

}
