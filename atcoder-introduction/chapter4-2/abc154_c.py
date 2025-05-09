N = int(input())
A = list(set(list(map(int, input().split()))))
print("YES") if len(A) == N else print("NO")
