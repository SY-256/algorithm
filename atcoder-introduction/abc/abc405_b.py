N, M = map(int, input().split())
A = list(map(str, input().split()))
base = [str(n) for n in range(1, M + 1)]
ans = 0
for i in range(0, N):
    if set(base) != set(A):
        exit(print(ans))
    A = A[:-1]
    ans += 1
print(ans)
