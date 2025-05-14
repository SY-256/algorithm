s = input()

ans = [s[0]]
count = 1
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        ans.append(str(count))
        ans.append(s[i + 1])
        count = 1
    else:
        count += 1

    if i == len(s) - 2:
        ans.append(str(count))

print("".join(ans))
