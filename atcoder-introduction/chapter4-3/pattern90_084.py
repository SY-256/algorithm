N = int(input())
S = str(input())

count = 0
vec = []
for i in range(N):
    count += 1
    if i == N - 1 or S[i] != S[i + 1]:
        vec.append((S[i], count))
        count = 0

ret = 0
for char, count in vec:
    ret += count * (count + 1) // 2

ans = (N * (N + 1)) // 2 - ret
print(ans)
