s = list(input())
t = list(input())

sp = sorted(s)
tp = sorted(t, reverse=True)

if sp < tp:
    print("Yes")
else:
    print("No")