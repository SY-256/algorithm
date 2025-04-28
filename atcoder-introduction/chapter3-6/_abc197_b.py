h,w,x,y=map(int,input().split())
x-=1
y-=1

x,y=y,x
a=[input() for _ in range(h)]
#print(a)

ans=0
for i in range(y-1,-1,-1):
  if a[i][x]=="#":
    break
  else:
    ans+=1

for i in range(y+1,h):
  if a[i][x]=="#":
    break
  else:
    ans+=1

for j in range(x+1,w):
  if a[y][j]=="#":
    break
  else:
    ans+=1

for j in range(x,-1,-1):
  if a[y][j]=="#":
    break
  else:
    ans+=1

print(ans)