pstr=input()
l=int(len(pstr)/2)
lt=len(pstr)-1
cp=0
for i in range(0,l):
  if(pstr[i]==pstr[lt]):
    cp=cp+1
    lt=lt-1
if(cp==l):
  print("yes")
else:
  print("no")
