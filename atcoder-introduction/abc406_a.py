ABCD = list(map(int, input().split()))
print("Yes") if ABCD[0] > ABCD[2] else (
    print("Yes") if ABCD[0] == ABCD[2] and ABCD[1] > ABCD[3] else print("No")
)
