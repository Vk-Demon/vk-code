nnum,knum=input().split()
nnum,knum=int(nnum),int(knum)
ary=[int(i) for i in input().split()]
rpc=0
for i in range(0,nnum):
  if(knum==ary[i]):
    rpc=rpc+1
print(rpc) 
