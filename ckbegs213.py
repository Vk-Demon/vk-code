prnum=int(input())
cp=0
for i in range(1,prnum+1):
  if(prnum%i==0):
    cp=cp+1
if(cp==2):
  print("yes")
else:
  print("no")  
