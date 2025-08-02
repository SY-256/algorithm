from collections import defaultdict
import bisect

N = int(input())
A = list(map(int, input().split()))

plus_dict = defaultdict(list)
minus_dict = defaultdict(list)

for i in range(N):
    plus_value = i + A[i]
    minus_value = i - A[i]

    plus_dict[plus_value].append(i)
    minus_dict[minus_value].append(i)

count = 0
for value in plus_dict:
    if value in minus_dict:
        i_idx = plus_dict[value]
        j_idx = minus_dict[value]

        j_idx_sorted = sorted(j_idx)

        for i in i_idx:
            pos = bisect.bisect_right(j_idx, i)
            count += len(j_idx_sorted) - pos
print(count)
