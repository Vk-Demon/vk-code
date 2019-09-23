def prime(p):  # Mr. Prime is a coder who loves solving problems which involve the mention of the word ‘prime’. He recently came across a puzzle in which he had to find sum of elements which are located at positions whose row+column index value is a prime number. After finding the sum, he had to check whether the sum obtained is a prime number or not. Assume that you are Mr. Prime and are given a matrix of arbitrary dimensions. Check whether the sum of elements located at prime indices is a prime number.
  cp=0
  for i in range(1,p+1):
    if(p%i==0):
     cp=cp+1
  if(cp==2):
    return 1
  else:
    return 0  
rn,cn=input().split()
rn,cn=int(rn),int(cn)
lt,s=[input().split() for i in range(rn)],0
for i in range(rn):
  for j in range(cn):
    if(prime(i+j)==1):
      s=s+int(lt[i][j])
if(prime(s)==1):
  print("YES")
else:
  print("NO")
