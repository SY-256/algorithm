N, M = map(int, input().split())
S = [c for c in input()]
T = [c for c in input()]

for i in range(M):
    L, R = map(int, input().split())
    L -= 1
    R -= 1

    S_swith = S[max(0, L) : min(N, R) + 1]
    T_swith = T[max(0, L) : min(N, R) + 1]
    S[max(0, L) : min(N, R) + 1] = T_swith
    T[max(0, L) : min(N, R) + 1] = S_swith

print(*S, sep="")
