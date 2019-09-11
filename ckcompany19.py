def asort(l,k): # Given an array N, sort it in ascending order till it reaches kth elements and after that sort it in descending order.
  for i in range(0,k):
    for j in range(0,k):
      if(l[i]<l[j]):
        t=l[i]
        l[i]=l[j]
        l[j]=t
  return l
def dsort(l,k):
  for i in range(k,len(l)):
    for j in range(k,len(l)):
      if(l[i]>l[j]):
        t=l[i]
        l[i]=l[j]
        l[j]=t
  return l
nnum,knum=input().split()
nnum,knum=int(nnum),int(knum)
lt=[int(i) for i in input().split()]
asort(lt,knum)
dsort(lt,knum)
for i in lt:
  print(i,end=" ")
  
