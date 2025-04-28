#include <iostream>
using namespace std;

int main() {
  int N, X, Y;
  cin >> N >> X;
  for (int i = 0; i < N; i++) {
    cin >> Y;
    if (X == Y) {
      cout << "OK" <<endl;
      return 0;
    }
  }
  cout << "NG" << endl;
  return 0;
}