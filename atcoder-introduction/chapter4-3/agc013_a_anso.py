N = int(input())
A = list(map(int, input().split()))

res = 0
i = 0
while i < N:
    # 同じ値を抜ける
    while i + 1 < N and A[i] == A[i + 1]:
        i += 1

    # 上昇
    if i + 1 < N and A[i] < A[i + 1]:
        while i + 1 < N and A[i] <= A[i + 1]:
            i += 1

    # 降下
    elif i + 1 < N and A[i] > A[i + 1]:
        while i + 1 < N and A[i] >= A[i + 1]:
            i += 1

    res += 1
    i += 1

print(res)
