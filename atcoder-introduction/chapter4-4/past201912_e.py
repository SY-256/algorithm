n, q = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(q):
    s = input().split()

    if s[0] == "1":
        s2 = int(s[1]) - 1
        s3 = int(s[2]) - 1

        g[s2].append(s3)

    elif s[0] == "2":
        s2 = int(s[1]) - 1

        for j, x in enumerate(g):
            if s2 in x and s2 != j:
                g[s2].append(j)

    elif s[0] == "3":
        s2 = int(s[1]) - 1
        v = g[s2]
        add = []
        for x in v:
            add += g[x]
        g[s2] += add

for i in g:
    ans = ["N" for _ in range(n)]
    x = sorted(list(set(i)))
    for j in x:
        ans[j] = "Y"
    print(*ans, sep="")
