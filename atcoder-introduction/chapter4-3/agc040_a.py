S = list(input())
N = len(S)
node = [0] * (N + 1)

for i in range(N):
    if S[i] == "<":
        node[i + 1] = max(node[i] + 1, node[i + 1])

for i in range(N - 1, -1, -1):
    if S[i] == ">":
        node[i] = max(node[i], node[i + 1] + 1)

print(sum(node))
