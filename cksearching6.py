nnum=int(input())
lt,c=[i for i in input().split()],0
for i in range(0,nnum):
  if(lt[i]=='P'):
    c=c+1
if(int(c/nnum*100)<=25):
  print("Blacklisted")
else:
  print("Not Blacklisted")
