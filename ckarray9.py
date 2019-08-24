nnum=int(input())    # Given a number N followed by N numbers if there is a number '0' occuring print all the numbers given before 0 till the previous 0
knum=input() 
s,c,k="",0,0
for i in range(0,nnum):
  if not(int(knum[i])==0):
    s=s+knum[i]
    k=k+1
  else:
    c=i+1
l=k-(nnum-c)
for i in range(0,l):
  print(s[i],end=" ")
