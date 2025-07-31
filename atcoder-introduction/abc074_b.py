N = int(input())
K = int(input())
x = list(map(int, input().split()))

ans = 0
for v in x:
    ans += min(abs(v - 0) * 2, abs(K - v) * 2)
print(ans)
