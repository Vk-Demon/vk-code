nnum=int(input())        # Given a number N, print the even factors of the number.
for i in range(2,nnum+1):
  s=nnum%i
  if(s==0 and i%2==0):
    print(i,end=" ")
