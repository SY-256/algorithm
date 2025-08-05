n, m = map(int, input().split())
h = list(map(int, input().split()))

g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())

    a -= 1
    b -= 1

    g[a].append(b)
    g[b].append(a)

count = 0
for i, v in enumerate(g):
    if len(v) == 0:
        count += 1
        continue

    for v_i in v:
        flag = True
        if h[i] <= h[v_i]:
            flag = False
            break
    if flag:
        count += 1
print(count)
