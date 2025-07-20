N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]

result = 0
for A, B in AB:
    if A < B:
        result += 1
print(result)
