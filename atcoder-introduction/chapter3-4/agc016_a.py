s = str(input())

# 使われている文字セットを作る
ch_set = set(s)

result = len(s)
# どの文字に統一するかは全探索で決める
for c in ch_set:
    # splitで分割して、一番長い部分の長さを求める
    tmp_r = max(len(p) for p in s.split(c))

    if tmp_r < result:
        result = tmp_r

print(result)
