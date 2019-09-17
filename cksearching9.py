def ksmall(l,k): # Given an array arr[] and a number K where K is smaller than the size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are NOT distinct.
  l=list(set(l))
  l=sorted(l)
  if(k<len(l)+1):
    return l[k-1]
  else:
    return l[len(l)-1]
nnum=int(input()) 
ks=[]
for i in range(0,nnum):
  n=int(input())
  lt=[int(i) for i in input().split()]
  k=int(input())
  ks.append(ksmall(lt,k))
for i in ks:
  print(i)
