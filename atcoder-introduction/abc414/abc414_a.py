N, L, R = map(int, input().split())
result = 0

for _ in range(N):
    X, Y = map(int, input().split())
    if X <= L <= R <= Y:
        result += 1
print(result)
