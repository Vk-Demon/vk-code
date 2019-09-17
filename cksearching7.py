nstd,rmrk=input().split()  # Ramesh is a studious student and wants to find out if there is any other student in his class who has got the same marks as his, in maths. Help him find out.
nstd,rmrk,idx=int(nstd),int(rmrk),0
amrk=[int(i) for i in input().split()]
for i in range(0,nstd):
  if(amrk[i]==rmrk):
    idx=i
if(idx>0):
  print(idx)
else:
  print("-1")
