import itertools
N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
comb = itertools.combinations(A, 5)
for v in comb:
    if (v[0] * v[1] * v[2] * v[3] * v[4]) % P == Q:
        ans += 1
print(ans)