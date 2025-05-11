N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# A_div = [n % 46 for n in A]
# B_div = [n % 46 for n in B]
C_div = [n % 46 for n in C]

AB = []
for i in range(N):
    for j in range(N):
        AB.append(46 - (A[i] + B[j]) % 46)

ans = 0
for v in AB:
    ans += C_div.count(v)

print(ans)
