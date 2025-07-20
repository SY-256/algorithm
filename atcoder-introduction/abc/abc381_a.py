N = int(input())
S = str(input())

if N % 2 == 1:
    i = ((N + 1) // 2) - 1
    j = (N + 1) // 2
    k = ((N + 1) // 2) + 1

    if N == 1:
        if S[j - 1] == "/":
            exit(print("Yes"))
    elif len(list(set(S[:i]))) == 1 and list(set(S[:i]))[0] == "1":
        if S[j - 1] == "/":
            if len(list(set(S[k - 1 :]))) == 1 and list(set(S[k - 1 :]))[0] == "2":
                exit(print("Yes"))
print("No")
