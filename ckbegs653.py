rnum=int(input())
ssum=0
while(rnum>0):
  rem=rnum%10
  ssum=ssum+rem
  rnum=rnum//10
print(ssum)
