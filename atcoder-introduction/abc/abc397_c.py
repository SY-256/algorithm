N = int(input())
A = list(map(int, input().split()))

suml = [0] * N
vis = [0] * (N + 1)
now = 0
for i in range(N):
    if not vis[A[i]]:
        now += 1
    vis[A[i]] = 1
    suml[i] = now

sumr = [0] * N
vis = [0] * (N + 1)
now = 0
for i in range(N - 1, -1, -1):
    if not vis[A[i]]:
        now += 1
    vis[A[i]] = 1
    sumr[i] = now

ans = 0
for i in range(N - 1):
    ans = max(ans, suml[i] + sumr[i + 1])

print(ans)
