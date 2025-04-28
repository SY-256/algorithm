N = int(input())
S = str(input())

patrn = len(list(set(S)))
if patrn == 1:
    exit(print(patrn))

ans = 0
for i in range(0, N):
    count = 0

    X = sorted(list(set(S[:i])))
    Y = sorted(list(set(S[i:])))
    
    for j in X:
        if j in Y:
            count += 1
    
    if count > ans:
        ans = count
    
    if ans == patrn:
        break

print(ans)