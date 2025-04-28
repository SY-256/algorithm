N = int(input())
A = list(map(int, input().split()))

ans = 0
while True:
    if max([a % 2 for a in A])!=0:
        break
    A = [a / 2 for a in A]
    ans += 1
print(ans)
