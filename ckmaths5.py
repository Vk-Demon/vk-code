def reverse(n):     # count all palindromic numbers present in that range
  r=0
  while(n>0):
    d=n%10
    r=r*10+d
    n=n//10
  return r
nnum=int(input())
c=0
for i in range(1,nnum+1):
  if(i==reverse(i)):
    c=c+1
print(c)
