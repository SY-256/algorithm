import sys

sys.setrecursionlimit(10000)


class UnionFind:
    def __init__(self, n):
        self.par = [-1] * n

    def root(self, x):
        if self.par[x] < 0:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def merge(self, x, y):
        x, y = self.root(x), self.root(y)
        if x == y:
            return
        if self.par[x] > self.par[y]:
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x


N, M = map(int, input().split())
edges = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

res = 0
for e in range(M):
    uf = UnionFind(N)
    for i, (a, b) in enumerate(edges):
        if i != e:
            uf.merge(a, b)

    componets = sum(1 for v in range(N) if uf.root(v) == v)
    if componets > 1:
        res += 1

print(res)
