s = list(input())
t = list(input())
if s == t:
    exit(print("Yes"))

for i in range(len(t)-1):
    t[i],t[i+1] = t[i+1],t[i]
    if s == t:
        exit(print("Yes"))
    t[i],t[i+1] = t[i+1],t[i] # 戻す
print("No")