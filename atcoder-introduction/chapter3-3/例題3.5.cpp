#include <iostream>
using namespace std;

int main() {
    // 整数H, Aの値を入力から受け取る
    int H, A;
    cin >> H >> A;

    // 攻撃回数を管理する変数
    int counter = 0;

    // 体力が0より大きい限り反復を繰り返す
    while (H > 0) {
        // HからAを引く
        H -= A;

        // 攻撃回数を1増やす
        ++counter;
    }

    // 答えを出力する
    cout << counter << endl;
}