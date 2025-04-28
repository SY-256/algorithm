#include <iostream>
using namespace std;

// N!を求める
int calc_Ni(long P){
    long P_diff = P;
    long N_sum = 1;
    int N_i = 0;

    while(P_diff>=0){
        N_i += 1;
        N_sum *= N_i;
        P_diff = P - N_sum;
        if(P_diff < 0) {
            N_i -= 1;
            break;
        }
    }
    return N_i;
}

int calc_N_upstairs(int n){
    long N_upstairs = 1;
    for (int i=1; i<=n; i++) {
        N_upstairs *= i;
    }
    return N_upstairs;
}

int main(){
    long P;
    cin >> P;

    int N = 1;
    int ans = 0;

    int N_i = calc_Ni(P);

    for(int i=N_i; i>=1; i--){
        long N_upstairs = calc_N_upstairs(i);

        ans += P / N_upstairs;
        P %= N_upstairs;
        if(P==0){
            break;
        }
    }
    cout << ans << endl;
}