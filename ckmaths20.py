nqnum=int(input()) # Given a number N, check if N is divisible by any number less than N other than 1.
c=0
for i in range(2,nqnum):
  if(nqnum%i==0):
    c=c+1
if(c>0):
  print("yes")
else:
  print("no")
