S = input()
T = input()

ans = "No"
for i in range(len(S)):
    W = ""
    for j in range(len(S)):
        W += S[-1+j]
    if W == T:
        ans = "Yes"
        break
    S = W
print(ans)