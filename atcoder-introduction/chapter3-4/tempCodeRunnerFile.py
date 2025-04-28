N = int(input())
d = list(map(int, input().split()))

d = sorted(d)
d_1 = d[:len(d)//2]
d_2 = d[len(d)//2:]
median = (d_1[-1]+d_2[0])//2
for i in range(median, d_2[0]):
    if len(d_2) == len([v for v in d_2 if v >= i]):
        ans += 1
ans = 0