nnum=int(input())  # You are provided with an array in which all elements are repeated thrice except one which is repeated twice.Your task is to print that number.
lte=[int(i) for i in input().split()]
for i in range(0,nnum):
  cq=0
  for j in range(0,nnum):
    if(lte[i]==lte[j]):
      cq=cq+1
  if not(cq==3):
    print(lte[i])
    break
