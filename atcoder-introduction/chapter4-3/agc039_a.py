S = input()
K = int(input())

v = []
i = 0

# 同じ文字が連続する区間を計測
while i < len(S):
    j = i
    while j < len(S) and S[j] == S[i]:
        j += 1
    v.append(j - i)
    i = j

# 最初と最後の文字が異なる
if S[0] != S[-1]:
    sum_val = 0
    for c in v:
        sum_val += c // 2
    exit(print(sum_val * K))
else:
    # 文字列がすべて同じ場合
    if len(v) == 1:
        exit(print(v[0] * K // 2))
    else:
        left = v[0]  # 最初に連続している
        right = v[-1]  # 最後に連続している
        mid = 0  # 中で連続している
        for i in range(1, len(v) - 1):
            mid += v[i] // 2

        result = (
            mid * K + (left + right) // 2 * (K - 1) + left // 2 + right // 2
        )  # （K - 1）⇒K回でK - 1箇所の連結部分ができる
        exit(print(result))
