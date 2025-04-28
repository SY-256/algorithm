#include <iostream>
using namespace std;

// 整数のnの各桁の和を求める関数
int calc_sum_digits(int n) {
    int sum_digit = 0;
    while (n > 0) {
        sum_digit += n % 10;
        n /= 10;
    }
    return sum_digit;
}

int main() {
    int N, A, B;
    cin >> N >> A >> B;

    int result = 0;
    
    // 1以上N以下の整数を調べていく
    for (int i = 1; i <= N; i++) {
        int x = calc_sum_digits(i);

        // 各桁の和がA以上B以下である場合は加算
        if (A <= x && x <= B) {
            result += i;
        }
    }
    cout << result << endl;
}