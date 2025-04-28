DX = [1, 0, -1, 0, 1, -1, -1, 1]
DY = [0, 1, 0, -1, 1, 1, -1, -1]

h, w = map(int, input().split())
s = [input() for i in range(h)]

result = [[0 if v == '.' else '#' for v in row] for row in s]

for i in range(h):
    for j in range(w):
        # 空きマス以外はそのまま
        if s[i][j] != '.':
            continue

        # 周囲8マスの'#'個数を数える
        for dx, dy in zip(DX, DY):
            ni, nj = i + dx, j + dy

            # マスが盤面外の場合はスキップ
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue

            # #であれば1増やす
            if s[ni][nj] == "#":
                result[i][j] += 1

for row in result:
    print(*row, sep="")
