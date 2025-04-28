s = list(input())
t = list(input())
s_dash = ""
t_dash = ""
for i in sorted(s):
    s_dash += i
for i in sorted(t, reverse=True):
    t_dash += i
ans = sorted([s_dash, t_dash])
print("Yes") if ans[0]==s_dash and ans[0]!=t_dash else print("No")