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
        add_set = set()
        for x in v:
            for c in g[x]:
                if c != s2 and c not in add_set:
                    add_set.add(c)
        for c in list(add_set):
            g[s2].append(c)

for i in range(n):
    for j in range(n):
        if j in g[i]:
            print("Y", end="")
        else:
            print("N", end="")
    print()
