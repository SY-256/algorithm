from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))

num = Counter(A).most_common()[::-1]
n = len(num) - K

ans = 0
for i in range(n):
    ans += num[i][1]
print(ans)
