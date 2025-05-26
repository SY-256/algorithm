A, B = map(int, input().split())

if abs(((A // B) + 1) - (A / B)) < abs((A // B) - (A / B)):
    print((A // B) + 1)
else:
    print(A // B)
