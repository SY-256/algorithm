N, C = map(int, input().split())
T = list(map(int, input().split()))
get_time = [T[0]]

ans = 1
for i in range(1, N):
    if T[i] - get_time[-1] >= C:
        get_time.append(T[i])
        ans += 1
print(ans)
