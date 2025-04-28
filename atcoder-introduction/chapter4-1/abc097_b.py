X = int(input())
exps = [v for v in range(2, 10)]

ans = [1]
for i in range(2, X+1):
    for exp in exps:
        if pow(i, exp) <= X:
            ans.append(pow(i, exp))
        else:
            break
print(max(ans))