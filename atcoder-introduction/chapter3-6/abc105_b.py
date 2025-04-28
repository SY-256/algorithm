N = int(input())
for i in range(0, N+1):
    for j in range(0, N+1):
        if N == (4 * i + 7 * j):
            exit(print("Yes"))
print("No")