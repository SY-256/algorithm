from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

D_A = defaultdict(int)
D_B = defaultdict(int)
D_C = defaultdict(int)
for i in range(N):
    a = A[i] % 46
    b = B[i] % 46
    c = C[i] % 46

    D_A[a] += 1
    D_B[b] += 1
    D_C[c] += 1

ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + j + k) % 46 == 0:
                ans += D_A[i] * D_B[j] * D_C[k]
print(ans)
