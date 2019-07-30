nt=int(input())
c=0
for i in range(1,nt):
  if((2**i)==nt):
    c=c+1
if(c==0):
  print("no")
else:
  print("yes")
