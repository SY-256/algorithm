N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
calc_result = T - H[0] * 0.006
ans = 1

for i in range(1, N):
    if pow((calc_result-A), 2) > pow(((T-H[i]*0.006)-A), 2):
        calc_result = (T-H[i]*0.006)
        ans = i+1
print(ans)