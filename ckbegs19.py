ntnum,ntk=input().split()
ntnum,ntk=int(ntnum),int(ntk)
ntsum=0
nset=[]
nset = [int(j) for j in input().split()]
for i in range(0,ntk+1):
  ntsum=ntsum+i
print(ntsum)
