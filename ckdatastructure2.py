def nearest(l1,k):  # Given two numbers N,K and an array of size N, print the three nearest neighbours of K(nearest neighbours are numbers which have least difference with K)
  l2,c=[],0
  for i in range(0,len(l1)):
    n=(max(k,l1[i]) - min(k,l1[i]))
    l2.append(n)
  for i in range(0,len(l2)):                 
    t,t1=l2[i],l1[i]
    j=i-1
    while(t<l2[j] and j>=0):
      l2[j+1]=l2[j]
      l1[j+1]=l1[j]
      j=j-1
    l2[j+1]=t
    l1[j+1]=t1
  for i in range(0,len(l1)):
    if(c==3):
      break
    if not(l1[i]==k):
      c=c+1
      print(l1[i],end=" ")      
n,k=input().split()
n,k=int(n),int(k)
lt=[int(i) for i in input().split()]
nearest(lt,k)
