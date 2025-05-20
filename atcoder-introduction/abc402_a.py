S = input()
ans = []
for i in S:
    if i.isupper():
        ans.append(i)
print(*ans, sep="")
