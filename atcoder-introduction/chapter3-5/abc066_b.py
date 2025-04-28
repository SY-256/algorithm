S = input()

for i in range(len(S)):
    S = S[:-1]
    n = len(S) // 2
    if S[:n] == S[n:]:
        print(len(S))
        break