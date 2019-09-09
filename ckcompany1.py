nnum=int(input()) # Given a number N and an array of N elements, print the number of lucky numbers in the array.Lucky number: N*I is also present in the array then the number is lucky where N is the number of elements in the array and I is the position of the element.(1 based indexing).
ltnum=[int(i) for i in input().split()]
lnc=0
for i in range(0,nnum):
  for j in range(1,nnum+1):
    if(nnum*j==ltnum[i]):
      lnc=lnc+1
print(lnc)
