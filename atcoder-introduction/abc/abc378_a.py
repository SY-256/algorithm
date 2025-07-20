from collections import defaultdict

A = list(map(int, input().split()))

D = defaultdict(int)
for i in A:
    D[i] += 1

ans = 0
for i in D.values():
    ans += i // 2
print(ans)
