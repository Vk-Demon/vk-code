nnum,dnum=input().split() # Given a number N followed by an array of N numbers. Another number D is given. Rotate the array D times and print the array.
nnum,dnum=int(nnum),int(dnum)
lt=[int(i) for i in input().split()]
qt=[]
for i in range(0,nnum):
  if(dnum==nnum):
    dnum=0
    qt.append(lt[dnum])
    dnum+=1
  else:
    qt.append(lt[dnum])
    dnum+=1
for i in qt:
  print(i,end=" ")
