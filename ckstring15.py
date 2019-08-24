def strcmp(a,b):                   # Given 2 strings and a number K, check whether they differ by exactly K characters
  f,c=len(a),0
  for i in range(0,f):
    if(a[i]==b[i]):
      c=c+1
  return f-c
fstr,lstr,n=input().split()
n=int(n)
m=strcmp(fstr,lstr)
if(n==m):
  print("yes")
else:
  print("no")
