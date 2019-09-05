nnum=int(input())         # Alternate sorting: Given a number N and followed by N numbers, sort the array in such a way that the first number is first maximum and second number is 1st minimum 3rd number is 2nd maximumand so on.
lt=[int(i) for i in input().split()]
for i in range(0,nnum-1):
  for j in range(i+1,nnum):
    if(lt[i]>lt[j]):
      t=lt[i]
      lt[i]=lt[j]
      lt[j]=t
dlt=list(reversed(lt))
j=0
for i in range(0,nnum):
  if(i%2==0):
    print(dlt[j],end=" ")
  else:
    print(lt[j],end=" ")
    j=j+1
