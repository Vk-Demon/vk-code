nnum=int(input())      # Given a number N and an array of N integers, find the Bitwise XOR of the array
lnum=[int(i) for i in input().split()]
for i in range(0,nnum-1):
  s=lnum[i]^lnum[i+1]
print(s)
