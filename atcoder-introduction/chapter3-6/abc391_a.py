table = {
    "N": "S",
    "S": "N",
    "W": "E",
    "E": "W"
}
D = input()
result = ''.join(table.get(c, c) for c in D)
print(result)