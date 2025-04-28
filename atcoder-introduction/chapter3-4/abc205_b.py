N = int(input())
A = list(map(int, input().split()))

n_list = [1 for n in range(1, N+1) if n in A]
print("Yes" if len(n_list)==N else "No")