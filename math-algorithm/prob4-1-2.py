N = int(input())
x = [0 for _ in range(N)]
y = [0 for _ in range(N)]
for i in range(N):
    x[i], y[i] = map(int, input().split())

# 全探索
Answer = 10000000.0
for i in range(N):
    for j in range(i + 1, N):
        dist = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5
        Answer = min(Answer, dist)

print(Answer)
