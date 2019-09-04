nnum=int(input())  # Given a number N and an array of N integers, print the prefix sum array
list=[int(i) for i in input().split()]
st=0
for j in range(0,nnum):
  st=st+list[j]
  print(st,end=" ")
  
