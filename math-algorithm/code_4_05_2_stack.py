# 深さ優先探索（DFS）をスタック用いて実装

# 入力
N, M = map(int, input().split())
A = [None] * M
B = [None] * M
for i in range(M):
    A[i], B[i] = map(int, input().split())

# 隣接リストの作成
G = [list() for _ in range(N + 1)]
for i in range(M):
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

# 深さ優先探索の初期化
visited = [False] * (N + 1)
S = list()  # スタックSを定義
visited[1] = True
S.append(1)  # Sに1を追加

# 深さ優先探索
while len(S) >= 1:
    pos = S.pop()  # Sの先頭を調べて、これを取り出す
    for nex in G[pos]:
        if not visited[nex]:
            visited[nex] = True
            S.append(nex)  # Sにnexを追加

# 連結かどうか判定
answer = True
for i in range(1, N + 1):
    if not visited:
        answer = False

if answer:
    print("The graph is connected.")
else:
    print("The graph is not connected.")
