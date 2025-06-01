from collections import defaultdict

N, M = map(int, input().split())
d = defaultdict(int)

for i in range(M):
    L, R = map(int, input().split())
    for j in range(L, R + 1):
        d[j] += 1

d_values = d.values()
print(0) if len(d_values) < N else print(min(d_values))


### memo
""""
2次元配列で持たせて、列方向にSUMとって最小値求めるとか？
⇒2次元配列を作る部分でTLEになるのでどうにかする必要ある
⇒過去に2次元配列で処理している問題あるので参考にする

def get_column_mins(matrix):
二次元配列の各列の最小値を返す
    return [min(column) for column in zip(*matrix)]

# 使用例
data = [
    [10, 20, 30],
    [5, 15, 25],
    [8, 12, 18]
]

result = get_column_mins(data)
print(result)  # [5, 12, 18]
"""
