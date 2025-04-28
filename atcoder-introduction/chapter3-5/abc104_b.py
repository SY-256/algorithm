s = input()
ans = "WA"
count = 0
break_check_flag = False
if s[0]=="A" and s[-1].islower() and s[1].islower():
    for c in s[2:len(s)-1]:
        if c == "C":
            count += 1
        elif c.islower():
            continue
        else:
            break_check_flag = True
            break
    if not break_check_flag and count == 1:
        ans = "AC"
print(ans)