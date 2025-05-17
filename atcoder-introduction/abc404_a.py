import string

alphabet = list(string.ascii_lowercase)
S = input()
for i in alphabet:
    if i not in S:
        exit(print(i))
