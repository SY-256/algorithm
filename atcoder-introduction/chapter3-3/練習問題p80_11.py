k = int(input())
a, b = map(int, input().split())

a_k = 0
b_k = 0
for i in range(0, len(str(a))):
    a_k += int(str(a)[::-1][i]) * pow(k, i)

for i in range(0, len(str(b))):
    b_k += int(str(b)[::-1][i]) * pow(k, i)

print(a_k * b_k)