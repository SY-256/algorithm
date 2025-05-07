### 連想配列使う方法
N = int(input())

# バスケットのサイズ
M = 101

# バスケット
exist = [0] * M

for i in range(N):
    d = int(input())

    # バスケット更新
    exist[d] = 1

# existの総和を求める
print(sum(exist))
