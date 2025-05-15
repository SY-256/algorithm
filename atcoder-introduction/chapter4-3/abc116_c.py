N = int(input())
h = [0] + list(map(int, input().split())) + [0]

ans = 0
for i in range(0, N + 1):
    ans += abs(h[i + 1] - h[i])

print(ans // 2)
