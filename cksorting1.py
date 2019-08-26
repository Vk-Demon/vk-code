n,k=input().split()      #Given 2 numbers N,K and an array of N integers, find if the element K exists in the array
n,k=int(n),int(k)
lt=[int(i) for i in input().split()]
c=0
for i in range(0,n):
  if(lt[i]==k):
    c=c+1
if(c==1):
  print("yes")
else:
  print("no")
