nnum,knum=input().split()    # Given 2 numbers N,K check if N is a power of K
nnum,knum=int(nnum),int(knum)
cp=0
for i in range(0,int(nnum*0.5)):
  if((knum**i)==nnum):
    cp=cp+1
if(cp>0):
  print("yes")
else:
  print("no")
