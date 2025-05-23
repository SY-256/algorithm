S = input()
N = len(S)

# dp[p][i] =  位置iから2^p回移動した後の位置
dp = [[0] * N for _ in range(33)]
ans = [0] * N

#  初期状態：1回の移動
for i in range(N):
    if S[i] == "R":
        dp[0][i] = i + 1  # 右端を超えないように制御
    else:  # S[i] == "L"
        dp[0][i] = i - 1  # 左端を超えないように制御

# ダブリング: 2^p回移動 = 2^(p-1)回移動を2回
for p in range(32):
    for i in range(N):
        dp[p + 1][i] = dp[p][dp[p][i]]

# 各位置から32回移動（2^32回移動）した後の到達位置をカウント
for i in range(N):
    ans[dp[32][i]] += 1

# 結果を出力
print(" ".join(map(str, ans)))
