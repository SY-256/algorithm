N = int(input())
A = list(map(int, input().split()))

A_tp = pow(sum(A), 2)
A_cp = sum([pow(n, 2) for n in A])
print((A_tp - A_cp) // 2)
