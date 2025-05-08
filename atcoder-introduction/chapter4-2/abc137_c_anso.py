from collections import Counter

N = int(input())
S = ["".join(sorted(input())) for _ in range(N)]

num = Counter(S)

print(sum(n * (n - 1) // 2 for n in num.values()))
