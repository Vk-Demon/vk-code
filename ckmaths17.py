def ncatalan(n): # Given a number N, print the first N Catalan numbers
  if(n<=1):
    return 1
  ncn=0
  for i in range(n):
    ncn += ncatalan(i) * ncatalan(n-i-1)
  return ncn
nnum=int(input())
for n in range(0,nnum+1):
    print(ncatalan(n),end=" ")
