N = int(input())
calc = 1
ans  = 1
for i in range(1, N+1):
    _calc = 0
    if i % 2 == 0:
        j = i / 2
        while True:
            _calc += 1
            if j % 2 != 0 or j / 2 == 0:
                break
            j = j / 2
    if calc <= _calc:
        calc = _calc
        ans = i
print(ans)