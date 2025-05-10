N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    del A[i][0]
    A[i] = set(A[i])

ans = A[0]
for i in range(N - 1):
    ans = ans & A[i + 1]
print(len(ans))
