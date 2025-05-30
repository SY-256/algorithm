N, M = map(int, input().split())

ans = 0
for i in range(0, M + 1):
    ans += pow(N, i)
    if ans > 1e9:
        exit(print("inf"))
print(ans)
