A, B, W = map(int, input().split())
W *= 1000

m = 1e9
M = 0
for n in range(1, 1000000 + 1):
    if A * n <= W <= B * n:
        m = min(m, n)
        M = max(M, n)

print(m, M) if M != 0 else print("UNSATISFIABLE")
