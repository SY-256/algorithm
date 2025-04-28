K, S = map(int, input().split())

ans = 0
for x in range(0, K+1):
    for y in range(0, K+1):
        z = S - x - y

        if z < 0 or z > K:
            continue

        if z <= K:
            ans += 1
print(ans)