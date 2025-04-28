import string
N = int(input())
S = input()
alphabet = [chr(ord("A")+i) for i in range(26)]
ans = ""
for s in S:
    indx = alphabet.index(s)
    calc_indx = indx + N
    if calc_indx > 25:
        calc_indx = (indx + N - 1) - 25
    ans += alphabet[calc_indx]
print(ans)
