from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))

count = Counter(A)

if len(count) <= K:
    exit(print(0))
else:
    freq = sorted(count.values())  # 出現回数の少ない順に並べる
    to_remove = freq[: len(freq) - K]  # 取り除く要素数決める
    print(sum(to_remove))
