R, X = map(int, input().split())
r1 = 1 if 1600 <= R <= 2999 else 0
r2 = 2 if 1200 <= R <= 2399 else 0
print("Yes") if X == r1 or X == r2 else print("No")
