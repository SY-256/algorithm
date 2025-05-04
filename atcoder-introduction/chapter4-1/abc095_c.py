a, b, c, x, y = map(int, input().split())

ans1 = x * a + y * b
ans2 = c * max(x, y) * 2
ans3 = c * min(x, y) * 2
if min(x, y) == x:
    ans3 += b * (y - x)
elif min(x, y) == y:
    ans3 += a * (x - y)

print(min(ans1, ans2, ans3))
