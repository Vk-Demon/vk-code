nnum=int(input())           # Given a number N, print the odd factors of the number
for i in range(1,nnum+1):
  k=nnum%i
  if(k==0 and i%2==1):
    print(i,end=" ")
