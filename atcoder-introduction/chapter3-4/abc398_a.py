N = int(input())
eq = "="*2 if N % 2 == 0 else "="
hy = (N-len(eq))//2
print("-"*(hy) + eq + "-"*(hy))