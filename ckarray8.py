nnum,knum=input().split()            # Given 2 numbers N and K followed by n numbers print the number of repetitions of K
nnum,knum,c=int(nnum),int(knum),0
l=[int(i) for i in input().split()]
for i in range(0,nnum):
  if(l[i]==knum):
    c=c+1
print(c)
