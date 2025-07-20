T = input()
U = input()

n = len(T) - len(U) + 1
j = len(U)

for i in range(n):
    _T = T[i : j + i]

    flag = True
    for k in range(j):
        if _T[k] != U[k] and _T[k] != "?":
            flag = False

    if flag:
        exit(print("Yes"))
print("No")
