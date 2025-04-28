A, B, C = map(int, input().split())
if A == B == C:
    exit(print("Yes"))
elif (A + B) == C or (A + C) == B or (B + C) == A:
    exit(print("Yes"))
else:
    print("No")
