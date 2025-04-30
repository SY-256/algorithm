N, M = map(int, input().split())
SC = [tuple(map(int, input().split())) for _ in range(M)]

for ans in range(10**N):
    flag = True

    str_ans = str(ans)
    if len(str_ans) != N:
        continue

    for s, c in SC:
        if (s - 1) >= len(str_ans):
            flag = False
            break

        if int(str_ans[s - 1]) != c:
            flag = False
            break

    if flag:
        exit(print(ans))
print(-1)
