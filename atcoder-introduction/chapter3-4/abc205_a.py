A, B = map(int, input().split())
print((B / 100) * A if B % 100 !=0 else (B // 100) * A)