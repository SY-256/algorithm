from collections import Counter

N = int(input())
a = list(map(int, input().split()))
count = Counter(a).most_common()
ans = 0

for i, v in count:
    if (i - v) > 0:
        ans += v
    elif (i - v) < 0:
        ans += v - i
print(ans)
