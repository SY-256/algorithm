N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = [0] * (N + 1)
for i in range(1, N + 1):
    ans[i] = ans[i - 1] + A[i - 1]

for i in range(1, (N - K + 1) + 1):
    print(ans[K + i - 1] - ans[i - 1])
