def sq(m):  # Given a number N, print the sum of the squares of its digits.
  return m*m
nnum=int(input())
st=0
while(nnum>0):
  rt=nnum%10
  st=st+sq(rt)
  nnum=nnum//10
print(st)
