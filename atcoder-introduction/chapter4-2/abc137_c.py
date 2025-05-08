from collections import defaultdict

N = int(input())

num = defaultdict(int)
for i in range(N):
    s = "".join(sorted(input()))
    num[s] += 1

ans = 0
for s in num:
    n = num[s]

    ans += (n * (n - 1)) // 2

print(ans)
