n = int(input())
st = [tuple(map(int, input().split())) for _ in range(n)]

v = st[0][1]
for i in range(1, n):
    t = st[i][0] - st[i - 1][0]
    v = st[i][1] + max(0, v - t)
print(v)
