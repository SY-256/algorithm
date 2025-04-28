N = int(input())
H = list(map(int, input().split()))

ans = 1
H_max = H[0]
for i in range(1, len(H)):
    if H[i-1] <= H[i] and H_max <= H[i]:
        ans += 1
    H_max = max(H_max, H[i])
print(ans)