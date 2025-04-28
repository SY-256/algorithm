r, g, b =   map(str, input().split())
print("YES") if int(r+g+b)%4 == 0 else print("NO")