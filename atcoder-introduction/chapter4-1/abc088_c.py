c = [list(map(int, input().split())) for _ in range(3)]

a = [0 for _ in range(3)]
b = [0 for _ in range(3)]
for a1 in range(0, 101):
    for a2 in range(0, 101):
        for a3 in range(0, 101):
            b1 = c[0][0] - a1
            b2 = c[0][1] - a1
            b3 = c[0][2] - a1

            a[0] = a1
            a[1] = a2
            a[2] = a3
            b[0] = b1
            b[1] = b2
            b[2] = b3

            ok = True
            for i in range(0, 3):
                for j in range(0, 3):
                    if a[i] + b[j] != c[i][j]:
                        ok = False
            if ok:
                exit(print("Yes"))
print("No")
