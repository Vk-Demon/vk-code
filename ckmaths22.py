npnum=int(input()) # Given a number N, check whether it is a power of 2.
c=0
for i in range(1,int(npnum*0.5)):
  if(2**i==npnum):
    c=1
if(c==1):
  print("yes")
else:
  print("no")
