pnum,qnum=input().split()
pnum,qnum=int(pnum),int(qnum)
def armscheck(znum): 
  tmp=znum
  tsum=0     
  while tmp>0:
    rem=tmp%10 
    tsum=tsum+rem**3 
    tmp=tmp//10  
  if(znum==tsum):
    return 1
  else:
    return -1
for i in range(pnum+1,qnum):
  y=armscheck(i)
  if(y==1):
    print(i,end=" ")
