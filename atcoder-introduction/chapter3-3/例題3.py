H, A = map(int, input().split())
if H <= A:
    print(1)
elif H % A == 0:
    print(H//A)
else:
    print((H//A) + 1)