N = int(input())

S = ""
ci = []
for _ in range(N):
    c, i = map(str, input().split())
    ci.append((c, int(i)))

for c, i in ci:
    if i > 100:
        exit(print("Too Long"))

    S += c * i
    if len(S) > 100:
        exit(print("Too Long"))
print(S)
