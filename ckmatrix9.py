rn,cn=input().split()  # Rohan is given a matrix with 1’s and 0’s. His task is to calculate the maximum possible rectangular area formed by 1’s. He has gone really confused after seeing this problem.Your task is to develop an algorithm for him.
rn,cn,mt=int(rn),int(cn),[]
lt=[int(i) for i in input().split()]
st,s=[lt[i*cn:(i+1)*cn]for i in range((len(lt)+cn- 1)//cn)],0
for i in range(rn):
  for j in range(cn):
    if(st[i][j]==0):
      if(s%rn==0):
        mt.append(s)
      s=0
    else:
      s=s+1
  mt.append(s)
print(max(mt))
