from collections import Counter
N = int(input())
A = list(map(int, input().split()))

counter = Counter(A)
sorted_result = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
l = []
for i in sorted_result:
    if i[1] == 1:
        l.append(i[0])        
print(A.index(max(l))+1 if len(l)>0  else "-1")