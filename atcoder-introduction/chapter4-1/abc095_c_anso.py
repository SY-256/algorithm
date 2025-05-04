a, b, c, x, y = map(int, input().split())

ans = 10e18
n = 10**5 + 1
for ab in range(0, n * 2):
    sm = c * ab

    x_ = x - ab // 2
    y_ = y - ab // 2

    if x_ > 0:
        sm += x_ * a
    if y_ > 0:
        sm += y_ * b

    ans = min(ans, sm)
print(ans)
