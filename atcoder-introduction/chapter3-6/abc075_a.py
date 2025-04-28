from collections import Counter

abc = list(map(int, input().split()))
ans = Counter(abc).most_common()[-1][0]
print(ans)