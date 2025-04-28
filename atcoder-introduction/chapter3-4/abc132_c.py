N = int(input())
d = list(map(int, input().split()))

d = sorted(d)
d_1 = d[:len(d)//2]
d_2 = d[len(d)//2:]

ans = 0
for i in range(d_2[0], d_1[-1], -1):
    ans += 1
print(ans)