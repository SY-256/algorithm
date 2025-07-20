N = int(input())
A = list(map(int, input().split()))

print(sum([v for i, v in enumerate(A) if (i + 1) % 2 == 1]))
