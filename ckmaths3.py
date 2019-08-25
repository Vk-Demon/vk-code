nnum=input()                  # Given a number N, print the odd digits in the number(space seperated)
for i in range(0,len(nnum)):
  if(int(nnum[i])%2==1):
    print(nnum[i],end=" ")
