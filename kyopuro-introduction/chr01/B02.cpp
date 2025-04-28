#include <iostream>
using namespace std;

int main() {
  int A, B, R, a[100];
  bool Answer = false;
  cin >> A >> B;
  R = B - A;
  for (int i = 0; i <= R; i++) {
    a[i] = A + i;
    if (100 % (A + i) == 0) Answer = true;
  }

  if (Answer == true) cout << "Yes" << endl;
  else cout << "No" << endl;
  return 0;
}