nnum=int(input())  # You are given with a number ‘n’. You have to count the pair of two numbers a and b such that sum of two numbers are equal to n.
cn=0
for i in range(0,nnum):
  for j in range(1,nnum):
    if(i+j==nnum):
      cn=cn+1
print(cn)
