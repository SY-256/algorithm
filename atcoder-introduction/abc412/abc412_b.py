S = str(input())
T = str(input())

for i in range(1, len(S)):
    if S[i].isupper() and S[i - 1] not in T:
        exit(print("No"))
print("Yes")
