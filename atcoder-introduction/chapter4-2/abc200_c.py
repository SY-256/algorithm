from collections import Counter

N = int(input())
A = list(map(int, input().split()))
A_div = [n % 200 for n in A]
count = Counter(A_div)
print(sum(n * (n - 1) // 2 for n in count.values() if n != 1))
