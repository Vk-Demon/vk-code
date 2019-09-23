rn,cn=input().split()  # You are given two numbers ‘n’ and ‘m’, denoting the size of matrix made up of only 1’s and 0’s. Your task is to calculate the maximum one’s in single row.
rn,cn,mt=int(rn),int(cn),[]
lt=[int(i) for i in input().split()]
st=[lt[i*cn:(i+1)*cn]for i in range((len(lt)+cn- 1)//cn)]
for i in range(rn):
  c=0
  for j in range(cn):
    if(st[i][j]==1):
      c=c+1
  mt.append(c)
print(max(mt))
