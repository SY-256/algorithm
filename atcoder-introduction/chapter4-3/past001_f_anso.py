S = input()

words = []

i = 0
while i < len(S):
    # S[j]が初めて大文字になるjを見つける
    j = i + 1
    while j < len(S) and S[j].islower():
        j += 1

    # 単語を切り出してリストに追加
    words.append(S[i : j + 1])

    # iをj + 1に進める
    i = j + 1

words.sort(key=str.lower)
print("".join(words))
