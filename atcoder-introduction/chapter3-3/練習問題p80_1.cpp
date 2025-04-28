#include <iostream>
using namespace std;

int calc_fizzbuzz(int n) {
    if (n % 3 != 0 && n % 5 != 0) {
        return n;
    }
    return 0;
}

int main () {
    int N ;
    cin >> N;

    long result = 0;

    for (int i = 1; i <= N; i++){
        result += calc_fizzbuzz(i);
    }
    cout << result << endl;
}
