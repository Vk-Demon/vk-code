def primefact(n):  # Given a number N, print its prime factors in sorted order.
  lt=[]
  for i in range(2,n+1):
    if(n%i==0):
      cp=1
      for j in range(2,(i//2+1)):
        if(i%j==0):
          cp=0
          break
      if(cp==1):
        lt.append(i)
  return(lt)
nnum=int(input())
ltnum=primefact(nnum)
for i in ltnum:
  print(i,end=" ")
