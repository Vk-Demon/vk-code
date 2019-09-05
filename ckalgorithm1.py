nnum=int(input())  # Given a number N followed by an array of N integers, every element appears twice except for one. Find that single one and print it.
lt=[int(i) for i in input().split()]
for i in range(0,nnum):
  cq=0
  for j in range(0,nnum):
    if(lt[i]==lt[j]):
      cq=cq+1
  if(cq==1):
    print(lt[i])
