from collections import defaultdict

N = int(input())
D = defaultdict(int)
for i in range(N):
    S = input()
    D[S] += 1

D_max = max(D.values())
ans = sorted([key for key, v in D.items() if v == D_max])
print(*ans, sep="\n")
