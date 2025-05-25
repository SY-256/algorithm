s = input()
chars = set(s)

if len(chars) == 1:
    exit(print(0))

res = 100
for key in chars:
    str_current = s
    flag = True  # すべての文字が同じでない場合: True
    times = 1  # 必ず一回は縮める

    while flag:
        vacant = ""
        flag = False
        for i in range(len(str_current) - 1):
            # shrink
            if str_current[i] == key or str_current[i + 1] == key:
                vacant += key
            else:
                vacant += str_current[i]
                flag = True  # 異なる文字が交じってしまったらループは続く

        if flag:
            # 1回の操作後、違う文字が混じっていた場合
            str_current = vacant
            times += 1

    res = min(res, times)

print(res)
