A = list(map(int, input().split()))
indx = []
for i, v in enumerate(A):
  if i+1 != v:
    indx.append(i)
print("Yes") if len(indx)==2 and (indx[1] - indx[0])==1  else print("No")