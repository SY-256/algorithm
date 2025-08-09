import sys

sys.setrecursionlimit(10000)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]


def dfs(v):
    if temp[v]:
        return
    temp[v] = True
    for vv in graph[v]:
        dfs(vv)


for i in range(M):
    a, b = map(int, input().split())

    a, b = a - 1, b - 1
    graph[a].append(b)

ans = 0
for i in range(N):
    temp = [False] * N
    dfs(i)
    ans += sum(temp)

print(ans)
