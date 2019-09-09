nnum=int(input()) # Given a number N followed by an array of N integers, replace every element with the greatest element on the right side(to that element) in the array. Replace last element with 0 as there no element on the right side of it.
lt=[int(i) for i in input().split()]
k=0
lt[0]=max(lt)
for i in range(1,nnum-1):
  max=lt[i+1]
  for j in range(i+1,nnum):
    if(lt[j]>max):
      max=lt[j]
    lt[i]=max
lt[len(lt)-1]=0
for i in lt:
  print(i,end=" ")
