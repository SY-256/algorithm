N, Y = map(int, input().split())

a, b, c = -1, -1, -1

for i in range(N + 1):
    for j in range(N + 1):
        k = N - i - j

        if k < 0 or k > N:
            continue

        if 10000*i + 5000*j + 1000*k == Y:
            a, b, c = i, j, k
print(a, b, c)