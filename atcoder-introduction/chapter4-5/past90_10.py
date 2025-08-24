N = int(input())
A = [0 for _ in range(N + 1)]
B = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    c, p = map(int, input().split())

    if c == 1:
        A[i] = A[i - 1] + p
        B[i] = B[i - 1]
    else:
        B[i] = B[i - 1] + p
        A[i] = A[i - 1]

print(A)
print(B)
Q = int(input())
for i in range(Q):
    lq, rq = map(int, input().split())
    print(A[rq] - A[lq - 1], B[rq] - B[lq - 1])
