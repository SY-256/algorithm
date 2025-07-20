N = int(input())
S = [str(input()) for _ in range(N)]

result = set()
for i in S:
    for j in S:
        if i != j:
            result.add(i + j)
print(len(result))
