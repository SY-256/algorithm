n = int(input())
p = list(map(int, input().split()))

ans, m = 0, 10**9
for i in range(n):
    if p[i] <= m:
        m = p[i]
        ans += 1
print(ans)