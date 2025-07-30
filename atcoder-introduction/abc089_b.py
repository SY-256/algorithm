N = int(input())
S = [char for char in input().split(" ")]
print("Four") if len(set(S)) == 4 else print("Three")
