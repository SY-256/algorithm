N, M = map(int, input().split())
graph = [[] for _ in range(N)]


def count_all_paths(graph, start):
    N = len(graph)

    def dfs(v, visited):
        visited.add(v)

        # 全ノードを訪問した場合
        if len(visited) == N:
            visited.remove(v)  # バックトラッキング
            return 1

        count = 0
        for next_node in graph[v]:
            if next_node not in visited:
                count += dfs(next_node, visited)

        visited.remove(v)  # バックトラッキング
        return count

    return dfs(start, set())


for i in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1

    graph[a].append(b)
    graph[b].append(a)

ans = count_all_paths(graph, 0)
print(ans)
