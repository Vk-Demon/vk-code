nnum=int(input())  # Given a square matrix of size N x N, find the product of the sum of diagonals.
lt=[input().split(" ",nnum) for i in range(nnum)]
for i in range(nnum):
  for j in range(nnum):
    d=(int(lt[0][0])+int(lt[1][1]))*(int(lt[0][1])+int(lt[1][0]))
print(d)
