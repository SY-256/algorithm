N, K = map(int, input().split())
X = list(map(int, input().split()))

mi = [0]
pr = [0]
for i in range(N):
    if X[i] <= 0:
        mi.append(abs(X[i]))
    else:
        pr.append(X[i])
mi = sorted(mi)
pr = sorted(pr)

n = len(mi)
m = len(pr)
ans = 10**18 * 2

# Lastが正
for i in range(0, n):
    j = K - i
    if j >= 0 and m > j:
        ans = min(ans, mi[i] * 2 + pr[j])

# Lastが負
for i in range(0, m):
    j = K - i
    if j >= 0 and n > j:
        ans = min(ans, pr[i] * 2 + mi[j])
print(ans)
