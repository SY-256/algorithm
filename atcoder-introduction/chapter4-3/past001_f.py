S = input()
ans = []
oomoji = False
start = 0
for i, char in enumerate(S):
    if char.isupper() and oomoji:
        ans.append(S[start : i + 1])
        oomoji = False
        continue

    if char.isupper() and not oomoji:
        oomoji = True
        start = i
print("".join(sorted(ans, key=str.lower)))
