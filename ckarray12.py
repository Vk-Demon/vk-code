nnum=int(input())       # Given a number N followed by N numbers. Find the smallest number and largest number and print both the indices(1 based indexing)
ltnum=[int(i) for i in input().split()]
a,b=min(ltnum),max(ltnum)
for i in range(0,nnum):
  if(ltnum[i]==a):
    k=i+1
  elif(ltnum[i]==b):
    l=i+1
print(k,l)
