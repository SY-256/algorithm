X, Y = map(int, input().split())

count = 0
for i in range(1, 7):
    for j in range(1, 7):
        if (i + j) >= X:
            count += 1
            continue
        elif abs(i - j) >= Y:
            count += 1

print(count / 36)
