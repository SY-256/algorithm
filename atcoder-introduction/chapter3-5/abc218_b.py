P = list(map(int, input().split()))
alphabet = [chr(ord("a")+i) for i in range(26)]

ans = ""
for p in P:
    ans += alphabet[p-1]
print(ans)