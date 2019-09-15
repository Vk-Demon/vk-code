nnum=int(input())  # Count the number of digits of a given number N.Size of the integer ranges from 1.
ct=0
while(nnum>0):
  rt=nnum%10
  nnum=nnum//10
  ct=ct+1
print(ct)
