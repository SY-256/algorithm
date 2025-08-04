n, m = map(int, input().split())

g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())

    a -= 1
    b -= 1

    g[a].append(b)
    g[b].append(a)

for i in g:
    print(len(i))
