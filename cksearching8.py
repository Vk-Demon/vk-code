rnum,cnum=input().split()  # The prison warden at Central jail is given a tip-off that a prison inmate is planning an escape. The warden suspects a particular prisoner of planning an escape and wants to find out if he/she is present in his/her cell. The layout of the prison is modelled in a matrix with every cell of the matrix representing a prison cell. The matrix is filled with the prisoner ids at the corresponding cells. Find out whether the person the warden suspects is present in the prison or not.
rnum,cnum,idx=int(rnum),int(cnum),0
prsn=list(map(int,input().split()))
sid=int(input())
for i in range(len(prsn)):
  if(int(prsn[i])==sid):
    idx=1
if(idx==0):
  print("No")
else:
  print("Yes")
