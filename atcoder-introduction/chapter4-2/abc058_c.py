from collections import defaultdict

N = int(input())
D_list = []
for i in range(N):
    S = input()
    D = defaultdict(int)
    for si in S:
        D[si] += 1
    D_list.append(D)

target = set(D_list[0].keys())
for i in range(N - 1):
    target = target & set(D_list[i + 1].keys())

ans = ""
if target:
    char_d = defaultdict(int)
    for t in list(target):
        num = 1e9
        for d in D_list:
            num = min(d[t], num)
        char_d[t] = num

    for k, v in char_d.items():
        ans += k * v

    print(*sorted(ans), sep="")
else:
    print(ans)
