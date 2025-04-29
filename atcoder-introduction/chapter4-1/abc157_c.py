N, M = map(int, input().split())
SC = [tuple(map(int, input().split())) for _ in range(M)]

for i in range(10**N):
    flag = True
    str_i = str(i)
    if len(str_i) != N:
        continue
    for v in SC:
        if v[0] - 1 >= len(str_i):
            flag = False
            break

        if int(str_i[v[0] - 1]) != v[1]:
            flag = False
            break

    if flag:
        exit(print(i))

print(-1)
