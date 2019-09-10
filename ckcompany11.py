nnum=int(input())  # Given a number N and a 2D matrix(N*N filled with 1's or 0's), find the number of island 1's(An island 1 is a 1 surrounded by 0's on all sides).
lt=[input().split(" ",nnum) for i in range(nnum)]
c=0
for i in range(nnum):
  for j in range(nnum):
    if(lt[i][j]=='1'):
      c=c+1
print(c)
