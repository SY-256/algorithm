N = int(input())
XYH = [list(map(int, input().split())) for _ in range(N)]
for x in range(0, 100 + 1):
    for y in range(0, 100 + 1):
        flag = True
        for i in range(N):
            h = XYH[i][2]
            if h > 0:
                H = h + abs(XYH[i][0] - x) + abs(XYH[i][1] - y)

        for i in range(N):
            h = XYH[i][2]
            if h != max((H - abs(XYH[i][0] - x) - abs(XYH[i][1] - y)), 0):
                flag = False

        if flag:
            exit(print(x, y, H))
