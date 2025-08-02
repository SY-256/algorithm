N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


for v in B:
    if v in A:
        A.remove(v)

print("") if len(A) == 0 else print(*A, sep=" ")
