from collections import Counter

N = int(input())

A = [int(input()) for _ in range(N)]
count = Counter(A).most_common()

ans = []
for i, v in count:
    if v % 2 == 1:
        ans.append(v)
print(len(ans))
