import math
N, D = map(int, input().split())
DX = [i for i in range(1, N)]
X = [list(map(int, input().split())) for _ in range(N)]

count = 0
for i in range(0, N-1):
    for dx in DX:
        calc = 0
        ni = i + dx
        if ni < 0 or ni >= N:
            continue

        for j in range(0, D):
            if D == 1:
                count += 1
                continue
            else:
                temp_calc = (X[i][j] - X[ni][j])**2
                calc += temp_calc
        if math.sqrt(calc).is_integer() and calc != 0:
            count += 1
print(count)