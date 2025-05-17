N = int(input())
A = list(map(int, input().split()))

d = dict()
ans = 1e10
for i, v in enumerate(A):
    if d.get(v) is not None:
        ans = min(ans, len(A[d[v] : i + 1]))
    d[v] = i

print(-1) if ans == 1e10 else print(ans)
