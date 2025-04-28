N, K = map(int, input().split())
l = list(map(int, input().split()))

sorted_l = sorted(l, reverse=True)
ans = 0
for l_i in sorted_l[:K]:
    ans += l_i
print(ans)