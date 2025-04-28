S = input()

count = 0
N = len(S) // 2
for i in range(N):
    if S[i] != S[-1-i]:
        count += 1
print(count)