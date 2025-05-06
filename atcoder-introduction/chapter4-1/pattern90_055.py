N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
count = 0
for i1 in range(0, N):
    for i2 in range(i1 + 1, N):
        for i3 in range(i2 + 1, N):
            for i4 in range(i3 + 1, N):
                for i5 in range(i4 + 1, N):
                    v = ((((A[i1] * A[i2] % P) * A[i3] % P) * A[i4] % P) * A[i5]) % P
                    if v == Q:
                        ans += 1
print(ans)
