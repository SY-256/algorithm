s = list(input())
t = list(input())

if s == t:
    exit(print("Yes"))

for i in range(len(s)-1):
    t[i], t[i+1] = t[i+1], t[i]
    if s == t:
        exit(print("Yes"))
    t[i], t[i+1] = t[i+1], t[i]

print("No")