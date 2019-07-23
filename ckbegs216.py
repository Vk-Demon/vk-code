pnum,qnum=input().split()
pnum,qnum=int(pnum),int(qnum)
def primecheck(prnum):
  cp=0
  for i in range(1,prnum+1):
    if(prnum%i==0):
      cp=cp+1
  if(cp==2):
    return 1
  else:
    return -1
for i in range(pnum+1,qnum):
  l=primecheck(i)
  if(l==1):
    print(i,end=" ")
