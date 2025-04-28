N, M = map(int, input().split())

A_list = []
for i in range(N):
    A_list.append(list(map(int, input().split())))
price_sorted = sorted(A_list, key=lambda x:x[0])

total_price = 0

for A_i in price_sorted:
    if (M - A_i[1]) >= 0:
        M -= A_i[1]
        total_price += A_i[1] * A_i[0]
    else:
        total_price += M * A_i[0]
        break
print(total_price)