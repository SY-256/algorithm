N = int(input())
A = list(map(int, input().split()))

ans = "No"
for i in range(2, N):
    if A[i-2]==A[i-1]==A[i]:
        ans = "Yes"
        break
print(ans)