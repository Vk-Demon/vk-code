def prime(p):  # Given a number N, How many ways are there to represent it as sum of 2 primes.
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
pt,ct,cs,s,st=[],0,0,0,[]
for i in range(0,nnum):
  p=prime(i)
  if(p==1):
    pt.append(i)
for i in range(len(pt)):
  s=0
  for j in range(len(pt)):
    s=pt[i]+pt[j]
    if(s==nnum and pt[i]!=pt[j]):
      ct=ct+1
    elif(s==nnum and pt[i]==pt[j]):
      cs=cs+1
cw=cs+int(ct/2)
print(cw)
