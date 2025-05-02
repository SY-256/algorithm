n, c1, c2 = map(str, input().split())
s = input()
ans = ""
for i in range(0, int(n)):
    if s[i] != c1:
        ans += c2
    else:
        ans += c1
print(ans)
