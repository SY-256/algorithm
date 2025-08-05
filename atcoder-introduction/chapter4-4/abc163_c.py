n = int(input())
g = [[] for _ in range(n)]

a = list(map(int, input().split()))

for i, v in enumerate(a, 1):
    v -= 1
    g[v].append(i)

[print(len(v)) for v in g]
