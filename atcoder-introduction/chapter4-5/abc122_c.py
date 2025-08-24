N, Q = map(int, input().split())
S = input()
lr = [list(map(int, input().split())) for _ in range(Q)]

ans = [0 for _ in range(N)]
for i in range(1, N):
    if (S[i - 1], S[i]) == ("A", "C"):
        ans[i] = ans[i - 1] + 1
    else:
        ans[i] = ans[i - 1]
print(ans)
for l, r in lr:
    print(ans[r - 1] - ans[l - 1])
