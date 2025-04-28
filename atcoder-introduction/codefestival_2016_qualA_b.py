# 仲良しうさぎ
from collections import Counter
N = int(input())
a = list(map(int, input().split()))
ans_list = []
ans = 0
for i in range(N):
    ans_list.append((min(i+1, a[i]), max(i+1, a[i])))
mx = Counter(ans_list).most_common()

for k, v in mx:
    if v > 1:
        ans += 1
print(ans)