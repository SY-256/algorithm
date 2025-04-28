N, M = map(int, input().split())
B = list(map(int, input().split()))
W = list(map(int, input().split()))

ans_1 = 0
ans_2 = 0
B_sorted = sorted(B, reverse=True)
W_sorted = sorted(W, reverse=True)

for i in range(min(N, M)): 
    if (B_sorted[i] + W_sorted[i]) > 0:
        ans_1 += B_sorted[i] + W_sorted[i]
    else:
        break

count = 0
if B_sorted[0] > 0:
    for i in range(N):
        if B_sorted[i] > 0:
            ans_2 += B_sorted[i]
        else:
            break
        count += 1

if W_sorted[0] > 0:
    for i in range(M):
        if W_sorted[i] > 0 and i+1 <= count:
            ans_2 += W_sorted[i]
        else:
            break

print(max(ans_1, ans_2))