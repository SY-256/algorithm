N, X = map(int, input().split())

m_list = []
ans = 0
for i in range(N):
    m = int(input())
    X -= m
    if X>= 0:
        ans += 1
    m_list.append(m)

m_min = min(m_list)

while X >= 0:
    X -= m_min
    if X >= 0:
        ans += 1
print(ans)