import sys

sys.setrecursionlimit(100000)


N = int(input())
graph = [[] for _ in range(N)]

for i in range(N - 1):
    A, B = map(int, input().split())

    graph[A - 1].append(B - 1)
    graph[B - 1].append(A - 1)
C = [1] * N


def dfs(v, p=-1):
    for c in graph[v]:
        if c == p:
            continue
        dfs(c, v)
        if C[c]:
            C[v] = 0


dfs(0)
print(*[v + 1 for v in range(N) if C[v]][: N // 2])
