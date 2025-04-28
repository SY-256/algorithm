A, B = map(int, input().split())
S = input()

print("Yes") if S[A] == "-" and S[:A].isdecimal() and S[A+1:].isdecimal() else print("No")