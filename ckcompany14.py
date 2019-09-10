def prime(p): # Given a number N, find the sum of prime numbers that end with 3 from 2 to N.
  cp=0
  p=int(p)
  for i in range(1,p+1):
    if(p%i==0):
      cp=cp+1
  if(cp==2):
    return 1
  else:
    return 0
nnum=int(input())
s,st="",0
for i in range(2+1,nnum):
  p=prime(i)
  if(p==1):
    s=str(i)
    if(s[len(s)-1]=='3'):
      st=st+int(s)
print(st)
