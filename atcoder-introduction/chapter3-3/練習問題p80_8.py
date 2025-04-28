a, b = map(int, input().split())

ans = -1
for i in range(13, 1001):
    tax_a = int(i * 0.08)
    tax_b = int(i * 0.10)
    if a==tax_a and b==tax_b:
        ans = i
        break
print(ans)