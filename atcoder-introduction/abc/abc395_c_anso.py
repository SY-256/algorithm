N = int(input())
A = list(map(int, input().split()))

ans = N + 1
pos = [[] for _ in range(1_000_001)]

for i in range(N):
    pos[A[i]].append(i)  # 値に対応する配列に添え字を格納

for i in range(1_000_001):
    if len(pos) < 2:
        continue
    for j in range(len(pos[i]) - 1):
        ans = min(ans, pos[i][j + 1] - pos[i][j] + 1)

if ans == N + 1:
    print(-1)
else:
    print(ans)
