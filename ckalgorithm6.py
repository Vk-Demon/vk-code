nnum=int(input())    # Given a number N and an array of N integers, sort the array in increasing order and print the original indices of the elements present in sorted array.   
lt=[int(i) for i in input().split()]
ilt=[i+1 for i in range(0,nnum)]
for i in range(0,nnum-1):
  for j in range(i+1,nnum):
    if(lt[i]>lt[j]):
      t,t1=lt[i],ilt[i]
      lt[i],ilt[i]=lt[j],ilt[j]
      lt[j],ilt[j]=t,t1 
for i in ilt:
  print(i,end=" ")  
