nnum=int(input())      # Given a number N and an array of N integers, find the Bitwise AND of the array
lnum=[int(i) for i in input().split()]
s=1
for i in range(0,nnum):
  s=s&lnum[i]
print(s)
