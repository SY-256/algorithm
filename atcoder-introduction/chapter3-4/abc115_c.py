N, K = map(int, input().split())
h=[int(input()) for i in range(N)]
h = sorted(h)
ans = h[-1]
for i in range(N-K+1):
    calc = h[i+K-1] - h[i]
    if ans > calc:
        ans = calc
print(ans)