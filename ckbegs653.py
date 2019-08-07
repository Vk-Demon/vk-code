rmnum=int(input())
ssum=0
while(rmnum>0):
  rem=rmnum%10
  ssum=ssum+rem
  rmnum=rmnum//10
print(ssum)
