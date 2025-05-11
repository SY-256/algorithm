from collections import defaultdict

N = int(input())
ans = []
D = defaultdict(int)
for i in range(N):
    S = input()
    if not D[S]:
        ans.append(i + 1)
        D[S] = 1
print(*ans, sep="\n")
