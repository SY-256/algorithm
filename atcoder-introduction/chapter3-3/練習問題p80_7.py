a, b, k = map(int, input().split())

for i in range(a, min(a + k, b + 1)):
    print(i)

for i in range(max(a + k, b - k + 1), b + 1):
    print(i)