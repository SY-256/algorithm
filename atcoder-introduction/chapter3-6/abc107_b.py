H, W = map(int, input().split())
a = [input() for _ in range(H)]
result = [[v for v in row] for row in a]

for i in range(H):
    break_flag = False
    for j in range(W):
        if result[i][j] == "#":
            break_flag = True
            break
    if not break_flag:
        for j in range(W):
            result[i][j] = "1"

for j in range(W):
    break_flag = False
    for i in range(H):
        if result[i][j] == "#":
            break_flag = True
            break
    if not break_flag:
        for i in range(H):
            result[i][j] = "1"
ans = []
for res in result:
    char = [v for v in res if v!="1"]
    if len(char) > 0:
        ans.append("".join(char))
print(*ans, sep="\n")    