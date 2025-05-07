N = int(input())
A, B, C = map(int, input().split())

ans = 1e9
for i in range(0, 10000):
    for j in range(0, 10000):
        v = A * i + B * j
        if v > N or (N - v) % C != 0:
            continue
        k = (N - v) // C
        if ans > i + j + k:
            ans = i + k + j
print(ans)
