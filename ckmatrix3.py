rnum,cnum=input().split() # Given 2 numbers N and M followed by a matrix of size N * M.if there is any entry which is 0 change the entire column and row to zero respectively and then print the matrix.
rnum,cnum=int(rnum),int(cnum)
lt=[input().split(" ",cnum) for i in range(rnum)]
slt=[[1 for i in range(cnum)]for j in range(rnum)]
for i in range(rnum):
  for j in range(cnum):
    if(lt[i][j]=='0'):
      row=i
      col=j
      for j in range(cnum):
        slt[row][j]='0'
      for i in range(rnum):
        slt[i][col]='0'
for i in range(rnum):
  for j in range(cnum):
    print(slt[i][j],end=" ")
  print(" ")
