ntnum,ntk=input().split()
ntnum,ntk=int(ntnum),int(ntk)
ntsum=0
nset=[]
for j in range(0,ntnum):
  nset.append(input())
for i in range(0,ntk+1):
  ntsum=ntsum+i
print(ntsum)
