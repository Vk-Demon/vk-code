xnum,ynum=input().split()
xnum,ynum=int(xnum),int(ynum)
pnum=xnum*ynum
s=0
for i in range(0,pnum+1):
  q=i*i
  if(q==pnum):
    s=s+1
if(s==1):
  print("yes")
else:
  print("no")
