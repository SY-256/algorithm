n, m, q = map(int, input().split())

g = [[] for i in range(n)]

# m本の辺を順番に受け取る
for i in range(m):
    u, v = map(int, input().split())

    # 頂点番号を0始まりにする
    u -= 1
    v -= 1

    # グラフに辺を追加
    g[u].append(v)
    g[v].append(u)


# 初期状態の各頂点の色を入力
col = list(map(int, input().split()))

# 各クエリに答える
for i in range(q):
    t, x, *y = map(int, input().split())

    # 頂点番号を0始まりにする
    x -= 1

    # 頂点xの色を出力
    print(col[x])

    # タイプ1の場合
    if t == 1:
        # 頂点xに隣接する各頂点vの色を更新
        for v in g[x]:
            col[v] = col[x]
    # タイプ2の場合
    else:
        # 頂点xの色をyに更新
        col[x] = y[0]
