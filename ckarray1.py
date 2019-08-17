lnum,rnum=input().split()
lnum,rnum=int(lnum),int(rnum)
cps=0
for i in range(lnum,rnum+1):
  for j in range(1,rnum+1):
    if(j*j==i):
      cps=cps+1
print(cps)
