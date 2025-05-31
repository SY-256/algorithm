N = int(input())
d = dict()
for i in range(N):
    S = input()
    d[S] = len(S)

sorted_d = sorted(d.items(), key=lambda x: x[1])
print("".join(key for key, _ in sorted_d))
