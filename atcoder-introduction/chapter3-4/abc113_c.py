N, M = map(int, input().split())
L = []
for i in range(M):
    P, V = input().split()
    val = (i, int(P), int(V), int(P+V.zfill(12)))
    L.append(val)

L_sorted = sorted(L, key=lambda x: x[3])
L_ans = [-1] * M
now_P = L_sorted[0][1]
count = 1
for v in L_sorted:
    if v[1]!=now_P:
        now_P = v[1]
        count = 1
    L_ans[v[0]] = str(now_P).zfill(6) + str(count).zfill(6)
    count += 1
print(*L_ans, sep="\n")