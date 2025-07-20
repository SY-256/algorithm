Q = int(input())

queue = []
ans = []
for i in range(Q):
    q = tuple(map(str, input().split()))
    if len(q) == 2:
        queue.append(q[1])
    else:
        ans.append(queue.pop(0))
print(*ans, sep="\n")
