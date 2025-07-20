N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = [1]

for i in range(N):
    if len(str(ans[i] * A[i])) > K:
        ans.append(1)
    else:
        ans.append(ans[i] * A[i])
print(ans[-1])
