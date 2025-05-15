N = int(input())
H = list(map(int, input().split()))
count = 0
ans = 0
for i in range(N - 1):
    if H[i] >= H[i + 1]:
        count += 1
    else:
        count = 0
    ans = max(ans, count)
print(ans)
