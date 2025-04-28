#include <iostream>
using namespace std;

int main () {
    long N;
    cin >> N;
    long result = 0;
    long i = 0;

    while (N > result)
    {
        i += 1;
        result += i;
    }
    cout << i << endl;
}