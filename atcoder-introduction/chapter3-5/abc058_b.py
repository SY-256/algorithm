O = input()
E = input()
ans = ""

for i in range(len(E)):
    ans += (O[i] + E[i])
print(ans) if len(O)-len(E) == 0 else print(ans+O[-1])