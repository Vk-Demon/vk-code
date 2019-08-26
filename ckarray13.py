n=int(input())     # Given an array of numbers switch(swap) the adjacent characters
lt=[int(i) for i in input().split()]
lt1,lt2=[],[]
for i in range(0,n):
  if(i%2==0):
    lt1.append(lt[i])
  else:
    lt2.append(lt[i])
if(n%2==0):
  for i in range(0,int(n/2)):
    print(lt2[i],lt1[i],end=" ")
else:
  for i in range(0,int(n/2)):
    print(lt2[i],lt1[i],end=" ")
  print(lt[n-1],end="")
