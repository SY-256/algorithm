n = int(input())
p = list(map(int, input().split()))

ans, m = 1, p[0]
for i in range(1, n):
    if p[i] <= m:
        m = p[i]
        ans += 1
print(ans)