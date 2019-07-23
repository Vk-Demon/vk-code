pnum,qnum=input().split()
pnum,qnum=int(pnum),int(qnum)
for i in range(pnum+1,qnum):
  if(i%2==1):
    print(i,end=" ")
