S = str(input())
N = len(S)
a = [0] * (N + 1)

# check "<"
for i in range(N):
    c = S[i]
    if c == "<":
        a[i + 1] = a[i] + 1

# check ">"
for i in range(N - 1, -1, -1):
    c = S[i]
    if c == ">":
        a[i] = max(a[i], a[i + 1] + 1)

print(sum(a))
