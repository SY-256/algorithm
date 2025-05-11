from collections import Counter
import math

N = int(input())
A = sorted(list(map(int, input().split())))

total = math.comb(N, 2)
num = Counter(A)
diff = sum(n * (n - 1) // 2 for n in num.values())
print(total - diff)
