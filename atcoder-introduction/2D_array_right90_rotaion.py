### 2次元配列で右に90°回転するサンプル
### ⇒上下逆転（S[::-1]）してから、転置（zip(*S[::-1])）する
N = int(input())
S = [input() for _ in range(N)]
for x in zip(*S[::-1]):
    print(*x, sep="")
