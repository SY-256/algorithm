### 隣接リストを利用したグラフ
# 入力
N, M = map(int, input().split())
A = [None] * M
B = [None] * M
for i in range(M):
    A[i], B[i] = map(int, input().split())

# 隣接リスト
G = [list() for i in range(N + 1)]
for i in range(M):
    G[A[i]].append(B[i])  # 頂点A[i]に隣接する頂点としてB[i]を追加
    G[B[i]].append(A[i])  # 頂点B[i]に隣接する頂点としてA[i]を追加

# 出力（len(G[i]) は頂点iに隣接する頂点のリストの大きさ = 次数）
for i in range(1, N + 1):
    output = str(i) + ": {"
    for j in range(len(G[i])):
        if j >= 1:
            output += ","
        output += str(G[i][j])  # G[i][j]は頂点iに隣接する頂点のうちj+1番目のもの
    output += "}"
    print(output)
