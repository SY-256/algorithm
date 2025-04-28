Q = int(input())

query = [0] * 100
count = 0
for i in range(Q):
    q = list(map(int, input().split()))
    
    if len(q) == 1:
        print(query.pop(-1))
    else:
        query.append(q[1])
        