N = int(input())
S = ["#"*N for _ in range(N)]
result = [[v for v in row] for row in S]

for i in range(0, N):
    for k in range(i, (N-i)):
        for j in range(i, (N-i)):
            if i > j:
                break

            if (i+1) % 2 == 0:
                result[k][j] = "."
            else:
                result[k][j] = "#"

print(*["".join(res) for res in result], sep="\n")