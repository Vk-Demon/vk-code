nnum,knum=input().split()  # Given 2 numbers N and K followed by N numbers find if there exists a pair of numbers such that it adds upto K.
nnum,knum=int(nnum),int(knum)
lt=[int(i) for i in input().split()]
c=0
for i in range(0,nnum-1):
  for j in range(i+1,nnum):
    if(lt[i]+lt[j]==knum):
      c=c+1
if(c>0):
  print("yes")
else:
  print("no")

