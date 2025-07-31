A, B = map(int, input().split())

ans = 0
for v in range(A, B + 1):
    if str(v) == str(v)[::-1]:
        ans += 1
print(ans)
