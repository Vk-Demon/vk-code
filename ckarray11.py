n=int(input())       # Given an array of numbers which contains all even numbers except one, or all odd numbers except one. Find the different number
l=[int(i) for i in input().split()]
c=0
for i in range(0,n):
  if(l[i]%2==0):
    c=c+1
  else:
    k=l[i]
if(c==1):
  c=0
  for i in range(0,n):
    if(l[i]%2==1):
      c=c+1
    else:
      k=l[i]
print(k)
