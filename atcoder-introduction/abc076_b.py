N = int(input())
K = int(input())
ans = 1e7
for i in range(0, N + 1):
    temp = 1
    temp = temp * 2**i + K * (N - i)
    ans = min(ans, temp)
print(ans)
