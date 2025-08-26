N = int(input())
S = [v for v in str(input())]

W = [0] * (N)
E = [0] * (N)

for i in range(0, N):
    if S[i] == "W":
        W[i] = 1
    else:
        E[i] = 1

for i in range(1, N):
    W[i] += W[i - 1]
    E[i] += E[i - 1]

print(W, E)
ans = 1e9
for i in range(N):
    sm = 0
    if i > 0:
        sm += W[i - 1]
    sm += E[N - 1] - E[i]
    ans = min(ans, sm)
print(ans)
