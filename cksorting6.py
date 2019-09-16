nnum,knum=input().split()  # ahir gets into an elevator. The elevator is programmed such that it moves up the number of floors mentioned at odd indexes of an array A[] and moves down the number of floors mentioned at even indexes of the array A[], in sequence. Sort the array such that when Tahir gets out of the elevator, he is at any floor other than the floor at which he got into the elevator. The index of the ground floor is 1 and assume that the building has 100 floors. The lift can move only up to the ground floor(i.e) floor indexes are positive integers.
nnum,knum=int(nnum),int(knum)
lt,et=[int(i) for i in input().split()],[]
for i in range(0,nnum):
  if(lt[i]<=knum):
    et.append(lt[i])
et=sorted(et)
if(len(et)>0):
  for i in et:
    print(i,end=" ")
else:
  print("Not possible")
