N = int(input())
S = input()
ans = [S[0]]
for i in range(N - 1):
    if S[i] != S[i + 1]:
        ans.append(S[i + 1])
print(len(ans))
