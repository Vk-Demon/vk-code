from itertools import permutations   # GIVEN A SET OF NUMBERS OF LENGTH N. YOUR TASK IS TO FIND THE quad ret (x1,x2,x3,x4) which will result the sum in 1. If quad ret exists print yes else print no.
def per(l):
  nt,k=[],0
  perm = permutations(l) 
  for i in list(perm): 
    nt.append(list(i))
    s=0
    for j in range(0,4):
      s=s+i[j]
    if(s==1):
      k=k+1
      break
  if(k>0):
    print("YES")
  else:
    print("No")
tc=int(input())
for t in range(0,tc):
  n=int(input())
  lt=[int(i) for i in input().split()]
  nt=per(lt)
