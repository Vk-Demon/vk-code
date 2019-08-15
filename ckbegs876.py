cpnum=int(input())
cp=0
for i in range(1,cpnum+1):
  if(cpnum%i==0):
    cp=cp+1
if(cp==2):
  print("no")
else:
  print("yes") 
