a, b = map(str, input().split())

ans = sorted([a * int(b), b * int(a)])
print(ans[0])