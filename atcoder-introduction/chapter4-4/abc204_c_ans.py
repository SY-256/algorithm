N, M = map(int, input().split())
graph = [[] for _ in range(N)]


def count_all_paths(graph, start):
    def dfs(v, visited):
        visited.add(v)

        count = 0
        for next_node in graph[v]:
            if next_node not in visited:
                count = max(dfs(next_node, visited), count)

        count = max(len(visited), count)
        visited.remove(v)  # バックトラッキング
        return count

    return dfs(start, set())


for i in range(M):
    a, b = map(int, input().split())

    a, b = a - 1, b - 1
    graph[a].append(b)

ans = 0
for i in range(N):
    ans += count_all_paths(graph, i)

print(ans)
