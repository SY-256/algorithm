H, W = map(int, input().split())
C = [input() for _ in range(H)]
result = []

for h in range(H):
    char = ""
    for w in range(W):
        char += C[h][w]
    result.append(char)
    result.append(char)
print(*result, sep="\n")