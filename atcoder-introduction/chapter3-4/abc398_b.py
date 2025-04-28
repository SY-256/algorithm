from collections import Counter
A = list(map(int, input().split()))

counter = Counter(A)
sorted_result = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
if len(sorted_result) > 1:
    print("Yes") if sorted_result[0][1] >= 3 and sorted_result[1][1] >= 2 else print("No")
else:
    print("No")