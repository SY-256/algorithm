N, D = map(int, input().split())
X = list(map(int, input().split()))

ans_list = [0]
for i, v in enumerate(X):
    ans_list.append(ans_list[i] + v)
ans = len([i for i in ans_list if i<=D])
print(ans)