lt=[i for i in input().split()]
for i in range(0,len(lt)):
  if(lt[i]=='and'):
    t=lt[i-1]
    lt[i-1]=lt[i+1]
    lt[i+1]=t
for i in lt:
  print(i,end=" ")
