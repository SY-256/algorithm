from collections import Counter

N, M = map(int, input().split())

if N == 1:
    exit(print(list(map(int, input().split()))[0]))

ans = 0
A = []
for i in range(N):
    a = sorted(list(map(int, input().split()))[1:])
    for v in a:
        A.append(v)

num = Counter(A).most_common()
for c, v in num:
    if v == N:
        ans += 1
print(ans)
