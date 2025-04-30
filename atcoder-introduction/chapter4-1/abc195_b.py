A, B, W = map(int, input().split())
W *= 1000

max = W // A
min = (W + B - 1) // B
if min <= max:
    print(min, max)
else:
    print("UNSATISFIABLE")
