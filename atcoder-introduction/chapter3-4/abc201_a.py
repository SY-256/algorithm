a = sorted(list(map(int, input().split())))
print("Yes") if (a[2]-a[1]) == (a[1]-a[0]) else print("No")