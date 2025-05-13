s = [char for char in input()]

count = 0
for i, c in enumerate(s):
    if (i + 1) % 2 != 0 and c != "i":
        count += 1
        s.insert(i, "i")
    if (i + 1) % 2 == 0 and c != "o":
        count += 1
        s.insert(i, "o")
if len(s) % 2 != 0:
    count += 1
print(count)
