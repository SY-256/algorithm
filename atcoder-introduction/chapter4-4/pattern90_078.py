n, m = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())

    a -= 1
    b -= 1

    g[a].append(b)
    g[b].append(a)

count = 0
for i, v in enumerate(g):
    result = [x for x in v if x < i]
    if len(result) == 1:
        count += 1
print(count)
