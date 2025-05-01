abcd = str(input())
operator = ["+", "-"]

for op1 in operator:
    for op2 in operator:
        for op3 in operator:
            ans = abcd[0] + op1 + abcd[1] + op2 + abcd[2] + op3 + abcd[3]
            if eval(ans) == 7:
                ans = ans + "=7"
                exit(print(ans))
