nnum=int(input())
lnum,rnum=input().split()
lnum,rnum=int(lnum),int(rnum)
cn=0
for i in range(lnum+1,rnum):
  if(i==nnum):
    cn=cn+1
if(cn==1):
  print("yes")
else:
  print("no")
