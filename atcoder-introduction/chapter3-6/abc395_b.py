N = int(input())
A = list(map(int, input().split()))

ans = 10**6
for i in range(0, N):
    for j in range(i+1, N):
        if A[i] == A[j]:
            index = j - i + 1
            if ans > index:
                ans = index

print(-1) if ans == 10**6 else print(ans)