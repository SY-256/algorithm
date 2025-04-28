import math
n, d = map(int, input().split())

ans = 0
for i in range(n):
    x, y = map(int, input().split())
    if math.sqrt(pow(x, 2) + pow(y, 2)) <= d:
        ans += 1
print(ans)