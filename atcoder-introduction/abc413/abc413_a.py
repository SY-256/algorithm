N, M = map(int, input().split())
A = list(map(int, input().split()))
print("Yes") if sum(A) <= M else print("No")
