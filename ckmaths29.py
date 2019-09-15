nnum=int(input())  # Given a number N,print the reverse of the number N.
st=0
while(nnum>0):
  rt=nnum%10
  st=st*10+rt
  nnum=nnum//10
print(st)
