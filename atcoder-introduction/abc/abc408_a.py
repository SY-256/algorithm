N, S = map(int, input().split())
T = list(map(int, input().split()))
T = [0] + T

for i in range(len(T) - 1):
    if T[i + 1] - T[i] >= S + 0.5:
        exit(print("No"))
print("Yes")
