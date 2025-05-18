N = int(input())
A = list(map(int, input().split()))
result = 1
delta = 0
for i in range(N - 1):
    if A[i] < A[i + 1]:
        ndelta = 1
    elif A[i] > A[i + 1]:
        ndelta = -1
    else:
        ndelta = 0
    if delta and ndelta and ndelta != delta:
        result += 1
        delta = 0
    elif not delta:
        delta = ndelta
print(result)
