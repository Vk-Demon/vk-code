nnum,knum=input().split() # Given a number N followed by an unsorted array of N numbers and a number K, find if there exists a pair of elements in the array whose difference is K. Return count of such pairs.
nnum,knum=int(nnum),int(knum)
lt=[int(i) for i in input().split()]
cd=0
for i in range(0,nnum):
  for j in range(0,nnum):
    if(max(lt[i],lt[j])-min(lt[i],lt[j])==knum):
      cd=cd+1
print(int(cd/2))
